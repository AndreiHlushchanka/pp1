films=["Joker","Driver","The  Machinist","American Psycho","Nightcrawler"]


with open("films.txt","w", encoding='UTF-8') as f:
    for film in films:
        f.write(film)
        f.write('\n')

#arr=['da','net']
#
#file=open('11.txt','w')
#
#for title in arr:
#    file.write(title)
#   file.write('\n')
#
#file.close()