# todo-list-django-react

Django/React/PostgreSQL project for Stantec

django username: root
django password: password
dont know if consistant for docker or not but its here.

## about

Backend is entirely dockerized, might to to stop docker and run again on first build. database sometimes builds slower than web even though web depends on database

## how to run

1. start by navigating to gamify_todo_frontend
2. run `npm run build`
3. navigate to gamify_todo
4. run `docker-compose up --build`
5. open webbrowser to localhost:8000

## useful commands

```console
docker-compose up --build
```

```console
docker-compose run web python manage.py [manage.py commands]
```

```console
npm run build
```

might want to update template dirs in settings.py for django
might want to switch package.json scripts -> build to "rm -rf ../gamify_todo/build && react-scripts build && cp -r build ../gamify_todo/build"
"react-scripts build"

## useful urls

[base todo list](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
[starting a django project with postgres](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
[postgres commands](https://www.postgresqltutorial.com/postgresql-administration/postgresql-show-tables/)
[session based Auth](https://www.youtube.com/watch?v=89KrqjqPeZ0)

## Lessions learned

dont write your own auth from scratch use a library maybe try [Auth0 for react](https://auth0.com/blog/complete-guide-to-react-user-authentication/) next time. or in the future. Could also use [react auth kit](https://www.npmjs.com/package/react-auth-kit) first time mulligan I guess?

## known issues

- routes aren't protected, you will just get unuseable access to them. /dashboard and /todo
    - [try this](https://stackoverflow.com/questions/62384395/protected-route-with-react-router-v6)
- registration sends plain text passwords.
- mobile interface is broken.
- axios requests could be updated to use .then/.catch methods instead of nesting them in a try/catch
