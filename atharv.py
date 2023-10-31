from tkinter import *
import pickle
def color():
    with open('buttons.dat','rb') as f:
        a=pickle.load(f)
        for i in a:
            if a[i]==1:
                exec(f'{i}.configure(bg="RED")')    
window =Tk()
val={i:0 for i in [f'{j}{k}' for j in 'ABCDE' for k in range(1,11)]}
d=65
for i in range(50,501,50):
    for j in range(100,501,100):
        h=f'{chr(d)}{j//100}'
        exec(f'global {h}')
        exec(f'{h}=Button(window,text="{h}")')
        exec(f'{h}.place(x={i},y={j})')
        exec(f'''def sub{h}():
                val[f"{h}"]=1
                with open("buttons.dat","wb") as f:
                    pickle.dump(val,f)
                color()
                ''')
        exec(f'{h}.configure(command=sub{h})')
    d+=1

window.mainloop()
