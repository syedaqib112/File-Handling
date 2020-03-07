import os
print("Do you want to create a file ?(Y/N)")
ans = input()
if ans == 'Y' or 'y':
    print("Enter the file name: \n")
    name = input()
    path = 'C:/Users/Prashant/Desktop/file_handling/' + name
    print(path)
    if os.path.exists(path) == True:
        print("File Exist")
    else:
        fhand = open(path, 'w')
        print("Enter the text: \n")
        text = input()
        fhand.write(text)
        fhand.close()
        print("File Created")
elif ans == 'N':
    print("Enter the file you want to open : ")
    nam = input()
    path = 'C:/Users/Prashant/Desktop/file_handling/' + nam
    print("File Opened")
    print(path)
    if os.path.exists(path) == True:
        fhand = open(path, 'r')
        for i in fhand:
            print(i)
    else:
        print("File does not exist")
        
else:
    print("Invalid Input")