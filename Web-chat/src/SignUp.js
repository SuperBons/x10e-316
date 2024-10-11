import React, { useState } from 'react';
import './SignIn.scss';
import logo from './LogoX.png';

function SignUp({ onSignIn, onBack }) {
    const [Fname, setFname] = useState('');
    const [Lname, setLname] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }
        console.log('FName:', Fname);
        console.log('LName:', Lname);
        console.log('Username:', username);
        console.log('Password:', password);
        onSignIn();
    };

    return (
        <div className="sign-in-app">
            <div className="line-1 anim-typewriter">
                <p>Create a new account</p>
            </div>
            <div className="backdrop">
                <div className="sign-in-container">
                    <h2 className="sign-in-title"></h2>
                    <p className="sign-in-subtitle">Sign Up</p>
                    <form onSubmit={handleSubmit}>
                        <input
                            type="text"
                            className="sign-in-input"
                            value={Fname}
                            onChange={(e) => setFname(e.target.value)}
                            placeholder="First Name"
                            required
                        />
                        <input
                            type="text"
                            className="sign-in-input"
                            value={Lname}
                            onChange={(e) => setLname(e.target.value)}
                            placeholder="Last Name"
                            required
                        />
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
                        <input
                            type="password"
                            className="sign-in-input"
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            placeholder="Confirm Password"
                            required
                        />
                        <button type="submit" className="sign-in-button">Sign Up</button>
                        <button type="button" className="sign-up-button" onClick={onBack}>
                            Back to Sign In
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default SignUp;