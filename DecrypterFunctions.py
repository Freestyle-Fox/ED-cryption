from EncrypterFunctions import *
print("Decrypter Open Sucsessfully")

def extract_encrypter_code(string):
    if len(string)%2==0:
        code = string[len(string)//2-1]
        string = string[0:len(string)//2-1] + string[len(string)//2:]
    else:
        code = string[len(string)//2]
        string = string[0:len(string)//2] + string[len(string)//2:]
    return code, string
    
    
def decryption(string, encryptercode):
    print(string)
    print(encryptercode)

while True:
    user_input = input("<< ")
    encryptercode, encrypted_text = extract_encrypter_code(user_input)
    decypted_text = decryption(encrypted_text, encryptercode)
    if user_input == "exit":
        # exit()
        break