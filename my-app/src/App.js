
import { Button, ButtonGroup, Dropdown } from "react-bootstrap";
import axios from 'axios';
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
// Bootstrap Bundle JS
import "bootstrap/dist/js/bootstrap.bundle.min";
import MyChatbot from "./Chatbot";
import NavPage from "./components/navigation";

function Summary_Pages() {

  const[apikey, setAPIKey] = useState("");

  const[prompt,setPrompt] = useState("");
  const[response,setResponse] = useState("");
  const[convo,setConvo] = useState([]);

  const addMessage = (message, role) => {
    const id = Date.now(); // generate a unique ID for the message
    setConvo([...convo, { id, role, content: message }]);
  }



  const addApiKEY = (e) =>{
    e.preventDefault();

    // const data = { "data": prompt };
    // axios.post("http://localhost:8000/GPT3/Test", 
    // headers:{"Content-Type":'application/json'}
    // ,data)
    const data = {"key":apikey}
    axios.post(
      "http://localhost:8000/GPT3",
      data,
      {headers: {
        'Content-Type':'application/json'
      }}
    )
    .then((res) =>{
      
      setAPIKey(res.data)
       

    })
    .catch((err) => {
      console.error(err)
    })
  }


  
  const handleChat = (e) =>{
    e.preventDefault();

    addMessage(prompt, 'user');
    


    // const data = { "data": prompt };
    // axios.post("http://localhost:8000/GPT3/Test", 
    // headers:{"Content-Type":'application/json'}
    // ,data)
    const data = {"data":prompt}
    axios.post(
      "http://localhost:8000/GPT3/Summary",
      data,
      {headers: {
        'Content-Type':'application/json'
      }}
    )
    .then((res) =>{
        setResponse(res.data)
        addMessage(res.data, 'assistant');

    })
    .catch((err) => {
      console.error(err)
    })
  }
  return (
 <>
  <MyChatbot/>
  <div>
    {/* <Navbar></Navbar> */}
    <div className="container text-center">
    <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">OpenAI Testing</h1>
    <h6 className="card text-white bg-info mb-3">React - OpenAI</h6>
    </div>
    
    {/*API KEY */}
    <div className=" list-group-item text-center justify-content-center align-items-center mx-auto" style={{"width":"300px", "backgroundColor":"white", "marginTop":"15px"}} >
      <form onSubmit={addApiKEY}>
         
          <input className="mb-2 form-control desIn"
          type="password"  
          value={apikey}
          onChange={(e) => setAPIKey(e.target.value)}
          placeholder='Summarize your text'/>
          <button className="btn btn-outline-primary mx-2 mb-3" 
          type="submit"
          style={{'borderRadius':'50px',"font-weight":"bold"}}  >Add API Key</button>
      </form>
    </div>   

<div className="list-group-item text-center justify-content-center align-items-center mx-auto" style={{"width":"500px", "backgroundColor":"white", "marginTop":"15px"}} >
    <div className="card-body">
      <h5 className="card text-white bg-primary mb-1">Text Summarizer</h5>
        <form onSubmit={handleChat}>
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
          <h5 className="card text-white bg-dark mb-3">Result</h5>
          <div>
            {response}
                {/* {convo.map((message) => {
                  if (message.role === 'user') {
                    return <div key={message.id} className="user-message">{message.content}</div>
                  } else if (message.role === 'assistant') {
                    return <div key={message.id} className="assistant-message">{message.content}</div>
                  }
                })} */}
          </div>
      </div>
    </div>
    </div>
                    
    </>   

  
 

   
  );
}

export default Summary_Pages;
