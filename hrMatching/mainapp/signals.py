from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Job_Post, Employee_Cluster, JobPost_Cluster
import requests


@receiver(post_save, sender=Employee)
def Employee_Cluster_handler(sender, instance, created, **kwargs):

    url = "http://127.0.0.1:8000/api/"
    edu = instance.education if instance.education is not None else ""
    exp = instance.experience if instance.experience is not None else ""
    awards = instance.awards if instance.awards is not None else ""
    skills = instance.skills if instance.skills is not None else ""

    data = {"text": edu + " " + exp + " " + awards + " " + skills}
    # Sending the POST request
    response = requests.post(url + "preprocess/", data=data).json()
    clusterable_text = response["preprocessed_text"]

    data = {"text": clusterable_text}
    response2 = requests.post(url + "predict/", data=data).json()
    cluster = response2["cluster"][0]

    if created:
        # print("created")
        Employee_Cluster.objects.create(
            employee=instance, cluster=cluster, clusterable_text=clusterable_text
        )
    else:
        # print("updated")
        employee_cluster = Employee_Cluster.objects.get(employee=instance)
        employee_cluster.cluster = cluster
        employee_cluster.clusterable_text = clusterable_text
        employee_cluster.save()


@receiver(post_save, sender=Job_Post)
def JobPost_Cluster_handler(sender, instance, created, **kwargs):

    url = "http://127.0.0.1:8000/api/"
    job_des = instance.jobDescription
    job_title = instance.job_title
    data = {"text": job_title + " " + job_des}

    # Sending the POST request
    response = requests.post(url + "preprocess/", data=data).json()
    clusterable_text = response["preprocessed_text"]

    data = {"text": clusterable_text}
    response2 = requests.post(url + "predict/", data=data).json()
    cluster = response2["cluster"][0]

    if created:
        # print("created")
        JobPost_Cluster.objects.create(
            jobpost=instance, cluster=cluster, clusterable_text=clusterable_text
        )
    else:
        # print("updated")
        jobpost_cluster = JobPost_Cluster.objects.get(jobpost=instance)
        jobpost_cluster.cluster = cluster
        jobpost_cluster.clusterable_text = clusterable_text
        jobpost_cluster.save()
