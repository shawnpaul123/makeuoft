//Test file in js

var Blynk = require('blynk-library');
var Gpio = require('onoff').Gpio;

var led  = new Gpio(18,'out');
var Auth = 
var Blynk = new Blynk.Blynk(Auth);


var sensor_1 = new.blynk.VirtualPin(0);//takes fuel amount
var sensor_2 = new.blynk.VirtualPin(1);//is button
var sensor_3 = new.blynk.VirtualPin(0);

# A - car drives

sensor_2.on('write', function(param){

	if (sensor_1 == '1'){
	  led.writeSync(1);
	} else{
	  led.writeSync(0);
	}

	console.log('V0', parm[0]):

});

