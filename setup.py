from setuptools import setup
from ceilometer_dispatchers.meta import version
from ceilometer_dispatchers.meta import description

entry_points = {
    'ceilometer.dispatcher.event': [
        'http = ceilometer.dispatcher.http:HttpDispatcher'
    ]
}

setup(
    name="ceilometer_dispatchers",
    version=version,
    author="sudarshan acharya",
    author_email="sudarshan.acharya@rackspace.com",
    packages=[
        'ceilometer_dispatchers',
        'ceilometer_dispatchers.influx'
    ],
    entry_points=entry_points,
    long_description=description
)
