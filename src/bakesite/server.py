import functools


def serve():
    import http.server
    import socketserver

    PORT = 8003

    Handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory="./_site"
    )

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port http://localhost:{PORT}")
        httpd.serve_forever()
