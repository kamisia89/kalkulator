print("KALKULATOR")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("Podaj działanie, posługując się odpowiednią liczbą: ")
dzialanie = input("Podaj numer działania: ")
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
if dzialanie == "1":
    print("   a+b= ",a+b)
elif dzialanie =="2":
    print("   a-b= ",a-b)
elif dzialanie =="3":
    print("   a*b= ",a*b)
elif dzialanie =="4":
    print("   a/b= ",a/b)
else:
    print("Nie ma takiego działania")