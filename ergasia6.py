import random
x = int(input("dwse ypsos"))
y = int(input("dwse platos"))
bomb = int(input("dwse arithmo apo vomves"))
a = [[0] * y for i in range(x)]

for i in range (0,bomb):
    row = random.randint(1,x-1)
    col =  random.randint(1,y-1)
    while True:
        if a[row][col] == '*':
            row = random.randint(1,x-1)
            col =  random.randint(1,y-1)
        else:
            break
            
    a[row][col] = '*'
    
for i in range (0,x):
    for z in range (0,y):
        n = 0
        if a[i][z] == 0:
            if i>0:
                if a[i-1][z] == '*':#panw
                    n+=1
            if z>0:
                if a[i][z-1] == '*':#aristera
                    n+=1
            if z>0:
                if i>0:
                    if a[i-1][z-1] == '*':#panw aristera
                        n+=1
            if z<y-1:
                if i<x-1:
                    if a[i+1][z+1] == '*':#katw dexia
                        n+=1
            if z<y-1:
                if a[i][z+1] == '*':#dexia
                    n+=1
            if i<x-1:
                if z>0:
                    if a[i+1][z-1] == '*':#katw aristera
                        n+=1
            if i<x-1:
                if a[i+1][z] =='*':#katw
                    n+=1
            if i>0:
                if z<y-1:
                    if a[i-1][z+1] == '*':#panw dexia
                        n+=1
            a[i][z] = n
                
        
            
for row in a:
    print(' '.join([str(elem) for elem in row]))
    
        
