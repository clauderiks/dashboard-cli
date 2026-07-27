"""
Unit tests for the Fortify AST Scan GitHub Actions workflow
(.github/workflows/fortify.yml).

These tests validate the structure and configuration of the workflow file
introduced in this PR: correct triggers, job/permission configuration,
pinned action references, and environment variable wiring for both the
Fortify on Demand (FoD) and Software Security Center (SSC)/ScanCentral
integration paths.

Note: PyYAML follows the YAML 1.1 spec, which resolves the unquoted
top-level key "on" to the boolean `True`. This is a well known quirk when
parsing GitHub Actions workflow files with a generic YAML parser, so the
tests below read the trigger block via the boolean key rather than the
string "on".
"""

import re
from pathlib import Path

import pytest
import yaml

WORKFLOW_PATH = (
    Path(__file__).resolve().parent.parent
    / ".github"
    / "workflows"
    / "fortify.yml"
)


@pytest.fixture(scope="module")
def workflow_text():
    return WORKFLOW_PATH.read_text()


@pytest.fixture(scope="module")
def workflow(workflow_text):
    return yaml.safe_load(workflow_text)


@pytest.fixture(scope="module")
def triggers(workflow):
    # PyYAML parses the unquoted "on:" key as the boolean True (YAML 1.1).
    assert True in workflow, "Expected trigger block parsed under boolean key `on`"
    return workflow[True]


@pytest.fixture(scope="module")
def job(workflow):
    jobs = workflow["jobs"]
    assert "Fortify-AST-Scan" in jobs
    return jobs["Fortify-AST-Scan"]


@pytest.fixture(scope="module")
def steps(job):
    return job["steps"]


@pytest.fixture(scope="module")
def fortify_step(steps):
    for step in steps:
        if step.get("uses", "").startswith("fortify/github-action@"):
            return step
    raise AssertionError("Fortify github-action step not found")


class TestWorkflowFileAndSyntax:
    def test_workflow_file_exists(self):
        assert WORKFLOW_PATH.is_file()

    def test_workflow_is_valid_yaml(self, workflow_text):
        # Should not raise
        parsed = yaml.safe_load(workflow_text)
        assert isinstance(parsed, dict)

    def test_workflow_has_no_duplicate_top_level_keys(self, workflow_text):
        # A naive duplicate-key check: PyYAML silently overwrites duplicate
        # keys, so we look at the raw top-level key tokens instead.
        top_level_keys = re.findall(r"^(\w[\w-]*):", workflow_text, re.MULTILINE)
        assert len(top_level_keys) == len(set(top_level_keys)), (
            f"Duplicate top-level keys detected: {top_level_keys}"
        )

    def test_workflow_uses_third_party_action_disclaimer(self, workflow_text):
        assert "not certified by GitHub" in workflow_text


class TestTopLevelStructure:
    def test_top_level_keys_present(self, workflow):
        assert set(workflow.keys()) == {"name", True, "jobs"}

    def test_workflow_name(self, workflow):
        assert workflow["name"] == "Fortify AST Scan"

    def test_jobs_contains_exactly_one_job(self, workflow):
        assert list(workflow["jobs"].keys()) == ["Fortify-AST-Scan"]


class TestTriggers:
    def test_trigger_events_are_expected_set(self, triggers):
        assert set(triggers.keys()) == {
            "push",
            "pull_request",
            "schedule",
            "workflow_dispatch",
        }

    def test_push_trigger_targets_main_branch(self, triggers):
        assert triggers["push"]["branches"] == ["main"]

    def test_pull_request_trigger_targets_main_branch(self, triggers):
        assert triggers["pull_request"]["branches"] == ["main"]

    def test_pull_request_branches_are_subset_of_push_branches(self, triggers):
        # The workflow comment states pull_request branches must be a subset
        # of push branches; verify that invariant holds.
        push_branches = set(triggers["push"]["branches"])
        pr_branches = set(triggers["pull_request"]["branches"])
        assert pr_branches.issubset(push_branches)

    def test_schedule_trigger_has_single_cron_entry(self, triggers):
        assert isinstance(triggers["schedule"], list)
        assert len(triggers["schedule"]) == 1

    def test_schedule_cron_expression_is_well_formed(self, triggers):
        cron_expr = triggers["schedule"][0]["cron"]
        assert cron_expr == "45 1 * * 2"
        fields = cron_expr.split()
        assert len(fields) == 5, "Cron expression must have 5 fields"
        minute, hour, dom, month, dow = fields
        assert minute.isdigit() and 0 <= int(minute) <= 59
        assert hour.isdigit() and 0 <= int(hour) <= 23
        assert dom == "*"
        assert month == "*"
        assert dow.isdigit() and 0 <= int(dow) <= 6

    def test_workflow_dispatch_trigger_present(self, triggers):
        assert "workflow_dispatch" in triggers


class TestJobConfiguration:
    def test_job_runs_on_ubuntu_latest(self, job):
        assert job["runs-on"] == "ubuntu-latest"

    def test_job_permissions_are_minimal_and_expected(self, job):
        assert job["permissions"] == {
            "actions": "read",
            "contents": "read",
            "security-events": "write",
        }

    def test_job_permissions_do_not_grant_pull_requests_write(self, job):
        # pull-requests: write is commented out in the source template and
        # should only be required if PR-comment support is explicitly
        # enabled; ensure it is not silently granted.
        assert "pull-requests" not in job["permissions"]

    def test_job_has_exactly_two_steps(self, steps):
        assert len(steps) == 2


class TestCheckoutStep:
    def test_checkout_step_name_and_action(self, steps):
        checkout_step = steps[0]
        assert checkout_step["name"] == "Check Out Source Code"
        assert checkout_step["uses"] == "actions/checkout@v4"


class TestFortifyStep:
    def test_fortify_step_name(self, fortify_step):
        assert fortify_step["name"] == "Run Fortify Scan"

    def test_fortify_action_pinned_to_full_length_commit_sha(self, fortify_step):
        uses = fortify_step["uses"]
        assert uses.startswith("fortify/github-action@")
        ref = uses.split("@", 1)[1]
        assert re.fullmatch(r"[0-9a-f]{40}", ref), (
            f"Fortify action should be pinned to a 40-character commit SHA, got: {ref!r}"
        )

    def test_fortify_step_with_inputs(self, fortify_step):
        assert fortify_step["with"] == {
            "sast-scan": True,
            "debricked-sca-scan": True,
        }

    def test_fortify_step_env_keys(self, fortify_step):
        expected_keys = {
            "FOD_URL",
            "FOD_TENANT",
            "FOD_USER",
            "FOD_PASSWORD",
            "SSC_URL",
            "SSC_TOKEN",
            "SC_SAST_TOKEN",
            "DEBRICKED_TOKEN",
            "SC_SAST_SENSOR_VERSION",
        }
        assert set(fortify_step["env"].keys()) == expected_keys

    def test_fod_url_is_hardcoded_not_a_secret_expression(self, fortify_step):
        # FOD_URL must be a plain value (hardcoded/variable), never a secret.
        assert fortify_step["env"]["FOD_URL"] == "https://ams.fortify.com"
        assert "secrets." not in fortify_step["env"]["FOD_URL"]

    @pytest.mark.parametrize(
        "env_key,secret_name",
        [
            ("FOD_TENANT", "FOD_TENANT"),
            ("FOD_USER", "FOD_USER"),
            ("FOD_PASSWORD", "FOD_PAT"),
            ("SSC_TOKEN", "SSC_TOKEN"),
            ("SC_SAST_TOKEN", "SC_CLIENT_AUTH_TOKEN"),
            ("DEBRICKED_TOKEN", "DEBRICKED_TOKEN"),
        ],
    )
    def test_credentials_are_sourced_from_secrets_context(
        self, fortify_step, env_key, secret_name
    ):
        value = fortify_step["env"][env_key]
        assert value == f"${{{{secrets.{secret_name}}}}}"

    def test_ssc_url_is_sourced_from_vars_context_not_secrets(self, fortify_step):
        value = fortify_step["env"]["SSC_URL"]
        assert value == "${{vars.SSC_URL}}"
        assert "secrets." not in value

    def test_sensor_version_is_pinned_semver_string(self, fortify_step):
        version = fortify_step["env"]["SC_SAST_SENSOR_VERSION"]
        assert version == "24.4.0"
        assert re.fullmatch(r"\d+\.\d+\.\d+", version)

    def test_no_secret_values_are_leaked_as_plain_text(self, fortify_step):
        # Every credential-bearing env var must reference the secrets/vars
        # GitHub Actions context rather than embedding a literal value.
        credential_keys = {
            "FOD_TENANT",
            "FOD_USER",
            "FOD_PASSWORD",
            "SSC_TOKEN",
            "SC_SAST_TOKEN",
            "DEBRICKED_TOKEN",
        }
        for key in credential_keys:
            value = fortify_step["env"][key]
            assert value.startswith("${{") and value.endswith("}}"), (
                f"{key} should reference a GitHub Actions expression, got: {value!r}"
            )

    def test_optional_env_vars_are_not_enabled_by_default(self, fortify_step):
        # These optional flags are commented out in the template and must
        # not appear as active configuration.
        optional_keys = {
            "DO_SETUP",
            "DO_WAIT",
            "DO_POLICY_CHECK",
            "DO_JOB_SUMMARY",
            "DO_PR_COMMENT",
            "DO_EXPORT",
            "FOD_CLIENT_ID",
            "FOD_CLIENT_SECRET",
        }
        assert optional_keys.isdisjoint(fortify_step["env"].keys())