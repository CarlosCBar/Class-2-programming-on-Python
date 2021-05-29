#VARIABLES


# CREATING VARIABLES
a= 5
b= 'Perro'
c= str(3)     # will be '3' Text
d= int(3)     # will be 3
e= float(3)   # will be 3.0



# KNOWING THE DATA TYPE
print(type(c))



# NOT THE SAME VARIABLE
# PYTHON IS CASE SENSITIVE
A = 4
a = 'doggy name'
print(a)
print(A)


#RULES FOR VARIABLE NAMES

'''
A NAME MUST START WITH A LETTER OR THE UNDERSCORE CHARACTER
CANNOT START WITH A NUMBER
THE VARIABLE NAME CAN ONLY USE ALPHA NUMERIC CHARACTERS AND UNDERSCORES
VARIABLE NAMES ARE CASE-SENSITIVE
'''

'''
ACCEPTED NAMES
myvar
my_var
_my_var
myVar
MYVAR
MYVAR2
'''

'''
ILLEGAL NAMES
2myvar
my-var
my var
'''

#HOW TO MAKE NAMES MORE READABLE


# CAMEL CASE
myVariableName = 'CCB'


# PASCAL CASE
MyVariableName = 'CCB'



# SNAKE CASE
my_variable_name = 'CCB'


#ASSIGN MULTIPLE VALUES


x, y, z = 'duck', 'rabbit', 'bear'

x = y = z = 'duck', 'rabbit', 'bear'


#UNPACK A COLLECTION

fruits = ['pomelo', 'watermelon', 'grape']
x, y, z = fruits
print(x)
print(y)
print(z)


#OUTPUT VARIABLES

a = 'awesome'
print ('Programming with Python is ' + a)


b= 'Python is '
c= 'awesome'
d= a+b
print (d)


e= 5
f= 89
print (e+f)

#GLOBAL VARIBLES


# CREATE A VARIABLE OUTSIDE OF A FUNCTION, ANS USE IT INSIDE THE FUNCTION

x= 'awesome'

def myfunc():
    print('Python is ' + x)

myfunc()  #CADA QUE LLAMES A LA FUNCIÓN SE IMPRIMIRÁ


#PUEDES IMPRIMIR DOS FUNCIONES DISTINTAS AL MISMO TIEMPO
'''
ej
myfunc();my_func() 
ESTO IMPRIMIRÁ AMBAS FUNCIONES EN DOS LINEAS DISTINTAS
'''
