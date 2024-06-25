import pandas as pd

class SchoolData():
    def __init__(self):
        self.file_path = 'wa_secondary_schools.csv'
        self.df = pd.read_csv(self.file_path)

    def get_schools_from_csv(self):

        df2 = self.df[['School Name', 'Street', 'Suburb', 'State', 'Postcode',
            'Postal Street', 'Postal Suburb', 'Postal State', 'Postal Postcode',
            'Latitude', 'Longitude', 'Phone', 'Education Region',
            'Broad Classification', 'Classification Group', 'Low Year', 'High Year', 'Total Students', 'BE Score',
            'ICSEA', 'ATAR Rank', 'Median ATAR','% students with ATAR']].copy()

        df2.dropna(inplace=True)
        # write to csv
        df2.to_csv('schools1.csv', index=False)
        
        return df2
