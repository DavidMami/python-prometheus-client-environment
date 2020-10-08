# python-prometheus-client-environment
Building a basic environment, which enables the ability to practice on the python prometheus client

The folowing services that i'm about to make use of in this specific environment are being run using the 
Docker-compose configuration file, but can be used with any other container run-time.

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

### Starting the environment
To run any of the commands, we have to ensure that we open a terminal and navigate to the path where this readme is located.

```
docker-compose up -d prometheus
docker-compose up -d grafana
docker-compose up -d --build python-application
```
### Accessibility to the services from the host
```
localhost:90 # python application metrics
localhost:9091 # prometheus web server
localhost:3000 # grafana
```

### A basic graph that visualizes the data
![Capture](https://user-images.githubusercontent.com/72276426/95464378-86fc1d00-0982-11eb-8e7b-abb5ea1ff131.PNG)

### Understanding the flow
Basicly, their are 3 main parts in the specified flow:
  - The python application that starts both web server and web application.
    * The web server - starts a basic wsgi server for routing the requests from the Prometheus service, and responses with the
    wanted metrics in the Prometheus format.
    * The web application - a basic wsgi app that works in collaboration with the python-prometheus-client.
    It generates data, updates the register's metric collectors and repeats it.
  - The Prometheus service - responsible on scraping the metrics from the python appliction and storing it.
  - The Grafana service - responsible on scraping the wanted metrics from the Prometheus servic and presenting them 
  in a nice graphic way.
  
    
    
      

