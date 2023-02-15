const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const fs = require('fs');
const path = require('path')


const app = express()

const router = express.Router()

app.use(bodyParser.urlencoded({extended:true}))
app.use(bodyParser.json())



app.set('view engine','ejs')
app.use(express.static(path.join(__dirname, 'public')));


app.get('/',(req,res)=>
{
    res.render('index',{prediction:null});
})

app.post("/predict", (req, res) => {
    // Insert your ML model here to make predictions
    const input = req.body.input;
    var model = JSON.parse(fs.readFileSync('model.json','utf-8'))
    const prediction = model.pred;
  
    res.render("index", { prediction: null});
  });
  



const port = process.env.port||8080

app.listen(port,(err)=>
{
    if(err) console.log("there is error in connecting to the server!")
    else console.log(`connection ot the port http://localhost:${port}`)
})



