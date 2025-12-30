from .ast import Program

def parse_source(source: str) -> Program:
    """
    Public-safe parser stub:
    - Demonstrates pipeline structure
    - Does NOT implement proprietary language parsing
    """
    lines = [ln.strip() for ln in source.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    return Program(statements=lines)
