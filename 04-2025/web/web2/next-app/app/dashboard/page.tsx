'use client'

import { useTransition, useEffect, useState } from 'react'
import { create } from '../actions'
import Image from 'next/image'

export default function ProtectedPage() {
  const [isPending, startTransition] = useTransition()
  const [showSecondMsg, setShowSecondMsg] = useState(false)
  const [password, setPassword] = useState('')
  const [flag, setFlag] = useState('')

  useEffect(() => {
    setPassword(process.env.NEXT_PUBLIC_MESSAGE || 'not-set')
    setFlag(process.env.NEXT_PUBLIC_FLAG1 || 'FLAG1 not found')

    const timer = setTimeout(() => {
      setShowSecondMsg(true)
    }, 2000)

    return () => clearTimeout(timer)
  }, [])

  const handleFlag = () => {
    alert(`FLAG1: ${flag}`)
  }

  return (
    <div className="body-wrap">
      {/* Header */}
      <header className="site-header">
        <div className="container">
          <div className="site-header-inner">
            <div className="brand header-brand">
              <h1 className="m-0">
                <a href="#">
                  <Image
                    className="header-logo-image"
                    src="/dist/images/logo.svg"
                    alt="Logo"
                    width={120}
                    height={40}
                  />
                </a>
              </h1>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main>
        <section className="hero">
          <div className="container">
            <div className="hero-inner">
              <div className="hero-copy text-center">
                <h1 className="hero-title mt-0">Protected Vault Interface</h1>
                <p className="hero-paragraph">
                  You are authenticated and can now access internal functionality.
                </p>

                <div className="hero-cta mt-6 space-x-4">
                  <form
                    action={() => startTransition(() => create())}
                    className="inline"
                  >
                    <button
                      type="submit"
                      disabled={isPending}
                      className="button button-primary"
                    >
                      {isPending ? 'Processing...' : 'Internal'}
                    </button>
                  </form>

                  <button onClick={handleFlag} className="button">
                    Get Flag 1
                  </button>
                </div>

                {/* Chatbox */}
                <div className="mt-10 max-w-md mx-auto bg-gray-100 rounded-lg p-4 shadow-lg text-left font-mono">
                  <div className="text-sm text-gray-700 mb-2">
                    <strong>Intern:</strong> Can you share me my credentials for the vault?
                  </div>

                  <div className="text-sm text-gray-900 bg-white p-3 rounded border">
                    <strong>DevOps:</strong> – here it is ⇒{' '}
                    <code className="break-all whitespace-pre-wrap">coder:{password}</code><br />
                    – update them ASAP and let me know
                  </div>
                </div>

                {/* Animated GIF */}
                <div className="mt-10 flex flex-col items-center">
                  <Image
                    src="/sigma.gif"
                    alt="Hacker GIF"
                    width={256}
                    height={160}
                    className="mb-4 rounded-md shadow-md"
                  />
                  <p className="text-lg font-semibold">
                    You should continue to hack for <code>flag2</code>.
                  </p>
                </div>
              </div>

              <div className="hero-figure anime-element">
                <svg className="placeholder" width="528" height="396" viewBox="0 0 528 396">
                  <rect width="528" height="396" style={{ fill: 'transparent' }} />
                </svg>
                {[...Array(10)].map((_, i) => (
                  <div key={i} className={`hero-figure-box hero-figure-box-0${i + 1}`} />
                ))}
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="site-footer">
        <div className="container">
          <div className="site-footer-inner">
            <div className="brand footer-brand">
              <a href="#">
                <Image
                  className="header-logo-image"
                  src="/dist/images/logo.svg"
                  alt="Logo"
                  width={120}
                  height={40}
                />
              </a>
            </div>
            <ul className="footer-links list-reset">
              <li><a href="#">Contact</a></li>
              <li><a href="#">About us</a></li>
              <li><a href="#">FAQ&apos;s</a></li>
              <li><a href="#">Support</a></li>
            </ul>
            <div className="footer-copyright">
              &copy; {new Date().getFullYear()} Vault, all rights reserved
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
