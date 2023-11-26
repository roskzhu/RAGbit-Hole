import React from 'react'
import styled from '@emotion/styled'
// import { Link } from 'react-router-dom'
import { useLocation } from 'react-router-dom';
import '../styles/NavBar.css'

const NavBar = () => {
  return (
    <div className="nav-container">
      <div className="left-container">
        <div className="left-bar">
          <p>Rag</p>
            <p style={{fontFamily:'Helvetica Now'}}>-</p>
          <p>bit Hole</p>
        </div>
      </div>
      <div className="right-container">
        <div className="right-bar">
          <p>
            Home
          </p>
          <p>
            Try Now
          </p>
        </div>
      </div>
    </div>
  )
}

const Filter = styled.svg`
  visibility: hidden; 
  position: absolute;
`

export default NavBar