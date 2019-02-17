let {PythonShell} = require('python-shell')


/*
PythonShell.run('my_script.py', null, function (err) {
  if (err) throw err;
  console.log('finished');
});
*/

var Blynk = require('blynk-library');
var Gpio = require('onoff').Gpio;

var Auth = '4fd693da193a43b1baaa489a4b73c7af';
var Blynk = new Blynk.Blynk(Auth);


var sensor_1 = new Blynk.VirtualPin(0);//takes fuel amount
var sensor_2 = new Blynk.VirtualPin(1);//is button
console.log(Number(sensor_1));

sensor_2.on('write', function(param){
	if (param[0] == '1'){
		//calling python magic
	  	PythonShell.run('my_script.py', null, function (err) {//change script name!
  			if (err) throw err;
	  		console.log('finished');
	  		Blynk.notify("Fuellling Complete!");
	 		Blynk.email("shawn20michaels@gmail.com", "F*** JS", "Lolz");
		}
		)
	}
});
