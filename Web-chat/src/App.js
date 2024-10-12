import './App.scss';
import logo from './LogoX.png';
import React, { useState } from 'react';
import SignIn from './SignIn';
import SignUp from './SignUp';
import ChatBox from './ChatBox';

function App() {
    const [isSignedIn, setIsSignedIn] = useState(false);
    const [isSigningUp, setIsSigningUp] = useState(false); // New state to track sign-up flow

    const handleSignIn = () => {
        setIsSignedIn(true);
    };

    const handleSignOut = () => {
        setIsSignedIn(false);
    };

    const handleSignUp = () => {
        setIsSigningUp(true); // Show the SignUp screen
    };

    const handleBackToSignIn = () => {
        setIsSigningUp(false); // Go back to SignIn screen
    };

    return (
        <React.Fragment>
            <img className="logo" src={logo} alt="Logo"/>

            <div className="wave-container">
                <div className="wave"></div>
                <div className="wave"></div>
                <div className="wave"></div>
            </div>
            {isSignedIn ? (
                <ChatBox onSignOut={handleSignOut}/>
            ) : isSigningUp ? (
                <SignUp onSignIn={handleSignIn} onBack={handleBackToSignIn}/>
            ) : (
                <SignIn onSignIn={handleSignIn} onSignUp={handleSignUp}/>
            )}
        </React.Fragment>
    );
}

export default App;