import cherrypy
cherrypy.config.update({
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 8082  
})
class MyApp:
    @cherrypy.expose
    def index(self):
        return("23b01a12g0")
    @cherrypy.expose
    def res_html(self):
        return open('res.html').read()
    @cherrypy.expose
    def html(self):
        return"""
        <html>
            <head>
                <title>CherryPy HTML Page.</title>
            </head>
            <body>
                <h1>Hello vasavi</h1>
                <p>23b01a12g0</p>
            </body>
        </html>
        """
if __name__ == '__main__':
    cherrypy.quickstart(MyApp())

