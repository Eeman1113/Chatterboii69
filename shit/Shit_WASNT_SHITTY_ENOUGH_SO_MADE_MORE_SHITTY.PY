def convert(lst):
      return (lst[0].split())
         
def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res
 
    
file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/error.txt", "r")
j=file.read()
k=[]
k.append(j)
l=convert(k)
c=remove_items(l, 'line')
print(c)


x,y,z=0,0,0
for i in range(0,len(c)):
    #count number of times 47,65,68 appears
    if c[i]=='47':
        x=x+1
    elif c[i]=='65':
        y=y+1
    elif c[i]=='68':
        z=z+1
    else:
        continue

print("\n x=",x,"\n y=",y,"\n z=",z)
import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'47':x, '65':y, '68':z,}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='black',
		width = 0.4  )

plt.xlabel("Name of error")
plt.ylabel("number of times error occured")
plt.title("Where eeman is wrong?")
plt.show()

