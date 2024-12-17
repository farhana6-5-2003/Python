#Write a python program to concatenate 2 dictionaries to create a new one
#dict1=name and age
#dict2=city and gender

dict1={"name":"John","age":"35"}
dict2={"city":"Newyork","gender":"M"}
dict1.update(dict2)
print(dict1)
d3=dict1|dict2
print(d3)
