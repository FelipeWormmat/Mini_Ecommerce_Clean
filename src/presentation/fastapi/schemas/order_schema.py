from datetime import date
from pydantic import BaseModel

class CreateOrderSchema(BaseModel):
    number : str
    status : str
    customer_id : int
    created_at : date
    address_id : int
    total_value : float
    payment_methods_id : int
    total_discount : float