from pynodejs import *

command=require('os').system
platform=require('platform')
if platform.system() == 'Windows':
    command('cls')
else:
    command('clear')

console.log(f"""Thank You For Installing NodePyJS!
Now, You Can Use Some Node JS Functions In Python!

Developer: Sancho Godinho
Docs: https://github.com/sancho1952007/PyNodeJS

Available Keywords:
require()
console.log()
""")