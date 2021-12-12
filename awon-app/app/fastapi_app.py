import uvicorn
from typing import Union
from fastapi import FastAPI
from findArea import find_area
from pydantic import (BaseModel, PositiveFloat, PositiveInt)

# Instantiate fastapi object
app = FastAPI()

# Set class for data validation check (from pydantic BaseModel)
class Area(BaseModel):
    # Set "length" and "width" to either positive float or positive int only
    length: Union[PositiveFloat, PositiveInt]
    width: Union[PositiveFloat, PositiveInt]

# Create post request to get data from client
@app.post('/')
def access_acre(calculate: Area): # assign "Area" to the variable "calculate"
    """
    The function takes the arguments from "Area" and assign them to the "find_area" function to process.
    """
    result = find_area(calculate.length, calculate.width)
    return {"Total field in acre": round(result, 2)}

if __name__ == "__main__":
    uvicorn.run()