import requests
import json

API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
    #'HTTP-Referer': '<YOUR_SITE_URL>',
    #'X-Title': '<YOUR_SITE_NAME>',
}
def getModelResponse(prompt):
    data = {
        'model': 'deepseek/deepseek-chat:free',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful code reviewer.'},
            {'role': 'user', 'content': prompt}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=data)


    if response.status_code == 200:
        response_json = response.json()
        return response_json['choices'][0]['message']['content']
    else:
        raise Exception(f'Erro {response.status_code}: {response.text}')

def reviewCode(codeSnippet):
    prompt = (
        "Analyze and explain the following Python code:\n\n"
        f"```python\n{codeSnippet}\n```\n\n"
        "Identify potential bugs or improvements, suggest optimizations, and provide alternative implementations if applicable."
    )
    return getModelResponse(prompt)

