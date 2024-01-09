from Pen import Pen
from Shop import Shop

pen = Pen(10)
pen.add(Shop('Shop1'))
pen.add(Shop('Shop2'))
pen.add(Shop('Shop3'))

pen.penPrize = 15
pen.penPrize = 20

pen.remove(pen.shops[0])

pen.penPrize = 30

pen.add(Shop('Shop4'))

pen.penPrize = 20