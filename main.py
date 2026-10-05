import tkinter as tk
window = tk.Tk()
window.title("Wordle")
window.geometry("600x700")
window.configure(bg="#121213")
canvas=tk.Canvas(window,width=600,height=700,bg="#121213")
canvas.pack()
start_x=100 
start_y=100
size=70
gap=10

for row in range(6):
    for col in range(5):
        x1= start_x + col*(gap+size)
        y1=start_x + row*(gap+size)
        x2= x1+size
        y2=y1+size
        canvas.create_rectangle(x1,y1,x2,y2,outline="white",width=2)

window.mainloop()

