# GitHub API Wrapper

This Flask application serves as a wrapper for various GitHub API endpoints, allowing users to interact with GitHub repositories.

## Endpoints:

### 1. `GET /`

- **Description:** Root endpoint returning a greeting message.

### 2. `GET /searchRepo`

- **Description:** Search for repositories on GitHub based on a given topic and language.

- **Parameters:**
  - `topic` (required): The topic to search for.
  - `lang` (optional): The programming language to filter by.

- **Usage:**
  ```http
  GET /searchRepo?topic=calculator&lang=javascript
  ```

- **Sample Success Response:**
  ```json
  {
      "code": 200,
      "message": "First repository found",
      "repository": {
          "name": "user/repo-name",
          "url": "https://github.com/user/repo-name"
      }
  }
  ```

- **Sample Error Response:**
  ```json
  {
      "code": 404,
      "message": "No repositories found for the given topic and language"
  }
  ```

### 3. `GET /newGist`

- **Description:** Create a new Gist on GitHub.

- **Parameters:**
  - `newgist` (required): The filename of the Gist.
  - `code` (required): The content of the Gist.
  - `token` (required): Your GitHub token.

- **Usage:**
  ```http
  GET /newGist?newgist=my_gist.py&code=print('Hello, world!')&token=your_token
  ```

- **Sample Success Response:**
  ```json
  {
      "code": 201,
      "message": "Gist created successfully",
      "gist_url": "https://gist.github.com/username/gist_id"
  }
  ```

- **Sample Error Response:**
  ```json
  {
      "code": 400,
      "message": "Missing parameters: newgist, code, or token"
  }
  ```

### 4. `GET /appendRepo`

- **Description:** Append data to an existing file in a repository on GitHub, or create a new file if it doesn't exist.

- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to append to.
  - `append` (required): The data to append.
  - `token` (required): Your GitHub token.

- **Usage:**
  ```http
  GET /appendRepo?repo=user/repo-name&filename=file.txt&append=New%20content&token=your_token
  ```

- **Sample Success Response:**
  ```json
  {
      "code": 200,
      "message": "File updated successfully"
  }
  ```

- **Sample Error Response:**
  ```json
  {
      "code": 404,
      "message": "Failed to update file on GitHub"
  }
  ```

### 5. `POST /editFile`

- **Description:** Edit the content of a file in a repository on GitHub, overriding the existing content.

- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to edit.
  - `token` (required): Your GitHub token.
  - `code` (required): The new content of the file.

- **Usage:**
  ```http
  POST /editFile?repo=user/repo-name&filename=file.txt&token=your_token
  ```

- **Sample Success Response:**
  ```json
  {
      "code": 200,
      "message": "File updated successfully"
  }
  ```

- **Sample Error Response:**
  ```json
  {
      "code": 404,
      "message": "Failed to update file on GitHub"
  }
  ```

### 6. `GET /deleteRepo`

- **Description:** Delete an entire repository from GitHub.

- **Parameters:**
  - `repo` (required): The repository name.
  - `token` (required): Your GitHub token.

- **Usage:**
  ```http
  GET /deleteRepo?repo=user/repo-name&token=your_token
  ```

- **Sample Success Response:**
  ```json
  {
      "code": 200,
      "message": "Repository deleted successfully"
  }
  ```

- **Sample Error Response:**
  ```json
  {
      "code": 404,
      "message": "Failed to delete repository on GitHub"
  }
  ```

### 7. `GET /readFile`

- **Description:** Read the content of a file in a repository on GitHub.

- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to read.
  - `token` (required): Your GitHub token.

- **Usage:**
  ```http
  GET /readFile?repo=user/repo-name&filename=file.txt&token=your_token
  ```

- **Sample Success Response:**
  ```json
  {
      "code": 200,
      "content": "File content goes here"
  }
  ```

- **Sample Error Response:**
  ```json
  {
      "code": 404,
      "message": "File not found in the repository"
  }
  ```