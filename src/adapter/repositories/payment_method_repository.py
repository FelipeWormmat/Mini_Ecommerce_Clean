from src.domain.payment_method.model import PaymentMethod
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class PaymentMethodRepository(SqlAlchemyRepository[PaymentMethod]):
    pass