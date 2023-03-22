sample_list=["BT_1","BT_2","BT_3","BT_4","BT_5","BT_6","BT_7","BT_8","BT_9","sw_AJTC6","sw_AXIAC","sw_BFE","sw_BLQC","sw_BONA","sw_BP447","sw_BT2","sw_BTC","sw_Campbell","sw_CART","sw_Chesterle","sw_CRAM","sw_DELTA","sw_DH2","sw_DHWH2","sw_DHWH","sw_DREAM","sw_DSD","sw_DZ51","sw_FB","sw_FJ72-1","sw_FQC","sw_FROST","sw_FW95-1","sw_gg2","sw_GILET","sw_GNZS","sw_HAL2","sw_HAL","sw_HQ","sw_HQTUN","sw_HRQC","sw_HUAH","sw_HYJHBTC","sw_JCKC721","sw_JCPY731","sw_JCYY736","sw_JHBTC","sw_JX2","sw_LateNavel","sw_LENG","sw_LJG","sw_MIDNIT","sw_Morita","sw_MORO","sw_MoroN2","sw_NAVALN","sw_NSTC","sw_NW","sw_NWQC","sw_OLDBUD","sw_Orinda","sw_PALM","sw_PearC2","sw_Powell","sw_QJ","sw_REDGRD","sw_REN4","sw_REN5","sw_RRJHBTC","sw_SHELD","sw_SHIM","sw_SUC","sw_Suzuki","sw_T1","sw_TaroROS","sw_TaroUn","sw_TaroWC","sw_TCPS1","sw_TOMSON","sw_TYC","sw_UKXC","sw_WHXG","sw_WHXHC","sw_WLQC","sw_WNP","sw_WSXG","sw_XP1"]
out=open("PoPTE-filter.txt",'w')
header="Num"+'\t'+"CHR"+'\t'+"POS"+'\t'+"INFO"+'\t'+"TYPE"+'\t'+"FAM"+'\t'+"READs"+'\t'+"."+'\t'
for f in sample_list:
    header+=f+'\t'
header=header[:-1]+'\n'
out.write(header)
count=0
with open("Somatic.ppileup.signatures.freqsig.teinsertions",'r') as fd:
    for line in fd:
        line=line.replace("\n","").split('\t')
        freq=[]
        gt=''
        ss=''
        for f in line[:8]:
            ss+=f+'\t'
        for i in line[8:]:
            if i =='NaN':
                gt='./.'
            if float(i) < 0.02:
                gt='0/0'
            if float(i) >0.01999 and float(i) < 0.95:
                gt='0/1'
            if float(i) >0.9499:
                gt='1/1'
            freq.append(gt)
            ss+=gt+'\t'
        ss=ss[:-1]+'\n'

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
        if not Allele1==0 and not Allele2==0 and abs(Allele1-Allele2)>10:
            if MIS<87*0.15:
                #print(Allele1,Allele2,REF,HET,HOM,MIS)
                if HOM >5 and REF >5:
                    pass
                else:
                    out.write(ss)
