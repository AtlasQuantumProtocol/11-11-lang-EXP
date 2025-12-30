 Key Systems Overview (Public Safe)

This repository demonstrates how a language and runtime can integrate with a security key system without including any sensitive implementations.

 Principles
- Key systems are accessed through explicit interfaces
- Context-based derivation is represented as data
- Real key material never appears in this public repository

 Context Model
A key request is represented as a context object:
- tenant identifier
- object identifier
- epoch or version number
- purpose label

This enables:
- compartmentalization
- rotation
- governance and audit alignment

 Implementation posture
- This public repository includes interfaces only
- Production key systems exist separately under controlled access
