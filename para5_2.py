import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.ismodule(requests))
print(inspect.isfunction(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))