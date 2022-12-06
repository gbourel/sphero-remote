import asyncio
import websockets
import json
import subprocess

print("Communication avec Robot Sphero")

status = {}
# DEBUG
status = {
  'history': [],
  'programs': [
  # {
#     'id': '12-a67',
#     'student': 'Laiponge Bob',
#     'program': """
# import time
# import sphero

# orb = sphero.init()

# orb.connect()
# orb.set_rgb_led(120,0,0)
# time.sleep(1)

# orb.roll(30, 0)
# """,
#     'state': 'READY'
#   }
#   ,
#    {
#     'id': '234',
#     'student': 'Doe John',
#     'program': """
# import time
# import sphero

# orb = sphero.init()

# orb.connect()
# orb.set_rgb_led(120,0,0)
# time.sleep(1)

# orb.roll(30, 0)
# """,
#     'state': 'WAITING'
#   }
  ]
}

async def get_status(ws, data=None):
  return status

async def add_program(ws, data=None):
  print(f"Add program {json.dumps(data)}")
  if(len(status["programs"]) > 0):
    data["state"] = "WAITING"
  else:
    data["state"] = "READY"
  status["programs"].append(data)
  return status

async def start_program(ws, data=None):
  print(f"Start program {data['id']}")
  for prgm in status["programs"]:
    if prgm["id"] == data["id"]:
      prgm["state"] = "RUNNING"
      await ws.send(json.dumps(status))
      try:
        with open('remote_prgm.py', 'w') as file:
          file.write(prgm["program"])
        subprocess.run(['python3', 'remote_prgm.py'], shell=False)
        # exec(prgm["program"])
      except Exception as e:
        print(f"Error {e}")
      status["history"].append(prgm)
      status["programs"].remove(prgm)
      if len(status["programs"]) > 0:
        status["programs"][0]["state"] = 'READY'
      prgm["state"] = "DONE"
      await ws.send(json.dumps(status))
  return status

handlers = {
  'add_program': add_program,
  'get_status': get_status,
  'start_program': start_program
}

# create handler for each connection
async def handler(websocket, path):
  while True:
    data = await websocket.recv()
    msg = json.loads(data)
    res = ''
    try:
      handler = handlers[msg["cmd"]]
      if "data" in msg:
        res = await handler(websocket, msg["data"])
      else:
        res = await handler(websocket)
    except Exception as e:
      print(f"Handler error for command {msg['cmd']}")
      print(e)
      res = { 'error': 'command error'}
    await websocket.send(json.dumps(res))

start_server = websockets.serve(handler, "localhost", 7007)

print("En attente d'un programme...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
