from fpdf import FPDF
import pandas as pd




#setting the orientation of the pdf we can pass L for landscape and P for portrait
pdf  =  FPDF(orientation='P', unit="mm",format = "A4")

df  = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    #ADD PAGES TO PDF
    pdf.add_page()

    #setting up font size and font family
    pdf.set_font(family="Times",style='B',size=24)

    #to change the text color
    #pdf.set_text_color(100,100,100)

    # adding topics in the pdf
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='L')

    # Add a line below the heading
    pdf.line(10,21,200,21)

#saving this pdf to same directory
pdf.output("output.pdf")

