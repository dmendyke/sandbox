#!/usr/bin/env python2

import glob
import re

FIRST_MATCH = 1

for module in glob.glob( 'content/[!_]*.py' ) :
  name = re.match( r"content/(.+).py", module ).group( FIRST_MATCH )
  print name
