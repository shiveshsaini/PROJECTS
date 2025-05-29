import openai

client = openai.OpenAI(
    api_key="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"
    )

response = client.chat.completions.create(
    model="gpt-3.5-turbo",      
    messages=[
        {"role": "system","content": "You are a Virtual Assistant named jarvis skilled in general tasks like Alexa and Google Cloud"}, 
        {"role":"user","content": "what is coding."}
    ]
)

print(response.choices[0].message.content)
