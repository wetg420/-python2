#mimu esimene programm
print("Tere maailm")
print(3+2)

nimi = input("Sisesta oma nimi")
print(nimi)

a = float(input("9"))
b = float(input("3"))

print("12:", a + b)
print("27:", a * b)
print("3:", a / b)
print("2.25:", a * 0.25)

if a == b:
    print("arvud on võrdsed")
else:
    print("arvud on erinevad")
    if a > b:
        print("Esimene arv on suurem")
    else:
        print("teine arv on suurem")