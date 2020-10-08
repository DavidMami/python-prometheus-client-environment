from prometheus_client import start_wsgi_server

from prom_client import HandleData, PromClient, working


def run():
    try:
        # simulating a synchronous code
        working()

        print()

        prom_client = PromClient()

        # simulating a sub-thread, for doing some work
        handle_data = HandleData(prom_client)
        handle_data.start()

        start_wsgi_server(8000, registry=prom_client.collector_registry)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
