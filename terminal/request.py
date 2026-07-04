# Creates a request object to send to the cloud.
def create_request(prompt, context):
    return {"prompt": prompt, "context": context}