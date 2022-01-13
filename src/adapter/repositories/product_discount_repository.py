from src.domain.product_discount.model import ProductDiscount
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class ProductDiscountsRepository(SqlAlchemyRepository[ProductDiscount]):
  pass