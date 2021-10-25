from src.fila_base import FilaBase


class FilaNormal(FilaBase):
    """ Representa uma fila de atendimento normal """

    TAMANHO_MAXIMO_DA_FILA = 200

    def gera_senha_atual(self) -> None:
        self._senha_atual = f"NM{self._codigo}"

    def _tamanho_maximo_da_fila(self) -> int:
        return FilaNormal.TAMANHO_MAXIMO_DA_FILA
