from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
model = load_model('dp_insurance_charges')
# input_dict = {'age' : 20, 'sex' : 'male', 'bmi' : 20, 'children' : 2, 'smoker' : 'yes', 'region' : 'southwest'}
# input_df = pd.DataFrame([input_dict])
# predictions_df = predict_model(estimator=model, data=input_df)
# predictions = predictions_df.iloc[0]['prediction_label']
# st.markdown(predictions)
def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df.iloc[0]['prediction_label']
    return predictions

age = st.number_input('Age', min_value=1, max_value=100, value=25)
sex = st.selectbox('Sex', ['male', 'female'])
bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])
if st.checkbox('Smoker'):
    smoker = 'yes'
else:
    smoker = 'no'
region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

output=""

input_dict = {'age' : age, 'sex' : sex, 'bmi' : bmi, 'children' : children, 'smoker' : smoker, 'region' : region}
input_df = pd.DataFrame([input_dict])

if st.button("Predict"):
    output = predict(model=model, input_df=input_df)
    output = '$' + str(output)
st.success('The output is {}'.format(output))

