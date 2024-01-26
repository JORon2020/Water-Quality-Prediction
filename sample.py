import numpy as np
import pickle
import streamlit as st
import os


# Function for Prediction
def water_quality(predictive_input, model):
    predictive_input_array = np.asarray(predictive_input).reshape(1, -1)
    prediction = model.predict(predictive_input_array)
    print('Prediction: ', prediction)
    
    # Adding a bias of 1 based on specified conditions
    if (float(predictive_input[0]) > 8.5 or float(predictive_input[0]) < 6.5 or
        float(predictive_input[1]) > 200 or float(predictive_input[2]) > 500 or
        float(predictive_input[3]) > 4 or float(predictive_input[4]) > 200 or
        float(predictive_input[5]) > 400 or float(predictive_input[6]) > 2 or
        float(predictive_input[7]) > 80 or float(predictive_input[8]) > 5):
        prediction += 1
    #return prediction
        
    if prediction[0] <= 0.8:
        return 'Congratulations, the Water Quality is Good.'
    else:
        return 'Water Quality is Bad for Drinking.'

# Main Function
def main():
    # Title
    st.title('Drinking Water Quality Checker')
    # Set page configuration with blue background
    page_bg = """
    <style>
    body {
        background-color: #3498db;  /* Blue color code */
    }
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)
    
    # Load the Saved Model
    model_path = r'C:\Users\JO Ron\water\model.pkl'
    with open(model_path, 'rb') as file:
        rf_regressor = pickle.load(file)

    # Input Features
    ph = st.text_input('Enter pH Level')
    Hardness = st.text_input('Enter Hardness')
    Solids = st.text_input('Enter Solids(TDS)')
    Chloramines = st.text_input('Enter Chloramines') 
    Sulfate = st.text_input('Enter Sulfate')
    Conductivity = st.text_input('Enter Conductivity')
    Organic_carbon = st.text_input('Enter Organic Carbon')
    Trihalomethanes = st.text_input('Enter Trihalomethanes')
    Turbidity = st.text_input('Enter Turbidity')

# Validation for numeric inputs
    try:
        ph = float(ph)
        Hardness = float(Hardness)
        Solids = float(Solids)
        Chloramines = float(Chloramines)
        Sulfate = float(Sulfate)
        Conductivity = float(Conductivity)
        Organic_carbon = float(Organic_carbon)
        Trihalomethanes = float(Trihalomethanes)
        Turbidity = float(Turbidity)

    # Prediction
        prediction = ''

        # Prediction Button
        if st.button('Check Quality Result'):
            prediction = water_quality([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity], rf_regressor)

        st.success(prediction)

    except ValueError:
        st.warning('Please enter valid numeric values for all input features.')

if __name__ == '__main__':
    main()