class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando = False):

        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Comer.
    def comer (self, alimento):

        if self.comendo:
            print (f'{self.nome} já esta comendo: {alimento}')
            return

        print (f'{self.nome} esta comendo: {alimento}')   
        self.comendo = True

    # Parar de comer.
    def parar_comer(self):

        if not self.comendo:
            print (f'{self.nome} não está comendo.')
            return
        print (f'{self.nome} parou de comer.')
        self.comendo = False

    # Falar.
    def falar (self, assunto):

        if self.comendo:
            print(f'{self.nome} não consegue falar enquanto está comendo.')
            return
        
        if self.falando:
            print (f'{self.nome} já esta conversando.')
            return
        
        print (f'{self.nome} começou a falar.')
        self.falando = True
        


