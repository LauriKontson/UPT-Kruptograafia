krupteeritav = str(input("Sisesta krüpteeritav sõnum: "))
i = 0
jarjend = []
jarjenda = []
jarjendb = []
jarj = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]


jarjend.append(krupteeritav)
while i < len(krupteeritav):
    jarjenda.append(krupteeritav[i])
    i+= 1
i = 0
j = 0

while i < len(krupteeritav):
    while j < len(jarj):
        if jarjenda[i] == jarj[j]:
            if not j+1 == len(jarj):
                jarjenda[i] = jarj[j+1]
            else:
                jarjenda[i] = jarj[0]
            break
        else:
            j+= 1
    j = 0
    i+= 1


i = 0
while i < len(krupteeritav):
    jarjendb.append(jarjenda[len(krupteeritav)-1-i])
    i+= 1


i = 0
krupteeritud = ""
while i < len(jarjendb):
    krupteeritud = str(krupteeritud + jarjendb[i])
    i+= 1
i = 0
print(krupteeritud)
dekrupteeritav = str(input("Sisesta dekrüpteeritav sõnum: "))

jarjend = []
jarjenda = []
jarjendb = []


jarjend.append(dekrupteeritav)
while i < len(dekrupteeritav):
    jarjenda.append(dekrupteeritav[i])
    i+= 1
i = 0
j = 0

while i < len(dekrupteeritav):
    while j < len(jarj):
        if jarjenda[i] == jarj[j]:
            if not j-1 < 0:
                jarjenda[i] = jarj[j-1]
            else:
                jarjenda[i] = jarj[len(jarj)-1]
            break
        else:
            j+= 1
    j = 0
    i+= 1
    
i = 0
while i < len(dekrupteeritav):
    jarjendb.append(jarjenda[len(dekrupteeritav)-1-i])
    i+= 1


i = 0
dekrupteeritud = ""
while i < len(jarjendb):
    dekrupteeritud = str(dekrupteeritud + jarjendb[i])
    i+= 1
i = 0


print(dekrupteeritud)