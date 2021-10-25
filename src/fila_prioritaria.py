from src.fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    """ Representa uma fila de atendimento para clientes que necessitam de prioridade """

    TAMANHO_MAXIMO_DA_FILA = 200

    def gera_senha_atual(self) -> None:
        self._senha_atual = f"PR{self._codigo}"

    def _tamanho_maximo_da_fila(self) -> int:
        return FilaPrioritaria.TAMANHO_MAXIMO_DA_FILA
