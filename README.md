# news-web-search
Backend that simulates a custom news web search engine.

## Dependencies:
- python==3.8
- postgresql==11
- flask==1.1.2
- flask-sqlalchemy==2.4.1

## Requirements:

* [Docker](https://docs.docker.com/engine/installation/).
* [Docker-compose](https://docs.docker.com/compose/install).

## Install:
* Clone the repository
```shell
$ git clone https://github.com/pixelead0/news-web-search.git
```
* Create and edit configuration files.
```shell
$ sh config.sh
```

* Run docker-compose to start the containers:
```shell
$ docker-compose up
```

* Send post request
```shell
curl -X POST \
  http://0.0.0.0:5000/api/news \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{"keywords": ["word1","word2"]
}'
```
> Change `word1` and `word2` for your search.


## Specifications:
This backend include a **RESTful API** with the following characteristics:

 - [X] It must expose an endpoint is exposed through a ** POST ** method;  e.g `/api/news`
 - [X] Any other case must return an error.
 - [X] The input of the API it's a JSON with one property called ​ **`keywords`** and its value is an array of n words (in Spanish) using the following format:

```json
{
"keywords": [ "one", "two", "three", "..."]
}
```
> - [X]  :bulb: Any other input different to the JSON above must return an error.

- [X] integrate a web scraper for downloading news from different sources (3 or more)-
- [ ] The output must include 3 news related to the input keywords sorted according to a custom ranking;
- [ ] it could be defined using a simple approach like word frequency or TF-IDF or using a more elaborated one using semantics

```json
{
  "news": [
    {
      "ranking": 0.89,
      "content": "First news...",
      "reference": "https://www.eluniversal.com.mx/noticia.html"
    },
    {
      "ranking": 0.75,
      "content": "Second news...",
      "reference": "https://www.excelsior.com.mx/noticia.html"
    },
    {
      "ranking": 0.56,
      "content": "Third news...",
      "reference": "http://media.jornada.com.mx/ultimas/noticia.html"
    }
  ]
}
```
- [X] Each output must be saved in the DB;
- [X] in case the input is repeated, the API must retrieve the data from the DB instead of the internet.

## Points to evaluate:
- [X] The code must be uploaded and shared through a Github repo (or similar).
- [X] The repo must include a README file with general info about the project.
- [ ] The code must be deployed in a public cloud service like Heroku (or similar).
- [ ] Must have at least one case working.

## Recommended technologies:
- [X] Flask: ​ https://flask.palletsprojects.com/en/1.1.x/
- [ ] Natural Language Toolkit: ​ https://www.nltk.org/
- [X] PostgreSQL: ​ https://www.postgresql.org/
- [ ] Heroku: ​ https://www.heroku.com/

## Nice to have:
- [X] A Postman collection with some examples: ​ https://www.getpostman.com/
- [ ] Unit and e2e tests: ​ https://docs.pytest.org/en/latest/
- [ ] Coverage report: ​ https://pytest-cov.readthedocs.io/en/latest/reporting.html
- [ ] Able to get news in English
