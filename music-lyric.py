import time
import sys

print('by @byntangxyz')

lyrics = [
    {"line": "I am not the only traveler", "delay": 3},
    {"line": "Who has not repaid his debt", "delay": 3},
    {"line": "I've been searching for a trail to follow again", "delay": 3},
    {"line": "Take me back to the night we met", "delay": 4},
    {"line": "And then I can tell myself", "delay": 3},
    {"line": "What the hell I'm supposed to do", "delay": 3},
    {"line": "And then I can tell myself", "delay": 3},
    {"line": "Not to ride along with you", "delay": 4},
]

# Fungsi untuk lirik
def type_line(text, typing_speed=0.08):
    for char in text:
        sys.stdout.write(char)     
        sys.stdout.flush()        
        time.sleep(typing_speed)   
    print()  


for lyric in lyrics:
    type_line(lyric["line"])      
    time.sleep(lyric["delay"])    
