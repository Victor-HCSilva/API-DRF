
class Cars:
    idade = 10
    def __init__(self, nome):
        self.nome = nome  # Usando o parâmetro `nome`
        print("Dentro do construtor da class pai, Cars")

    def model(self): # Adicionado self para ser um método de instancia
        return "Modelo Genérico"

class Toyota(Cars):
    def __init__(self, nome):
        super().__init__(nome) # Chamada correta ao construtor da classe pai, passando o parâmetro 'nome'
        print("Dentro do construtor da class filha, Toyota")

    def model(self): # Adicionado self para ser um método de instancia
        print(self.nome) # Acessando o atributo da instancia corretamente
        print(self.idade)

        return "Toyota"



def teste():
    return 'Ola, mundo'

if __name__ == '__main__':
    t = Toyota('Victor')
    print(t.model())
