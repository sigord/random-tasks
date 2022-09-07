# Test assignment

1. Scrape the two ratings - the left one (all-time reviews) and the right one (reviews from the last year) for the top 250 movies from Kinopoisk at [the link](https://www.kinopoisk.ru/lists/top250/?tab=all).
2. Load all data into python
3. Compare the data using appropriate statistical Data Science methods, specifying for each method the null hypothesis, the resulting p-value, and your conclusion.

### Prerequisites

1. Install all requirements
```bash
conda create --name <env> --file conda-requirements.txt --channel default --channel anaconda --channel conda-forge
```
2. Need to change the line 99 in fake_useragent/utils.py to:

```python
html = html.split('<table class="ws-table-all notranslate">')[1]
```
3. If you receive `ValueError("Can not get data")` paste your headers to prevent block by Yandex Smart Captcha
4. The data is already collected, but if you want to update it, run this command
```bash
scrapper.py -p data.csv
```
5. Open the notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sigord/random-tasks/blob/main/test%20assignments/Product%20analyst%20test%20assignment/hypothesis_testing.ipynb)

### Further work
1. Add proxing to scraper

