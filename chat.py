from openai import OpenAI

client = OpenAI(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)

print(chat_completion)