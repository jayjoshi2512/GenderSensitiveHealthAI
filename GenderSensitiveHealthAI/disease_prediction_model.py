import webbrowser
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import PySimpleGUI as sg

# Function to calculate accuracy manually
def calculate_accuracy(y_true, y_pred):
    correct_predictions = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    total_predictions = len(y_true)
    return (correct_predictions / total_predictions) * 100

# Load the dataset for disease symptoms
df_symptoms = pd.read_csv('disease_data_engineered.csv')

# Load the dataset for disease remedies
df_remedies = pd.read_csv('disease_data_engineered.csv')

# Define the layout for the GUI
layout = [
    [sg.Text("Enter 'disease' to predict disease based on symptoms or 'remedy' for the remedies:")],
    [sg.Input(key='-INPUT-'), sg.Button('Submit')],
    [sg.Output(size=(60, 10))],
    [sg.Text("Click here to search on YouTube:"), sg.Button("Search on YouTube")]
]

# Create the GUI window
window = sg.Window('Disease Prediction and Remedy Recommendation').Layout(layout)

# Event loop to process events and interact with the GUI
while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
   
    elif values['-INPUT-'].lower() == 'disease':
        # Feature selection for disease prediction
        X = df_symptoms['Symptoms']
        y = df_symptoms['Disease']
        
        # Vectorize symptoms using TF-IDF
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(X)
        
        # Initialize and train the decision tree classifier
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X, y)
        
        # Get user input symptoms
        user_symptoms = sg.PopupGetText("Enter your symptoms (separated by commas):")
        
        # Vectorize user input symptoms
        user_symptoms_vectorized = vectorizer.transform([user_symptoms])
        
        # Predict disease based on user symptoms
        user_input_pred = clf.predict(user_symptoms_vectorized)
        
        print("Predicted disease based on provided symptoms:", user_input_pred[0])
        # Update the text in the input field to the predicted disease
        window['-INPUT-'].update(user_input_pred[0])

    elif event == "Search on YouTube":
        disease_name = values['-INPUT-']
        if disease_name:
            query = "+".join(disease_name.split())
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        else:
            print("Please predict a disease before searching on YouTube.")
    
    elif values['-INPUT-'].lower() == 'remedy':
        # Get user input disease name
        disease_name = sg.PopupGetText("Enter the name of the disease:")
        
        # Filter remedy data for the given disease
        disease_remedies = df_remedies[df_remedies['Disease'] == disease_name]['Treatments'].values
        
        if len(disease_remedies) > 0:
            print("Recommended remedies for", disease_name, ":")
            for remedy in disease_remedies:
                print("-", remedy)
        else:
            print("No remedies found for", disease_name)
    
    else:
        print("Invalid input. Please enter 'disease' or 'remedy'.")

# Close the GUI window
window.close()
