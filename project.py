input_list=[]
zoj_list=[]
fard_list=[]

input_list=list(map(int,input("ورودي :").split()))


for number in input_list:
    if number<0:
        input_list.remove(number)

    else:
        pass

for number in input_list:
     if number%2==0:
           zoj_list.append(number)

     else:
           fard_list.append(number)

array1=list(set(zoj_list))
array2=list(set(fard_list))
print("خروجي آرايه زوج" ,array1)
print("خروجي آرايه فرد " ,array2)
