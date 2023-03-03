import React from 'react';
import Navbar from '../components/Navbar';
import { Fragment } from 'react';
import { connect } from 'react-redux';
import { checkAuthenticated } from '../actions/auth';
import { useEffect } from 'react';

const Layout = ({ children, checkAuthenticated }) => {
   useEffect(() => {
         checkAuthenticated();
   }, []);
     return(
         <Fragment>
            <Navbar />
            { children }
         </Fragment>
     );
};

export default connect(null, { checkAuthenticated })(Layout);