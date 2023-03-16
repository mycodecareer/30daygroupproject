# 30daygroupproject

This is the repository for the SDR 30 day builder's challenge group project. It is a recipe app with a react frontend and a python flask backend.

## Requirements
- Flask
- Python 3
- pip
- NodeJS
- npm
- yarn

## React Frontend

See [Frontend README](./frontend/README.md)

## Flask Backend

This app uses a Python Flask app as a backend. [This guide](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3) was used to initialize.

### Running Backend

To run the backend flask app first `cd` into the `backend` directory:
```bash
cd backend
```
Create a virtual environment
```bash
python3 -m venv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```
> `venv\Scripts\activate` for windows users

Install packages
```bash
pip install -r requirements.txt
```
Next, export the following variables
```bash
export FLASK_APP=app
export FLASK_ENV=development
```
Then run the flask app:
```bash
flask run
```
The flask app will now be visible at `http://127.0.0.1:5000/`
