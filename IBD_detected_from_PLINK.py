group=["BT_1","BT_2","BT_3","BT_4","BT_5","BT_6","BT_7","BT_8","BT_9","sw_AJTC6","sw_AXIAC","sw_BFE","sw_BLQC","sw_BONA","sw_BP447","sw_BT2","sw_BTC","sw_CART","sw_CRAM","sw_Campbell","sw_Chesterle","sw_DELTA","sw_DH2","sw_DHWH","sw_DHWH2","sw_DREAM","sw_DSD","sw_DZ51","sw_FB","sw_FJ72-1","sw_FQC","sw_FROST","sw_FW95-1","sw_GILET","sw_GNZS","sw_HAL","sw_HAL2","sw_HJC","sw_HQ","sw_HQTUN","sw_HRQC","sw_HUAH","sw_HYJHBTC","sw_JCKC721","sw_JCPY731","sw_JCYY736","sw_JHBTC","sw_JJCYC","sw_JX2","sw_LENG","sw_LJG","sw_LateNavel","sw_MIDNIT","sw_MORO","sw_Morita","sw_MoroN2","sw_NAVALN","sw_NSTC","sw_NW","sw_NWQC","sw_OLDBUD","sw_Orinda","sw_PALM","sw_PearC2","sw_Powell","sw_QJ","sw_REDGRD","sw_REN4","sw_REN5","sw_RRJHBTC","sw_SHELD","sw_SHIM","sw_SUC","sw_Suzuki","sw_T1","sw_TCPS1","sw_TOMSON","sw_TYC","sw_TaroROS","sw_TaroUn","sw_TaroWC","sw_UKXC","sw_WHXG","sw_WHXHC","sw_WLQC","sw_WNP","sw_WSXG","sw_XP1","sw_gg2"]
dict={}
with open("plink.genome","r") as fd:
    for line in fd:
        line=line.replace("\n","").split('\t')
        #print(line)
        num=line[-3]
        target1=line[1]+'+'+line[3]
        target2=line[3]+'+'+line[1]
        dict[target1]=num
        dict[target2]=num
        #print(target1)

out=open("out.txt",'w')
for one in group:
    s=''
    for two in group:
        if one==two:
            s+='1'+'\t'
        else:
            site=one+'+'+two
            s+=dict[site]+'\t'
    s=one+'\t'+s[:-1]+'\n'
    out.write(s)
        
