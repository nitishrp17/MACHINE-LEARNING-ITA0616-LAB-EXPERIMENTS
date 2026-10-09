import pandas as pd

# Training dataset
data = pd.DataFrame({
    'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny'],
    'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm'],
    'Humidity': ['Normal', 'High', 'High', 'High'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool'],
    'Forecast': ['Same', 'Same', 'Change', 'Change'],
    'EnjoySport': ['Yes', 'Yes', 'No', 'Yes']
})

print("Training Data:")
print(data)

# Initialize the most specific hypothesis
hypothesis = ['0'] * (len(data.columns) - 1)

# FIND-S algorithm
for index, row in data.iterrows():
    if row['EnjoySport'] == 'Yes':
        for i, attribute in enumerate(data.columns[:-1]):
            if hypothesis[i] == '0':
                hypothesis[i] = row[attribute]
            elif hypothesis[i] != row[attribute]:
                hypothesis[i] = '?'

    print(f"Example {index + 1}: {hypothesis}")

# Final hypothesis
print("\nFinal Most Specific Hypothesis:")
print(hypothesis)
