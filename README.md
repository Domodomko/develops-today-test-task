# Develops Today Test Task
## Made by Sergei Shinn
A Django app made as a test task for a Backend-developer vacancy.
## [Deployed On Heroku](https://develops-today-test-task.herokuapp.com/)

## Link Structure

- **/** - Home, Swagger
- **/?format=openapi** - Swagger link for Postman collection
- **/redoc** - Redoc API Page
- **/admin** - Admin panel
- **/api** - API part of the App
    - **/posts-list** - API Posts List
    - **/post-detail/(int:pk)/** - API Post Detail
    - **/create-post** - API Create new Post
    - **/update-delete-post/(int:pk)/** - API Update or Delete Post
    - **/create-comment/(int:post_pk)/** - API Create Comment
    - **/update-delete-comment/(int:pk)/** - API Update or Delete Comment
    - **/post-upvote/(int:post_pk)/** - API Upvote the Post


## Installation
##### *For Linux users*
After pushing this repository and creating your DB on Postgre, you'll need to create new python venv for it and install requirements:

```sh
pipenv install
pipenv shell
cp .env.example .env
docker-compose build
docker-compose up -d
```

After that you'll need to migrate the data, create a superuser, fill database (it's gonna take a long time) and run the application:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py fill_db
python manage.py runserver
```
