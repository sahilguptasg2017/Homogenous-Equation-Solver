#The first row determines the number of rows and colums in the matrix respectively
f1=open(r"F1\Sahil\maths assignment\matrix.txt","r+")
x=f1.readlines()




list_1=[]
for y in x:
    if "\n" in y:
       y=y.replace("\n","")
    if 'Â\xa0' in y:
        y=y.replace("Â\xa0"," ")   
    list_1.append(y)
    


list_2=[]
i=1
while i<len(list_1):
    s=list_1[i].split(" ")
    list_2.append(s)
    i+=1
#print(list_2)




def swap_rows(n,i,list_2):
    flag=True 
    while flag==True:
        if float(list_2[n][i])==0:
            j=n+1
            while j<len(list_2):
                count1=0
                if float(list_2[j][i])!=0:
                    temp=list_2[n]
                    list_2[n]=list_2[j]
                    list_2[j]=temp
                    count1+=1
                    break
                j+=1
        if count1==0:
            flag=False
            i+=1
            try:
                row_scaling1(n,i,list_2)
            except:
                IndexError            
        else:
            flag=False



def row_scaling1(n,i,list_2):
    if float(list_2[n][i])!=0:
        j=n+1
        while j<len(list_2):
            s=float(list_2[j][i])/float(list_2[n][i])
            h=i
            while h<len(list_2[n]):
                list_2[j][h]=str(float(list_2[j][h])-s*float(list_2[n][h]))
                h+=1
            j+=1



def row_scaling(n,i,list_2):
    if float(list_2[n][i])!=0:
        j=n+1
        while j<len(list_2):
            s=float(list_2[j][i])/float(list_2[n][i])
            h=i
            while h<len(list_2[n]):
                list_2[j][h]=str(float(list_2[j][h])-s*float(list_2[n][h]))
                h+=1
            j+=1
    else:
        swap_rows(n,i,list_2)
        row_scaling1(n,i,list_2)


n=0
i=0

while n<len(list_2)-1 and i<len(list_2[n]):
    row_scaling(n,i,list_2)
    n+=1
    i+=1
#print(list_2)




def rref(list_2):
    for x in list_2:
        count=0
        for y in x:
            if count>0:
                break
            elif float(y)!=0:
                count+=1
                for r in list_2:
                    if r!=x:
                        s=float(r[x.index(y)])/float(y)
                        p=0
                        while p<len(r):
                            r[p]=str(round((float(r[p])-float(x[p])*s),2))   
                            p+=1
                     


rref(list_2)  
  


def scaling_rref(list_2):
    v=0
    while v<len( list_2):
        count=0
        for t in list_2[v]:
            if count>0:
                break
            elif float(t)!=0:
                i=0
                while i<len(list_2[v]):
                    list_2[v][i]=str(round((float(list_2[v][i])/float(t)),3))
                    i+=1
                count+=1   
        v+=1        
scaling_rref(list_2)
i=0
while i<len(list_2):
    j=0
    while j<len(list_2[i]):
        if float(list_2[i][j])==(-0.0):
            list_2[i][j]="0"
        j+=1
    i+=1      
print("The RREF of the matrix is:")    
print(list_2)



v=len(list_2)
for x in list_2:
    b=len(x)
j=0
list_3=[]    
while j<b:
    i=0
    list_4=[]
    while i<v:
        list_4.append(list_2[i][j])
        i+=1
    list_3.append(list_4)    
    j+=1 
#print(list_3) 




def parametric(list_2):
    d={}
    d1={}
    for i in list_2:
        for g in i:
            if float(g)==1:
                d[i.index(g)+1]=1
                break
    for i in list_2:        
        for g in range(1,len(i)+1):
            if g not in d  :
                d1[g]=1      
    #print(d)
    
   # print(d1) 
    list_7=[]
    for c in d1:
        list_8=[]
        for x in list_3[c-1]:
    
    
            if float(x)!=0 and len(list_8)<len(list_2[0]):
                list_8.append(str(-(float(x))))



            elif float(x) ==0 and len(list_8)<len(list_2[0]):
                list_8.append(str(float(x)))
        #list_8.insert(c-1,'1')
        for f in d1:

            if f!=c and len(list_8)<len(list_2[0]):
                list_8.insert(f-1,'0')  
        list_8.insert(c-1,'1')        
        count_3=0
        """for u in d1:
            count_3+=1
        count_2=0
        for r in d:
            count_2+=1
        if len(list_2)==1 or len(list_2)==2:
            flag=True
        else:
            if (count_2+count_3)%2!=0:                      
                if count_3>(count_2+count_3)//2 and len(list_2[0])>len(list_2):
                    list_8=list_8[:len(list_8)-1]
                elif count_3>=(count_2+count_3)//2 and len(list_2[0])<=len(list_2):
                    list_8=list_8[:len(list_8)-1]
            else:
                if count_3>=(count_2+count_3)//2 and len(list_2[0])>len(list_2):
                    list_8=list_8[:len(list_8)-1]
                elif count_3>=(count_2+count_3)//2 and len(list_2[0])<=len(list_2):
                    list_8=list_8[:len(list_8)-1]"""
        if len(list_8)>len(list_2[0]):
            list_8.pop()

            
        list_7.append(list_8)



    #print(list_7)

    list_9=[]
    for c in d1:
        list_9.append(c)
    i=0
    list_10=[]
    while i<len(list_9):
        list_10.append("x"+str(list_9[i])+"*"+str(list_7[i]))
        i+=1
    s=""        
    for c in list_10:
        if list_10.index(c)!=len(list_10)-1:
            s+=str(c)+"+"
        else:
            s+=str(c)
    list_11=[]         
    for g in range(0,len(list_2[0])):
        list_11.append('0')
    print("The parametric form is:")        
    print(s)            
    print("The solution is:")
    if s=='':
        print(str(list_11))
    else:
        print(str(list_11)+"+"+s)    

parametric(list_2)


#print(list_2)           