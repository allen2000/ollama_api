import ollama
response = ollama.chat(model='qwen2.5:7b-instruct-q8_0', messages=[
  {
    'role': 'user',
    'content': '范德彪是谁？',
  },
])
print(response['message']['content'])