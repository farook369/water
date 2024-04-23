import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

st.markdown(
    """
    <style>
    .heading-container {
        background-color: #f0f0f0; /* Background color */
        padding: 3px 10px; /* Padding */
        border-radius: 5px; /* Rounded corners */
        box-shadow: 2px 2px 5px grey; /* Box shadow */
    }
    .heading-text {
        font-size: 30px; /* Font size */
        color: #333333; /* Text color */
        font-weight: bold; /* Font weight */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="heading-container"><span class="heading-text">Water potability dataset</span></div>',
    unsafe_allow_html=True
)
st.write("                   ")

df=pd.read_csv("water_potability (1).csv")
st.write(df)

st.markdown(
    '<div class="heading-container"><span class="heading-text">Missing Values</span></div>',
    unsafe_allow_html=True
)
# st.title("MISSING VALUE")
st.write('          ')
st.write('          ')

st.write('Missing Value Counts')
st.write(df.isna().sum())
st.write("  ")

df['ph'] = df['ph'].fillna(df['ph'].mean())
df['Sulfate'] = df['Sulfate'].fillna(df['Sulfate'].mean())
df['Trihalomethanes'] = df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean())
fill = st.button("Fill Values")
if fill:
    st.write(df)
st.markdown(
    '<div class="heading-container"><span class="heading-text"> Datatypes of features</span></div>',
    unsafe_allow_html=True
)
st.write('               ')
st.write(df.isna().sum())


st.write("   ")
st.markdown(
    '<div class="heading-container"><span class="heading-text"> df.describe()</span></div>',
    unsafe_allow_html=True
)
# # potable_count = df["Potability"].value_counts()[0]
# # non_potable_count = df["Potability"].value_counts()[1]
# # x= [potable_count, non_potable_count]
# # nlables=["Potable", "Non-potable"]
# # plt.figure(figsize=(3, 3))
# # plt.pie(x,labels=nlables,autopct="%1.1f%%")
# # plt.title("Potability Distribution")
# # plt.legend()
# # st.pyplot(plt)
# sns.histplot(x='Organic_carbon',data=df,hue='Potability',kde=True,bins=20)
# plt.title('Organic_carbon vs Potability')
# st.pyplot(plt)

st.write(df.describe())
st.write("   ")
st.markdown(
    '<div class="heading-container"><span class="heading-text"> Correlation()</span></div>',
    unsafe_allow_html=True
)
st.write(df.corr())



