import React, { useState } from 'react';

const {Configuration,OpenAIApi} = require("openai");

function Website() {
  const [text, setText] = useState('');
  const [completion, setCompletion] = useState('');

  const generateCompletion = async () => {
    const configuration = new Configuration({
        apiKey: process.env.OPENAI_API_KEY,
      });
      const openai = new OpenAIApi(configuration);
      const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: text,
        max_tokens: 7,
        temperature: 0,
      });
      setCompletion(response.choices[0].text)
  };
  const handleTextChange = (e) => {
    setText(e.target.value);
  };
  return (
    <div>
      <form onSubmit={generateCompletion}>
        <textarea placeholder="Enter text" value={text} onChange={handleTextChange} />
        <button type="submit">Generate Summary</button>
      </form>
      {completion && <p>{completion}</p>}
    </div>
  );
}

export default Website;