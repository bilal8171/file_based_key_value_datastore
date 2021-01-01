import code_Module as code

code.create('India',1)
code.create('Hindustan',26,180)
code.read('India')
code.read('Hindustan')
code.delete('Hindustan')
#code.modify('India',11)
code.read('India')
code.read('Chennai')
code.create('Develop@r',78)
code.read('Developer')

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
