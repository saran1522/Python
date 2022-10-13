#*********opening and reading a file*********
'''# o=open("sample.txt")   by default it is opened in reading mode
o=open("sample.txt", "r") # it will open the file in reading mode
content=o.read() # reading the file
# o.read(5) will read first 5 character from the file
print(content)
o.close() #it wiil close the file'''

#**********reading a file line by line************
'''f=open("sample.txt", "r")
data=f.readline() # it will read only 1st line
print(data)
data=f.readline() # it will read 2ne line... and so on..........
f.close()
print(data)'''

n=input("")
vi="1"
decimal="0"
while n>0:
    rem=n%10
    decimal=rem*vi+decimal
    vi=vi*10
    n=n/10
print(decimal)