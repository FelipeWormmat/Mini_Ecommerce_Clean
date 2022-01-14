from src.domain.order.model import Order
from src.services.order.order_dto import OrderDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

def create_order(orderDTO: OrderDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        address = uow.addresses_repository.get(id=orderDTO.address_id)
        if not address:
            raise Exception()
        payment_method = uow.payment_methods_repository.get(id=orderDTO.payment_methods_id)
        if not payment_method or payment_method.enabled == False:
            raise Exception()
        uow.order_repository.add(Order(**orderDTO.__dict__))
        uow.commit()