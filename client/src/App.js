import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavBar from "./components/NavBar";
import Landing from "./pages/landing/Landing";
import ChatPane from './pages/chat/ChatPane';


function App() {
  return (
    <BrowserRouter>
        <NavBar/>
        <Routes>
          <Route path="/" element={<Landing />}/>
          <Route path="/chat" element={<ChatPane />}/>
        </Routes>
    </BrowserRouter>
  );
}

export default App;

//     <div className="home-container">
//       <ChatPane/>

//     <div className="App">
//       <Landing/>
//     </div>