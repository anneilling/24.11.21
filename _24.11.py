def loe_failist(file:str)->str: #loeme tekst failist
    f=open(file,"r")
    stroka=f.read()#читает строку str
    stroka=f.readlines() #делает список list
    f.close()
    return stroka
stroka=loe_failist("TextFile1.txt")
print(stroka)
def loe_failist_listisse(file:str)->list: #loeme tekst failist ja salvestame listisse
    f=open(file,"r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_
spisok=loe_failist_listisse("TextFile1.txt")
print(spisok)

def salvesta_failisse(file:str):
    f=open(file,"a")
    text=input("Sisesta tekst: ")
    f.write(text+"\n")
    f.close()

for i in range(10):
    salvesta_failisse("Loetelu.txt")
    
 def faili_sisu_umberkirjutamine(file:str):
     text=input("Sisesta uus tekst: ")
     with open(file,"w") as f:
         f.write(text+"\n")
faili_sisu_umberkirjutamine(input("Faili nimetus ")+".txt")