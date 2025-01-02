from flask import Flask, render_template, request, jsonify
import joblib
import smtplib

app = Flask(__name__)

# Load the trained spam detection model
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to send email alerts
def send_email_alert(email, message):
    try:
        sender_email = "sender email"
        sender_password = "app password "
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(
                sender_email,
                email,
                f"Subject: Spam Alert\n\n{message}",
            )
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect_spam():
    user_input = request.form["message"]
    user_email = request.form["email"]
    
    # Preprocess and predict
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]

    # Check if spam and send email
    if prediction == 1:
        send_email_alert(user_email, f"Spam detected: {user_input}")
        return jsonify({"result": "Spam detected. Email alert sent!"})
    else:
        return jsonify({"result": "Not spam."})

if __name__ == "__main__":
    app.run(debug=True)
