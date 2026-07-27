"use client";

import Link from "next/link";
import { BookOpen, Shield, Code2, Rocket } from "lucide-react";

const menus = [
  {
    title: "Getting Started",
    icon: Rocket,
    items: [
      {
        name: "Introduction",
        path: "introduction"
      }
    ]
  },
  {
    title: "Developer",
    icon: Code2,
    items: [
      {
        name: "API",
        path: "api"
      }
    ]
  },
  {
    title: "Security",
    icon: Shield,
    items: [
      {
        name: "Security Guide",
        path: "security"
      }
    ]
  }
];

/**
 * Renders the documentation sidebar with grouped navigation links.
 *
 * @returns The sidebar markup for the documentation navigation.
 */
export default function DocsSidebar() {
  return (
    <aside className="w-72 min-h-screen border-r border-zinc-800 bg-[#050915] p-6">

      <div className="flex items-center gap-2 mb-8">
        <BookOpen size={22}/>
        <h1 className="font-bold text-xl">
          ClaudeRiks Docs
        </h1>
      </div>


      {menus.map((menu)=>(
        <div key={menu.title} className="mb-8">

          <div className="flex items-center gap-2 text-sm text-zinc-400 mb-3">
            <menu.icon size={16}/>
            {menu.title}
          </div>


          {menu.items.map(item=>(
            <Link
              key={item.path}
              href={`/docs/${item.path}`}
              className="block px-3 py-2 rounded hover:bg-zinc-800 text-sm"
            >
              {item.name}
            </Link>
          ))}

        </div>
      ))}

    </aside>
  );
}
