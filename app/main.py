import os
import pickle
import uvicorn
import logging
import pandas as pd
from dotenv import load_dotenv
from routers.predictor import Predictor
from fastapi import FastAPI,Request,APIRouter,Body
import json

load_dotenv() 
app = FastAPI()
router = APIRouter()
logging.basicConfig(filename=(os.getenv('LOG_FILE')), encoding='utf-8', level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d | %(message)s')


@app.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/analize/")
async def analize(str = Body()):
    result = oAnalize.analyze_packet(clf, clfrf, modelmlp, gnb, modelgb, clf_knn, str)
    return result

app.include_router(router)
if __name__ == "__main__":
    logging.debug("Loading models")
    with open(os.getenv('DT'), 'rb') as file:  
        clf = pickle.load(file)
    with open(os.getenv('RF'), 'rb') as file:  
        clfrf = pickle.load(file)
    with open(os.getenv('MLP'), 'rb') as file:  
        modelmlp = pickle.load(file)
    with open(os.getenv('NB'), 'rb') as file:  
        gnb = pickle.load(file)
    with open(os.getenv('GB'), 'rb') as file:  
        modelgb = pickle.load(file)
    with open(os.getenv('KNN'), 'rb') as file:  
        clf_knn = pickle.load(file)   
    logging.debug("Models loaded")
    logging.debug("Creating Predictor object")
    oAnalize = Predictor()
    logging.debug("Created Predictor object")
    uvicorn.run(app, host="127.0.0.1", port=8000)