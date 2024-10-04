import './App.scss';
import logo from './LogoX.png';
import React, { useState, useEffect, useRef } from 'react';

// Component for each message
function Message({ str, sender }) {
    return (
        <div className={`chat-box-message ${sender}`}>
            <div className="chat-box-message-text">{str}</div>
        </div>
    );
}

function ChatBox() {
    const [msg, setMsg] = useState([]); // State for messages
    const [input, setInput] = useState(""); // State for input text
    const chatBoxRef = useRef(null);

    // Function to handle sending a message
    const handleSend = () => {
        if (input.trim() !== "") {
            const newMessage = {
                text: input,
                sender: 'user', // Mark this as user's message
            };

            // Add user message to the messages list
            setMsg([...msg, newMessage]);

            // Simulate a bot response
            setTimeout(() => {
                const botResponse = {
                    text: `Bot: You said "${input}"`, // Simple bot response
                    sender: 'bot',
                };
                setMsg((prevMessages) => [...prevMessages, botResponse]);
            }, 1000);

            // Clear the input after sending
            setInput("");
        }
    };

    // Automatically scroll to the bottom when a new message is added
    useEffect(() => {
        if (chatBoxRef.current) {
            chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
        }
    }, [msg]);

    // Function to handle Enter key press
    const handleKeyPress = (e) => {
        if (e.key === "Enter") {
            handleSend();
        }
    };

    return (
        <React.Fragment>
            <div className="chat-box">
                <div className="chat-box-header">
                    <h4>Chat with GPT</h4>
                </div>
                <div className="chat-box-body" ref={chatBoxRef}>
                    {msg.map((message, index) => (
                        <Message key={index} str={message.text} sender={message.sender} />
                    ))}
                </div>
                <div className="chat-box-footer">
                    <input
                        className="chat-box-input"
                        type="text"
                        placeholder="Type your message..."
                        value={input}
                        onChange={(e) => setInput(e.target.value)} // Update input state
                        onKeyPress={handleKeyPress} // Handle Enter key press
                    />
                    <button className="chat-box-send" onClick={handleSend}>
                        Send
                    </button>
                </div>
            </div>
        </React.Fragment>
    );
}

function App() {
    return (
        <React.Fragment>
            <div className="wave-container">
                <div className="wave"></div>
                <div className="wave"></div>
                <div className="wave"></div>
                <img className="logo" src={logo} alt="Logo" />
            </div>
            <ChatBox />
        </React.Fragment>
    );
}

export default App;
