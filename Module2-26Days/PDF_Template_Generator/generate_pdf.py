from fpdf import FPDF


def generate_pdf(df):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)

    for index, row in df.iterrows():
        for _ in range(row["Pages"]):
            pdf.add_page()
            pdf.set_font(family="Times", style='B', size=24)
            pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='L')

            for i in range(20, 298, 10):
                pdf.line(10, i, 200, i)

            pdf.ln(265)
            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

    output_path = "output.pdf"
    pdf.output(output_path)
    return output_path
