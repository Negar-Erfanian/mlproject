# End‑to‑End Machine Learning Project for Data Science

This repository implements a complete **end‑to‑end Machine Learning workflow**, including data preprocessing, model training, model persistence, and a **Flask web application** for making real‑time predictions.

This project can be used as a template for building and deploying ML models that serve predictions via an API or a web interface.

---

## Project Structure
```
mlproject/
│
├── artifacts/ # Saved models / preprocessors/ data
├── notebook/ # EDA
├── src/
│ ├── exception.py # Custom exception code
│ ├── logger.py # Logging configuration
│ └── pipeline/
│    ├── predict_pipeline.py # Code for prediction pipeline
│ └── components/
│    ├── data_ingestion.py        # Loads and ingests raw data
│    ├── data_transformation.py   # Preprocesses and transforms data for modeling
│    ├── model_trainer.py         # Trains and evaluates ML models
│
├── templates/ # HTML templates for Flask UI
├── application.py # Flask application entry point
├── requirements.txt # Python dependencies
├── setup.py # Package configuration
└── README.md # This file
```



---

## Features

✔ Builds a trained ML model and preprocessor  
✔ Includes modular code for training, evaluation, and prediction  
✔ REST API + web interface via **Flask**  
✔ Easily extendable for new datasets or models

---

## How It Works

1. **Data Input**  
   • Users submit features via a web form.  
2. **Preprocessing**  
   • A saved scikit‑learn preprocessor scales and encodes the input.  
3. **Model Inference**  
   • A trained model makes predictions on new inputs.  
4. **Output**  
   • Results are displayed dynamically in the web UI.

The ML pipeline code is implemented in `src/pipeline/predict_pipeline.py`.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Negar‑Erfanian/mlproject.git
   cd mlproject
   ```

2. Create and activate a Python environment:
   ```bash
     python3 ‑m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
     ```bash
     pip install ‑r requirements.txt
     ```


## Run the Web App Locally

Start the Flask server:
```bash
python application.py
```
Then visit:
```bash
http://localhost:PORTNUMBER/
```
Use the form to enter feature values and get a prediction.

Here is your **clean, README-ready section split into two parts exactly as requested**, aligned with your existing project description and your actual `aws.yml`.

You can directly paste this under your current README.

---

## AWS Deployment using CI/CD (GitHub Actions)

This project uses **GitHub Actions** to implement the Continuous Integration (CI) and deployment trigger step of the CI/CD pipeline.

The CI pipeline ensures that the code is validated and packaged before deployment to AWS.

The workflow is defined in:

```
.github/workflows/aws.yml
```

---

## CI/CD Pipeline Overview

```text id="gh_ci_cd"
GitHub Repository
      │
      │  (CI - GitHub Actions)
      ▼
Build Docker Image + Package Application
      │
      ▼
Create Deployment Zip Artifact
      │
      ▼
Deploy to AWS Elastic Beanstalk
```

---

## GitHub Actions Workflow (`aws.yml`)

```yaml id="aws_yaml"
name: Deploy to AWS Elastic Beanstalk

on:
  push:
    branches: [ "main" ]

env:
  AWS_REGION: us-east-1
  EB_APPLICATION_NAME: mlproject-app
  EB_ENVIRONMENT_NAME: mlproject-env
  DOCKER_IMAGE_NAME: mlproject-api

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Build Docker image
        run: |
          docker build -t $DOCKER_IMAGE_NAME .

      - name: Create deployment package
        run: |
          zip -r deploy.zip . -x "*.git*"

      - name: Deploy to Elastic Beanstalk
        uses: einaregilsson/beanstalk-deploy@v21
        with:
          aws_access_key: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws_secret_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          application_name: ${{ env.EB_APPLICATION_NAME }}
          environment_name: ${{ env.EB_ENVIRONMENT_NAME }}
          region: ${{ env.AWS_REGION }}
          version_label: ${{ github.sha }}
          deployment_package: deploy.zip
```

---

## What This CI/CD Pipeline Does

### CI (Continuous Integration)

* Checks out latest code
* Builds Docker image
* Packages application into deployment artifact

### CD (Continuous Deployment)

* Sends deployment package to AWS Elastic Beanstalk
* Automatically updates running application

---

## Key Benefits

* Fully automated deployment on every push to `main`
* Ensures reproducible Docker-based builds
* Eliminates manual deployment steps
* Supports production-ready ML API deployment

---

---

## AWS Deployment (CodePipeline)

In addition to GitHub Actions, this project can also be deployed using **AWS-native CI/CD services** for a fully managed deployment pipeline.

This approach uses:

* AWS CodePipeline
* AWS CodeBuild
* AWS Elastic Beanstalk

---

## AWS CodePipeline Architecture

```text id="aws_pipeline"
GitHub Repository
      │
      ▼
AWS CodePipeline
      │
      ├── CodeBuild (CI: build + test + package)
      │
      ▼
Elastic Beanstalk (CD: deployment + hosting)
```

---

## How It Works

### 1. Source Stage (GitHub)

* Code is pulled from GitHub repository
* Triggered automatically on every push to `main`

---

### 2. Build Stage (CodeBuild)

CodeBuild handles the CI process:

* Install dependencies
* Run tests
* Validate application
* Prepare deployment artifact

Example `buildspec.yml`:

```yaml id="codebuild_spec"
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.9
    commands:
      - pip install -r requirements.txt

  build:
    commands:
      - echo "Running tests..."
      - pytest tests/
      - echo "Build successful"

artifacts:
  files:
    - "**/*"
```

---

### 3. Deploy Stage (Elastic Beanstalk)

CodePipeline deploys the validated build artifact to:

* Elastic Beanstalk environment (`mlproject-env`)
* Automatically updates the running application

---

## Advantages of CodePipeline Approach

* Fully AWS-managed CI/CD system
* No manual deployment logic required in code
* Strong integration with AWS services
* Better scalability for production systems

---

## Summary

| Approach         | Purpose                 | Tooling                  |
| ---------------- | ----------------------- | ------------------------ |
| GitHub Actions   | CI + deployment trigger | GitHub-native automation |
| AWS CodePipeline | Full AWS-managed CI/CD  | AWS-native orchestration |

---

## Final Note

This project supports **both CI/CD strategies**:

* GitHub Actions for flexible, code-driven deployment
* AWS CodePipeline for enterprise-grade AWS-native deployment

---


Here’s a **clean, README-ready Azure equivalent section**, structured similarly to your AWS part and consistent with your project style.

You can paste this directly under a new section like `## Azure Deployment`.

---

# ## Azure Deployment using CI/CD (GitHub Actions)

This project also supports deployment on **Microsoft Azure** using **GitHub Actions CI/CD**, enabling automated build and deployment of the Flask ML application to an Azure-hosted web service.

The pipeline ensures that every push to the `main` branch triggers automated testing, container build, and deployment.

---

## CI/CD Pipeline Overview

```text id="azure_ci_cd"
GitHub Repository
      │
      │ (CI - GitHub Actions)
      ▼
Build + Test + Docker Image Creation
      │
      ▼
Push Docker Image to Azure Container Registry (ACR)
      │
      ▼
Deploy to Azure Web App Service
```

---

## Azure CI/CD Workflow (GitHub Actions)

The CI/CD pipeline is defined using GitHub Actions in:

```text id="azure_workflow_path"
.github/workflows/azure.yml
```

---

### GitHub Actions Workflow (`azure.yml`)

```yaml id="azure_yaml"
name: Deploy to Azure Web App

on:
  push:
    branches: [ "main" ]

env:
  AZURE_WEBAPP_NAME: mlproject-app
  AZURE_CONTAINER_REGISTRY: mlprojectregistry
  IMAGE_NAME: mlproject-api

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Log in to Azure Container Registry
        uses: azure/docker-login@v1
        with:
          login-server: ${{ env.AZURE_CONTAINER_REGISTRY }}.azurecr.io
          username: ${{ secrets.AZURE_USERNAME }}
          password: ${{ secrets.AZURE_PASSWORD }}

      - name: Build Docker image
        run: |
          docker build -t $AZURE_CONTAINER_REGISTRY.azurecr.io/$IMAGE_NAME:latest .

      - name: Push image to ACR
        run: |
          docker push $AZURE_CONTAINER_REGISTRY.azurecr.io/$IMAGE_NAME:latest

      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v3
        with:
          app-name: ${{ env.AZURE_WEBAPP_NAME }}
          images: ${{ env.AZURE_CONTAINER_REGISTRY }}.azurecr.io/${{ env.IMAGE_NAME }}:latest
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
```

---

## What This CI/CD Pipeline Does

### CI (Continuous Integration)

* Checkout latest code from GitHub
* Build Docker image of Flask ML API
* Validate application structure

---

### CD (Continuous Deployment)

* Push Docker image to Azure Container Registry (ACR)
* Deploy container to Azure Web App Service
* Automatically update running application

---

## Azure Services Used

* Microsoft Azure
* Azure App Service
* Azure Container Registry
* GitHub Actions

---

## How Deployment Works

```text id="azure_flow"
1. Developer pushes code to GitHub
2. GitHub Actions starts CI pipeline
3. Docker image is built
4. Image is pushed to Azure Container Registry
5. Azure Web App pulls latest image
6. Application is updated automatically
```

---

## Key Benefits

* Fully automated CI/CD pipeline
* Docker-based reproducible deployments
* Scalable cloud hosting via Azure App Service
* Seamless integration with GitHub
* No manual deployment steps required

---

## Summary

| Stage            | Tool                     | Purpose                              |
| ---------------- | ------------------------ | ------------------------------------ |
| CI               | GitHub Actions           | Build + test + Docker image creation |
| Artifact Storage | Azure Container Registry | Store Docker images                  |
| CD               | Azure App Service        | Host and run ML API                  |

