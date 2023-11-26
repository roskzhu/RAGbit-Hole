import React from 'react'
import styled from '@emotion/styled'
import { keyframes } from '@emotion/react';
import { useNavigate } from 'react-router-dom';
import '../../styles/Landing.css'

const Header = () => {
  return (
    <div className="header">
      <div className="header-img">
      <img src="/main.svg" alt="demo" />
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
        <button>
          EXPLORE
        </button>
      </div>
    </div>
  )
}

export default Header