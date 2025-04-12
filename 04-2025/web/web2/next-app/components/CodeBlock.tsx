'use client'

import { useState } from 'react'

export default function CodeBlock({
  code,
  language = 'shell',
}: {
  code: string
  language?: string
}) {
  const [copied, setCopied] = useState(false)

  const handleCopy = () => {
    navigator.clipboard.writeText(code)
    setCopied(true)
    setTimeout(() => setCopied(false), 1500)
  }

  return (
    <div className="relative my-6 rounded-md bg-zinc-900 text-white font-mono text-sm overflow-hidden">
      <div className="flex justify-between items-center bg-zinc-800 px-4 py-2 text-zinc-400 text-xs uppercase font-semibold">
        <span>{language}</span>
        <button
          onClick={handleCopy}
          className="border border-zinc-700 px-2 py-0.5 rounded hover:bg-white hover:text-black transition-all"
        >
          {copied ? 'Copied!' : 'Copy'}
        </button>
      </div>
      <pre className="px-4 py-3 whitespace-pre-wrap overflow-x-auto">{code}</pre>
    </div>
  )
}
