# PokèScrauso
[ITA](./README.md)


PokèScrauso is a project relized by 5 students on their 4th year of highschool during the PCTO experience at the company AddValue.
This consists in a game strongly inspired by Pokemon games made by GameFreak, but with customizations added.

# Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages. 

```
pip install numba pygame 
```

## Methods of use 

Currently the only way of playing the game is by executing the file main.py, we are currently developing a version with an executable file (.exe) to simplify the launch of the game.
It is possible to modify settings by opening and modifying the file settings.txt, we are currently working on implementing a GUI that allows the player to modify settings directly in the game.

## !CAREFUL!

If by launching the main.py file you get the following error:
```bash
ImportError: cannot import name 'Game' from 'game'
```
it is possible to solve it by moving the files main.py and setting.py in the classes folder and modifying game.py in the following way:

![before](./data/screen_before.png)
![after](./data/screen_after.png)

## Credits 

We don't own any of the elements used in this game, every asset used in the realization of this game belong to their respective owner.

### Since this project was realized purely to test ourself and without any intention to profit on it, we declare that the distribution of PokeScrauso is severly forbidden.