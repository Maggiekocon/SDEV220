""""
a. convert password to bytes
b. generate a salt
c. encrypt (remember to store your tag, nounce, salt -> need to decrypt)

to decrypt need key, tag, nounce, salt, encypted message
"""
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes # for salt
from Crypto.Protocol.KDF import PBKDF2 # generates key from your password
from Crypto.Hash import SHA256 # hash for extra security

def encrypt_aes(message, password):

    # derive key from password and salt

    # PBKDF2 takes 
        # password (encoded in bytes)
        # salt in bytes
        # length (how long you want your key to be)
        # count (how many times you want it to hash it)
        # hmac_module (the hashing module to use)


    # need password to beggin encryption
    password_bytes = password.encode('utf-8')

    # generate salt as a random number/string in bytes
    salt= get_random_bytes(16)

    key = PBKDF2(password_bytes, salt, dkLen=32, count = 100000, hmac_hash_module = SHA256)

    # to encrypt, we need to use a specific AES MODE
    # Create a new AES cipher in GCM mode contains a nonce

    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    encrypted_message, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    #print(encrypted_message)
    
    # DECRYPT
    # need: key salt, tag, encrypted_message, nonce

    decrypt = AES.new(key, AES.MODE_GCM, nonce = nonce)
    decrypted_message = decrypt.decrypt_and_verify(encrypted_message, tag)

    #print( decrypted_message.decode('utf-8'))
    return encrypted_message, decrypted_message.decode('utf-8')

#encrypt_aes('Hello')  
    





