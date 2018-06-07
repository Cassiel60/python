out=file('1.txt','w')
with open('new 1.txt','r') as fp:
	for line in fp:
		lst_alpha=[]
		lst_number=[]
		di={}
		for num in line:
			if num.isalpha() :
				lst_alpha.append(num)
			else:
				lst_number.append(num)
		if ''.join(lst_alpha).isupper():
			lst_alpha='-'.join(lst_alpha)
		else:
			lst_alpha=''.join(lst_alpha)
			lst_number=[''.join(lst_number).split('\n')][0]
		if ''.join(lst_number).__contains__('>\n'):
		 	lst_number=''.join(lst_number)[:-2]
		elif ''.join(lst_number).__contains__('>'):
			lst_number=''.join(lst_number)[:-1]
		else:
		 	lst_number=''.join(lst_number)
		di[lst_number]=lst_alpha
		out.write(lst_number+'\t'+lst_alpha+'\n')		
		print di
out.flush()
out.close()



