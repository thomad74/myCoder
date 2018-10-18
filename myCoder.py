alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
range(26)
zip(alphabet, range(26))
dic = dict(zip(alphabet, range(26)))

dic2 = {v: k for k, v in dic.items()}

while True: # adding an encoder
    string = input("Enter a string to cipher?: ").upper()
    task = input("Would you like to encode or decode?: ").lower()
    while True:
        try:
            key = int(input("Choose a key to cipher with?: "))
            break
        except ValueError:
            pass
    if task == "decode": # adding a decoder
        key = -key

    list = (dic[x] for x in string)
    encode = ((x + key) % 27 for x in list)
    encodeString = (dic2[x] for x in encode)
    print("".join(encodeString))

# # dic1 = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8,
# # "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
# # "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, " ": 26}
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# range(26)
# zip(alphabet, range(26))
# dic1 = dict(zip(alphabet, range(26)))
#
# dic2 = {v: k for k, v in dic1.items()}
#
# myCoder = True
#
# while True: # adding an encoder
#     list = []
#     encode = []
#     encodeString = []
#     decode = []
#     decodeString = []
#     task = input("Would you like to encode or decode?: ").lower()
#     if task == "encode":
#         string = input("Enter a string to encode?: ").upper()
#         key = input("Choose a key to encode with?: ")
#         list = [dic1[x] for x in string]
#         for x in list:
#             encode.append(eval("{}{}".format(x,key)) % 27)
#         for x in encode:
#             encodeString.append(dic2[x])
#         print("".join(encodeString))
#     if task == "decode": # adding a decoder
#         key = -key
#
#     # else: # adding a decoder
#     #     task == "decode"
#     #     string = input("What would you like to decode?: ").upper()
#     #     key = input("What key would you like to use?: ")
#     #     list = [dic1[x] for x in string]
#     #     for x in list:
#     #         decode.append(eval("{}{}".format(key,x)) % 27)
#     #     for x in decode:
#     #         decodeString.append(dic2[x])
#     #     print("".join(decodeString))
