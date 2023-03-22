
##############PRONUNCIATION#######################
def dictionary_matching_pronunciation(top1):#A040
    str_list_pronunce={
        'پر':"O001",'پرى':"D021",'بري':"O001 D021 D054","پرت":'O001 D021 X001 N005','جر':"W011 D021 A002",'نيس':"T035 S029 N035 A002",
        'ممي':'G018 Z004 F027', 'بري':"D021 O001 D055"
    }
    
    key_list_pronunciation=list(str_list_pronunce.keys())
    val_list_pronunciation=list(str_list_pronunce.values())
    
    if top1 not in val_list_pronunciation:
        message="لا يوجد صوت"
    else:
        ind_pronunciation=val_list_pronunciation.index(top1)   
        message=key_list_pronunciation[ind_pronunciation]
        
        
    return message