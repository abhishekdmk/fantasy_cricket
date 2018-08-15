#CALCULATES BATSCORE OF PLAYER
def batscore(p_details):
    runs=int(p_details[1])
    balls=int(p_details[2])
    four=int(p_details[3])
    six=int(p_details[4])
    batscore=int(runs/2)
    if runs>=50:
        batscore+=5
    if runs>=100:
        batscore+=10
    if runs>0:
        sr=runs*100/balls
        if sr>=80 and sr<=100:
            batscore+=2
        if sr>100:
            batscore+=4
    batscore=batscore+four
    batscore=batscore+2*six
    return batscore 

#CALCULATES BOWLSCORE AND FIELDSCORE OF PLAYER
def bowlscore(p_details):
    wkt=int(p_details[8])
    overs=int(p_details[5])/6
    runs=int(p_details[7])
    field=int(p_details[9])+int(p_details[10])+int(p_details[11])
    bowlscore=wkt*10
    if wkt>=3:
        bowlscore=bowlscore+5
    if wkt>=5:
        bowlscore=bowlscore+10
    if overs>0:
        er=runs/overs
        if er<2: bowlscore=bowlscore+10
        if er>=2 and er<3.5: bowlscore=bowlscore+7
        if er>=3.5 and er<4.5: bowlscore=bowlscore+4
    bowlscore=bowlscore+10*field
    return bowlscore 
 
