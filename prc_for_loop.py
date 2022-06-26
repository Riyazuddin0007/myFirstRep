from asyncio.windows_events import NULL


# def fun_tri(_range):
#     for i in range(_range):
#         for j in range(i,_range):
#             print("*",end=" ")
#         print(" ")
#     return " "

# print(fun_tri(10))

# def fun_tri(_range):
#     for i in range(_range):
#         for j in range(i,_range):
#             print(" ",end=" ") 
#             # print blank spaces
#         for k in range(i+1):
#             print("*",end=" ")
#             # print * trinagel 1
#         for k in range(i):
#             print("*",end=" ")
#             # print * trinagel 2
#         print(" ")
#     return " "

# print(fun_tri(5))



# def fun_tri(_range):
#     for i in range(_range):
#         for j in range(i):
#             print(" ",end=" ") 
#             # print blank spaces

#         for k in range(i,_range):
#             print("*",end=" ")
#             # print * trinagel 2
        
#             # print blank spaces
#         for k in range(i,_range-1):
#             print("*",end=" ")
#         #     # print * trinagel 1
        
#         print(" ")
#     return " "





# dimond shape

def fun_tri(_range):
    for i in range(_range-1):
        for j in range(i,_range-1):
            print("  ",end="") 
            # print blank spaces
        for k in range(i+1):
            print("* ",end="")
            # print * trinagel 1
        for k in range(i):
            print("* ",end="")
            # print * trinagel 2
        print("")
        # main lower triangel 
    for i in range(_range):
        for j in range(i):
            print("  ",end="") 
            # print blank spaces

        for k in range(i,_range):
            print("* ",end="")
            # print * trinagel 2
        
            # print blank spaces
        for k in range(i,_range-1):
            print("* ",end="")
        #     # print * trinagel 1
        
        print(" ")
    return " "


print(fun_tri(3))




