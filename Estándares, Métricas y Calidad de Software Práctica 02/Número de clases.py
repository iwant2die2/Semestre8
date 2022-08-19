class Bicicleta:
    counter = 0
    def __init__(self):
        Bicicleta.counter += 1
  
g1 = Bicicleta()
g2 = Bicicleta()
g3 = Bicicleta()
print(Bicicleta.counter)
