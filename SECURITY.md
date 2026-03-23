# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| `main`  | ✅ Yes     |
| older   | ❌ No      |

## Reporting a Vulnerability

**Please do NOT open a public GitHub issue for security vulnerabilities.**

Report security issues privately by emailing:
**security@pcvr.lol**

Include:
- A clear description of the vulnerability
- Steps to reproduce
- Affected module(s) (e.g., `eve_toolkit`, `skyburner`, `project_dont_die`)
- Any suggested mitigations

We aim to acknowledge all reports within **48 hours** and provide a full response within **7 days**.

## Disclosure Policy

Once a fix is merged, a security advisory will be published on the
[GitHub Security Advisories](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/security/advisories)
page and noted in [CHANGELOG.md](./CHANGELOG.md).

## Scope

- Core Python modules (`skyburner/`, `eve_toolkit/`, `project_dont_die/`)
- Web dashboard (`dashboard/`)
- GitHub Actions workflows (`.github/workflows/`)

Dependency issues in downstream projects (e.g., Chart.js CDN) are out of scope
unless they directly affect PCVR Studios code.
