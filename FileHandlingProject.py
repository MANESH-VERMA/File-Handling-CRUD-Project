from pathlib import Path
import os





def readFileandFolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")
        
    
    
def createFile():
    try:
        readFileandFolder()
        name=input("Tell Your File Name:- ")
        p=Path(name)
        
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write in this file:- ")
                fs.write(data)
                
            print(f"File created\nSuccessfullyyy")
                        
        else:
            print("This File Already exists..")
      
    except Exception as err:
        print(f"An error occured as {err}")
        
        
           
def readFile():
    try:
        readFileandFolder()   
        name=input("Which File you want to read..")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
                
            print("File, Readed Successfullyyyyyyy")
        
        else:
            print("File Does not Exists..")
                       
    except Exception as err:
        print(f"An error occured as {err}")
   
   

def updateFile():
    try:
        readFileandFolder()
        name=input("tell name of File You wants to Update:-")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1- for Changing the name of your File :-")
            print("press 2- for Overwriting some data on our File :-")
            print("press 3- for appending some Content on your File :-")
        
            res=int(input("tell your response :-"))
            if res==1:
                name2=input("tell your new FileName:-")
                p2=Path(name2)
                p.rename(p2)
                         
            if res==2:
                with open(p,"w") as fs:
                    data=input("tell What you want to write\nThis will Overwrite the Data :-")
                    fs.write(data)
                    
            if res==3:
                with open(p,"a") as fs:
                    data=input("tell What you want to append :-")
                    fs.write(" "+data)
    
    except Exception as err:
        print(f"An error occured as {err}")
    


def deletionFile():
    try:
        readFileandFolder()
        name=input("Which file you want to Delete :- ")
        p=Path(name)
        
        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfullyyyy ")
      
        else:
            print("No such file exists..")
    
    
    except Exception as err:
        print(f"An error occured as {err}")   
        
   

print("Enter 1 for Creating a File.")
print("Enter 2 for Reading a File.")
print("Enter 3 for Updating a File.")
print("Enter 4 for Deleting a File.")



check=int(input("Please, Tell your response :-" ))
if check==1:
    createFile()   
if check==2:
    readFile()
if check==3:
    updateFile()  
if check ==4:
    deletionFile()