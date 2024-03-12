﻿﻿﻿﻿﻿from string import *
from time import sleep
from os import path, remove
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioon
    """
    while True:
        nimi=input("Mis on sinu nimi?: ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                    break
                else:
                    print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemas!" kui kasutaja on olemas nimeekirjas"""
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:           
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uueti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
            print("kasutajat pole")
def nimi_või_parooli(list_:list):
    """Funtsioon
    """
    muutuja=input("Vana nimi või parool")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,"r",encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):#Salasõnad.txt, Salasõnad
    """Salvesta tekst failisse
    """
    n=int(input("Mitu: "))#
    for i in range(n):#
        järjend.append(input(f"{i+1}. sõna: "))#
    f=open(fail,"a",encoding="utf-8")#w
    for element in järjend:
        f.white(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,"w") #a
    text=input("Sisesta tekst:")
    f.white(text+"\n")
    f.close()
def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
    print()
def failed_KS(fail:str):
    """
    """
    fail=input(fail,"")
def kirjuta_failisse(fail:str,Salasõnad=[]):
    """
    """
    f=open(fail,"w",encoding="utf-8")
    for element in Salasõnad:
        f.white(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,"a") 
    text=input("Sisesta tekst:")
    f.white(text+"\n")
    f.close()

