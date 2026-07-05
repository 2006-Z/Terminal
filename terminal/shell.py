# Shell logic.

import subprocess
from protocol import COMMAND_END_MARKER

def start():
    shell = subprocess.Popen(["zsh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    return shell

def send(shell, command):
    shell.stdin.write(command + "\n")
    shell.stdin.flush()

def receive(shell):
    output = []
    while True:
        line = shell.stdout.readline().strip()
        if line == COMMAND_END_MARKER:
            break
        output.append(line)
    return output

def close(shell):
    shell.terminate()
    shell.wait()