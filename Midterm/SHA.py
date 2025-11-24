import hashlib
string="Hello"

def hash_sha(message, bits=265):
    """
    Takes a string and SHA type returns its SHA hash. Popular SHA types: 1, 224, 256, 384, 512, 512_224 and 512_256.
    """
    # encode string so readable by machine
    encoded_string = message.encode("utf-8")

    # generate hash
    hashed_string = getattr(hashlib, f"sha{bits}")()

    # Update hash with the string you want to hash
    hashed_string.update(encoded_string)

    # convert output to hexadecimal
    #print(hashed_string.hexdigest())
    return hashed_string.hexdigest()

