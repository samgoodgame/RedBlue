# RedBlue
**A political language classifier for news articles**

## Quick Start

This quick start is intended to help you replicate our process:

Clone the repository:

    ```
$ git clone git@github.com:samgoodgame/redblue.git
$ cd redblue
    ```

Create a virtualenv and install the dependencies:

    ```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
    ```

Create a "models" directory where you'll store the pickled models:

```
$ mkdir models
```

Build the models by running the classification script:

```
$ cd scripts
$ python svm_classify.py
```

Classify the RSS data. You'll need to go into _predict.py_ and adjust the path to the
dataset (news source) that you wish to analyze:

```
$ python predict.py
```

## About

RedBlue is a political language classifier for news articles. It trains a
Support Vector Machine (SVM) algorithm using training data from the 2016 Democratic
and Republican presidential primary debates. It then uses Baleen
(https://github.com/bbengfort/baleen) to ingest RSS feeds into MongoDB, parses the feeds,
removes stop words, and vectorize the data.

Once the RSS data is in the proper format (a sparse matrix with words as
features and documents as instances), we pass it to our fitted model, which predicts
if articles are "red" (Republican) or "blue" (Democratic).
