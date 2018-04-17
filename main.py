#FileName: main.py
#Creator: Sirus Das
from LL import LL

ll = LL()

def ask():
	return input("\n Please Enter \n 1. Insert at Start \n 2. Insert at End \
			\n 3. Display values \n 4. Remove any value \n 5. Exit \n" )

def compute(x):
	if x == '1':
			y = 'sirus'
			while y != '': #looop will exit if u enter nothing!
				y = input("Enter a value to insert ")
				ll.insertStart(y)
		
	elif x=='2':
			y = 'sirus'
			while y != '': #looop will exit if u enter nothing!
				y = input("Enter a value to insert ")
				r  = ll.insertEnd(y)
				if r == 0: y = ''
	elif x=='3':
		ll.traverseList()
	elif x=='4':
			y = 'sirus'
			while y != '': #looop will exit if u enter nothing!
				y = input("Enter the value to remove ")
				r = ll.remove(y)
				if r == 0: y = ''
	
	elif x=='5':
		return 0
		
	return 1
	
	'''
	switcher = {
		1: ll.insertStart(x),
		2: ll.insertEnd(x),
		3: ll.traverseList(),
		4: ll.remove(input("Enter the value to remove ")),
		5: "false"
	}
	print (switcher.get(x, "false"))
	'''
	  
	  
while(compute(ask())):
	pass
'''
ll.insertStart(12)
ll.insertStart(34)
ll.insertStart(56)
ll.insertEnd(76)

ll.traverseList()

ll.remove(56)

ll.traverseList()
'''