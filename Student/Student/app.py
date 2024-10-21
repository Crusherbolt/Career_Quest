from flask import Flask, render_template, request
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Data preparation
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

if __name__ == "__main__":
    app.run(debug=True)
