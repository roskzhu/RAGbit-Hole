import React from 'react'
import '../../styles/Landing.css'
import { Link } from 'react-router-dom';


const Header = () => {
  return (
    <div className="header">
      <div className="header-img">
      <img src="/main.png" alt="demo" />
      </div>
      <div className="text-container">
        <div className="title">
        <h1>Rag
        <span style={{fontFamily:'Helvetica Now', backgroundImage:'linear-gradient(to bottom right, black, black)'}}>-</span>
        bit Hole</h1>
        </div>
        <div>
        <p>Your passport to immersive exploration. <br/>
          Rabbit hole into your favourite topics with ease, uncovering a trove of 
          knowledge and discovering the endless wonders that await your curiosity.</p>
        </div>
        <Link to="/chat">
        <button>
          EXPLORE
        </button>
      </Link>
      </div>
    </div>
  )
}

export default Header