# python-prometheus-client-environment
Building a basic environment, which enables the ability to practice on the python prometheus client

### Build-up of the environment
The environment enables us to run a all the needed apps in a convenient manner, in order to monitor the metrics 
that the python-prometheus-client offers us.

### How does it work
The docker-compose runs 3 services for each needed app:
  - Prometheus
  - Grafana
  - The python project, which is being monitored with the prom-client (might be considered as an exporter)

### How to use
Taking into account that all the containers are running, with the right farwarded ports, 
we can acces them from the browser, and watch the metrics.

