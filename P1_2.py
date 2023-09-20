from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(hosts=["http://localhost:9200"])  # Replace with your Elasticsearch server's address

@app.route('/add', methods=['POST'])
def add_to_elasticsearch():
    try:
        data = request.get_json()
        es.index(index='application_status', doc_type='status', body=data)
        return "Data added to Elasticsearch successfully", 201
    except Exception as e:
        return str(e), 500

@app.route('/healthcheck', methods=['GET'])
def get_healthcheck():
    try:
        # Query Elasticsearch to check if any application status is "DOWN"
        result = es.search(index='application_status', body={"query": {"term": {"application_status": "DOWN"}}})
        if result['hits']['total']['value'] > 0:
            return "DOWN", 200
        else:
            return "UP", 200
    except Exception as e:
        return str(e), 500

@app.route('/healthcheck/<service_name>', methods=['GET'])
def get_healthcheck_service(service_name):
    try:
        # Query Elasticsearch to check the status of a specific service
        result = es.search(index='application_status', body={"query": {"term": {"service_name": service_name}}})
        if result['hits']['total']['value'] > 0:
            return "DOWN", 200
        else:
            return "UP", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
