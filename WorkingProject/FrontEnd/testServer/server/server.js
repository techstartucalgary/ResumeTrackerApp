const express = require('express')
const upload = require('upload')
const cors = require('cors')

const server = express()

var corsOption = {
	origin: '*',
	optionsSuccessStatus: 200,
}

server.use(cors(corsOptions))

server.post('/upload', upload)

server.listen(8000, () => {
	console.log('Server started!')
})



