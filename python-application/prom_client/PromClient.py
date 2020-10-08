import time

from prometheus_client.core import CollectorRegistry
from prometheus_client import Gauge, start_wsgi_server

from prometheus_client.metrics_core import GaugeMetricFamily


class PromClient(object):

    def __init__(self):
        self.collector_registry = CollectorRegistry(auto_describe=True)
        self.collectors_handler = CollectoresHandler(self.collector_registry)


class CollectoresHandler(object):

    def __init__(self, collector_registry):
        self.collector_registry = collector_registry

        self.gauge = Gauge('my_gauge', 'my gauge description', registry=collector_registry)
        self.custom_collector = CustomCollector()

        # Adding to registry all the collectors that are not registered
        self.collector_registry.register(self.custom_collector)


class CustomCollector(object):

    def __init__(self):
        self.data = None

    def update(self, data_dict):
        self.data = data_dict

    def collect(self):
        gauge_metric_family = GaugeMetricFamily(
            'my_gauge_family',
            'my gauge family description',
            labels=['ip']
        )

        if self.data is not None:
            for key, value in self.data.items():
                gauge_metric_family.add_metric([key], value=value)

        return [gauge_metric_family]


if __name__ == '__main__':
    prom_client = PromClient()

    start_wsgi_server(8000, registry=prom_client.collector_registry)

    while True:
        time.sleep(1)