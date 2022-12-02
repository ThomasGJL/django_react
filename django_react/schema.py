import graphene
import book.schema

class Query(book.schema.Query, graphene.ObjectType):
    # 总的Schema的query入口
    book_list = book.schema.Query.all_books
    pass

class Mutations(graphene.ObjectType):
    # 总的Schema的mutations入口
    create_book = book.schema.CreateBook.Field()
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)
