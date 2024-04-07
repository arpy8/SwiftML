import pickle 
import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class Predict(BaseModel):
    values: list

pickle_path = "models/final_dumped_LinearDiscriminantAnalysis.pkl"

app = FastAPI()

@app.get("/")
def read_root():
    return "blep"

@app.post("/predict")
async def predict(values: Predict):
    with open(pickle_path, 'rb') as file:
        params, model = pickle.load(file)
    
    values = values.values
    data = pd.DataFrame([values], columns=params)
    
    prediction = model.predict(data)
    prediction = prediction.tolist()    
    
    return {"prediction": prediction, "model": model.__class__.__name__}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)