import web

from mvc.controllers.index import index
from mvc.controllers.contactos import contactos

web.config.debug = False

urls = (
    '/', 'index',
    '/contactos', 'contactos'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()