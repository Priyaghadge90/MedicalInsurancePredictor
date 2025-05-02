# MedicalInsurancePredictor

🏥 Medical Insurance Charges Predictor
This is a Flask web application that predicts medical insurance charges based on user input like age, gender, BMI, number of children, smoking habits, and region. It uses a pre-trained machine learning model.

📁 Project Structure
bash
Copy
Edit
MedicalInsurancePredictor/
│
├── project_app/
│   └── utils.py                # Utility class to load model and predict charges
│
├── templates/
│   └── index.html              # Frontend UI for user input
│
├── Static/
│   └── image/                  # Optional images
│
├── medical_insurance_model_venv/  # Virtual environment (not pushed to GitHub)
├── main.py                     # Flask app with API routes
├── project_config.py          # Configuration for port and settings
├── Nootebooks/
│   └── medical.ipynb           # Jupyter notebook used for training and EDA
├── .gitignore                 # To ignore virtualenv, pycache, etc.
└── README.md                  # Project documentation
🚀 How to Run the Project
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Priyaghadge90/MedicalInsurancePredictor.git
cd MedicalInsurancePredictor
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On Mac/Linux
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
(You can generate requirements.txt using pip freeze > requirements.txt)

4. Run the Flask App
bash
Copy
Edit
python main.py
Visit the app in your browser at:
🔗 http://127.0.0.1:5000/

🧠 Features
Predict medical charges using a trained ML model.

Dropdowns for gender, smoker, and region populated dynamically.

Separate API endpoints:

/gender_option

/smoker_option

/region_option

/prediction

🛠 Technologies Used
Python

Flask

scikit-learn

HTML, CSS (for frontend)

JSON (for mappings)

📊 Model Details
The ML model was trained using features:

Age

Gender

BMI

Children

Smoker status

Region

📎 Sample API Usage
To get gender options: GET /gender_option

To submit prediction: POST /prediction with form data

🙋‍♀️ Author
👩‍💻 Priya Ghadge