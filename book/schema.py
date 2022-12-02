import graphene
from graphene_django.types import DjangoObjectType

from .models import BookInfo


class BookType(DjangoObjectType):
    class Meta:
        model = BookInfo


# 定义动作，类似POST, PUT, DELETE
class BookInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    author = graphene.String(required=True)

class CreateBook(graphene.Mutation):
    # api的输入参数
    class Arguments:
        book_data = BookInput(required=True)

    # api的响应参数
    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    # api的相应操作，这里是create
    def mutate(self, info, book_data):
        book = BookInfo.objects.create(name=name, author=author)
        ok = True
        return CreateBook(book=book, ok=ok)

class Query(object):
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        # 查询所有book的逻辑
        return BookInfo.objects.all()
