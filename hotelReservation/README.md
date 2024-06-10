In order to deploy the hotelReservation application to a Kubernetes cluster navigate to the `\kubernetes` path.

Run `kubectl apply -Rf \<path-of-folder>\kubernetes` and wait for all the pods to be deployed and have status `Running`

Run `kubectl apply -f \<path-of-folder>\hr-client\hr-client.yaml` to create the hr-client pod

Copy the `wkr2` folder to the hr-client pod

Log in to hr-client pod

Install wrk2 with `sudo apt-get wrk2`

Running `python3 command.py` will run the workload script and start workload generation

The original application can be found in the DeathStarBench repository `https://github.com/delimitrou/DeathStarBench.git`
