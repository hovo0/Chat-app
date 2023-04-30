# Secure Chat Application
This secure chat application was built using a combination of Django, Channels, Channels-Redis, Redis, JavaScript, HTML, CSS, regex, and Daphne. The WebSocket and JSEncrypt protocols were utilized for message encoding and decoding. Redis server was run using Docker, and SQLite3 was used as the database, though you can set up your own preferred database. For user authentication, Django's built-in authentication module was used. A custom chat module was also written specifically for this Django application.

## Getting Started
To get started with this project, follow these steps:

Clone the repository to your local machine:
```bash
git clone https://github.com/username/repo.git
```
Navigate into the project directory:
```bash
cd mysite
```
Create and activate a virtual environment:
```bash
python -m venv myvenv
source myvenv/bin/activate
```
Install the required packages:
```
pip install -r req.txt
```
Make migrations and migrate the database:
```
python manage.py makemigrations
python manage.py migrate
```
We will use a channel layer that uses Redis as its backing store. To start a Redis server on port 6379, run the following command:

```
docker run -p 6379:6379 -d redis:5
```
Create a superuser:
```
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver
```
You should now be able to access the application at http://localhost:8000/ in your web browser. You can log in with your superuser account and start using the chat application.
