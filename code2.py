num=int(input("Enter the length of password:"))
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 8:

        print('length should be at least '+str(8-len(passwd)))
        val = False


    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


passwd = input("Enter Password")

if (password_check(passwd)):
    print("Strong Password,good to go!")
else:
    if len(passwd)!=8:
        count=8-len(passwd)
        print(str(count)+" more characters to be added")
