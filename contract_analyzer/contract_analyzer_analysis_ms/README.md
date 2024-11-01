docker build -t bchaparro4/contract_analyzer_analysis_ms .; docker build -t bchaparro4/contract_analyzer_analysis_db .

docker run --rm -p 8000:8000 --name container bchaparro4/contract_analyzer_analysis_ms

hostname -I | awk '{print $1}'