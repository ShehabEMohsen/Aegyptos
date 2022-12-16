from fuzzywuzzy import process
from fuzzywuzzy import fuzz
str_list = {
    "Mouth": 'D021', "House": 'O001', "Man and his occupation": 'A001',
    "God,King": 'A040', "Soker (The god)": 'O004 V031 D021 A040',
    "Sun": 'N005', "Day": 'O004 D021 G001 N005',
    "Motion": 'D054', "Send": 'O004 G001 D058 D054',
    "Small bird used for bad,weak, or little things": 'G037', "Bad,evil": 'D058 T035 G037A N035',
    "Ton,Village": 'O049', "Qis (Place-name)": 'X007 T035 S029 O049',
    "Eating,speaking or Metaphorically (emotions,attitude,thinking)": 'A002', "Call out": 'T035 S029 N035 A002', "Recount": 'S029 D046 I010 A002', 
    "Silent": 'W011 D021 A002', "Think": 'V031 G001 A002', "Hungry": 'V028 D021 X007 A002', "Drink": 'VS029 D021 G037A A002', "Eat": 'E034 N035 G017 A002',
    "Tired": 'G037 D021 D046 A007 G037A', "Faint": 'D058 N037 D046 A007 G037A',
    "Infantry": 'Y005 N035 I009 G001 X001 A012 Z003', "Army": 'G017 D036 N037 A012 Z003', "Army": 'A012 Z003',
    "Women": 'O034 X001 B001', "Women, Wife": 'N042 X001 B001', "Goddess": 'T007A X001 D021 X001 B001', "Daughter": 'X001 G039 B001', "Slave": 'O029A X001 B001', 
    "Widow": 'K005 G001 X001 D021 D003 B001',
    "Hair": 'V007 N035 Z004 D003', "Grey-haired": 'S029 O040 G017 D003', "Complexion":
    'T035 N035 E034 D003', "Skin": 'T035 N035 K001 T034 G017 D003', 
    "Mourn": 'M017 G001 V031 D058 D003', "Widow": 'K005,G001,X001,D021,D003,B001', "Fall out (of hair)": 'G043 D003 N037',
    "Found defective (of text)": 'G028 D003',"Look": 'V007 N035 Z004 D003', "Blind": 'N037 Q003 D005', "Blind": 'N037 Q003 D004',
    "Wakeful": 'N037 Q003 D005', "Wakeful": 'N037 Q003 D004',
    "Record royal titulary": 'G043 N035 D046 D066', "Write": 'S029 D066 F046A',
    "Serpent": 'V028 G001 I009 G043 I014', "Snake": 'I010 D046 X001 I009 I014',
    "king of Upper Egypt": 'M023 X001 N035 ', "king of Upper Egypt": 'M023 X001 ', "king of Upper Egypt": 'M023',
    "king of Upper and Lower Egypt": 'M023 X001 X001 L002',"Priest": 'D060 N035A A001', "God’s father": 'T007A X001 ', "God’s father": 'T007A X001 I009',
    "Lector priest": 'V028 W005 D058', "General-in-chief": 'G017 Z015 D021 A011 Z003 D021 G037A', "Soldier of the town regment": 'S034 O049 N035',
    "Governor, mayor of the town": 'F004 D036 A003', "Reporter,Herald": 'F025 G017',  "King’s adviser, Royal intimate": 'M023 D021 AA001 Y001', "King’s adviser, Royal intimate": 'M024',
    "Follower of the palace": 'T018 G037A O001 T001 O001',
    "Keeper of the royal diadem": 'A048 F035 X001 F004', "Chamberlain": 'W017 G017', "King’s seal-bearer": 'L002 X001 S019', "Sole companion": 'S029 S034 X001 T021 Z001',
    "Anubis": 'T035 N035 Q003 G043 E016', "Ptah": 'Q003 X001 V028', "Heket": 'V028 X001 X007 A041', "Sebek or Sobek": 'S029 D058 V031', "Ra or Re": 'D021 D036 N005',
    "Seker or Soker": 'O034 V031 D021',
    "raise": 'A009 G001 I009',"work":'A009 X001 D028',"load":'A009 Q003 V013 G001',"raise":'A009 A024',"load":'A009 D036',
    "Build, fashion(men)":'A035 A024',"Bricklayer,Potter":'A035 A024 A001', "Build":'A035 D040',"Builder of walls":'A035 D040 M017 K001 N035 D058 O036 A001',"Build":
    'A035 Y001 A024 A001 Z002',
    "Vulture":'G001',"To injure,to harm, denounce":'G001 D036 D036 D036',"To injure,to harm, denounce":'G001 D036 D036 D006',"Foreigner":'G001 D036 D036 F018 A002',
    "Foreigner":'G001 D036 D036 F018 A002 A001',"Foreigner, translator, interpreter,soldier":'G001 D036 D036 F018 T014 A002',"Constructing (a boat)":'G001 D036 D036 G043 D040',
    "Jars, Containers":'G001 D036 D036 G043 D040 X001 W023',"A tree":'G001 D036 D036 M001A',"Multitude, many":'I002 A001 Z002',"Many, numerous,much":'I002 G001',
    "Excessive crying of children":'I002 G001 G043 X001 A002 Z003',"Noisy":'I002 G001 Z002 P008 Z007 A002',"Noisy":'I002 G001 Z002 AA001 D021 E023 G043 P008 A002',
    "Multitude (of people), Company(of guests)":'I002 G001 X001 A001 Z002',"Multitude (of people), Company(of guests)":'I002 G001 X001 A001 B001 Z002',
    "Well to do person, King of the birds":'I002 Z002 G039 Z003',"Throat":'I002 Z002 X001 F051B I001',"Garrulous, Chattering":'I002 Z002 P008 G043 A002',
    "Official":'A021 D021 S029',"Courtier":'A021 X001 V001 W024 N035 V007',"Friend":'A021 S029 G017 T034 N035 AA001',"Statue":'A021 U033 D033 N035',
    "Courtiers":'I002 A001 Z002 A021 X001 V001 W024 N035 V007',
    }

match_ratios = process.extract('A021 S029 G017 T034 N035 AA001', str_list, scorer=fuzz.token_sort_ratio)
print(match_ratios)

best_match = process.extractOne('I002 A001 Z002 A021 X001 V001 W024 N035 V007', str_list, scorer=fuzz.token_sort_ratio)
print(best_match)
