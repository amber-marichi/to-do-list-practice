from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django_flatpickr.widgets import DateTimePickerInput
from todolist.models import Tag, Task


class DatePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateTimeField(
        required=False,
        widget=DateTimePickerInput(),
    )

    class Meta:
        model = Task
        exclude = ["is_done", "datetime"]

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < timezone.now():
            raise ValidationError("The date cannot be in past")
        return deadline
