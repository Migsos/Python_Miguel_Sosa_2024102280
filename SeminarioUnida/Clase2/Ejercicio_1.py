a=int(input("Ingrse un numero: "))
b=int(input("Ingrse otro numero: "))
if ((a%2==0) and (b%2==0)):
    print("Ambos son pares")
elif ((a%2==0) and (b%2!=0)):
    print(f"[{a} es par")
    print(f"[{b} es impar")
elif ((a%2!=0) and (b%2==0)):
    print(f"[{a} es impar")
    print(f"[{b} es par")  
else:
    print("Los dos numero son impares")  
