import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Layout from './hocs/Layout';

import Home from './containers/Home';
import Login from './containers/Login';
import Register from './containers/Register';
import Dashboard from './containers/Dashboard';
import Todo from './containers/Todo';
import Leaderboard from './containers/Leaderboard';

import { Provider } from 'react-redux';
import store from './store';

const App = () => (
  <Provider store={store}>
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route exact path="/" element={ <Home/> } />
          <Route exact path="/dashboard" element={ <Dashboard/>} />
          <Route exact path="/login" element={ <Login/> } />
          <Route exact path="/register" element={ <Register/> } />
          <Route exact path="/todo" element = { <Todo/> } />
          <Route exact path="/leaderboard" element = { <Leaderboard/> } />
        </Routes>
      </Layout>
    </BrowserRouter>
  </Provider>
);

export default App;