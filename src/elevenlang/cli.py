import argparse
from .parser_stub import parse_source
from .ir_stub import lower_to_ir
from .runtime_stub import run_ir

def main():
    p = argparse.ArgumentParser(prog="elevenlang", description="11/11 Language EXP demo CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    demo = sub.add_parser("demo", help="Run a demo .111 program through the stub pipeline")
    demo.add_argument("path", help="Path to .111 file")

    args = p.parse_args()

    if args.cmd == "demo":
        src = open(args.path, "r", encoding="utf-8").read()
        ast = parse_source(src)
        ir = lower_to_ir(ast)
        result = run_ir(ir)
        print(result)

if __name__ == "__main__":
    main()
