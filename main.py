from pgtty import *

display = PgTTY()

display.print("Hello World! ")
display.print("Hello but in blue!", foreground=(0, 0, 255))
display.print("\nHello from a second line!")
display.print("\nHello in inverted!", foreground=(0, 0, 0), background=(127,127,127))

display.set((0, 0), "h")
display.set((5, 4), "E", foreground=(255, 255, 0), background=(0, 0, 255))
display.update()

#input is only to suspend program, otherwise it would close
input()
