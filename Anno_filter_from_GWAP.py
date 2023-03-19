
import argparse

parser = argparse.ArgumentParser(description = 'gff changed', add_help = False, usage = '\n [used for each chromosome] \n python3 -s [HA or HB tag] -i [input.gff3] -t [1-only one transrcipts; 2-two or more transcripts]-o [output.gff3]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-s', '--hap', metavar = '[HA or HB tag]', help = 'HA or HB tag', required = True)
required.add_argument('-i', '--input', metavar = '[input.gff3]', help = 'input', required = True)
required.add_argument('-t', '--type', metavar = '[type 1 or2 ]', help = 'input', required = True)
required.add_argument('-o', '--output', metavar = '[output.gff3]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()
count=0
seq={}

#报错：Error: no valid ID found for GFF record
HAP_name=args.hap
out=open(args.output,'w')

count=0
list=[]
list_lines=[]
with open(args.input,'r') as fd:
    for line1 in fd:
        list_lines.append(line1)
        count+=1
        line=line1.replace("\n","").split('\t')
        #print(line)
        chr=line[0][-1]
        if line[2]=='gene':
            list.append(count)
list.append(count)
#print(list)

HA1g=args.hap+chr+'g'
for nums,each in enumerate(list):#list存储了基因的行数，和最后一行
    #print(each)
    if nums+1 ==len(list):
        break
    gene_line=list_lines[each-1]#list_lines是所有每一行
    #print(gene_line)
    region1=list_lines[int(list[nums]-1):int(list[nums+1])-1]
    #print(region1)
    name=HA1g+str(nums+1)
    seq[name]=region1
       
if args.type=='2':
    new_seq={}
    count_re=0
    for key,value in seq.items():
        new_value=''
        for re in value:
            #if 'gene' in re or '.t01' in re:###修改这里保留一个转录组本！！
            new_value+=re
        new_value=new_value[:-1]
        #print(key)
        #print(value)
        gene_o=value[0].split('\t')
        #print(gene_o)
        if abs(int(gene_o[3])-int(gene_o[4])) >450:
            count_re+=1
            name_re=HA1g+str(count_re)
            new_seq[name_re]=new_value
        #count_re
if args.type=='1':
    new_seq={}
    count_re=0
    for key,value in seq.items():
        new_value=''
        for re in value:
            if 'gene' in re or '.t01' in re:###修改这里保留一个转录组本！！
                new_value+=re
        new_value=new_value[:-1]
        #print(key)
        #print(value)
        gene_o=value[0].split('\t')
        #print(gene_o)
        if abs(int(gene_o[3])-int(gene_o[4])) >450:
            count_re+=1
            name_re=HA1g+str(count_re)
            new_seq[name_re]=new_value
seq=new_seq

#print(seq['HA1g2'])
for key,value in seq.items():
    count=int(key.split('g')[-1])
    if count<10:
        name=HAP_name+chr+'g'+'000'+str(count)+'0'
    if count>9 and count<100:
        name=HAP_name+chr+'g'+'00'+str(count)+'0'
    if count>99 and count<1000:
        name=HAP_name+chr+'g'+'0'+str(count)+'0'
    if count>999 and count<10000:
        name=HAP_name+chr+'g'+''+str(count)+'0'
    #print(name)
    #out.write(value)
    gene_t=value.split('\n')[0]
    gene_id='ID='+name+';'
    gene_new=gene_t.split('ID')[0]+gene_id+'\n'
    #print(gene_new)
    out.write(gene_new)

    list_mRNA_CDS=value.split('\n')
    all_len=len(list_mRNA_CDS)
    mRNA_list=[]
    for num,i in enumerate(list_mRNA_CDS):
        if 'mRNA' in i:
            #out.write(i+'\n')
            mRNA_list.append(num)
    mRNA_list.append(all_len)
    #print(mRNA_list)
    #print(len(mRNA_list))
    #out.write(str(len(mRNA_list)-1))
    for trans in range(len(mRNA_list)-1):
        transcript='.'+str(trans+1)
        #print(transcript)
        #print(mRNA_list[trans],mRNA_list[trans+1])
        #print(value)
        mRNA_t=value.split('\n')[int(mRNA_list[trans])]
        #print(mRNA_t)
        mRNA_id='ID='+name+transcript+';Parent='+name+';'
        mRNA_new=mRNA_t.split('ID')[0]+mRNA_id+'\n'
        #print(mRNA_t)
        out.write(mRNA_new)
        others_target_list=value.split('\n')[int(mRNA_list[trans])+1:int(mRNA_list[trans+1])]
        #print(others_target_list)
        for one in others_target_list:
            if not 'lnc_RNA' in one:
                one=one.split('ID')[0]
                pw='ID='+name+transcript+';'+'Parent='+name+transcript+';'
                new_one=one+pw+'\n'
                #print(new_one)
                out.write(new_one)
    out.flush()
        
