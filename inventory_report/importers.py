from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        """
        Importa os dados do arquivo para uma lista de produtos.

        Args:
            path: Caminho do arquivo.

        Returns:
            Lista de produtos.
        """
        pass


class JsonImporter(Importer):

    def import_data(self) -> list[Product]:
        """
        Importa os dados do arquivo JSON para uma lista de produtos.

        Args:
            path: Caminho do arquivo.

        Returns:
            Lista de produtos.
        """

        with open(self.path, "r") as file:
            data = json.load(file)

        products = []
        for item in data:
            product = Product(
                id=item["id"],
                product_name=item["product_name"],
                company_name=item["company_name"],
                manufacturing_date=item["manufacturing_date"],
                expiration_date=item["expiration_date"],
                serial_number=item["serial_number"],
                storage_instructions=item["storage_instructions"],
            )
            products.append(product)

        return products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
