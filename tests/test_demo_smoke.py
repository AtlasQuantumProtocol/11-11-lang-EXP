from elevenlang.parser_stub import parse_source
from elevenlang.ir_stub import lower_to_ir
from elevenlang.runtime_stub import run_ir

def test_demo_pipeline_smoke():
    src = "print hello\nprint world\n"
    ast = parse_source(src)
    ir = lower_to_ir(ast)
    out = run_ir(ir)
    assert "hello" in out and "world" in out
