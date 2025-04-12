'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function LoginPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const router = useRouter()

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault()

    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    })

    if (!res.ok) {
      setError('Invalid credentials')
    } else {
      router.push('/protected')
    }
  }

  return (
    <main className="is-boxed has-animations">
      <div className="body-wrap">
        <header className="site-header">
          <div className="container">
            <div className="site-header-inner">
              <div className="brand header-brand">
                <h1 className="m-0">
                  <a href="/">
                    <img className="header-logo-image" src="/dist/images/logo.svg" alt="Vault Logo" />
                  </a>
                </h1>
              </div>
            </div>
          </div>
        </header>

        <section className="hero">
          <div className="container">
            <div className="hero-inner">
              <div className="hero-copy" style={{ maxWidth: '400px', margin: '0 auto' }}>
                <h1 className="hero-title mt-0 text-center">Employee Login</h1>
                <p className="hero-paragraph text-center">
                  Enter your credentials to access the secure vault.
                </p>

                <form onSubmit={handleLogin} className="mt-8">
                  <div className="mb-4">
                    <input
                      type="text"
                      placeholder="Username"
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                      required
                      style={{
                        width: '100%',
                        padding: '12px',
                        borderRadius: '4px',
                        border: '1px solid #ccc',
                      }}
                    />
                  </div>
                  <div className="mb-4">
                    <input
                      type="password"
                      placeholder="Password"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                      style={{
                        width: '100%',
                        padding: '12px',
                        borderRadius: '4px',
                        border: '1px solid #ccc',
                      }}
                    />
                  </div>

                  {error && (
                    <p style={{ color: 'red', fontSize: '0.9rem', marginBottom: '1rem' }}>
                      {error}
                    </p>
                  )}

                  <button
                    type="submit"
                    className="button button-primary button-block"
                    style={{ width: '100%' }}
                  >
                    Login
                  </button>

                  <div className="text-center mt-3">
                    <a href="#" className="text-sm" style={{ color: '#0270D7' }}>
                      Forgot password?
                    </a>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  )
}
