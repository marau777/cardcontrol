const express = require('express')
const ip = require('ip');
const app = express();
const port = 3000;
const ipAddress = ip.address();

const spawn = require("child_process").spawn;

app.get('/', (req, res) => {
  res.sendfile('./cardcontrol-index.html');
})

app.get('/insert', (req, res) => {
  const insertProcess = spawn('python3',["./cardcontrol.py", "insert"]);
  insertProcess.stdout.on('data', (data) => {
    console.log(data.toString())
    res.writeHead(200, {'content-type': 'text'})
    res.write(data.toString())
    res.end()
  });
}) 

app.get('/remove', (req, res) => {
  const removeProcess = spawn('python3',["./cardcontrol.py", "remove"]);
  removeProcess.stdout.on('data', (data) => {
    console.log(data.toString())
    res.writeHead(200, {'content-type': 'text'})
    res.write(data.toString())
    res.end()
  });
})

/*
app.get('/update', (req, res) => {
  const updateProcess = spawn('python3',["./cardcontrol.py", "update"]);
  updateProcess.stdout.on('data', (data) => {
    console.log(data.toString())
    res.writeHead(200, {'content-type': 'text'})
    res.write(data.toString())
    res.end()
  });
})
*/

app.listen(port, () => {
  console.log(`cardcontrol app listening at http://${ipAddress}:${port}`);
})