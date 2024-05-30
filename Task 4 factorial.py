def triangle(N):
    #Base case
    if N==1:
        return 1
    #Recursive Call
    else:
        return N*triangle(N-1)
print(triangle(5))
