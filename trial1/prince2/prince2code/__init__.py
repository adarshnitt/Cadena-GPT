import logging
import openai
import azure.functions as func

api_key3="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"
api_key4="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"
openai.api_key=api_key3
# {"model":"text-davinci-003", "promt":"Tell me which technology is better either Blockchain or Artificial Intelligence ",  "max_tokens":200, "temperature":1 }

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    
    req_body = req.get_json()
    output=openai.Completion.create(
        model=req_body["model"],
        prompt=req_body["promt"],
        max_tokens=req_body["max_tokens"],
        temperature=req_body["temperature"]
    )
    
    if output:
        output_response=output["choices"][0]["text"]
        return func.HttpResponse(output_response,status_code=200 )
    else:
        return func.HttpResponse("output response is none",status_code=200 )

