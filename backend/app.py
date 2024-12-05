from flask import Flask, render_template, request, jsonify
import os
import requests
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ===================== GEMINI API CONFIGURATION =====================
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
API_KEY = os.getenv("GEMINI_API_KEY")  # Replace with your actual API key

# ===================== ROUTES FOR GEMINI QUESTION GENERATION =====================
@app.route('/generate-questions')
def gemini_index():
    return render_template('index2.html')  # Serve index2.html for Gemini functionality

def get_questions_from_gemini(domain):
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Generate 1 insightful interview question for a {domain} role."
                    }
                ]
            }
        ]
    }
    response = requests.post(f"{GEMINI_API_URL}?key={API_KEY}", json=payload)
    if response.status_code == 200:
        questions = response.json().get('candidates', [])
        return [question['content']['parts'][0]['text'] for question in questions[:5]]
    else:
        print("API Error Response:", response.json())
        return ["Error: Could not generate questions."]

@app.route('/api/get-questions', methods=['POST'])
def get_questions():
    data = request.get_json()
    domain = data.get('domain', '').strip()
    if not domain:
        return jsonify({"error": "Domain cannot be empty."}), 400
    questions = get_questions_from_gemini(domain)
    return jsonify({"questions": questions})

# ===================== AUDIO PROCESSING AND GEMINI FEEDBACK =====================
def analyze_audio_with_gemini(audio_file, question):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    audio_path = os.path.join(upload_dir, audio_file.filename)
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            transcribed_text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        transcribed_text = "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        transcribed_text = f"Speech recognition service error: {e}"
    except ValueError:
        transcribed_text = "Error: Audio file could not be processed."
    os.remove(audio_path)

    feedback_prompt = (
        f"Please evaluate the following response to the interview question, give short answer as you can in para "
        f"focusing on weaknesses, and suggestions for improvement.\n\n"
        f"Question: {question}\n\n"
        f"Transcribed Response: {transcribed_text}\n\n"
        "1. Weaknesses: Highlight areas for improvement.\n"
        "2. Suggestions: Provide actionable advice for improvement."
    )

    feedback_payload = {
        "contents": [
            {
                "parts": [{"text": feedback_prompt}]
            }
        ]
    }

    response = requests.post(f"{GEMINI_API_URL}?key={API_KEY}", json=feedback_payload)
    if response.status_code == 200:
        feedback = response.json().get('candidates', [])[0].get('content', {}).get('parts', [{}])[0].get('text', "No feedback available.")
        return feedback
    else:
        print("API Error Response:", response.json())
        return f"Error: {response.json().get('message', 'Failed to process audio.')}"

@app.route('/api/submit-audio', methods=['POST'])
def submit_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
    audio_file = request.files['audio']
    question = request.form.get('question', '')
    feedback = analyze_audio_with_gemini(audio_file, question)
    return jsonify({"feedback": feedback})

# ===================== COURSE SUGGESTION SYSTEM =====================
l1 = ['Drawing', 'Dancing', 'Singing', 'Sports', 'Video Game', 'Acting', 'Travelling',
      'Gardening', 'Animals', 'Photography', 'Teaching', 'Exercise', 'Coding',
      'Electricity Components', 'Mechanic Parts', 'Computer Parts', 'Researching',
      'Architecture', 'Historic Collection', 'Botany', 'Zoology', 'Physics',
      'Accounting', 'Economics', 'Sociology', 'Geography', 'Psycology', 'History',
      'Science', 'Bussiness Education', 'Chemistry', 'Mathematics', 'Biology',
      'Makeup', 'Designing', 'Content writing', 'Crafting', 'Literature', 'Reading',
      'Cartooning', 'Debating', 'Asrtology', 'Hindi', 'French', 'English',
      'Other Language', 'Solving Puzzles', 'Gymnastics', 'Yoga', 'Engeeniering',
      'Doctor', 'Pharmisist', 'Cycling', 'Knitting', 'Director', 'Journalism',
      'Bussiness', 'Listening Music']

Course = ['BBA- Bachelor of Business Administration',
          'BEM- Bachelor of Event Management',
          'Integrated Law Course- BA + LL.B',
          'BJMC- Bachelor of Journalism and Mass Communication',
          'BFD- Bachelor of Fashion Designing',
          'BBS- Bachelor of Business Studies',
          'BTTM- Bachelor of Travel and Tourism Management',
          'BVA- Bachelor of Visual Arts',
          'BA in History', 'B.Arch- Bachelor of Architecture',
          'BCA- Bachelor of Computer Applications',
          'B.Sc.- Information Technology',
          'B.Sc- Nursing', 'BPharma- Bachelor of Pharmacy',
          'BDS- Bachelor of Dental Surgery',
          'Animation, Graphics and Multimedia',
          'B.Sc- Applied Geology', 'B.Sc.- Physics',
          'B.Sc. Chemistry', 'B.Sc. Mathematics',
          'B.Tech.-Civil Engineering',
          'B.Tech.-Computer Science and Engineering',
          'B.Tech.-Electrical and Electronics Engineering',
          'B.Tech.-Electronics and Communication Engineering',
          'B.Tech.-Mechanical Engineering',
          'B.Com- Bachelor of Commerce', 'BA in Economics',
          'CA- Chartered Accountancy', 'CS- Company Secretary',
          'Diploma in Dramatic Arts', 'MBBS',
          'Civil Services', 'BA in English',
          'BA in Hindi', 'B.Ed.']

# Load and prepare the data
df = pd.read_csv("stud_training.csv")
df.replace({'Courses': {name: idx for idx, name in enumerate(Course)}}, inplace=True)

X = df[l1]
y = df["Courses"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_evaluate_model(algorithm):
    if algorithm == "DecisionTree":
        clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
    elif algorithm == "RandomForest":
        clf = RandomForestClassifier().fit(X_train, y_train)
    elif algorithm == "NaiveBayes":
        clf = GaussianNB().fit(X_train, y_train)
    else:
        clf = None

    # Calculate accuracy if classifier is valid
    if clf:
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
    else:
        accuracy = None
    
    return clf, accuracy

def predict_course(model, interests):
    l2 = [0] * len(l1)
    for interest in interests:
        if interest in l1:
            l2[l1.index(interest)] = 1
    input_test = [l2]
    predicted = model.predict(input_test)[0]
    return Course[predicted] if predicted < len(Course) else "Not Found"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    accuracy = None
    if request.method == "POST":
        interests = [request.form.get(f"interest{i}") for i in range(1, 6)]
        algorithm = request.form.get("algorithm")

        clf, accuracy = train_and_evaluate_model(algorithm)

        if clf:
            result = predict_course(clf, interests)

    return render_template("index.html", interests=l1, result=result, accuracy=accuracy)

# ===================== MAIN ENTRY POINT =====================
if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
