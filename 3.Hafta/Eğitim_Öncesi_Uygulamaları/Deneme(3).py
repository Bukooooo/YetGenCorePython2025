# Karşılaştırma operatörleri
# ' = ' atama operatörüdür.
a, b, c = 7, 10, 578
print(a)
print(c)

# == değerlerin eşit midir diye sorar.
# != değerlerin eşit değil midir diye sorar.
x = 678
y = 1000
print(x == y)

Username = "Bugra"
print("Ayşe" != Username)


print(a > b)
print(a <= b)
print(b < c)
print(c >= b)

print("------------------------------")

# Mantıksal operatörler

# AND Operatörü
# True and True = True, Geriye kalan bütün durumlar için false

Sayi3 = int(input("Bana bir sayı ver: "))
print(x > 8 and x <15)

# OR Operatörü
# False and False = False, Geriye kalan bütün durumlar için True

Sayi4 = int(input("Bana bir sayı ver: "))
print(Sayi4 > 0 or Sayi4 % 2 == 0 )

# NOT Operatörü 
# True değerini False, False değerini True yapar.
print(not(True))
print(not(False))

print("----------------------------")

#