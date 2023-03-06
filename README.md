# todo-list-django-react

Django/React/PostgreSQL project

django username: root
django password: password
dont know if consistant for docker or not but its here.

## about

Backend is entirely dockerized, might to to stop docker and run again on first build. database sometimes builds slower than web even though web depends on database

10 points are awarded uppon completion of a todo, all todos are worth the same. points are removed on uncompletion.
leaderboard shows users who have completed the most tasks.

## how to run

1. start by navigating to gamify_todo_frontend
2. run `npm run build`
3. navigate to gamify_todo
4. run `docker-compose up --build`
5. open webbrowser to [localhost:8000](http://localhost:8000/)

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

## useful sites/tutorials

- [base todo list](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
- [starting a django project with postgres](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
- [CRUD in Django Rest Framework and React](https://saasitive.com/tutorial/crud-django-rest-framework-react/)
- [postgres commands](https://www.postgresqltutorial.com/postgresql-administration/postgresql-show-tables/)
- [session based Auth](https://www.youtube.com/watch?v=89KrqjqPeZ0)
- [django ModelViewSet docs](https://www.cdrf.co/3.1/rest_framework.viewsets/ModelViewSet.html)

## Lessions learned

- dont write your own auth from scratch use a library maybe try [Auth0 for react](https://auth0.com/blog/complete-guide-to-react-user-authentication/) next time. or in the future. Could also use [react auth kit](https://www.npmjs.com/package/react-auth-kit) first time mulligan I guess?
- ask more questions! how should I gamify this, right now every task is worth 10 points.
- made some guesses on gamification as well. Ask sooner not later.
- dont let the backend suffer because you cant figure out front end... it should be better than it is.

## known issues

- routes aren't protected, you will just get unuseable access to them. /dashboard and /todo
  - [try this](https://stackoverflow.com/questions/62384395/protected-route-with-react-router-v6)
  - [or this](https://stackoverflow.com/questions/66289122/how-to-create-a-protected-route-with-react-router-dom)
- registration sends plain text passwords.
- axios requests could be updated to use .then/.catch methods instead of nesting them in a try/catch
- most of the bodies of the backend are wrapped in try catch, (account/userprofile apps) not sure how I feel about that.
- there are no real rewards. In the future I could do avatars that unlock with points earned or something along those lines.
- using alerts for notifications.
- docker shoud be able to run whole thing, shoudnt need to restart after first run because database is slow to create.
- all tasks are worth the same.
- no notifications for tasks near due date.
- due dates are entirely pointless at the moment, it would be nice to tie points to how far from due date in future.
- userprofile endpoints arent super restful, it would be better if it was {base}/profile/{user_id}
- mobile interface for todo's isnt perfect.
