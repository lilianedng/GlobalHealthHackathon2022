import React, {useState} from 'react' 

const ReadingsContext = React.createContext({
    video: null,
})


const address = "10.101.62.80";

const video_socket = new WebSocket(`ws://${address}:1234`)

export const ReadingsContextProvider = (props) => {
    const [video, setVideo] = useState(null);

    video_socket.addEventListener('open', function (event) {
        console.log('Connected to the video WS Server!')
    });

    // Connection closed
    video_socket.addEventListener('close', function (event) {
        console.log('Disconnected from the video WS Server!')
    });

    video_socket.addEventListener('message', function(event) {
        if (event.data instanceof Blob) {
            setVideo(event.data)
        }
    });

    return (
        <ReadingsContext.Provider
            value={{
                video: video,
            }}>
                {props.children}
        </ReadingsContext.Provider>
    )
}

export default ReadingsContext