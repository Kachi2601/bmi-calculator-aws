from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # Route for handling the BMI calculation form submission and displaying results
def index():
    if request.method == "POST":
        try:
            age = int(request.form.get("age"))
            height = float(request.form.get("height"))  # in cm
            weight = float(request.form.get("weight"))  # in kg
            gender = request.form.get("gender")
            race = request.form.get("race")

            height_m = height / 100
            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal weight"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"

            message = (
                "Note: BMI is a general indicator and doesn't fully reflect individual health. "
                "It does not account for muscle mass, bone density, or body composition."
            )

            return render_template("result.html", bmi=bmi, status=status, message=message)

        except (ValueError, TypeError):
            return "Invalid input. Please enter valid numbers."

    return render_template("bmi_form.html")  # Replace with your actual HTML filename