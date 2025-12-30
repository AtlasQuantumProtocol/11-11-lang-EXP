"""
Public-safe audit interfaces (no implementation).
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class AuditEvent:
    event_type: str
    context_hash: str
    timestamp_ms: int

class AuditSinkInterface:
    def emit(self, event: AuditEvent) -> None:
        raise NotImplementedError("Interface only (public-safe).")
