from abc import abstractmethod, ABC
from typing import Dict, Any


class FilaBase(ABC):
    """Fila base"""

    def __init__(self):
        self.__fila: list = []
        self.__clientes_atendidos: list = []
        self._codigo: int = 0
        self._senha_atual: str = ""

    @property
    def tamanho(self):
        return len(self.__fila)

    @abstractmethod
    def gera_senha_atual(self) -> None:
        pass

    @abstractmethod
    def _tamanho_maximo_da_fila(self) -> int:
        pass

    def reseta_fila(self) -> None:
        if self._codigo >= self._tamanho_maximo_da_fila():
            self._codigo = 1
        else:
            self._codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.__fila.append(self._senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.__fila.pop(0)
        self.__clientes_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}"

    def estatistica(self, dia: str, agencia: int, flag: str):
        estatistica: Dict[str, Any] = {}

        if flag != "detail":
            estatistica[f"{agencia}-{dia}"] = len(self.__clientes_atendidos)
        else:
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["clientes_atendidos"] = self.__clientes_atendidos
            estatistica["quantidade_clientes_atendidos"] = \
                len(self.__clientes_atendidos)

        return estatistica
