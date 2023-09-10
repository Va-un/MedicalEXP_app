import pickle
import streamlit as st
import pandas as pd
import time
st.set_page_config(
    page_title="Modeling",
    page_icon="🔧",
)

#---------------------------------------------------------------------------------------------------------------------

model = pickle.load(open("Model/finalized_model.sav", 'rb'))

NUM = pickle.load(open("Model/Numeric_model.sav", 'rb'))

sub = '''
Introducing our cutting-edge predictive model! 💫 Get ready for precise estimates of healthcare expenses like never before. 🌟 This model, fueled by data analytics and machine learning magic, delivers spot-on cost predictions for medical treatments. ✨ It's a game-changer, bringing transparency and efficiency to healthcare, benefiting everyone from patients to providers, insurers, and policymakers. 🚀 Say hello to informed healthcare decisions and optimized resource allocation! 💡'''
A_image = 'Img/Age.png'
G_image = 'Img/Gender.png'
B_image = 'Img/BMI.png'
C_image = 'Img/child.png'
S_image = 'Img/Smoker.png'
R_image = 'Img/Region.png'

region = {'southwest': 3, 'southeast': 2, 'northwest': 1, 'northeast': 0}
smoker = {'Yes': 1, 'No': 0}
Gen = {'Male': 1, 'Female': 0}

def predection(Value):
    y_pred1 = model.predict([Value])
    Predicted_error = y_pred1.tolist()[0]
    return int(Predicted_error)




#---------------------------------------------------------------------------------------------------------------------

st.header("Lets Check The Price :money_with_wings:")
st.write(sub)

st.image(A_image)
st.subheader('What is your age:')
Age = st.slider("", min_value=1 , max_value=90)

st.image(G_image)
st.subheader('What is your gender?')
Gender = st.selectbox("", ["Male", "Female"])

st.image(B_image)
st.subheader("Enter what is your BMI:")
BMI = int(st.number_input(""))

st.image(C_image)
st.subheader("How many children do you have?")
Child = st.radio("", [0, 1, 2, 3, 4, 5])

st.image(S_image)
st.subheader("Are you a Smoker?")
Smoker = st.selectbox("", ["Yes", "No"])

st.image(R_image)
st.subheader("From which region are you?")
Region = st.selectbox("",['southwest', 'southeast', 'northwest', 'northeast'])


Predict = st.button("Predict")

bmi = NUM.transform([[BMI]]).tolist()
bmi = bmi.reshape(1, )
Value = [Gen[Gender], smoker[Smoker], region[Region], Age, bmi, Child ]

if (Predict):
    with st.spinner('Estimating The Cost'):
        time.sleep(0)
    #Cost = f'The Estimated money required is  ${predection(Value)}'
    st.subheader(Value)


