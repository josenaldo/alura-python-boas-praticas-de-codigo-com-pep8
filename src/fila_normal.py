from src.fila_base import FilaBase


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self._senha_atual = f"NM{self._codigo}"
