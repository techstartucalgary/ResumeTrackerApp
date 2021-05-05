const IncomingForm = 
require('formidable').IncomingForm

module.exports = function upload(req, res) {
	var form = new IncomingForm()
	form.on('file', (field, file) => {
		// save it on the data base, access using file.path
	})
	
	form.on('end', () => {
		res.json()
	})
	
	form.parse(req)
}