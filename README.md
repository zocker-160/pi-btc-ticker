# BTC ticker for Raspberry Pi LCD (16x2) screen

## How to install

### Requirements

- Raspberry Pi (Zero/1/2/3/4)
- LCD screen (16x2)
- Python3
- Binance API key; [create one here](https://www.binance.com/userCenter/createApi.html)

### Installation

```bash
# clone repository
git clone https://github.com/zocker-160/pi-btc-ticker.git

cd pi-btc-ticker

# install requirements
sudo -H pip3 install -r requirements.txt

# set your own Binance KEY and SECRET
nano src/main.py

# paste your key into the API_KEY and API_SECRET variables

# run
python3 src/main.py

# (optional) add to autostart
crontab -e

# add
@reboot python3 /path/to/repo/src/main.py
```


## Credits

Thanks to Felix [in this article](https://tutorials-raspberrypi.de/raspberry-pi-lcd-display-16x2-hd44780/) for the nice template for the lcd script (up to commit [427514822c039ffb7c0a27f742430b5def5ee37d](https://github.com/zocker-160/pi-btc-ticker/tree/427514822c039ffb7c0a27f742430b5def5ee37d))
