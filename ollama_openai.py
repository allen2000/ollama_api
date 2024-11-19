from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

response = client.chat.completions.create(
  model="qwen2.5:7b-instruct-q8_0",
  messages=[
    {"role": "system", "content": "你是一名资深的日语老师"},
    {"role": "user", "content": "用比较地道的日语来形容饭菜非常好吃"}
  ]
)
print(response.choices[0].message.content)