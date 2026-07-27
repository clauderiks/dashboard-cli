---
title: 'Application card: GitHub security and quality AI features'
shortTitle: Security and quality AI features
intro: Use GitHub's AI-powered code security and code quality features responsibly by understanding their purposes, capabilities, and limitations.
versions:
  fpt: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning
  - /code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning
  - /code-security/responsible-use/responsible-use-autofix-code-scanning
  - /code-security/secret-scanning/about-the-detection-of-generic-secrets-with-secret-scanning
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/generic-secret-detection/about-the-detection-of-generic-secrets-with-secret-scanning
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/generic-secret-detection/responsible-ai-generic-secrets
  - /code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets
  - /code-security/secret-scanning/copilot-secret-scanning
  - /code-security/responsible-use/responsible-ai-generic-secrets
  - /code-security/secret-scanning/about-the-regular-expression-generator-for-custom-patterns
  - /code-security/secret-scanning/about-generating-regular-expressions-with-ai
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/about-generating-regular-expressions-with-ai
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/responsible-use-ai-regex-generator
  - /code-security/secret-scanning/copilot-secret-scanning/responsible-use-ai-regex-generator
  - /code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator
  - /code-security/responsible-use/responsible-ai-regex-generator
  - /code-security/code-quality/responsible-use/code-quality
  - /code-security/responsible-use/code-quality
contentType: rai
category:
  - Responsible use
---

## What is an Application Card?

{% data reusables.rai.copilot.application-card-intro %}

## 1. Overview

GitHub's security and quality platform includes several AI-powered capabilities that help developers find and fix security vulnerabilities, detect leaked secrets, and improve code quality. This application card covers the following experiences:

* **Copilot Autofix for code scanning**: Automatically generates fix suggestions for CodeQL alerts on pull requests and the default branch.
* **Generic secret detection**: Uses a model to identify unstructured secrets in source code that deterministic pattern matching cannot find.
* **Custom pattern regex generator**: Uses AI to generate regular expressions for custom secret scanning patterns from natural language descriptions.
* **GitHub Code Quality**: Surfaces code quality issues and offers LLM-powered fix suggestions on pull requests and the default branch.

Copilot Autofix is an expansion of code scanning that provides users with targeted recommendations to help them fix code scanning alerts, avoiding the introduction of new security vulnerabilities. Potential fixes are generated automatically by large language models (LLMs) using data from the codebase and from code scanning analysis. Copilot Autofix is available for CodeQL analysis and does not require a GitHub Copilot subscription.

Code scanning users can already see security alerts on their pull requests. However, developers often have little training in secure coding, so fixing these alerts requires substantial effort. Copilot Autofix lowers the barrier of entry by combining information on best practices with details of the codebase and alert to suggest a potential fix. Instead of starting with a search for information about the vulnerability, the developer starts with a code suggestion that demonstrates a potential solution for their codebase. The developer evaluates the potential fix to determine whether it is the best solution for their codebase and to ensure that it maintains the intended behavior.

Secret scanning's generic secret detection is an AI-powered expansion of secret scanning that identifies unstructured secrets in source code or other GitHub surfaces and generates an alert. GitHub Secret Protection and GitHub Advanced Security users can already receive secret scanning alerts for partner or custom patterns found in their source code, but unstructured secrets are not easily discoverable. Secret scanning uses models to identify these secrets. When a finding is detected, an alert is displayed in the "Generic" list of secret scanning alerts (under the **{% octicon "shield" aria-hidden="true" aria-label="shield" %} {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository, organization, or enterprise), so that maintainers and security managers can review the alert and, where necessary, remove the credential or implement a fix. Generic secret detection does not require a GitHub Copilot subscription.

Secret scanning's custom pattern regular expression generator makes it possible to define custom secret scanning patterns without knowledge of regular expressions. Users input a natural language description of what they want to detect, along with optional example strings, and the generator produces up to three candidate regular expressions. These patterns can then be validated via the dry-run mechanism before being deployed as custom patterns. The regular expression generator does not require a GitHub Copilot subscription.

GitHub Code Quality helps users improve code reliability, maintainability, and overall project health by surfacing actionable feedback and offering automatic fixes for findings in pull requests and on the default branch. When Code Quality is enabled, two types of analysis run: CodeQL quality queries identify problems with the maintainability, reliability, or style of code, and LLM-powered analysis provides additional insights beyond what deterministic engines can find. When a quality issue is detected, Copilot Autofix suggests a relevant fix. On pull requests, results are displayed as comments left by the `github-code-quality` bot. On the default branch, LLM-powered findings are displayed in the **AI findings** dashboard under the **{% octicon "shield" aria-hidden="true" aria-label="shield" %} {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.

The primary supported language for GitHub Code Security AI features is English.

## 2. Key terms

The following list provides a glossary of key terms related to GitHub Code Security AI features:

* **CodeQL**: GitHub's semantic code analysis engine for identifying security vulnerabilities in source code.
* **Copilot Autofix**: GitHub's LLM-powered feature that automatically generates fix suggestions for code scanning alerts. Copilot Autofix is available for CodeQL analysis and does not require a GitHub Copilot subscription.
* **Large language model (LLM)**: A type of neural network trained on a large body of text data that can generate, analyze, and transform natural language and code. Copilot Autofix uses one or more LLMs to process code scanning alerts and produce fix suggestions.
* **AI detection for secret scanning**: AI-powered capabilities that extend secret scanning, including generic secret detection. Does not require a GitHub Copilot subscription.
* **Generic secret detection**: AI identification of unstructured secrets (such as passwords) that are not covered by partner or custom patterns. Generic secret detection uses models to scan for password-like strings in source code.
* **Custom pattern**: A user-defined regular expression used by secret scanning to detect secrets that match a specific format. The custom pattern regular expression generator helps create these patterns from natural language descriptions.
* **SARIF**: Static Analysis Results Interchange Format—the standard format CodeQL uses to report code scanning findings, including alert locations and descriptions.
* **GitHub Code Quality**: A feature that surfaces code quality issues and offers LLM-powered fixes. Code Quality combines CodeQL quality queries with LLM-powered analysis to identify maintainability, reliability, and style issues.
* **AI findings**: The dashboard under the **{% octicon "shield" aria-hidden="true" aria-label="shield" %} {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab where LLM-powered Code Quality findings for the default branch are displayed.

## 3. Key features or capabilities

The key features and capabilities outlined here describe what GitHub Code Security AI features are designed to do and how they perform across supported tasks.

* **Automated fix suggestions for security alerts**: Copilot Autofix automatically generates code change suggestions for CodeQL alerts found on pull requests and on the default branch. Each suggestion includes both the proposed code change and a natural language explanation of the fix.
* **Alert-to-fix translation**: Copilot Autofix translates the description and location of a code scanning alert into actionable code changes that may resolve the underlying security vulnerability. The system uses CodeQL alert data in SARIF format, surrounding code snippets, and query help text to generate relevant fixes.
* **Multi-language support**: Copilot Autofix supports fix generation for a subset of queries included in the default and security-extended CodeQL query suites for C#, C/C++, Go, Java/Kotlin, Swift, JavaScript/TypeScript, Python, Ruby, and Rust. For more information on these query suites, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites#built-in-codeql-query-suites).
* **AI-powered password detection**: Secret scanning's generic secret detection scans repository content using AI to identify unstructured secrets (like passwords) that deterministic pattern matching cannot find. Detected secrets are surfaced as alerts in the secret scanning alert list under the **{% octicon "shield" aria-hidden="true" aria-label="shield" %} {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
* **AI-powered regular expression generation**: Secret scanning's regular expression generator takes a natural language description of the pattern you want to detect, along with optional example strings, and produces up to three candidate regular expressions. Each result includes an AI-generated plain language description, and you can validate patterns via a dry run before deployment.
* **Code quality issue detection**: GitHub Code Quality runs CodeQL quality queries on changed code in pull requests and periodically on the full default branch. These queries identify maintainability, reliability, and style issues.
* **LLM-powered code quality analysis**: After each push to the default branch, an LLM analyzes recently changed files for quality issues beyond what deterministic engines can find. Findings are displayed in the **AI findings** dashboard.
* **Automated fix suggestions for quality findings**: When a quality issue is detected by either type of analysis, Copilot Autofix generates a fix suggestion. On pull requests, the `github-code-quality` bot posts a comment with the suggested change.

## 4. Intended uses

GitHub Code Security AI features can be used in multiple scenarios across a variety of industries. Some examples of use cases include:

* **Accelerating remediation of security vulnerabilities**: Use Copilot Autofix to quickly generate fix suggestions for CodeQL alerts, reducing the time and expertise required to address security issues found during code scanning.
* **Reducing the barrier to secure coding**: Copilot Autofix helps developers with limited secure-coding training. Instead of researching vulnerabilities independently, developers start with a code suggestion that demonstrates a potential solution for their codebase.
* **Streamlining pull request review**: When code scanning finds alerts on a pull request, Copilot Autofix provides suggested fixes inline, helping developers resolve security issues before merging.
* **Fixing alerts on the default branch**: Copilot Autofix can also generate fix suggestions for existing alerts on the default branch, helping teams reduce their backlog of security findings.
* **Detecting leaked passwords in source code**: Use generic secret detection to find unstructured secrets in repositories that fall outside the coverage of partner and custom secret scanning patterns.
* **Triaging credentials with contextual alerts**: When a password is detected, an alert with AI-detection context is displayed in the alerts list, enabling maintainers and security managers to review the finding and take action.
* **Creating custom secret scanning patterns without regex expertise**: Use the regular expression generator to define custom patterns by describing what you want to detect in natural language, removing the need to write regular expressions manually.
* **Validating generated patterns before deployment**: After generating regular expressions, use the dry-run mechanism to test patterns across your repository or organization before deploying them as custom patterns.
* **Surfacing code quality issues across a repository**: Use GitHub Code Quality to identify maintainability, reliability, and style issues so developers and administrators can quickly prioritize areas of risk.
* **Accelerating remediation of code quality findings**: Copilot Autofix suggests fixes for quality findings, combining information on best practices with details of the codebase to propose a potential fix directly on the pull request or in the AI findings dashboard.
* **Providing actionable feedback on pull requests**: The `github-code-quality` bot posts comments with suggested fixes on pull requests, helping developers address quality issues before merging.

## 5. Models and training data

Copilot Autofix uses internal GitHub Copilot APIs interfacing with the large language models, which produce both suggested fixes in code and explanatory text for those fixes.

Generic secret detection uses models to scan for unstructured secrets.

The custom pattern regular expression generator uses LLMs and the GitHub Copilot API to generate regular expressions that match user-provided descriptions and examples.

GitHub Code Quality's LLM-powered analysis uses Copilot language models to analyze recently changed files for quality issues. The CodeQL quality queries component does not use an LLM. Copilot Autofix for Code Quality findings uses the same LLM pipeline as Copilot Autofix for code scanning.

For a comparison of the models available for Copilot, see [AUTOTITLE](/copilot/reference/ai-models/model-comparison). For the full list of supported models, see [AUTOTITLE](/copilot/reference/ai-models/supported-models). For information on where models are hosted, see [AUTOTITLE](/copilot/reference/ai-models/model-hosting). To learn more about the data used to train the foundation models behind GitHub security and quality, see [What data has GitHub Copilot been trained on?](https://github.com/features/copilot#faq) in the GitHub Copilot FAQ.

Data handled by Copilot Autofix is not employed for LLM training purposes. The use of this feature is governed by the existing terms and conditions associated with GitHub Advanced Security. For more information, see [AUTOTITLE](/free-pro-team@latest/site-policy/github-terms/github-terms-for-additional-products-and-features#advanced-security){% ifversion fpt %}.{% else %} in the Free, Pro, & Team documentation.{% endif %}

## 6. Performance

When Copilot Autofix is enabled for a repository, code scanning alerts are processed through the following pipeline:

1. **Input processing**: When a code scanning alert is identified, GitHub assembles the relevant data into a prompt for the language model. This data includes:
   * CodeQL alert data in SARIF format
   * Code from the current version of the branch, including short snippets around each source location, sink location, and any location referenced in the alert message or flow path
   * The first ~10 lines from each file involved in any of those locations
   * Help text for the CodeQL query that identified the problem
1. **Language model analysis**: The assembled prompt is sent to the language model, which analyzes the alert context, code structure, and query help information.
1. **Response generation**: The model generates a potential fix, including both the proposed code change and an explanatory text describing the fix.
1. **Output formatting**: The suggestion is stored within the code scanning backend and displayed as an inline suggestion on the pull request or alert detail page. No user interaction is needed beyond enabling code scanning on the codebase and creating a pull request.

### Differences by experience

**AI secret detection** processes input and produces output as follows:

1. **Input processing**: Input is limited to text (typically code) that a user has checked into a repository. The system provides this text to the model along with a meta prompt asking the model to find unstructured secrets within the scope of the input. The user does not interact with the model directly. Multiple models may be used to validate a single finding.
1. **Model analysis**: The model scans for strings that resemble unstructured secrets like passwords.
1. **Response generation**: The model verifies that the identified strings included in the response actually exist in the input.
1. **Output formatting**: Detected strings are surfaced as alerts on the secret scanning alerts page in a separate list from regular secret scanning alerts. Each alert notes that it was detected by AI.{% ifversion secret-scanning-ai-generic-secret-detection %} For information on how to view alerts for generic secrets, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/viewing-alerts).{% endif %}

**Custom pattern regex generator** processes input and produces output as follows:

1. **Input processing**: Users input a natural language text description of the pattern they want to detect, along with optional example strings that should be matched.
1. **Language model analysis**: The description and examples are sent to the LLM via the GitHub Copilot API, which generates regular expressions matching the input.
1. **Response generation**: The model returns up to three candidate regular expressions. Each result includes an AI-generated plain language description. Some results may be quite similar, and some may not match every instance of the intended pattern.
1. **Output formatting**: Results are displayed in the custom pattern definition form. When you click **Use result**, the expression and any examples are copied to the main custom pattern form, where you can perform a dry run to validate the pattern across your repository or organization. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns).

**GitHub Code Quality LLM-powered analysis** processes input and produces output as follows:

1. **Input processing**: After each push to the default branch, recently changed files are combined with other relevant contextual information to form a prompt. The prompt is sent to a Copilot language model.
1. **Language model analysis**: The language model analyzes the code for maintainability, reliability, and other quality issues.
1. **Response generation**: The model generates a response that can include natural language suggestions and code suggestions linked to specific lines.
1. **Output formatting**: Findings are displayed in the **AI findings** dashboard under the **{% octicon "shield" aria-hidden="true