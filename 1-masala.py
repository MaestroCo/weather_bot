byt = bytearray()

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")

byt.extend(ism.encode('utf-8'))
byt.extend(familiya.encode('utf-8'))
byt.extend(str(yosh).encode('utf-8'))

print("Ma'lumotlar bytearray shaklida:", byt)
