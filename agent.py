import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("""musisz podac conajmniej 1 parametr:
          1 - hasło (konieczny)
          2 - nazwa pliku do zapisu (domyslnie password.txt)""")

    sys.exit(0)
elif len(sys.argv) == 3:
    file = sys.argv[2]
else:
    file = 'password.txt'


my_pass = [sys.argv[1]]



def add_number(password, number, newlist):
    newlist.append(password + str(number))
    if number < 9:
        return add_number(password, number + 1, newlist)
    else: return newlist


def change_case(password: str, number, newlist):
    if number == len(password): return newlist
    if password[number].islower():
        password2 = password[:number] + password[number].upper() + password[number + 1:]
        newlist.append(password2)
    return change_case(password, number + 1, newlist)


def check(li_st, position, new, func):
    new += func(li_st[position], 0, [])
    if position < len(li_st) - 1:
        return check(li_st, position + 1, new, func)
    else: return new


my_check = check(my_pass, 0, [], add_number)
my_check = check(my_check, 0, [], change_case)


with open(file, 'w') as my_file:
    my_file.write('\n'.join(my_check))