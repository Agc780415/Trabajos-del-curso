#!/usr/bin/env python
# coding=utf-8
import os
import jinja2
import webapp2
import re

from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class ResultHandler(BaseHandler):
    # 2) Añadimos lógica necesaria al POST de este controlador para guardar el mensaje en db
    def post(self):
        nombre = remove_tags(self.request.get("nombre"))
        correo = remove_tags(self.request.get("correo"))
        texto = remove_tags(self.request.get("texto"))

        # aquí creamos un objeto nuevo de la clase Message, con el contenido que ha escrito el usuario
        new_message = Message(contenidonombre=nombre, contenidocorreo=correo, contenidotexto=texto )


        # aquí guardamos el mensaje en db
        new_message.put()

        context = {
            "nombre": nombre,
        }

        return self.render_template("resultado.html", params=context)


TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
        return TAG_RE.sub('', text)




# 4) Añadimos la lógica necesaria a nuestro controlador para obtener todos los mensajes desde db y pasarlos a
# la vista
class MessageListHandler(BaseHandler):
    def get(self):

        # aquí obtenemos todos los mensajes de db
        resegnas = Message.query().fetch()

        context = {
            "resegnas": resegnas,
        }

        return self.render_template("listado.html", params=context)




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/resultado', ResultHandler),

    # 3) Añadimos ruta, controlador y template necesarios para la página de listar mensajes
    webapp2.Route('/listado', MessageListHandler),
], debug=True)