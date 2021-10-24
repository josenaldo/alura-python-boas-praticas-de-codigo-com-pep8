import pytest

from src.fila_normal import FilaNormal


class TestFilaNormal:

    @pytest.fixture
    def fila(self):
        return FilaNormal()

    def test_fila_normal_deve_ser_criada_com_tamanho_inicial_0(self, fila):
        assert fila.tamanho == 0

    def test_fila_normal_deve_ter_tamanho_1_quando_adicionado_um_elemento(self, fila):
        fila.atualiza_fila()
        assert fila.tamanho == 1

    def test_fila_normal_devendo_ter_tamanho_2_quando_adicionados_dois_elementos(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        assert fila.tamanho == 2

    def test_fila_normal_deve_chamar_1_cliente_com_primeira_senha_da_fila(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        chamado = fila.chama_cliente(10)

        assert chamado == "Cliente atual: PR1, dirija-se ao caixa: 10"

    def test_fila_normal_deve_chamar_2_clientes_com_as_duas_primeiras_senhas_da_fila(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        chamado1 = fila.chama_cliente(10)
        chamado2 = fila.chama_cliente(1)

        assert chamado1 == "Cliente atual: PR1, dirija-se ao caixa: 10"
        assert chamado2 == "Cliente atual: PR2, dirija-se ao caixa: 1"

    def test_fila_normal_deve_ter_tamanho_0_quando_todos_os_clientes_foram_atendidos(self, fila):
        fila.atualiza_fila()
        fila.atualiza_fila()
        fila.atualiza_fila()

        fila.chama_cliente(10)
        fila.chama_cliente(1)
        fila.chama_cliente(5)

        assert fila.tamanho == 0
