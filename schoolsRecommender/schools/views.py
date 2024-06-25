from .recommender import recommend_schools
from django.shortcuts import render, get_object_or_404
from .models import School

def recommend_view(request):
    if request.method == 'GET' and 'latitude' in request.GET and 'longitude' in request.GET:
        latitude = float(request.GET['latitude'])
        longitude = float(request.GET['longitude'])
        recommendations = recommend_schools(latitude, longitude)

        context = {
            'recommendations': recommendations,
        }
        print(recommendations)

        return render(request, 'schools/recommendations.html', context)

    return render(request, 'schools/recommend_form.html')

def school_detail_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    context = {
        'school': school,
    }
    return render(request, 'schools/school_detail.html', context)
