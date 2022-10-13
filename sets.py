# ***********sets in python*******
'''set1={3,4,1,44}
print(set1)
# a() will create empty dictionary 
a=set() # will creare empty set, now a is empty set
#  we can add tuples in sets but we can not add list or liabrary in set,
#  because they are not hashable means we can change their value
a.add(3) #it will add 3 into set
a.add(5)'''

s={1,4,5,6, (1,3,3,5)}
print(type(s))
print(s)
print(s.pop())
s.remove(4)
print(s)
print(len(s))
print(s.union({8,(1,3,3,5)}))
print(s.intersection({2,3,6,5}))
print(s)
s.clear()