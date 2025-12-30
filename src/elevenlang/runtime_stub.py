def run_ir(ir):
    """
    Toy runtime: executes a tiny set of ops for demo purposes.
    """
    out = []
    for op in ir:
        if op[0] == "PRINT":
            out.append(op[1])
        else:
            # NOOP — in real implementation this would be meaningful.
            pass
    return "\n".join(out)
