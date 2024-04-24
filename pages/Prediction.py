import streamlit as st
import pickle
from PIL import Image

def main():

    st.title(":red[WATER POTABILITY PREDICTION ]")
    # image=Image.open('potable-water-1429216_1920.jpg')
    st.image("https://www.unicef.org/sites/default/files/styles/hero_extended/public/UNI182807.jpg.webp?itok=SL076Pyp")
    # ph=st.text_input("pH value")
    ph = st.slider("Select ph value", min_value=2.0, max_value=14.0, value=0.25)
    Hardness= st.text_input("Hardness")
    Solids= st.text_input("Solids",help="Total dissolved solids in ppm")
    Chloramines= st.text_input("Chloramines ",help="Amount of Chloramines in ppm.")
    Sulfate=st.text_input("Sulfate",help="Amount of Sulfates dissolved in mg/L")
    Conductivity = st.text_input("Conductivity",help="Electrical conductivity of water in μS/cm")
    Organic_carbon = st.text_input("Organic_carbon",help="Amount of organic carbon in ppm")
    Trihalomethanes = st.text_input("Trihalomethanes",help="Amount of Trihalomethanes in μg/L")
    Turbidity = st.text_input("Turbidity",help="Measure of light emiting property of water in NTU")
    features=[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]
    scaler = pickle.load(open('scaler.sav', 'rb'))
    model = pickle.load(open('rf_model.sav', 'rb'))
    pred=st.button('PRDICT')
    if pred:
        result = model.predict(scaler.transform([features]))
        if result==1:
            st.write("# The water is Potable.")
        else:
            st.write('# The water is Not Potable.')
main()
