# fx,y = 3xxy
# h=0.1
#x0=0
#x0
#y1

def jeho(x,y):
    return 3 *x*x*y

def euler(x0, y, h, x):
    
    while x0 < x:
        y = y+h*jeho(x0, y)
        x0 = x0+h
        print('Approximate solution of y at x = ', "%.1f"%x0 ,' is, ', "%.8f"%y)
        
    
x0 = 0
x = 1
h = 0.1
y = 1
euler(x0, y, h, x)