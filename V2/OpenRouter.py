import requests
import json

API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
    #Preencher para a divulgação do site no openRouter
    #'HTTP-Referer': '<YOUR_SITE_URL>',
    #'X-Title': '<YOUR_SITE_NAME>',
}
def getModelResponse(prompt):
    data = json.dumps({
        'model': 'deepseek/deepseek-chat:free',
        'messages': [
            {
                {'role': 'system', 'content': 'You are a helpful code reviewer.'},
                {'role': 'user', 'content': prompt}
            }
        ]
    })

    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
    else:
        raise Exception(f'Erro {response.status_code}: {response.text}')

def reviewCode(codeSnippet, language):
    prompt = f"""
    Analyze and explain the following {language}
    Code Snippet:
    {codeSnippet}

    Explain and identify potential bugs or improvements, suggest optimizations, and provide alternative implementations if applicable.
    """
    return getModelResponse(prompt)