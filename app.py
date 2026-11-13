import web
import logging

from mvc.controllers.index import index
from mvc.controllers.contactos import contactos
from mvc.controllers.insertar_contacto import InsertarContacto
from mvc.controllers.ver_contacto import VerContacto
from mvc.controllers.actualizar_contacto import ActualizarContacto

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",  # Evita errores con tildes o caracteres especiales
)

web.config.debug = False

urls = (
    '/', 'index',
    '/contactos', 'contactos',
    '/insertar_contacto', 'InsertarContacto',
    '/ver_contacto/(.*)', 'VerContacto',
    '/actualizar_contacto/(.*)', 'ActualizarContacto'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()