import os
initial_count = 0
dir = "c:/Users/Escovar/Desktop/Python"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1
print("Numero de archivos: ", initial_count)
