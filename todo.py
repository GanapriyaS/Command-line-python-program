import sys
import os
import datetime
a=sys.argv[1:]
if(a==[]):
	print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')
else:
	if(a[0]=="help"):
		print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')

	elif(a[0]=="ls"):
		a=os.path.exists('todo.txt')
		if(a==False):
			print("There are no pending todos!")
		else:	
			with open('todo.txt','rt') as f1:
				s1=f1.readlines()
			if(s1==[] or os.path.getsize('todo.txt')<=0):
				print("There are no pending todos!")
			else:
				for i in range(len(s1)-1,-1,-1):
					print("[{0}] {1}".format(i+1,s1[i][:-1]))
		

	elif(a[0]=="add"):
		if(len(a)==1):
			print("Error: Missing todo string. Nothing added!")
		else:	
			with open('todo.txt','a') as f1:
				f1.write(a[1])
				f1.write("\n")
			print("Added todo:",'"'+a[1]+'"')

	elif(a[0]=="del"):
		if(len(a)==1):
			print("Error: Missing NUMBER for deleting todo.")
		else:	
			with open('todo.txt','rt') as f1:
				s1=f1.readlines()
			if (int(a[1])>len(s1) or int(a[1])<=0):
				print("Error: todo #"+a[1],"does not exist. Nothing deleted.")
			else:
				del(s1[len(s1)-int(a[1])])
				with open('todo.txt','wt') as f1:
					f1.writelines(s1)
				print("Deleted todo #"+a[1])

	elif(a[0]=="done"):
		if(len(a)==1):
			print("Error: Missing NUMBER for marking todo as done.")
		else:	
			with open('todo.txt','rt') as f1:
				s1=f1.readlines()
			if (int(a[1])>len(s1) or int(a[1])<=0):
				print("Error: todo #{0} does not exist.".format(a[1]))
			else:	
				with open('done.txt','a') as f2:
					f2.write(s1[len(s1)-int(a[1])])
				del(s1[len(s1)-int(a[1])])
				with open('todo.txt','wt') as f1:
					f1.writelines(s1)
				print("Marked todo #{0} as done.".format(a[1]))

	elif(a[0]=="report"):
		with open('todo.txt','rt') as f1:
			s1=f1.readlines()
		with open('done.txt','rt') as f2:
			s2=f2.readlines()
		now=datetime.datetime.now()
		print(now.strftime("%Y-%m-%d"),end=" ")
		print("Pending :",len(s1),"Completed :",len(s2))
	
