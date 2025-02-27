from datetime import datetime

class Pessoa:
    
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    
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
        
        if self.falando:
            print (f'{self.nome} não pode comer enquanto fala.')
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
        
        print (f'{self.nome} começou a falar. Ele esta dizendo: - {assunto}')
        self.falando = True
        
    # Parar Fala.
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False
        
    # Ano de Nascimento.
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
        
    
        


