def create_account():
    print("enter new account number")
    acc=int(input(""))
    my=open("file.txt","r")
    list1=[]
    for line in my:
        line_strip=line.strip()
        line_split=line_strip.split()
        list1.append(line_split)
        
    my.close()
    
    list_final=[]
    for i in list1:
        for j in i:
            list_final.append(j)

    
    newacc=str(acc)
    
    if newacc in list_final:
        print ("this accoun number is alrady used")
        
    else:
        print("diposit amount")
        bal=int(input(""))
    
        details = acc
        details1=bal
        with open('file.txt','a') as data: 
            data.write(str(details))
            data.write("\n")
            data.write(str(details1))
            data.write("\n")
         
def cash_deposite():
    accno=int(input("enter your account number"))
    acc=str(accno)
    my=open("file.txt","r")
    list1=[]
    for line in my:
        line_strip=line.strip()
        line_split=line_strip.split()
        list1.append(line_split)

    my.close()
    v=0
    
    list_final=[]
    for i in list1:
        for j in i:
            list_final.append(j)
    try:
        while True:
        
            if  list_final[v]==acc:
                bal=int(input("diposit amount"))
                dip=int(list_final[v+1])
                dip=dip+bal
                #return ("your transaction is a success")
                print("your transaction is a success")
                print("amount in account Rs",dip)
                print("\n")      
                dipnew=str(dip)
                #print (v)
                #print (list_final)
                list_final[v+1]= dipnew

                with open('file.txt','w') as d:
                    for i in list_final:
                        d.write(i)
                        d.write("\n")
                    
                                            
                break
            else:
                v=v+2
                continue
    except:
        print("invalid account number\n")

def cash_withdraw():
    accno=int(input("enter your account number"))
    acc=str(accno)
    bal=int(input("withdraw amount"))
    my=open("file.txt","r")
    list1=[]
    for line in my:
        line_strip=line.strip()
        line_split=line_strip.split()
        list1.append(line_split)

    my.close()
    v=0
    
    list_final=[]
    for i in list1:
        for j in i:
            list_final.append(j)
    try:
        while True:
        
            if  list_final[v]==acc:
                dip=int(list_final[v+1])
                if dip>=bal:
                    dip=dip-bal
                    #return ("your transaction is a success")
                    print("your transaction is a success")
                    print("amount in account Rs",dip)
                    dipnew=str(dip)
                    #print (v)
                    #print (list_final)
                    list_final[v+1]= dipnew
                
                    #print (list_final)
                    #for new_dep in list_final:
                    #whatweneed=new_dep.replace(list_final[v+1],dipnew)
                    #newlist.append(whatweneed)
                    #print(newlist)
                    with open('file.txt','w') as d:
                        for i in list_final:
                            d.write(i)
                            d.write("\n")                      

                    break
                else:
                    print("You don't have enough money \n")
                    break
            else:
                v=v+2
                continue
    except:
        print("invalid account number")

def loan_cal():
    x=0
    y=0
    ins=0
    cal=0
    ly=0
    intr=0
    y=int(input("enter the loan amount"))
    print("1.3 year")
    print("2.5 year")
    print("3.7 year")
    print("4.more than 7 year")
    ins=int(input("select"))

    if (ins==1):
        intr=((y*0.15)*3)
        #return(intr+y)/36
        cal = (intr+y)/36
        
    elif (ins==2):
        intr=((y*0.2)*5)
        #return((intr+y)/60)
        cal = (intr+y)/60
        
    elif (ins==3):
        intr=((y*0.25)*7)
        #return((intr+y)/84)
        cal = (intr+y)/84
        
    elif (ins==4):
        print("number of year")
        ly=int(input(""))
        intr=((y*0.3)*ly)
        #return((intr+y)/(ly*12))
        cal = (intr+y)/(ly*12)
        
    print ("intrest %f"%intr)        
    print ("Monthly installment %f \n"%cal)

def account_incuiry():
    accno=int(input("enter your account number"))
    acc=str(accno)
    my=open("file.txt","r")
    list1=[]
    for line in my:
        line_strip=line.strip()
        line_split=line_strip.split()
        list1.append(line_split)
    my.close()

    v=0
    list_final=[]
    for i in list1:
        for j in i:
            list_final.append(j)

    try:
        while True:
        
            if  list_final[v]==acc:
                return (list_final[v+1])
                print ("your account balance is:Rs.",list_final[v+1],"\n")
                break
            else:
                v=v+2
                continue
    except:
        print("invalid account number")
    



main=0
acc=0
bal=0
while main!=6:
     print("1.create acccount")
     print("2.cash deposit")
     print("3.cash withdraw")
     print("4.loan calculate")
     print("5.account inquiry")
     print("6.close")
     main=int(input("\tenter the number"))
    
     if (main==1):
         create_account()
  
     elif (main==2):
         cash_deposite()
               
     elif (main==3):
         cash_withdraw()
          
     elif (main==4):
         loan_cal()
       
     elif (main==5):
         account_incuiry()
   
     elif (main==6):
         print ("exit")
         break
