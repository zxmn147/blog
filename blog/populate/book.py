from populate import base

import datetime
import random
from book.models import Book



def populate():
    print('Populating Book...', end='')
    titles = ['python', '小王子' , 'Java' , '黑子的籃球' , 'Django' , '管理數學' , '計概' , 'c++' , 'vb' ,'少年陰陽師']
    authornames = ['王一' , '王二' , '王三']
    Book.objects.all().delete()
    for title in titles:
        book = Book()
        book.title = title
        book.authorname = authornames[random.randint(0,len(authornames)-1)]
        book.Publisher=book.authorname
        book.Date=datetime.datetime.today()
        book.version = '1'
        book.price = 1000
        book.save()
    print('done')    
        
if __name__ == '__main__':
    populate()