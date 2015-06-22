#coding: utf-8
from lingualeo import LinguaLeo

try:
    bot = LinguaLeo()
    bot.authenticate()
    bot.run()
finally:
    print 'finally'