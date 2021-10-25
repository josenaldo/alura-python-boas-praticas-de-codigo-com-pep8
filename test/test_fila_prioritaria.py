from typing import Dict, Any

import pytest

from src.fila_prioritaria import FilaPrioritaria


class TestFilaPrioritaria:

    @pytest.fixture
    def fila(self):
        return FilaPrioritaria()

    def test_fila_prioritaria_deve_ser_criada_com_tamanho_inicial_0(self, fila):
        assert fila.tamanho == 0

    def test_fila_prioritaria_deve_ter_tamanho_1_quando_adicionado_um_elemento(self, fila):
        fila.atualiza_fila()
        assert fila.tamanho == 1

    def test_fila_prioritaria_devendo_ter_tamanho_2_quando_adicionados_dois_elementos(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        assert fila.tamanho == 2

    def test_fila_prioritaria_deve_reciclar_senhas_apos_o_numero_maximo_de_senhas_ser_atingido(self, fila):
        senha = None
        for i in range(0, 101):
            fila.atualiza_fila()
            senha = fila.chama_cliente(i)

        assert senha == "Cliente atual: PR1, dirija-se ao caixa: 100"

    def test_fila_prioritaria_deve_chamar_1_cliente_com_primeira_senha_da_fila(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        chamado = fila.chama_cliente(10)

        assert chamado == "Cliente atual: PR1, dirija-se ao caixa: 10"

    def test_fila_prioritaria_deve_chamar_2_clientes_com_as_duas_primeiras_senhas_da_fila(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        chamado1 = fila.chama_cliente(10)
        chamado2 = fila.chama_cliente(1)

        assert chamado1 == "Cliente atual: PR1, dirija-se ao caixa: 10"
        assert chamado2 == "Cliente atual: PR2, dirija-se ao caixa: 1"

    def test_fila_prioritaria_deve_ter_tamanho_0_quando_todos_os_clientes_foram_atendidos(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        assert fila.tamanho == 0

    def test_fila_prioritaria_deve_mostrar_estatisticas_detalhadas(self, fila: FilaPrioritaria):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        estatisticas = fila.estatistica("10/01/1993", 198, "detail")

        estatistica_esperada: Dict[str, Any] = {
            "dia": "10/01/1993",
            "agencia": 198,
            "clientes_atendidos": ["PR1", "PR2", "PR3"],
            "quantidade_clientes_atendidos": 3,
        }

        assert estatisticas == estatistica_esperada

    def test_fila_prioritaria_deve_mostrar_estatisticas_resumidas(self, fila: FilaPrioritaria):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        estatisticas = fila.estatistica("10/01/1993", 198, "resumidas")

        estatistica_esperada = {"198-10/01/1993": 3}

        assert estatisticas == estatistica_esperada
