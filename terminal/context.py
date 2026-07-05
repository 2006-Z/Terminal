# Collects context.

import os

def collect(*context):
    if len(context) > 0:
        pass
    return {
        "pwd": os.getcwd(),
        "OS": os.name,
        "Shell": os.getenv("SHELL")
    }