class Stationery:

    def draw(self, title):
        self.title = title
        print('Начинается отрисовка' )

class Pen(Stationery):

    def draw(self, title):
        print('Начинается отрисовка by', title)

class Pensil(Stationery):

    def draw(self, title):
        print('Начинается отрисовка by ', title)

class Handle(Stationery):

    def draw(self, title):
        print('Начинается отрисовка by', title)

pen = Pen()
pen.draw('ручка')

pensil = Pensil()
pensil.draw('карандаш')

handle = Handle()
handle.draw('маркер')
