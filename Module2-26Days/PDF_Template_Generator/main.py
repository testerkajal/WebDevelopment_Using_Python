import streamlit as st
import pandas as pd
import os
from generate_pdf import generate_pdf
from help import display_help


def main():
    st.set_page_config(page_title="PDF Generator", layout="centered")

    menu = ["Application", "Help"]
    choice = st.sidebar.selectbox("📌 Select Page", menu)

    if choice == "Application":
        st.markdown("""
        <h1 style='text-align: center; color: #4CAF50;'>📄 PDF Generator from CSV</h1>
        """, unsafe_allow_html=True)

        st.write("Upload a CSV file and generate a structured PDF.")
        uploaded_file = st.file_uploader("📂 Upload CSV file", type=['csv'])

        if uploaded_file:
            df = pd.read_csv(uploaded_file)  # Read file as DataFrame
            if st.button("🚀 Generate PDF", help="Click to generate your PDF file"):
                output_pdf_path = generate_pdf(df)
                st.success("✅ PDF generated successfully!")

                # Provide a download button for the generated PDF
                with open(output_pdf_path, "rb") as file:
                    st.download_button(
                        label="📥 Download PDF",
                        data=file,
                        file_name="generated_output.pdf",
                        mime="application/pdf"
                    )

    elif choice == "Help":
        display_help()





if __name__ == "__main__":
    main()