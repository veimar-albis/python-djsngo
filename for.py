'''for numero in range (1,11):
    print(numero)'''
    
'''vocales=0
consonantes=0
palabra=input("Escribe una palabra para contar sus consonantes y vocales: ").strip().lower()
for letra in palabra:
    if letra in "aeiou":
        vocales=vocales+1
    else:
        consonantes=consonantes+1
print(" la palabra tiene {} vocales y {} consonantes".format(vocales,consonantes))'''

estudiantes={
    "masculino":["Tom","Charlie","Harry","Frank"],
    "femenino":["Sarah","Huda","Samantha","Emily","Elizabeth"]
}
for key in estudiantes.keys():
    for n in estudiantes[key]:
        if "a" in n:
            print(n)