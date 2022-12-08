
function $builtinmodule(name) {
  // Depends on turtle module
  Sk.importModule('turtle', false, true);

  const mod = {};

  let _connected = false;
  let _speed = 50;
  let _dir   = 0;

  function initSphero(self) {
  	Sk.TurtleGraphics.module.colormode.func_code(255);
  }

  function set_rgb_led(self, r, g, b) {
		if(r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255) {
			throw new Sk.builtin.ValueError(`Invalid led value`);
		}
		Sk.TurtleGraphics.module.pencolor.func_code(r, g, b, 100);
	}

  function move(self, dir) {
		if(dir < 0 || dir > 359) {
			throw new Sk.builtin.ValueError(`move, invalid direction value (${dir})`);
		}
		_dir = dir;
		return Sk.TurtleGraphics.module.setheading.func_code(_dir);
  }

  function roll(self, dir, speed) {
		if(dir < 0 || dir > 360) {
			throw new Sk.builtin.ValueError(`roll, invalid direction value (${dir})`);
		}
		if(speed < 0 || speed > 255) {
			throw new Sk.builtin.ValueError(`roll, invalid speed value (${speed})`);
		}
		_speed = speed;
		_dir = dir;
		return Sk.TurtleGraphics.module.setheading.func_code(_dir);
  }

  function wait(self, duration) {
  	if(duration > 0) {
  		throw new Sk.builtin.ValueError(`wait, invalid duration value (${duration})`);
  	}
  	if(duration > 2) {
  		duration = 2;			// timeout de 2s
  	}
  	return Sk.TurtleGraphics.module.forward.func_code(_speed * duration);
  }

  function SpheroWrapper($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(initSphero);
    $loc.set_rgb_led = new Sk.builtin.func(set_rgb_led);
    $loc.move = new Sk.builtin.func(move);
    $loc.wait = new Sk.builtin.func(wait);
    $loc.roll = new Sk.builtin.func(roll);
  }

  mod.Sphero = Sk.misceval.buildClass(mod, SpheroWrapper, "Sphero", []);

  mod.connect = new Sk.builtin.func(function(arg) {
  	if (arg) {
  		throw new Sk.builtin.ValueError(`connect error : argument invalid`);
  	}
  	if(_connected) {
  		throw new Sk.builtin.ValueError(`already connected`);
  	}
  	_connected = true;
    var newInstance = Sk.misceval.callsimOrSuspendArray(mod.Sphero);
    return newInstance;
  });

  // console.info('Module', Sk.TurtleGraphics.module)

  mod.__name__ = new Sk.builtin.str("sphero");

  return mod;
};
