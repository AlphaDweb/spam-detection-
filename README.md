# Spam Detection and Email Alert System  

This repository implements a **Spam Detection and Email Alert System** using **Flask** and **Machine Learning**. The system is designed to identify spam messages and notify users via email alerts when spam is detected.  

---

## Features  

### 1. **Spam Detection**  
- Utilizes a pre-trained machine learning model to classify messages as **spam** or **not spam**.  
- Processes input text using a **vectorizer** for feature extraction before prediction.  

### 2. **Email Alert System**  
- Sends an **email notification** to the user if a spam message is detected.  
- Uses Python's built-in **smtplib** module for email handling.  

### 3. **User-Friendly Web Interface**  
- Built with **Flask** for a responsive and intuitive user interface.  
- Allows users to submit messages and email addresses directly via the web application.  

---

## Applications  

- **Email Security Systems**: Helps identify and report spam emails effectively.  
- **Content Moderation Tools**: Filters spam content in user-generated comments and forums.  
- **Business Communication Safety**: Ensures secure and spam-free communication channels.  

---

## Technical Stack  

- **Flask**: Web framework for backend development.  
- **Scikit-learn**: Used for training and saving the spam detection model.  
- **Joblib**: Loads the pre-trained model and vectorizer.  
- **SMTP**: Sends email alerts when spam is detected.  
- **HTML/CSS**: For frontend user interface design.  

---

## Installation  

### 1. Clone the Repository:  
```bash  
https://github.com/AlphaDweb/spam-detection-.git
cd spam-detection-email-alert  
```  

### 2. Install Dependencies:  
```bash  
pip install -r requirements.txt  
```  

**Note:** Create a `requirements.txt` file with the following content:  
```
Flask  
joblib  
scikit-learn  
```  

### 3. Add Pre-Trained Models:  
- Place your **spam_model.pkl** and **vectorizer.pkl** files in the project directory.  

### 4. Update Email Credentials:  
- Edit the `app.py` file to update the following variables with your Gmail credentials:  
```python  
sender_email = "your-email@gmail.com"  
sender_password = "your-app-password"  
```  

---

## Usage  

1. **Run the Flask Application**:  
```bash  
python app.py  
```  

2. **Access the Web Interface**:  
Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

3. **Submit Message for Spam Detection**:  
- Enter a message and email address in the input fields.  
- Click **Submit** to check if the message is spam.  

4. **Receive Email Alerts**:  
- If spam is detected, an email notification will be sent to the provided email address.  

---

## Project Structure  

```
spam-detection-email-alert/  
├── app.py                 # Backend Flask code  
├── templates/  
│   └── index.html         # Frontend HTML template  
├── spam_model.pkl         # Pre-trained machine learning model  
├── vectorizer.pkl         # Pre-trained vectorizer for input processing  
├── requirements.txt       # List of dependencies  
```  

---

## Contributing  

Contributions are welcome! If you’d like to improve this project, feel free to fork the repository and submit a pull request.  

---

## Acknowledgments  

- **Scikit-learn** for providing tools for machine learning model training and saving.  
- **Flask** for creating a lightweight and flexible web application.  
- **Python SMTP Library** for enabling email functionality.  
- Special thanks to the open-source community for helpful resources and tools.  

