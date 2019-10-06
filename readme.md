# GraphQL + Django

Django Project utlizing Graphql to serve the models.


to use install requirements.txt

    pip install -r requirements.txt

then run the django server

    python manage.py runserver
    
After that you can visit http://localhost:8000/graphql and query the following

    query{
      allMovies{
        title
      }
    }
    
or to get one movie pass the following, do the following.

    query{
      movie(id:<PLACE_ID_HERE>) {
        title
      }
    }