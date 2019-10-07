import tkinter as tk
    

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
   
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="what is 2+2?",
                   command=helloCallBack)
slogan.pack(side=tk.LEFT)

root.mainloop()
