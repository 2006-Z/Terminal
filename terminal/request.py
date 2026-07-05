# Creates requests for the cloud.

from system import SYSTEM_PROMPT

def create_request(prompt, context):
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]