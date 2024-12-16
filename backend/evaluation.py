import requests

def call_api(prompt, input_text):
    api_url = "https://example.com/api"  # Replace with actual API URL
    payload = {
        "prompt": prompt,
        "input": input_text
    }
    response = requests.post(api_url, json=payload)
    return response.json()
