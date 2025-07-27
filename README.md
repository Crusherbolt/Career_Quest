# Career Quest 🚀

A comprehensive career guidance platform that combines AI-powered course recommendations, personalized learning paths, and interview preparation tools to help students and professionals navigate their career journey.

## ✨ Features

- **AI-Powered Course Recommendations**: Get personalized course suggestions based on your interests and career goals
- **Interactive Interview Practice**: Practice with AI-generated interview questions and receive detailed feedback
- **Course Discovery**: Explore and search through a vast database of online courses
- **Personalized Learning Roadmaps**: Get tailored learning paths for your chosen career
- **Speech Analysis**: Upload audio responses and get AI-powered feedback on your interview performance
- **Modern Web Interface**: Clean, responsive UI built with React and TypeScript

## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** for fast development and building
- **Tailwind CSS** for styling
- **React Router** for navigation
- **Axios** for API calls
- **Lucide React** for icons

### Backend
- **Flask** (Python web framework)
- **Scikit-learn** for machine learning models
- **Pandas** for data manipulation
- **Google Speech Recognition** for audio processing
- **Gemini AI API** for question generation and feedback
- **TF-IDF Vectorization** for course recommendations

### Machine Learning
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Naive Bayes Classifier**
- **Content-based Filtering** for course recommendations

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AryanMittal11/Career_Quest.git
   cd Career_Quest
   ```

2. **Backend Setup**
   ```bash
   cd backend
   
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Create environment file
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   
   # Install Node.js dependencies
   npm install
   ```

### Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

To get a Gemini API key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and paste it in your `.env` file

### Running the Application

1. **Start the Backend Server**
   ```bash
   cd backend
   python app.py
   ```
   The backend will run on `http://localhost:5000`

2. **Start the Frontend Development Server**
   ```bash
   cd frontend
   npm run dev
   ```
   The frontend will run on `http://localhost:5173`

## 📁 Project Structure

```
Career_Quest/
├── frontend/                 # React TypeScript frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Page components
│   │   └── ...
│   ├── package.json
│   └── ...
├── backend/                 # Flask Python backend
│   ├── templates/          # HTML templates
│   ├── static/            # CSS and JS files
│   ├── uploads/           # Audio file uploads
│   ├── app.py             # Main Flask application
│   ├── course.py          # Course-related utilities
│   ├── requirements.txt   # Python dependencies
│   └── *.csv             # Training data files
└── README.md
```

## 🔧 API Endpoints

### Course Recommendation
- `GET /` - Main course recommendation interface
- `POST /` - Submit interests and get course recommendations
- `GET /api/courses?degree=<degree_name>` - Get courses for specific degree

### Interview Practice
- `GET /generate-questions` - Interview question generation interface
- `POST /api/get-questions` - Generate AI-powered interview questions
- `POST /api/submit-audio` - Submit audio response for feedback

### Course Discovery
- `GET /coursera` - Course search interface
- `POST /predict` - Search and get course recommendations

## 📊 Machine Learning Models

The application uses multiple ML algorithms for course recommendation:

1. **Decision Tree Classifier** - Fast and interpretable
2. **Random Forest Classifier** - Improved accuracy through ensemble learning
3. **Naive Bayes Classifier** - Probabilistic approach
4. **Content-based Filtering** - TF-IDF vectorization for course similarity

## 🎯 Usage Examples

### Getting Course Recommendations
1. Select your interests from the provided list
2. Choose a machine learning algorithm
3. Get personalized course recommendations with accuracy metrics

### Interview Practice
1. Enter your target job domain
2. Get AI-generated interview questions
3. Record your audio response
4. Receive detailed feedback and improvement suggestions

### Course Discovery
1. Search for courses using keywords
2. Get similar course recommendations
3. Explore course details and links

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **AryanMittal11** - Project Lead & Developer

## 🙏 Acknowledgments

- Google Gemini AI for powering the interview questions and feedback
- Scikit-learn for machine learning capabilities
- The open-source community for amazing tools and libraries

## 📞 Support

If you have any questions or need help, please:
1. Check the [Issues](https://github.com/AryanMittal11/Career_Quest/issues) page or contact Collaborators vidhan365@gmail.com , nikhilshaw575@gmail.com
2. Create a new issue if your question isn't already answered
3. Contact the maintainers

---

Made with ❤️ for helping people find their perfect career path!
