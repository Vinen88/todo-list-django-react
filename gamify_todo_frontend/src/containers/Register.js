import React from 'react';
import { useState } from 'react';
import { connect } from 'react-redux';
import { register } from '../actions/auth';
import { Navigate } from 'react-router-dom';

const Register = ({ register }) => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        re_password: ''
    });
    const [accountCreated, setAccountCreated] = useState(false);
    const { username, password, re_password } = formData;
    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });
    const onSubmit = e => {
        e.preventDefault();
        if (password === re_password){
            register(username, password, re_password);
            setAccountCreated(true);
        }
    };

    if (accountCreated){
        return <Navigate to="/" />
    }
    return(
        <div className='container mt-5'>
            <h1>Register for an Account</h1>
            <p>Create an account!</p>
            <form onSubmit={e => onSubmit(e)}>
                <div className="form-group">
                    <label className='form-label'>Username:</label>
                    <input
                        className='form-control'
                        type='text'
                        placeholder='Username*'
                        name='username'
                        value={username}
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label className='form-label mt-3'>Password:</label>
                    <input
                        className='form-control'
                        type='password'
                        placeholder='Password*'
                        name='password'
                        minLength='6'
                        value={password}
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label className='form-label mt-3'>Confirm Password:</label>
                    <input
                        className='form-control'
                        type='password'
                        placeholder='Confirm Password*'
                        name='re_password'
                        minLength='6'
                        value={re_password}
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <button className='btn btn-primary mt-4' type='submit'>Register</button>
            </form>
            <p className='mt-3'>
                Already have an account? <a href='/login'>Sign in</a>
            </p>
        </div>
    );
};

export default connect(null, { register })(Register);