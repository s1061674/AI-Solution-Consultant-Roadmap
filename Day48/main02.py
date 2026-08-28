from dataclasses import dataclass
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

@dataclass
class Order:
    product: str
    status: OrderStatus

    def ship(self) -> None:
        self.status = OrderStatus.SHIPPED

    def get_status_message(self) -> str:
        match self.status:

            case OrderStatus.PENDING:
                return "等待出貨"

            case OrderStatus.SHIPPED:
                return "已出貨"

            case OrderStatus.DELIVERED:
                return "已送達"

order = Order("Keyboard", OrderStatus.PENDING)

print(order.get_status_message())

order.ship()

print(order.get_status_message())