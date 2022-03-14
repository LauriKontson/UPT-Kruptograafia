import math

krupteeritav = str(input("Sisesta krüpteeritav sõnum: "))
voti = str(input("Sisesta võti: "))
i = 0
j = 0
jarjend = []
jarjenda = []
tagurpidi = []

key = []
while i < len(voti):
    key.extend(voti[i])
    i += 1

i = 0


#key = ["c","h","e","e","s","e"]
sifer = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
while i < len(key): #key to num
    while j < len(alphabet):
        if not key[i] == alphabet[j]:
            j += 1
        else:
            key[i] = j
    j = 0
    i +=1

krupteeritav = krupteeritav.lower()

i = 0
j = 0

jarjend.append(krupteeritav) #creates list
while i < len(krupteeritav):
    jarjenda.append(krupteeritav[i])
    i+= 1
i = 0
j = 0




while " " in jarjenda:
    jarjenda.remove(" ")


while " " in key:
    key.remove(" ")





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

while i < len(jarjenda): # sum of both
    if len(jarjenda) > len(key):
        key.extend(key)
    else:
        abimuutuja = int(jarjenda[i]) + int(key[i])
        sifer.append(abimuutuja) 
    i += 1


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
print(d)

#while i < len(krupteeritav):
#    tagurpidi.append(jarjenda[len(krupteeritav)-1-i])
#    i+= 1
#print(tagurpidi)
