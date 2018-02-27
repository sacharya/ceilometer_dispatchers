from setuptools import setup
from ceilometer_dispatchers.meta import version
from ceilometer_dispatchers.meta import description

entry_points = {
    'ceilometer.dispatcher.meter': [
        'influx = ceilometer.dispatcher.http:HttpDispatcher'
    ]
}

setup(
    name="usage_meters",
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
