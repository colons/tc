# tc

A robot that does the boring bits of playing Time Clickers for you using
Selenium and the WebGL version of the game, recommended for people who have
already time warped a bunch of times.

## What it doesn't do

- Manipulate the game internally at all
- Spend Time Cubes or Weapon Cubes for you

## What it does

- Click in the centre of the screen a hundred times
- Click the upgrade buttons for each of your team members in sequence
- Click 'Activate All'
- Click Dimension Shift
- Click Cooldown
- Repeat

## How to use it

### Requirements

- A Time Gamers account with a Time Clickers save synced to it
- Python 3
- chromedriver (probably in your system's package manager)
- selenium (from pypi)

### Usage

- Run `TC_USERNAME=[your time gamers username] TC_PASSWORD=[your time gamers password] python tc.py`
- Wait, and _do not move your mouse over the Chrome window_
- Leave it running until you want to time warp or spend Weapon Cubes, at which
  point you should interrupt the process in your terminal and do so in another
  instance of the game.

Once it's up and running, it'll just keep going. Be careful when mousing over
the window, since the mouse will be clicking constantly while you're there.

The game uploads a cloud save pretty often, but if you want to ensure you're up
to date, carefully hover your mouse over the cloud icon in the top right before
quitting.
