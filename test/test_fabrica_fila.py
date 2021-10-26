import pytest

from src.fabrica_fila import FabricaFila
from src.fila_normal import FilaNormal
from src.fila_prioritaria import FilaPrioritaria


class TestFabricaFila:

    def test_deve_retornar_uma_fila_normal_se_o_tipo_for_normal(
            self):
        fila = FabricaFila.pega_fila('normal')
        assert isinstance(fila, FilaNormal)

    def test_deve_retornar_uma_fila_prioritaria_se_o_tipo_for_prioritaria(
            self):
        fila = FabricaFila.pega_fila('prioritaria')
        assert isinstance(fila, FilaPrioritaria)

    def test_deve_lancar_um_erro_se_nenhum_tipo_de_fila_for_especificado(
            self):

        with pytest.raises(NotImplementedError):
            FabricaFila.pega_fila(None)

    def test_deve_lancar_um_erro_se_o_tipo_de_fila_nao_for_conhecido(
            self):

        with pytest.raises(NotImplementedError):
            FabricaFila.pega_fila('fila_desconhecida')
