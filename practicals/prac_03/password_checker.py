
"""
Daniel McMillan.

"""


def main():

    password = input("Please enter your password. ")
    while len(password) < 8:
        print("Please use 8 or more characters.")
        password = input("Please enter your password. ")
    get_password(password)


def get_password(password):

    for character in password:
        hidden_password = "*"
        print(hidden_password, end="")


main()

