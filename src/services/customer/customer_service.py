from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.domain.customer.model import Customer
from src.domain.addres.model import Addresses
from src.services.exceptions import CustomerNotFound
from src.services.customer.customer_dto import CustomerDTO
from src.services.address.address_dto import AddressDTO


def create_customer(customer_dto: CustomerDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer = Customer(
            first_name=customer_dto.first_name,
            last_name=customer_dto.last_name,
            phone_number=customer_dto.phone_number,
            genre=customer_dto.genre,
            document_id=customer_dto.document_id,
            birth_date=customer_dto.birth_date,
        )
        uow.category_repository.add(customer)
        uow.commit()


def create_address(address_dto: AddressDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer = uow.customer_repository.get(id=address_dto.customer_id)
        if not customer:
            raise CustomerNotFound("Produto não encontrado")

        addresses = Addresses(
            address=address_dto.address,
            city=address_dto.city,
            state=address_dto.state,
            number=address_dto.number,
            zipcode=address_dto.zipcode,
            neighbourhood=address_dto.neighbourhood,
            primary=address_dto.primary,
        )
        customer.add_address(addresses)
        uow.commit()