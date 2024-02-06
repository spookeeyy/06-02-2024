fail = open("jooks.txt", encoding="UTF-8")
kokku = 0
jooksud = []
for rida in fail:
    jooksud.append(float(rida))
    kilomeetreid = float(rida)
    if kilomeetreid > 10:
        kokku += kilomeetreid
fail.close()
print("Kokku joosti pikki jookse",kokku,"kilomeetrit")