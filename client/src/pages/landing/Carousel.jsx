import React, { useState, useEffect, useRef, useCallback } from "react";
import "../../styles/Carousel.css";

const InfiniteSlider = function InfiniteSlider({
  speed,
  direction,
  children,
}) {
  const [looperInstances, setLooperInstances] = useState(1);
  const outerRef = useRef(null);
  const innerRef = useRef(null);

  function resetAnimation() {
    if (innerRef?.current) {
      innerRef.current.setAttribute("data-animate", "false");

      setTimeout(() => {
        if (innerRef?.current) {
          innerRef.current.setAttribute("data-animate", "true");
        }
      }, 10);
    }
  }

  const setupInstances = useCallback(() => {
    if (!innerRef?.current || !outerRef?.current) return;

    const { width } = innerRef.current.getBoundingClientRect();

    // If width is 0, set it to a default value (e.g., 500)
    const defaultWidth = 800;
    const actualWidth = width === 0 ? defaultWidth : width;

    const { width: parentWidth } = outerRef.current.getBoundingClientRect();
    const widthDeficit = parentWidth - width;
    const instanceWidth = actualWidth / innerRef.current.children.length;

    console.log("parentWidth:", parentWidth);
    console.log("width:", width);

    console.log("instanceWidth:", instanceWidth);

    const calculatedInstances = Math.ceil(parentWidth / instanceWidth) +1;
    if (widthDeficit) {
      setLooperInstances(calculatedInstances || 1);
    }
    console.log("looperInstances:", calculatedInstances || 1);


    resetAnimation();
  }, [looperInstances]);

  useEffect(() => setupInstances(), [setupInstances]);

  useEffect(() => {
    window.addEventListener("resize", setupInstances);

    return () => {
      window.removeEventListener("resize", setupInstances);
    };
  }, [looperInstances, setupInstances]);

  return (
    <div className="looper" ref={outerRef}>
      <div className="looper__innerList" ref={innerRef} data-animate="true">
        {[...Array(looperInstances)].map((_, ind) => (
          <div
            key={ind}
            className="looper__listInstance"
            style={{
              animationDuration: `${speed}s`,
              animationDirection: direction === "right" ? "reverse" : "normal",
            }}
          >
            {children}
          </div>
        ))}
      </div>
    </div>
  );
};

export default InfiniteSlider;
