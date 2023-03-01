import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from './hocs/Layout';

import Home from './containers/Home';
import Login from './containers/Login';
import Register from './containers/Register';
import Dashboard from './containers/Dashboard';

const App = () => (
  <BrowserRouter>
    <Layout>
      <Routes>
        <Route exact path="/" element={ <Home/> } />
        <Route exact path="/dashboard" element={ <Dashboard/> } />
        <Route exact path="/login" element={ <Login/> } />
        <Route exact path="/register" element={ <Register/> } />
      </Routes>
    </Layout>
  </BrowserRouter>
);

export default App;