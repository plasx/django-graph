# GraphQL + Django

Django Project utlizing Graphql to serve the models.


to use install requirements.txt

    pip3 install -r requirements.txt

then run the django server

    python3 manage.py runserver
    
Dump GraphQL Schema to schema.json. This is useful for frontend developers who don't have time to stand up their python environment for this application:
    
    python3 manage.py graphql_schema
    
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
    
Controlling the amount of pages works as so.

    query AllMoviesPagination{
      allMovies(first: 2) {
        pageInfo{
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
        }
        edges{
          node{
            id
            title
          }
        }
      }
    }
Pagination works as follows, below it means you want the first 2 results after the cursor item "TW92aWVOb2RlOjk=" which is the item you might of gotten in the original query(above):
    
    query AllMoviesPagination{
      allMovies(first: 2, after: "TW92aWVOb2RlOjk=") {
        pageInfo{
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
        }
        edges{
          node{
            id
            title
          }
        }
      }
    }