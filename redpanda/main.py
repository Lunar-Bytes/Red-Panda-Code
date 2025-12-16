import os
from redpanda.runtime.runner import run_rpc

# Compute path relative to this file
rpc_path = os.path.join(os.path.dirname(__file__), "examples", "syntax.rpc")

with open(rpc_path) as f:
    code = f.read()

run_rpc(code)
