
 11-11-lang-EXP (Public Demo Repo)

11-11-lang-EXP is a public, safe demonstration repository for the 11/11 Language concept: a security-first, audit-first execution model designed for long-horizon computing.

This repo is intentionally non-production and non-implementing for proprietary components. It is designed to demonstrate:

- language structure and developer experience
- architecture and module boundaries
- audit plus security interfaces
- an executable demo flow (safe stub pipeline)

 What this repo is
- A public demo of how 11/11 Language is structured
- A reference for interfaces and governance
- A safe sandbox for docs, examples and demos

 What this repo is NOT
- Not the full 11/11 compiler
- Not the proprietary IR engine
- Not production cryptography
- Not the proprietary key system implementation

 Ownership
All concepts, naming and associated intellectual property are owned and stewarded by:

11 AI Blockchain Developments LLC (Wyoming)

See: `NOTICE.md` and `IP_GUARDRAILS.md`.



 Quick Start

 Requirements
- Python 3.11+

 Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .

Run a demo
elevenlang demo src/demo/examples/hello.111

Run tests
pytest

Repo Layout

docs/ — public-safe specs and architecture notes

src/elevenlang/ — demo compiler pipeline (stubs plus interfaces)

src/demo/ — example programs and demo runner

tests/ — contract tests that ensure repo stays “safe”
