# # import streamlit as st

# # st.set_page_config(page_title="Unit Converter", layout="centered")

# # st.title("🔄 Unit Converter")

# # # Category selection
# # category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# # # Length conversions
# # def convert_length(value, from_unit, to_unit):
# #     units = {
# #         "meters": 1,
# #         "kilometers": 1000,
# #         "miles": 1609.34,
# #         "feet": 0.3048
# #     }
# #     return value * units[from_unit] / units[to_unit]

# # # Weight conversions
# # def convert_weight(value, from_unit, to_unit):
# #     units = {
# #         "kilograms": 1,
# #         "grams": 0.001,
# #         "pounds": 0.453592,
# #         "ounces": 0.0283495
# #     }
# #     return value * units[from_unit] / units[to_unit]

# # # Temperature conversions
# # def convert_temperature(value, from_unit, to_unit):
# #     if from_unit == to_unit:
# #         return value
# #     if from_unit == "Celsius":
# #         if to_unit == "Fahrenheit":
# #             return (value * 9/5) + 32
# #         elif to_unit == "Kelvin":
# #             return value + 273.15
# #     elif from_unit == "Fahrenheit":
# #         if to_unit == "Celsius":
# #             return (value - 32) * 5/9
# #         elif to_unit == "Kelvin":
# #             return ((value - 32) * 5/9) + 273.15
# #     elif from_unit == "Kelvin":
# #         if to_unit == "Celsius":
# #             return value - 273.15
# #         elif to_unit == "Fahrenheit":
# #             return ((value - 273.15) * 9/5) + 32

# # # Input section
# # value = st.number_input("Enter Value", value=0.0)

# # if category == "Length":
# #     units = ["meters", "kilometers", "miles", "feet"]
# #     from_unit = st.selectbox("From", units)
# #     to_unit = st.selectbox("To", units)
# #     result = convert_length(value, from_unit, to_unit)

# # elif category == "Weight":
# #     units = ["kilograms", "grams", "pounds", "ounces"]
# #     from_unit = st.selectbox("From", units)
# #     to_unit = st.selectbox("To", units)
# #     result = convert_weight(value, from_unit, to_unit)

# # elif category == "Temperature":
# #     units = ["Celsius", "Fahrenheit", "Kelvin"]
# #     from_unit = st.selectbox("From", units)
# #     to_unit = st.selectbox("To", units)
# #     result = convert_temperature(value, from_unit, to_unit)

# # # Output
# # st.markdown(f"### Result: `{result:.2f}` {to_unit}")


# import streamlit as st
# from io import BytesIO
# from reportlab.pdfgen import canvas

# st.set_page_config(page_title="Unit Converter", layout="centered")

# st.title("🔄 Unit Converter")

# # Category selection
# category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# # Length conversions
# def convert_length(value, from_unit, to_unit):
#     units = {
#         "meters": 1,
#         "kilometers": 1000,
#         "miles": 1609.34,
#         "feet": 0.3048
#     }
#     return value * units[from_unit] / units[to_unit]

# # Weight conversions
# def convert_weight(value, from_unit, to_unit):
#     units = {
#         "kilograms": 1,
#         "grams": 0.001,
#         "pounds": 0.453592,
#         "ounces": 0.0283495
#     }
#     return value * units[from_unit] / units[to_unit]

# # Temperature conversions
# def convert_temperature(value, from_unit, to_unit):
#     if from_unit == to_unit:
#         return value
#     if from_unit == "Celsius":
#         if to_unit == "Fahrenheit":
#             return (value * 9/5) + 32
#         elif to_unit == "Kelvin":
#             return value + 273.15
#     elif from_unit == "Fahrenheit":
#         if to_unit == "Celsius":
#             return (value - 32) * 5/9
#         elif to_unit == "Kelvin":
#             return ((value - 32) * 5/9) + 273.15
#     elif from_unit == "Kelvin":
#         if to_unit == "Celsius":
#             return value - 273.15
#         elif to_unit == "Fahrenheit":
#             return ((value - 273.15) * 9/5) + 32

# # Input section
# value = st.number_input("Enter Value", value=0.0)

# if category == "Length":
#     units = ["meters", "kilometers", "miles", "feet"]
#     from_unit = st.selectbox("From", units)
#     to_unit = st.selectbox("To", units)
#     result = convert_length(value, from_unit, to_unit)

# elif category == "Weight":
#     units = ["kilograms", "grams", "pounds", "ounces"]
#     from_unit = st.selectbox("From", units)
#     to_unit = st.selectbox("To", units)
#     result = convert_weight(value, from_unit, to_unit)

# elif category == "Temperature":
#     units = ["Celsius", "Fahrenheit", "Kelvin"]
#     from_unit = st.selectbox("From", units)
#     to_unit = st.selectbox("To", units)
#     result = convert_temperature(value, from_unit, to_unit)

# # Output result
# st.markdown(f"### Result: `{result:.2f}` {to_unit}")

# # Generate PDF in memory
# def create_pdf(value, from_unit, to_unit, result):
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer)
#     c.drawString(100, 750, "Unit Conversion Result")
#     c.drawString(100, 720, f"Category: {category}")
#     c.drawString(100, 700, f"From: {value} {from_unit}")
#     c.drawString(100, 680, f"To: {result:.2f} {to_unit}")
#     c.save()
#     buffer.seek(0)
#     return buffer

# # Show download button
# if value:
#     pdf = create_pdf(value, from_unit, to_unit, result)
#     st.download_button(
#         label="📄 Download Result as PDF",
#         data=pdf,
#         file_name="conversion_result.pdf",
#         mime="application/pdf"
#     )


import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Page config with custom background color
st.set_page_config(page_title="Professional Unit Converter", layout="centered")

# CSS Styling for Google-like modern UI
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .stApp {
        background: linear-gradient(145deg, #ffffff, #e6ecf5);
        border-radius: 16px;
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 0 15px rgba(0,0,0,0.05);
    }
    .title {
        font-size: 36px;
        font-weight: 700;
        color: #202124;
        text-align: center;
        margin-bottom: 30px;
    }
    .stDownloadButton > button {
        background-color: #1a73e8;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🔄 Professional Unit Converter</div>', unsafe_allow_html=True)

# Category selection
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    units = {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048
    }
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    }
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32

# Input UI
value = st.number_input("Enter Value", value=0.0)

if category == "Length":
    units = ["meters", "kilometers", "miles", "feet"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = convert_length(value, from_unit, to_unit)

elif category == "Weight":
    units = ["kilograms", "grams", "pounds", "ounces"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = convert_weight(value, from_unit, to_unit)

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = convert_temperature(value, from_unit, to_unit)

# Result Display
st.markdown(f"### ✅ Result: `{result:.2f}` {to_unit}")

# PDF Generator
def create_pdf(value, from_unit, to_unit, result):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, height - 100, "📄 Unit Conversion Result")
    c.setFont("Helvetica", 14)
    c.drawString(100, height - 140, f"Category: {category}")
    c.drawString(100, height - 160, f"From: {value} {from_unit}")
    c.drawString(100, height - 180, f"To: {result:.2f} {to_unit}")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, height - 220, "Generated by Professional Unit Converter App")
    c.save()
    buffer.seek(0)
    return buffer

# Show download button if input is valid
if value:
    pdf = create_pdf(value, from_unit, to_unit, result)
    st.download_button(
        label="📥 Download as PDF",
        data=pdf,
        file_name="conversion_result.pdf",
        mime="application/pdf"
    )
