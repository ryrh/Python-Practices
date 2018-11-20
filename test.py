import re
m=re.search(r'\\s','\s')
print(m.group())

print('\\')
print(r'\\s')

n=re.search(r'\\n','\\n')
print(n.group())

'''
n=re.search(r'\n','\\n')
print(n.group())
'''

d=re.search(r'\\','\\\\')
print(d.group())


c=re.search(r'\\\\','\\\\')
print(c.group())


a=re.search(r'ABC\\n123',r'ABC\n123')
print(a.group())


b=re.search(r'ABC\\s123','ABC\s123')
print(b.group())
