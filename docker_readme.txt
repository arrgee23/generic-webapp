docker build -t flask-sql-app .

# running in local
docker run -d -p 8080:8080 --name my-container flask-sql-app

Log in to Docker Hub:

    docker login

Tag your Docker image:

    docker tag flask-sql-app dockerahul187/flask-sql-app:latest

Push the Docker image:

    docker push dockerahul187/flask-sql-app:latest
