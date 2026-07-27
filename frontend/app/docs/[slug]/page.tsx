import MarkdownViewer from "@/components/docs/MarkdownViewer";
import fs from "fs";
import path from "path";

/**
 * Renders the Markdown document identified by the route slug.
 *
 * @param params - Route parameters containing the document slug.
 * @returns The rendered Markdown document.
 */
export default async function DocsPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  const filePath = path.join(
    process.cwd(),
    "docs",
    `${slug}.md`
  );

  const content = fs.readFileSync(
    filePath,
    "utf8"
  );

  return (
    <div className="p-10">
      <MarkdownViewer content={content}/>
    </div>
  );
}
