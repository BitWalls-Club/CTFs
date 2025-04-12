'use client'

import Image from 'next/image'

export default function HomePage() {
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

      {/* Hero Section */}
      <main>
        <section className="hero">
          <div className="container">
            <div className="hero-inner">
              <div className="hero-copy">
                <h1 className="hero-title mt-0">Internal Password Vault Server</h1>
                <p className="hero-paragraph">
                  A <strong>secure, minimal password vault</strong> for developers and internal teams to store credentials inside a protected network.
                </p>
                <ul>
                  <li>✅ Free and open source for personal use</li>
                  <li>🔒 For internal network deployment (VPN/proxy)</li>
                  <li>🔐 Retrieve passwords via Basic Auth header</li>
                  <li>💾 Stored in plain text <code>creds.txt</code></li>
                </ul>
                <div className="hero-cta">
                  <a className="button button-primary" href="/login">Employee Login</a>
                  <a className="button" href="/vault.zip" download>Download</a>
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

        {/* Pricing Section */}
        <section className="pricing section">
          <div className="container-sm">
            <div className="pricing-inner section-inner">
              <div className="pricing-header text-center">
                <h2 className="section-title mt-0">Unlimited for all, Secure and Open Source</h2>
                <p className="section-paragraph mb-0">
                  Used in DevOps, CI/CD pipelines, and CTFs. Simple vaulting, fast retrieval, zero external dependencies.
                </p>
              </div>
              <div className="pricing-tables-wrap">
                <div className="pricing-table">
                  <div className="pricing-table-inner is-revealing">
                    <div className="pricing-table-main">
                      <div className="pricing-table-header pb-24">
                        <div className="pricing-table-price">
                          <span className="pricing-table-price-currency h2">$</span>
                          <span className="pricing-table-price-amount h1">49</span>
                          <span className="text-xs">/month</span>
                        </div>
                      </div>
                      <div className="pricing-table-features-title text-xs pt-24 pb-24">
                        What you will get
                      </div>
                      <ul className="pricing-table-features list-reset text-xs">
                        <li>Store credentials via HTTP GET</li>
                        <li>Retrieve all credentials with auth</li>
                        <li>Minimal config: <code>.vault.env</code></li>
                        <li>No DB required, file-based storage</li>
                      </ul>
                    </div>
                    <div className="pricing-table-cta mb-8">
                      <a className="button button-primary button-shadow button-block" href="/login">
                        Employee Login
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="cta section">
          <div className="container">
            <div className="cta-inner section-inner">
              <h3 className="section-title mt-0">Examine the internal Dashboard</h3>
              <div className="cta-cta">
                <a className="button button-primary button-wide-mobile" href="/dashboard">
                  Go to Dashboard
                </a>
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
