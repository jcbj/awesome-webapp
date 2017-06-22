#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'jc'


import orm, asyncio
from models import User, Blog, Comment

async def testUser(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data',db='awesome')
    user = User(name='jc2235', email='jc2235@126.com', passwd='123456', image='about:blank')
    await user.save()

def test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testUser(loop))
    loop.close()

if __name__ == '__main__':
    test()
