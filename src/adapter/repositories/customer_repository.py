from src.domain.customer.model import Customers
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CustomersRepository(SqlAlchemyRepository[Customers]):
  pass