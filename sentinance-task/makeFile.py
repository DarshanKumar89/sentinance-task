import os 
# list the files in directory /Users/darshankumar/dgod/sentinance-task
lis = os.listdir('/Users/darshankumar/sentinance-task')
print(lis) 
tgt = os.listdir('/Users/darshankumar/sentinance-task')

file_dir ='/Users/darshankumar/sentinance-task/master.txt'
ct = 0

print('target file :', tgt) 
try: 
	# if yes delete the file 
	# otherwise data will be appended to existing file 
	if len(tgt)>0: 
		os.remove('/Users/darshankumar/sentinance-task')  

		open(tgt, 'a').close() 
	else: 
		# create an empty file 
		open(tgt, 'a').close() 
except: 
	head = open('/Users/darshankumar/sentinance-task/master.txt', 'a+') 

	line ='empno, ename, sal'
	# write header to output 
	print(head, line) 
	head.close() 
	# below loop to write data to output file 
	for line1 in lis: 
		f_dir = file_dir+'\\'+line1 
		# open files in read mode 
		in_file = open(f_dir, 'r+') 

		# open output in append mode 
		w = open(out_file, 'a+') 
		d = in_file.readline() 
		d = in_file.readlines() 
		w.write("\n") 
		for line2 in d: 
			print(line2) 
			w.write(line2) 
			
		ct = ct + 1
	w.close()	 
