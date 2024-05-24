import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    json = JSONRenderer().render(CarSerializer(car).data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    return Car(**data)
