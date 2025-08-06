edad= int(input("Ingrese su edad: "))
if edad < 13:
    print("Usted es un niño")
elif edad >=13 and edad <18:
    print("Usted es un adolescente") 
elif edad >=18 and edad <65:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor") 