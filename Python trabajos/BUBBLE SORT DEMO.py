arr=[6,5,3,1,8,7,2,4]



for i in range(len(arr)):
    for j in range(i):
        if arr[j+1]<arr[j]:
            arr[j], arr[j+1]=arr[j+1],arr[j]#la coma sirve para comparar darle una pocicion a los dos elementos que estoy poniendo, despues del igual y poner la coma en lo que esta despues
            #lo compara segun la pocicon, la coma determina el lugar de algo que se compara en este caso


print(arr)
