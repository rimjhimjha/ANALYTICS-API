## to create env:-

python -m venv analyticsapi

analyticsapi\Scripts\activate

## to download requirements

pip install -r requirements.txt


## DOCKER

'docker build -t analytics-api -f Dockerfile.web'

'docker run analytics-api'

## becomes

docker compose up --watch

docker compose down or docker compose down -v (to remove volumes)

docker compose run app /bin/bash or docker compose run app python

## github push

git add .
git commit -m "Your message"
git push

