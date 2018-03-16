import PyPDF2
import pickle
import pandas as pd

from tabula import read_pdf

df = read_pdf('aaa.pdf')

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


llist = [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]


def predict():
        # load the model from disk
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    llist = [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
    
    df = pd.DataFrame(llist)
    X_test = df.T
    
    
    y_pred = loaded_model.predict(X_test)

    if y_pred[0]==1:
        return('M')
    else:
        return('B')

if __name__ == '__main__':
    
    tlist = getText('aaa.pdf')

    ans = predict()
    
    print(ans)
    
 