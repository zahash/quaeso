# quaeso

> python cli program to send requests

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python program that reads a json/yml file for request data and sends the request

## Installation

pip install this repo.
(Note: Incompatible with Python 2.x)

```sh
pip3 install git+https://github.com/zahash/quaeso.git
```

(or)

```sh
pip install git+https://github.com/zahash/quaeso.git
```

## Usage example

To get help with commandline arguments

```sh
quaeso --help
```

Using Command-line Arguments

```sh
quaeso "some/folder/myrequest.yml"
```

(or)

```sh
quaeso "some/folder/myrequest.json"
```

### Disclaimer

sometimes the quaeso command doesn't work in windows if the package is installed globally.

to avoid this, install the package in a local virtual env

first, create a env

```sh
python3 -m venv env_for_quaeso
```

activate that env

```sh
.\env_for_quaeso\Scripts\activate
```

and then pip install. But you will have to activate that env everytime you want to use quaeso.

## IO Redirection

the response is written to stdout and headers/status are written to stderr so that users can take IO redirection to their advantage. This works on windows, linux and mac.

```sh
quaeso "some/folder/myrequest.yml" > res.json 2> res_headers.txt
```

both stdout and stderr can be redirected to the same file

```sh
quaeso "some/folder/myrequest.yml" > res.json 2>&1
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

#### File Download (`quaeso "some/folder/myrequest.yml" > book.pdf`)

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

## Complete request file with all available fields (`myrequest.yml`)

```yaml
method: XXX # (REQUIRED) GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
url: XXX # (REQUIRED) must be prefixed with http:// or https://

params: # url query parameters. have as many as you like
  offset: 0
  limit: 10

data: # data for POST
  name: john
  age: 22
  hobbies:
    - running
    - eating
    - sleeping

# you can also type data in json format instead of yaml
data: |
  {
    "name": "john",
    "age": 22,
    "hobbies": ["running", "eating", "sleeping"]
  }

headers: # have as many as you like
  Content-Type: application/json
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c


cookies: # have as many as you like
  mycookie: cookievalue
  myothercookie: othercookievalue

timeout: 3.14 # seconds

allow_redirects: true # true or false

proxies: # have as many as you like
  http: http://10.10.1.10:3128
  https: https://10.10.1.11:1080
  ftp: ftp://10.10.1.10:3128

# EITHER verify server's TLS certificate. true or false
verify: true
# OR path to a CA bundle to use
verify: some/folder/cacert.crt

# EITHER path to single ssl client cert file (*.pem)
cert: some/folder/client.pem
# OR (*.cert), (*.key) pair.
cert:
  - some/folder/client.cert
  - some/folder/client.key

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

1. Fork it (<https://github.com/zahash/quaeso/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
