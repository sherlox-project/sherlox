#!/usr/bin/env python
import sys
import Core

import os
from Core import Core
from optparse import OptionParser


def main():

	parser = OptionParser()

	#Parser Options
	parser.add_option("-s", "--starting-point", dest="start",
	help="Use <name>|<email>|<username>|<id> to set the OSINT starting point. \
	Use <id> to OSINT based on a Profile template", metavar="START")

	parser.add_option("-o", "--outdir", dest="outdir",
	help="The IDENTIFIER will name the directory that contains the collected information", metavar="IDENTIFIER")

	parser.add_option("-l", "--level", dest="level",
	help="Use FAST|MEDIUM|HIGH|EXTREME to set LEVEL to the depth of the information gathering.",
	metavar="LEVEL")

	parser.add_option("-v", "--verbose", dest="verbosity",
	help="Use VERBOSITY SILENT|NORMAL|DEBUG to set the verbosity level", metavar="VERBOSITY", default="NORMAL")

	options, arguments = parser.parse_args()

	core = Core("sana.abrahimen")
	core.username_osint()

	return 0

if __name__ == "__main__":
	main()