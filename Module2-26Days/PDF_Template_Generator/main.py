from fpdf import FPDF

#setting the orientation of the pdf we can pass L for landscape and P for portrait
pdf  =  FPDF(orientation='P', unit="mm",format = "A4")

#ADD PAGES TO PDF
pdf.add_page()

#adding topics in the pdf
pdf.set_font(family="Times",style='B',size=12)
pdf.cell(w=0, h=12, txt="Hello There", border=1, ln=1, align='L')

#saving this pdf to same directory
pdf.output("output.pdf")