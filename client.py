from openai import OpenAI
client = OpenAI(
    api_key="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")

    


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful  VIRTUAL assistant named JARVIS like alexa."},
        {
            "role": "user",
            "content": "what is coding"
        }
    ]
)

print(completion.choices[0].message)


