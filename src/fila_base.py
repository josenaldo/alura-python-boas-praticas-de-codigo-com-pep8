from abc import abstractmethod, ABC
from typing import Dict, Any, List

from estatistica import Estatistica
from src.constantes import TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO


class FilaBase(ABC):
    """Fila base"""

    def __init__(self):
        self.__fila: List[str] = []
        self.__clientes_atendidos: List[str] = []
        self._codigo: int = TAMANHO_PADRAO_MINIMO
        self._ultima_senha_gerada: str = ""
        self.__cliente_atual: str = ""

    @property
    def tamanho(self) -> int:
        return len(self.__fila)

    @property
    def cliente_atual(self) -> str:
        return self.__cliente_atual

    @abstractmethod
    def _obtem_prefixo(self) -> str:
        pass

    def _usa_codigo(self) -> int:
        cod: int = self._codigo
        self._codigo += 1
        return cod

    def _gera_senha_atual(self) -> None:
        prefixo = self._obtem_prefixo()
        codigo = self._usa_codigo()
        self._ultima_senha_gerada = f"{prefixo}{codigo}"

    def _reseta_fila(self) -> None:
        if self._codigo >= TAMANHO_PADRAO_MAXIMO:
            self._codigo = TAMANHO_PADRAO_MINIMO

    def atualiza_fila(self) -> None:
        self._reseta_fila()
        self._gera_senha_atual()
        self.__fila.append(self._ultima_senha_gerada)

    def chama_cliente(self, caixa: int) -> str:
        self.__cliente_atual = self.__fila.pop(0)
        self.__clientes_atendidos.append(self.__cliente_atual)
        return (f"Cliente atual: {self.__cliente_atual}, "
                f"dirija-se ao caixa: {caixa}")

    def estatistica(self, estatistica: Estatistica) -> Dict[str, Any]:
        return estatistica.gera_estatistica(self.__clientes_atendidos)
