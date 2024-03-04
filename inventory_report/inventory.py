from inventory_report.product import Product
from typing import Optional


class Inventory:

    def __init__(self, data: Optional[list[Product]] = None):
        self._data = [] if data is None else data

    @property
    def data(self) -> list[Product]:
        return self._data

    def add_data(self, data: list[Product]):
        self._data.extend(data)
