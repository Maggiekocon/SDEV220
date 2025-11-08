

def CaesarCipher(Message, shft):
    Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    Cipher_text =[]
    for i in Message:
        index = Letters.index(i)
        shft_index = index + shft
        # How to when index is not in range 1-24
        if shft_index > 23: 
            shft_index = shft_index % 24
        elif shft_index < 0:
            shft_index=shft_index + 24
        Cipher_text.append(Letters[(shft_index)])
        
    print(f"Message: {Message}")
    print(f"Shift: {shft_index}")
    # make list into a string
    separator = " "
    Cipher_text_string = separator.join(Cipher_text)    
    print(f"Cipher Text: {Cipher_text_string}")

    
   
CaesarCipher(input("What would you like to encode? ").upper(), int(input("Input shift value negative for backwards, positive for forward: ")))







# def primelist(lower,upper):
#     primes = []
#     for number in range(lower, upper+1):
#         factors= []
#         for i in range(1,number+1):
#             print(i)
#             if number%i == 0:
#                 factors.append(number)
#         if len(factors)== 2:
#             primes.append(number) 
#     print(primes)  

# def coprime(p,q):
#     phi_n = (p-1)(q-1)
#     return phi_n

# # n = p*q
# # list = coprime(phi_n) Intercept phi_n

    


