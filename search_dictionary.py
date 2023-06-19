from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import re


search_list={
	"mouth": '𓂋', "house": '𓉐', "man ans his occupation": '𓀀',"king": '𓀭',"backward motion":'𓂽',"Hare":'𓃹',
	"soker (the god)":'𓉔 𓎡 𓂋 𓀭', "sun": '𓇳',"day": '𓉔 𓂋 𓄿 𓇳',"owl": '𓅓', "morning": '𓇼',"Folded cloth":'𓋴',"Water ripple":'𓈖',
        "motion": '𓂻', "send": '𓉔 𓄿 𓃀 𓂻',"walk": '𓉐 𓂋 𓂻',"winter season": '𓉐 𓂋 𓏏 𓇳',
        "small bird used for bad,weak, or little things": '𓅪', "bad,evil": '𓃀 𓌱 𓅫 𓈖',
        "ton,village": '𓊖', "qis (place-name)":  '𓏘 𓌱 𓋴 𓊖',
        "eating,speaking or metaphorically (emotions,attitude,thinking)": '𓀁', "call out": '𓌱 𓋴 𓈖 𓀁', "recount": '𓋴 𓂧 𓆓 𓀁', 
        "silent": '𓎼 𓂋 𓀁', "think": '𓎡 𓄿 𓀁', "hungry": 'v 𓂋 𓏘 𓀁', "drink": 'v𓋴 𓂋 𓅫 𓀁', "eat": '𓃹 𓈖 𓅓 𓀁',
        "tired": '𓅪 𓂋 𓂧 𓀉 𓅫', "faint": '𓃀 𓈙 𓂧 𓀉 𓅫',
        "infantry": '𓏠 𓈖 𓆑 𓄿 𓏏 𓀎 𓏪', "army": '𓅓 𓂝 𓈙 𓀎 𓏪', "army": '𓀎 𓏪',
        "women": '𓊃 𓏏 𓁐', "women, wife": '𓈟 𓏏 𓁐', "goddess": '𓌏 𓏏 𓂋 𓏏 𓁐', "daughter": '𓏏 𓅭 𓁐', "slave": '𓉼 𓏏 𓁐', 
        "widow": '𓆟 𓄿 𓏏 𓂋 𓁸 𓁐',
        "hair": '𓍲 𓈖 𓏭 𓁸', "grey-haired": '𓋴 𓊍 𓅓 𓁸', "complexion": '𓌱 𓈖 𓃹 𓁸',
        "skin": '𓌱 𓈖 𓆛 𓌰 𓅓 𓁸', 
        "mourn": '𓇋 𓄿 𓎡 𓃀 𓁸', "widow": '𓆟,𓄿,𓏏,𓂋,𓁸,𓁐', "fall out (of hair)": '𓅱 𓁸 𓈙',
        "found defective (of text)": '𓅠 𓁸',"look": '𓍲 𓈖 𓏭 𓁸', "blind": '𓈙 𓊪 𓁺', "blind": '𓈙 𓊪 𓁹',
        "wakeful": '𓈙 𓊪 𓁺', "wakeful": '𓈙 𓊪 𓁹',
        "record royal titulary": '𓅱 𓈖 𓂧 𓃈', "write": '𓋴 𓃈 𓄳',
        "serpent": '𓎛 𓄿 𓆑 𓅱 𓆙', "snake": '𓆓 𓂧 𓏏 𓆑 𓆙',
        "king of upper egypt": '𓇓 𓏏 𓈖 ', "king of upper egypt": '𓇓 𓏏 ', "king of upper egypt": '𓇓',
        "king of upper and lower egypt": '𓇓 𓏏 𓏏 𓆤',"priest": '𓃂 𓈗 𓀀', "god's father": '𓌏 𓏏 ', "god's father": '𓌏 𓏏 𓆑',
        "lector priest": '𓎛 𓎴 𓃀', "general-in-chief": '𓅓 𓏺 𓂋 𓏺 𓏪 𓂋 𓅫', "soldier of the town regment": '𓋹 𓊖 𓈖',
        "governor, mayor of the town": '𓄂 𓂝 𓀂', "reporter,herald": '𓄙 𓅓',  "king's adviser, royal intimate": '𓇓 𓂋 𓐍 𓏛', "king's adviser, royal intimate": '𓇔',
        "follower of the palace": '𓌞 𓅫 𓉐 𓌇 𓉐',
        "keeper of the royal diadem": '𓀹 𓄤 𓏏 𓄂', "chamberlain": '𓏃 𓅓', "king's seal-bearer": '𓆤 𓏏 𓋨', "sole companion": '𓋴 𓋹 𓏏 𓌡 𓏤',
        "anubis": '𓌱 𓈖 𓊪 𓅱 𓃣', "ptah": '𓊪 𓏏 𓎛', "heket": '𓎛 𓏏 𓏘 𓀯', "sebek or sobek": '𓋴 𓃀 𓎡', "ra or re": '𓂋 𓂝 𓇳',
        "seker or soker": '𓊃 𓎡 𓂋',
        "raise": '𓀋 𓄿 𓆑',"work": '𓀋 𓏏 𓂓',"load": '𓀋 𓊪 𓍿 𓄿',"raise": '𓀋 𓀜',"load": '𓀋 𓂝',
        "build, fashion(men)": '𓀨 𓀜',"bricklayer,potter": '𓀨 𓀜 𓀀', "build": '𓀨 𓂡',"builder of walls": '𓀨 𓂡 𓇋 𓆛 𓈖 𓃀 𓊅 𓀀',"build":
        '𓀨 𓏛 𓀜 𓀀 𓏥',"vulture": '𓄿',"to injure,to harm, denounce": '𓄿 𓂝 𓂝 𓂝',"to injure,to harm, denounce": '𓄿 𓂝 𓂝 𓁻',
        "foreigner": '𓄿 𓂝 𓂝 𓄑 𓀁',"foreigner": '𓄿 𓂝 𓂝 𓄑 𓀁 𓀀',"foreigner, translator, interpreter,soldier": '𓄿 𓂝 𓂝 𓄑 t014 𓀁',
        "constructing (a boat)": '𓄿 𓂝 𓂝 𓅱 𓂡',"jars, containers": '𓄿 𓂝 𓂝 𓅱 𓂡 𓏏 𓏋',"a tree": '𓄿 𓂝 𓂝 𓆮',
        "multitude, many": '𓆉 𓀀 𓏥',"many, numerous,much": '𓆉 𓄿',"excessive crying of children": '𓆉 𓄿 𓅱 𓏏 𓀁 𓏪',
        "noisy": '𓆉 𓄿 𓏥 𓊤 𓏲 𓀁',"noisy": '𓆉 𓄿 𓏥 𓐍 𓂋 𓃭 𓅱 𓊤 𓀁',"multitude (of people), company(of guests)": '𓆉 𓄿 𓏏 𓀀 𓏥',
        "multitude (of people), company(of guests)": '𓆉 𓄿 𓏏 𓀀 𓁐 𓏥',"well to do person, king of the birds": '𓆉 𓏥 𓅭 𓏪',
        "throat": '𓆉 𓏥 𓏏 𓄻 𓆈',"garrulous, chattering": '𓆉 𓏥 𓊤 𓅱 𓀁',"official": '𓀙 𓂋 𓋴',
        "courtier": '𓀙 𓏏 𓍢 𓏌 𓈖 𓍲',"friend": '𓀙 𓋴 𓅓 𓌰 𓈖 𓐍',"statue": '𓀙 𓍘 𓂙 𓈖',
        "courtiers": '𓆉 𓀀 𓏥 𓀙 𓏏 𓍢 𓏌 𓈖 𓍲',"herdsman": '𓀜 𓅱 𓂡',"combat": '𓀜 𓈖 𓏭 𓂋 𓁷 𓏤',
        "ship part": '𓀜 𓏲 𓇋 𓆛 𓆛 𓈖 𓏲 𓏫',"beat, srike, smite": '𓀝',"utterance, recitation": '𓀝 𓈇 𓈖 𓏤',
        "re or ra": '𓁛',"seth": '𓁣',"truth, righteousness,justice, right doing ": '𓁦',"heh (section of a phyle)": '𓁨',
        "millions, a great number": '𓁨 𓁨 𓁨',"innumerable": '𓁨 𓏤 𓏪', "millions, a great number": '𓁨 𓏤 𓏲 𓏭 𓏪',
        "a type of wine": '𓅻 w051',"to tear asunder": '𓅻 𓐝 𓅻 𓐝 𓏴 𓂡',"capable": '𓅻 𓐝 𓏛 𓂧 𓏏 𓏤',
        "the two ladies ( nekhbet and wadjet)": '𓅒',"the two ladies ( nekhbet and wadjet)": '𓅒 𓁐 𓁐',
        "the two ladies ( nekhbet and wadjet)": '𓅒 𓅆 𓅆',"among, therein": '𓅔 𓂠',"giraffe": '𓅔 𓏭 𓄛',
        "daughter, daughter in law, granddaughter": '𓊨',"authority": '𓊨 𓁷 𓂋', "affection": '𓊨 𓄣 𓏤',
        "double throne": '𓊨 𓅱 𓏏 𓏏 𓉐 𓏫',"place of truth, tomb, necropolis": '𓊨 𓆄',"tomb": '𓊨 𓉐',
        "cash payment": '𓊨 𓉔 𓄿 𓀋',"lion, lion shaped image (of king), sphinx": '𓃬', "master, lord": '𓃭',"lion": '𓃭 𓏤',
        "two lion gods(tefnut & shu), ruty(god)": '𓃭 𓃭 𓇋',"magazine": '𓃭 𓉐 𓂝 𓏥',"warehosue, storehouse, labour establishment, ergastulum": '𓃭 𓉐 𓂝',
        "a fish": '𓃭 𓆛 𓂝',"a fish": '𓃭 𓆛 𓂝 𓌪',"flame": '𓃭 𓇋 𓇋 𓊮 𓂋',"gateway": '𓃭 𓇋 𓇋 𓉞 𓂋',
        "court of law, hall, gateway, waiting place": '𓃭 𓇋 𓇋 𓏏 𓂋 𓉐',"selket": '𓆫',"selket, scorpion": '𓆫 𓏏',
        "to hinder": '𓍲 𓂝',"court, royal household": '𓍲 𓀙 𓇋 𓇋 𓏥',"breast, chest, upper body": '𓍲 𓃀 𓏏 𓄹'
}
# def search(top1):
#     # temp=[]
#     # temp.append(top1)
#     # if isinstance(top1,list):
#     #     temp=top1
#     #     top1 = top1[0]
#     new_dict=lower_dict(search_list)
#     # match_ratios = process.extract(top1, new_dict, scorer=fuzz.token_sort_ratio)
#     # print(match_ratios)

#     # best_match = process.extractOne(top1, new_dict, scorer=fuzz.token_sort_ratio)
#     # print(best_match)
#     # print("best match2"+ best_match[2])

#     key_list=list(new_dict.keys())
#     val_list=list(new_dict.values())
    
#     if top1.lower() in key_list:

#         ind=key_list.index(top1.lower())
#         ans = val_list[ind]
#     else:
#         ans = "-"
#         print ("temp ="+str(top1))
        
        
    
#     result = any(any(top1 in s for s in subList) for subList in new_dict.keys())
#     # print("result", result)
#     # print("answer", ans)
#     # max_key = max(d, key=lambda k: d[k])

#     return ans
############################################################################################
# def search(word):
#     new_dict = lower_dict(search_list)
#     result = {}
    
#     for key, value in new_dict.items():
#         if word.lower() in key:
#             result[key] = value
    
#     return result
############################################################################################

def search(word):
    new_dict = lower_dict(search_list)
    result = {}
    pattern = r"\b{}\b".format(re.escape(word.lower()))
    resultList=[]
    for key, value in new_dict.items():
        if re.search(pattern, key):
            result[key] = value
            resultList.append({key:value})
    return resultList
############################################################################################
def lower_dict(d):
   new_dict = dict((k.lower(), v) for k, v in d.items())
   return new_dict
# print(search("King"))
