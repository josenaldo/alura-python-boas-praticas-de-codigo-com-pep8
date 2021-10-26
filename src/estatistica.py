from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Estatistica(ABC):
    def __init__(self, dia: str, agencia: int) -> None:
        self.__dia = dia
        self.__agencia = agencia

    @property
    def dia(self):
        return self.__dia

    @property
    def agencia(self):
        return self.__agencia

    @abstractmethod
    def gera_estatistica(
            self, clientes_atendidos: List[str]) -> Dict[str, Any]:
        pass


class EstatisticaDetalhada(Estatistica):

    def gera_estatistica(
            self, clientes_atendidos: List[str]) -> Dict[str, Any]:
        estatistica: Dict[str, Any] = {}
        estatistica["dia"] = self.dia
        estatistica["agencia"] = self.agencia
        estatistica["clientes_atendidos"] = clientes_atendidos
        estatistica["quantidade_clientes_atendidos"] = len(clientes_atendidos)

        return estatistica


class EstatisticaResumida(Estatistica):

    def gera_estatistica(self, clientes_atendidos: list) -> Dict[str, Any]:
        estatistica: Dict[str, Any] = {}
        chave: str = f"{self.agencia}-{self.dia}"
        estatistica[chave] = len(clientes_atendidos)

        return estatistica
