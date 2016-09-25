import requests


url="http://localhost:8000/?wsdl"
headers = {'content-type': 'application/soap+xml'}
# headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="UTF-8"?>
		<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:crm="http://some-fake-address.cc">
			<soapenv:Header>
				<crm:txHeader>
					<crm:timestamp>2016-06-09T08:00:00.000+02:00</crm:timestamp>
					<crm:POS id="1" name="Salonik"/>
				</crm:txHeader>
			</soapenv:Header>
			<soapenv:Body>
				<crm:registerNewRequest>
					<crm:brand>Motor</crm:brand>
					<crm:sim>1234567890</crm:sim>
					<crm:pesel>66778899232</crm:pesel>
				</crm:registerNewRequest>
			</soapenv:Body>
		</soapenv:Envelope>"""


response = requests.post(url, data=body, headers=headers)
print response.status_code
print response.content