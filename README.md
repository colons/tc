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

- Run `python tc.py`
- Log in to your Time Gamers account in the Chrome window that appears
- Once the homepage starts loading, hit enter in your terminal
- Wait for the game to load (which can take a while)
- Set up the game:
    - Dismiss the upgrade thing that covers the team info pane
    - Enable idle mode for your click weapons
    - Set the buy mode (in the bottom left corner) to 'until upgrade' (xU)
    - You might also want to disable screen post effects and screen shake,
      that's up to you
- Hit enter in your terminal again
- Leave it running until you want to time warp or spend Weapon Cubes, at which
  point you should interrupt the process in your terminal and do so in another
  instance of the game.

The game uploads a cloud save pretty often, but if you want to ensure you're up
to date, hover your mouse over the cloud icon in the top right before quitting.
