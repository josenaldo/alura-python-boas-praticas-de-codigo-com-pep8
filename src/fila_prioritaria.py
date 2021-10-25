from src.fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    """Representa uma fila normal"""

    def gera_senha_atual(self) -> None:
        self._senha_atual = f"PR{self._codigo}"
