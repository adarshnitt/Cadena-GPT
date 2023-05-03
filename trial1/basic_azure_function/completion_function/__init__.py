#It will complete a text given by user input or comment on it.
import logging

import azure.functions as func
import openai

api_key2="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"
api_key3="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"
"""
user__body={"model":"text-davinci-003", "promt":"Tell me which technology is better either Blockchain or Artificial Intelligence ",  "max_tokens":200, "temperature":1 }
"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # give openai our secret key
    openai.api_key=api_key3
    
    # get varibale from http request body
    req_body=req.get_json()

    # call the openai api
    output=openai.Completion.create(
        model=req_body["model"],
        prompt=req_body["promt"],
        max_tokens=req_body["max_tokens"],
        temperature=req_body["temperature"]
    )
    output_response=output["choices"][0]["text"]
    return func.HttpResponse(output_response,status_code=200 )
