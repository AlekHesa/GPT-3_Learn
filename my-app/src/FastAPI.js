import { useState } from "react";
import { Button, ButtonGroup, Dropdown } from "react-bootstrap";



function Website() {
  const ThemeSwitcher = () => {
    const [theme, setTheme] = useState(null);
  
    const resetTheme = () => {
      setTheme(null);
    };
  
  <div className="mb-2">
      <Dropdown as={ButtonGroup} size="lg">
        <Button
          className="text-capitalize"
          variant={theme ? theme : "secondary"}
        >
          {theme ? theme : "Default"}
        </Button>
        <Dropdown.Toggle
          split
          variant={theme ? theme : "secondary"}
          id="dropdown-split-basic"
        />
        <Dropdown.Menu>
          <Dropdown.Item eventKey="1" onClick={() => setTheme("primary")}>
            Primary
          </Dropdown.Item>
          <Dropdown.Item eventKey="2" onClick={() => setTheme("danger")}>
            Danger
          </Dropdown.Item>
          <Dropdown.Item eventKey="3" onClick={() => setTheme("success")}>
            Success
          </Dropdown.Item>
          <Dropdown.Divider />
          <Dropdown.Item eventKey="4" onClick={resetTheme}>
            Default Theme
          </Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    </div>
  
  // // const [text, setText] = useState('');
  // // const [completion, setCompletion] = useState('');

  // // const generateCompletion = async () => {
  // //   const configuration = new Configuration({
  // //       apiKey: process.env.OPENAI_API_KEY,
  // //     });
  // //     const openai = new OpenAIApi(configuration);
  // //     const response = await openai.createCompletion({
  // //       model: "text-davinci-003",
  // //       prompt: text,
  // //       max_tokens: 7,
  // //       temperature: 0,
  // //     });
  // //     setCompletion(response.choices[0].text)
  // // };
  // // const handleTextChange = (e) => {
  // //   setText(e.target.value);
  // // };
  // // return (
  // //   <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
  // //   <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Text Summarizer</h1>
  // //   <h6 className="card text-white bg-info mb-3">React - OpenAI</h6>
  // //  <div className="card-body">
  // //   <form >
  // //   <span className="card-text"> 
  // //     <textarea className="mb-2 form-control desIn"   
  // //     placeholder='Summarize your text'/>
  // //   <button className="btn btn-outline-primary mx-2 mb-3" 
  // //   type="submit"
  // //   style={{'borderRadius':'50px',"font-weight":"bold"}}  >Summarize Text</button>
  // //   </span>
  // //   </form>
  // //   <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
  // //   <div >
  // //   <p></p>    
  // //   </div>
  // //   </div>
  // // </div>
  // );
}
}
export default Website;

