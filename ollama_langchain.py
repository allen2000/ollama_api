from langchain_ollama.llms import OllamaLLM
ollama = OllamaLLM(
    base_url='http://localhost:11434',
    model="qwen2.5:7b-instruct-q8_0"
)
print(ollama.invoke("为什么天空是蓝色的？"))