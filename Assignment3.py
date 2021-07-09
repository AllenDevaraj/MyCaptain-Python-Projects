#Assignment 3 Task 1
#To display frequency of letters using dict
s = input('Please enter a string: ')
s = s.lower()
d = {}

def getkey(d,val):
	      for k,v in d.items():
		      if v == val:
			      return k

def most_frequent(s,d):
  for i in s:
    if i not in d:
      d[i] = 1
    else:
      d[i] += 1
  for i in sorted (d.values(),reverse=True):
    print(getkey(d,i),'=',i,end = '\n')

#Thank you
