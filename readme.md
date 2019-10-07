# GraphQL + Django

Django Project utlizing Graphql to serve the models.


to use install requirements.txt

    pip install -r requirements.txt

then run the django server

    python manage.py runserver
    
After that you can visit http://localhost:8000/graphql and query the following

    query AllMovies{
      allMovies(title: "Timecop") {
        edges{
          node{
            id
            title
          }
        }
      }
    }
   
Querying movies that contain character of "a" in the title

    query AllMovies{
      allMovies(title_Icontains: "a") {
        edges{
          node{
            id
            title
          }
        }
      }
    }
    
relay mutations will be similar:

    mutation MutateRelay{
      updateMovieRelay(
        input: {id: "TW92aWVOb2RlOjI=", title: "New Title Here"}
      ){
        movie {
          id
          title
          year
        }
      }
    }

or to get one movie pass the following, do the following.

    query{
      movie(id:<PLACE_ID_HERE>) {
        title
      }
    }