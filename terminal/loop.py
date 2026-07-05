# Runs the AI execution loop.

from context import collect
from request import create_request
from cloud import send
from response import decode
from display import show

def session_loop(shell, prompt):
    step = 1
    while step != 0:
        context = collect()
        request = create_request(prompt, context)
        response = send(request)
        response = decode(response)
        step = response["step"]
    show(response)