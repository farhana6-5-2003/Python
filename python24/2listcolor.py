#Create 2 lists of colours,List1 with colours red,blue,green,yellow,purple and List2 with colours blue,yellow,pink.Use a set to find colours in List1 that #are not in List2.
list1=["red","blue","green","yellow","purple"]
list2=["blue","yellow","pink"]
result=set(list1)-set(list2)
print("Colours in list1 not in list2:",result)
print(list(result))

