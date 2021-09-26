import streamlit as st

from PIL import Image 
# Image.open('MMU_logo.png').convert('RGB').save('MMU_logo.png')
im = Image.open(".\images\MMU_logo.png")
st.image(im, width=500)

st.title("TDS 3301 - Data Mining")
st.header("Assignment in Healthcare Domain")
st.subheader("Group Members:")
st.markdown("- Nicholas Chee Jian Shen 1171103441")
st.markdown("- Chan Jun Ting 1171103572")
st.markdown("- Tee Wai Bing 1171103537")

st.markdown("""---""")

st.subheader("Question 1")
st.markdown("** Discuss the exploratory data analysis steps you have conducted including detection of outliers and missing values? **")
q1_1 = Image.open(".\images\q1-1.png")
q1_2 = Image.open(".\images\q1-2.png")
q1_3 = Image.open(".\images\q1-3.png")
q1_4 = Image.open(".\images\q1-4.png")
q1_5 = Image.open(".\images\q1-5.png")
st.image(q1_1, caption="Boxplot of Each State from Septemeber 2020 to November 2020")
st.image(q1_2, caption="Boxplot of Each State from December 2020 to February 2021")
st.image(q1_3, caption="Boxplot of Each State from March 2021 to May 2021")
st.image(q1_4, caption="Boxplot of Each State from June 2021 to August 2021")
st.image(q1_5, caption="Total Number of Cases of Each State")

st.markdown("""---""")

st.subheader("Question 2")
st.markdown("** What are the states that exhibit strong correlation with (i) Pahang, and (ii) Johor? **")
q2_1 = Image.open(".\images\q2-1.png")
st.image(q2_1, caption="TODO")

st.markdown("""---""")

st.subheader("Question 3")
st.markdown("** What are the strong features/indicators to daily cases for (i) Pahang, (ii) Kedah, (iii) Johor, and (iv) Selangor? **")
q3_1 = Image.open(".\images\q3-1.png")
q3_2 = Image.open(".\images\q3-2.png")
q3_3 = Image.open(".\images\q3-3.png")
q3_4 = Image.open(".\images\q3-4.png")
q3_5 = Image.open(".\images\q3-5.png")
q3_6 = Image.open(".\images\q3-6.png")
q3_7 = Image.open(".\images\q3-7.png")
q3_8 = Image.open(".\images\q3-8.png")
st.image(q3_1, caption="TODO")
st.image(q3_2, caption="TODO")
st.image(q3_3, caption="TODO")
st.image(q3_4, caption="TODO")
st.image(q3_5, caption="TODO")
st.image(q3_6, caption="TODO")
st.image(q3_7, caption="TODO")
st.image(q3_8, caption="TODO")

st.markdown("""---""")

st.subheader("Question 4")
st.markdown("** Comparing regression and classification models, what model performs well in predicting the daily cases for (i) Pahang, (ii) Kedah, (iii) Johor, and (iv) Selangor? **")
q4_1 = Image.open(".\images\q4-1.png")
q4_2 = Image.open(".\images\q4-2.png")
q4_3 = Image.open(".\images\q4-3.png")
q4_4 = Image.open(".\images\q4-4.png")
st.image(q4_1, caption="TODO")
st.image(q4_2, caption="TODO")
st.image(q4_3, caption="TODO")
st.image(q4_4, caption="TODO")




