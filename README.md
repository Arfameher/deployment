# Steam Dataset Analysis --  Deployment-flask-heroku  
To give a brief itroduction of this project you can refer to the description below.
- `Deployment strategy` :
  - GitHub page - code with data cleaning and analysis.
  - Heroku - Deployed webpage
  - https://steam-games-analysis.herokuapp.com/
  - Jupyter Notebook - 
  - Python file
<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ30L8aV7_xXsF65jwQYIbIgGSoXFhBWgclpA&usqp=CAU" />
</p>

***
### Description
To visualize some interesting aspects about this scraped steam data. Here is a json file containing data on some 4000 odd games sold on the popular digital games storefront steam. Performing data cleaning, exploration and visualization on the given dataset in jupyter notebook and deploy a web page showing an interactive model on heroku. 

Objectives of the Project :
<p align="center">
  <img src="https://github.com/Arfameher/deployment/blob/main/static/Screenshot%20from%202021-12-26%2022-29-07.png?raw=true" />
</p>

***
### Installation
To run this code you need to have anaconda installed in your system and jupyter notebook running with basic libraries or Python IDE such as [Visual Studio Code](https://code.visualstudio.com/)

To run this code you have to clone the repository or download it as a zip file and run it. But before that we need to install some libraries to run this code.

- Create virtual environment to run this code. 
    - If you are using anaconda --> `conda create -n <yourenvname> python=x.x anaconda`
    - Activate your virtual environment -->
    `conda activate <yourenvname>`

- Now we will have to download libraries that are specifically used for this code to run and to read and write a GeoTiff file or a shape file. All these libraries are written in reuirements.txt file.
To install all these libraries do the folling steps:

    1. cd to the directory where `requirements.txt` is located
    2. run the command in your shell: 
        ```javascript
        pip install -r requirements.txt
        ``` 
***
### Running the project

1. Once you are through with the installation, Ensure that you are in the project home directory. Run `flask_app.py` using below command to start Flask API
    ```javascript
    python flask_app.py
    ```
2. By default, flask will run on port 5000.
    ```javascript
    Navigate to URL http://localhost:5000
    ```
You should be able to view the homepage as below:
<p align="center"><img src="https://github.com/Arfameher/deployment/blob/main/static/Screenshot%20from%202021-12-28%2011-12-20.png?raw=true"/>
</p>

You are now able to view a navigation menu --> 

Home - which displays a table with information on all the games with genre, release date and price in EUR.

Insights - which displays some of the insights that i have found from the dataset.

3. You can also view the deployed webpage on heroku by clicking on the link below :
    ```javascript
    https://steam-games-analysis.herokuapp.com/
    ```

***
### Repo Architecture
#### Dataset 
- Contains the clean dataset of games required for analysis in a csv file format.

#### templates 
- Contains the templates of html required to deploy the web page using flask.

#### Jupyter notebook 
- `01.Create_database.ipynb` : To parse json file and read it in SQL database format.
- `02.Steam_Data_Cleaning.ipynb` : To clean the dataset and extract the values from the dictionaries within.
- `03.Data_Visualization.ipynb` : To visualize the clean dataset and extract the valuable insights.

#### Python file 
- `create_database.py` : Python file parse json file and read it in SQL database format.
- `flask_app_MVP.py` : Deployed the basic MVP to test. 
- `flask_app.py` : Python file that creates a webpage and then build a docker image and deploy it on heroku.

#### requirements.txt 
- Gives all the required libraries to run this code. Also required to deploy the web page online if we deploy through github.

#### Dockerfile

#### Procfile
OK, one more necessary plaintext file: Heroku needs a file to tell it how to start up the web app. By convention, this file is just a plaintext file is called (and named): Procfile:

    A Procfile is a text file in the root directory of your application that defines process types and explicitly declares what command should be executed to start your app.

And for now, Procfile can contain just this line:

`web: gunicorn app:app flask_app`

#### heroku.yml 

***
### Visuals
<p align="center"><img src="https://github.com/Arfameher/deployment/blob/main/static/Screenshot%20from%202021-12-28%2011-08-26.png?raw=true"/>
</p>

<p align="center"><img src="https://github.com/Arfameher/deployment/blob/main/static/Screenshot%20from%202021-12-28%2011-08-35.png?raw=true"/>
</p>

***
### References
Referred to the docs of flask, heroku and docker.
https://devcenter.heroku.com/categories/deploying-with-docker

https://flask-doc.readthedocs.io/en/latest/

https://docs.docker.com/

***
### Contributors
There are no contributors as of now, this is a solo project. If you wish to contribute to this repo, you are Welcome!
You can clone this repository and create a new branch and push your changes.

***
### Timeline
Dec 2021

Time limit: 2 weeks --> 15/12/2021 - 27/12/2021 

This is a solo project given to us at [BeCode](https://becode.org/) after completion of our study material related to deployment where we learnt how to use `flask`, `docker` and `heroku`.
I would like to further improve this project by doing more analysis on the dataset.

***
### Personal Situation
This is a solo project given to me at [BeCode](https://becode.org/)
I am currently aspiring to be a Data Scientist. This is a Deployment project where I have used python library such as Flask to create my webpage and deployed it using docker and heroku.

Here is how you can contact me :

LinkedIn : [Arfameher](https://www.linkedin.com/in/arfa-meher/)  
Email : arfaameher@outlook.com

Here is how you can have a look at my WebPage created for the data analysis of the Steam Dataset : 

https://steam-games-analysis.herokuapp.com/

