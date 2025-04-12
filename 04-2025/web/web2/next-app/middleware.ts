import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

const isAuthenticated = false
export function middleware(request: NextRequest) {
  console.log('Headers:')
  const headerEntries = Array.from(request.headers.entries())
  headerEntries.forEach(([key, value]) => {
    console.log(`  ${key}: ${value}`)
  })
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!isAuthenticated) {
      console.log('Auth failed - redirecting to /')
      return NextResponse.redirect(new URL('/', request.url))
    }
  }
  return NextResponse.next()
}
export const config = {
  matcher: ['/dashboard/:path*'],
} 