﻿﻿﻿from MinuOmaModul import *
from string import *

salasõnad=loe_failist("Salasõnad.txt")
kasutajanimed=loe_failist("Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taasatamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõna=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutumine: ")
            kasutajanimed=nimi_või_parooli(kasutajanimed)
            print("Parooli muutumine: ")
            salasõnad=nimi_või_parooli(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")
    elif vastus==5:
        print("Lõpetamine")
    elif vastus==6:
        print("")
        Salasõnad=failed_KS(Salasõnad)
    elif vastus==7:
        print("")
        Päevad=kirjuta_failisse(Päevad)
        break
    else:
        print("Tundmatu valik")
