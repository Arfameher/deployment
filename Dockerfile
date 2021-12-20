# init a base image (Alpine is small Linux distro)
FROM python:3.8
# define the present working directory
WORKDIR /deployment
# copy the contents into the working dir
ADD . /deployment
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","flask_app.py"]