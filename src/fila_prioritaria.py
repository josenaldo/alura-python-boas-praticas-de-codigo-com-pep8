class FilaPrioritaria:
    """Representa uma fila normal"""

    def __init__(self):
        self.fila: list = []
        self.clientes_atendidos: list = []
        self.codigo: int = 0
        self.senha_atual: str = ""

    @property
    def tamanho(self):
        return len(self.fila)

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"PR{self.codigo}"

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}"

    def estatistica(self, dia: str, agencia: int, flag: str):
        if flag != "detail":
            estatistica = {f"{agencia}-{dia}": len(self.clientes_atendidos)}
        else:
            estatistica = {
                "dia": dia,
                "agencia": agencia,
                "clientes_atendidos": self.clientes_atendidos,
                "quantidade_clientes_atendidos": len(self.clientes_atendidos)
            }

        return estatistica
