#coding: utf-8
from lingualeo import LinguaLeo

try:
    bot = LinguaLeo()
    bot.authenticate()
    bot.run()
    # print bot.check_user()
    # if bot.check_user() == 'registered':
    #
    #     print 'user registered'
    # else:
    #     bot.registration_user()


    pass

finally:
    print 'finally'