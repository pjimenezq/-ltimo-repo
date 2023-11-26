import pip._vendor.requests#Importando requests
import json #Importando json

#Pegando las url donde están almacenadas las API's
urlUno='https://www.boredapi.com/api/activity'
urlDos="https://catfact.ninja/fact"
urlTres="https://official-joke-api.appspot.com/random_joke"

def api(url):#Función para obtener pares de llave:valor de API's
    peticion=pip._vendor.requests.get(url)#Se llama la API
    contenido=json.loads(peticion.content)#Se obtiene el contenido del json
    for k,v in contenido.items():#Para las llaves y valores en el json
        print(k,":",v)#Imprimir el par llave:valor

if __name__=="__main__":
    #Se aplica la función para obtener pares de llave:valor en las tres API's 
    bored=api(urlUno)
    cat=api(urlDos)
    joke=api(urlTres)



