from getpass import getpass
from operator import length_hint
def main():
    password=get_valid_password()
    print_stars(length_hint(password))

def get_valid_password():
    password = getpass.getpass(prompt='Password: ')
    while len(password) >6:
        print('Password must be at least 6 characters long')
        password = get_valid_password()
    return password
def print_stars(length):
    print('*'*length)
