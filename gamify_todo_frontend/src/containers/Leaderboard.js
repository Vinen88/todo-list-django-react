import React from 'react';
import { Link } from 'react-router-dom';

const leaderboard = () => (
    <div className='container'>
        <div className='mt-5 p-5 bg-light'>
            <h1 className = 'display-4'>Leaderboard</h1>
            <p className = 'lead'>These are our users who have scored the most points!</p>
            <hr className = 'mt-4' />
            {/* insert request and display data */}
        </div>
    </div>
);

export default leaderboard;