import requests
import json

API_KEY = 'sk-3e8c4f05c14d4f879b6e9f6454626f39'
API_URL = 'https://api.deepseek.com/chat/completions'

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def getDeepSeekRessponse(prompt):
    data = {
        'model': 'deepseek-chat',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful code reviewer.'},
            {'role': 'user', 'content': prompt}
        ],
        'stream': False
    }
'''
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()  # Retorna a resposta do DeepSeek
    else:
        raise Exception(f'Erro {response.status_code}: {response.text}')
'''
    response = response.post(API_URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
    else:
        raise Exception(f'Erro {response.status_code}: {response.text}')

def reviewCode(codeSnippet):
    prompt = f"""
    Code Snippet:
    {codeSnippet}
    
    Task: Analyze the provided code snippet. 
    Identify potential bugs or improvements, suggest optimizations, and provide alternative implementations if applicable.
    """
    return getDeepSeekRessponse(prompt)