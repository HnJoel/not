import falcon
import falcon.asgi
class HelloResource:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = (
            'Hello World'
        )
app = falcon.asgi.App()
hello = HelloResource()
app.add_route('/hello', hello)
