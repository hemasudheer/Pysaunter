#Pysaunter Starter Project

__Quick[er] start to writing object oriented tests with Pysaunter.__

Pysaunter has numerous configuration and dependencies to get up and running.
This project goes a few steps beyond `pysaunter --new` to help us create
a fresh environment and get to work writing tests.

##Quick Quick Start

If you already have python 2.7, pip, and virtualenvwrapper then start here.

    git clone https://github.com/DamienBell/pysaunterstarter.git [project directory]
    cd [project directory]
    cp conf/saunter.ini.default conf/saunter.ini

###Edit saunter.ini
  `saunter.ini` is our configuration file. We must define **base_url**
  This is the initial url that our tests will open to.
  Optionally we can set set **browser** to something other than firefox.
  The chrome driver is included in this package. So setting the browser to chrome
  should work without extra downloads.

  ###Virtual Environment

  Let's startup a virtual environment.
  If you already have one you'd like to use run:

    workon [yourenv]

  otherwise run:

    mkvirtualenv [yournewenv]

###Start Selenium Server

  Note: if you already have a selenium server running then you don't
  need to run a new one.
  This package includes the selenium.jar file if you don't already
  have it. To turn on the server run:

    java -jar server/selenium-server-standalone-2.41.0.jar

### Run tests

    pysaunter -m scratch

  This command should run the tests with the tag 'scratch'.
  It should open the defined __base_url__ with the defined __browser__.
  If no browser was specified it should just open in firefox.
  
