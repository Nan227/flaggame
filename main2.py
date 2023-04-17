f=open('highscore.txt','w')
for p in players:
  f.write(p+'\n')
  f.close()