from pydantic import BaseModel, Field, validator

class caloriesSchema(BaseModel):
    age: float = Field(..., description='Age in years')
    gender: str = Field(..., description='Gender')