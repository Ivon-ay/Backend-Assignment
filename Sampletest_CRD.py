import CRD as c #importing the modularized CRD.py

c.create('12','52') #Create with ivalid key, error
#o/p=>Error: Invalid key. Characters in the key should only be alphabets.

c.create('Age','xyz') #Create with invalid value error
#o/p=>Error: value 'xyz', is not a valid JSON object.

c.create('abcdefghijklmnopqrstuvwxyzabcdefg','33') #create with #char error
#o/p=>Error: Length of key must be less than or equal to 32.

#c create with key,value given (no error)
c.create('Age','25')
c.create('Movie','{"actors":{"actor":[{"id":"1","firstName":"Tom","lastName":"Cruise"}]}}')
c.create('People','{"emp_name":"Noviya","emp_no.":["noviya2000@gmail.com"]}')
c.show()
#o/p=>{'Age': ['25', 0], 'Movie': ['{"actors":{"actor":[{"id":"1","firstName":"Tom","lastName":"Cruise"}]}}', 0], 'People': ['{"emp_name":"Noviya","emp_no.":["noviya2000@gmail.com"]}', 0]}

c.create('Age','26') #check if already exists
#o/p=>Error: key 'Age', already exists.

c.read('People') #read by providing the key
#o/p=>'People:{"emp_name":"Noviya","emp_no.":["noviya2000@gmail.com"]}'

c.read('Age') #read by providing the key
##o/p=>'Age:25'

c.read('xyz') #read, but not foud in database
#o/p=>Error: key 'xyz', is not found in the database.

c.delete('Movie') #delete by providing the key
c.show() #displaying the datas
#o/p=>key 'Movie' deleted successfully.
#{'Age': ['25', 0], 'People': ['{"emp_name":"Noviya","emp_no.":["noviya2000@gmail.com"]}', 0]}

c.create('Types','50',60) #create with key,value given and with time-to-live property value given(number of seconds) 
c.show()
#o/p=>{'Age': ['25', 0], 'People': ['{"emp_name":"Noviya","emp_no.":["noviya2000@gmail.com"]}', 0], 'Types': ['50', 1606849604.1571605]}

c.read('Types')#read within time-to-live property value-1 min(60s)
#o/p=>'Types:50'

c.read('Types')#read after time-to-live property value
#o/p=>Error: Time-To-Live for 'Types', has expired.

c.delete('Types') #delete after time-to-live property value
#o/p=>Error: Time-To-Live for 'Types', has expired.

#CRD library throws error if size of the file storing data exceeds 1GB.
#And it is thread-safe by locking mechanisms to synchronize threads.
