import mysql.connector
print("This is my project.")
con = mysql.connector.connect(host="localhost",
                              user="root",
                              passwd="root",
                              database="world")
mycursor = con.cursor(buffered=True)

def Menu( ):
    print("BBT SHOWROOM".center(140))
    print("*"*140)
    print("MAIN MENU".center(140))
    print("1.  Insert Details".center(121))
    print("2.  Display Details as per ID Number".center(140))
    print("      a.  Sorted as per ID Number".center(140))
    print("      b.  Sorted as per Model Name".center(140))
    print("      c.  Sorted as per Manufacturer Name".center(148))
    print("      d.  Sorted as per Price".center(136))
    print("      e.  Sorted as per Category".center(138))
    print("      f.  Sorted as per Specification".center(145))
    print("      g.  Sorted as per Buyer Name".center(140))
    print("3.  Search Details as per the ID Number".center(144))
    print("4.  Update Details".center(122))
    print("5.  Delete Details".center(122))
    print("6.  Display the Number of Buyers".center(136))
    print("7.  Display Total Sales".center(128))
    print("8.  Display Price".center(122))
    print("      L. Least Price".center(130))
    print("      H. Highest Price".center(132))
    print("      B. Back".center(123))      
    print("9.  Exit".center(112))
    print("*"*140)

def MenuSort( ):
    print("      a.   Sorted as per ID Number".center(140))
    print("      b.   Sorted as per Model Name".center(140))
    print("      c.   Sorted as per Manufacturer Name".center(140))
    print("      d.   Sorted as per Price".center(140))
    print("      e.   Sorted as per Category".center(140))
    print("      f.    Sorted as per Specification".center(140))
    print("      g.   Sorted as per Buyer Name".center(140))
    print("      h.   Back".center(140))

def MenuPrice( ):
    print("      H.  Highest Price ".center(140))
    print("      L.  Lowest Price".center(140))
    print("     B.  Back".center(140))

def CreateTable( ):
    try:
        mycursor.execute('create table BBT(ID integer,ModelName varchar(30) ,ManufacturerName varchar(30) ,Price integer ,Category varchar(30) ,Specification varchar(30) ,BuyerName varchar(25))')
        print("Table Created")
    except:
        print("Table Exist")
        Insert( )
        
def Insert( ):
    while True:
        ID = int(input("Enter ID :"))
        ModelName = input("Enter Model Name :")
        ManufacturerName = input("Enter ManufacturerName :")
        Price = int(input("Enter Price :"))
        Category = input("Enter Vehicle's Category :")
        Specification = input("Enter Vehicle's Specification :")
        BuyerName = input("Enter Buyer Name :")
        Rec = [ID,ModelName.upper( ),ManufacturerName.upper( ),Price,Category.upper( ),Specification.upper( ),BuyerName.upper( )]
        Cmd = "insert into BBT values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        con.commit( )
        ch=input("Do you want to enter more records")
        if ch == 'N' or ch == 'n':
            break

def DispSortID( ):
    try:
        cmd = "select * from BBT order by ID"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortModelName( ):
     try:
        cmd = "select * from BBT order by ModelName"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
     except:
        print("Table doesn't exist")

def DispSortManufacturerName( ):
    try:
        cmd = "select * from BBT order by ManufacturerName"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortPrice( ):
     try:
        cmd = "select * from BBT order by Price"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
     except:
         print("Table doesn't exist")

def DispSortCategory( ):
    try:
        cmd = "select * from BBT order by Category"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortSpecification( ):
    try:
        cmd = "select * from BBT order by Specification"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortBuyerName( ):
    try:
        cmd = "select * from BBT order by BuyerName"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s "
        print(F % ("ID","ModelName","ManufacturerName","Price","Category","Specification","BuyerName"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print( )
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSearchID( ):
        ch = input("Enter the ID Number to show the details:")
        cmd = "select * from BBT where ID='%s'"%(ch)
        mycursor.execute(cmd)
        data = mycursor.fetchall( )
        print(data)

def Update( ):
    try:
        cmd = "select * from BBT "
        mycursor.execute(cmd)
        A = int(input("Enter the ID whose detail to be changed"))
        for i in mycursor:
            i=list(i)
            if i[0] == A:
                ch=input ("Change ModelName(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter ModelName")
                    i[1]=i[1].upper( )
                ch=input ("Change ManufacturerName(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter ManufacturerName")
                    i[2]=i[2].upper( )
                ch=input ("Change Price(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=int(input("Enter Price"))
                ch=input ("Change Category(Y/N)")
                if ch=='y' or ch=='Y': 
                    i[4]=input("Enter Category")
                    i[4]=i[4].upper( )
                ch=input ("Change Specification(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter Specification")
                    i[5]=i[5].upper( )
                ch=input ("Change BuyerName(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter BuyerName")
                    i[6]=i[6].upper( )
                cmd="Update BBT set BuyerName=%s, ManufacturerName=%s, Price=%s, Category=%s, Specification=%s, BuyerName=%s where ID=%s"
                val=(i[1], i[2], i[3], i[4], i[5], i[6], i[0])
                mycursor.execute(cmd,val)
                con.commit( )
                print("Details Updated !")
                break
        else:
            print("Record not found")
            
    except:
        print("No such table")

def Delete( ):
    try:
        A=int(input("Enter the ID whose details to be changed"))
        cmd="Delete from BBT where ID =%s"%(A)
        mycursor.execute(cmd)
        con.commit( )
        print("Records are deleted")
    except:
        print("No such table")

def BuyerNumber( ):
    cmd = "select * from BBT"
    mycursor.execute(cmd)
    print("No. of Buyers:",mycursor.rowcount)

def TotalSales( ):
    mycursor.execute("Select sum(Price) from BBT")
    print("Total income from the sales",mycursor.fetchall()[0][0])

def LeastPrice( ):
  mycursor.execute("Select MIN(Price) as LeastPrice from BBT")              
  result = mycursor.fetchall() 
  for i in result: 
    minimum= float(i[0]) 
    print("Least Price:",minimum)
    
def HighestPrice( ):
  mycursor.execute("Select MAX(Price) as HighestPrice from BBT") 
  result = mycursor.fetchall() 
  for i in result: 
    maximum = float(i[0]) 
    print("Highest Price:",maximum)

while True:
    Menu( )
    ch = int(input("Enter your choice :"))
    if ch == 1:
        CreateTable( )
    elif ch == 2:
        while True:
            MenuSort( )
            sch = input("Enter your sorting choice :")
            if sch == "a":
                DispSortID( )
            elif sch == "b":
                DispSortModelName( )
            elif sch == "c":
                DispSortManufacturerName( )
            elif sch == "d":
                DispSortPrice( )
            elif sch == "e":
                DispSortCategory( )
            elif sch == "f":
                DispSortSpecification( )
            elif sch == "g":
                DispSortBuyerName( )
            elif sch == "h":
                break
            else:
                print("Invalid choice!")
        else:
            print("Table doesn't exist.")
    elif ch == 3:
        DispSearchID( )
    elif ch == 4:
        Update( )
    elif ch == 5:
        Delete( )
    elif ch == 6:
        BuyerNumber( )
    elif ch == 7:
        TotalSales( )
    elif ch == 8:
        while True:
            MenuPrice( )
            dch = input("Enter your choice of price :")
            if dch == 'H':
                HighestPrice( )
            elif dch == 'L':
                LeastPrice( )
            elif dch == 'B':
                break
            else:
                print("Invalid choice!")
        else:
            print("Table doesn't exist.")
    elif ch == 9:
        break
    else:
        print("Invalid choice!")
 
 
 
 
 
 
 
                 
                 
           
         
         
       
      

    
 
                
                 
 
 
 
 
 
