print( "       ADAM ASMACA OYUNU" )

kelime = input("Tahmin ettirmek istediğiniz kelimeyi girin: ").upper()


adam = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]


adim = 0
tahmin = []
print(adam[adim])


for i in kelime:
    tahmin.append("_")
print(tahmin)

while adim < 6 and "_" in tahmin:   # adam listesininin uzunluğu 7, index 6dan küçük olmalı 
    harf = input("Tahmininizi girin: ").upper()
    
    if harf in kelime:
        for index, h in enumerate(kelime):
            if harf == h:
                tahmin[index] = harf             
                print(adam[adim])
                print(tahmin)        
    else:
        adim +=1
        print(adam[adim])
        print("{} harfi kelimede bulunmuyor.".format(harf))
        print(tahmin)
                
if adim < len(adam) and not "_" in tahmin:
    print("Kazandınız!")
else:
    print("Kaybettiniz!")
