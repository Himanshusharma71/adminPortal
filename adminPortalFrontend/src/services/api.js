const BASE_URL = 'http://127.0.0.1:8000/auth'

export const loginUser = async (credentials) => {
  const res = await fetch(`${BASE_URL}/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(credentials)
  })

  if (!res.ok) throw new Error('Login failed')

  const data = await res.json()
  return { email: credentials.email, token: data.access_token }
}
