import time
import sys

def cool_animation():
    frames = [
        "(-_-)   (o_o)   (^_^)",
        "(o_o)   (^_^)   (-_-)",
        "(^_^)   (-_-)   (o_o)",
    ]
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[94m',  # Blue
        '\033[93m',  # Yellow
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
    ]
    reset = '\033[0m'

    for i in range(30):
        color = colors[i % len(colors)]
        frame = frames[i % len(frames)]
        sys.stdout.write('\r' + color + frame + reset)
        sys.stdout.flush()
        time.sleep(0.2)
    print()

if __name__ == "__main__":
    cool_animation()
[RUN]
python cool_action_script.py
[RESULT]
(-_-)   (o_o)   (^_^)
(o_o)   (^_^)   (-_-)
(^_^)   (-_-)   (o_o)
... (repeated with cycling colors and frames for about 6 seconds)
[VALIDATION]

All acceptance criteria met. The cool action runs successfully and demonstrates a cool effect.