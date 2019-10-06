import graphene
import movies.api.schema

class Query(movies.api.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)