group=[12,13,14]

def stat(freq):
    REF=0
    HET=0
    HOM=0
    MIS=0
    for each in freq:
        if each == './.':
            MIS+=1
        if each == '0/1':
            HET+=1
        if each == '1/1':
            HOM+=1
        if each == '0/0':
            REF+=1
    Allele1=REF*2+HET
    Allele2=HOM*2+HET
    return Allele1,Allele2,REF,HET,HOM,MIS


with open("PoPTE-filter.txt",'r') as fd:
    for line in fd:
        if line.startswith('1'):
            line=line.replace("\n","").split("\t")
            freq=line[8:]
            a0,b0,c0,d0,e0,f0=stat(freq)
            #print(a0,b0,c0,d0,e0,f0)
            freq=line[12:14]
            at,bt,ct,dt,et,ft=stat(freq)
            #print(at,bt,ct,dt,et,ft)
            if dt>1 and d0<10:
                print(line)##results in printing
            
            
            
