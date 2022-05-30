
import os, os.path
"Case study for gathering information from a file system"

menu = "please choose your command number:" \
       "\n1- List the current directory" \
       "\n2- Move up" \
       "\n3- Move down" \
       "\n4- Number of file in the directory " \
       "\n5- Size of the directory in the bytes" \
       "\n6-Search for a filename" \
       "\n7- Quit the program"
QUIT = '7'
commands = ('1','2','3','4','5','6','7')

def main():
    while True:
        print(os.getcwd())
        print(menu)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break

def acceptCommand():
    command = input("Enter a number: ")
    if command in commands:
        return command
    else:
        print("Error:command not valid,")
        return acceptCommand()


def runCommand(command):
    if command == '1':
        print(listCurrentDir(os.getcwd()))
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        countFils(os.getcwd())
    elif command == '5':
        countBytes(os.getcwd())
    elif command == '6':
        target = input("Enter your search string")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found in any file")
        else:
            for f in fileList:
                print(f)


def listCurrentDir(dirName):
     list = os.listdir(dirName)
     for element in list:
         print(element)


def moveUp():
    os.chdir("..")


def moveDown(currntDir):
    newDir = input("Enter the directory name: ")
    if os.path.exists(currntDir + os.sep + newDir) and os.path.isdir(newDir):
        os.chdir(newDir)

    else:
        print("Error, there is not a directory name such loke that")


def countFils(dirName):
    count = 0
    contentDir = os.listdir(dirName)
    for element in contentDir:
        if os.path.isfile(element):
            count +=1
        else:
            os.chdir(element)
            count += countFils(element)
            os.chdir("..")
    return count


def countBytes(path):
    countByte = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            countByte += os.path.getsize(element)
        else:
            os.chdir(element)
            countByte += countBytes(os.getcwd())
            os.chdir("..")

    return countByte


def findFiles(target ,path):
    files =[]
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)

            else:
                os.chdir(element)
                files.extend(findFiles(target, os.getcwd()))
                os.chdir("..")
    return files

if __name__ == "__main__":
    main()
