from Tkinter import *
root = Tk()

def hello():
	data_get = get_text.get()
	print(data_get)
	get_text.delete(0 , END)

root.title("Chat by python")
root.geometry("400x800")
root.resizable(width=False, height=False)

lbl = Label(root , text="hello" , bg="white" , fg="black" , borderwidth=2 , relief="ridge")
lbl.pack(fill=X , side=BOTTOM)

but = Button(root , text="Click Me" , command=hello)
but.pack(fill=X , side = BOTTOM)

get_text = Entry(root)
get_text.pack(fill = X , side=BOTTOM)


root.mainloop()
