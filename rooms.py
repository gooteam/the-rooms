from tkinter import *
app = ""
class Rooms:
    def __init__(prefenses, monster_name, monster_hp, treser, doorleft, doorrigth, doorup, back):
         prefenses.monster_name = monster_name
         prefenses.monster_hp = monster_hp
         prefenses.treser = treser
         prefenses.doorleft = doorleft
         prefenses.doorrigth= doorrigth
         prefenses.doorup= doorup
         prefenses.back = back

    def showroom(self):
        #crate window
        app = Tk()
        app.geometry('600x400')
        app.mainloop()
        #crate the doors in the grafic
        if doorup == True:
            app.door_up = tk.Button(app)
            app.door_up["text"] = u"\u2B06"
            app.door_left.pack(side="top")
        if doorleft == True:
            app.door_left = tk.Button(app)
            app.door_left["text"] = u"\u2B05"
            app.door_left.pack(side="left")
        if doorrigth == True:
            app.door_rigth = tk.Button(app)
            app.door_rigth["text"] = u"\u27A1"
            app.door_rigth.pack(side="right")
        if back == True:
            app.back = tk.Button(app)
            app.back["text"] = 	u"\u2B07"
            app.back.pack(side="bottom")
        if monster_name != None:
            monser_name_label = Label( app, text= monster_name, relief = RAISED )
            monser_name_label.pack(side="top")
            monser_name_label.place(x=278, y=80)
            monser_level_label_set = StringVar()
            monser_level_label = Label( app, textvariable = monser_level_label_set, relief = RAISED)
            monser_level_label_set.set("life level: 100hp")
            monser_level_label.pack(side="top")
            monser_level_label.place(x=245, y=110)
        #humen difint in the page i will mack a bag
        life_humen_level_set = StringVar()
        life_humen_level = Label( app, textvariable = life_humen_level_set, relief = RAISED )
        life_humen_level_set.set("your life level: 100hp")
        life_humen_level.pack()
        life_humen_level.place(x=0, y=0)
        app.mainloop()

word = Rooms("monster_name", "monster_hp", "treser", True, True, True, True)
word.showroom()
