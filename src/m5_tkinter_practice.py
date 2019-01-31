"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Yu Xin.
"""  # DO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk

def print_hello_or_goodbye(entry_box):
    if entry_box.get()=="ok":
        print("hello")
    else:
        print("goodbye")

def print_entry_for_n_times(entry_box1,entry_box2):
    s=entry_box2.get()
    n=int(s)
    for k in range(n):
        print(entry_box1.get())


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DO: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root=tkinter.Tk()


    # -------------------------------------------------------------------------
    # DO: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    main_frame=ttk.Frame(root,padding=50)
    main_frame.grid()

    # -------------------------------------------------------------------------
    # DO: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    button1=ttk.Button(root,text="hello, hello?")
    button1.grid()

    # -------------------------------------------------------------------------
    # DO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    button1["command"]=(lambda:print("hello"))

    # -------------------------------------------------------------------------
    # DO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    a_entry_box=ttk.Entry(main_frame)
    a_entry_box.grid()

    button2=ttk.Button(root,text="print hello or goodbye")
    button2.grid()
    button2["command"]=(lambda:print_hello_or_goodbye(a_entry_box))

    # -------------------------------------------------------------------------
    # DO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    second_entry_box=ttk.Entry(main_frame)
    second_entry_box.grid()

    button3=ttk.Button(main_frame,text="print n times")
    button3.grid()
    button3["command"]=lambda:print_entry_for_n_times(a_entry_box,second_entry_box)

    root.mainloop()
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
