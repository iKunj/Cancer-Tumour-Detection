from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import PyPDF2
from tkinter import *  
from PIL import ImageTk,Image  


root = tk.Tk()

global st

def getText(filename):
    tlist = []
    
    pdf_file = open('aaa.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    tlist = list(page_content.split())
    print(tlist)
    
    return tlist


def helloCallBack(ans):
    
    if ans=='M':
        ans = 'Malignant'
    else:
        ans = 'Benign'
    
    st = 'Your tumour is :'
    msg = messagebox.showinfo( "Results", 'Your tumour is : '+ans)
    st = 'Your tumour is :' + ans
    status = tk.Label(root, text="Status:"+st, bd=1, anchor = tk.W, relief = tk.SUNKEN)
    status.pack(fill = tk.X, side = tk.BOTTOM)

   
def predict():
        # load the model from disk
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    mlist = [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
    blist = [13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,	15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259]


    if ty == 'B':
        df = pd.DataFrame(blist)
    else:
        df = pd.DataFrame(mlist)
    X_test = df.T

    
    y_pred = loaded_model.predict(X_test)

    if y_pred[0]==1:
        return('M')
    else:
        return('B')
        
def check():

    ans = predict()
    helloCallBack(ans)

def open_command():
	

	file = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("PDF File", "*.pdf"),("All Files","*.*")),
                           title = "Choose a file."
                           )

	usefile = open(file, mode='rb')
	print(usefile)
    
	if file != None:
            contents = usefile.read()
            strr = str(usefile)
            tl = strr.split('/')
            a = tl[-1]
            a = a[0:7]
            print(a[0:7])
            if a == "aaa.pdf":
                global ty
                ty='M'
            else:
                #global ty
                ty='B'
                
            #print(contents)
            
root.minsize(width=400, height=400)

        
framea = tk.Frame(root)
framea.pack(side = tk.TOP)

w = tk.Label(framea, text="Hello Welcome to Tumour Detection!", padx=10,pady=10)
w.grid(columnspan=2)
#w.pack()
image = Image.open("med.jpg")
photo = ImageTk.PhotoImage(image)

label = tk.Label(image=photo)
label.image = photo # keep a reference!
label.pack(side = "bottom", fill = "both", expand = "yes")

B = tk.Button(framea, text ="Click to Upload your Report", command = open_command, padx=10,pady=10)

B.grid(rowspan=2,columnspan=2)

L2 = tk.Label(framea, text ="Now Click below to check your result!!!")
L2.grid(columnspan=2)


B1 = tk.Button(framea, text ="Check Result", command = check, padx=10,pady=20)

B1.grid(rowspan=3,columnspan=2)

L2 = tk.Label(framea, text ="About\n Cancer is a group of diseases involving abnormal \ncell growth with the potential to invade or spread \nto other parts of the body. These contrast with benign tumors, which\n do not spread to other parts of the body. Possible signs and symptoms\n include a lump, abnormal bleeding, prolonged cough, \nunexplained weight loss, and a change in bowel movements.",padx=10,pady=20)
L2.grid(columnspan=2)


L2 = tk.Label(framea, text ="The Results will be shown that whether the tumour is Malignant or Benign",padx=10,pady=20)
L2.grid(columnspan=2)

st = 'Upload the PDF report file and click Check Result'

status = tk.Label(root, text="Status:"+st, bd=1, anchor = tk.W, relief = tk.SUNKEN)
status.pack(fill = tk.X, side = tk.BOTTOM)


root.mainloop()