import React from 'react';
import Header from './Header';

const HomePage = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <main className="p-4">
        <h2 className="text-xl font-semibold">Bienvenue sur la plateforme !</h2>
        <p className="mt-2">Connectez-vous ou inscrivez-vous pour commencer.</p>
      </main>
    </div>
  );
};

export default HomePage;