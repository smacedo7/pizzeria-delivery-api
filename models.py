from sqlalchemy import create_engine, String, Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType


# data base connection 
db = create_engine("sqlite:///banco.db")

# data base basis
Base = declarative_base()

# create the tables/classes
# order
# OrderItens

# users table


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin


# Order table: 

class Order(Base):
    __tablename__ = "orders"

    # ORDER_STATUS = (
    #     ("PENDING", "PENDING"),
    #     ("CANCELED", "CANCELED"),
    #     ("FINISHED", "FINISHED")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user = Column("user", ForeignKey("users.id"))
    status = Column("status", String)
    price = Column("price", Float)

    def __init__(
            self,
            user: User,
            price=0,
            status="Pending"
    ) -> None:
        self.user = user
        self.price = price
        self.status = status


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unit_price = Column("unit_price", Float)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self, quantity, flavor, size, unit_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price
        self.order = order

# execute the creation of the datas of your data base
