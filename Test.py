from operator import truediv

print("Test Message") #String
print(-111)
print(123.4) #Float

print(None) #Null or None
print(False) #Boolean

print(type("Test Message"))
print(type(123.5))
print(type(False))
print(['Inimene1','Inimene2','Inimene 3'])
print([{
    'name': 'Inimene1',
    'age': 28,
    'address': 'This street, That City'
}])
#Excercise1

print("This is a standard text sequence.") #string
print(-4) #integer?
print(0) #integer?
print(13.676) #Float
print(True) #Boolean
print(None) #Null
print(b'This is a byte text sequence.') #? String Sequence?
print([1,2,3,4,5,6,7,8]) #list
print([{'name' : 'xyz'}]) #string


#Excercise2
"""
score = 80

if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
else:
    result = 'F'

print(result)
"""
age = 17
has_license = 0

if age >= 18 and has_license >= 1:
    result = 'Adult with license'
elif age >= 18 and has_license <= 0:
    result = 'Adult without license'
elif age < 18:
    result = 'Minor'

print(result)

#End