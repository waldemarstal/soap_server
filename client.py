from suds.client import Client


hello_client = Client('http://localhost:8000/?wsdl')
print hello_client.service.say_hello("Waldest", 5)
print hello_client