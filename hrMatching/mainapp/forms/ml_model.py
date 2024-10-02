from django import forms
from datetime import date
from ..models import Job_Post
from django.core.exceptions import ValidationError
from django.db.models import Min


class test_n_clusters_form(forms.Form):

    start_number = forms.IntegerField(
        label="Min n.of.clusters",
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        min_value=2,
    )

    end_number = forms.IntegerField(
        label="Max n.of.clusters",
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        min_value=2,
    )

    step = forms.IntegerField(
        label="Step between tests",
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        min_value=1,
    )

    word2vec_vector_size = forms.IntegerField(
        label="word2vec vector size",
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        min_value=100,
    )

    word2vec_window_size = forms.IntegerField(
        label="word2vec window size",
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        min_value=5,
    )

    word2vec_word_min_count_percentage = forms.FloatField(
        label="word2vec word_min_count_percentage",
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        min_value=0.01,
        max_value=0.99,
    )

    start_date = forms.DateField(
        label="Use Data Starting From:",
        help_text="Default to use all data",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super(test_n_clusters_form, self).__init__(*args, **kwargs)
        self.fields["start_date"].initial = self.get_min_addedDate()
        self.fields["word2vec_window_size"].initial = 12
        self.fields["word2vec_vector_size"].initial = 2500
        self.fields["word2vec_word_min_count_percentage"].initial = 0.35

    def get_min_addedDate(self):
        min_date = Job_Post.objects.aggregate(Min("addedDate"))["addedDate__min"]
        if min_date:
            return min_date
        else:
            return date.today()

    def clean_end_number(self):
        data1 = self.cleaned_data["end_number"]
        data2 = self.cleaned_data["start_number"]
        if data1 < data2:
            raise ValidationError(
                "Max number of clusters must be smaller or equal to Min number"
            )
        return data1
