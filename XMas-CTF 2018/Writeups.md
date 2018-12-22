# X-MAS CTF 2018 Writeups

## The Ultimate Christmas Game

1. Run keygen.py in the respective folder to obtain string needed to bypass CAPTCHA
2. Get nim's game logic from Wikipedia and beat the computer using it

## Santa's Lucky Number

Run brute.py

First, I noticed that `/?page=1` gets appended to the URL when clicking on `Page 1`, and 
`/?page=2` gets appended to the URL when clicking on `Page 2`. So, brute.py scrapes URLs with
higher page numbers until it finds something on the webpage resembling `X-MAS`.

## Santa's Security Levels

1. Record audio to mp3 file because unable to download it
2. Drag mp3 file to Audacity 
3. Play it using the Spectrogram setting
4. Translate mp3 into Morse Code 

   At this point, you should get `github com gooogal xmas`

5. Google the message and navigate to the found GitHub repository
6. Translate all the uppercase letters in line 5 of the text file in the repo to ROT13

## Special Christmas Wishlist

1. Assign each symbol a letter of the alphabet in roughly the first four lines
2. Plug your string into an online substitution solver
3. Use this knowledge to find what XMAS should look like
5. Find and decode the rest of the line with XMAS in it

## Santa the Weaver

1. `hexedit flag.png`
2. `/ 4d4153`, or alternatively `ctrl-T / X-MAS`


   Searches image for flag

## Oh Christmas Tree

See Santa the Weaver. Basically the same thing, except part of the flag is split from the rest of it.

## Gnome's Buttons

Change button value to flag