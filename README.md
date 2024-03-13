# GitHub API Wrapper

This Flask application serves as a wrapper for interacting with GitHub repositories through a set of defined endpoints. It allows users to perform various operations such as searching for repositories, creating new Gists, appending data to files, editing files, deleting files, and deleting entire repositories.

## Endpoints:

### 1. Root Endpoint

- **Description:** Returns a greeting message.
- **Method:** `GET`
- **Endpoint:** `/`
- **Sample Response (200 OK):**
  ```json
  {
    "message": "Hello, world!"
  }
  ```

### 2. Search Repositories

- **Description:** Searches for repositories on GitHub based on a given topic and optional language filter.
- **Method:** `GET`
- **Endpoint:** `/searchRepo`
- **Parameters:**
  - `topic` (required): The topic to search for.
  - `lang` (optional): The programming language to filter by.
- **Sample Response (200 OK):**
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

### 3. Delete Repository

- **Description:** Deletes an entire repository from GitHub.
- **Method:** `GET`
- **Endpoint:** `/deleteRepo`
- **Parameters:**
  - `repo` (required): The repository name.
  - `token` (required): Your GitHub token.
- **Sample Response (200 OK):**
  ```json
  {
    "code": 200,
    "message": "Repository deleted successfully"
  }
  ```

### 4. Create New Gist

- **Description:** Creates a new Gist on GitHub.
- **Method:** `GET`
- **Endpoint:** `/newGist`
- **Parameters:**
  - `newgist` (required): The filename of the Gist.
  - `code` (required): The content of the Gist.
  - `token` (required): Your GitHub token.
- **Sample Response (201 Created):**
  ```json
  {
    "code": 201,
    "message": "Gist created successfully",
    "gist_url": "https://gist.github.com/username/gist_id"
  }
  ```

### 5. Append to Repository

- **Description:** Appends data to an existing file in a repository on GitHub or creates a new file if it doesn't exist.
- **Method:** `GET`
- **Endpoint:** `/appendRepo`
- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to append to.
  - `append` (required): The data to append.
  - `token` (required): Your GitHub token.
- **Sample Response (200 OK):**
  ```json
  {
    "code": 200,
    "message": "File updated successfully"
  }
  ```

### 6. Edit File

- **Description:** Edits the content of a file in a repository on GitHub, overriding the existing content.
- **Method:** `POST`
- **Endpoint:** `/editFile`
- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to edit.
  - `token` (required): Your GitHub token.
- **Request Body:**
  ```json
  {
    "code": "New file content"
  }
  ```
- **Sample Response (200 OK):**
  ```json
  {
    "code": 200,
    "message": "File updated successfully"
  }
  ```

### 7. Delete File from Repository

- **Description:** Deletes a file from a repository on GitHub.
- **Method:** `GET`
- **Endpoint:** `/deleteFile`
- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to delete.
  - `token` (required): Your GitHub token.
- **Sample Response (200 OK):**
  ```json
  {
    "code": 200,
    "message": "File deleted successfully"
  }
  ```

### 8. Read Repository File

- **Description:** Reads the content of a file in a repository on GitHub.
- **Method:** `GET`
- **Endpoint:** `/readFile`
- **Parameters:**
  - `repo` (required): The repository name.
  - `filename` (required): The name of the file to read.
  - `token` (required): Your GitHub token.
- **Sample Response (200 OK):**
  ```json
  {
    "code": 200,
    "content": "File content"
  }
  ```
