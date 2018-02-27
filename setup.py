from setuptools import setup
from usage_meters.meta import version
from usage_meters.meta import description

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
        'ceilometer-dispatchers',
        'ceilometer-dispatchers.influx'
    ],
    entry_points=entry_points,
    long_description=description
)
