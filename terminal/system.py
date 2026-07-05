SYSTEM_PROMPT = """{
        "step": "0 if the task is complete, otherwise previous step + 1",
        "commands": ["List of shell commands to execute in order. Maximum 15 commands."],
        "messages": ["Different message to display to the user while executing different command."],
        "permission": ["index no of commands in which user permission is required."],
        "timeout": ["estimated time in seconds for each command to complete."],
        "tools": ["what tools you want to use in next step."],
        "output": "Final message",
        "summary": "Only when step is 0. A highly compressed summary of the entire session."
    }"""