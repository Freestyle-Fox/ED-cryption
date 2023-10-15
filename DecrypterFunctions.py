from EncrypterFunctions import *
print("Decrypter Open Sucsessfully")

def extract_encrypter_code(string):
    if len(string)%2==0:
        code = int(string[len(string)//2-1])
        string = string[0:len(string)//2-1] + string[len(string)//2:]
    else:
        code = int(string[len(string)//2])
        string = string[0:len(string)//2] + string[len(string)//2:]
    return code, string
    
    
def decryption(string, encryptercode):
    encryption_list = [encryption001, encryption002, encryption003, encryption004]
    dicrypted_text = ''
    split_list = []
    if encryptercode ==1:
        split_list = [string[i:i+1] for i in range(0, len(string))]
    elif encryptercode > 1 and encryptercode<5:
        split_list = [string[i:i+3] for i in range(0, len(string), 3)]
        
    key_list = list(encryption_list[encryptercode-1].keys())
    val_list = list(encryption_list[encryptercode-1].values())
    for i in split_list:
        position = val_list.index(i)
        dicrypted_text += key_list[position]
    print(dicrypted_text)
        
while True:
    user_input = input("<< ")
    encryptercode, encrypted_text = extract_encrypter_code(user_input)
    decypted_text = decryption(encrypted_text, encryptercode)
    if user_input == "exit":
        # exit()
        break