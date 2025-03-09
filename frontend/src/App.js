import React from 'react';
import HomePage from './components/HomePage';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';

function App() {
  return (
    <div className="App">
      <HomePage />
      <div className="flex justify-center space-x-4 mt-8">
        <LoginForm />
        <RegisterForm />
      </div>
    </div>
  );
}

export default App;