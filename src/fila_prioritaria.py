from src.fila_base import FilaBase
from src.constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    """ Representa uma fila de atendimento para clientes que necessitam
    de prioridade
    """

    def _obtem_prefixo(self) -> str:
        """ Retorna o prefixo da fila """

        return CODIGO_PRIORITARIO
