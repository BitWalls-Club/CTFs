'use server'

import { redirect } from 'next/navigation'

export async function create() {
  console.log('Clicked')
  return redirect('/?clicked=true')
}
