from datetime import datetime

class Coupon:
    def __init__(
        self, code: str, expire_at: datetime, limit: int, type: str, value: float
    ) -> None:
        self.code = code
        self.expire_at = expire_at
        self.limit = limit
        self.type = type
        self.value = value