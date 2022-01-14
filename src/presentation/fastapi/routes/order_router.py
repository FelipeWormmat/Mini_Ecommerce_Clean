from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.order_schema import CreateOrderSchema
from src.services.order.order_dto import OrderDTO
from src.services.order.order_service import create_order
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateOrderSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = OrderDTO(**schema.dict())
  
  order = create_order(dto, uow=uow)

  return order