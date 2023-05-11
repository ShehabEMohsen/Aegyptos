from fuzzywuzzy import process
from fuzzywuzzy import fuzz

str_list0={
        "Mouth": ['D021'],"House": ['O001'],"Man and his occupation": ['A001'],"King": ['A040'],"Sun": ['N005'],"Motion": ['D054'],
        "Small bird used for bad,weak, or little things": ['G037'],"Ton,Village": ['O049'],
        "Eating,speaking or Metaphorically (emotions,attitude,thinking)": ['A002'],
        "king of Upper Egypt": ['M023'],"King's adviser, Royal intimate": ['M024'],"Vulture": ['G001'],"Beat, srike, smite": ['A025'],
        "Re or Ra": ['C002'],"Seth": ['C007'],"Truth, righteousness,justice, right doing" : ['C010'],"Heh (section of a phyle)": ['C011'],
        "Daughter, daughter in law, granddaughter": ['Q001'],"Lion, lion shaped image (of king), sphinx": ['E022'],"Master, Lord": ['E023'],
        "Selket": ['L007']
}

str_list1={
        "Army": ['A012 Z003'],"Found defective (of text)": ['G028 D003'],"Reporter,Herald": ['F025 G017'],"Chamberlain": ['W017 G017'],
        "raise": ['A009 A024'],"load": ['A009 D036'],"Build, fashion(men)": ['A035 A024'],"Many, numerous,much": ['I002 G001'],
        "A type of wine": ['G051 W051'],"Among, therein": ['G018 D039'],"Place of truth, tomb, necropolis": ['Q001 H006'],
        "Tomb": ['Q001 O001'],"Lion": ['E023 Z001'],"Selket, Scorpion": ['L007 X001'],"To hinder": ['V007 D036']
}

str_list2={
        "walk": ['O001 D021 D054'],"Silent": ['W011 D021 A002'],"Think": ['V031 G001 A002'],"Women": ['O034 X001 B001'],
        "Women, Wife": ['N042 X001 B001'],"Daughter": ['X001 G039 B001'],"Slave": ['O029A X001 B001'],"Fall out (of hair)": ['G043 D003 N037'],
        "Blind": ['N037 Q003 D004'],"Wakeful": ['N037 Q003 D004'],"Write": ['S029 D066 F046A'],"Priest": ['D060 N035A A001'],
        "God's father": ['T007A X001 I009'],"Lector priest": ['V028 W005 D058'],"Soldier of the town regment": ['S034 O049 N035'],
        "Governor, mayor of the town": ['F004 D036 A003'],"King's seal-bearer": ['L002 X001 S019'],"Ptah": ['Q003 X001 V028'],
        "Sebek or Sobek": ['S029 D058 V031'],"Ra or Re": ['D021 D036 N005'],"Seker or Soker": ['O034 V031 D021'],"work": ['A009 X001 D028'],
        "Bricklayer,Potter": ['A035 A024 A001'],"Multitude, many": ['I002 A001 Z002'],"Official": ['A021 D021 S029'],
        "Herdsman": ['A024 G043 D040'],"Innumerable": ['C011 Z001 Z003'],"The two ladies ( Nekhbet and Wadjet)": ['G016 G007 G007'],
        "Giraffe": ['G018 Z004 F027'],"Authority": ['Q001 D002 D021'],"Affection": ['Q001 F034 Z001'],
        "Two lion gods(Tefnut & Shu), Ruty(god)": ['E023 E023 M017'],"Warehosue, storehouse, Labour establishment, ergastulum": ['E023 O001 D036'],
}

str_list3={
        "Soker (The god)": ['O004 V031 D021 A040'],"Day": ['O004 D021 G001 N005'],"Send": ['O004 G001 D058 D054'],
        "winter season": ['O001 D021 X001 N005'],"Bad,evil": ['D058 T035 G037A N035'],"Qis (Place-name)": ['X007 T035 S029 O049'],
        "Call out": ['T035 S029 N035 A002'],"Recount": ['S029 D046 I010 A002'],"Hungry": ['V028 D021 X007 A002'],
        "Drink": ['VS029 D021 G037A A002'],"Eat": ['E034 N035 G017 A002'],"Hair": ['V007 N035 Z004 D003'],
        "Grey-haired": ['S029 O040 G017 D003'],"Complexion": ['T035 N035 E034 D003'],
        "Look": ['V007 N035 Z004 D003'],"Record royal titulary": ['G043 N035 D046 D066'],"king of Upper and Lower Egypt": ['M023 X001 X001 L002'],
        "Keeper of the royal diadem": ['A048 F035 X001 F004'],"Heket": ['V028 X001 X007 A041'],
        "To injure,to harm, denounce": ['G001 D036 D036 D006'],"A tree": ['G001 D036 D036 M001A'],
        "Well to do person, King of the birds": ['I002 Z002 G039 Z003'],"Statue": ['A021 U033 D033 N035'],
        "Utterance, recitation": ['A025 N023 N035 Z001'],"Cash payment": ['Q001 O004 G001 A009'],"Magazine": ['E023 O001 D036 Z002'],
        "A fish": ['E023 K001 D036 T030'],"Breast, chest, upper body": ['V007 D058 X001 F051']
}

str_list4={
        "Tired": ['G037 D021 D046 A007 G037A'],"Faint": ['D058 N037 D046 A007 G037A'],"Goddess": ['T007A X001 D021 X001 B001'],
        "Mourn": ['M017 G001 V031 D058 D003'],"Serpent": ['V028 G001 I009 G043 I014'],"Snake": ['I010 D046 X001 I009 I014'],
        "Follower of the palace": ['T018 G037A O001 T001 O001'],"Sole companion": ['S029 S034 X001 T021 Z001'],
        "Anubis": ['T035 N035 Q003 G043 E016'],"Build": ['A035 Y001 A024 A001 Z002'],"Constructing (a boat)": ['G001 D036 D036 G043 D040'],
        "Throat": ['I002 Z002 X001 F051B I001'],"Garrulous, Chattering": ['I002 Z002 P008 G043 A002'],
        "Millions, a great number": ['C011 Z001 Z007 Z004 Z003'],"Flame": ['E023 M017 M017 Q007 D021'],
        "Gateway": ['E023 M017 M017 O007 D021'],"Court, Royal Household": ['V007 A021 M017 M017 Z002']
}

str_list5={
        "Skin": ['T035 N035 K001 T034 G017 D003'],"Foreigner": ['G001 D036 D036 F018 A002 A001'],"Courtier": ['A021 X001 V001 W024 N035 V007'],
        "Friend": ['A021 S029 G017 T034 N035 AA001'],"Combat": ['A024 N035 Z004 D021 D002 Z001'],"Widow": ['K005 G001 X001 D021 D003 B001'],
        "To tear asunder": ['G051 AA015 G051 AA015 Z009 D040'],"Capable": ['G051 AA015 Y001 D046 X001 Z001'],
        "Double throne": ['Q001 G043 X001 X001 O001 Z003A'],"Court of law, hall, gateway, waiting place": ['E023 M017 M017 X001 D021 O001']
}

str_list6={
        "Infantry": ['Y005 N035 I009 G001 X001 A012 Z003'],"General-in-chief": ['G017 Z015 D021 A011 Z003 D021 G037A'],
        "Jars, Containers": ['G001 D036 D036 G043 D040 X001 W023'],
}

str_list7={
        "Builder of walls": ['A035 D040 M017 K001 N035 D058 O036 A001'],
        "Ship part": ['A024 Z007 M017 K001 K001 N035 Z007 Z003A'],
}

str_list8={
        "Noisy": ['I002 G001 Z002 AA001 D021 E023 G043 P008 A002'],
        "Courtiers": ['I002 A001 Z002 A021 X001 V001 W024 N035 V007'],
}


def dictionary_matching(top1,choose_dictionary_list):
    str_list="str_list"+str(choose_dictionary_list)
    dictionary_list=globals()[str_list]
    
    match_ratios = process.extract(top1, dictionary_list, scorer=fuzz.token_sort_ratio)
    print(match_ratios)

    best_match = process.extractOne(top1, dictionary_list, scorer=fuzz.token_sort_ratio)
    print(best_match)
    
    return best_match[2]