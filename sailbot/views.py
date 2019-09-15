from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

Wind = [
    {
        'SensorID': 'TestID',
        'WindSpeed': 'Test Title',
        'WindDirection': 'Here is the content',
        'WindReference': 'August 27, 2018',
        'WindTemperature': 'August 27, 2018',
        'Current': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
    }
]

WinchMotor = [
    {
        'SensorID': '1',
        'Current': '21',
        'Voltage': '51',
        'Temperature': '18',
        'Status': 'on',
        'UpdatedTime': 'August 27, 2018',
        'Editable': 1,
    },{
        'SensorID': '2',
        'Current': '65',
        'Voltage': '56',
        'Temperature': '15',
        'Status': 'off',
        'UpdatedTime': 'August 27, 2018',
        'Editable': 1,
    }
]


RudderMotor = [
    {
        'SensorID': 'Test',
        'Current': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
    }
]


GPS = [
    {
        'SensorID': 'Test',
        'Quality': 'Test Title',
        'HDOP': 'Here is the content',
        'AntennaAltitude': 'August 27, 2018',
        'GeoidalSeparation': 'August 27, 2018',
        'Lat': 'August 27, 2018',
        'Lon': 'August 27, 2018',
        'GroundSpeed': 'August 27, 2018',
        'TrackMadeGood': 'August 27, 2018',
        'MagneticVariation': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
    }
]

BoomAngle = [
    {
        'SensorID': 'Test',
        'Angle': 'Test Title',
        'Current': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
    }
]

BMS = [
    {
        'SensorID': 'Test',
        'BatteryCurrent': 'Test Title',
        'BatteryTemperature': 'Test Title',
        'BatteryVoltage': 'Test Title',
        'Current': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
    },
]

Accelerometer = [
    {
        'SensorID': 'Test',
        'x_pos': 'Test Title',
        'y_pos': 'Test Title',
        'z_pos': 'Test Title',
        'Current': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
    },
]

navHome  = [
    {
        'name': 'ABOUT',
        'url': '#about',
    },
    {
        'name': 'SENSORS',
        'url': '#services',
    },
    {
        'name': 'WAYPOINT',
        'url': '#portfolio',
    },
    {
        'name': 'CONTACT',
        'url': '#contact',
    },
]

navWinch = [
    {
        'name': 'DATA',
        'url': '#Data',
    },
    {
        'name': 'FORM',
        'url': '#Forme',
    },
    {
        'name': 'HISTORY',
        'url': '#History',
    },
]

def home(request):
    context = {
        'Winds': Winds,
        'WinchMotor': WinchMotor,
        'RudderMotor': RudderMotor,
        'GPS': GPS,
        'BoomAngle': BoomAngle,
        'BMS': BMS,
        'Accelerometer': Accelerometer,
        'Navbar': navHome,
        'PageName': 'Sailbot'
    }
    return render(request, 'sailbot/home.html',context)

def about(request):
    return render(request, 'sailbot/about.html')


def winchmotor (request):
    context={
        'WinchMotor': WinchMotor,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/winchmotor.html', context)

def accelerometer (request):
    context={
        'Accelerometer': Accelerometer,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/accelerometer.html', context)

def bms (request):
    context={
        'BMS': BMS,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/bms.html', context)

def boomangle (request):
    context={
        'Boomangle': BoomAngle,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/boomangle.html', context)

def gps (request):
    context={
        'GPS': GPS,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/gps.html', context)


def ruddermotor (request):
    context={
        'Ruddermotor': RudderMotor,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/ruddermotor.html', context)

def wind (request):
    context={
        'Wind': Wind,
        'Navbar': navWinch,
        'PageName': 'Winch Motor'
    }
    return render(request, 'sailbot/wind.html', context)
