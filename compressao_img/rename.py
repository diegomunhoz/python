import os

def rename(directory):
    for name in os.listdir(directory):
        print(name)
        os.rename(os.path.join(directory,name),
                  os.path.join(directory,'0'+name))


path = input("Enter the file path")
rename(path)