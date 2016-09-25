import logging

from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne import Iterable
from spyne.decorator import srpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server


logging.basicConfig(level=logging.DEBUG)


class HelloWorldService(ServiceBase):
    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(name, times):
        for i in range(times):
            yield 'Hello, %s' % name

application = Application([HelloWorldService],
    tns='spyne.examples.hello.http',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)
    print "listening to http://127.0.0.1:8000"
    print "wsdl is at: http://localhost:8000/?wsdl"
    server.serve_forever()