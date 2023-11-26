import logo from './logo.svg';
import './App.css';
import NavBar from "./components/NavBar";
import Landing from "./pages/landing/Landing";
import Header from './pages/landing/Header';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Landing/>
      {/* <Header/> */}
    </div>
  );
}

export default App;
