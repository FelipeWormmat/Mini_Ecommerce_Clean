from dataclasses import dataclass

@dataclass
class PaymentMethodDTO:
    name: str
    enabled: bool