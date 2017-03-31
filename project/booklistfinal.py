class book(object):
    def __init__(self,name,author):
        self.name=name
        self.author=author
def addlist(booklist):
    name=input("Enter the book name:")
    author=input("Enter the book author name:")
    booklist.append(book(name.upper(),author.title()))
def listbook(booklist):
    if not booklist:
        print("the list is empty")
    else:
        for i in booklist:
            print((i.name.upper(),i.author.title()))
def readbook(booklist):
    blist=[]
    f=open(input("Enter the filename"))
    for line in f:
        comma=line.find(",")
        name=line[0:comma]
        author=line[comma+1:]
        blist.append(book(name.upper(),author.title()))
        print((name.upper(),author.title()))
    userinput=input("woud you like to add the book in the temporary list\n1.yes\n2.no\nEnter the option")
    if userinput=="1":
        for i in blist:
            booklist.append(i)
        print ("saved")
    else:
        print ("not saved")
    f.close()
def savenew(booklist):
    userinput=input("enter the file name you want to write:")
    f=open(userinput,'w')
    for i in booklist:
        f.write("%s,%s\n"%(i.name.upper(),i.author.title()))
    f.close()
def saveexisting(booklist):
    userinput=input("enter the exisitng file name you want to write:")
    f=open(userinput,'a')
    for i in booklist:
       f.write ("%s,%s\n"%(i.name.upper(),i.author.title()))
    f.close()               
booklist=[]
running=True
while(running ==True):
    userinput=input("\nEnter the option \n1.Add book to the temporary list\n2.list the books in the temporary list \n3.Read an existing file \n4.save new file\n5. Save existing file\n6.clear the temporary list\n7.exit\n")
    if userinput =="1":
        addlist(booklist)
    elif userinput =="2":
        listbook(booklist)
    elif userinput =="3":
        readbook(booklist)
    elif userinput =="4":
        savenew(booklist)
    elif userinput=="5":
        saveexisting(booklist)
    elif userinput =="6":
        booklist=[]
    elif userinput =="7":
        running=False
    else:
        print ("enter the valid command")
print()
