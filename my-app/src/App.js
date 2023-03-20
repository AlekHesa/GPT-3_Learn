
import { Button, ButtonGroup, Dropdown } from "react-bootstrap";
import './App.css';
import ThemeSwitcher from './summary'
import axios from 'axios';
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
// Bootstrap Bundle JS
import "bootstrap/dist/js/bootstrap.bundle.min";



function App() {

  const[prompt,setPrompt] = useState("");
  const[response,setResponse] = useState("");

  const prompt_api = {'text':prompt}

  const json = JSON.stringify(prompt_api)

  const handleSubmit = (e) =>{
    e.preventDefault();

    const data = { "data": prompt };
    axios.post("http://127.0.0.1:8000/GPT3/Test", data)
    .then((res) =>{
      setResponse(res.data)
    })
    .catch((err) => {
      console.error(err)
    })
  }
  return (
    
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
    <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Text Summarizer</h1>
    <h6 className="card text-white bg-info mb-3">React - OpenAI</h6>
   <div className="card-body">
    <form onSubmit={handleSubmit}>
    <span className="card-text"> 
      <textarea className="mb-2 form-control desIn"   
      value={prompt}
      onChange={(e) => setPrompt(e.target.value)}
      placeholder='Summarize your text'/>
    <button className="btn btn-outline-primary mx-2 mb-3" 
    type="submit"
    style={{'borderRadius':'50px',"font-weight":"bold"}}  >Summarize Text</button>
    </span>
    </form>
    <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
    <div >
    <p>{response}</p>    
    </div>
    </div>
  </div>
     
       
 
    
   
  );
}

export default App;
