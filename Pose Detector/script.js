let img_1
let capture
let noseX, noseY
let singlePose
let skeleton
function setup() {
    createCanvas(800, 500)
    capture = createCapture(VIDEO)
    capture.hide()
    img_1 = loadImage('images/shahrukh.png')
    posenet = ml5.poseNet(capture)
    posenet.on('pose', (poses) => {
        // console.log(poses)
        if (poses.length > 0) {
            singlePose = poses[0].pose
            skeleton = poses[0].skeleton
            // noseX = singlePose.pose.leftEye.x
            // noseY = singlePose.pose.leftEye.y
            // console.log(noseX , noseY)
        }
    })
}


function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min
}
function draw() {
    // background(200)
    // line(200,200,300,300)
    // triangle(100,200,300,400,150,450)
    // stroke(200, 0, 0)
    // strokeWeight(5)
  
    image(capture, 0, 0)
    fill(255, 0, 0)
    ellipse(noseX, noseY, 30)
    // r = getRandomArbitrary(0,255)
    // g = getRandomArbitrary(0,255)
    // b = getRandomArbitrary(0,255)
    if (singlePose) {
        // for (let i = 0; i < singlePose.keypoints.length; i++) {
        //     ellipse(singlePose.keypoints[i].position.x, singlePose.keypoints[i].position.y, 50)
        // }
        // for(let j=0; j<skeleton.length; j++){
        //     line(skeleton[j][0].position.x, skeleton[j][0].position.y, skeleton[j][1].position.x, skeleton[j][1].position.y)
        // }
        image(img_1, singlePose.nose.x-100, singlePose.nose.y-120, 200, 200)
    }
    // fill(r,g,b)
    // circle(mouseX,mouseY,100,100)
    // ellipse(250,200,100,100)
    // ellipse(400,200,100,100)
    // stroke(255, 165, 0)
    // ellipse(550,200,100,100)
    // ellipse(700,200,100,100)
}