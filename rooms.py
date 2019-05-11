import tkinter as tk
app = ""
class rooms:
    def __init__(prefenses, monster_name, monster_hp, treser, doorleft, doorrigth, doorup, back):
         prefenses.monster_name = monster_name
         prefenses.monster_hp = monster_hp
         prefenses.treser = treser
         prefenses.doorleft = doorleft
         prefenses.doorrigth= doorrigth
         prefenses.doorup= doorup
         prefenses.back = back

    def showroom():
        #crate window
        app = tk.Tk()
        app.geometry('600x400')
        app.mainloop()
        #crate the doors in the grafic
        if doorup == True:
            app.door_up = tk.Button(app)
            app.door_up["text"] = u"\u2B06"
        if doorleft == True:
            app.door_left = tk.Button(app)
            app.door_left["text"] = u"\u2B05"
        if doorrigth == True:
            app.door_rigth = tk.Button(app)
            app.door_rigth["text"] = u"\u27A1"
        if back == True:
            app.back = tk.Button(app)
            app.back["text"] = 	u"\u2B07"

        if monster_name != None:


