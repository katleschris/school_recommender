from geopy.distance import geodesic
from schools.models import School

def recommend_schools(latitude, longitude, max_distance_km=50, top_n=20):
    all_schools = School.objects.all()
    recommendations = []


    for school in all_schools:
        print('school:', school.school_name)
        distance = geodesic((latitude, longitude), (school.latitude, school.longitude)).km
        distance = round(distance, 2)
        if distance <= max_distance_km:
            recommendations.append((school, distance))

    # sort by distance
    recommendations.sort(key=lambda x: x[1])
    

    return recommendations[:top_n]