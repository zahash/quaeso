# yeet

> yeet dem requests

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python program that reads a json/yml file for request data and sends the request

## Installation

pip install this repo.
(Note: Incompatible with Python 2.x)

```sh
pip3 install git+https://github.com/zahash/yeet.git
```

(or)

```sh
pip install git+https://github.com/zahash/yeet.git
```

## Usage example

To get help with commandline arguments

```sh
yeet --help
```

Using Command-line Arguments

```sh
yeet "some/folder/myrequest.yml"
```

(or)

```sh
yeet "some/folder/myrequest.json"
```

## IO Redirection

the response is written to stdout and headers/status are written to stderr so that linux users can take IO redirection to their advantage

```sh
yeet "some/folder/myrequest.yml" > res.json 2> res_headers.txt
```

## Sample request file (`myrequest.yml`)

### GET

```yaml
url: https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658
method: get
params:
  offset: 2
  limit: 100
headers:
  accept: text/xml
  accept-language: en
timeout: 5000
```

#### File Download (`yeet "some/folder/myrequest.yml" > book.pdf`)

```yaml
url: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
method: get
```

### POST

```yaml
url: https://jsonplaceholder.typicode.com/todos/
method: POST
headers:
  Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk
  content-type: application/json
data:
  title: walk the dog
  completed: false
timeout: 5000
```

### PUT

```yaml
url: https://jsonplaceholder.typicode.com/todos/1
method: PUT
headers:
  content-type: application/json
data:
  title: walk the dog
  completed: true
timeout: 5000
```

### DELETE

```yaml
url: https://jsonplaceholder.typicode.com/todos/1
method: DELETE
```

## Development setup

Clone this repo and install packages listed in requirements.txt

```sh
pip3 install -r requirements.txt
```

## Meta

M. Zahash – zahash.z@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/zahash/](https://github.com/zahash/)

## Contributing

1. Fork it (<https://github.com/zahash/yeet/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
