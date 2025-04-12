import './globals.css'
import '../public/dist/css/style.css'

export const metadata = {
  title: 'Secrets Management',
  description: 'Secure internal password vault for devs',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="no-js">
      <head>
        {/* ✅ Google Fonts with display=optional */}
        <link
          href="https://fonts.googleapis.com/css?family=IBM+Plex+Sans:400,600&display=optional"
          rel="stylesheet"
        />
      </head>
      <body className="is-boxed has-animations">
        {children}

        {/* ✅ External scripts loaded at bottom for animation */}
        <script
          src="https://unpkg.com/animejs@3.0.1/lib/anime.min.js"
          defer
        ></script>
        <script
          src="https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js"
          defer
        ></script>
      </body>
    </html>
  )
}
