'''
// RSA Notes:
key = (e,n)
Encrypt message
1. Come up with 2 prime numbers (p q)
2. Multiply them, result is n
3. Count the numbers co-prime (GCF is 1) with n 
    phi_n = (p-1)(q-1)
4. then you find e: 1 < e < phi_n and coprime of phi_n 
    e = coprime(Phi_n)
5. encript c = message^e(mod(n))
Decript:
 find d: 1 = d*e(mod(phi_n))
        d = 1/(e*(mod(phi_n))
then find messege
    message = c^d(mod(n))

*look into kerberos

// Complete solution off the internet

RSA Encryptor/Decryptor
RSA Information Source: https://www.cryptool.org/en/cto/rsa-step-by-step/

def phi(a, b):
    return ((a - 1) * (b - 1))
    
def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
    
def mod_inverse():
    for i in range(2, phiNum):
        if (i * coprime) % phiNum == 1:
            return i

# select two prime numbers
primeNum1 = 5915587277
primeNum2 = 1500450271

RSAModule = primeNum1 * primeNum2
phiNum = phi(primeNum1, primeNum2)

coprime = None
for i in range(2, phiNum):
    if gcd(i, phiNum) == 1:
        coprime = i
        break

multiplicativeInverse = mod_inverse()

message = 10
cypherText = (message ** coprime) % RSAModule
decrypted_message = (cypherText ** multiplicativeInverse) % RSAModule

print(cypherText)
print(decrypted_message)

'''

import math


def RSA(message, prime1, prime2):
    n=p*q 

    phi_n = (p-1)*(q-1)

    # find first coprime of phi_n
    for i in range(2,phi_n): 
        if math.gcd(i,phi_n)==1:
            e=i
            break

    # encrypting the message
    c = message**e %n
    print(f"Public keys ({e},{n})")
    print(f"Cipher Text {c}")

    # find d
    #d = 1/(e % phi_n) This uses simple algebra, unfortunatly it does not work in python
    for j in range(1,100):
        if (j*e) % phi_n == 1:
            d=j
            print(f"D is: {d}")
            break

    # decript

    plaintext = c**d % n 
    print(f"Plaintext: {plaintext}")

p = 3
q = 7
message = 10 # i.e. J
RSA(message, p,q)
