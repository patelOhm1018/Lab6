if __name__ == '__main__':
    #My name is Thomas Hahn and I wrote this encode function
    def encode(password):
        encoded_password =""
        for element in password:
            encoded_num = str((int(element) + 3) % 10)
            encoded_password += encoded_num
        return encoded_password

    #This decode function made by Om Patel
    def decode(password):
        decoded_password = ""
        for element in password:
            decoded_num = str((int(element) - 3) % 10)
            decoded_password += decoded_num
        return decoded_password

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    user_input = input("Please enter an option:")
    #option 1 encodes the password
    if user_input == "1":
        password = str(input("Please enter your password to encode: "))
        encoded_password = encode(password)
        print("Your password has been encoded and stored!")
        print(encoded_password)
    #option 2 decodes the password
    if user_input == 2:
        password = str(input("Please enter your password to decode: "))
        decoded_password = decode(password)
        print("Your password has been decoded and stored!")
        print(decoded_password)
