"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeSlug from "rehype-slug";
import rehypeAutolinkHeadings from "rehype-autolink-headings";

interface Props {
  content: string;
}

export default function MarkdownViewer({ content }: Props) {
  return (
    <article className="prose prose-invert max-w-none">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[
          rehypeSlug,
          rehypeAutolinkHeadings,
        ]}
      >
        {content}
      </ReactMarkdown>
    </article>
  );
}
