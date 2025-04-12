# 🛡️ Internal Password Vault Server

A **secure, minimal password vault** for developers and internal teams to store credentials inside a protected network. Built for simplicity and extensibility — also used by **ourselves internally**.

- ✅ Free and open source for personal use
- 🏢 Paid support for enterprise use
- 🔒 Intended for internal network deployment (e.g., behind a VPN or proxy)

---

## ✅ Key Features

- Save passwords via HTTP GET — **no authentication required**
- Retrieve all stored passwords (including FLAGS) — **authentication required**
- Custom header-based Basic Auth
- `.vault.env` support for configuring auth and port
- Plain text storage in `creds.txt`
- Minimal dependencies, fast setup, ready for devs and DevOps use

---

## 🚀 Getting Started

### 1. Install requirements (optional)

Only `.env` support is used:

```bash
pip install python-dotenv
```

### 2. Create your config file

Create a `.vault.env` in the same directory:

```env
USERNAME=admin
PASSWORD=admin
PORT=8000
```

### 3. Run the Server

```bash
python vault_server.py
```

It runs on `http://localhost:8000` (or your specified port).

---

## 💾 Saving Credentials (No Auth Required)

Send a `GET` request with `login:password` in the URL:

```bash
curl http://localhost:8000/devuser:supersecret
```

This will append the entry to `creds.txt` like:

```
devuser:supersecret
```

---

## 🔐 Retrieving Credentials (Auth Required)

You must include the `Authorization-Internal` header using your `.vault.env` credentials:

```bash
echo -n 'admin:admin' | base64
```

Then:

```bash
curl -H "Authorization-Internal: Basic YWRtaW46YWRtaW4=" http://localhost:8000/
```

Returns all stored credentials.

---

## 📁 Vault File Format

All saved credentials go into `creds.txt`:

```
user1:pass123
admin:letmein
ci-bot:token-value
```

---

## 🛡️ Security Design

This vault is **intentionally minimal and safe for internal use**:

- Auth required **only for reading**
- Runs behind **VPN or proxy**
- We use it internally to manage secrets for development, CTFs, and automation tooling
- Custom header avoids conflicts with standard HTTP Basic Auth clients

---

## 💸 Licensing & Support

- ✅ **Free for personal and non-commercial use**
- 🏢 **Enterprise support/licensing available** (priority fixes, onboarding, hardening)

---

## 🧠 Example Use Cases

- Internal DevOps secrets exchange
- Temporary vaulting in CI pipelines
- Lightweight secrets manager for homelabs

---

## 📬 Contact

Need help or want to contribute?
Open an issue or submit a pull request — we're actively improving this!

---
