def lower_to_ir(program):
    """
    Public-safe IR stub:
    Converts statements into a toy intermediate representation (list of ops).
    This is not the proprietary 11/11 IR.
    """
    ir = []
    for stmt in program.statements:
        if stmt.lower().startswith("print "):
            ir.append(("PRINT", stmt[6:].strip()))
        else:
            ir.append(("NOOP", stmt))
    return ir
