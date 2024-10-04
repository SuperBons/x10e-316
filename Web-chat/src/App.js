import './App.scss';
import logo from './LogoX.png';
import React, { useState } from 'react';

function Message({ str }) {
  return (
      <div className="chat-box-message">
        <div className="chat-box-message-text">{str}</div>
      </div>
  );
}

function ChatBox() {
  const [msg, setMsg] = useState([]); // Declare msg state here
  const [input, setInput] = useState(""); // State to handle input text

  // Function to handle sending a message
  const handleSend = () => {
    if (input.trim() !== "") {
      setMsg([...msg, input]); // Create a new array with the new message
      setInput(""); // Clear input after sending
    }
  };

  // Function to handle Enter key press
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
      <div className="chat-box">
        <div className="chat-box-body">
          {msg.map((message, index) => (
              <Message key={index} str={message} /> // Display each message
          ))}
        </div>
        <div className="chat-box-footer">
          <input
              className="chat-box-input"
              type="text"
              placeholder="Message x10e"
              value={input}
              onChange={(e) => setInput(e.target.value)} // Update input state
              onKeyPress={handleKeyPress} // Handle Enter key press
          />
          <button className="chat-box-send" onClick={handleSend}>
            Send
          </button>
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
          <img className="logo" src={logo} alt="Logo" />
        </div>
        <ChatBox />
      </div>
  );
}

export default App;