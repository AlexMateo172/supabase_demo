import web

from mvc.controllers.index import index
from mvc.controllers.contactos import contactos
from mvc.controllers.insertar_contacto import InsertarContacto

web.config.debug = False

urls = (
    '/', 'index',
    '/contactos', 'contactos',
    '/insertar_contacto', 'InsertarContacto'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()