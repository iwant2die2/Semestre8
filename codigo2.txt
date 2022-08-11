class Bicicleta:
    counter = 0

    def __init__(self):
        pass
    def one_method(self):
        Bicicleta.counter += 1
        return Bicicleta.counter
  
g1 = Bicicleta()
print(g1.one_method())
