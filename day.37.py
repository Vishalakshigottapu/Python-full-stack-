'''
Functions -> User Define Functions,Built-in Functions,Anonymous Functions(lambda keyword),Recursive Functions -> procedure oriented programming
Modules->A Python file containing variables,functions and classes,objects
Userdefined modules(import) ,built-in modules,Availble modules (pypi)
'''

def details(name,place):
    """Details to stored"""
    print(f'name is {name}')
    print(f'place is {place}')
#details("vishala","codegnan")

data = {'ids':[12,32,43,23],
        'name':['vishala','swpana','meena','thanu'],
        'batch':['pfs','jfs','da','ds','cse']}

if __name__ == "__main__":#we call __name__ as dunder name
    details("vishala","codegnan")
    print(data)
    print(__name__)

    
