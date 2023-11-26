import React from 'react';
import Header from './Header';
import Carousel from './Carousel';


const Landing = () => {
  return (
    <div className='landing-container'>
      <Header />
      <Carousel speed="50" direction="right" className='dance'>
        <div className="contentBlock contentBlock--one">
          <img src='/demo1.png' className="scroller-photo"/>
        </div>
        <div className="contentBlock contentBlock--one">
        <img src='/demo2.png' className="scroller-photo"/>
        </div>
        <div className="contentBlock contentBlock--one">
        <img src='/demo3.png' className="scroller-photo"/>
        </div>
        <div className="contentBlock contentBlock--one">
        {/* <svg className="scroller-photo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"> */}
          {/* Your SVG path or other elements go here */}
        {/* </svg> */}
        <img src='/demo4.png' className="scroller-photo"/>
        </div>
    </Carousel>
    </div>
  );
};

export default Landing;
