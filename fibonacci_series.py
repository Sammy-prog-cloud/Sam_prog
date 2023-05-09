#Fibaonacci series
#The sum of two elements define the next
a, b = 0, 1
while a < 10:
    print(a, b)
#The while loop keeps printing until a stop loop has been inputed in the code
    # which brings about the next code included to stop the while loop
    a, b = b, a + b
