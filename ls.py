#! /usr/bin/env python

import os
mulu=raw_input("pls ,echo what\'s dir you watch : ")
print "-----------------------"

dir=[d for d in os.listdir(mulu)]
changdu=len(dir)
for z in range(changdu):
        print dir[z]

