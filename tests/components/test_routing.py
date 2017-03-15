from apistar import App, Route
from apistar.components import http, test
from apistar.routing import URLArg, URLArgs


def get_args(path: http.Path, args: URLArgs) -> http.Response:
    return http.Response({
        'path': path,
        'args': args
    })


def get_arg(path: http.Path, var: URLArg) -> http.Response:
    return http.Response({
        'path': path,
        'var': var
    })


app = App(routes=[
    Route('/args/<int:var>/', 'get', get_args),
    Route('/arg/<int:var>/', 'get', get_arg),
])


client = test.RequestsClient(app)


def test_args():
    response = client.get('http://example.com/args/1/')
    assert response.json() == {
        'path': '/args/1/',
        'args': {'var': 1}
    }


def test_arg():
    response = client.get('http://example.com/arg/1/')
    assert response.json() == {
        'path': '/arg/1/',
        'var': 1
    }
