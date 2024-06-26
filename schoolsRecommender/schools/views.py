from .models import School
from django.shortcuts import render, get_object_or_404
from .recommender import recommend_schools
import googlemaps
from django.conf import settings

def recommend_view(request):
    if request.method == 'GET':
        address = request.GET.get('address')
        broad_classification = request.GET.get('broad_classification')
        classification_group = request.GET.get('classification_group')
        school_year = request.GET.get('school_year')
        
        if address:
            gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
            geocode_result = gmaps.geocode(address)
            
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
                recommendations, extended_recommendations = recommend_schools(
                    latitude, longitude,
                    broad_classification=broad_classification,
                    classification_group=classification_group,
                    school_year=school_year
                )
                
                if not recommendations:
                    return render(request, 'schools/recommendations.html', {
                        'recommendations': extended_recommendations,
                        'message': 'No schools within 50km. Here are some schools within 100km.',
                        'extended': True
                    })
                
                return render(request, 'schools/recommendations.html', {'recommendations': recommendations})
            else:
                return render(request, 'schools/recommend_form.html', {'error': 'Geocode was not successful: No results found'})
        else:
            return render(request, 'schools/recommend_form.html', {'error': 'Address is required'})
    return render(request, 'schools/recommend_form.html')

def school_detail_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    context = {
        'school': school,
    }
    return render(request, 'schools/school_detail.html', context)