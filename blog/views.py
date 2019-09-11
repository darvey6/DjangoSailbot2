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

Winds = [
    {
        'SensorID': 'Test',
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
        'SensorID': 'Test',
        'Current': 'August 27, 2018',
        'Voltage': 'August 27, 2018',
        'Temperature': 'August 27, 2018',
        'Status': 'August 27, 2018',
        'UpdatedTime': 'August 27, 2018'
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

Acceleratometer = [
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




def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')

def sensors(request):
    context={
        'Winds': Winds
    }
    return render(request, 'blog/sensors.html', context)


