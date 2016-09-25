import logging

from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne import Iterable
from spyne.decorator import srpc
from spyne.model.complex import ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server


class txHeader(ComplexModel):
   timestamp = Unicode
   POS = Unicode


class registerService(ServiceBase):
    # __in_header__ = txHeader

    @rpc(Unicode, Integer, Integer, _in_header = txHeader, _returns=Integer)
    def registerNewRequest(ctx, brand, sim, pesel):
        return 1001


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('listening to http://127.0.0.1:8000')
    logging.info('wsdl is at: http://localhost:8000/?wsdl')

    application = Application([registerService],
        tns='http://some-fake-address.cc',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )
    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()