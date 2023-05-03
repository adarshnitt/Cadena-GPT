#It will complete a text given by user input or comment on it.
import logging

import azure.functions as func
import openai

api_key2="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"
api_key3="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"
"""
user__body={"model":"text-davinci-003", "promt":"what is earth ",  "max_tokens":200, "temperature":1 }

"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # give openai our secret key
    openai.api_key=api_key3
    
    # get varibale from http request body
    req_body=req.get_json()  # {"model":"text-davinci-003", "promt":"what is earth ",  "max_tokens":200, "temperature":1 }#req.get_json()

    # call the openai api
    output=openai.Completion.create(
        model=req_body["model"],
        prompt=req_body["promt"],
        max_tokens=req_body["max_tokens"],
        temperature=req_body["temperature"]
    )
    output_response=output["choices"][0]["text"]
    print(output_response)
    return func.HttpResponse(output_response,status_code=200 )
print("file is running...")