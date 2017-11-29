# DouBook
Crawl books from https://book.douban.com

# Environment
- Python3.5+
- [Scrapy](https://scrapy.org/) => better use [Virtualenv](https://virtualenv.pypa.io/en/stable/) to install it
- [PhantomJS](http://phantomjs.org/) => in this project I download the binary version and put it in
**venv/bin/** which created by [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [Selenium](http://www.seleniumhq.org/)

# Usage

##### in command line, at the top level of the project:
```scrapy crawl DB -a search=what_you_want_to_search -a rate=what_rate_of_book_do_you_want```

such as
```scrapy crawl DB -a search=妖怪 -a rate=8.0```

then a file named **妖怪(8.0+).json** will be in top level of the project

##### or you can just check and change the **configs.py** and then
```scrapy crawl DB```

# License
This repository uses the [MIT License](/LICENSE).
