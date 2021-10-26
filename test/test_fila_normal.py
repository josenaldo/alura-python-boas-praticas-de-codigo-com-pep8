from typing import Dict, Any

import pytest

from estatistica import EstatisticaDetalhada, EstatisticaResumida
from src.constantes import (
    CODIGO_NORMAL,
    TAMANHO_PADRAO_MINIMO,
    TAMANHO_PADRAO_MAXIMO,
)
from src.fila_normal import FilaNormal


class TestFilaNormal:

    @pytest.fixture
    def fila(self):
        return FilaNormal()

    def test_deve_ser_criada_com_tamanho_inicial_0(self, fila):
        assert fila.tamanho == 0

    def test_deve_ter_tamanho_1_quando_adicionado_um_elemento(self, fila):
        fila.atualiza_fila()
        assert fila.tamanho == 1

    def test_devendo_ter_tamanho_2_quando_adicionados_dois_elementos(
            self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        assert fila.tamanho == 2

    def test_deve_reciclar_senhas_apos_o_numero_maximo_de_senhas_ser_atingido(
            self, fila):
        senha: str = ""
        ultimo_caixa: int = 0

        for i in range(TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO + 1):
            fila.atualiza_fila()
            senha = fila.chama_cliente(i)
            ultimo_caixa = i

        assert senha == (f"Cliente atual: {fila.cliente_atual}, "
                         f"dirija-se ao caixa: {ultimo_caixa}")

    def test_deve_chamar_1_cliente_com_primeira_senha_da_fila(
            self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        chamado = fila.chama_cliente(10)

        assert chamado == f"Cliente atual: {fila.cliente_atual}, " \
                          f"dirija-se ao caixa: 10"

    def test_deve_chamar_2_clientes_com_as_duas_primeiras_senhas_da_fila(
            self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        chamado1 = fila.chama_cliente(10)
        cliente_atual_1: str = fila.cliente_atual

        chamado2 = fila.chama_cliente(1)
        cliente_atual_2: str = fila.cliente_atual

        assert chamado1 == (f"Cliente atual: {cliente_atual_1}, "
                            f"dirija-se ao caixa: 10")

        assert chamado2 == (f"Cliente atual: {cliente_atual_2}, "
                            f"dirija-se ao caixa: 1")

    def test_deve_ter_tamanho_0_quando_todos_os_clientes_foram_atendidos(
            self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        assert fila.tamanho == 0

    def test_deve_mostrar_estatisticas_detalhadas(self, fila: FilaNormal):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        estatistica_detalhada = EstatisticaDetalhada("10/01/1993", 198)
        estatisticas = fila.estatistica(estatistica_detalhada)

        estatisticas_esperada: Dict[str, Any] = {
            "dia": "10/01/1993",
            "agencia": 198,
            "clientes_atendidos": [
                f"{CODIGO_NORMAL}{TAMANHO_PADRAO_MINIMO}",
                f"{CODIGO_NORMAL}{TAMANHO_PADRAO_MINIMO + 1}",
                f"{CODIGO_NORMAL}{TAMANHO_PADRAO_MINIMO + 2}"
            ],
            "quantidade_clientes_atendidos": 3,
        }

        assert estatisticas == estatisticas_esperada

    def test_deve_mostrar_estatisticas_resumidas(self, fila: FilaNormal):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        estatistica_resumida = EstatisticaResumida("10/01/1993", 198)
        estatisticas = fila.estatistica(estatistica_resumida)

        estatistica_esperada = {"198-10/01/1993": 3}

        assert estatisticas == estatistica_esperada
