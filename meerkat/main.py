from fastapi import FastAPI



from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)



from fastapi import FastAPI, Header, File, UploadFile, HTTPException
from pydantic import BaseModel
import csv
from random import randint
from time import sleep
import pandas as pd 
from prometheus_client import start_http_server, Counter, Histogram



app = FastAPI()
start_http_server(8000)
metrics_counter = Counter('contact_sort_counter', 'Counter for the number of POST requests to contact-sort')



    
