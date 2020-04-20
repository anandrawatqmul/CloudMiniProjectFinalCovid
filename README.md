#Cloud Mini Project covid
In this project we are using Flask and Flask-SQLAlchemy.
We are managing user account management, like Registration, login, logout, Forgot password, Deactivate user.
Deactivate is basically delition of user record. These are all the functionalies with internal APIs.

Along with these internal APIs we have funtion with external API, we are using covid 19 API to fetch the latest records and show the details for the requested country.

We have created form for all the functionalities, along with user Interface. 

## Requirements.txt
    Flask
    Flask-SQLAlchemy
    requests


## Setup Repo
```
virtualenv
git clone:
cd CloudMiniProjectFinal
pip install -r requirements.txt
python app.py
```


## Example Project
- The user will be register into the website.
- The user will be login into the website.
- The user enters the country name and get details associated with that particular country.
- The user can further logout or deactivate.
- The user deactivate will delete the user records.
- The user can also update their password.

