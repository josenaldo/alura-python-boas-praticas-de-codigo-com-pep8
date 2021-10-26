from src.constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from src.fila_normal import FilaNormal
from src.fila_prioritaria import FilaPrioritaria


class FabricaFila:
    """Representa uma fábrica de filas"""

    @staticmethod
    def pega_fila(tipo_fila):
        """Retorna uma fila de acordo com o tipo"""
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')
