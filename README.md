# Hackatrix-2019

## Idea

WebApp que centraliza y resume información sobre problemas actuales con el medio ambiente, ofreciendo acciones que uno puede realizar en su vida cotidiana para ayudar. Al mimsmo tiempo, conectandote con organizaciones y centros de reciclaje para mejorar la situacion actual.

## Secciones

### Problemas

Contiene tarjetas con un resumen de cada problema y posibles acciones, ademas de un boton de "Yo lo estoy haciendo" para generar presion y concientizacion social.

### Reciclaje

Contiene categorias de materiales y estados, que luego de completarlos muestra un mapa y acciones para tomar.

### Tips

Contiene todas las acciones que se muestran en problemas, para poder ver todo en una pagina.

### organizaciones

Contiene todas las organizaciones que se involucran, con informacion y contacto.

## Flask

Para routear hay que hacer:

  @app.route("/")

Y despues hacer un metodo que devuelva un STRING:

  def home_page():
      data = mongo.db.info.find()[0]['name']
      return str(data)

## MongoDB

Accedemos a la instancia de mongo:

  mongo

Accedemos a la base:

  mongo.db

Accedemos a la coleccion:

  mongo.db.info

Accedemos al cursor:

  mongo.db.info.find()

Ese cursor hay que iterarlo y sacarle la data
