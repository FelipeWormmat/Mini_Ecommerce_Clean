from pydantic import BaseModel

class CreatePaymentMethodSchema(BaseModel):
    name: str
    enabled: bool