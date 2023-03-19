
seq={}
with open("pro.fa") as f:
    for line in f:
        if line.startswith('>'):
            name=line.replace('>','').split()[0]
            seq[name]=''
        else:
            seq[name]+=line.replace('\n','').strip()

count=0
out=open("new.output.txt",'w')
with open("jieguo.txt",'r') as fd:
    for line1 in fd:
        line=line1.replace("\n",'').split('\t')
        #print(line1)
        chr=line[0]
        pos=int(line[1])
        with open("out.GeneModels.gff3",'r') as f2:
            for each1 in f2:
                each=each1.replace("\n",'').split('\t')
                if each[0]==chr and abs(pos- int(each[3]))<5000 and each[2]=='gene':
                    name=each[8].split(';')[0].split('=')[1]+'.t01'
                    print('>',name)
                    print(seq[name])
                    ll1='>'+name+'\n'
                    ll2=seq[name]+'\n'
                    out.write(ll1)
                    out.write(ll2)

#jieguo.txt
#chr5	36951639	2	18	18	0
#chr7	26668292	2	18	18	0
#chr8	6431337	2	14	14	0
#chr1	5196676	2	20	19	1
#chr3	2318301	2	20	19	1
#chr5	50401578	2	20	19	1
#chr8	6984899	2	16	15	1
#chr8	33841162	2	20	19	1
