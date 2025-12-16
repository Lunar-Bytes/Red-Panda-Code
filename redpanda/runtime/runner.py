import re
from redpanda.engine.game import Game

def run_rpc(code: str):
    # Convert shorthand math like 5x → 5 * x
    code = code.replace(" ", "")
    code = re.sub(r"(\d)([a-zA-Z_]\w*)", r"\1*\2", code)

    # Create the global environment
    exec_globals = {'game': Game()}

    # For convenience, allow 'player = game.player'
    exec_globals['player'] = exec_globals['game'].player

    # Execute the code
    exec(code, exec_globals)
