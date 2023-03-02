# todo-list-django-react

Django/React/PostgreSQL project for Stantec

django username: root
django password: password
dont know if consistant for docker or not but ay

## about

Backend is entirely dockerized, might to to stop docker and run again on first build. database sometimes build fasters than web even though web depends on database

## useful commands

```console
docker-compose up --build
```

```console
docker-compose run web python manage.py [manage.py commands]
```

might want to update template dirs in settings.py for django
might want to switch package.json scripts -> build to "rm -rf ../gamify_todo/build && react-scripts build && cp -r build ../gamify_todo/build"
"react-scripts build"

## useful urls

[base todo list](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
[starting a django project with postgres](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
[postgres commands](https://www.postgresqltutorial.com/postgresql-administration/postgresql-show-tables/)
[session based Auth](https://www.youtube.com/watch?v=89KrqjqPeZ0)
