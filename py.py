import peewee 
from peewee import PostgresqlDatabase
from datetime import datetime
db = PostgresqlDatabase(
'orm_py25',
user = 'samat',
password = '1' ,
host = 'localhost',
port = 5432
)


class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100, unique = True) #charfield = varchar
    created_at = peewee.DateTimeField(default= datetime.now())

    class Meta:
        database = db
        db_table = 'category'

class Product(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10 , decimal_places=2 , default = 10)
    amount = peewee.IntegerField(null=False)
    category = peewee.ForeignKeyField(Category , related_name='products', to_field='id' , on_delete='cascade')
    class Meta:
        database = db
        db_table = 'product'

db.connect()


def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print('saved!!!')
    except peewee.IntegrityError:
        print('Такая категория уже существует!')


def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'{category.id} -{category.name}- {category.created_at}')
    print((categories))

def delete_category(category_id):
    try:
        category = Category.get(id = category_id)
        category.delete_instance()
        print('Deleted!!!')
    except peewee.DoesNotExist:
        print('Категория для удаления не найдено')
def update_category(category_id, new_name):
    try:
        category = Category.get(id = category_id)
        category.name = new_name
        category.save()
        print('Обнавление прошло успешно!!!')
    except peewee.DoesNotExist:
        print('Категория для обновления не найдено')

# def detail_category(category_id):
#     try:
#         category = Category.get(id = category_id)
#         products = Product.select().where(Product.category == category)
#         print(f'Category: {category.name}')
#         print('Products in this category:')
#         for product in products:
#             print(f'{product.id} - {product.name} - {product.price} - {product.amount}')
#     except peewee.DoesNotExist:
#         print('Category not found')
# def detail_category(category_id):
#     try:
#         category = Category.get(id = category_id)
#         print(f'Category: {category.name}, Id: {category.id}, Created at: {category.created_at}')
        
#     except peewee.DoesNotExist:
#         print('Category not found')

# detail_category(15)


# def func():
#     try:
#         print('!!!')
#         return 0
#     finally:
#         print('!!')
#         return 1
# print(func())

# class A:
#     def __init__(self,name):
#         self.name = name

#     def get_info(self):
#         return f'my name is {self.name}'
# onj = A('j')
# print(A('john').get_info())