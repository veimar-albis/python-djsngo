#perbir email
email=input("cual es t email?: ").strip()
#cortar nombre
nombre=email[:email.index("@")]
#cortar diminio
dominio=email[email.index("@")+1:]
#formatera el emnsaje
salida="tu nombre de usuario es {}, y tu nombre de dominio es {}".format(nombre,dominio)
print(salida)