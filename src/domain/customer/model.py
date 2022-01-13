from datetime import date
from typing import List
from src.domain.addres.model import Addresses


class Customer:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        phone_number: str,
        genre: str,
        document_id: str,
        birth_date: date,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.document_id = document_id
        self.birth_date = birth_date
        self.address: List[Addresses] = []

    def add_address(self, address: Addresses):
        if address.primary:
            filter_primary = list(filter(lambda p: p.primary == True, self.address))

            if len(filter_primary) > 0:
                filter_primary[0].primary = False

        self.address.append(address)