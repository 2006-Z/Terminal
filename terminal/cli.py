import sys

from parser import parse
from display import show
from context import collect
from dashboard import dashboard
from request import create_request
from cloud import send

def main():

    if len(sys.argv) < 2:
        dashboard()
        return

    prompt = parse(sys.argv[1:])
    context = collect()

    request = create_request(prompt, context)
    response = send(request)

    show(f"Prompt: {prompt}")
    show(f"Current Directory : {context['cwd']}")
    show(f"Response: {response}")

if __name__ == "__main__":
    main()