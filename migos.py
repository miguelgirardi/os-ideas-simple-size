#!/usr/bin/env python3
import sys
LOREM="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
def about():print("MigOS Version 2KiB\nMade in 2026")
def echo(s):print(LOREM if s=="TESTMESSAGE"else s.strip('"'))
while True:
 c=input("> ").split(maxsplit=1)
 if not c:continue
 if c[0]=="about":about()
 elif c[0]=="echo":echo(c[1]if len(c)>1 else"")
 elif c[0]=="exit":break
 else:print("Unknown command")
