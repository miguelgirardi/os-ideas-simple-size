def usarKernel():
  while True:
    cmd=input("$")
    if cmd=="about":
      print("MigOS version 2KiB")
      print("Made in 2026")
    elif cmd.startswith("echo"):
      if cmd!="echo TESTMESSAGE":
        print(cmd[5:])
      else:
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    
usarKernel()
