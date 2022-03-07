def bin2dec(n):
    s = 0
    for i , elem in enumerate(n[::-1]):
        s += int(elem) * (2**i)
    return s

def dec2bin(n,nbit):
    s =  bin(n)[2:]
    s = "0"*(nbit-len(s)) + s
    return s

def  IP_dec2bin(n):
    s=""
    x = n.split(".")
    for k in range(4):
        s += ((dec2bin(int(x[k]),8))) 
    return s

def  IP_bin2dec(n):
    s=""
    for k in range(0,32,8):
        s += str(bin2dec(n[k: k + 8])) + "."
    return s[:-1]

def controlloIP(ip,subnet):
    conversione,err = IP_dec2bin(ip)[::-1],False
    for k in range(0,subnet):
        if conversione[k] != "0":
            err = True
    return err
    
def ip_Broadcast(ip,subnet):
    ip_binario = IP_dec2bin(ip)
    n = ""
    n = ip_binario[:subnet] + ip_binario[subnet:].replace("0","1")
    return IP_bin2dec(n)

hostMIN = lambda ip: ip[:-1] + str((int(ip[-1])+1))
hostMax = lambda ip,subnet: ip_Broadcast(ip,subnet) [:-1] + str((int(ip_Broadcast(ip,subnet)[-1])-1))

def hostMax(ip,subnet):
    ip_binario,n= IP_dec2bin(ip),""
    n = ip_binario[:subnet] + ip_binario[subnet:].replace("0","1")
    f = n[:31] + n[31:].replace("1","0")
    return IP_bin2dec(f)
    
def main():
    IP_Rete = input("Inserisci IP di rete:")
    SUBNET_MASK = int(input("Inserisci subnet mask /n : /"))
  
    controlloIP(IP_Rete,SUBNET_MASK)
    if(controlloIP(IP_Rete,SUBNET_MASK)):
        print("giusto")
        print(f"Numero di host disponibili: {2**(32-SUBNET_MASK)-2} \nSubnetMask:{IP_bin2dec('1'*SUBNET_MASK+ '0'*(32-SUBNET_MASK))}")
        print(f"Broadcast: {ip_Broadcast(IP_Rete,SUBNET_MASK)}")
        print(f"Host minimo: {hostMIN(IP_Rete)}")
        print(f"Host massimo: {hostMax(IP_Rete,SUBNET_MASK)}")
    else:
        print("sbagliato")
    

if __name__ == "__main__":
    main()