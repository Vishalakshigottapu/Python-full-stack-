'''
fro<temp> in range(obj):
Doc
Nested Loops -->(for in for) - these are primarily used for pattern printings
Matrix Operations and problems solving scenarios (data structures)

syntax:
for i in range(outer_loop_range):
    for j in range(inner_loop_range): #inner loop will be completely executed
                                      #for every outer loop
        #code block

for i in range(3): #->0,1,2
    for j in range(2):#j->0,1
        print(f'i = {i},j = {j}')
#In above case for complete j values of 0 i value will be 0,1,2 and follws
# same for others

for i in range(3): # in this case both i and j are same 
    for j in range(3):
        print(i,j)

for i in range(3): 
    for j in range(3):
        print(i,j,end=' ') #now entire result will be in single line
        print('python')
    #print('Codegnan')
    print() #only when inner loop is complete before starting outer loop it generates

for i in range(2): #i ->0,1
    for j in range(i): #first i value will be 0 loop doesn't start fro j 
        print(f'i = {i},j={j}')

for i in range(3):
    for j in range(i+1):
        print(f'i = {i},j = {j}')

#Now lets links above to patterns
for i in range(5): 
    for j in range(4):
        print('*',end = "   ")
    print()


#same as square patterns we just change inner loop
for i in range(3): 
    for j in range(4):
        print(j+1,end= ' ')
    print()

#Now keeping both start and end values
for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()
#outer loop rows
#inner loop column
for i in range(1,5):
    for j in range(4):
        print(i,end = ' ')
    print()

#for above number grid lets take square patterns as example
num = 1
for i in range(3):
    for j in range(3):
        print(num,end=" ")#check here by changing end argment
        num+=1
    print()



'''

for i in range(4):
    for j in range(4):
        print(chr(65 + j), end=" ")
    print()
       
for i in range(4):
    for j in range(4):
        print(chr(65 + i), end=" ")
    print()
        
    
            
