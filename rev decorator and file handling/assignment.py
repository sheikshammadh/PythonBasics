fp1=open('data.txt','r')
data=fp1.read()

fp2=open('wish.txt','w')
fp2.write(data)
print('new file created successfully')

fp1.close()
fp2.close()