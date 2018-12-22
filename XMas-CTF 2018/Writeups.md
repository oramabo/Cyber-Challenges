# X-MAS CTF 2018 Writeups

## The Ultimate Christmas Game

You must netcat to a connection. Upon doing so, you see a CAPTCHA message.
   
1. Run keygen.py in the respective folder to obtain the string needed to bypass the CAPTCHA

Now, you must beat the computer at a game of nim.
   
2. Get nim's game logic from Wikipedia and beat the computer using it

## Santa's Lucky Number

You arrive at a webpage. You click on `Page 1`, `Page 2`, and `Page 3`, but all you get are
random sequences of numbers.

1. Run brute.py

First, I noticed that `/?page=1` gets appended to the URL when clicking on `Page 1`, and 
`/?page=2` gets appended to the URL when clicking on `Page 2`. So, brute.py scrapes URLs with
higher page numbers until it finds something on the webpage resembling `X-MAS`.

## Santa's Security Levels

You arrive at a webpage which has an audio message.

1. Record message using OBS into an mp3 file because I couldn't find a way to download it
2. Drag mp3 file to Audacity 
3. Use Spectrogram setting for better visuals
4. Translate visual into Morse Code 

At this point, you should get `github com gooogal xmas`

5. Google `gooogal xmas` and navigate to the found GitHub repository

The GitHub repository contains a single text file which contains an encrypted flag

6. Translate all the uppercase letters to ROT13

## Special Christmas Wishlist

You get a png file with mysterious symbols.

1. Assign each symbol a letter of the alphabet in roughly the first four lines
2. Plug your string into an online substitution cipher solver
3. Use this knowledge to find what XMAS should look like
5. Find the line with XMAS in it and decode the rest of it

## Santa the Weaver

You get a png file.

1. `hexedit flag.png`
2. `/ 4d4153`, or alternatively `ctrl-T / X-MAS`

Searches image for flag format

## Oh Christmas Tree

See Santa the Weaver. Same challenge, except part of the flag is split and is further down in hexedit.

## Gnome's Buttons

You arrive at a webpage which has a single button.

Change the button's value to flag