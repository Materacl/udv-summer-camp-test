# udv-summer-camp-test
Test Assignment for the Python Developer Position at UDV Summer Camp

## 🚀 Installation & Deployment

### 📌 Prerequisites
To run the project, ensure you have:
- 🐳 [Docker](https://www.docker.com/)
- 🛠️ [Make](https://www.gnu.org/software/make/)

### ▶️ Running in Development Mode
```sh
make up
```
Starts the application in a Docker container.

### ⏹️ Stopping the Development Environment
```sh
make down
```

### 🔥 Running in Production Mode
```sh
make up-prod
```
Starts the production-ready version of the application.

### ❌ Stopping the Production Environment
```sh
make down-prod
```

### 📦 Installing Dependencies
```sh
make install-deps
```

### 🔍 Running Linter & Formatting Code
```sh
make lint
make format
```

### 🧪 Running Tests
```sh
make test
```

### 🚀 Starting the Application
```sh
make start
```

## 📚 API Documentation
The API is documented using OpenAPI and can be explored via [Swagger Editor](https://editor-next.swagger.io) using the provided `openapi.json` file.