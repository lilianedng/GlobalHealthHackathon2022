import React, {useState, useEffect, useContext} from 'react' 
import ReadingsContext from '../Context/context'

const VideoStream = (props) => {
    const context = useContext(ReadingsContext)
    useEffect(() => {
        let msg = document.getElementById("qr_canvas");
        if (context.video instanceof Blob) {
            let ctx = msg.getContext("2d")
            let image = new Image();
            image.src = URL.createObjectURL(context.video);
            console.log("----",context.video);
            image.addEventListener("load", (e) => {
                ctx.drawImage(image, 0, 0, msg.width, msg.height);
            });
        }
    })

    return (
        <canvas id="qr_canvas" ></canvas>
    )
}

export default VideoStream