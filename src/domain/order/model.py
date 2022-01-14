class Order:
    def __init__(self, number, status, customer_id, created_at, address_id, total_value, payment_methods_id, total_discount) -> None:
        self.number = number
        self.status = status
        self.customer_id = customer_id
        self.created_at = created_at
        self.address_id = address_id
        self.total_value = total_value
        self.payment_methods_id = payment_methods_id
        self.total_discount = total_discount