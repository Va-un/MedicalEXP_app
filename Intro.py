
import pickle
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Intro",
    page_icon="ℹ️",
)





#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
#streamlit run ℹ️Intro.py


#------------------------------------------------------------------------------------------------------------------------
#Varible Selector

df = pd.read_csv("medical_cost.csv", index_col = "Id")
I_image = "Img/Intro.png"
INFO1 = '''
### :ambulance: Introduction 

The rising cost of healthcare is a major challenge facing many countries around the world. In the United States, healthcare costs are particularly high, and they continue to grow at an alarming rate. This is putting a strain on both individuals and businesses, and it is also a major factor in the national debt.

One way to address the rising cost of healthcare is to improve our understanding of the factors that influence medical charges. This is where the Medical Cost Dataset comes in. This dataset provides valuable insights into the factors that can affect a patient's medical costs, such as age, sex, BMI, smoking status, and geographic region.
'''

INFO2 = '''
### :notebook: Dataset Description 

The Medical Cost Dataset includes the following information for each patient:

* ID: A unique identifier assigned to each individual record.
* Age: The age of the patient.
* Sex: The gender of the patient.
* BMI: The Body Mass Index (BMI) of the patient.
* Children: The number of children or dependents covered under the medical insurance.
* Smoker: A binary indicator of whether the patient is a smoker or not.
* Region: The geographic region of the patient.
* Charges: The medical charges incurred by the patient.

The dataset includes over 7000 observations, which makes it a valuable resource for researchers. The data is also well-curated and contains complete information on all of the variables. This makes it easy to use and analyze the data.
'''

INFO3 = '''
###  :email: Use Cases

The Medical Cost Dataset can be used for a variety of purposes, including:

* Exploring the relationships between different factors and medical charges.
* Predicting future healthcare costs.
* Developing data-driven models to enhance the efficiency of healthcare resource allocation.
* Refining pricing strategies for insurers.
* Making informed decisions to improve the overall healthcare system.

For example, researchers could use the dataset to investigate whether there is a correlation between age and medical charges, or whether the number of children has an impact on healthcare costs. They could also use the data to develop models that can be used to predict future healthcare costs for individuals or groups of people.

###  :white_check_mark: Conclusion 

The Medical Cost Dataset is a valuable resource for healthcare research. It can be used to gain insights into the factors influencing medical charges, predict future healthcare costs, and make informed decisions about healthcare policy. I encourage researchers, analysts, and healthcare professionals to explore this dataset and use it to advance their work.

##### Site created by **Varun Chindage**
'''



#-----------------------------------------------------------------------------------------------------------------
# App


st.title("Medical Cost Dataset :male-doctor: : A Valuable Resource for Healthcare Research ")
st.image(I_image)
st.markdown(INFO1)
st.markdown(INFO2)
st.dataframe(df.head(5))
st.markdown(INFO3)

