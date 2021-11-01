[![Python application test with Github Actions](https://github.com/mgorkii-nlplogix/azure-devops-ML/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/mgorkii-nlplogix/azure-devops-ML/actions/workflows/pythonapp.yml)

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

<TODO: Instructions for running the Python project. How could a user with no context run this project without asking you for any help. Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

Project running on Azure App Service

Project cloned into Azure Cloud Shell

Passing tests that are displayed after running the make all command from the Makefile

Output of a test run

Successful deploy of the project in Azure Pipelines. Note the official documentation should be referred to and double checked as you setup CI/CD.

Running Azure App Service from Azure Pipelines automatic deployment

Successful prediction from deployed flask app in Azure Cloud Shell. Use this file as a template for the deployed prediction. The output should look similar to this:

udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
Output of streamed log files from deployed application
Enhancements
<TODO: A short description of how to improve the project in the future>

Demo
<TODO: Add link Screencast on YouTube>
