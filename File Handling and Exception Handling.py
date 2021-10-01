#Reading an entire filr in read mode
f = open("file.txt","r")
text = f.read()
print(text)
#Reading the first line charchter by charachter
f = open('file.txt','r')
for line in f.readline():
    print(line)
#Reading an entire fine line by line
f = open('file.txt','r')
for line in f.readlines():
    print(line)
#Reading an entire file charachter by charachter
f = open('file.txt','r')
for line in f.readlines():
    for ch in line:
        print(ch)

#Code for pickling WRITE
import pickle
f1 = open("test.pck","wb")
pickle.dump(12.3, f1)
pickle.dump([1,2,3], f1)
f1.close()

#Code for pickling READ
f = open("test.pck","rb")
x = pickle.load(f)
print(x)
print(type(x))
y = pickle.load(f)
print(y)
print(type(y))


#Exceptions
filename = 'fileA'
try:
    f = open (filename, "r")
except IOError:
    print('There is no file named', filename)


#Exception handling using raise
def inputNumber () :
    x = input ('Pick a number: ')
    if x==17:
        raise ValueError("17 is a bad number")
    return x

inputNumber()

print('Execution Complete')