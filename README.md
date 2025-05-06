# End2End_Text_Summarizer
[![workflow](https://github.com/KLTsai/End2End_Text_Summarizer/actions/workflows/main.yaml/badge.svg?branch=master&event=deployment_status)](https://github.com/KLTsai/End2End_Text_Summarizer/actions/workflows/main.yaml)

## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update configuration manager in `src/config`
5. Update `components` folder
6. Update `pipeline` folder
7. Update `main.py`
8. Update `app.py`

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/KLTsai/End2End_Text_Summarizer
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n textS python=3.10 -y
```

```bash
conda activate textS
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```




# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	# with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	# Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	# Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 750205244105.dkr.ecr.eu-north-1.amazonaws.com/e2e-texts

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:

### 🔧 Optional: Update your EC2 instance
#### These steps are optional, but it's a good idea to make sure your system is up to date:

```bash
sudo apt-get update -y
```
```bash
sudo apt-get upgrade
```	
### 🐳 Required: Install Docker
#### These steps are required to install and set up Docker:
#### 1. Download the Docker installation script:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```	
#### 2. Run the installation script:
```bash
sudo sh get-docker.sh
```	
#### 3. Add your user (e.g., `ubuntu`) to the Docker group:
```bash
sudo usermod -aG docker ubuntu
```	
#### 4. Apply the new group membership (run this in the same shell session):
```bash
newgrp docker
```	
> 💡 If you use a different username instead of ubuntu, make sure to update that in the command.

# 6. Configure EC2 as self-hosted runner:
### To set up your EC2 instance as a GitHub self-hosted runner, follow these steps:

#### 1. Go to your GitHub repository.

#### 2. Click on Settings → Actions → Runners.

#### 3. Click "New self-hosted runner".

#### 4. Select your operating system (e.g., Linux).

#### 5. Follow the instructions shown to run the following commands on your EC2 instance.


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = eu-north-1

    AWS_ECR_LOGIN_URI = demo>>  750205244105.dkr.ecr.eu-north-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app