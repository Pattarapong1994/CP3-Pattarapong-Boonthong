from tkinter import*
import math
def leftClickButton(event):
    result = float(textBoxWidth.get())/ math.pow(float(textBoxHeight.get())/100,2)
    if result >= 30.0:
        bmi = "อ้วนมาก"
    elif result < 30.0 and result >= 25.0:
        bmi = "อ้วน"
    elif result < 25.0 and result >= 23.0:
        bmi = "น้ำหนักเกิน"
    elif result < 23.0 and result >= 18.6:
        bmi = "น้ำหนักปกติ"
    else:
        bmi = "ผอมเกินไป"
    print(float(textBoxWidth.get())/ math.pow(float(textBoxHeight.get())/100,2))
    #ไม่จำเป็นต้องใส่ print ก็ได้ แต่เพื่อความมั่นใจของคำตอบเลยใส่ไว้
    labelcalculate.configure(text= bmi)

mainWindow = Tk()
labelHeight = Label(mainWindow,text="Height (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWidth = Label(mainWindow,text="Width (kg.)")
labelWidth.grid(row=1,column=0)
textBoxWidth = Entry(mainWindow)
textBoxWidth.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="Calcuate")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelcalculate = Label(mainWindow,text="Result N/A")
labelcalculate.grid(row=2,column=1)
mainWindow.mainloop()