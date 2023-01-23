# Bitly URL shortener

The program interacts with the [Bitly API](https://bitly.com/): shortens long links and gets the number of clicks on a short link.


### How to install

To use the Bitly API, you'll need an OAuth access token to authorize and authenticate the connection to Bitly.
Paste your token into the `.env` file by issuing the command:
```
echo "BITLY_TOKEN=<your bitly token>" > .env
```

This project requires the following Python packages:
- python-dotenv >= 0.21.1
- requests >= 2.28.2

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```


### Run

To run the program, enter the following command:

```python
python main.py <user url>
```


### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
