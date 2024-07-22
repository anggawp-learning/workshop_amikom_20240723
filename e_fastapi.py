from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

class User_input(BaseModel):
	operation : str
	x : str
	y : str

app = FastAPI()

@app.get("/")
def root():
    return {'message':'This is Calculator API'}

@app.post("/calculate")
def operate(input:User_input):
	result = calculate(input.operation, input.x, input.y)
	return result