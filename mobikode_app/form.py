from django.forms import ModelForm
from mobikode_app.models import Employ
class EmployForm(ModelForm):
    class Meta:
        model = Employ

        fields = ['Name','Skill','Experience','Relevant_Experience','Company','Availability','Offer','CTC',
                'ECTC','Location','Contact','Mail_id','Reason_for_job_change','Resume','PassPort','status'
        
        ]
