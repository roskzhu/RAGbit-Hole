import React, { useState, useEffect, useRef } from 'react';
import Webcam from 'react-webcam';
import '../../styles/audio.css'; // Import your CSS file

const Record = () => {
  const webcamRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const [recordedChunks, setRecordedChunks] = useState([]);
  const [isRecordingStopped, setIsRecordingStopped] = useState(false);

  const handleConvertToBinary = async () => {
    if (recordedChunks.length === 0) {
      return;
    }

    setIsRecordingStopped(false); // Reset the flag

    // Concatenate the recorded chunks into a single Blob
    const combinedBlob = new Blob(recordedChunks, { type: 'audio/webm' });

    try {
      const file = new File([combinedBlob], 'temp-audio.webm');

      const formData = new FormData();
      formData.append('file', file);

      

    } catch (error) {
      console.log('error', error);
    }
  };

  const handleStartRecording = () => {
    const constraints = { audio: true, video: false };

    navigator.mediaDevices
      .getUserMedia(constraints)
      .then((stream) => {
        const videoStream = webcamRef.current.stream;
        mediaRecorderRef.current = new MediaRecorder(stream, { mimeType: 'audio/webm' });

        mediaRecorderRef.current.ondataavailable = (event) => {
          if (event.data.size > 0) {
            setRecordedChunks((prev) => prev.concat(event.data));
          }
        };

        mediaRecorderRef.current.start();
      })
      .catch((error) => console.log('error', error));
  };

  const handleStopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      mediaRecorderRef.current.onstop = () => {
        setIsRecordingStopped(true);
      };
    }
  };

  useEffect(() => {
    if (isRecordingStopped) {
      handleConvertToBinary();
    }
  }, [isRecordingStopped]);

  return (
    <div className="h-screen text-white">
      <div className="flex justify-center">
        <div className="flex flex-col">
          <Webcam audio={true} ref={webcamRef} className="rounded-2xl max-w-1" />
          <div className="flex justify-around mt-8">
            <button
              onClick={handleStartRecording}
              type="submit"
              className="btn-start-recording"
            >
              Start Recording
            </button>
            <button
              onClick={handleStopRecording}
              type="submit"
              className="btn-stop-recording"
            >
              Stop Recording
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Record;
