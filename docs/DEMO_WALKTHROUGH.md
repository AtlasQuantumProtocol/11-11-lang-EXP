 Demo Walkthrough

This walkthrough shows how to run the public demo.

 Install
python -m venv .venv
source .venv/bin/activate
pip install -e .

 Run a demo program
elevenlang demo src/demo/examples/hello.111

 What happens
1) The demo reads the `.111` file
2) The parser stub creates a Program object
3) The IR stub converts it into a toy IR
4) The runtime executes the toy IR
5) Output is printed

 Why this matters
This demonstrates:
- how language pipelines are structured
- where security boundaries should live
- how audit and governance attach cleanly

This repo is intentionally public-safe and non-production.
