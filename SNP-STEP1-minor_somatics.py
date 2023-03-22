out=open("87.all.NOMAF.frq.count.filter",'w')
with open("87.all.NOMAF.frq.count",'r') as fd:
    for line in fd:
        if 'chr' in line:
            line=line.replace("\n","").split()
            #print(line)
            if not '0' in line[4] and not '0' in line[5]:
                if abs(int(line[4])-int(line[5]))>50:
                    ll=line[0]+'\t'+line[1]+'\n'
                    out.write(ll)
