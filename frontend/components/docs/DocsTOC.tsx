"use client";

const headings = [
 "Introduction",
 "Features",
 "Getting Started"
];


export default function DocsTOC(){

return (

<aside className="
w-64
border-l
border-zinc-800
p-6
hidden
xl:block
">

<h3 className="text-sm font-semibold mb-4">
On this page
</h3>


<nav className="space-y-3">

{headings.map(item=>(

<a
key={item}
href={`#${item.toLowerCase().replaceAll(" ","-")}`}
className="
block
text-sm
text-zinc-400
hover:text-white
"
>
{item}
</a>

))}

</nav>

</aside>

);

}
