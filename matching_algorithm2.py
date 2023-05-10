
str_list = {
        "Mouth": ['D021'], "House": [ 'O001'], "Man and his occupation": [ 'A001'],
        "King": [ 'A040'], "Soker (The god)": ['O004 V031 D021 A040'],
        "Sun": [ 'N005'], "Day": [ 'O004 D021 G001 N005'],
        "Motion": [ 'D054'], "Send": [ 'O004 G001 D058 D054'],"walk": [ 'O001 D021 D054'],"winter season": [ 'O001 D021 X001 N005'],
        "Small bird used for bad,weak, or little things": [ 'G037'], "Bad,evil": [ 'D058 T035 G037A N035'],
        "Ton,Village": [ 'O049'], "Qis (Place-name)": [ 'X007 T035 S029 O049'],
        "Eating,speaking or Metaphorically (emotions,attitude,thinking)": [ 'A002'], "Call out": [ 'T035 S029 N035 A002'], "Recount": [ 'S029 D046 I010 A002'], 
        "Silent": [ 'W011 D021 A002'], "Think": [ 'V031 G001 A002'], "Hungry": [ 'V028 D021 X007 A002'], "Drink": [ 'VS029 D021 G037A A002'], "Eat": [ 'E034 N035 G017 A002'],
        "Tired": [ 'G037 D021 D046 A007 G037A'], "Faint": [ 'D058 N037 D046 A007 G037A'],
        "Infantry": [ 'Y005 N035 I009 G001 X001 A012 Z003'], "Army": [ 'G017 D036 N037 A012 Z003'], "Army": [ 'A012 Z003'],
        "Women": [ 'O034 X001 B001'], "Women, Wife": [ 'N042 X001 B001'], "Goddess": [ 'T007A X001 D021 X001 B001'], "Daughter": [ 'X001 G039 B001'], "Slave": [ 'O029A X001 B001'], 
        "Widow": [ 'K005 G001 X001 D021 D003 B001'],
        "Hair": [ 'V007 N035 Z004 D003'], "Grey-haired": [ 'S029 O040 G017 D003'], "Complexion": [ 'T035 N035 E034 D003'],
        "Skin": [ 'T035 N035 K001 T034 G017 D003'], 
        "Mourn": [ 'M017 G001 V031 D058 D003'], "Widow": [ 'K005,G001,X001,D021,D003,B001'], "Fall out (of hair)": [ 'G043 D003 N037'],
        "Found defective (of text)": [ 'G028 D003'],"Look": [ 'V007 N035 Z004 D003'], "Blind": [ 'N037 Q003 D005'], "Blind": [ 'N037 Q003 D004'],
        "Wakeful": [ 'N037 Q003 D005'], "Wakeful": [ 'N037 Q003 D004'],
        "Record royal titulary": [ 'G043 N035 D046 D066'], "Write": [ 'S029 D066 F046A'],
        "Serpent": [ 'V028 G001 I009 G043 I014'], "Snake": [ 'I010 D046 X001 I009 I014'],
        "king of Upper Egypt": [ 'M023 X001 N035 '], "king of Upper Egypt": [ 'M023 X001 '], "king of Upper Egypt": [ 'M023'],
        "king of Upper and Lower Egypt": [ 'M023 X001 X001 L002'],"Priest": [ 'D060 N035A A001'], "God's father": [ 'T007A X001 '], "God's father": [ 'T007A X001 I009'],
        "Lector priest": [ 'V028 W005 D058'], "General-in-chief": [ 'G017 Z015 D021 A011 Z003 D021 G037A'], "Soldier of the town regment": [ 'S034 O049 N035'],
        "Governor, mayor of the town": [ 'F004 D036 A003'], "Reporter,Herald": [ 'F025 G017'],  "King's adviser, Royal intimate": [ 'M023 D021 AA001 Y001'], "King's adviser, Royal intimate": [ 'M024'],
        "Follower of the palace": [ 'T018 G037A O001 T001 O001'],
        "Keeper of the royal diadem": [ 'A048 F035 X001 F004'], "Chamberlain": [ 'W017 G017'], "King's seal-bearer": [ 'L002 X001 S019'], "Sole companion": [ 'S029 S034 X001 T021 Z001'],
        "Anubis": [ 'T035 N035 Q003 G043 E016'], "Ptah": [ 'Q003 X001 V028'], "Heket": [ 'V028 X001 X007 A041'], "Sebek or Sobek": [ 'S029 D058 V031'], "Ra or Re": [ 'D021 D036 N005'],
        "Seker or Soker": [ 'O034 V031 D021'],
        "raise": [ 'A009 G001 I009'],"work": [ 'A009 X001 D028'],"load": [ 'A009 Q003 V013 G001'],"raise": [ 'A009 A024'],"load": [ 'A009 D036'],
        "Build, fashion(men)": [ 'A035 A024'],"Bricklayer,Potter": [ 'A035 A024 A001'], "Build": [ 'A035 D040'],"Builder of walls": [ 'A035 D040 M017 K001 N035 D058 O036 A001'],"Build":
        ['A035 Y001 A024 A001 Z002'],"Vulture": [ 'G001'],"To injure,to harm, denounce": [ 'G001 D036 D036 D036'],"To injure,to harm, denounce": [ 'G001 D036 D036 D006'],
        "Foreigner": [ 'G001 D036 D036 F018 A002'],"Foreigner": [ 'G001 D036 D036 F018 A002 A001'],"Foreigner, translator, interpreter,soldier": [ 'G001 D036 D036 F018 T014 A002'],
        "Constructing (a boat)": [ 'G001 D036 D036 G043 D040'],"Jars, Containers": [ 'G001 D036 D036 G043 D040 X001 W023'],"A tree": [ 'G001 D036 D036 M001A'],
        "Multitude, many": [ 'I002 A001 Z002'],"Many, numerous,much": [ 'I002 G001'],"Excessive crying of children": [ 'I002 G001 G043 X001 A002 Z003'],
        "Noisy": [ 'I002 G001 Z002 P008 Z007 A002'],"Noisy": [ 'I002 G001 Z002 AA001 D021 E023 G043 P008 A002'],"Multitude (of people), Company(of guests)": [ 'I002 G001 X001 A001 Z002'],
        "Multitude (of people), Company(of guests)": [ 'I002 G001 X001 A001 B001 Z002'],"Well to do person, King of the birds": [ 'I002 Z002 G039 Z003'],
        "Throat": [ 'I002 Z002 X001 F051B I001'],"Garrulous, Chattering": [ 'I002 Z002 P008 G043 A002'],"Official": [ 'A021 D021 S029'],
        "Courtier": [ 'A021 X001 V001 W024 N035 V007'],"Friend": [ 'A021 S029 G017 T034 N035 AA001'],"Statue": [ 'A021 U033 D033 N035'],
        "Courtiers": [ 'I002 A001 Z002 A021 X001 V001 W024 N035 V007'],"Herdsman": [ 'A024 G043 D040'],"Combat": [ 'A024 N035 Z004 D021 D002 Z001'],
        "Ship part": [ 'A024 Z007 M017 K001 K001 N035 Z007 Z003A'],"Beat, srike, smite": [ 'A025'],"Utterance, recitation": [ 'A025 N023 N035 Z001'],
        "Re or Ra": [ 'C002'],"Seth": [ 'C007'],"Truth, righteousness,justice, right doing ": [ 'C010'],"Heh (section of a phyle)": [ 'C011'],
        "Millions, a great number": [ 'C011 C011 C011'],"Innumerable": [ 'C011 Z001 Z003'], "Millions, a great number": [ 'C011 Z001 Z007 Z004 Z003'],
        "A type of wine": [ 'G051 W051'],"To tear asunder": [ 'G051 AA015 G051 AA015 Z009 D040'],"Capable": [ 'G051 AA015 Y001 D046 X001 Z001'],
        "The two ladies ( Nekhbet and Wadjet)": [ 'G016'],"The two ladies ( Nekhbet and Wadjet)": [ 'G016 B001 B001'],
        "The two ladies ( Nekhbet and Wadjet)": [ 'G016 G007 G007'],"Among, therein": [ 'G018 D039'],"Giraffe": [ 'G018 Z004 F027'],
        "Daughter, daughter in law, granddaughter": [ 'Q001'],"Authority": [ 'Q001 D002 D021'], "Affection": [ 'Q001 F034 Z001'],
        "Double throne": [ 'Q001 G043 X001 X001 O001 Z003A'],"Place of truth, tomb, necropolis": [ 'Q001 H006'],"Tomb": [ 'Q001 O001'],
        "Cash payment": [ 'Q001 O004 G001 A009'],"Lion, lion shaped image (of king), sphinx": [ 'E022'], "Master, Lord": [ 'E023'],"Lion": [ 'E023 Z001'],
        "Two lion gods(Tefnut & Shu), Ruty(god)": [ 'E023 E023 M017'],"Magazine": [ 'E023 O001 D036 Z002'],"Warehosue, storehouse, Labour establishment, ergastulum": [ 'E023 O001 D036'],
        "A fish": [ 'E023 K001 D036'],"A fish": [ 'E023 K001 D036 T030'],"Flame": [ 'E023 M017 M017 Q007 D021'],"Gateway": [ 'E023 M017 M017 O007 D021'],
        "Court of law, hall, gateway, waiting place": [ 'E023 M017 M017 X001 D021 O001'],"Selket": [ 'L007'],"Selket, Scorpion": [ 'L007 X001'],
        "To hinder": [ 'V007 D036'],"Court, Royal Household": [ 'V007 A021 M017 M017 Z002'],"Breast, chest, upper body": [ 'V007 D058 X001 F051']
        }

result_dict = {}
for key, value in str_list.items():
    num_spaces = value[0].count(' ')
    if num_spaces not in result_dict:
        result_dict[num_spaces] = {}
    result_dict[num_spaces][key] = value

# create separate dictionary for each group of values with the same number of spaces
grouped_dicts = []
for num_spaces, data_dict in result_dict.items():
    new_dict = {}
    for key, value in data_dict.items():
        new_dict[key] = value
    grouped_dicts.append(new_dict)

# print the result
for i, data_dict in enumerate(grouped_dicts):
    print(f"Group {i+1}:")
    for key, value in data_dict.items():
        print(f"\t{key}: {value}")