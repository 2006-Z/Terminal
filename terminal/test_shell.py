# Testing.

from .shell import start, close, send, receive
from .protocol import COMMAND_END_MARKER

shell = start()
command = "pwd"
send(shell, f"{command} && echo {COMMAND_END_MARKER}")
print(receive(shell))

close(shell)