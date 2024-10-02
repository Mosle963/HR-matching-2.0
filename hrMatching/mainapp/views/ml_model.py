from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ..models import JobPost_Cluster
from ..forms.ml_model import test_n_clusters_form
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
import requests
from datetime import date
import json

def staffaccess(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(staffaccess, login_url="login")
def test_n_clusters_view(request):

    if request.method == "POST":
        form = test_n_clusters_form(request.POST)
        if form.is_valid():
            word2vec_vector_size = form.cleaned_data["word2vec_vector_size"]
            word2vec_window_size = form.cleaned_data["word2vec_window_size"]
            word2vec_word_min_count_percentage = form.cleaned_data[
                "word2vec_word_min_count_percentage"
            ]
            start_date = form.cleaned_data["start_date"]
            start_date = start_date.strftime("%Y-%m-%d")

            start_number = form.cleaned_data["start_number"]
            end_number = form.cleaned_data["end_number"]
            step = form.cleaned_data["step"]
            url = "http://127.0.0.1:8000/api/"
            filtered_records = JobPost_Cluster.objects.filter(
                jobpost__addedDate__range=[start_date, date.today()]
                )
            filtered_records = list(filtered_records.values_list('clusterable_text',flat=True))

            data = {
                "textList": filtered_records,
                "word2vec_vector_size": word2vec_vector_size,
                "word2vec_window_size": word2vec_window_size,
                "word2vec_word_min_count_percentage": word2vec_word_min_count_percentage,
                "start_number": start_number,
                "end_number": end_number,
                "step": step,
            }
            requests.post(url + "retrain/", data=data)

    form = test_n_clusters_form()
    return render(request, "mainapp/ml_model/test_n.html",
                  {"form": form,
                   })


@user_passes_test(staffaccess, login_url="index")
def Cluster_records_list_View(request):
    url = "http://127.0.0.1:8000/api/"
    response = requests.get(url+"list/")
    if response.status_code == 200:
        data = response.json()
    else:
        data = []
    return render(request, 'mainapp/ml_model/cluster_records_list.html', {'Cluster_records_list': data})



from django.http import JsonResponse

def delete_cluster_record_view(request):
    """view to delete a cluster record and delete attached ML trained model"""
    if request.method == 'POST':
        record_id = request.POST.get('id')
        url = "http://127.0.0.1:8000/api/"
        data = {
            'text':record_id
        }
        requests.post(url + "delete/", data=data)
        return JsonResponse({'success': True})


def apply_cluster_record_view(request):
    """
    view to change the ML model in use

    - fetch the inctance of the model curently have applied = True
    - change it to False
    - change applied attrbiute in the model inctance chodes to True
    - change the model via api to make sure it's possiple
    - special use case to apply pre trained model provided by external data is handled when -1 is passed as id

    """
    record_id = request.POST.get('id')
    url = "http://127.0.0.1:8000/api/"
    data = {
        'text':record_id
    }
    requests.post(url + "apply/", data=data)
    return JsonResponse({'success': True})


