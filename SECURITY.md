# Security Policy

## Scope

This project distributes natural-language workflows and helper scripts for coding agents. Skills can influence what an agent attempts to do; treat them as executable policy, not harmless documentation.

## Reporting

Please do not publish secrets, exploit instructions against real third-party systems, or sensitive user data in a public issue. Contact the repository maintainer through a private channel listed on the repository profile when one is available. Include the affected path, impact, minimal reproduction, and a proposed mitigation when safe.

## Maintainer guidance

- Keep helper scripts dependency-free where possible.
- Do not require secrets for local validation or packaging.
- Avoid implicit network access or destructive behavior.
- Never send repository contents to a model provider without an explicit user-authorized path.
- Review changes to installer paths and overwrite behavior carefully.
