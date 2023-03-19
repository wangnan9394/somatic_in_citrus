seq={}
with open("HAP1.CHR.fa.mod.EDTA.TElib.fa") as f:
    for line in f:
        if line.startswith('>'):
            name='TE_'+line.replace('>','').split()[0].split("#")[0].split('_')[1]
            seq[name]=''
        else:
            seq[name]+=line.replace('\n','').strip()
list=[]
out=open('te.modified.fa','w')
with open("te-hierarchy.txt") as fd:
    for line in fd:
        line=line.replace("\n","").split('\t')
        name1='TE_'+line[0].split('_')[1]
        out1='>'+line[0]+'\n'
        out2=seq[name1]+'\n'
        out.write(out1)
        out.write(out2)
        out.flush()


