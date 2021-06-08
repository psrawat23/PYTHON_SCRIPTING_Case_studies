import threading
import concurrent.futures
import sys

#Counting number of lines and words for each file using separate thread
def count(f_name):
    count_newline=0
    count_word=0
    with open(f_name,"r") as file:
        for char in file:
            count_newline+=1
            char=char.split()
            for word in char:
                if word=='\t' or word==' ' or word=='\n':
                    count_word+=1
                else:
                    count_word+=1
    return f_name,count_newline,count_word
thread=[]
result=[]
#Using ThreadPool full creating thread for each file and storing the thread in thread list
with concurrent.futures.ThreadPoolExecutor() as executer:
    thread=[executer.submit(count,sys.argv[i]) for i in range(1,len(sys.argv))]

#Storing the result of each thread 
for f in concurrent.futures.as_completed(thread):
    result.append(f.result())
    
#printing no. of lines and word along with file name 
for i in sorted(result):
    print(i[0]," "*(20-len(i[0])),i[1]," "*3,i[2])

    
