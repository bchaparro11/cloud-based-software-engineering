docker build -t bchaparro4/contract_analyzer_analysis_ms .; docker build -t bchaparro4/contract_analyzer_analysis_db .

docker run --rm -p 8000:8000 --name container bchaparro4/contract-analyzer-analysis-ms:1.3

hostname -I | awk '{print $1}' --> To know Host IP to connect container to MongoDB Daemon

docker build -t bchaparro4/contract-analyzer-analysis-ms .; docker push bchaparro4/contract-analyzer-analysis-ms

az aks create     --resource-group rsrc-grp-1     --name contract-analyzer-cluster     --node-count 1     --node-vm-size Standard_B2s     --enable-cluster-autoscaler     --min-count 1     --max-count 1     --location East US