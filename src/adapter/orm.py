from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, Numeric, String
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount


metadata = Base.metadata


table_category = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45)),
)

table_supplier = Table(
    "suppliers",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45)),
)

table_product = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("description", String(100)),
    Column("technical_details", String(255)),
    Column("price", Numeric(10, 2)),
    Column("visible", Boolean),
    Column("category_id", ForeignKey("categories.id")),
    Column("supplier_id", ForeignKey("suppliers.id")),
)


table_coupon = Table(
    "coupons",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("code", String(10), unique=True),
    Column("expire_at", DateTime),
    Column("limit", Integer),
    Column("type", String(15)),
    Column("value", Numeric(10, 2)),
)

table_payment_method = Table(
    "payment_methods",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45)),
    Column("enabled", Boolean, default=True),
)


table_product_discount = Table(
    "product_discounts",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("mode", String(45)),
    Column("value", Numeric(10, 2)),
    Column("product_id", ForeignKey("products.id")),
    Column("payment_method_id", ForeignKey("payment_methods.id")),
)


def start_mapper():
    category_mapper = mapper(Category, table_category)
    supplier_mapper = mapper(Supplier, table_supplier)
    payment_method_mapper = mapper(PaymentMethod, table_payment_method)

    product_discount_mapper = mapper(
        ProductDiscount,
        table_product_discount,
        properties={
            "payment_method": payment_method_mapper,
        },
    )

    mapper(
        Product,
        table_product,
        properties={
            "category": relationship(category_mapper),
            "supplier": relationship(supplier_mapper),
            "discounts": relationship(product_discount_mapper),
        },
    )

    mapper(Coupon, table_coupon)