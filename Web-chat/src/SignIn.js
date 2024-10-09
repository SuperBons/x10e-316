// src/SignIn.js
import React, { useState } from 'react';
import './SignIn.scss'; // Import the CSS file with unique styles
import logo from './LogoX.png';

function SignIn({ onSignIn }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [rememberMe, setRememberMe] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add your sign-in logic here
        console.log('Username:', username);
        console.log('Password:', password);
        console.log('Remember Me:', rememberMe);
        onSignIn(); // Call the onSignIn function passed as a prop
    };

    return (

        <div className="sign-in-app">
            <div className="sign-in-container">
                <h2 className="sign-in-title"></h2>
                <p className="sign-in-subtitle">Sign-In</p>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        className="sign-in-input"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Username"
                        required
                    />
                    <input
                        type="password"
                        className="sign-in-input"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Password"
                        required
                    />
                    <div className="sign-in-form-group">
                        <input
                            type="checkbox"
                            className="sign-in-checkbox"
                            checked={rememberMe}
                            onChange={(e) => setRememberMe(e.target.checked)}
                        />
                        <label className="sign-in-checkbox-label">Remember me</label>
                        <a href="" className="forgot-pass">Forgot password?</a>

                    </div>
                    <button type="submit" className="sign-in-button">Sign In</button>
                </form>
            </div>
        </div>
    );
}

export default SignIn;