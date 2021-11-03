import query as query
from firebase import firebase

firebase=firebase.FirebaseApplication("https://bd2-prueba-5c25b-default-rtdb.firebaseio.com/",None)

lista=[]
cambiar="Pedro"

# datos={
#     'id':'3',
#     'edad':'35',
#     'nombre':'Pedro'
# }
# datos2={
#     'id':'5',
#     'edad':'18',
#     'nombre':'Matias'
# }
# #para llenar la base de datos método post
# lista.append(datos)
# lista.append(datos2)
#
# for x in lista:
#     resultado=firebase.post('/Base/',x)
#     print("Enviado")
# #la direccion donde se envio los datos
#     print(resultado)
#
#
# #Para leer la base de datos metodo GET
# leer2=firebase.get('/Base/','')
# for identificador in leer2:
#     leer=firebase.get('/Base/',identificador)
#     print(leer.get('nombre'))
#     print(leer.get('id'))
#     print(leer.get('edad'))

#update = firebase.put('Base/-MnYKvUkLawXP-0YddHB', 'nombre',cambiar)



remove=firebase.delete('/Base','-MnYKvUkLawXP-0YddHB')