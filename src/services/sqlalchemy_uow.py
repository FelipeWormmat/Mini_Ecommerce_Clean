from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.addres_repository import AddressesRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.adapter.repositories.customer_repository import CustomersRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.product_discount_repository import ProductDiscountsRepository
from src.adapter.repositories.order_repository import OrderRepository
from src.domain.addres.model import Addresses
from src.domain.category.model import Category
from src.domain.coupon.model import Coupon
from src.domain.customer.model import Customer
from src.domain.product_discount.model import ProductDiscount
from src.domain.supplier.model import Supplier
from src.domain.payment_method.model import PaymentMethod
from src.domain.product.model import Product
from src.domain.order.model import Order
from src.adapter.database import Session


class SqlAlchemyUnitOfWork:
    def __init__(self):
        self.session = Session()

    def __enter__(self):
        self.payment_method_repository = PaymentMethodRepository(
            self.session, PaymentMethod)
        self.category_repository = CategoryRepository(self.session, Category)
        self.supplier_repository = SupplierRepository(self.session, Supplier)
        self.product_repository = ProductRepository(self.session, Product)
        self.addresses_repository = AddressesRepository(self.session, Addresses)
        self.coupons_repository = CouponRepository(self.session, Coupon)
        self.customers_repository = CustomersRepository(self.session, Customer)
        self.payment_methods_repository = PaymentMethodRepository(self.session, PaymentMethod)
        self.product_discounts_repository = ProductDiscountsRepository(self.session, ProductDiscount)
        self.order_repository = OrderRepository(self.session, Order)

    def __exit__(self, *args):
        self.session.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()