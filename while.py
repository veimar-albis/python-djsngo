'''n=1
while n<=100:
    if n%2==0:
        print(n)
    n=n+1'''

L=[]
while len(L)<3:
    nuevo_nombre=input("agrega un ombre: ").strip().capitalize()
    L.append(nuevo_nombre)
print("la lista esta llena")
print(L)
