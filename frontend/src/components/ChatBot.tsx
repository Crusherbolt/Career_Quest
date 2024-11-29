import { useState } from "react"
import axios from "axios"
import ReactMarkdown from "react-markdown"

function ChatBot() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [generatingAnswer, setGeneratingAnswer] = useState(false);
  
    async function generateAnswer(e) {
      setGeneratingAnswer(true);
      e.preventDefault();
      setAnswer("Loading your answer... \n It might take up to 10 seconds");
      try {
        const response = await axios({
          url: `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyC1d3uER9eKSxpSmYM-eE0__yj1byMJrDA`,
          method: "post",
          data: {
            contents: [{ parts: [{ text: question }] }],
          },
        });
  
        setAnswer(
          response["data"]["candidates"][0]["content"]["parts"][0]["text"]
        );
      } catch (error) {
        console.log(error);
        setAnswer("Sorry - Something went wrong. Please try again!");
      }
  
      setGeneratingAnswer(false);
    }
  
    return (
      <div className="bg-gradient-to-r from-blue-50 to-blue-100 flex flex-col justify-center items-center p-8">
        <form
          onSubmit={generateAnswer}
          className="w-full text-center rounded-lg shadow-lg bg-white py-6 px-4 transition-all duration-500 transform hover:scale-105"
        >
          <a href="https://github.com/Vishesh-Pandey/chat-ai" target="_blank" rel="noopener noreferrer">
            <h1 className="text-4xl font-bold text-blue-500 mb-4 animate-bounce">Chat AI</h1>
          </a>
          <textarea
            required
            className="border border-gray-300 rounded w-full my-2 min-h-fit p-3 transition-all duration-300 focus:border-blue-400 focus:shadow-lg"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask anything"
          ></textarea>
          <button
            type="submit"
            className={`bg-blue-500 text-white p-3 rounded-md hover:bg-blue-600 transition-all duration-300 ${
              generatingAnswer ? "opacity-50 cursor-not-allowed" : ""
            }`}
            disabled={generatingAnswer}
          >
            Generate answer
          </button>
        </form>
        <div className="w-full text-center rounded-lg bg-white my-4 shadow-lg transition-all duration-500 transform hover:scale-105">
          <ReactMarkdown className="p-4">{answer}</ReactMarkdown>
        </div>
      </div>
    );
}

export default ChatBot