from threading import *
import time
import json

#For colors of the error message
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[92m'

lock = Lock() #locking the mechanisms to synchronize threads

#My main datastore
data_file={}

#json validator
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        return False

#Create operation
def create(key,value,timeout=0):
    if key.isalpha():
        if (json_validator(value)):
            if len(key)<=32:
                if key in data_file:
                    print(CRED +"Error: key '"+key+"', already exists."+ CEND) #error message if the key already exist in the file
                else:
                    if len(bytes(value,'utf-8'))<=(16*1024) and len(data_file)<(1024*1024*1024):
                        if timeout==0:
                            v=[value, timeout]
                        else:
                            v=[value, time.time()+timeout]
                        lock.acquire()    
                        data_file[key]=v
                        lock.release()    
                    else:
                        print(CRED + "Error: Storage limit exceeded." + CEND) #error message if JSON object value less than 16KB and file size less than 1GB
            else:
                print(CRED + "Error: Length of key must be less than or equal to 32. " + CEND) #error message if length of key_name capped at 32chars
        else:
            print(CRED +"Error: value '"+value+"', is not a valid JSON object." + CEND) #error message if value is not a JSON object
    else:
        print(CRED +"Error: Invalid key. Characters in the key should only be alphabets."+ CEND) # error message if key is not a string of alphabets only

#Read operation
def read(key):
    if key in data_file:
        lock.acquire() 
        vals=data_file[key]
        lock.release()
        if vals[1]==0 or time.time()<vals[1]:
            return key+':'+str(vals[0])
        else:
            print(CRED + "Error: Time-To-Live for '" + key + "', has expired." + CEND)#if current time exceeds time-to-live property value
    else:
        print(CRED +"Error: key '"+key+"', is not found in the database."+ CEND)

#Delete operation
def delete(key):
    if key in data_file:
        vals = data_file[key]
        if vals[1] == 0 or time.time() < vals[1]:
            lock.acquire() 
            del data_file[key]
            lock.release()
            print(CGREEN+ "key '"+key +"' deleted successfully." + CEND)
        else:
            print(CRED + "Error: Time-To-Live for '" + key + "', has expired." + CEND)#if current time exceeds time-to-live property value

#just to display
def show():
    print(data_file)
