import math

krupteeritav = str(input("Sisesta krüpteeritav sõnum: "))
key = int(input("Sisesta võti: "))
i = 0
j = 0
jarjend = []
jarjenda = []
tagurpidi = []


sifer = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]


krupteeritav = krupteeritav.lower()

i = 0
j = 0

#jarjend.append(krupteeritav) creates list
while i < len(krupteeritav):
    jarjenda.append(krupteeritav[i])
    i+= 1
i = 0
j = 0




while " " in jarjenda:
    jarjenda.remove(" ")



while i < len(jarjenda): #to num
    while j < len(alphabet):
        if not jarjenda[i] == alphabet[j]:
            j += 1
        else:
            jarjenda[i] = j
    j = 0
    i +=1



i = 0
j = 0

while i < len(jarjenda): # encryption
    abimuutuja = int(jarjenda[i]) % key
    sifer.append(abimuutuja)
    i += 1

#print("Jäägid on: ")
#print(sifer)

private = []

i = 0
while i < len(jarjenda): # private key
    abimuutuja = int(jarjenda[i]) // key
    private.append(abimuutuja) 
    i += 1

print("Privaatne võti: ")
print(private)

i = 0

while i < len(sifer): #to str
    if sifer[i] >= len(alphabet):
        sifer[i] = alphabet[sifer[i]-len(alphabet)]
    else:
        sifer[i] = alphabet[sifer[i]]
    i += 1

i = 0

f = math.floor(len(sifer) / 5)


d = ""
while i < len(sifer)+f: #to text
    if i % 5 == 0 and not i == 0:
        d = str(d) + " "
        i += 1
        j += 1
    else:
        d = str(d) + str(sifer[i-j])
        i += 1
print(" ")
print("Krüpteeritud sõnum: ")
print(d)


jarjend = []
jarjenda = []



i = 0
j = 0


#jarjend.append(d) #creates list
while i < len(d):
    jarjenda.append(d[i])
    i+= 1
i = 0
j = 0


while " " in jarjenda:
    jarjenda.remove(" ")

while i < len(jarjenda): #to num
    while j < len(alphabet):
        if not jarjenda[i] == alphabet[j]:
            j += 1
        else:
            jarjenda[i] = j
    i += 1
    j = 0


i = 0
j = 0

dekrupteeritud = ""

while i < len(jarjenda): #decrypt
    for x in jarjenda:
        jarjenda[i] = x + key * private[i]
        jarjenda[i] = alphabet[jarjenda[i]]
        i += 1


for x in jarjenda:
    dekrupteeritud = dekrupteeritud + str(x)
print(" ")
print("Dekrüpteeritud sõnum: ")
print(dekrupteeritud)

test = str(input(" "))
