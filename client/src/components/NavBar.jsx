import React, { useState, useEffect } from 'react';
import styled from '@emotion/styled'
import '../styles/NavBar.css'
import { Link, useLocation } from 'react-router-dom';


const NavBar = () => {
  const location = useLocation();
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY;
      setIsScrolled(scrollPosition > 0);
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

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
        <Link to="/" className={location.pathname === '/' ? 'active' : ''}>
            <p>
              Home
            </p>
          </Link>
          <Link to="/chat" className={location.pathname === '/chat' ? 'active' : ''}>
            <p>
              Try Now
            </p>
          </Link>
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