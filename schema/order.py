from typing import Union
from enum import Enum
from pydantic import BaseModel
from decimal import Decimal
from schema.customer import Customer

from schema.product import Product

#Adding status to the order entity
class OrderStatus(str, Enum):
    Pending = "Pending"
    In_progress = "In_progress"
    Completed = "Completed"

    print (OrderStatus.Completed.value)

    stat = OrderStatus.Completed.value

class Order(BaseModel):
    id: int
    customer_id: Union[int, Customer]
    items: list[int | Product]
    status: str = OrderStatus.Pending.value


class OrderCreate(BaseModel):
    customer_id: int
    items: list[int | Product]

orders: list[Order] = [
    Order(id=1, customer_id=1, items=[1, 2])
]