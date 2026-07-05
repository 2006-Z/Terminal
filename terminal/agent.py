# Starts and ends the session.

from shell import start, close
from loop import session_loop

def run(prompt):
    shell = None
    try:
        shell = start()
        session_loop(shell, prompt)

    finally:
        if shell:
            close(shell)