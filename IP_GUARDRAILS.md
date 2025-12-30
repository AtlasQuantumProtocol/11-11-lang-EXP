 IP_GUARDRAILS (Public Repo Safety Rules)

This repo must remain public-safe.

 Allowed
- Interface definitions
- Documentation and architecture
- Toy examples and stub implementations
- Non-proprietary demo code

 NOT Allowed
- Real encryption/key derivation implementations used in production
- Proprietary compiler optimizations, internal IR transforms
- Any private keys, real endpoints, infrastructure references
- Any “copy of the production repo” code

 Contribution Rule
If a change reveals proprietary implementation detail, reject it and keep only interface-level documentation.
