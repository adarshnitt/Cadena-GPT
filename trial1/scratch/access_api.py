api_key1="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"
api_key2="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"



user_query="tell me a love quote for swati"
import openai
openai.api_key=api_key2

output=openai.Completion.create(
    model="text-davinci-003",
    prompt=user_query,
    max_tokens=200,
    temperature=1
)

print("output is ---- ",output["choices"][0]["text"][3:])