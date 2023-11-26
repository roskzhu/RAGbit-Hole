import React, { useState, useEffect } from "react"
import "./ChatPane.css"
import { BsTrash3Fill } from "react-icons/bs"
import { PiPaperPlaneTiltFill } from "react-icons/pi"

const ChatPane = () => {
  const [message, setMessage] = useState("")
  const [responses, setResponses] = useState([])

  const [loading, setLoading] = useState(false)

  const handleSendMessage = async (event) => {
    event.preventDefault()

    if (message === "") {
      return
    }

    const userMessage = { sender: "user", content: message }
    setResponses((prevResponses) => [...prevResponses, userMessage])
    setMessage("")
    setLoading(true)

    //Grab response from the API
    const response = await fetch(
      `http://127.0.0.1:5000/get_response?message=${userMessage.content}`,
      {
        method: "POST",
        // headers: {
        //   Authorization: `Bearer ${localStorage.getItem("token")}`,
        //   "Content-Type": "application/json",
        // },
        // body: JSON.stringify({
        //   query: message,
        // }),
      }
    )

    if (!response.ok) {
      throw new Error("Network response was not ok")
    }

    const responseData = await response.json()

    // Remove the loading message and add the bot's response
    setResponses((prevResponses) => {
      const updatedResponses = [...prevResponses]
      updatedResponses.push({ sender: "bot", content: responseData }) // Add the bot's response
      return updatedResponses
    })

    setLoading(false)
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
                {response.sender === "bot" ? (
                  loading ? (
                    "..."
                  ) : (
                    <>
                      <div>{response.content.text}</div>
                      <div className="links">
                        <div className="link-header">
                          Dive down the rabbit hole; Topics:
                        </div>
                        {response.content.citations.map((citation, i1) => {
                          return (
                            <div className="citation-flex">
                              {citation.text}:
                              {citation.document_ids.map((id, i2) => {
                                const doc = response.documents.find(
                                  (doc) => doc.id === id
                                )
                                return (
                                  <div className="citation-flex link-clr">
                                    <a href={doc.url}>[{i2}]</a>
                                  </div>
                                )
                              })}
                            </div>
                          )
                        })}
                      </div>
                    </>
                  )
                ) : (
                  response.content
                )}
              </div>
            ))}
          {/* <div ref={messagesEndRef}></div> This is the dummy div */}
        </div>
      </div>
      <div className="form-container">
        <form className="input-area" onSubmit={handleSendMessage}>
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
