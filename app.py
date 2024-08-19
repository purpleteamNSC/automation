import os
import random
import time
import subprocess

if not os.path.exists('code.txt'):
    open('code.txt', 'w').close()

while True:
    
    numero_aleatorio = random.randint(1, 500)

    with open('code.txt', 'a') as f:
        f.write(str(numero_aleatorio) + '\n')

    subprocess.run(['git', 'add', 'code.txt'])
  
    subprocess.run(['git', 'commit', '-m', 'update'])

    subprocess.run(['git', 'push'])
 
    time.sleep(numero_aleatorio)