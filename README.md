# Cyber Ware

This cyber ware is for make you safer when ware mask. This will help you know your temperature in 14 days and also
detect the person that come near you more than 1 meters.

Presentation:
https://youtu.be/h7nAJFsMnHo

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes. See deployment for notes on how to deploy the project on a server.

### Requirements

- Python3.6 or higher
- pip
- pipenv
- mongoDB [optional]

### Setup for Cyber Ware Web application

Download the code from git using `git clone`. Do the following step to use this application.

`python3` refers to the Python 3 command using in Linux and Mac system. For window use `python` or `py`.

1. Check python version (it should be 3.6 or 3.7).

   ```bash
   python --version
   ```

2. Install `pipenv`

   ```bash
   pip install pipenv
   ```

3. Install all required packages.

   ```bash
   pipenv install -r requirements.txt
   ```

## Running the application

`python3` refers to the Python 3 command using in Linux and Mac system. For window use `python` or `py`.

1. Start the server int the `pipenv`

   ```bash
   pipenv shell
   python main.py
   ```

   This starts the web server at port 3000.

2. You should see this messages printed from the terminal.

   ```bash
    * Serving Flask app "main" (lazy loading)
    * Environment: production WARNING: This is a development server. Do not use it in a production deployment. Use a
      production WSGI server instead.
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 270-248-137
    * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
   ```

3. In web browser, paste the link: <http://127.0.0.1:3000/>

4. You can stop the python server by press CTRL-C in terminal that you run server. Then exit the `pipenv`

   ```bash
   exit
   ```

## Team Members

| Student ID |     Name     |   Lastname    |   Role   |                     Github                      |
| :--------: | :----------: | :-----------: | :------: | :---------------------------------------------: |
| 6210503535 |    Chunya    |    Tangoen    | Backend  |     [softchun](https://github.com/softchun)     |
| 6210503527 | Chalanthorns | Aenguthaivadt | Backend  | [ChalanthornA](https://github.com/ChalanthornA) |
| 6210500145 |   Parichat   |  Chantathai   | Hardware |       [meindv](https://github.com/meindv)       |
| 6210546447 |   Sirapop    |    Kunjiak    | Frontend |     [bemyXmas](https://github.com/bemyXmas)     |
| 6210503721 |   Phanphut   | Saengkitamorn | Frontend |     [Phanphut](https://github.com/Phanphut)     |
| 6210503870 |   Sirapop    |   Chayajet    | Hardware |   [SirapopPCC](https://github.com/SirapopPCC)   |
| 6210546013 |  Vichisorn   |  Wejsupakul   | Frontend |    [james31366](https://github.com/james31366)    |
| 6210545734 |    Puvana    |  Swatvanith   | Backend  |     [Noboomta](https://github.com/Noboomta)     |

