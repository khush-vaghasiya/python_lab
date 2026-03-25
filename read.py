f = open("read.txt","r")
data = f.read()
print("file.content:",data)
f.close()


f = open("read.txt","r")
data = f.read(10)
print("first part:",data)
f.close()

f = open('read.txt', 'r') 
line1 = f.readline() 
line2 = f.readline()      
print('line 1:', line1.strip())
print('line 2:', line2.strip())

f = open('read.txt', 'r')
lines = f.readlines()
f.close() 
print('list of lines:', [line.strip() for line in lines]) 
print('number of lines:', len(lines))


f = open("read.txt","r")
lines = f.readlines()
print(lines[1].strip())
f.close()
