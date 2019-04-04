# OpenWeatherApiScript
# Author: Nikolaj Vorobiev
# Date: 20.02

import socket, ast, sys
appid = sys.argv[1]; city = sys.argv[2]
# creating a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting
sock.connect(('api.openweathermap.org', 80))
# Sending get request
sock.send(bytes('GET /data/2.5/weather?q={0}&appid={1}\n'.format(city, appid), 'utf-8'))
# Decoding response
data = ast.literal_eval(sock.recv(1024).decode('utf-8'))
# Closing socket
sock.close()
# Output
if data['cod'] == 200:
    print(
            data['name'] + '\n' +
            data['weather'][0]['description'] + '\n' +
            'temp: '         + str(round(float(data['main']['temp']) - 273.15, 2)) + u'\N{DEGREE SIGN}' + 'C\n' +
            'humidity: '     + str(data['main']['humidity']) + '%\n'
            'preasure: '     + str(data['main']['pressure']) + 'hPa'
            )
    try:
        print(
                'wind-speed: '   + str(data['wind']['speed'])    + 'km/h\n'
                'wind-deg: '     + str(data['wind']['deg'])
                )
    except KeyError:
        print(
                'wind-speed: 0km/h\n' +
                'wind-deg: -'
                )
else :
    print(data['message'])
