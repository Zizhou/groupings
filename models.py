from django.db import models

from django import forms

from groupings import get_groups
# Create your models here.

class SubmitForm(forms.Form):
    class_size = forms.IntegerField(min_value = 1, max_value = 100, label = 'Class size(1-100):')
    group_size = forms.IntegerField(min_value = 1, max_value = 100, label = 'Group size(1-100):')
    
    def groups(self):
        total = self.cleaned_data['class_size']
        group = self.cleaned_data['group_size']
        processed = get_groups.pick_groups(get_groups.make_groups(total, group))
        processed.sort(key = len, reverse = True)
        return processed
