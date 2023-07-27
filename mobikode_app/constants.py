# constants.py
# Reporting to AnkitaAdhau
from .management.commands.mobikode_hr_updated_records import get_hr_details_aa_pb
HR_DETAILS_USER = []
HR_DETAILS_USER = get_hr_details_aa_pb(HR_DETAILS_USER)
HR_DETAILS_AA= [
        {"key": "Nazim Khan", "value": "NazimKhan", "reportTo":"AA"},
        {"key": "Dhanya Nair", "value": "DhanyaNair","reportTo":"AA"},
        {"key": "Amey Chavan", "value": "AmeyChavan","reportTo":"AA"},
        {"key": "Vedika Wankhede", "value": "VedikaWankhede","reportTo":"AA"},
        {"key": "rahul", "value": "rahul","reportTo":"AA"},
]
#HR_DETAILS_AA.extend(HR_DETAILS_AA1)
#print(HR_DETAILS_AA)
# Reporting to PoojaBerde
HR_DETAILS_PB= [
        {"key": "Rahul Kulkarni", "value": "RahulKulkarni", "reportTo":"PB"},
        {"key": "Reema Girme", "value": "ReemaGirme","reportTo":"PB"},
        {"key": "Neha Sawant", "value": "NehaSawant","reportTo":"PB"},
        {"key": "Mayuri Pise", "value": "MayuriPise","reportTo":"PB"},
]
#HR_DETAILS_AA.extend(HR_DETAILS_PB1)

# ALL HR data
# Priority : 0  indicates Normal USER, 
# Priority : 1  indicates SUPER USER, 
# Priority : 2  indicates Master USER/Admin, 
HR_DETAILS= [
        {"key": "Nazim Khan", "value": "NazimKhan", "reportTo":"AA", "priority": 0},
        {"key": "Amey Chavan", "value": "AmeyChavan","reportTo":"AA",  "priority": 0},
        {"key": "Dhanya Nair", "value": "DhanyaNair","reportTo":"AA", "priority": 0},
        #{"key": "rahul", "value": "rahul","reportTo":"AA","priority": 0},
      

        {"key": "Vedika Wankhede", "value": "VedikaWankhede","reportTo":"AA","priority": 0},
        {"key": "Rahul Kulkarni", "value": "RahulKulkarni", "reportTo":"PB", "priority": 0},
        {"key": "Reema Girme", "value": "ReemaGirme","reportTo":"PB",  "priority": 0},
        {"key": "Mayuri Pise", "value": "MayuriPise","reportTo":"PB","priority": 0},
        {"key": "Neha Sawant", "value": "NehaSawant","reportTo":"PB","priority": 0},
        {"key": "Ankita Adhau", "value": "AnkitaAdhau", "reportTo":"Admin", "priority": 1},
        {"key": "Pooja Berde", "value": "PoojaBerde","reportTo":"Admin", "priority": 1},
        {"key": "Atharva Pasalkar", "value": "AtharvaPasalkar","reportTo":"Admin", "priority": 1},
]


HR_DETAILS.extend(HR_DETAILS_USER)
print(HR_DETAILS)
SUPERUSER_DETAILS= [
        {"key": "Atharva Pasalkar", "value": "AtharvaPasalkar","reportTo":"AA", "priority": 1},
        {"key": "Ankita Adhau", "value": "AnkitaAdhau", "reportTo":"Admin", "priority": 1},
        

]
#SUPERUSER_DETAILS.extend(SUPERUSERS)
#print(SUPERUSER_DETAILS)
SUPER_USER_AA = 'AnkitaAdhau'
SUPER_USER_AP = 'AtharvaPasalkar'
ALERT_RECORD_UPDATE= 'Record updated successfully'
ALERT_RECORD_DELETE= 'Record deleted successfully'

HOME_PAGE_PRIORITY = '0'
MYTEAM_PAGE_PRIORITY = '1'