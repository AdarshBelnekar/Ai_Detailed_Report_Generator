import streamlit as st
import os

from modules.document_loader import extract_text
from modules.image_extractor import extract_images
from modules.ai_engine import generate_ddr
from modules.report_builder import build_report


st.set_page_config(page_title="AI DDR Generator", layout="wide")

st.title("AI Detailed Diagnostic Report Generator")

st.write("Upload the Inspection Report and Thermal Report to generate a DDR.")

inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf"])


if st.button("Generate DDR"):

    if inspection_file is None or thermal_file is None:
        st.warning("Please upload both documents.")
    
    else:

        os.makedirs("data", exist_ok=True)

        inspection_path = "data/inspection.pdf"
        thermal_path = "data/thermal.pdf"

        # Save uploaded files
        with open(inspection_path, "wb") as f:
            f.write(inspection_file.getbuffer())

        with open(thermal_path, "wb") as f:
            f.write(thermal_file.getbuffer())


        st.info("Extracting text from inspection report...")
        inspection_text = extract_text(inspection_path)

        st.info("Extracting text from thermal report...")
        thermal_text = extract_text(thermal_path)


        st.info("Extracting images from documents...")
        inspection_images = extract_images(inspection_path)
        thermal_images = extract_images(thermal_path)


        st.info("Generating AI DDR report...")
        report = generate_ddr(inspection_text, thermal_text)


        st.success("DDR Report Generated")

        st.subheader("Generated DDR Report")

        st.markdown(report)


        st.subheader("Extracted Images")

        all_images = inspection_images + thermal_images



        st.subheader("Download Final Report")

        pdf_path = build_report(report)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download DDR PDF",
                data=f,
                file_name="DDR_Report.pdf",
                mime="application/pdf"
            )