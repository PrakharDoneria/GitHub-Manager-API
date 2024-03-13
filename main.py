import requests
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, world!<p>'

@app.route('/searchRepo')
def search_repo():
    if 'topic' not in request.args:
        return jsonify({"code": 400, "message": "Missing topic parameter"})
    topic = request.args.get('topic')
    language = request.args.get('lang', 'all')

    url = f'https://api.github.com/search/repositories?q={topic}+language:{language}&sort=stars&order=desc'

    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json().get('items', [])
        if repos:
            first_repo = repos[0]
            repo_name = first_repo.get('full_name', '')
            repo_url = first_repo.get('html_url', '')
            return jsonify({"code": 200, "message": "First repository found", "repository": {"name": repo_name, "url": repo_url}})
        else:
            return jsonify({"code": 404, "message": "No repositories found for the given topic and language"})
    else:
        return jsonify({"code": response.status_code, "message": "Failed to fetch repositories from GitHub"})

@app.route('/deleteRepo')
def delete_repo():
    if 'repo' not in request.args or 'token' not in request.args:
        return jsonify({"code": 400, "message": "Missing repo or token parameter"})
    repo = request.args.get('repo')
    token = request.args.get('token')

    url = f'https://api.github.com/repos/{repo}'
    headers = {'Authorization': f'token {token}'}

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        return jsonify({"code": 200, "message": "Repository deleted successfully"})
    else:
        return jsonify({"code": response.status_code, "message": "Failed to delete repository on GitHub"})

@app.route('/newGist')
def create_new_gist():
    if 'newgist' not in request.args or 'code' not in request.args or 'token' not in request.args:
        return jsonify({"code": 400, "message": "Missing newgist, code, or token parameter"})
    filename = request.args.get('newgist')
    code = request.args.get('code')
    token = request.args.get('token')

    files = {filename: {'content': code}}
    data = {"files": files, "public": True}

    url = 'https://api.github.com/gists'
    headers = {'Authorization': f'token {token}'}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        gist_url = response.json().get('html_url', '')
        return jsonify({"code": 201, "message": "Gist created successfully", "gist_url": gist_url})
    else:
        return jsonify({"code": response.status_code, "message": "Failed to create Gist on GitHub"})

@app.route('/appendRepo')
def append_to_repository():
    if 'repo' not in request.args or 'filename' not in request.args or 'append' not in request.args or 'token' not in request.args:
        return jsonify({"code": 400, "message": "Missing repo, filename, append, or token parameter"})
    repo = request.args.get('repo')
    filename = request.args.get('filename')
    append_data = request.args.get('append')
    token = request.args.get('token')

    existing_content = read_file_content(repo, filename, token)

    if existing_content is not None:
        new_content = existing_content + append_data
        write_response = write_to_repository(repo, filename, new_content, token)
        return jsonify(write_response)
    else:
        return jsonify({"code": 404, "message": "File not found in the repository"})

@app.route('/editFile', methods=['POST'])
def edit_file():
    if 'repo' not in request.args or 'filename' not in request.args or 'token' not in request.args or 'code' not in request.json:
        return jsonify({"code": 400, "message": "Missing repo, filename, token, or code parameter"})
    repo = request.args.get('repo')
    filename = request.args.get('filename')
    token = request.args.get('token')
    new_content = request.json['code']

    write_response = write_to_repository(repo, filename, new_content, token)
    return jsonify(write_response)

@app.route('/deleteFile')
def delete_file():
    if 'repo' not in request.args or 'filename' not in request.args or 'token' not in request.args:
        return jsonify({"code": 400, "message": "Missing repo, filename, or token parameter"})
    repo = request.args.get('repo')
    filename = request.args.get('filename')
    token = request.args.get('token')

    url = f'https://api.github.com/repos/{repo}/contents/{filename}'
    headers = {'Authorization': f'token {token}'}

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return jsonify({"code": 200, "message": "File deleted successfully"})
    else:
        return jsonify({"code": response.status_code, "message": "Failed to delete file on GitHub"})

@app.route('/readFile')
def read_file():
    if 'repo' not in request.args or 'filename' not in request.args or 'token' not in request.args:
        return jsonify({"code": 400, "message": "Missing repo, filename, or token parameter"})
    repo = request.args.get('repo')
    filename = request.args.get('filename')
    token = request.args.get('token')

    file_content = read_file_content(repo, filename, token)

    if file_content is not None:
        return jsonify({"code": 200, "content": file_content})
    else:
        return jsonify({"code": 404, "message": "File not found in the repository"})

def read_file_content(repo, filename, token):
    url = f'https://api.github.com/repos/{repo}/contents/{filename}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_content = response.json().get('content', '')
        file_content = base64.b64decode(file_content).decode('utf-8')
        return file_content
    else:
        return None

def write_to_repository(repo, filename, content, token):
    data = {
        "message": "Updating file via API",
        "content": base64.b64encode(content.encode()).decode(),
        "sha": get_file_sha(repo, filename, token)
    }

    url = f'https://api.github.com/repos/{repo}/contents/{filename}'
    headers = {'Authorization': f'token {token}'}

    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 200:
        return {"code": 200, "message": "File updated successfully"}
    else:
        return {"code": response.status_code, "message": "Failed to update file on GitHub"}

def get_file_sha(repo, filename, token):
    url = f'https://api.github.com/repos/{repo}/contents/{filename}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('sha')
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
