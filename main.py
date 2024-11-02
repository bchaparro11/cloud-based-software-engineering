from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

client = MongoClient(os.getenv("URI"))
db = client[str(os.getenv("DB"))]
col = db[str(os.getenv("COLLECTION"))]

app = FastAPI()

@app.get("/all_contracts")
def all_contracts():
    contracts = list(col.find({},{"_id":0}))
    return contracts

@app.get("/contract_id/{id}")
def contract_id(id = str):
    contract  = list(col.find({"contract_id":id},{"_id":0}))
    return contract

@app.get("/")
def root():
    # print(os.getenv("IS_IT_WORKING"))
    return {"answer":"Hello, my friend"}