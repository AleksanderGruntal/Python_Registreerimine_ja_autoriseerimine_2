﻿from MinuOmaModul import *

failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("Päevad.txt")

päevad=loe_failist("Päevad.txt")

kirjuta_failisse("Salasõnad.txt")

ümber_kirjuta_fail("Päevad.txt")

#1
print(päevad)
#2
for päev in päevad:
    print(päev)
