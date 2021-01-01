from threading import*
import time

database={}            #Actually its dictionary
def create(k,v,timeout=0):
    if k in database:
        print("error: this key already exists")
    else:
        if(k.isalpha()):
            if len(database)<(1024*1024*1024) and v<=(16*1024*1024): 
                if timeout==0:
                    l=[v,timeout]
                else:
                    l=[v,time.time()+timeout]
                if len(k)<=32: 
                    database[k]=l
                    print('Key, value has been inserted in Databases')
                 
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")


            
def read(k):
    if k not in database:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=database[k]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(k)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                print(stri)
            else:
                print("error: time-to-live of",k,"has expired") 
        else:
            stri=str(k)+":"+str(b[0])
            print(stri)



def delete(k):
    if k not in database:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=database[k]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del database[k]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",k,"has expired") #error message5
        else:
            del database[k]
            print("key is successfully deleted")



def modify(k,v):
    b=database[k]
    if b[1]!=0:
        if time.time()<b[1]:
            if k not in database:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(v)
                l.append(b[1])
                database[k]=l
        else:
            print("error: time-to-live of",k,"has expired")
    else:
        if k not in database:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(v)
            l.append(b[1])
            database[k]=l
            print('Database after Modification key --> {} '.format(database))