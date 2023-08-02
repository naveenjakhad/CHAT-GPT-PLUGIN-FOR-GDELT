from waitress import serve


from flask import Flask, jsonify, request,send_from_directory
import requests

app = Flask(__name__)

def get_articles(keyword):
    base_url = "https://api.gdeltproject.org/api/v1/search_ftxtsearch/search_ftxtsearch"
    params = {
        "query": keyword,
        "output": "artlist",
        "dropdup": "true"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.text.split('\n')
    else:
        return None

@app.route('/gdelt_search', methods=['GET'])
def gdelt_search():
    keyword = request.args.get('keyword', default = 'india', type = str)
    articles = get_articles(keyword)
    if articles:
        return jsonify(articles)
    else:
        return jsonify({"message": "No articles found for keyword: " + keyword})

#https://textkeywordchat-gpt-plugin.naveenjakhad1.repl.co/.well-known/ai-plugin.json
@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')

#https://textkeywordchat-gpt-plugin.naveenjakhad1.repl.co/.well-known/openapi.yaml
@app.route('/.well-known/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == '__main__':
    serve(app,host="0.0.0.0",port=8080)
  

