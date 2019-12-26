from os import listdir
from shutil import copy2
from re import compile, match
from sys import exit
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

downloads_location = config['DEFAULT']['DownloadsLocation'] + '/'
mp4_location = config['DEFAULT']['MP4Location']
webm_location = config['DEFAULT']['WebmLocation']
mp3_location = config['DEFAULT']['MP3Location']
m4a_location = config['DEFAULT']['M4ALocation']

mp4 = compile('^.*\.mp4')
webm = compile('^.*\.webm')
mp3 = compile('^.*\.mp3')
m4a = compile('^.*\.m4a')

memes = {
    'mp4': [],
    'webm': [],
    'mp3': [],
    'm4a': []
}

list = listdir(downloads_location)
print('Looking for memes in', downloads_location)

for meme in list:
    if(mp4.match(meme)):
        memes['mp4'].append(meme)
    if(webm.match(meme)):
        memes['webm'].append(meme)
    if(mp3.match(meme)):
        memes['mp3'].append(meme)
    if(m4a.match(meme)):
        memes['m4a'].append(meme)

print('Total number of found memes', len(memes))
print('''Memes found:
    {0} mp3 memes {1}
    {2} mp4 memes {3}
    {4} webm memes {5}
    {6} m4a memes {7}
    '''.format(len(memes['mp3']), memes['mp3'],
    len(memes['mp4']), memes['mp4'],
    len(memes['webm']), memes['webm'],
    len(memes['m4a']), memes['m4a']))
input('Checkpoint! [Enter] to copy found files, [CTRL + C] to cancel')

for meme in memes['mp4']:
    copy2(downloads_location + meme, mp4_location)
    print(meme, 'copied to', mp4_location)
for meme in memes['webm']:
    copy2(downloads_location + meme, webm_location)
    print(meme, 'copied to', webm_location)
for meme in memes['mp3']:
    copy2(downloads_location + meme, mp3_location)
    print(meme, 'copied to', mp3_location)
for meme in memes['m4a']:
    copy2(downloads_location + meme, m4a_location)
    print(meme, 'copied to', m4a_location)
print('Done')