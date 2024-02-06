from time import sleep

keel = int(input("1) Eesti \n2) English \n3) Deutsche"))

if keel == 2:
    failinimi = "eng.txt"
elif keel == 3:
    failinimi = "ger.txt"
else:
    failinimi = "est.txt"
    
readfailist = open(failinimi, encoding = "UTF-8")
read = []

for rida in readfailist:
    read = read + [rida.strip("\n")]
readfailist.close()

sisestatudPin = "",
katseid = 3

while sisestatudPin != "1234" and katseid > 0:
    print(read[0])
    print(read[1]+str(katseid)+read[2])
    katseid -= 1
    sisestatudPin = input()
    
if sisestatudPin == "1234":
    print(read[3])
else:
    print(read[4])
    i = 10
    while i > 0:
        print(i)
        i -= 1
        sleep(1)