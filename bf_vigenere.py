def ataque(ciphertext, idioma):
    max_key = 20
    tolerance = 10

    ct = ciphertext.replace(' ', '').upper()   #Formata texto para facilitacao de analise

    #Descobrimento do tamanho da chave
    spacing = []
    for i in range(len(ct) - 2):
        tmp = ct[i] + ct[i+1] + ct[i + 2]
        for j in range(3, len(ct) - 2 - i):
            if tmp == ct[i+j] + ct[i+j+1] + ct[i+j+2]:
                spacing.append(j)
                break

    max_mmc = 0
    key_len = 0
    for i in range(2, max_key + 1):
        counter = 0
        for n in spacing:
            if n % i == 0:
                counter += 1
        if counter + tolerance > max_mmc:
            key_len = i
            max_mmc = counter
            
    print("\nComprimento de chave estimado:", key_len)

    #Distribuindo letras de mesmo deslocamento
    box = []
    for i in range(key_len):
        group = []
        j = 0
        while(j*key_len+i < len(ct)):
            group.append(ct[j * key_len + i])
            j += 1
        box.append(group)

    #Analise de frequencia de cada grupo
    en_freq = [
            ('A', 8.167), ('B', 1.492), ('C', 2.782), ('D', 4.253),
            ('E',12.702), ('F', 2.228), ('G', 2.015), ('H', 6.094),
            ('I', 6.966), ('J', 0.153), ('K', 0.772), ('L', 4.025),
            ('M', 2.406), ('N', 6.749), ('O', 7.507), ('P', 1.929),
            ('Q', 0.095), ('R', 5.987), ('S', 6.327), ('T', 9.056),
            ('U', 2.758), ('V', 0.978), ('W', 2.360), ('X', 0.150),
            ('Y', 1.974), ('Z', 0.074)]
    pt_freq = [
            ('A',14.63), ('B', 1.04), ('C', 3.88), ('D', 4.99),
            ('E',12.57), ('F', 1.02), ('G', 1.30), ('H', 1.28),
            ('I', 6.18), ('J', 0.40), ('K', 0.02), ('L', 2.78),
            ('M', 4.74), ('N', 5.05), ('O',10.73), ('P', 2.52),
            ('Q', 1.20), ('R', 6.53), ('S', 7.81), ('T', 4.34),
            ('U', 4.63), ('V', 1.67), ('W', 0.01), ('X', 0.47),
            ('Y', 0.01), ('Z', 0.47)]

    freq = en_freq if idioma == 0 else pt_freq
    key = []
    for group in box:
        curr_key = ''
        min_dif = 10000
        for i in range(26):
            aux = []
            for c in group:
                if ord(c) - i >= ord('A'):
                    aux.append(chr(ord(c) - i))
                else:
                    aux.append(chr(ord('A') + 26 - i + (ord(c) % ord('A'))))
            dif = 0
            for c in aux:
                prob = [letra for letra in freq if letra[0] == c][0][1] / 100
                dif += abs(prob - (aux.count(c) / len(aux)))
            dif = dif / len(aux)
            if dif < min_dif:
                min_dif = dif
                curr_key = chr(ord('A')+i)
        key.append(curr_key)
    print("Chave mais provavel: ", end='')
    for c in key: print(c, end='')
    print()

print("Texto cifrado (portugues):")
ataque(input(), 1)
print("\nTexto cifrado (ingles):")
ataque(input(), 0)
