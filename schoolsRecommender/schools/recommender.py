from geopy.distance import geodesic
from schools.models import School

def recommend_schools(latitude, longitude, broad_classification=None, classification_group=None, school_year=None, max_distance_km=50, extended_distance_km=100, top_n=20):
    all_schools = School.objects.all()
    
    # Filter based on additional parameters
    if broad_classification:
        all_schools = all_schools.filter(broad_classification=broad_classification)
    if classification_group:
        all_schools = all_schools.filter(classification_group=classification_group)
    if school_year:
        all_schools = all_schools.filter(low_year__lte=school_year, high_year__gte=school_year)
    
    recommendations = []
    extended_recommendations = []

    for school in all_schools:
        distance = geodesic((latitude, longitude), (school.latitude, school.longitude)).km
        distance = round(distance, 2)
        if distance <= max_distance_km:
            recommendations.append((school, distance))
        elif distance <= extended_distance_km:
            extended_recommendations.append((school, distance))

    recommendations.sort(key=lambda x: x[1])
    extended_recommendations.sort(key=lambda x: x[1])

    return recommendations[:top_n], extended_recommendations[:top_n]
