from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

def get_hr_details_aa_pb(HR_DETAILS_USER):
    group_a = Group.objects.get(name='Ankita')
    users_group_a = group_a.user_set.all()

    HR_DETAILS_AA1 = [
        {"key": user.username, "value": user.username, "reportTo": "AA"}
        for user in users_group_a
    ]
    
    group_b = Group.objects.get(name='Pooja') 
    users_group_b = group_b.user_set.all()

    HR_DETAILS_PB1 = [
        {"key": user.username, "value": user.username, "reportTo": "PB"}
        for user in users_group_b
    ]
    
   # group_c = Group.objects.get(name='Admin') 
   # users_group_c = group_c.user_set.all()
#
   # SUPERUSERS =[
   #     {"key": user.username, "value": user.username, "reportTo": "Admin", "priority": 1}
   #     for user in users_group_c
   #     
   # ]
    
    
    HR_DETAILS1 = [
        {"key": user["key"], "value": user["value"], "reportTo": user["reportTo"], "priority": 0}
        for user in HR_DETAILS_AA1
    ]
    
    HR_DETAILS2 = [
        {"key": user["key"], "value": user["value"], "reportTo": user["reportTo"], "priority": 1}
        for user in HR_DETAILS_PB1
    ]
    
    HR_DETAILS0 = HR_DETAILS1 + HR_DETAILS2
    
    
    # Append HR_DETAILS0 to HR_DETAILS_USER
    HR_DETAILS_USER.extend(HR_DETAILS0)
    #superuser.extend(SUPERUSERS)
    
    return HR_DETAILS_USER

class Command(BaseCommand):
    help = 'Get users from group A and print HR_DETAILS_AA format in CMD'

    def handle(self, *args, **kwargs):
        HR_DETAILS_USER = [{'key': 'karan Nair', 'value': 'DhanyaNair', 'reportTo': 'AA', 'priority': 0}]
        hr_details_user = get_hr_details_aa_pb(HR_DETAILS_USER)
        print(hr_details_user)