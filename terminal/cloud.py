# Sends requests to the cloud.

from openai import OpenAI

client = OpenAI(api_key=API_KEY, base_url="https://aicredits.in/v1")

def send(request):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=request
    )

    return response