import React, { useState } from "react";
import ChatBot from "./ChatBot";

const ChatBotPopup = () => {
  const [isOpen, setIsOpen] = useState(false);

  const togglePopup = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      {/* Chatbot Trigger Button */}
      <button
        onClick={togglePopup}
        className="fixed h-24 w-24 rounded-full right-4 bottom-8 animate-bounce z-10"
      >
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6wAnOJDCUsDCy3EgZET2z1QMY6u8Z2afXBg&s" alt="" className='rounded-full' />
      </button>

      {/* Chatbot Popup */}
      {isOpen && (
        <div className="fixed right-4 bottom-8 bg-gray-800 bg-opacity-50 z-50 ">
            {/* Close Button */}
            <button
              onClick={togglePopup}
              className="absolute top-3 right-3 text-gray-500 hover:text-gray-700"
            >
              &times;
            </button>

            <ChatBot />
        </div>
      )}
    </div>
  );
};

export default ChatBotPopup;
