from langchain_ollama.llms import OllamaLLM

input = input("What is your question?")
llm = OllamaLLM(model="qwen2.5:7b-instruct-q8_0")
res = llm.invoke(input)
print (res)