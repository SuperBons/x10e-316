import './App.scss';
import logo from './images/LogoX.png';
import React from 'react'; // Ensure React is capitalized.

function ChatBox(){
    return (
        <div className="chat-box">
            <div className="chat-box-header">
                <div className="chat-box-header-text">Chat</div>
            </div>
            <div className="chat-box-body">
                <div className="chat-box-message">
                    <div className="chat-box-message-text">Hello</div>
                </div>
                <div className="chat-box-message">
                    <div className="chat-box-message-text">Hi</div>
                </div>
            </div>
            <div className="chat-box-footer">
                <input className="chat-box-input" type="text" placeholder="Type a message..." />
                <button className="chat-box-send">Send</button>
            </div>
        </div>
    );
}

function App() {
    return (
        <div>
            <div className="wave-container">
                <div className="wave"></div>
                <div className="wave"></div>
                <div className="wave"></div>
                <img className={"logo"} src={logo} alt="Logo" />
            </div>
            {/* Place the ChatBox component here */}
            <ChatBox />
        </div>
    );
}

export default App;