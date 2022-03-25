"""
File: my_drawing
Name: Ariel Pai
----------------------
TODO: Draw~~~
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Happy New Year, Everyone!
    """
    window = GWindow(800, 800)
    rect = GRect(800, 800, x=0, y=0)
    rect.filled = True
    rect.fill_color = 'black'
    rect.color = 'black'
    window.add(rect)

    circle_3 = GOval(550, 550, x=-120, y=280)
    circle_3.filled = True
    circle_3.fill_color = 'red'
    circle_3.color = 'red'
    window.add(circle_3)

    circle_2 = GOval(400, 400, x=-50, y=350)
    circle_2.filled = True
    circle_2.fill_color = 'tomato'
    circle_2.color = 'tomato'
    window.add(circle_2)

    circle_1 = GOval(250, 250, x=20, y=420)
    circle_1.filled = True
    circle_1.fill_color = 'red'
    circle_1.color = 'red'
    window.add(circle_1)

    lantern_1 = GPolygon()
    lantern_1.add_vertex((100, 180))  # point A
    lantern_1.add_vertex((200, 110))  # point B
    lantern_1.add_vertex((210, 350))  # point C
    lantern_1.add_vertex((180, 370))  # point D
    lantern_1.filled = True
    lantern_1.fill_color = 'tomato'
    window.add(lantern_1)

    lantern_2 = GPolygon()
    lantern_2.add_vertex((200, 110))  # point B
    lantern_2.add_vertex((320, 160))  # point E
    lantern_2.add_vertex((270, 360))  # point F
    lantern_2.add_vertex((210, 350))  # point C
    lantern_2.filled = True
    lantern_2.fill_color = 'white'
    window.add(lantern_2)

    lantern_3 = GPolygon()
    lantern_3.add_vertex((180, 370))  # point D
    lantern_3.add_vertex((210, 350))  # point C
    lantern_3.add_vertex((270, 360))  # point F
    lantern_3.add_vertex((240, 380))  # point G
    lantern_3.filled = True
    lantern_3.fill_color = 'yellow'
    window.add(lantern_3)

    lantern_4 = GPolygon()
    lantern_4.add_vertex((370, 400))  # point J
    lantern_4.add_vertex((510, 345))  # point K
    lantern_4.add_vertex((470, 320))  # point I
    lantern_4.add_vertex((400, 350))  # point H
    lantern_4.filled = True
    lantern_4.fill_color = 'white'
    window.add(lantern_4)

    lantern_5 = GPolygon()
    lantern_5.add_vertex((470, 320))  # point I
    lantern_5.add_vertex((540, 340))  # point N
    lantern_5.add_vertex((560, 360))  # point O
    lantern_5.add_vertex((510, 345))  # point K
    lantern_5.filled = True
    lantern_5.fill_color = 'white'
    window.add(lantern_5)

    lantern_6 = GPolygon()
    lantern_6.add_vertex((370, 400))  # point J
    lantern_6.add_vertex((510, 345))  # point K
    lantern_6.add_vertex((500, 500))  # point M
    lantern_6.add_vertex((450, 525))  # point L
    lantern_6.filled = True
    lantern_6.fill_color = 'white'
    window.add(lantern_6)

    lantern_7 = GPolygon()
    lantern_7.add_vertex((510, 345))  # point K
    lantern_7.add_vertex((560, 360))  # point O
    lantern_7.add_vertex((530, 510))  # point P
    lantern_7.add_vertex((500, 500))  # point M
    lantern_7.filled = True
    lantern_7.fill_color = 'tomato'
    window.add(lantern_7)

    lantern_8 = GPolygon()
    lantern_8.add_vertex((450, 525))  # point L
    lantern_8.add_vertex((500, 500))  # point M
    lantern_8.add_vertex((530, 510))  # point P
    lantern_8.add_vertex((480, 535))  # point Q
    lantern_8.filled = True
    lantern_8.fill_color = 'yellow'
    window.add(lantern_8)

    lantern_9 = GPolygon()
    lantern_9.add_vertex((590, 120))  # point R
    lantern_9.add_vertex((650, 135))  # point S
    lantern_9.add_vertex((675, 190))  # point T
    lantern_9.add_vertex((550, 165))  # point U
    lantern_9.filled = True
    lantern_9.fill_color = 'white'
    window.add(lantern_9)

    lantern_10 = GPolygon()
    lantern_10.add_vertex((545, 145))  # point V
    lantern_10.add_vertex((590, 120))  # point R
    lantern_10.add_vertex((550, 165))  # point U
    lantern_10.add_vertex((510, 175))  # point W
    lantern_10.filled = True
    lantern_10.fill_color = 'white'
    window.add(lantern_10)

    lantern_11 = GPolygon()
    lantern_11.add_vertex((510, 175))  # point W
    lantern_11.add_vertex((550, 165))  # point U
    lantern_11.add_vertex((555, 250))  # point X
    lantern_11.add_vertex((525, 260))  # point Y
    lantern_11.filled = True
    lantern_11.fill_color = 'white'
    window.add(lantern_11)

    lantern_12 = GPolygon()
    lantern_12.add_vertex((550, 165))  # point U
    lantern_12.add_vertex((675, 190))  # point T
    lantern_12.add_vertex((630, 265))  # point Z
    lantern_12.add_vertex((555, 250))  # point X
    lantern_12.filled = True
    lantern_12.fill_color = 'red'
    window.add(lantern_12)

    lantern_13 = GPolygon()
    lantern_13.add_vertex((525, 260))  # point Y
    lantern_13.add_vertex((555, 250))  # point X
    lantern_13.add_vertex((630, 265))  # point Z
    lantern_13.add_vertex((600, 275))  # point AA
    lantern_13.filled = True
    lantern_13.fill_color = 'yellow'
    window.add(lantern_13)

    rect = GRect(800, 100, x=300, y=600)
    rect.filled = True
    rect.fill_color = 'orange'
    rect.color = 'orange'
    window.add(rect)
    label = GLabel('新年快樂！')
    label.color = 'black'
    label.font = 'Courier-60-italic'
    window.add(label, 300, 700)




if __name__ == '__main__':
    main()
