from pyzxing import BarCodeReader


#Esto es de la libreria
reader = BarCodeReader()
results = reader.decode("./natu.png")

print(results)