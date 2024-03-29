import pandas as pd

# Sample dataset
data = {
    'Disease': ['Common Cold', 'Influenza', 'Headache', 'Sore Throat', 'Upset Stomach',
                'Sunburn', 'Insomnia', 'Allergies', 'Muscle Strain', 'Acne'],
    'Symptoms': [
        'Runny nose, sore throat, cough, congestion',
        'Fever, chills, body aches, fatigue',
        'Head pain, sensitivity to light or sound',
        'Throat pain, difficulty swallowing',
        'Nausea, vomiting, diarrhea, stomach pain',
        'Redness, pain, swelling, blisters (severe)',
        'Difficulty falling or staying asleep',
        'Sneezing, runny or stuffy nose, itchy eyes',
        'Muscle pain, swelling, limited movement',
        'Pimples, blackheads, whiteheads'
    ],
    'Prevalence Male (%)': [40, 45, 40, 30, 50, 40, 40, 30, 60, 35],
    'Prevalence Female (%)': [60, 55, 60, 70, 50, 60, 60, 70, 40, 65],
    'Treatments': [
        'Rest, fluids, over-the-counter cold medication',
        'Rest, fluids, antiviral medications (if severe), over-the-counter pain and fever relievers',
        'Pain relievers, relaxation techniques',
        'Gargling with warm salt water, throat lozenges, pain relievers',
        'BRAT diet (bananas, rice, applesauce, toast), fluids, over-the-counter antidiarrheal meds',
        'Cool compresses, moisturizers, aloe vera gel',
        'Establishing a bedtime routine, relaxation techniques, cognitive-behavioral therapy',
        'Antihistamines, nasal corticosteroids, avoiding allergens',
        'Rest, ice packs, compression, elevation (RICE), pain relievers',
        'Gentle cleansers, topical treatments (benzoyl peroxide, salicylic acid), avoiding triggers'
    ]
}

# Convert the dictionary to DataFrame
df = pd.DataFrame(data)

# Check if the CSV file exists
try:
    existing_data = pd.read_csv('disease_data.csv')
    existing_diseases = existing_data['Disease'].tolist()
except FileNotFoundError:
    existing_diseases = []

# Filter out diseases that are already present in the CSV file
new_diseases = df[~df['Disease'].isin(existing_diseases)]

# Append new diseases to the existing CSV file
if not new_diseases.empty:
    new_diseases.to_csv('disease_data.csv', mode='a', header=not existing_diseases, index=False)
    print("New diseases added to the CSV file.")
else:
    print("No new diseases to add.")

