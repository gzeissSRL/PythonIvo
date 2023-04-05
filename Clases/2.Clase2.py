#Listas

my_list = list()
my_other_list = []

print(type(my_list))
print(type(my_other_list))

list = [1,2,3,4,5,6,7,8]

print(list.count(1))
print(len(list))

list_user = ['gonzalo', 'zeiss', 'zeiss', 27, False]

print(list[5])#ve el contenido en la 6 posicion de la lista

name, lastname, apodo, ege, casado = list_user

print(lastname)

list_user.append(False)#agrega al final

print(list_user)

list_user.insert(1,'insert')#inserta en una posicion especifica

print(list_user)

list_user.remove('zeiss')#elimina el primer elemento que encuentra

print(list_user)

list_user.pop()#Devuelve ultimo valor de la lista

print(list_user)

print(list_user.pop())

print(list_user)

lista2 = list_user.copy()#Copia la lista

list3 = [22,1,5,100]

list3.sort()#ordena lista 

print(list3)

del list3[2]#elimina el elemento sin retorno 

#del list3

print(list3)

list3.clear()

print(list3)

my_set = set()
my_newSet = {}
my_newSet = {'gonzalo', 'zeiss', 27}

print(type(my_set))
print(type(my_newSet))

print(my_newSet)

my_newSet.add(10)

my_newSet.pop()

print(my_newSet)

my_dic = {'gonzalo':'12335','pedro':'2732621','juan': 12831,'lenguajes':["c#","Python","java"]}

print(my_dic['lenguajes'][1])

my_dic['gonzalo'] = 'zeiss'

print(my_dic['gonzalo'])

print('gonzalo' in my_dic)

print(my_dic.items())
print(my_dic.keys())
print(my_dic.values())


#Los caracteres tienen unv alor numerico en python 
if('ab' > 'ac'):
    print('true')
else:
    print('false')


#Funciones

def hola():
    print('hola')
def chau():
    print('chau')

hola()
chau()
chau()





'''
funtions_list_new = funtions_list.copy()#copia la lista

funtions_list_new.sort()#ordena la lista 

del funtions_list[1] #elimina el elemento sin retorno como con el pop()

print(funtions_list)

funtions_list.clear() #borra todo el contenido de la lista

print(funtions_list)
print(funtions_list_new)
'''