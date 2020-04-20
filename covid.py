__author__ = "Anand Rawat"
"""To view the records form covid19 api"""
import requests

def getCountryData(country):
    """View the records associated the entered country"""
    link = f'https://api.covid19api.com/country/{country}'
    data = requests.get(link).json()
    if (len(data) > 1) :
        return (data[-1])
    return (data)
