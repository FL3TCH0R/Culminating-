outfileName = input("Where do you want to save the data? ")
outfile=open(outfileName, "a")

def classes():
    outfile=open(outfileName, "a")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    name = str(input("Enter a name: "))
    age = float(input("Enter their average: "))
    p1 = Person(name , str(age))
    outfile.write(str("Student Identification: " + p1.name +". Their average is: " + p1.age + "\n"))
    outfile.close()
#classes()


def replacing():
    search_text = input("Insert text to look for: ")
      
    replace_text = input("insert text to replace it:")
      
    with open(outfileName, 'r') as outfile: 
      
        data = outfile.read() 
      
       
        data = data.replace(search_text, replace_text) 
      
    with open(outfileName, 'w') as outfile: 
      
        outfile.write(data) 
      
    print("Text replaced") 

def details():
    outfile=open(outfileName, "a")
    classes()
    outfile.close()
    
def deleting():
    try:
        with open(outfileName, 'r') as outfiler:
            lines = outfiler.readlines()
     
            with open(outfileName, 'w') as outfilew:
                for line in lines:
                    dele = input("enter text to delete: ")
                    if line.find(str(dele)) == -1:
                        outfilew.write(line)
        print("Deleted")
    except:
        print("Oops! somethings wrong")

def main():
    moreadd = "add"
    morereading = "read"
    moredelete = "delete"
    moreupdate = "update"
    print("\nDo you want to add details? read the data? delete someones data? or update their data?(add/read/delete/update. to quit press <Enter>)")
    choice = str(input("Your choice: "))
    if (choice.lower() == moreadd):
        details()
        main()
    elif(choice.lower() == morereading):
        read()
        main()
    elif(choice.lower() == moredelete):
        deleting()
        main()
    elif(choice.lower() == moreupdate):
        replacing()
        main()
    else:
        print("goodbye")

def read():
    outfile=open(outfileName, "r")
    reading = outfile.read()
    print(reading)

main()
