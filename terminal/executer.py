# Executes commands list.

from .protocol import MAX_COMMANDS_PER_STEP

def execute(commands):
    if len(commands) > MAX_COMMANDS_PER_STEP:
        raise Exception("Too many commands provided")
    results = []
    for command in commands:
        pass
    return results