import React, { useEffect, useState } from 'react';
import axios from 'axios';


const Leaderboard = () => {
    const [leaderboard, setLeaderboard] = useState([]);
    useEffect(() => {
        load_leaderboard();
    }, []);

    const load_leaderboard = async () => {
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        };
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/profile/leaderboard/`, config);
        setLeaderboard(await res.data['top_users'])
    };

    return(
        <div className='container'>
            <div className='mt-5 p-5 bg-light'>
                <h1 className = 'display-4'>Leaderboard</h1>
                <p className = 'lead'>These are our users who have scored the most points!</p>
                <hr className = 'mt-4' />
                <ol className='list-group list-group-numbered'>
                {leaderboard.map((user, index) => {
                    return(
                        <li key={index}>{user.user} - {user.points}</li>
                    )
                })}
                </ol>
            </div>
        </div>
    );
};

export default Leaderboard;