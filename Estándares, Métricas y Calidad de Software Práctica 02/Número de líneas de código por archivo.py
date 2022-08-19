with open('c:/Users/Escovar/Desktop/Python/Archivo.txt') as myfile:
    total_lines = sum(1 for line in myfile)
print("Numero de lineas en un archivo: ", total_lines)
