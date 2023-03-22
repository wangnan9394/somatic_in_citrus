
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

out=open('BT.SNPs.results.txt','w')
with open("87.Minor.SNPs.vcf",'r') as fd:
    for line1 in fd:
        if line1.startswith('c'):
            line=line1.replace("\n","").split("\t")
            g_list=[]
            for one in line[9:]:
                one=one.split(':')[0]
                g_list.append(one)
            #print(g_list)
            freq=g_list
            a0,b0,c0,d0,e0,f0=stat(freq)
            #print(a0,b0,c0,d0,e0,f0)
            #print(g_list[4:7])
            freq=g_list[4:7]
            #print(line)
            at,bt,ct,dt,et,ft=stat(freq)
            print(at,bt,ct,dt,et,ft)
            if dt>2 and d0<10:
                out.write(line1)
            
            
            
