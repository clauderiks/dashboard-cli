"use client";

import { Search, Github, Moon } from "lucide-react";

export default function DocsHeader(){

return (
<header className="h-16 border-b border-zinc-800 flex items-center justify-between px-8 bg-[#050915]">

  <div className="flex items-center gap-3 w-full max-w-xl">

    <Search size={18} className="text-zinc-400"/>

    <input
      placeholder="Search documentation..."
      className="
      bg-transparent
      outline-none
      text-sm
      w-full
      "
    />

  </div>


  <div className="flex items-center gap-5">

    <button>
      <Moon size={18}/>
    </button>

    <button>
      <Github size={19}/>
    </button>

  </div>

</header>
);

}
