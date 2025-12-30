"""
Public-safe crypto interfaces (no implementation).
These demonstrate integration points without exposing IP.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class KeyContext:
    tenant_id: str
    object_id: str
    epoch: int
    purpose: str

class KeySystemInterface:
    def derive_key(self, ctx: KeyContext) -> bytes:
        raise NotImplementedError("Interface only (public-safe).")
