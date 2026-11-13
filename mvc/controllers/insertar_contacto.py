import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views/', base='template')

class InsertarContacto:
    #Renriza el archivo insertar_contacto.html
    def GET(self):
        return render.insertar_contacto()
    #Recibe los inputs del formulario y accede a cada uno
    #utilizando el atributo name
    def POST(self):
        formulario = web.input()
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']

        #print(f"Nombre: {nombre}")
        #print(f"Email: {email}")
        #print(f"Telefono: {telefono}")

        model_contactos = ModelContactos()

        datos = model_contactos.insertarContacto(nombre,email,telefono)

        html = """
          <h1>Contacto almacenado exitposamente</h1>
          <a href='/contactos'>Volver a la lista de contactos</a>
        """

        return html

