
## xiaomiapppppp by Danyang Chen
![alt text](https://www.wunderlist.com/blog/google-play-best-apps-of-2014-featuring-yours-truly/2@2x.jpg)
# When
From 06/04/2016 to 07/02/2016

# How
## Description
We used a python package called Scrapy to crawl XiaoMi app store and saved our results on MongoDB database.There were about 30 categories of apps on [XiaoMi app store page](http://app.xiaomi.com). We aimed to crawl all the apps under each category and collected their titles, absolute urls, ids and their categories. This project was finished in June 2016. The information we gathered through this project could be potentionally useful for establishing search database in the future. 

## Demo
This is a demo created by our group leader [Ankai Liang](https://github.com/AnkaiLiang/-12WebCralwer). It demonstrates the crawling process when we start to execute Scrapy on the terminal.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=HVAR5syRljc
" target="_blank"><img src="http://img.youtube.com/vi/HVAR5syRljc/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

## Usage
### A. Install Packages:
We used Scrapy and MongoDB to crawl Xiaomi app store. 
The related packages involved in this project were listed below: 

  1. Scrapy Installation:  
    `pip install Scrapy`  
     More about Scrapy: <http://scrapy.org>  

  2. MongoDB Community Edition Installiation with Homebrew:  
    * Install Homebrew  
       `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  

    * Install MongoDB  
       `brew install mongodb`  
       `brew install mongodb --with-openssl`  
       `brew install mongodb --devel`  
        More about MongoDB: <https://www.mongodb.com>  

  3. Install Scrapy-Splash for Rendering JavaScript:  
    `pip install scrapy-splash`  
     More about Scrapy-Splash: <https://github.com/scrapy-plugins/scrapy-splash>  
     Also you need to install docker: <https://www.docker.com/products/docker#/mac>    

  4. Robomongo *optional:  
     The necessary Robomongo is a good software for me to quickly view the data which is uploaded through MongoDB.
     Robomongo can be downloaded here: <https://robomongo.org>

### B. Start to Crawl
  1. Start Splash and Mongodb Server  
     open terminal:  
     `mongod`  
     open another terminal:  
     `$ docker run -p 8050:8050 scrapinghub/splash`
  
  2. Clone Files  
Clone files from my xiaomiapppppp REPO:   
`git clone https://github.com/jenny91515/Xiaomi.git`
  
  3. Modify the Files under Settings.py  
MONGODB_COLLECTION is the name of the file on MONDODB database you want to created
MONGODB_SERVER and MONGODB_PORT should be the same as what your MONGODB shows  
    `set up the MONGODB`  
    `MONGODB_SERVER = "localhost"`   
    `MONGODB_PORT = 27017`  
    `MONGODB_DB = "xiaomi"`  
    `MONGODB_COLLECTION = "test3"`  
  
  4. Run Crawler:  
     In another terminal window:  
     `scrapy crawl xiaomi`


  
## 12WebCralwer TeamMembers
[me](https://github.com/jenny91515)  
[AnkaiLiang](https://github.com/AnkaiLiang)  
[Taran](https://github.com/songtailun)  
[Kristy Luo](https://github.com/Kristy-Luo)  


  
## Acknowledgement
BigTiger  
Jing Li  
jamesyx  
  
  

## License
[License](https://github.com/AnkaiLiang/-12WebCralwer/blob/master/LICENSE.md)
  
  
## Project Information
Category: full stack  
Team Name: 12WebCralwer  
Description: this is a project using Scrapy to crawl Xiaomi app store  
Stack: Python, MongoDB


