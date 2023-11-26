import React, { useState, useEffect } from "react"
import "./ChatPane.css"
import { BsTrash3Fill } from "react-icons/bs"
import { PiPaperPlaneTiltFill } from "react-icons/pi"
import {Link } from "react-router-dom";
import { FaFileVideo } from "react-icons/fa";

const ChatPane = () => {
  const [message, setMessage] = useState("")
  const [responses, setResponses] = useState([])
  console.log("initialization")
  console.log(responses)
  console.log(message)

  const getChatHistory = async () => {
    // Get request for past convo
    //   const response = await fetch(`http://127.0.0.1:5000/chatHistory/get-chat-history/` + fileName, {
    //     method: 'GET',
    //     headers: {
    //       'Authorization': `Bearer ${localStorage.getItem('token')}`,
    //       'Content-Type': 'application/json',
    //     }
    //   });

    //   if (!response.ok) {
    //     throw new Error('Network response was not ok');
    //   }

    //const responseData = await response.json();
    //Sample chat history
    const responseData = {
      chatHistory: [
        {
          sender: "sender-user",
          content: "Hi, bot. How are you today?",
        },
        {
          sender: "sender-bot",
          content: "Hello! I'm doing well, thank you for asking.",
        },
        {
          sender: "sender-user",
          content: "I have a question about your services.",
        },
        {
          sender: "sender-bot",
          content: "Sure, go ahead and ask your question.",
        },
      ],
    }

    console.log("Response chat history", responseData)

    // Since responseData is an array, map over it directly
    const formattedResponses = responseData.chatHistory.map(
      (message, index) => {
        const sender = index % 2 === 0 ? "user" : "bot" // Alternate between 'user' and 'bot'
        return { sender, content: message.content }
      }
    )

    setResponses(formattedResponses)
  }

  useEffect(() => {
    getChatHistory()
  }, [])

  const handleSendMessage = async (event) => {
    event.preventDefault()

    if (message === "") {
      return
    }

    const userMessage = { sender: "user", content: message }
    setResponses((prevResponses) => [...prevResponses, userMessage])
    setMessage("")

    // Add a loading message
    const loadingMessage = {
      sender: "bot",
      content: (
        <div className="typing-indicator">
          <div className="dot"></div>
          <div className="dot"></div>
          <div className="dot"></div>
        </div>
      ),
    }
    setResponses((prevResponses) => [...prevResponses, loadingMessage])

    //Grab response from the API
    // try {
    //     const response = await fetch(`http://127.0.0.1:5000/chat/get-response`, {
    //         method: 'POST',
    //         headers: {
    //             'Authorization': `Bearer ${localStorage.getItem('token')}`,
    //             'Content-Type': 'application/json',
    //         },
    //         body: JSON.stringify({
    //             query: message,
    //         }),
    //     });

    //     if (!response.ok) {
    //         throw new Error('Network response was not ok');
    //     }

    const responseData = {
      role: "Bot",
      response: "My response to your question",
    }

    // const responseData = await response.json();
    const reply = responseData.response

    // Remove the loading message and add the bot's response
    setResponses((prevResponses) => {
      const updatedResponses = prevResponses.slice(0, -1) // Remove the last message (loading message)
      updatedResponses.push({ sender: "bot", content: reply }) // Add the bot's response
      return updatedResponses
    })
  }

  return (
    <div className="container">
      <div className="chat-pane">
        <div className="messages">
          {responses &&
            responses.map((response, index) => (
              <div key={index} className={`message ${response.sender}`}>
                <div className="messenger-name">
                  {response.sender === "bot" ? "Rabbit" : "You"}
                </div>
                {response.content}
              </div>
            ))}
          {/* <div ref={messagesEndRef}></div> This is the dummy div */}
        </div>
      </div>
      <div className="form-container">
        <form className="input-area" onSubmit={handleSendMessage}>
          <Link to="/audio">
            <button className="audioButton">
            <FaFileVideo size={24}/>
            </button>
          </Link>
          
          <input
            type="text"
            value={message}
            placeholder="Type a message..."
            onChange={(e) => setMessage(e.target.value)}
          />
          <button className="basic-button" type="submit">
            <PiPaperPlaneTiltFill size={24} />
          </button>
        </form>
      </div>
    </div>
  )
}

export default ChatPane
