class Bomba:
    def __init__(self, tipo_combustivel, valor_litro, qntd_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qntd_combustivel = qntd_combustivel

    def abastecer_valor(self, valor):
        qntd_veiculo = valor / self.valor_litro
        print("Foi colocada a quantia %.2f litros" % qntd_veiculo)
        self.qntd_combustivel -= qntd_veiculo

    def abastecer_qntd(self, qntd):
        aPagar = qntd*self.valor_litro
        print(f"Valor do abastecimento: R${aPagar}")
        self.qntd_combustivel -= qntd


b = Bomba("Alcool", 5.00, 150)
b.abastecer_qntd(40)
print(b.qntd_combustivel)
b.abastecer_valor(100)
print(b.qntd_combustivel)
