# BTC ticker for Raspberry Pi LCD (16x2) screen

## How to install

### Requirements

- Raspberry Pi (Zero/1/2/3/4)
- LCD screen (16x2)
- python3

### Installation

```bash
# clone repository
git clone https://github.com/zocker-160/pi-btc-ticker.git

cd pi-btc-ticker

# install requirements
sudo -H pip3 install -r requirements.txt

# run
python3 src/main.py

# (optional) add to autostart
crontab -e

# add
@reboot python3 /path/to/repo/src/main.py
```
