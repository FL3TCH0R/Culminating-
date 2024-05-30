filename = input("Where do you call the data? ") #task5.txt file
infile= open(filename, "a")

file2 = str(input("Enter the new file location")) #taslt.txt file
outfile = open(file2, "a")

def main():
    moredata = "add"#enables user to write add
    moreinfo = "transfer"
    print("\nDo you want to add data? or transfer information? (add/transfer. to quit press <Enter>)")
    choice = str(input("Your choice: "))
    
    if (choice.lower() == moredata):#if they write add it will go here
        addata()
        main()
    elif(choice.lower() == moreinfo):
        transfer()
        main()
    else:
        print("goodbye")

def addata():  
    infile=open(filename, "a")
    n = input("Enter the first name ")
    a = input("Enter the last name ")
    s = (n + " " + a+"\n")
    infile.write(s)
    infile.close()
    print("Text successfully inserted")

def transfer():
    infile= open(filename, "r")
    outfile = open(file2, "w")
    for line in infile:
        # get the first and last names from line 
        first,last = line.split()
        uname = (first + " " + last)
        # write it to the output file
        print (uname, file=outfile)
    infile.close()
    outfile.close()
main()
