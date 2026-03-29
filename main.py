# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

# Input features (X) and output (y)
X = data[["StudyHours", "Attendance", "PreviousMarks"]]
y = data["FinalMarks"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Take user input
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
previous_marks = float(input("Enter previous marks: "))

# Make prediction
import pandas as pd

input_data = pd.DataFrame([[study_hours, attendance, previous_marks]],
                          columns=["StudyHours", "Attendance", "PreviousMarks"])

prediction = model.predict(input_data)

print("\nPredicted Final Marks:", round(prediction[0], 2))

# Generate suggestions based on input values

print("\nSuggestions:")

if study_hours < 4:
    print("- Try to increase your study hours by 1-2 hours daily.")

if attendance < 75:
    print("- Your attendance is low. Try to attend more classes.")

if previous_marks < 60:
    print("- Focus on basic concepts and revise regularly.")

if study_hours >= 6 and attendance >= 80:
    print("- Great job! Keep maintaining your performance.")
