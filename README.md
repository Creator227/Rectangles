# Rectangles
Условие.
На плоскости заданы N прямоугольников со сторонами, параллельными осям координат. 
Прямоугольники могут пересекаться, совпадать друг с другом или быть нарисованы один внутри другого. 
Координаты вершин прямоугольников – целые неотрицательные числа, причем координата x не превосходит параметра Xmax ,
а координата y - параметра Ymax . Из точки A(0, 0) в точку B с целочисленными координатами, лежащую на одном из отрезков 
[(0, Ymax), (Xmax, Ymax)] либо [(Xmax, 0), (Xmax, Ymax)], проведен отрезок. Отрезок AB может пересекать построенные прямоугольники
(будем считать, что отрезок пересекает прямоугольник, даже если отрезок проходит только через одну из его вершин).
Вы должны найти такую точку B, удовлетворяющую описанным выше условиям, что отрезок AB пересечет максимальное число прямоугольников.