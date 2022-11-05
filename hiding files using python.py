import os
import ast
imp_extension = ".txt"

dict1 = {}
dict2 = {}


def hide():
    i = 1
    path = input("Enter the location of the folder to hide the files in it : ")
    os.chdir(path)
    list_of_files = list(filter(os.path.isfile, os.listdir(os.getcwd())))
    print("Files hidden successfully....")

    for file in os.listdir(f'{path}'):
        dict1 = {f'{i}': f'{file}'}
        dict2.update(dict1)
        os.rename(file, f'{i}..')
        i += 1

    with open("imp.txt", "a+") as f:
        f.write(str(dict2))

def unhide():
    i = 1
    path = input("Enter the location of the folder to Unhide the files in it : ")
    os.chdir(path)
    if os.path.isfile("imp.txt"):
        pass
    else:
        print("imp.txt File may removed or renamed please check once again....")

    with open("imp.txt") as f:
        content = f.read()

    names_of_items = ast.literal_eval(content)
    os.remove(os.getcwd()+"\imp.txt")

    for items in os.listdir():
        if items == "imp.txt":
            pass
        else:
            items = items.split('.')[0]
            filename = names_of_items[f'{items}']
            os.replace(f'{items}..',f'{filename}')
    else:
        print("Files are successfully recovered.....")





print("Welcome To Our Hide Files Program....")
choice = input("1.Hide Data \n2.UnHide Data\nEnter Your Choice : ")

if choice == '1':
    hide()

elif choice == '2':
    unhide()

else:
    print("Wrong Input....")