import './App.css';
import pic from './Assets/Health-Hackathon.jpeg'
import VideoStream from './VideoStream/VideoStream';

function App() {
  return (
    <div className="App">
      
      <div className="ImageContainer">
        <VideoStream></VideoStream>
        <div className="Overlay">
          {/* <h1 className="Title">Becoming the voice for the muted and hard of hearing</h1>
          <p className="Description">TransL is a free web application that connects the impaired (in speech and listening) to the rest of the world by providing a stable platform to translate between American sign language and English text in real-time.</p>
          <div className="Button">
            Read more
          </div> */}
        </div>
      </div>
      <h1 className="Work">
        How it works
      </h1>
      <p className="WorkDes">The website uses a real-time video captured from the domestic devices of the users to translate the gestures of sign language into English text and/or sound to help bridge the gap and enabling users to lead more independent lives.</p>
      <div className='Container'>
        <div className="Card">
          <img className="CardImage" src="https://global-uploads.webflow.com/5a5de2c1a0eb5000019e4dc0/5a796bf35df1250001149a00_Blind_1.jpg"></img>
          
        </div>
        <div className="Card">
        <h1 className="CardTitle">Visit the TransL webapp to make use of our services</h1>
          <p className="CardText">As a mute or hearing-impaired person, whenever you need assistance in translating between sign language and English to accomplish your daily tasks, our website will just provide you with the needed support. In a simple and one-stop solution, you will be able to speak to your mobile phone or tablet which will in turn process this motion to display English text. Being a user of the system, you get to decide from text and/or speech forms of output depending on the situation. We hope this app will be revolutionary to guide you along your simple way of life ranging from difficult tasks like consulting doctors to easy ones like checking your directions with a stranger.</p>
        </div>
      </div>
      <h1 className="Work">
        Join the community
      </h1>
      <p className="WorkDes">Become an exclusive user of the app to help make this world a more accessible place to the differently abled to lead everyday lives that we have accepted for granted. We couldn’t do this much without the help and dedication of our community that supports innovative thoughts for the health and welfare sector.</p>
      <div className="Container">
        <div className="Community">
          <img className="CommunityImage" src="https://global-uploads.webflow.com/5a5de2c1a0eb5000019e4dc0/5a8bcdd9d906b100019094a8_Dwonload.png"></img>
          <h1 className="CTitle">Download TransL</h1>
          <div className="CDes">
          Get the TransL app and join our global community as a blind/low-vision user or a sighted volunteer.
          </div>
        </div>
        <div className="Community">
          <img className="CommunityImage" src="https://global-uploads.webflow.com/5a5de2c1a0eb5000019e4dc0/5a8bcdf60c611b00011884c7_Translate.png"></img>
          <h1 className="CTitle">Translate TransL</h1>
          <div className="CDes">
          Help us make our app accessible for more people in their native language. Getting started is easy and straightforward.
          </div>
        </div>
        <div className="Community">
          <img className="CommunityImage" src="https://global-uploads.webflow.com/5a5de2c1a0eb5000019e4dc0/5a8bce0dd906b100019094b8_Share.png"></img>
          <h1 className="CTitle">Translate TransL and Help us spread the word</h1>
          <p className="CDes">
          Helping through Trans is easy. Invite your friends, family or colleagues.
          </p>
        </div>
      </div>
      <div className='Container'>
        <div className="VContainer">
          <h1 className="CTitle">How can TransL help your business?</h1>
          <p>The virtual assistance provided by TransL might just be the next upgrade for CX teams and other employees to help bring inclusivity and accessibility to companies of all sizes.</p>
        </div>
        <img className="HelpImg" src="https://global-uploads.webflow.com/5a5de2c1a0eb5000019e4dc0/624ffbd32a16a11d8a2e65a4_morey-illustration_2.png"></img>
      </div>
    </div>
  );
}

export default App;
