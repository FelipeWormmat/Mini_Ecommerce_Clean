from dataclasses import dataclass
from datetime import date

@dataclass
class CustomerDTO:
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date