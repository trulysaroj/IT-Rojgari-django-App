from django.shortcuts import render, get_object_or_404
from .models import JobPosting


# Create your views here.
def index(request):
    jobs = JobPosting.objects.all()
    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {
        "job_posts": active_jobs
    }

    return render(request, 'IT_Rojgari/index.html', context)


# job details views
def job_details(request, id):
    # job_detail = JobPosting.objects.get(id=id)
    job_detail = get_object_or_404(JobPosting, id=id, is_active=True)
    context = {
        "job": job_detail
    }

    return render(request, 'IT_Rojgari/details.html', context)
