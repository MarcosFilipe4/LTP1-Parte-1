class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False
        
    def exibir_informacoes(self):
        if self.vendido:
            return f"carro: \nMarca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano} \nPreço R$: {self.preco:.2f} mil \nVeiculo Vendido!\n\n"
        else:
            return f"carro: \nMarca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano} \nPreço R$: {self.preco:.2f} mil \nEm estoque. \n\n"
    
    def vender(self):
        self.vendido = True

    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco

primavia = Carro("Fiat", "Mobi", 2023, 4500)
formosa_fiat= Carro("Fiat", "HB20", 2023, 11000)
honda = Carro("Honda", "Civic", 2020, 13000)
revenda_car = Carro("Honda", "cit", 2010, 9900)
revenda_autorizada = Carro("Fiat", "Argo", 2022, 9000)


print(primavia.exibir_informacoes())
print(formosa_fiat.exibir_informacoes())
print(honda.exibir_informacoes())
print(revenda_car.exibir_informacoes())
print(revenda_autorizada.exibir_informacoes())

primavia.vender()
primavia.ajustar_preco(50)

revenda_autorizada.ajustar_preco(133)
revenda_autorizada.vender()

print(primavia.exibir_informacoes())

print(revenda_autorizada.exibir_informacoes())

print(honda.exibir_informacoes())