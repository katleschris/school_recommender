<h1 align="center">School Recommendation System for Students in Australia</h1>

<div align="center" >
  <img src="https://img.shields.io/badge/made%20by-Katlego%20Leshiba-blue?style=for-the-badge&labelColor=20232a" />
  <img src="https://img.shields.io/badge/Python-20232a?style=for-the-badge&logo=python&labelColor=2e2f38" />
  <img src="https://img.shields.io/badge/Django-20232a?style=for-the-badge&logo=django&labelColor=162e16" />
  <img src="https://img.shields.io/badge/CSS-20232a?style=for-the-badge&logo=css&labelColor=2e2f35" />
  <img src="https://img.shields.io/badge/Pandas-20232a?style=for-the-badge&logo=pandas&labelColor=2e2f38" />
  <img src="https://img.shields.io/badge/GeoPy-20232a?style=for-the-badge&logo=geopy&labelColor=2e2f38" />
</div>

## Project Overview

This project involves designing and implementing a school recommendation system for students in Australia. The system helps students find schools that best fit their criteria, including geolocation, classification, and year range.

## Table of Contents

- [School Recommendation Prototype](#school-recommendation-prototype)
  - [Objective](#objective)
  - [Dependencies and Imports](#dependencies-and-imports)
  - [Criteria for Recommendation](#criteria-for-recommendation)
  - [Approach and Methods](#approach-and-methods)
  - [Validation](#validation)
  - [Output](#output)
  - [Future Scope](#future-scope)

## School Recommendation Prototype

### Objective

Analyze provided datasets of secondary schools and develop a proof-of-concept prototype to recommend schools to students based on various criteria.

### Dependencies and Imports

- **Python**: The main programming language used for development.
- **Django**: The web framework used to build the application.
- **Pandas**: A data manipulation and analysis library used for handling datasets.
- **GeoPy**: A library used for geocoding and calculating distances.

### Criteria for Recommendation

- Geolocation of the school and student
- Distance
- Classification group
- General classification
- Year range

### Approach and Methods

1. **Set-up Django App**: Initialized a new Django project and app to handle the recommendation system.
2. **Analyzed Datasets**: Used pandas to read the CSV file into a dataframe and analyzed the data to determine relevant criteria for school recommendations.
3. **Extracted Relevant Fields**: Identified and extracted necessary fields from the dataframe.
4. **Created CSV Copy**: Made a copy of the dataframe and saved it as a CSV file for further processing.
5. **Database Setup**: Created a Django model with the relevant fields, then migrated and initialized the database.
6. **Database Population**: Wrote a Python script using Django's BaseCommand to populate the database from the CSV file.
7. **Recommender View and Template**: Developed a view and template to receive input from students for the recommendation system.
8. **Recommendation Display View**: Created a view to display the recommended schools based on student input.
9. **School Details View**: Developed a view to display detailed information about the chosen school.
10. **Address Validation**: Used google maps API to autocomplete and convert addresses to latitude and longitude
11. **Distance Calculation**: Applied geopy to calculate the distance between the student's location and the schools using latitude and longitude.
12. **Filtering based on additional parameters**: Used if statements to check if the school meets additional parameters

### Validation

- **Effectiveness Testing**: Use a subset of the data to test the recommendations and compare them against known outcomes.
- **Feedback Loop**: Incorporate feedback to continuously improve the recommendation accuracy.

### Output

A proof-of-concept prototype that suggests schools to students based on their address general attributes.

## Project Setup and Installation

Before running the application, make sure you have Python and Django installed on your machine.

1. Clone the repository:
   ```bash
   git clone <repository-url>

## Future Scope

### Machine Learning Integration

- **Personalized Recommendations**: Implement machine learning algorithms to provide more personalized school recommendations based on historical data and user preferences.
- **Predictive Analytics**: Use predictive models to anticipate student needs and preferences, improving the accuracy of recommendations.

### Data Expansion

- **Broader Data Collection**: Extend the data collection process to include more comprehensive details such as extracurricular activities, facilities, and reviews.
- **Real-Time Updates**: Implement a system for real-time data updates to ensure the recommendation engine uses the most current information.

### Enhanced User Interface

- **Interactive Maps**: Integrate interactive maps to visualize school locations and distances dynamically.
- **User Profiles**: Allow users to create profiles to save their preferences and receive tailored recommendations.

### Performance Optimization

- **Scalability**: Optimize the system for handling large datasets and multiple concurrent users.
- **Efficiency**: Improve the efficiency of the recommendation algorithms to reduce processing time.

<p align="center">Made with :heart: in Django</p>
