import './App.scss';
import logo from './images/LogoX.png';
import React from 'react';
import { useState } from 'react';

function Message(str){
    const [msg, setMsg] = useState([]);
    return (
        <>
            <div className="chat-box-message">
                <div className="chat-box-message-text">{str}</div>
            </div>
        </>
    );
}

function ChatBox() {
    return (
        <div className="chat-box">
            <div className="chat-box-body">
                {msg}
            </div>
            <div className="chat-box-footer">
                <input className="chat-box-input" type="text" placeholder="Message x10e"/>
                <button className="chat-box-send" onKeyUp={OnClick}>Send</button>
            </div>
        </div>
    );
}

function OnClick() {
    let a = msg;
    a.push(document.getElementsByClassName("chat-box-input")[0].innerText);
    setMsg(a);
    console.log("ASD");
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