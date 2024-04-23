import streamlit as st


st.set_page_config(
    page_title="Water Potability Prediction",
    initial_sidebar_state="expanded"

)
st.sidebar.success("selact a page above")
st.markdown(
    """
    <style>
    body {
    .heading-container {
        background-color: #56ECDD; /* White background color */
        padding: 2px 35px; /* Padding */
        border-radius: 10px; /* Rounded corners */
        box-shadow: 2px 2px 5px grey; /* Box shadow */
    }

    .heading-text {
        font-size: 80px; /* Font size */
        color:#FFFFFF; /* Text color */
        font-weight: bold; /* Font weight */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<div class="heading-container"><span class="heading-text">INTRODUCTION</span></div>',
    unsafe_allow_html=True
)
st.write("     ")
st.write("     ")
# st.video("https://raw.githubusercontent.com/jaykumar1607/Water-Quality/main/water_sanitation.gif", start_time=0, format='mp4')
st.image("https://raw.githubusercontent.com/jaykumar1607/Water-Quality/main/water_sanitation.gif",width=700)
st.write("Safe and readily available water is important for public health, whether it is used for drinking, domestic use, food production or recreational purposes."
         "Improved water supply and sanitation, and better management of water resources, can boost countries’ economic growth and can contribute greatly to poverty reduction.",)
st.write("Contaminated water and poor sanitation are linked to transmission of diseases such as cholera, diarrhoea, dysentery, hepatitis A, typhoid, and polio."
         " Absent, inadequate, or inappropriately managed water and sanitation services expose individuals to preventable health risks."
         " This is particularly the case in health care facilities where both patients and staff are placed at additional risk of infection and disease when water, sanitation, and hygiene services are lacking. "
         "Globally, 15% of patients develop an infection during a hospital stay, with the proportion much greater in low-income countries.")
st.write("So, I took some inspiration from this to use this Water Quality dataset to understand what consitutes to safe,"
         " Potable water and apply machine learning to it to distinguish between Potable and Non-Potable water.")

st.markdown(
    """
    <style>
    .heading-text {
        font-size: 50px; /* Font size */
        color:#000000; /* Text color */
        font-weight: bold; /* Font weight */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.write("   ")
st.markdown("## CONTACT")
st.write("  ")

st.markdown("[Instagram](https://www.instagram.com/f.aroo.k?igsh=M2dlYzZvN213b3cy)")
