// src/app/api/login/route.ts
import { NextResponse } from 'next/server'

export async function POST() {
  return new NextResponse('Unauthorized', { status: 401 })
}
