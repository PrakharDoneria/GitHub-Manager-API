# Using the Git API

This API provides various endpoints to interact with GitHub's API for repository and Gist management.

## Endpoints

### 1. Search GitHub Repository

#### Endpoint: `/git?search={topic}&lang={language}`

**Description:** Search for GitHub repositories based on a topic and an optional language.

**Usage:**
- Send a GET request to the endpoint `/git?search={topic}&lang={language}`.
- Replace `{topic}` with the topic you want to search for and `{language}` (optional) with the programming language.
- Example: `/git?search=python&lang=javascript`

**Possible Responses:**
```json
{
  "code": 200,
  "message": "First repository found",
  "repository": {
    "name": "user/repo",
    "url": "https://github.com/user/repo"
  }
}
```
```json
{
  "code": 404,
  "message": "No repositories found for the given topic and language"
}
```

### 2. Create New Gist

#### Endpoint: `/git?newgist={filename}&code={code}&token={token}`

**Description:** Create a new Gist on GitHub with the specified filename and code content.

**Usage:**
- Send a GET request to the endpoint `/git?newgist={filename}&code={code}&token={token}`.
- Replace `{filename}` with the name of the file to be created, `{code}` with the code content, and `{token}` with your GitHub personal access token.
- Example: `/git?newgist=myfile.py&code=print("Hello, world!")&token=your_token_here`

**Possible Responses:**
```json
{
  "code": 201,
  "message": "Gist created successfully",
  "gist_url": "https://gist.github.com/username/abcdef1234567890"
}
```

### 3. Read File from GitHub Repository

#### Endpoint: `/git?read={filename}&repo={repository}&token={token}`

**Description:** Read the content of a file from a GitHub repository.

**Usage:**
- Send a GET request to the endpoint `/git?read={filename}&repo={repository}&token={token}`.
- Replace `{filename}` with the name of the file to read, `{repository}` with the name of the repository, and `{token}` with your GitHub personal access token.
- Example: `/git?read=myfile.py&repo=user/repo&token=your_token_here`

**Possible Responses:**
```json
{
  "code": 200,
  "content": "File content here..."
}
```
```json
{
  "code": 404,
  "message": "File not found in the repository"
}
```
```json
{
  "code": 401,
  "message": "Unauthorized access to the repository"
}
```

### 4. Write File to GitHub Repository

#### Endpoint: `/git?write={data}&filename={filename}&repo={repository}&token={token}`

**Description:** Write data to a file in a GitHub repository.

**Usage:**
- Send a GET request to the endpoint `/git?write={data}&filename={filename}&repo={repository}&token={token}`.
- Replace `{data}` with the content to write, `{filename}` with the name of the file to write to, `{repository}` with the name of the repository, and `{token}` with your GitHub personal access token.
- Example: `/git?write=NewContent&filename=myfile.py&repo=user/repo&token=your_token_here`

**Possible Responses:**
```json
{
  "code": 200,
  "message": "File updated successfully"
}
```
```json
{
  "code": 404,
  "message": "File not found in the repository"
}
```
```json
{
  "code": 401,
  "message": "Unauthorized access to the repository"
}
```

### 5. Append to File in GitHub Repository

#### Endpoint: `/git?append={data}&filename={filename}&repo={repository}&token={token}`

**Description:** Append data to the end of a file in a GitHub repository.

**Usage:**
- Send a GET request to the endpoint `/git?append={data}&filename={filename}&repo={repository}&token={token}`.
- Replace `{data}` with the content to append, `{filename}` with the name of the file to append to, `{repository}` with the name of the repository, and `{token}` with your GitHub personal access token.
- Example: `/git?append=NewContent&filename=myfile.py&repo=user/repo&token=your_token_here`

**Possible Responses:**
```json
{
  "code": 200,
  "message": "File updated successfully"
}
```
```json
{
  "code": 404,
  "message": "File not found in the repository"
}
```
```json
{
  "code": 401,
  "message": "Unauthorized access to the repository"
}
```

### 6. Delete File from GitHub Repository

#### Endpoint: `/git?del={filename}&repo={repository}&token={token}`

**Description:** Delete a file from a GitHub repository.

**Usage:**
- Send a GET request to the endpoint `/git?del={filename}&repo={repository}&token={token}`.
- Replace `{filename}` with the name of the file to delete, `{repository}` with the name of the repository, and `{token}` with your GitHub personal access token.
- Example: `/git?del=myfile.py&repo=user/repo&token=your_token_here`

**Possible Responses:**
```json
{
  "code": 200,
  "message": "File deleted successfully"
}
```
```json
{
  "code": 404,
  "message": "File not found in the repository"
}
```
```json
{
  "code": 401,
  "message": "Unauthorized access to the repository"
}
```