from dataclasses import dataclass
from datetime import date
from dataclasses import dataclass

@dataclass
class OrderDTO:
    number : str
    status : str
    customer_id : int
    created_at : date
    address_id : int
    total_value : float
    payment_methods_id : int
    total_discount : float