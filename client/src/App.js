import logo from './logo.svg';
import './App.css';
import NavBar from "./components/NavBar";
import Landing from "./pages/landing/Landing";

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Landing/>
    </div>
  );
}

export default App;
