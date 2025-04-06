import re

str = '''

Bilzerian played in the 2008 World Series of Poker Main Event, finishing in 180th place.[15] In 2010, he was voted one of the funniest poker players on Twitter by Bluff magazine.[16] In November 2011, Bilzerian was one of those sued over debt of honor winnings they had been paid in no-contract poker games by Tobey Maguire.[17]

That same year, Bilzerian defended Alex Rodriguez publicly against accusations that he had gambled illegally, claiming that he was present when the alleged gambling event had taken place and Rodriguez was not present.[18] In November 2013, Bilzerian posted an unconfirmed claim that he won $10.8 million from a single night of playing poker,[19] and in 2014 he claimed to have won $50 million throughout the year, adding that he "doesn't play against professionals anymore and the most he's ever lost in a single session is $3.6 million."[20] Bilzerian has discussed his Poker career on Joe Rogan's podcast on YouTube.
'''

patt = re.compile(r'finishing')
matches = patt.finditer(str)

for match in matches:
    print(match)