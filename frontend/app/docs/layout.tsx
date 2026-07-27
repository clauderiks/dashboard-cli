import DocsSidebar from "@/components/docs/DocsSidebar";
import DocsHeader from "@/components/docs/DocsHeader";
import DocsTOC from "@/components/docs/DocsTOC";


/**
 * Renders the documentation page layout with header, navigation sidebar, content area, and table of contents.
 */
export default function DocsLayout({
 children,
}: {
 children: React.ReactNode;
}) {


return (

<div className="min-h-screen bg-[#02050c] text-white">


<DocsHeader />


<div className="flex">


<DocsSidebar />


<main className="
flex-1
max-w-5xl
p-10
">

{children}

</main>


<DocsTOC />


</div>


</div>

);

}
