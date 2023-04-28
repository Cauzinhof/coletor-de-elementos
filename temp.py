bairros = open('bairros.txt', 'r')

for line in bairros:
    #print (line)
    if 'centro' == line.strip():
        print("sim")