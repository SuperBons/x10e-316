import './App.scss'; // Import the necessary CSS
import React, { useState, useEffect, useRef } from 'react';

// Component for each message
function Message({ str, sender }) {
    return (
        <div className={`chat-box-message ${sender}`}>
            <div className="chat-box-message-text">{str}</div>
        </div>
    );
}

function ChatBox({ onSignOut }) {
    const [msg, setMsg] = useState([]); // State for messages
    const [input, setInput] = useState(""); // State for input text
    const [isThinking, setIsThinking] = useState(false); // State for bot thinking
    const chatBoxRef = useRef(null);

    // Function to handle sending a message
    const handleSend = () => {
        if (input.trim() !== "" && !isThinking) {
            const newMessage = {
                text: input,
                sender: 'user', // Mark this as user's message
            };

            // Add user message to the messages list
            setMsg([...msg, newMessage]);

            // Clear the input after sending
            setInput("");

            // Set bot thinking state to true
            setIsThinking(true);

            // Simulate a bot response
            setTimeout(() => {
                const botResponse = {
                    text: `Bot: You said "${input}"`, // Simple bot response
                    sender: 'bot',
                };
                setMsg((prevMessages) => [...prevMessages, botResponse]);

                // Set bot thinking state to false
                setIsThinking(false);
            }, 1000);
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
        if (e.key === "Enter" && !isThinking) {
            handleSend();
        }
    };

    return (
        <React.Fragment>
            <div className="chat-box">
                <div className="chat-box-header">
                    <h4>Chat with x10e</h4>
                    <button className="sign-out-button" onClick={onSignOut}>
                        Sign Out
                    </button>
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
                        disabled={isThinking} // Disable input when bot is thinking
                    />
                    <button className="chat-box-send" onClick={handleSend} disabled={isThinking}>
                        Send
                    </button>
                </div>
            </div>
        </React.Fragment>
    );
}

export default ChatBox;