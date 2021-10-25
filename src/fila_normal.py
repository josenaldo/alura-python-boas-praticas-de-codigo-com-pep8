from src.fila_base import FilaBase
from src.constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    """ Representa uma fila de atendimento normal """

    def _obtem_prefixo(self) -> str:
        """ Retorna o prefixo da fila """

        return CODIGO_NORMAL
