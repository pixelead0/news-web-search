# news-web-search
Backend that simulates a custom news web search engine.


## Specifications:
This backend include a **RESTful API** with the following characteristics:

 - [X] It must expose an endpoint is exposed through a ** POST ** method;  e.g `/api/news`
 - [X] Any other case must return an error.
 - [ ] The input of the API it's a JSON with one property called ​ **`keywords`** and its value is an array of n words (in Spanish) using the following format:
```json
{
"keywords": [ "one", "two", "three", "..."]
}
```
> :bulb: Any other input different to the JSON above must return an error.

- [X] integrate a web scraper for downloading news from different sources (3 or more)-
- [ ] The output must include 3 news related to the input keywords sorted according to a custom ranking;
- [ ] it could be defined using a simple approach like word frequency or TF-IDF or using a more elaborated one using semantics

- [ ] It must integrate a web scraper for downloading news from different sources (3 or more)
- [ ]  The output must include 3 news related to the input keywords sorted according to a custom ranking; it could be defined using a simple approach like word frequency or TF-IDF or using a more elaborated one using semantics,

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
- [ ] Each output must be saved in the DB; in case the input is repeated, the API must
retrieve the data from the DB instead of the internet.

## Points to evaluate:
 - The code must be uploaded and shared through a Github repo (or similar).
 - The repo must include a README file with general info about the project.
 - The code must be deployed in a public cloud service like Heroku (or similar).
 - Must have at least one case working.

## Recommended technologies:
 - Flask: ​ https://flask.palletsprojects.com/en/1.1.x/
 - Natural Language Toolkit: ​ https://www.nltk.org/
 - PostgreSQL: ​ https://www.postgresql.org/
 - Heroku: ​ https://www.heroku.com/

## Nice to have:
 - A Postman collection with some examples: ​ https://www.getpostman.com/
 - Unit and e2e tests: ​ https://docs.pytest.org/en/latest/
 - Coverage report: ​ https://pytest-cov.readthedocs.io/en/latest/reporting.html
 - Able to get news in English
