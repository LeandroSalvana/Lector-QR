from pyzxing import BarCodeReader

def procesar_codigo(imagen):
#Esto es de la libreria
    reader = BarCodeReader()
    results = reader.decode(imagen)

#----------------Aca esta la magia----------------------
    for diccionario in results:
        if len(diccionario) == 1:       
            print("Codigo no encontrado")
        else:
        #Accedo al indice 0 de la lista que me devuelve (que es un diccionario)
            raw = results[0]
            valor_raw = raw["raw"]
            valor_raw = valor_raw.decode("utf-8")
            valor_raw = valor_raw.replace("NXX","Ñ")
            valor_raw = valor_raw.split("@")
            llave_lista = ["N° de Tramite", "Apellido", "Nombre", "Sexo","N° Dni", "Tipo", "Fecha de Nacimiento", "Fecha de emisión"]
            objeto_raw = {llave:valor for llave, valor in zip(llave_lista, valor_raw[:8])}
            print (objeto_raw)

procesar_codigo("./micky.jpg")



