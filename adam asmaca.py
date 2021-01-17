print( "       ADAM ASMACA OYUNU" )

kelime = input("Tahmin ettirmek istediğiniz kelimeyi girin: ").upper()


resim = ["""
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
print(resim[adim])


for i in kelime:
    tahmin.append("_")
print(tahmin)

while adim < 6 and "_" in tahmin:   # 7 resim listesininin uzunluğu 
    harf = input("Tahmininizi girin: ").upper()
    
    if harf in kelime:
        for index, h in enumerate(kelime):
            if harf == h:
                tahmin[index] = harf             
                print(resim[adim])
                print(tahmin)        
    else:
        adim +=1
        print(resim[adim])
        print("{} harfi kelimede bulunmuyor.".format(harf))
        print(tahmin)
                
if adim < len(resim) and not "_" in tahmin:
    print("Kazandınız!")
else:
    print("Kaybettiniz!")
