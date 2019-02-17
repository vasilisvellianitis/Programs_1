import random
a = [[0] * 3 for i in range(3)]
for row in a:
    print(' '.join([str(elem) for elem in row]))#typwma pinaka


nikhths = 0
n = 1
#xekinaei prwtos o xrhsths
while True:
    if n % 2 == 1:
        z = int(input("dwse syntetagmenh ypsous"))
        y = int(input("dwse syntetagmenh platous"))
        a[z][y] =  1
    else:
        print ("Computer is loading")
        while True:
            z = random.randint(0,2)
            y = random.randint(0,2)
            if a[z][y] == 0:
                a[z][y] =  'x'
                break
    #xekinaei o elegxos an exei nikhsei kapoios
    if (a[0][0] == 1 and a[0][1] == 1 and a[0][2] == 1):#orizontia1
        nikhths = 1
        break
    if (a[1][0] == 1 and a[1][1] == 1 and a[1][2] == 1):#orizontia1
        nikhths = 1
        break
    if (a[2][0] == 1 and a[2][1] == 1 and a[2][2] == 1):#orizontia1
        nikhths = 1
        break
    if (a[0][0] == 1 and a[1][0] == 1 and a[2][0] == 1):#katheta1  
        nikhths = 1
        break
    if (a[0][1] == 1 and a[1][1] == 1 and a[2][1] == 1):#katheta1
        nikhths = 1
        break
    if (a[0][2] == 1 and a[1][2] == 1 and a[2][2] == 1):#katheta1
        nikhths = 1
        break
    if (a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1):#diagwnia1
        nikhths = 1
        break
    if (a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1):#diagwnia1
        nikhths = 1
        break
    if (a[0][0] == 'x' and a[0][1] == 'x' and a[0][2] == 'x'):#orizontia2
        nikhths = 2
        break
    if (a[1][0] == 'x' and a[1][1] == 'x' and a[1][2] == 'x'):#orizontia2
        nikhths = 2
        break
    if (a[2][0] == 'x' and a[2][1] == 'x' and a[2][2] == 'x'):#orizontia2
        nikhths = 2
        break
    if (a[0][0] == 'x' and a[1][0] == 'x' and a[2][0] == 'x'):#katheta2
        nikhths = 2
        break
    if (a[0][1] == 'x' and a[1][1] == 'x' and a[2][1] == 'x'):#katheta2
        nikhths = 2
        break
    if (a[0][2] == 'x' and a[1][2] == 'x' and a[2][2] == 'x'):#katheta2
        nikhths = 2
        break
    if (a[0][0] == 'x' and a[1][1] == 'x' and a[2][2] == 'x'):#diagwnia2
        nikhths = 2
        break
    if (a[0][2] == 'x' and a[1][1] == 'x' and a[2][0] == 'x'):#diagwnia2
        nikhths = 2
        break
    n+=1
    for row in a:                
        print(' '.join([str(elem) for elem in row]))

for row in a:                
        print(' '.join([str(elem) for elem in row]))
if nikhths == 1:
    print ("Nikhsate!!!")
elif nikhths == 2:
    print ("O ypologisths se nikhse")
else:
    print ("isopalia")

    
    
    
    


