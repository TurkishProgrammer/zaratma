import zarfonk
while True:
    #while True döngüsü kurarak zarların her seferinde tekrar atılmasını sağlıyorum.
    zar1 = zarfonk.zar()
    zar2 = zarfonk.zar()
    zar3 = zarfonk.zar()
    zar4 = zarfonk.zar()
    zar5 = zarfonk.zar()
    #Kaç tane zar atmak istediğiniz sizin isteğinize bağlı.
    print(zar1,zar2,zar3,zar4,zar5)
    #her döngüde zarlarda gelen değerleri ekrana bastırıyorum
    if zar1 == zar2 == zar3 == zar4 == zar5 == 6:
    #İf komutuyla tüm zarlar 6'ya eşit olduğunda döngüden çık diyorum.
        break
