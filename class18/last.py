fp=open('data.txt','r+')
print("before closing")
print(fp.closed)
fp.close()
print('after closing')
print(fp.closed)