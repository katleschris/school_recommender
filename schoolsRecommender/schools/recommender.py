from geopy.distance import geodesic
from schools.models import School

def recommend_schools(latitude, longitude, max_distance_km=50, extended_distance_km=100, top_n=20):
    all_schools = School.objects.all()
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
