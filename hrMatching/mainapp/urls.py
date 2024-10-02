from django.urls import path, include
from .views import home, company, employee, job_post, ml_model

urlpatterns = [
    path("", home.index, name="index"),
]

urlpatterns += [
    path(
        "employee/<int:pk>/update/<int:changed>",
        employee.EmployeeUpdateView.as_view(),
        name="employee_update",
    ),
    path(
        "employee/<int:pk>/details",
        employee.EmployeeDetailView.as_view(),
        name="employee_detail",
    ),
]

urlpatterns += [
    path(
        "company/<int:pk>/update/<int:changed>",
        company.CompanyUpdateView.as_view(),
        name="company_update",
    ),
    path(
        "company/<int:pk>/details",
        company.CompanyDetailView.as_view(),
        name="company_detail",
    ),
]

urlpatterns += [
    path(
        "job_post/create",
        job_post.Job_PostCreateView.as_view(),
        name="job_post_create",
    ),
    path(
        "job_post/<int:pk>/update/<int:changed>",
        job_post.Job_PostUpdateView.as_view(),
        name="job_post_update",
    ),
    path(
        "job_post/<int:pk>/details",
        job_post.Job_PostDetailView.as_view(),
        name="job_post_detail",
    ),
    path("job_post/list", job_post.Job_PostListView.as_view(), name="job_post_list"),
    path(
        "job_post/list/mine",
        job_post.Job_Post_Company_ListView.as_view(),
        name="job_post_company_list",
    ),
    path(
        "job_post/<int:pk>/delete",
        job_post.Job_PostDeleteView.as_view(),
        name="job_post_delete",
    ),
]


urlpatterns += [
    path("test-n"       , ml_model.test_n_clusters_view             , name="test_n_clusters"),
    path("tests"        , ml_model.Cluster_records_list_View, name="cluster_tests"),
    path("apply_record" , ml_model.apply_cluster_record_view        , name="apply_record"),
    path("delete_record", ml_model.delete_cluster_record_view       , name="delete_record"),
]
