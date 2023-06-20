from typing import Any


class Application:
    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        path = env['PATH_INFO']

        if path in self.routes:
            view = self.routes[path]
            request = {}

            for controller in self.front_controllers:
                controller(request)

            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 PAGE NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Page not found!"]