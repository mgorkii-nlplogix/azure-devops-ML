[![Python application test with Github Actions](https://github.com/mgorkii-nlplogix/azure-devops-ML/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/mgorkii-nlplogix/azure-devops-ML/actions/workflows/pythonapp.yml)

[![Build Status](https://dev.azure.com/mgorki/flask-ml-app-deploy/_apis/build/status/mgorkii-nlplogix.azure-devops-ML?branchName=main)](https://dev.azure.com/mgorki/flask-ml-app-deploy/_build/latest?definitionId=3&branchName=main)

# Overview
This project uses Git Hub Actions to test if the script is healthy and build a CI piplene. It also uses Azure piplines to build CD pipeline. 

## Project Plan
[Trello board](https://trello.com/b/EsRMtX99/devops-pipeline) 


[Project Managment Spreadsheet](https://github.com/mgorkii-nlplogix/azure-devops-ML/blob/main/project-management.xlsx)

## Instructions
 
### Architectural Diagram: 
![Projet Diagram](https://user-images.githubusercontent.com/82521640/139153485-6cb3ce0b-a007-49a4-9016-90a48b0d7269.png)

### Add ssh key to GitHub 

Open your Azure CLI and create an SSH key using the following command: 
```
ssh-keygen -t rsa
```
You will be asked to provide the key path - you can skip it. Remember the file name where the key is saved to 
Now open the key file and copy it's content: 
```
cat ~/.ssh/id_<file name>.pub
```
Open you GitHub page and go to settings-SSH and GPG keys - New SSH Key. Name the new key, past the .pub file content and save it. 
Now you should be able to clone the project. 

### Clone the project 

cd to the folder you want to clone the project to and run the following command: 
```
git clone git@github.com:mgorkii-nlplogix/azure-devops-ML.git
```
![image](https://user-images.githubusercontent.com/82521640/139696520-e44c0223-f2df-404c-a628-c44dd0665608.png)

### GitHub Actions

Once you push any changes to GitHub you can check the test results. Go to the repo page on GitHub and click actions 

![image](https://user-images.githubusercontent.com/82521640/140065390-1e241378-5b96-4adc-8990-501ff3627e80.png)


### Run project in Azure Webapp Service
To create the app service with minimum storage run the following command: 
```
az webapp up --sku F1 --name flask-ml-app
```
It will create and run an app named "flask-ml-app"
You can check if the app is running ny opening the following url in the browser: 

![image](https://user-images.githubusercontent.com/82521640/139700814-b8a5a6a0-548c-48eb-ad90-d1d251679f43.png)

Open the file make_predict_azure_app.sh and replace the POST url with url of your service.

### Create virtual env
Run the following command : 
```
make setup
```
It will create a vitrual environment in /.udacity-devops folder
To activate the venv run the follwoing command: 

```
source ~/.udacity-devops/bin/activate
```
Run the following command to run the full setup and test: 

```
make all
```
![image](https://user-images.githubusercontent.com/82521640/139702011-b1f881d2-88a8-42b5-a0bc-20d3c7170e24.png)


### Test an application using Locust (swarm the target website from localhost)

Source your venv: 

```
source ~/.udacity-devops/bin/activate
```
Install locust: 
```pip install locust
```
run 
```
locust
```
Open localhost:8089. Make sure to open that exact url.

![image](https://user-images.githubusercontent.com/82521640/140084201-8512b159-3ca3-4b79-93af-71189ba51ce3.png)

![image](https://user-images.githubusercontent.com/82521640/140084664-80584a61-39d6-4f8e-a6e6-e6375eef1fd5.png)


### Deploy project in Azure Pipelines
open dev.azure.com and click "New project"
![image](https://user-images.githubusercontent.com/82521640/139725127-33b632a7-3607-495b-a04b-f389526cbc8b.png)
Create a new project and go to "settings" - "service connections" - "new service connections" - "azure resourse manager"
![image](https://user-images.githubusercontent.com/82521640/139725729-94cd8cdd-c838-4131-b4f6-752dd8b9956d.png)
Choose "Service principal" - "Subscription". Choose your Subscription, Resource group, Service connection name. Grant access permissions to all pipelines. 

Go back to your account and choose "Pipelines" - "Pipelines" - "Create Pipeline"
![image](https://user-images.githubusercontent.com/82521640/139727441-df1dc4b1-af7f-4121-ad7d-3c21e0302e6b.png)

Create a GitHub Integration 
![image](https://user-images.githubusercontent.com/82521640/139727532-a09ab4f0-3859-40ca-b9dc-0f0b6700047c.png)

Configure Python to Linux Web App on Azure
![image](https://user-images.githubusercontent.com/82521640/139727566-17808782-424d-4b51-8e1e-f9dc76e147a1.png)

Once your pipline is set up you can check all the recent runs: 

![image](https://user-images.githubusercontent.com/82521640/139727776-987b85dc-5ac2-4458-968f-352f713a64ef.png)
![image](https://user-images.githubusercontent.com/82521640/139727818-7ebcf54a-00e7-46a6-92b0-8f83d6d6f749.png)
![image](https://user-images.githubusercontent.com/82521640/139727847-8b0082ea-2039-4cff-ba77-6da713464efb.png)

Check the if the project succesfully deployed: 
![image](https://user-images.githubusercontent.com/82521640/140066017-b3c7058a-25c8-4412-b49e-02121440018e.png)


### Check the predict

To check the prediction run the script in power shell: 
```
./make_predict_azure_app.sh
```
![image](https://user-images.githubusercontent.com/82521640/139728348-f3c33f19-c667-4474-baa2-a2cb76755654.png)

### Enhancements
Might apply more security policies 
Deploy a Kubernetes version in Azure
Set up log trail 
Set up Monitoring alerts 
Set up Budgeting in Azure 

Demo

[demo link](https://youtu.be/z9cosUpexhk)
