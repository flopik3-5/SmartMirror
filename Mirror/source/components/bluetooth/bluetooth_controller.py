import jsonpickle
from bluetooth import *

from source.components.configurator.models.config_field import ConfigField
from source.components.configurator.models.config_field_type import ConfigFieldType

if __name__ == '__main__':

    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service(server_sock, "SampleServer",
                      service_id=uuid,
                      service_classes=[uuid, SERIAL_PORT_CLASS],
                      profiles=[SERIAL_PORT_PROFILE],
                      #                   protocols = [ OBEX_UUID ]
                      )

    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        data = client_sock.recv(1024)
        print("received [%s]" % data)
        a = ConfigField("Password", "******", ConfigFieldType.text, None, None)
        b = ConfigField("Time", "", ConfigFieldType.time, None, None)
        c = ConfigField("Data", "", ConfigFieldType.date, None, None)
        d = ConfigField("Dropdown", "", ConfigFieldType.dropdown, ['red','blue','green'], None)
        e = ConfigField("Checkbox", "", ConfigFieldType.checkbox, ['c++','c#','python'], None)
        client_sock.send(jsonpickle.encode([a,b,c,d,e], unpicklable=False))
    except IOError as e:
        print(e)
        pass

    while True:
        a=0

    print("disconnected")

    client_sock.close()
    server_sock.close()
    print("all done")
