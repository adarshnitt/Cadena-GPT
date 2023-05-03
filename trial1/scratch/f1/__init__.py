import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    
    return func.HttpResponse(f"Hello basic code run successfullly...",status_code=200)
    
