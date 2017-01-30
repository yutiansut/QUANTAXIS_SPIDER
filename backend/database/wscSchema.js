var mongoose = require('mongoose')

var wscSchema = new mongoose.Schema({
	title:Array,
    url:Array,
    content:Array,
    poster:Array,
    viewNum:Array,
    tag:Array,
    time:Array
})


module.exports = wscSchema;