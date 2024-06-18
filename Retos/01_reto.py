# # Manejo de excepciones
# try:
#     print(10 / 0)
# except:
#     print('Se ha produccido un error')
# finally:
#     print('Ha finalizado el manejo de excepciones')

# for number in range(10, 56):
#     if number % 2 == 0 and number != 16 and number % 3 != 0:
#         print(number)

# def imprimir(primer_parametro, segundo_parametro):
#     count = 0
#     for number in range(1,101):
#         if number % 3 == 0 and number % 5 == 0:
#             print(primer_parametro + segundo_parametro)
#         elif number % 3 == 0:
#             print(primer_parametro)
#         elif number % 5 == 0:
#             print(segundo_parametro)
#         else:
#             print(number)
#             count += 1
#     return count

# print(imprimir('Hola','mundo'))

# def my_agenda():

#     agenda = {}


#     def insert_contact():
#         phone = input('Agrega el numero de la persona: ')
    
#         if phone.isdigit() and 0 < len(phone) < 11:
#             agenda[name] = phone
#         else:
#             print('El phone tiene que ser en numero y debe contener maximo 10 digitos')


#     while True:


#         print('1. Buscar contacto.')
#         print('2. Insertar contacto.')
#         print('3. Actualizar contacto.')
#         print('4. Eliminar contacto.')
#         print('5. Salir de la agenda.')
    
#         option = input('\n Selecciona una de las 5 opciones:')
    
#         match option:
#             case '1':
#                 name = input('Cual es el nombre que buscas: ')
                
#                 if name in agenda:
#                     print(f'El numero de telefono de {name} es {agenda[name]}')
#                 else:
#                     print(f'No existe {name} en la agenda')
    
#             case '2':
#                 name = input('Agregar el nombre de la persona: ')
#                 insert_contact()
    
#             case '3':
#                 name = input('Cual es el nombre que quieres actualizar: ')
#                 insert_contact()
                
#             case '4':
#                 name = input('Cual es el contacto que quieres eliminar: ')
#                 if name in agenda:
#                     del agenda[name]
#                 else:
#                     print('El usuario no existe')
#             case '5':
#                 print('Saliendo de la agenda')
#                 break
#             case _:
#                 print('Opcion no valida elige una de las 5 opciones')
    








