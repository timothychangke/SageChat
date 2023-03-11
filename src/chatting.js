import './App.css';
import React from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';

var prompt = `You: `;

const Chatting = () => {

    /*const [language_name, setlanguagename] = React.useState('English')*/

    const [translatedtranscript, settranslated] = React.useState("")

    const addtranslation = (translation) => {
      const tmp = translation + "\n"
      settranslated(prev => tmp+prev)
    };

  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition
  } = useSpeechRecognition();

  if (!browserSupportsSpeechRecognition) {
    return <span>Browser doesn't support speech recognition.</span>;
  }

  function handleclick(event) {
    event.preventDefault();

    if (listening){
        SpeechRecognition.stopListening()

        console.log(transcript)

        /* Chat-GPT api */
        const { Configuration, OpenAIApi } = require('openai');
        const configuration = new Configuration({
            apiKey: process.env.REACT_APP_API
        });
        const openai = new OpenAIApi(configuration);          
        /*
        openai.createCompletion({
          model: "text-davinci-003",
            prompt:`Translate this into ${language_name}:\n\n${transcript}\n\n`, 
            temperature:0.7,
            max_tokens:200,
            top_p:1.0,
            frequency_penalty:0.2,
            presence_penalty:0.2
              })
        .then((response) => {
        const tmp = response.data.choices[0].text;
        console.log(tmp)
        addtranslation(tmp);
        })
        */
        prompt += transcript
        prompt += "\nFriend: "
        
        openai.createCompletion({
          model: "text-davinci-003",
          prompt: prompt,
          temperature: 0.7,
          max_tokens: 256,
          top_p: 1.0,
          frequency_penalty: 0.6,
          presence_penalty: 0.6,
          stop: ["You:"],
        })
        .then((response) => {
          const tmp = response.data.choices[0].text
          prompt += tmp
          prompt += "\nYou:"
          console.log(tmp)
          addtranslation(tmp);
          });

        console.log(translatedtranscript)
    }
    else {
      resetTranscript()
      console.log('listening start')
        SpeechRecognition.startListening({ continuous: true, language: 'en-US' })
    }
  }

  return (
    <div className='translate'>

      {/* 
      <div className="what-to-translate">
        <p className='translate-p'>Let's translate to</p>
        <select className="language" id="language" onChange={changelanguage}>
            {options.map(({ name, code }, index) => <option key={code} value={name} >{name}</option>)}
        </select>
      </div>*/
      }     

      <div className='buttons'>
        <button className = {listening ? 'stopbutton' : 'listenbutton'} onClick={handleclick}>{listening ? 'Stop' : 'Listen'}</button>
      </div>

      <div className='text-area'>
      <textarea className = 'transcript-text'placeholder='Conversation will show here' value = {transcript} rows="5" cols="50"></textarea>
      <textarea placeholder="Translation will show here" value={translatedtranscript} rows="8" cols="50"></textarea>
      </div>

    </div>
  );
};
export default Chatting;

