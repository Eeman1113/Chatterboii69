import string


def convert(lst):
  return (lst[0].split())

def line_maker():        
    lines=[]
    file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/testing1.txt", "w+")
    with open ('/Users/eemanmajumder/code_shit/abstract/Student /text/recognized.txt', "r") as f:
      lines = [line.rstrip() for line in f]
    
    for i in lines:
      if i=='':
        lines.remove(i)
    file.write(str(lines))
    file.close()
    
    return lines

def extractDigits(lst):
    return [[el] for el in lst]
                

file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/recognized.txt", "r")
j=file.read()
k=[]
k.append(j)
l=convert(k)
#print(l)
print(line_maker())
r=line_maker()
q=extractDigits(r)
r=len(q)
m=0
for i in range(0,r):
  m=q[i]
  q.append(convert(m))
file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/tokenised.txt", "w+")

print(q)
file.write(str(q))
file.close()
x=0
y=0
file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/error.txt", "w+")
for i in range(0,len(q)-1):
  x=len(q[i])
  if i==len(q)-1:
    file.write("\n line 47")
    break

  else:
    y=len(q[i+1])
    
  if  x>1 and y>1:
     if q[i][0]==q[i+1][0] and q[i][1]==q[i+1][1]:
       
       if x>y:
         q.remove(q[i+1])
       else:
         q.remove(q[i])
   
     else: 
       file.write("\n line 65")
       continue
  else:
    file.write("\n line 68")
    continue
file.close()
file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/tokenised.txt", "w+")
file.write(str(q))
file.close()
   