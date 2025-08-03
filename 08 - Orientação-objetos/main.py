from transportes import Carro, Bicicleta

def main():
    carro = Carro("Fusca", 4, "gasolina")
    bicicleta = Bicicleta("Caloi", 1, "mountain bike")

    print(carro)
    carro.mover()
    carro.abastecer()

    print()

    print(bicicleta)
    bicicleta.mover()
    bicicleta.empinar()

if __name__ == "__main__":
    main()
