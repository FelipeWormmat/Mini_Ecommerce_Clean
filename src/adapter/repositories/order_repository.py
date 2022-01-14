from src.domain.order.model import Order
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository

class OrderRepository(SqlAlchemyRepository[Order]):
  pass