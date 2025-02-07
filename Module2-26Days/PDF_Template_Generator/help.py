import streamlit as st


def display_help():
    st.markdown("""
    <h1 style='text-align: center; color: #2196F3;'>📖 Help Documentation</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    ## 📝 How to Use This Application

    **1️⃣ Upload a CSV File:**
    - Click on **Browse files** to select your CSV file.
    - Ensure the file follows the required format.

    **2️⃣ CSV File Format:**
    - The CSV file must have two columns:
      - **Topic**: The title of the topic.
      - **Pages**: Number of pages required for that topic.

    **📌 Example CSV Format:**
    ```
    Topic,Pages
    Python Basics,2
    Data Science,3
    ```

    **3️⃣ Generate PDF:**
    - Click the **🚀 Generate PDF** button.
    - The system will process your file and create a structured PDF.

    **4️⃣ Download Your PDF:**
    - Once the PDF is generated, click the **📥 Download PDF** button to save it.

    **💡 Tips:**
    - Ensure the CSV file has no missing values.
    - Use meaningful topic names to organize your PDF better.

    **🔍 Need Help?**
    - If you encounter issues, check your CSV file format.
    - Contact support for further assistance.
    """)
