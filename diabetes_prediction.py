# # -*- coding: utf-8 -*-
# """
# Created on Thu Dec 15 14:49:07 2022

# @author: dell
# """
# import numpy as np
# import pickle
# import streamlit as st


# loaded_model = pickle.load(open(r'C:\Users\pc\OneDrive\Desktop\diabetes_prediction\trained_model.sav', 'rb'))


# def predict(input_data):
    
    
#     #changing the input data to numpy array
#     input_data_as_numpy_array=np.asarray(input_data)
    
#     #reshape the array as we are predicting for one instance
#     input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
#     prediction=loaded_model.predict(input_data_reshaped)
#     print(prediction)
#     if prediction[0]==0:
#       return "the user is not diabetic"
#     else:
#       return "the user is diabetic"
  
# def main():
    
#     #giving a title
#     st.title("Diabetes Prediction Web App")
    
#     #getting the input data from the user
    
#     Pregnancies = st.text_input("enter no.of pregnancies")
#     Glucose = st.text_input("enter glucose level")
#     BloodPressure= st.text_input("enter blood pressure value")
#     skinthickness= st.text_input("enter skinthickness") 
#     Insulin = st.text_input("enter insulin level")
#     BMI = st.text_input("enter BMI")
#     DiabetesPedigreeFucntion = st.text_input("enter DPF")
#     Age= st.text_input("enter your age")
    
    
#     #code for prediction
#     diagonosis=''
#     if st.button("Diabetes Test Result"):
#         diagonosis=predict([Pregnancies,Glucose,BloodPressure,skinthickness,Insulin,BMI,DiabetesPedigreeFucntion,Age
#         ])
#     st.success(diagonosis)
    
# if __name__=='__main__':
#     main()

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:49:07 2022

@author: dell
"""
import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open(r'C:\Users\pc\OneDrive\Desktop\diabetes_prediction\trained_model.sav', 'rb'))

# Function to predict diabetes
def predict(input_data):
    # Convert the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The user is not diabetic"
    else:
        return "The user is diabetic"

# Main function for the Streamlit app
def main():
    # Title of the app
    st.title("Diabetes Prediction Web App")

    # Getting user inputs with default values to prevent empty fields
    Pregnancies = st.text_input("Enter number of pregnancies", value="0")
    Glucose = st.text_input("Enter glucose level", value="0")
    BloodPressure = st.text_input("Enter blood pressure value", value="0")
    skinthickness = st.text_input("Enter skin thickness", value="0")
    Insulin = st.text_input("Enter insulin level", value="0")
    BMI = st.text_input("Enter BMI", value="0")
    DiabetesPedigreeFucntion = st.text_input("Enter Diabetes Pedigree Function (DPF)", value="0")
    Age = st.text_input("Enter your age", value="0")

    # Variable to store diagnosis result
    diagnosis = ""

    # Predict diabetes when the button is clicked
    if st.button("Diabetes Test Result"):
        try:
            # Convert inputs to floats
            inputs = list(map(float, [
                Pregnancies, Glucose, BloodPressure, skinthickness, Insulin, BMI, DiabetesPedigreeFucntion, Age
            ]))
            diagnosis = predict(inputs)
        except ValueError:
            st.error("Please enter valid numbers for all fields.")

    # Display the prediction result
    st.success(diagnosis)

# Run the main function
if __name__ == '__main__':
    main()
