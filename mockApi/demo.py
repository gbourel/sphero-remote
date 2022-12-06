import sphero

orb = sphero.connect()

orb.set_rgb_led(0,120,0)

orb.move(0) # Se déplace direction 0°
orb.wait(1) # Attend 1s
orb.move(90) # Se déplace direction 180°
orb.wait(1) # Attend 1s
orb.move(230)

orb.done()

