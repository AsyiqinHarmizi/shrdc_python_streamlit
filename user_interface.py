import streamlit as st

st.write("Hello friends!")
st.header("Hello everyone!")
st.subheader("Hello niece and nephews!")
st.caption("Hello to you!")

st.write("Chocolate and blueberries are my favourite!")
st.write("My birth month is September.")
st.write("\n")

st.subheader("Text Formatting")
#Text formatting
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(''' :red[Streamlit] :orange[is] :green[fun] ''')
st.markdown("Here's a bouquet &mdash;\ :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

#Bootstrap text
st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")
st.write("\n")

#Advanced Font
st.subheader("Advanced Font")
new_title = '''<p style="font-family:sans-serif;
                 color:Green;
                 font-size: 24px;
                 ">This is advanced font manipulation!</p>'''
st.markdown(new_title, unsafe_allow_html=True)
st.write("\n")

#Selection Box
st.subheader("Selection Box")
st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])
st.write("\n")

#Buttons
st.subheader("Buttons")
st.button("Click Here to Proceed")
st.slider("Select the length of stay", 1,10, value=3)
st.write("\n")

#Input Box
st.subheader("Input Box")
number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number)
st.write("\n")

#Insert graphics
st.subheader("Graphics")
from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)
st.write("\n")

#Dataframe
import pandas as pd
st.subheader("Dataframe")
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)
st.write("\n")

# i) Bar chart
st.write("Bar chart")
st.bar_chart(df, x="Location", y="Income")

# i) Line chart
st.write("Line chart")
st.line_chart(df, x="Household", y="Income")

# i) Scatter chart
st.write("Scatter chart")
st.scatter_chart(df, x="Household", y="Income")

#Creating multi-tab page
st.subheader("Multi-tab pages")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
st.write("\n")

#Create multi-columns
st.subheader("Multi-columns")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")



