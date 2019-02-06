#!/usr/bin/env python
import os
import jinja2
import webapp2

#setting jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

# base controladores para mis controladores
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

# CONTROLADORES
class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("sobremi.html")

class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class ContactoHandler(BaseHandler):
    def get(self):
        return self.render_template("contacto.html")


class ProyectosHandler(BaseHandler):
    def get(self):
        return self.render_template("proyectos.html")



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/contacto', ContactoHandler),
    webapp2.Route('/proyectos', ProyectosHandler),
], debug=True)
