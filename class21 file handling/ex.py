import csv
fp=open('json.csv','r',newline="")
csv_writer=csv.writer(fp)
csv_writerwriter.writerow(['eid','ename','gender'])
fp.close()
