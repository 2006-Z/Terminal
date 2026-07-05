# Takes user input and passes it to the agent.

import sys
from parser import parse
from dashboard import dashboard
from agent import run

def main():

    if len(sys.argv) < 2:
        dashboard()
        return

    prompt = parse(sys.argv[1:])
    run(prompt)

if __name__ == "__main__":
    main()