from django.db import models

from django import forms

from groupings import get_groups
# Create your models here.

class SubmitForm(forms.Form):
    class_size = forms.IntegerField(min_value = 1, max_value = 100, label = 'Class size(1-100):')
    group_size = forms.IntegerField(min_value = 1, max_value = 100, label = 'Group size(1-100):')
    iterations = forms.IntegerField(min_value = 1, label = 'Iterations(higher values may yield more full groupings):')
    
    def groups(self):
        total = self.cleaned_data['class_size']
        group = self.cleaned_data['group_size']
        processed = []
        max_length = 0
        max_max = 0 #maximum number of max_length items
        for x in range(0, self.cleaned_data['iterations']):
            processed_temp = get_groups.pick_groups(get_groups.make_groups(total, group))
            processed_temp.sort(key = len, reverse = True)
            if len(processed_temp[0]) >= max_length:
                if len(processed_temp[0]) > max_length:
                    max_max = 0
                max_list = []
                max_m_temp = len([max_list for entry in processed_temp if len(entry) >= len(processed_temp[0])])
                if max_m_temp > max_max:
                    max_max = max_m_temp
                    print "more" + str(max_max)
                    print processed_temp
                    max_length = len(processed_temp[0])
                    processed = processed_temp
       
        print max_length, max_max 
        return processed
