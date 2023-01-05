from tkinter import *

def small():
	file.write("Small\n")
def med():
	file.write("Medium\n")
def large():
	file.write("Large\n")
		  
def mel():
	file.write("Water Melon Juice     ")
	sizeWindow()
def straw():
	file.write("Strawberry Juice      ")
	sizeWindow()
def qasab():
	file.write("Qasab Juice           ")
	sizeWindow()
def mango():
	file.write("Mango Juice           ")
	sizeWindow()

file = open("orders.txt","w+")
file.write("Orders:\n")

main1 = Tk()
main1.title("Qasab Shop")
main1.geometry('440x170')



photo_water = PhotoImage(file = "water.png")
photo_water = photo_water.subsample(11,11)
photo_straw = PhotoImage(file = "Strawberry.png")
photo_straw = photo_straw.subsample(12,12)
photo_qasab = PhotoImage(file = "qasab.png")
photo_qasab = photo_qasab.subsample(2,2)
photo_mango = PhotoImage(file = "Mango.png")
photo_mango = photo_mango.subsample(12,12)

lm_water = Label(main1,image=photo_water).grid(row=0,column=0)
lm_straw = Label(main1,image=photo_straw).grid(row=0,column=1)
lm_qasab = Label(main1,image=photo_qasab).grid(row=0,column=2)
lm_mango = Label(main1,image=photo_mango).grid(row=0,column=3)

bm_water = Button(main1,text="Water Melon",bd=4,background='orange', command=mel).grid(row=1,column=0)
bm_straw = Button(main1,text="Strawberry",bd=4,background='orange',command=straw).grid(row=1,column=1)
bm_qasab = Button(main1,text="Qasab",bd=4,background='orange', command=qasab).grid(row=1,column=2)
bm_mango = Button(main1,text="Mango",bd=4,background='orange',command=mango).grid(row=1,column=3)

exit_button = Button(main1, text="Exit",bd=3,fg="#fa5b3d",font=('optima',12), command=main1.destroy).grid(row=2)


def sizeWindow():
	sizeW = Toplevel(main1)
	sizeW.title("Choose Cup size")
	sizeW.geometry("300x140")
	size_small = Button(sizeW,text="Small",bd=4,background='orange',command=small).grid(row=0,column=0)
	size_med = Button(sizeW,text="Medium",bd=4,background='orange',command=med).grid(row=1,column=0)
	size_large = Button(sizeW,text="Large",bd=4,background='orange',command=large).grid(row=2,column=0)
	exit_button = Button(sizeW, text="Exit",bd=3,fg="#fa5b3d",font=('optima',12), command=sizeW.destroy).grid(row=3)
	
main1.mainloop()