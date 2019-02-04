#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")

    def post(self):
        # get numbers and operation
        primer_numero = int(self.request.get("numero1"))
        segundo_numero = int(self.request.get("numero2"))
        operacion_par = self.request.get("operacion")
       
        if operacion_par == "+":
            resultado=primer_numero + segundo_numero
        elif operacion_par == "-":
            resultado=primer_numero - segundo_numero
        elif operacion_par == "*":
            resultado = primer_numero * segundo_numero
        elif operacion_par == "/":
            resultado=primer_numero / segundo_numero


        context = {
            "resultado": resultado,
            "numero1": primer_numero,
            "numero2": segundo_numero
        }
        return self.render_template("calculator.html", params=context)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
