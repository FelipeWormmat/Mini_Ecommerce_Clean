from src.domain.addres.model import Addresses
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class AddressesRepository(SqlAlchemyRepository[Addresses]):
  pass