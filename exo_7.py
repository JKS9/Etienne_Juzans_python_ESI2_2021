print("Exo 7 :")

def password_check(password):

    SpecialSym = ["$", "#", "%"]
    val = True

    if len(password) < 6:
        print("- length should be at least 6")
        val = False

    if len(password) > 12:
        print("- length should be not be greater than 12")
        val = False

    if not any(char.isdigit() for char in password):
        print("- Password should have at least one numeral")
        val = False

    if not any(char.isupper() for char in password):
        print("- Password should have at least one uppercase letter")
        val = False

    if not any(char.islower() for char in password):
        print("- Password should have at least one lowercase letter")
        val = False

    if not any(char in SpecialSym for char in password):
        print("- Password should have at least one of the symbols $@#")
        val = False
    if val:
        return True

# Main method


def main(password):
    array_password = password.split(",")

    for i in array_password:

      if (password_check(i)):
          print(i)
          print("Password is valid")

      else:
          print("Invalid Password !!")

print("exemple not valid password : Aa1etienne")
print("exemple valid password : Aa1etienne#")
password = input("password : ")
main(password)