shp = 100
bhp = 150
def bossatk(bhp, shp):
  atk = randint(1,3)
  if atk == 1:
    print('Boss used Punch (-25 health)')
    shp -= 25
  if atk == 2:
    print('Boss used Kick (-30 health)')
    shp -= 30
  if atk == 3:
    print('Boss used Tackle (-35 health)')
    shp -= 35
def satk(shp, bhp):
  satkone = input('Fireblast, Laserblast')
  if satkone.lower() == 'fireblast':
    burn = randint(10, 40)
    print('Boss Hp - ', burn)
    bhp -= (burn)
  if satkone.lower() == 'laserblast':
    pain = randint(0, 70)
    print('Boss Hp - ', pain)
    bhp -= (pain)
from time import sleep as wait
print('Hello, Welcome to Boss Fight!')
wait(1)
print('Stage 1.')
wait(1)
print('Begin!')

