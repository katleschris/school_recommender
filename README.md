<h1 align="center">School Recommendation System for Students in Australia </h1>

<div align="center" >
  <img src="https://img.shields.io/badge/made%20by-Katlego%20Leshiba-blue?style=for-the-badge&labelColor=20232a" />
  <img src="https://img.shields.io/badge/Python-20232a?style=for-the-badge&logo=python&labelColor=2e2f38" />
  <img src="https://img.shields.io/badge/Django-20232a?style=for-the-badge&logo=django&labelColor=162e16" />
  <img src="https://img.shields.io/badge/CSS-20232a?style=for-the-badge&logo=css&labelColor=2e2f35" />
  <img src="https://img.shields.io/badge/Pandas-20232a?style=for-the-badge&logo=pandas&labelColor=2e2f38" />
  <img src="https://img.shields.io/badge/GeoPy-20232a?style=for-the-badge&logo=geopy&labelColor=2e2f38" />
  
</div>

## Project Overview

This project involves designing and implementing a school recommendation system for students in Australia. The system will help students find schools that best fit their criteria, including geolocation, academic scores, and other relevant factors. The project is divided into two main tasks: developing a web scraper to collect data on secondary schools in Victoria and analyzing provided datasets to create a recommendation prototype for secondary schools in Western Australia.

## Table of Contents

- [Task 1: Web Scraper Development](#task-1-web-scraper-development)
  - [Objective](#objective)
  - [Data Collection](#data-collection)
  - [Steps taken](#steps-taken)
  - [Tools and Libraries](#tools-and-libraries)
  - [Challenges](#challenges)
  - [Output](#output)
- [Task 2: School Recommendation Prototype](#task-2-school-recommendation-prototype)
  - [Objective](#objective-1)
  - [Dependencies and Imports](#dependencies-and-imports)
  - [Criteria for Recommendation](#criteria-for-recommendation)
  - [Approach and Methods](#approach-and-methods)
  - [Validation](#validation)
  - [Output](#output-1)
  - [Future Scope](#future-scope)

## Task 1: Web Scraper Development

### Objective

Develop a web scraper to navigate Goodschools.com and collect data on secondary schools in Victoria. The collected data should be formatted and presented in a CSV file.

### Data Collection

The information collected should include at least the following fields:
- School Name
- Postcode
- Geolocation (Latitude and Longitude)
- Sector (Public/Private)
- Academic Results

## Steps Taken

### Fetching Web Pages
The `fetch_page` function uses the `requests` library to fetch the content of web pages. It handles exceptions to ensure the script can continue running even if a request fails.

### Parsing Search Results
The `parse_search_results` function uses `BeautifulSoup` to parse the HTML content of the search results page. It extracts URLs of individual school pages by finding the a tags in each div that contains a school.

### Fetching and Parsing School Information
The `fetch_school_info` function fetches and parses information from individual school pages. It extracts the school's name, location, address, sector, and academic results.

### Main Function
The `main` function coordinates the entire scraping process. It iterates over multiple pages of search results, fetches and parses each school's information, and stores the data in a list. Finally, it converts this list into a pandas DataFrame and saves it as a CSV file

### Tools and Libraries

- **Python**: The main programming language used for web scraping.
- **BeautifulSoup**: A Python library for parsing HTML and XML documents.
- **Requests**: A simple HTTP library for Python to make network requests.
- **Pandas**: A data manipulation and analysis library used to create the CSV file.

### Challenges
- **Incomplete or Inconsistent Data**: Not all school pages had complete information, requiring robust error handling and data validation.
- **Data Duplication**: At first there were a lot of instances where there was data duplication.
- **Parsing the right tag**: The academic results div had multiple p and span tags with the same class names and the only thing different was the text inside it and that was the only thing I could parse in order to get the correct data.
- **Choosing when to fetch the school data**: Considering that the name, suburb, and sector of the school was in the search results div already, it seemed more efficient to fetch information in the school information page after following the a tag to avoid errors.
- **Steep learning curve**: This was the first time I scraped a website, there were minor challenges but I was able to learn quickly and I am glad I did this assignment.

### Output

The output of Task 1 is a CSV file containing information for at least 50 secondary schools in Victoria.

## Task 2: School Recommendation Prototype

### Objective

Analyze provided CSV datasets of secondary schools in Western Australia and develop a proof-of-concept prototype to recommend schools to students based on various criteria.

### Criteria for Recommendation

- Geolocation of the school and student
- Distance
- Classification group
- General classification
- Year range
- Student's academic score
- Other potential factors (e.g., extracurricular activities, facilities)

### Steps Taken

1. **Set-up Django App**: Initialized a new Django project and app to handle the recommendation system.
2. **Analyzed Datasets**: Used pandas to read the CSV file into a dataframe and analyzed the data to determine relevant criteria for school recommendations.
3. **Extracted Relevant Fields**: Identified and extracted necessary fields from the dataframe.
4. **Created CSV Copy**: Made a copy of the dataframe and saved it as a CSV file for further processing.
5. **Database Setup**: Created a Django model with the relevant fields, then migrated and initialized the database.
6. **Database Population**: Wrote a Python script using Django's BaseCommand to populate the database from the CSV file.
7. **Recommender View and Template**: Developed a view and template to receive input from students for the recommendation system.
8. **Recommendation Display View**: Created a view to display the recommended schools based on student input.
9. **School Details View**: Developed a view to display detailed information about the chosen school.
10. **Distance Calculation**: Applied geopy to calculate the distance between the student's location and the schools using latitude and longitude.

### Validation

- **Effectiveness Testing**: Use a subset of the data to test the recommendations and compare them against known outcomes.
- **Feedback Loop**: Incorporate feedback to continuously improve the recommendation accuracy.

### Output

A proof-of-concept prototype that suggests schools to students based on general attributes.

## Project Setup and Installation

Before running the application, make sure you have Node.js installed on your machine.

Use the following command to install dependencies (in the root of the project):

bash
source venv/Scripts/activate

bash
pip3 install -Ur requirements.txt

## Running the Application locally

Once the dependencies are installed, you can start the development server using the following command:

Change the active directory to schoolRecommender

bash
cd schoolrecommender
run the following command to start a local server 
bash
python3 manage.py runserver
## Future Scope

### Machine Learning Integration

- **Personalized Recommendations**: Implement machine learning algorithms to provide more personalized school recommendations based on historical data and user preferences.
- **Predictive Analytics**: Use predictive models to anticipate student needs and preferences, improving the accuracy of recommendations.

### Data Expansion

- **Broader Data Collection**: Extend the web scraper to collect data from additional sources and include more comprehensive details such as extracurricular activities, facilities, and reviews.
- **Real-Time Updates**: Implement a system for real-time data updates to ensure the recommendation engine uses the most current information.

### Enhanced User Interface

- **Interactive Maps**: Integrate interactive maps to visualize school locations and distances dynamically.
- **User Profiles**: Allow users to create profiles to save their preferences and receive tailored recommendations.

### Performance Optimization

- **Scalability**: Optimize the system for handling large datasets and multiple concurrent users.
- **Efficiency**: Improve the efficiency of the web scraping and recommendation algorithms to reduce processing time.

---
<p align="center">Made with :heart: in Django</p>
