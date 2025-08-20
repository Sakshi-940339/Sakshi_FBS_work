rows=10
col=10
num=100
for i in range(rows):
    row=[]
    for j in range(col):
        row.append(num)
        num-=1
        if i % 2==0:
            row = row[:: -1]
        print(row)
        
