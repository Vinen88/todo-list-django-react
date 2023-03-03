import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Layout from './hocs/Layout';
import PrivateRoute from './hocs/PrivateRoute';

import Home from './containers/Home';
import Login from './containers/Login';
import Register from './containers/Register';
import Dashboard from './containers/Dashboard';

import { Provider } from 'react-redux';
import store from './store';

const App = () => (
  <Provider store={store}>
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route exact path="/" element={ <Home/> } />
          <Route exact path="/dashboard" element={ 
            <RequireAuth redirectTo="/login">
            <Dashboard/> 
            </RequireAuth>
            } />
          <Route exact path="/login" element={ <Login/> } />
          <Route exact path="/register" element={ <Register/> } />
        </Routes>
      </Layout>
    </BrowserRouter>
  </Provider>
);

function RequireAuth({ children, redirectTo }) {
  let isAuthenticated = getAuth();
  return isAuthenticated ? children : <Navigate to={redirectTo} />;
}

export default App;