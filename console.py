from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.product.model import Product
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.product_discount_repository import ProductDiscountsRepository
from src.adapter.database import Session
from src.adapter.orm import start_mapper

from datetime import datetime


start_mapper()

db = Session()


coupon_repository = CouponRepository(db)
coupon = Coupon('abcde',datetime.now(),10,'percentage',19.00)
coupon_repository.add(coupon)
print(coupon.id)
print(coupon.expire_at)
print(coupon.code)

supplier_repository = SupplierRepository(db)
supplier = Supplier('maicao')
supplier_repository.add(supplier)
print(supplier.name)
print(supplier.id)

category_repository = CategoryRepository(db)
category = Category('alimentos')
category_repository.add(category)
print(category.name)
print(category.id)

payment_methods_repository = PaymentMethodRepository(db)
payment_method = PaymentMethod('cartao', True)
payment_methods_repository.add(payment_method)
print(payment_method.enabled)
print(payment_method.id)

product_repository = ProductRepository(db)
product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True, supplier=supplier, category=category)
product_repository.add(product)
print(product.id)
print(product.description)
print(product.category.id)
print(product.supplier.id)

product_discounts_repository = ProductDiscountsRepository(db)
product_discounts = ProductDiscount(product, 'percentage', 12, payment_method)
product_discounts_repository.add(product_discounts)
print(product_discounts.id)

import pdb
pdb.set_trace()