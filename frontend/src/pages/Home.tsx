import React from 'react';
import { Search, BarChart2, DollarSign, MapPin } from 'lucide-react';
import ChatBot from '../components/ChatBot';
import { Link, Route, Routes } from 'react-router-dom';
import ChatBotPopup from '../components/ChatBotPopUp';

const Home: React.FC = () => {
  const navigateToChatBot = () => {
    <ChatBot />;
  };

  const navigateToCounselling = () => {
    window.location.href = 'http://127.0.0.1:5000/';
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <ChatBotPopup />

      <section className="mb-12">
        <div className='flex justify-around items-center bg-white flex-wrap'>
          <div className='flex flex-col items-start p-4 w-2/5'>
            <h1 className="text-4xl font-bold mb-4">Welcome to Career Quest</h1>
            <p className="text-2xl text-gray-600">Your ultimate career guidance platform</p>
            <p className='test-2xl gap-4'>Empowering individuals to navigate their career journey with confidence, unlock endless opportunities, and achieve their professional dreams through personalized guidance and resources.</p>
            <button 
            className='bg-blue-500 p-4 rounded-lg text-white border-black mt-4 text-2xl'
            onClick={navigateToCounselling}>Get Your Free Guidance</button>
          </div>
          <img src="https://img.freepik.com/premium-vector/man-learning-put-together-puzzle-trending-concept-flat-illustration_720185-1423.jpg?semt=ais_hybrid" alt="" />
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-6">Our Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 ">
          <button
          onClick={navigateToCounselling}>
          <FeatureCard
            icon={<BarChart2 className="w-12 h-12 text-green-500" />}
            title="Career Counselling for Students"
            description="Get data-driven insights on industry trends and right path based on your interest"
          />
          </button>
          
          <FeatureCard
            icon={<Search className="w-12 h-12 text-blue-500" />}
            title="Test Your Interview Skills"
            description="Discover your communication skills with our AI-powered assessment"
          />
          <FeatureCard
            icon={<Search className="w-12 h-12 text-blue-500" />}
            title="Personalized Career Quiz"
            description="Discover your ideal career path with our AI-powered assessment"
          />
          <FeatureCard
            icon={<DollarSign className="w-12 h-12 text-yellow-500" />}
            title="Salary Predictions"
            description="Accurate salary forecasts based on your skills and experience"
          />
          <FeatureCard
            icon={<MapPin className="w-12 h-12 text-red-500" />}
            title="Career Roadmaps"
            description="Tailored guidance to achieve your professional goals"
          />
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-6">How It Works</h2>
        <div className="bg-white rounded-lg shadow-md p-6">
          <ol className="list-decimal list-inside space-y-4">
            <li>Take Career Counselling to choose right path</li>
            <li>Test your interview skills and recieve feedback</li>
            <li>Take our comprehensive career assessment quiz</li>
            <li>Receive personalized career recommendations</li>
            <li>Explore detailed job market insights and salary predictions</li>
            <li>Get a customized roadmap to achieve your career goals</li>
            <li>Access resources and courses to enhance your skills</li>
          </ol>
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-6">Take Help From Our Mentors</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 ">
          <Mentors
            name="Aryan"
            contact="+919350280890"
          />
          <Mentors
            name="Vidhan Gupta"
            contact="+918318634460"
          />
          <Mentors
            name="Nikhil Kumar"
            contact="+916206007732"
          />
          <Mentors
            name="Aarushi Sharma"
            contact="+917624937102"
          />
          <Mentors
            name="Manas Awasthi"
            contact="+917876628027"
          />
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-6">Testimonials</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <TestimonialCard
            quote="Career Quest helped me find my dream job in tech. The personalized roadmap was a game-changer!"
            author="Sarah L., Software Engineer"
          />
          <TestimonialCard
            quote="The salary predictions were spot-on. I felt confident negotiating my new position thanks to Career Quest."
            author="Michael R., Marketing Manager"
          />
        </div>
      </section>

      <section>
        <div className="bg-blue-600 text-white rounded-lg shadow-md p-8 text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Start Your Career Journey?</h2>
          <p className="text-xl mb-6">Join Career Quest today and unlock your professional potential!</p>
          <button 
          className="bg-white text-blue-600 px-6 py-3 rounded-md font-semibold hover:bg-blue-100 transition duration-300"
          onClick={navigateToCounselling}>
            Get Started
          </button>
        </div>
      </section>
    </div>
  );
};

const FeatureCard: React.FC<{ icon: React.ReactNode; title: string; description: string }> = ({ icon, title, description }) => (
  <div className="bg-white rounded-lg p-8 text-center shadow-lg hover:bg-blue-100 hover:text-blue-800 hover:scale-105 hover:rotate-1 hover:shadow-2xl transition-transform transition-colors duration-300 cursor-pointer">
    <div className="mb-4">{icon}</div>
    <h3 className="text-xl font-semibold mb-2">{title}</h3>
    <p className="text-gray-600">{description}</p>
  </div>
);

const TestimonialCard: React.FC<{ quote: string; author: string }> = ({ quote, author }) => (
  <div className="bg-white rounded-lg shadow-md p-6">
    <p className="text-gray-600 italic mb-4">"{quote}"</p>
    <p className="font-semibold">- {author}</p>
  </div>
);

const Mentors: React.FC<{name: string; contact: string }> = ({name, contact }) => (
  <div className="bg-white rounded-xl p-6 flex items-center justify-between space-x-6 shadow-md hover:shadow-xl hover:bg-blue-50 transition-all duration-300 transform hover:scale-105 hover:-rotate-2 cursor-pointer">
    {/* Mentor Details */}
    <div className="flex flex-col text-left">
      <h3 className="text-2xl font-bold text-gray-800">{name}</h3>
      <p className="text-gray-500 text-lg">{contact}</p>
    </div>

    {/* Action Button */}
    <div className="text-blue-600 hover:text-blue-800 transition-colors duration-300">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        strokeWidth={2}
        stroke="currentColor"
        className="w-6 h-6"
      >
        <path strokeLinecap="round" strokeLinejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
      </svg>
    </div>
  </div>
);


export default Home;