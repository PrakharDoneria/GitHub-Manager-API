import requests
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, world!<p>'

@app.route('/searchRepo')
def search_repo_handler():
    if 'topic' in request.args:
        return search_github_repo()
    else:
        return jsonify({"code": 400, "message": "Invalid request: Missing topic parameter"})

@app.route('/deleteRepo')
def delete_repo_handler():
    repo_param = request.args.get('repo')
    token_param = request.args.get('token')

    if repo_param and token_param:
        url = f'https://api.github.com/repos/{repo_param}'
        headers = {'Authorization': f'token {token_param}'}

        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            return jsonify({"code": 200, "message": "Repository deleted successfully"})
        else:
            return jsonify({"code": response.status_code, "message": "Failed to delete repository on GitHub"})
    else:
        return jsonify({"code": 400, "message": "Missing parameters: repo or token"})


@app.route('/appendRepo')
def append_repo_handler():
    append_data = request.args.get('append')
    filename = request.args.get('filename')
    repo_param = request.args.get('repo')
    token_param = request.args.get('token')

    if append_data and filename and repo_param and token_param:
        existing_content = read_file_content(repo_param, filename, token_param)

        if existing_content is not None:
            new_content = existing_content + append_data
            return write_to_github_helper(repo_param, filename, new_content, token_param)
        else:
            # If the file doesn't exist, create a new one
            return write_to_github_helper(repo_param, filename, append_data, token_param)
    else:
        return jsonify({"code": 400, "message": "Missing parameters: append, filename, repo, or token"})

@app.route('/editFile', methods=['POST'])
def edit_file_handler():
    repo_param = request.args.get('repo')
    filename = request.args.get('filename')
    token_param = request.args.get('token')
    code = request.args.get('code')

    if repo_param and filename and token_param and code:
        return write_to_github_helper(repo_param, filename, code, token_param)
    else:
        return jsonify({"code": 400, "message": "Missing parameters: repo, filename, token, or code"})

@app.route('/newGist')
def create_new_gist():
    filename = request.args.get('newgist')
    code = request.args.get('code')
    token = request.args.get('token')

    if filename and code and token:
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
    else:
        return jsonify({"code": 400, "message": "Missing parameters: newgist, code, or token"})

# Helper functions

def search_github_repo():
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

def write_to_github_helper(repo, filename, content, token):
    data = {
        "message": "Updating file via API",
        "content": base64.b64encode(content.encode()).decode(),
        "sha": get_file_sha(repo, filename, token)
    }

    url = f'https://api.github.com/repos/{repo}/contents/{filename}'
    headers = {'Authorization': f'token {token}'}

    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 200:
        return jsonify({"code": 200, "message": "File updated successfully"})
    else:
        return jsonify({"code": response.status_code, "message": "Failed to update file on GitHub"})

def get_file_sha(repo, filename, token):
    url = f'https://api.github.com/repos/{repo}/contents/{filename}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('sha')
    else:
        return None

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

if __name__ == '__main__':
    app.run(debug=True)
