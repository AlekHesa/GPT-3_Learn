import logo from './logo.svg';
import './App.css';
import React, {useState,useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios';

function App() {

  const [apiKey, setApiKey] = useState('');
  const[TEXT,inputText] = useState('')


  
  //Post API KEY
  const addAPIHandler = () => {
    

    

    axios.post('http://127.0.0.1:8000/GPT3', 
    {
      "data":{
        key:apiKey     
       }
    },
    
    )
    .then(response => { 
      console.log(response.data)
    })
    .catch(error => {
        console.log(error)
    });
  };

  const addText = () => {
    axios.post('http://127.0.0.1:8000/GPT3/Summary',{'text':TEXT})
    .then(res => console.log(res))
  };

  return (
    
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-info mb-1" styleName="max-width: 20rem;">GPT-APP</h1>
      <form onSubmit={addAPIHandler}>
        <span className="card-text"> 
          <input className="mb-2 form-control titleIn"  type="text" value={apiKey} onChange={(event) => setApiKey(event.target.value)} placeholder='API KEY'/> 
          
          <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}
          type='submit' onClick={addAPIHandler}>Insert API KEY</button>
        </span>
      </form>
      <h6 className="card text-white bg-primary mb-3">FastAPI-React</h6>
     <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Add your text</h5>
      <span className="card-text"> 
        <textarea className="mb-2 form-control titleIn"  placeholder='Text' 
        onChange={event => inputText(event.target.value)}/> 
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}} 
      onClick={addText} >Summarize this Text</button>
      </span>
      <h5 className="card text-white bg-primary mb-3">Result</h5>
      <div >
      
      </div>
      </div>
    </div>




    
          
  );
}

export default App;
