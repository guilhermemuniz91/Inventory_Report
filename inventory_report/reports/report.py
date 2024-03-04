from inventory_report.inventory import Inventory
from abc import abstractmethod
from typing import Protocol


class Report(Protocol):

    @abstractmethod
    def add_inventory(self, inventory: Inventory) -> None:
        """
        Adiciona um inventário ao relatório.

        Args:
            inventory: O inventário a ser adicionado.
        """
        pass

    @abstractmethod
    def generate(self) -> str:
        """
        Gera o relatório em formato string.

        Returns:
            String com o conteúdo do relatório.
        """
        pass
