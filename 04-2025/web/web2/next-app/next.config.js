/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  reactStrictMode: true,
  // Using the old rewrites/redirects system for middleware
  // This is to match a more vulnerable configuration
  experimental: {
    // Turn off newer security protections
    instrumentationHook: false,
  }
}

module.exports = nextConfig
