
from django.shortcuts import render
from .recommender import recommend_schools

def recommend_view(request):
    if request.method == 'GET':
        address = request.GET.get('address')
        if address:
            # Geocode the address using Nominatim API
            url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
            response = request.get(url)
            data = response.json()
            
            if data:
                latitude = float(data[0]['lat'])
                longitude = float(data[0]['lon'])
                recommendations = recommend_schools(latitude, longitude)
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
