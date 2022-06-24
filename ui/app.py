from tkinter import *
from tkinterdnd2 import *
import file_m

# creer une premiere fenetre
window = Tk()

# personnaliser la fenêtre
window.title("Master Campeurs")
window.geometry("1080x720+50+40")
window.minsize(480, 480)
window.iconbitmap("")
window.config(background='#00C522')

frame = Frame(window)
frame.pack()

"""
frame_header = Frame(window, width=1000, height=100, bg='#ffffff')

labal_titlte = Label(frame_header, text="Master Campeur", font=("Courrier", 40))


frame_left = Frame(window, width=100, height=710, bg='#C17830')
frame_left.grid(row=0, column=0, sticky=N, padx=5, pady=5)

frame_drag_drop = Frame(window, width=960, height=710, bg='#FFFBF7')
frame_drag_drop.grid(row=0, column=1, sticky=W, padx=(0, 5), pady=5)
"""


def path_listbox(event):
    listbox.insert("end", event.data)



listbox = Listbox(
    frame,
    width=50,
    height=15,
    selectmode=SINGLE,
)
listbox.pack(fill=X, side=LEFT)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', path_listbox)

scrolbar = Scrollbar(
    frame,
    orient=VERTICAL
)
scrolbar.pack(side=RIGHT, fill=Y)
# displays the content in listbox
listbox.configure(yscrollcommand=scrolbar.set)
# view the content vertically using scrollbar
scrolbar.config(command=listbox.yview)


# afficher
window.mainloop()
