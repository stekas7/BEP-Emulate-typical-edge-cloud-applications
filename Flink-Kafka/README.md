Deploy Flink using the `.YAML` files in the Flink folder

Deploy the Strimzi operator using Helm or through `https://strimzi.io/downloads/`

Create the necessary topics and Kafka configuration using the  `.YAML` files in the Kafka folder

Access the Flink UI through port 8081 or expose the JobManger as a NodePort service and access it

Upload the Flink job

For workload generation:

Latest Docker image used in the BEP can be pulled with `docker pull stekinho/kafkascriptv2` , otherwise adjust the script found in the `Workload\script`, then build and push the Docker image and then pull it on the cluster from Dockerhub

Pod will be created which runs the workload script

In the workload folder a Python script for data extraction from Prometheus and creation of a parallel plot can be found. Adjust as needed
