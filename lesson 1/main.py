import views
from wavy import Application
from wavy.routes import routes


def work_controller(request):
    request['workers'] = {
        'position': 'director FBI',
        'first_name': 'Etnaise',
        'last_name': 'Deviant'
    }


front_controllers = [
    work_controller
]

app = Application(routes, front_controllers)

