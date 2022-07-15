from django import forms

from api.models.schedule import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['worker', 'work_day', 'time_start', 'time_end', 'work_location']

    def clean_day_validator(self):
        day = self.cleaned_data.get('work_day')
        print(day)
        for item in Schedule.objects.all():
            if item.work_day == day:
                raise forms.ValidationError("This day already EXIST")
        return day