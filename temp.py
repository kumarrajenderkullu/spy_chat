import sys
from termcolor import colored, cprint
from datetime import datetime

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

message = "hiii"
message=colored(message, 'red')
time = datetime.now()
time=str(time)
sent_by_me = True
sent_by_me=str(sent_by_me)
msg=message+" ("+time+") "+sent_by_me
print msg