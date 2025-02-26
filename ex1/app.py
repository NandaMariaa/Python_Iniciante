# vendedor Classe.

class Vendedor (): 

    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu (self, vendas):
        self.vendas = vendas

    def bateu_meta (self, meta):
        if self.vendas > meta:
            print(self.nome,"Bateu a Meta!!")
        else: 
            print(self.nome,"Não Bateu a Meta!")

# vendedor 1.

vendedor1 = Vendedor ("Lira")

print ("Vendedor:",vendedor1.nome)
vendedor1.vendeu(1000)
print ("Vendeu:",vendedor1.vendas)
vendedor1.bateu_meta(500)

# vendedor 2.

vendedor2 = Vendedor ("Ana")

print ("Vendedor:",vendedor2.nome)
vendedor2.vendeu(400)
print ("Vendeu:",vendedor2.vendas)
vendedor2.bateu_meta(500)


