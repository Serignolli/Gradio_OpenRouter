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
    data = json.dumps({
        'model': 'deepseek/deepseek-chat:free',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful code reviewer.'},
            {'role': 'user', 'content': prompt}
        ]
    })

    print(json.dumps({
        'model': 'deepseek/deepseek-chat:free',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful code reviewer.'},
            {'role': 'user', 'content': prompt}
        ]
    }, indent=2))

    print("\n🔍 DEBUG: JSON Payload being sent:")
    print(json.dumps(data, indent=2))  # Exibe o JSON formatado

    response = requests.post(API_URL, headers=HEADERS, json=data)

    print("\n📩 DEBUG: Response Status Code:", response.status_code)

    try:
        response_json = response.json()
        print("\n📩 DEBUG: Response JSON:")
        print(json.dumps(response_json, indent=2))  # Exibe a resposta formatada
        return response_json
    except json.JSONDecodeError:
        print("\n❌ ERROR: Response is not a valid JSON.")
        print(response.text)  # Se não for JSON, imprime o texto bruto
        raise
    '''
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))


    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Erro {response.status_code}: {response.text}')
'''
def reviewCode(codeSnippet):
    prompt = (
        "Analyze and explain the following Python code:\n\n"
        f"```python\n{codeSnippet}\n```\n\n"
        "Identify potential bugs or improvements, suggest optimizations, and provide alternative implementations if applicable."
    )
    return getModelResponse(prompt)

