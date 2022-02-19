def bin2dec(nBin):
    nDec = 0
    n = len(nBin) - 1
    for cifra in nBin:
        nDec += int(cifra) * (2**n)
        n = n - 1

    return nDec

def dec2bin(nDec,nbit):
    nBin = bin(nDec)[2:]
    nBin = "0"*(nbit - (len(nBin))) + nBin
    return nBin

def IP_dec2bin(ip):
    ipNew = ip.split(".")
    s = ""
    for elemento in ipNew:
        s += dec2bin(int(elemento),8)
    return s

def IP_bin2dec(ipBin):
    lista = []
    convertito = ""
    lista.append(ipBin[0:8]) #separo ip  in blocchi da 8 bit
    lista.append(ipBin[8:16])
    lista.append(ipBin[16:24])
    lista.append(ipBin[24:32])

    for elemento in lista:  #converto la stringa di 8 bit in un numero decimale
        convertito += str(bin2dec(elemento))+'.'
    
    return convertito[:-1]

def controlloIP(ip,subnet):
    convertito = IP_dec2bin(ip)

    return True

def main():
    while True:
        IP = input("Inserisci indirizzo IP: ")
        subnet = int(input("Inserisci la subnet mask (es. 25): /"))
        if controlloIP(IP,subnet):
            break

if __name__ == "__main__":
    main()