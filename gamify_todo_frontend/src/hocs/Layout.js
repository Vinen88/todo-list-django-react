import React from 'react';
import Navbar from '../components/Navbar';
import { Fragment } from 'react';

const layout = ({ children }) => (
     <Fragment>
        <Navbar />
        { children }
     </Fragment>
);

export default layout;