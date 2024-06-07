helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

kubectl create namespace monitoring

helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring

kubectl expose svc prometheus-kube-prometheus-prometheus --type="NodePort"  -n monitoring --name="prometheus-nodeport"
