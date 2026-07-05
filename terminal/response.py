# Decodes AI responses.

import json

def decode(response):
    content = response.choices[0].message.content
    return json.loads(content)