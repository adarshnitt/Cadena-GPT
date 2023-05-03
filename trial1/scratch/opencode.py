# task: text completion using openai
# kinldy install "pip install openai"

import openai
api_key3="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"
openai.api_key=api_key3
req_body={"model":"text-davinci-003",
          "promt":"write a love letter for boy name adarsh who is just completing his btech",
          "max_tokens":100,
          "temperature":1}
    # temperature: randomness, max_tokens: # word output 
# call the openai api
output=openai.Completion.create(
        model=req_body["model"],
        prompt=req_body["promt"],
        max_tokens=req_body["max_tokens"],
        temperature=req_body["temperature"]
    )
output_response=output["choices"][0]["text"]
print(output_response)