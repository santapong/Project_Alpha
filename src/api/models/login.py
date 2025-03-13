from pydantic import BaseModel, Field, field_validator

class LoginModel(BaseModel):
    
    username: str
    password: str