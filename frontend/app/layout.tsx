import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Risk AI',
  description: 'Codex-like AI Assistant for Code',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  )
}
