name=input("Enter file:")
handle=open(name)
counts=dict()
times=list()
ist=list()
for line in handle:
    line=line.rstrip()
    if line.startswith('From'):
        if(line.endswith('2008')):
           words=line.split()
           x=words[-2]
           saat=x.split(':')
           times.append(saat[0])
for time in times:
    if time not in counts:
        counts[time]=1
    else:
        counts[time]=counts[time]+1
for s,count in counts.items():
        result=(s,count)
        ist.append(result)
ist=sorted(ist)
for key,val in ist:
    print(key,val)
