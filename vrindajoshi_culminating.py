#vrinda joshi
#january 22nd 2023
#ics208
#this program is an escape room where the user has to find out what happened to waldo junior while also manuevering the weird manor of the waldos

#import modules
import tkinter as tk
import tkinter.messagebox as mb
import time

#main variables--------------------------------------------------------------

#colour variables
cream = "#f4eee0"
blue = "#151983"
black = "#000000"
white = "#ffffff"

global note1r
global note2r
global cipher1r
global key1r
global key2r
global note3r

note1r = "no"
note2r = "no"
cipher1r = "no"
key1r = "no"
key2r = "no"
note3r = "no"

#font presets
title_font = ("Century Schoolbook L", 30)
main_header_font = ("Century Schoolbook L", 18)
header_font = ("Century Schoolbook L", 16)
text_font = ("Century Schoolbook L", 11)
button_font = ("Century Schoolbook L", 10)
#---------------------------------------------------------------------------

global window
window = tk.Tk()
global frame1
frame1 = tk.Frame(window)
global frame2
frame2 = tk.Frame(window, bg = cream)
global frame3
frame3 = tk.Frame(window, bg = blue)
global frame5
frame5 = tk.Frame(window, relief='flat', borderwidth=6)

#____________________DOOR_4_______________________________________________________________________________________________________________________________________

# redirect to landing.........................................................................................
def door4n():
    frame2.destroy()
    frame3.destroy()

    mb.showinfo("!","There's nothing else here. Let's go back to the landing")

    landing()
#door 4......................................................................................................
def door4():
    frame1.destroy()
    frame4.destroy()

    mb.showinfo("!","we're on the balcony! there's nothing here, except for a key... to where?")

    window.configure(bg = cream)
    
    global frame2
    frame2 = tk.Frame(window, bg = cream)
    global frame3
    frame3 = tk.Frame(window, relief='flat', borderwidth=6)

    key2 = tk.Label(frame3, text="a key", height=10, width=10, bg = cream, fg = blue)
    key2.pack()
    global key2r
    key2r = "yes"

    next_button = tk.Button(frame2, text='NEXT', bg = blue, fg = cream, font = button_font ,command =  door4n)
    next_button.pack()

    frame3.pack()
    frame2.pack()
#............................................................................................................
#____________________DOOR_3_________________________________________________________________________________________________________________________________________


#if the user lost..........................................................................................
def lose():
    frame5.destroy()
    frame3.destroy()

    global frame2
    frame2 = tk.Frame(window, bg = black)

    dark0 = tk.Label(frame2, text = ("well tough luck buddy!"), bg = black, fg = white, font = text_font)

    dark0.pack()

    frame2.pack()

#if the user won...........................................................................................
def win():
    
    frame2.destroy()
    frame6.destroy()
    frame4.destroy()

    window.configure(bg = cream)
    window.geometry("500x150")

    global frame3
    frame3 = tk.Frame(window, bg = cream)

    dark0 = tk.Label(frame3, text = ("well",user_name), bg = cream, fg = blue, font = text_font)
    dark1 = tk.Label(frame3, text = "that was was a journey! we finally know the truth. what to", bg = cream, fg = blue, font = text_font)
    dark2 = tk.Label(frame3, text = "do with what we learned.. well that's another question", bg = cream, fg = blue, font = text_font)

    dark0.pack()
    dark1.pack()
    dark2.pack()

    frame3.pack()
#........................................................................................................
#check whether they signed the nda
def ifwin():
    global user_name
    user_name = entry_user.get()
    
    if cb_var1.get() == 1 and entry_user.get() != "":
        win()
    else:
        mb.showinfo("!","you must sign it.")

#reveal identity.................................................................................................       
def reveal():

    frame3.destroy()
    frame5.destroy()
    window.geometry("500x400")

    mb.showinfo("!",'"I see you\'re not THEM. after all, you\'re smart."')
    
    global frame2
    frame2 = tk.Frame(window, bg = black)
    global frame4
    frame4 = tk.Frame(window, bg = black)
    global frame6
    frame6 = tk.Frame(window)

    dark0 = tk.Label(frame2, text = "im actually waldo junior, and im in the", bg = black, fg = white, font = text_font)
    dark1 = tk.Label(frame2, text = "hideout due to my desceased father's loans.", bg = black, fg = white, font = text_font)
    dark2 = tk.Label(frame2, text = "the debts have passed onto me, and the banks", bg = black, fg = white, font = text_font)
    dark3 = tk.Label(frame2, text = "are after me. i cannot pay them, and therefore", bg = black, fg = white, font = text_font)
    dark4 = tk.Label(frame2, text = "must hideout here. i apologize for trapping", bg = black, fg = white, font = text_font)
    dark5 = tk.Label(frame2, text = 'you here, and wrongfully accusing you. i ', bg = black, fg = white, font = text_font)
    dark6 = tk.Label(frame2, text = 'can let you go, but you must sign an NDA', bg = black, fg = white, font = text_font)

    dark0.pack()
    dark1.pack()
    dark2.pack()
    dark3.pack()
    dark4.pack()
    dark5.pack()
    dark6.pack()

    global cb_var1
    cb_var1 = tk.IntVar()

    cb_var1.set(0)
    cb1 = tk.Checkbutton(frame6, text='i will not disclose what i heard', variable=cb_var1)

    cb1.pack()

    global entry_user
    entry_user = tk.Entry(frame6, width = 10)
    entry_user_p = tk.Label(frame6, text = 'enter what everyone else uses, but is yours:', font = text_font)

    entry_user_p.pack(side='left')
    entry_user.pack(side='left')
    
    userAgreement_button = tk.Button(frame4, text="ILL SIGN IT", bg = black, fg = white, font = button_font, command = ifwin)
    userAgreement_button.pack()

    frame2.pack()
    frame6.pack()
    frame4.pack()
#second window in the hideout.........................................................................................................    
def hideout2():
    window.geometry("500x120")
    #check riddles
    def check():
        ans = entry.get()
        if ans == "time":
            mb.showinfo("!", "\"you're right!\"")
            reveal()
        else:
            mb.showinfo("!","i guess you're trapped. forever.")
            lose()
            
    frame1.destroy()

    global frame5
    frame5 = tk.Frame(window, bg = black)
    global frame3
    frame3 = tk.Frame(window, bg = black)

    prompt_label = tk.Label(frame5, text = 'what flies with no wings? (answer in lowercase)', bg = black, fg = white, font = text_font)
    entry = tk.Entry(frame5, width = 10)

    prompt_label.pack(side='left')
    entry.pack(side='left')
    
    check_button = tk.Button(frame3, text='will he trust you',command = check,bg = black, fg = white, font = button_font)
    check_button.pack()

    frame5.pack()
    frame3.pack()
    
#1st window in the hideout
def hideout1():
    
    frame2.destroy()
    window.geometry("500x400")

    global frame1
    frame1 = tk.Frame(window, bg = black)

    dark = tk.Label(frame1, text = "oh my! it seems like we've gotten trapped.", bg = black, fg = white, font = text_font)
    dark1 = tk.Label(frame1, text = "           ", bg = black, fg = white, font = text_font)
    dark2 = tk.Label(frame1, text = "someone's footsteps are coming closer.....", bg = black, fg = white, font = text_font)
    dark3 = tk.Label(frame1, text = "           ", bg = black, fg = white, font = text_font)
    dark4 = tk.Label(frame1, text = "           ", bg = black, fg = white, font = text_font)
    dark5 = tk.Label(frame1, text = '"who are you?", says a distant male voice.', bg = black, fg = white, font = text_font)
    dark6 = tk.Label(frame1, text = '"i hope you aren\'t who i\'ve been avoiding.." (who is he talking about)', bg = black, fg = white, font = text_font)
    dark7 = tk.Label(frame1, text = '"well.. i\'ll give you a chance to prove yourself"', bg = black, fg = white, font = text_font)
    dark8 = tk.Label(frame1, text = '                  ', bg = black, fg = white, font = text_font)
    dark9 = tk.Label(frame1, text = '"answer this riddle correctly, and ill let you go."', bg = black, fg = white, font = text_font)

    dark.pack()
    dark1.pack()
    dark2.pack()
    dark3.pack()
    dark4.pack()
    dark5.pack()
    dark6.pack()
    dark7.pack()
    dark8.pack()
    dark9.pack()

    userAgreement_button = tk.Button(frame1, text="we might as well try", bg = black, fg = white, font = button_font, command=hideout2)
    userAgreement_button.pack()

    frame1.pack() 
#slide..................................................................................................................    
def slide():
    frame3.destroy()
    frame1.destroy()
    window.configure(bg = black)
    window.geometry("500x200")
    mb.showinfo("!", "wheeee!")

    global frame2
    frame2 = tk.Frame(window, bg = black)

    dark = tk.Label(frame2, text = "it's dark...", bg = black, fg = white, font = text_font)
    dark.pack()

    dark2 = tk.Label(frame2, text = "maybe we can call for help?", bg = black, fg = white, font = text_font)
    dark2.pack()

    userAgreement_button = tk.Button(frame2, text="CALL FOR HELP", bg = black, fg = white, font = button_font, command=hideout1)
    userAgreement_button.pack()

    time.sleep(1)

    frame2.pack()
#riddle...................................................................................................................
def slide_riddle():
    #check riddle
    def check():
        ans = entry.get()
        if ans == "a slide":
            mb.showinfo("!", "oh! it's a slide! let's go down it")
            slide()
        else:
            mb.showinfo("!","but it doesn't seem to be that. hmm what else could it be?")
            
    frame2.destroy()
    
    mb.showinfo("!","Underneath the box, is a dark hole. Now we aren't going to jump into it, \
especially with it being in this strange manor. Let's try and find a hint.")

    global frame1
    frame1 = tk.Frame(window, bg = cream)
    global frame3
    frame3 = tk.Frame(window, bg = cream)

    prompt_label = tk.Label(frame3, text = 'i take people down, but they love me. what am i?', bg = cream, fg = blue, font = text_font)
    entry = tk.Entry(frame3, width = 10)

    prompt_label.pack(side='left')
    entry.pack(side='left')
    
    check_button = tk.Button(frame1, text='CONTINUE',command = check,bg = cream, fg = blue, font = button_font)
    check_button.pack()

    frame3.pack()
    frame1.pack()
#.............................................................................................................................
#user update
def moved():
    mb.showinfo("!","The box has been moved...")

    frame3.destroy()
    frame1.destroy()

    slide_riddle()
#..............................................................................................................................
#redirect to landing
def landingc():
    frame3.destroy()
    frame1.destroy()
    landing()

#allow user to input what the note says...........................................................................
def note():
    #check riddle
    def check():
        ans = entry.get()
        if ans == "MOVETHEBOX":
            mb.showinfo("!", "You're right!")
            moved()
        else:
            mb.showinfo("!","You're wrong. Try again!")

    #refresh
    frame2.destroy()

    #instructions
    mb.showinfo("!","write what the note in the box says (all lowercase)")

    #make frames
    global frame1
    frame1 = tk.Frame(window, bg = cream)
    global frame3
    frame3 = tk.Frame(window, bg = cream)

    #prompt + entry
    prompt_label = tk.Label(frame3, text = 'what did the note say?', bg = cream, fg = blue, font = text_font)
    entry = tk.Entry(frame3, width = 10)
    prompt_label.pack(side='left')
    entry.pack(side='left')

    #buttons
    check_button = tk.Button(frame1, text='CONTINUE', fg = blue, bg = cream, font = button_font, command = check)
    check_button.pack(side='left')
    exit_button = tk.Button(frame1, text='GO BACK TO LANDING', fg = blue, bg = cream, font = button_font, command = landingc)
    exit_button.pack(side='left')

    frame3.pack()
    frame1.pack()
#..............................................................................................................................
#redirect to landing
def landingb():
    frame2.destroy()
    landing()
    
#see if the user knows what the box says........................................................................................    
def boxif():

    #refresh
    frame1.destroy()

    #format window
    window.geometry("500x100")

    #make frame
    global frame2
    frame2 = tk.Frame(window)

    #option buttons    
    door1_button = tk.Button(frame2, text='i know what the note says.', bg = blue, fg = cream, font = button_font, command = note)
    door2_button = tk.Button(frame2, text='go to landing', bg = blue, fg = cream, font = button_font, command = landingb)
    
    door1_button.pack(side="left")
    door2_button.pack(side="left")
    
    frame2.pack()

#door 3....................................................................................................    
def door3():
    #check riddle
    def check2():
        #if no key
        if key1r == "no":
            mb.showinfo("!","Hmmm.. seems like you don't have the key to this box. Come back later when you do.")
            frame3.destroy()
            landing()
        #if key
        else:
            #make frame
            global frame1
            frame1 = tk.Frame(window, bg = cream)

            #refresh
            frame3.destroy()

            #notes
            note3 = tk.Label(frame1, text="01001101 01001111 01010110 01000101 01010100",bg = blue, fg = cream, font = text_font)
            note32 = tk.Label(frame1, text="01001000 01000101 01000010 01001111 01011000",bg = blue, fg = cream, font = text_font)
            note3.pack()
            note32.pack()

            #change user recieved variable
            global note3r
            note3r = "yes"

            #next door button
            next_door1 = tk.Button(frame1, text="NEXT", bg = blue, fg = cream, font = button_font, command=boxif)
            next_door1.pack()

            frame1.pack()

    #refresh
    frame1.destroy()
    frame4.destroy()

    #format window
    window.configure(bg = cream)

    #make frames
    global frame3
    frame3 = tk.Frame(window)

    #box button
    box = tk.Button(frame3, text="BOX", height=5, width=10, bg = blue, fg = cream, font = button_font, command = check2)
    box.pack()

    frame3.pack()
#...............................................................................................................



#____________________DOOR_2_______________________________________________
#redirect to landing
def landingd():
    frame3.destroy()
    landing()
    
#choose where to go..............................................................................................
def choosed2():
    #pack frames
    global frame3
    frame3 = tk.Frame(window, bg = blue)

    #format window
    window.geometry("250x250")
    window.configure(bg = blue)

    mb.showinfo("!","Seems like were done here. Would you like to go to the landing (w 4 doors), or where you chose from 2 doors?")

    #doors   
    door1_button = tk.Button(frame3, text='landing',height = 40, width = 10, bg = cream, fg = blue, command = landingd)
    door2_button = tk.Button(frame3, text='2 doors', height = 40, width = 10, bg = cream, fg = blue, command = door2e)
    
    door1_button.pack(side="left")
    door2_button.pack(side="left")

    #pack frame
    frame3.pack()
#...................................................................................................................    
#redirect to choose 2
def choosed2y():
    #refresh
    frame3.destroy()
    frame2.destroy()

    choosed2()
#waldo senior's office..............................................................................................    
def sroffice():
    #refresh
    frame1.destroy()
    frame4.destroy()

    #user update
    mb.showinfo("!","It seems we're in Waldo Sr's office!!!")

    #window format
    window.configure(bg = cream)

    #make frames
    global frame2
    frame2 = tk.Frame(window, bg = cream)
    global frame3
    frame3 = tk.Frame(window, relief='flat', borderwidth=6)

    #key
    key1 = tk.Label(frame3, text="a key", height=10, width=10, bg = cream, fg = blue)
    key1.pack()
    global key1r
    key1r = "yes"

    #next button
    next_button = tk.Button(frame2, text='NEXT', bg = blue, fg = cream, font = button_font ,command =  choosed2y)
    next_button.pack()

    frame3.pack()
    frame2.pack()

    mb.showinfo("!","a key!")

#hallway.......................................................................................................    
def door21h():
    #refresh
    frame3.destroy()
    frame2.destroy()

    #make frames
    global frame1
    frame1 = tk.Frame(window, bg = cream)
    global frame4
    frame4 = tk.Frame(window, bg = cream)

    #format window
    window.geometry("600x250")

    #header
    cdins = tk.Label(frame1, text = "it seems like a hallway with a door at the end...", fg = cream, bg = blue, font = header_font)
    cdins.pack()

    #door
    door1_button = tk.Button(frame4, text='door', height = 40, width = 10, bg = cream, fg = blue, command = sroffice)
    door1_button.pack()

    #pack frames
    frame1.pack()
    frame4.pack()
#door 1 lock...................................................................................................    
def door21():
    #riddle check
    def check():
        ans = entry.get()
        if ans == "9" or ans == "nine":
            mb.showinfo("!", "You picked the right passcode!")
            door21h()
        else:
            mb.showinfo("!","You picked the wrong passcode. Try again!")

    #refresh        
    frame1.destroy()
    frame4.destroy()

    #format window
    window.geometry("700x120")

    #make frames
    global frame2
    frame2 = tk.Frame(window, relief='flat', borderwidth=6,)
    global frame3
    frame3 = tk.Frame(window, bg = blue)

    #riddle + entry
    prompt_label = tk.Label(frame3, text = 'if two’s company, and three’s a crowd, what are four and five?', fg = cream, bg = blue, font = text_font)
    entry = tk.Entry(frame3, width = 10)
    prompt_label.pack(side='left')
    entry.pack(side='left')

    #check button
    check_button = tk.Button(frame2, text='unlock', fg = blue, bg = cream, font = button_font ,command = check)
    check_button.pack(side='left')

    frame3.pack()
    frame2.pack()

    #update message boxes
    mb.showinfo("!","IT'S LOCKED")
    mb.showinfo("!","there's a riddle behind the lock. it seems the answer is the passcode")
#..............................................................................................................    
#refreesh 2 go to the 2 doors frame
def choosed2x():
    frame2.destroy()
    choosed2()
#drawer.........................................................................................................
def drawer():
    #refresh
    frame1.destroy()
    frame4.destroy()

    #window format
    window.geometry("400x300")

    #check whether user has key  
    if key2r == "no":
        mb.showinfo("!","Hmmm.. seems like you don't have the key to this drawer. Come back later when you do.")
        choosed2x()
    else:
        #if user has key
        global frame2
        frame2 = tk.Frame(window, bg = cream)
        
        cipher2 = tk.Label(frame2, text="binary code cipher", height=10, bg = cream, fg = blue)
        cipher2.pack()

        global cipher1r
        cipher1r = "yes"

        next_door1 = tk.Button(frame2, text="NEXT", fg = cream, bg = blue, font = button_font, command=choosed2x)
        next_door1.pack()

        frame2.pack()
#waldo junior's office............................................................................................
def door22r():
    #refresh
    frame3.destroy()
    frame2.destroy()

    #update user
    mb.showinfo("!","We've entered what seems to be Waldo Jr's office. There's nothing here, except for the suspicious looking drawer in his desk")

    #format window
    window.geometry("500x120")
    window.configure(bg = cream)

    #make frames
    global frame1
    frame1 = tk.Frame(window)
    global frame4
    frame4 = tk.Frame(window)

    #header
    cdins = tk.Label(frame1, text = "open the drawer", bg = cream, fg = blue, font = header_font)
    cdins.pack()

    #drawer open button
    door1_button = tk.Button(frame4, text='drawer', bg = blue, fg = cream, font = text_font, command = drawer)
    door1_button.pack()

    #pack frames
    frame1.pack()
    frame4.pack()

# door 2 lock................................................................................................    
def door22():
    #check riddle
    def check():
        ans = entry.get()
        if ans == "a barber":
            mb.showinfo("!", "You picked the right passcode!")
            door22r()
        else:
            mb.showinfo("!","You picked the wrong passcode. Try again!")
    #refresh      
    frame1.destroy()
    frame4.destroy()

    #tell user status
    mb.showinfo("!","IT'S LOCKED")

    #make frames
    global frame2
    frame2 = tk.Frame(window, bg = blue)
    global frame3
    frame3 = tk.Frame(window, bg = blue)

    #riddle + entry
    prompt_label = tk.Label(frame3, text = 'i shave every day, but my beard stays the same. what am i? (answer in lowercase)', fg = cream, bg = blue)
    entry = tk.Entry(frame3, width = 15)

    #window format
    window.geometry("700x120")

    #pack
    prompt_label.pack(side='left')
    entry.pack(side='left')

    #check button
    check_button = tk.Button(frame2, text='UNLOCK', fg = blue, bg = cream, font = button_font, command = check)
    check_button.pack(side='left')

    #pack frames
    frame3.pack()
    frame2.pack()

#choose 2 doors......................................................................................
def door2e():
    #refresh
    frame2.destroy()
    frame3.destroy()

    #make frames
    global frame1
    frame1 = tk.Frame(window, bg = blue)
    global frame4
    frame4 = tk.Frame(window, bg = blue)

    #format window
    window.geometry("600x250")

    #header
    cdins = tk.Label(frame1, text = "CHOOSE DOOR", fg = cream, bg = blue, font = header_font)
    cdins.pack()

    #doors
    door1_button = tk.Button(frame4, text='1',height = 40, width = 10, bg = cream, fg = blue, command = door21)
    door2_button = tk.Button(frame4, text='2',height = 40, width = 10, bg = cream, fg = blue, command = door22)
    door1_button.pack(side="left")
    door2_button.pack(side="left")

    #pack frames
    frame1.pack()
    frame4.pack()

#door 2 lock.................................................................................................    
def door2():
    #riddle check
    def check():
        ans = entry.get()
        if ans == "a deck of cards":
            mb.showinfo("!","the lock unlocked!")
            door2e()
        else:
            mb.showinfo("Oh No!","it didn't work :(")

    #refresh      
    frame1.destroy()
    frame4.destroy()

    #inform whats going on         
    mb.showinfo("!","IT'S LOCKED")
    mb.showinfo("!","there's a riddle behind the lock. it seems the answer in the passcode")

    #format window
    window.configure(bg = blue)
    window.geometry("700x150")

    #make frames
    global frame2
    frame2 = tk.Frame(window, bg = blue)
    global frame3
    frame3 = tk.Frame(window, relief='flat', borderwidth=6)

    #riddle + entry
    prompt_label = tk.Label(frame2, text = 'what is cut on a table, but is never eaten? (answer in lowercase!)', \
                            bg = blue, fg = cream, font = text_font)
    entry = tk.Entry(frame2, width = 25)

    prompt_label.pack()
    entry.pack()

    #check button
    check_button = tk.Button(frame3, text='UNLOCK', fg = blue, bg = cream, font = button_font ,command = check)
    check_button.pack(side='left')

    #make frames
    frame2.pack()
    frame3.pack()
#..........................................................................................



#____________________DOOR_1____________________________________________________________________________________________________________________________________________
    
#direct to landing
def endd1():
    #refresh
    frame2.destroy()
    frame3.destroy()
    
    mb.showinfo("!","There's nothing else here. Let's go back to the landing")
    landing()

#bathroom ..................................................................................   
def bathroom():
    #direct user
    mb.showinfo("!","There's nothing else here.. lets go to the bathroom")

    #refresh
    frame1.destroy()
    frame5.destroy()

    #make frames
    global frame2
    frame2 = tk.Frame(window, relief='flat', borderwidth=6)
    global frame3
    frame3 = tk.Frame(window, relief='flat', borderwidth=6)

    #note  
    note21 = tk.Label(frame2, text="01010100 01001000 01000101 01011001 01000001", bg = blue, fg = cream)
    note22 = tk.Label(frame2, text="01010010 01000101 01000001 01000110 01010100", bg = blue, fg = cream)
    note23 = tk.Label(frame2, text="01000101 01010010 01001101 01000101 00101110", bg = blue, fg = cream)
    note24 = tk.Label(frame2, text="01010101 01010011 01000101 01001011 01000101", bg = blue, fg = cream)
    note25 = tk.Label(frame2, text="01011001 01001001 01001110 01001111 01000110", bg = blue, fg = cream)
    note26 = tk.Label(frame2, text="        01000110 01001001 01000011 01000101         ", bg = blue, fg = cream)
    
    note21.pack()
    note22.pack()
    note23.pack()
    note24.pack()
    note25.pack()
    note26.pack()

    #change note recieved variable
    global note2r
    note2r = "yes"

    #next button
    next_door2 = tk.Button(frame3, text="NEXT", command=endd1, bg = blue, fg = cream, font = button_font)
    next_door2.pack()

    #pack frames
    frame2.pack()
    frame3.pack()

    #tell user what they found
    mb.showinfo("!","a note!")

#room w lights on..................................................................................................................   
def door1l():
    #format window
    window.configure(bg = cream)

    #refresh
    frame2.destroy()

    #make frames
    global frame1
    frame1 = tk.Frame(window, relief='flat', borderwidth=6)
    global frame5
    frame5 = tk.Frame(window, relief='flat', borderwidth=6)

    #note 
    note1 = tk.Label(frame1, text="01010111 01000001 01001100 01000100 01001111 01001010 01010010", bg = blue, fg = cream)
    note2 = tk.Label(frame1, text="01010111 01001001 01001100 01001100 01000010 01000101 01000010", bg = blue, fg = cream) 
    note3 = tk.Label(frame1, text="01000001 01000011 01001011 01001001 01001110 00110010 01000100", bg = blue, fg = cream) 
    note4 = tk.Label(frame1, text="01000001 01011001 01010011 00101110 01010000 01001001 01000011", bg = blue, fg = cream) 
    note5 = tk.Label(frame1, text="01001011 01001000 01001001 01001101 01010101 01010000 01010100", bg = blue, fg = cream) 
    note6 = tk.Label(frame1, text="01001111 01000101 01001110 01010011 01010101 01010010 01000101", bg = blue, fg = cream) 
    note7 = tk.Label(frame1, text="01010011 01000001 01000110 01000101 01010100 01011001 00101110", bg = blue, fg = cream) 

    note1.pack()
    note2.pack()
    note3.pack()
    note4.pack()
    note5.pack()
    note6.pack()
    note7.pack()

    #change note recieved variable
    global note1r
    note1r = "yes"

    #next button
    next_door1 = tk.Button(frame5, text="NEXT", bg = blue, fg = cream, font = button_font, command=bathroom)
    next_door1.pack()

    #pack frames
    frame1.pack()
    frame5.pack()

    #tell user what they found
    mb.showinfo("!","a note!")
    
#room w lights off............................................................................................
def door1():
    #refresh
    frame1.destroy()
    frame4.destroy()

    #make frame
    global frame2
    frame2 = tk.Frame(window)

    #formant window
    window.configure(bg = "#000000")

    #give user hint
    mb.showinfo("!","Somethings weird here.., maybe the lights are off?")

    #light switch
    switch = tk.Button(frame2, text="lights", fg = "#000000", bg="#000000", font = button_font, highlightthickness = 0, bd=0, command=door1l)
    switch.pack()

    #pack frame
    frame2.pack()
#................................................................................................................
#____________________________________________________________________________________________________________________________________________________________________
#4th window......................................................................................................
def landing():
    #make frames
    global frame1
    frame1 = tk.Frame(window, bg = blue)
    global frame4
    frame4 = tk.Frame(window, bg = blue)

    #format window
    window.geometry("600x250")
    window.configure(bg = blue)

    #header
    cdins = tk.Label(frame1, text = "CHOOSE DOOR", fg = cream, bg = blue, font = header_font)
    cdins.pack()

    #doors
    door1_button = tk.Button(frame4, text='1',height = 40, width = 10, bg = cream, fg = blue, command = door1)
    door2_button = tk.Button(frame4, text='2',height = 40, width = 10, bg = cream, fg = blue, command = door2)
    door3_button = tk.Button(frame4, text='3',height = 40, width = 10, bg = cream, fg = blue, command = door3)
    door4_button = tk.Button(frame4, text='4',height = 40, width = 10, bg = cream, fg = blue, command = door4)
    
    door1_button.pack(side="left")
    door2_button.pack(side="left")
    door3_button.pack(side="left")
    door4_button.pack(side="left")

    #pack frames
    frame1.pack()
    frame4.pack()
#................................................................................................................

#refesh b4 going to landing
def landingz():
    frame2.destroy()
    frame3.destroy()

    landing()
#3rd window.......................................................................................................
def broke():
    #check riddle function
    def check():
        #get user entry
        ans = entry.get()
        #if right
        if ans == "pencil lead":
            mb.showinfo("!","Pencil lead was right! A little odd, but so is this manor!")
            landingz()
        #if wrong
        else:
            mb.showinfo("Oh No!","You picked the wrong material. Try again!")

    #infrom about situation         
    mb.showinfo("Oh No!", "The stairs broke! You'll need to figure out what the stairs were made of (so the butler can fix it) before we can go up.")

    #refresh
    frame1.destroy()

    #format window
    window.geometry("700x120")

    #make frame
    global frame2
    frame2 = tk.Frame(window, bg = blue)

    #riddle
    prompt_label = tk.Label(frame3, text = 'i come from a mine and always get surrounded by wood. what am i? (answer in lowercase!)', \
                            bg = blue, fg = cream, font = text_font)
    #entry widget
    entry = tk.Entry(frame3, width = 20)

    #pack 
    prompt_label.pack()
    entry.pack()

    #next button + pack
    check_button = tk.Button(frame2, text='FIX', fg = blue, bg = cream, font = button_font ,command = check)
    check_button.pack(side='left')

    #pack frame
    frame3.pack()
    frame2.pack()

#3rd window......................................................................................................
def stairs():
    #refresh
    frame2.destroy()

    #introduce menu bar
    mb.showinfo("keep in mind!","you can access the notes and ciphers you collect on the way using the menu bar!")

    #format window
    window.geometry("400x150")
    window.configure(bg = blue)

    #make frame
    global frame1
    frame1 = tk.Frame(window, bg = blue)

    #text
    intro_text = tk.Label(frame1, text="we've entered the house...there's nothing", fg = cream, bg = blue, font = text_font)
    intro_text2 = tk.Label(frame1, text="on the ground floor though. lets go upstairs!", fg = cream, bg = blue, font = text_font)
    intro_text3 = tk.Label(frame1, text="    ", fg = cream, bg = blue, font = text_font)

    #pack text
    intro_text.pack()
    intro_text2.pack()
    intro_text3.pack()

    #next button + pack
    walk_up = tk.Button(frame1, text="walk up the stairs", font = button_font, fg = blue, bg = cream, command=broke)
    walk_up.pack()

    #pack frame
    frame1.pack()
#............................................................................................................................

#menu bar (con't)-----------------------------------------
#note menu section
def notewindow():

    #check if there are any
    if note1r != 'yes' and note2r != 'yes' and note2r != 'yes':
            #if there are none
            mb.showinfo("!","No notes yet")
    #there are notes
    else:
        #mae window + format
        note_window = tk.Toplevel()
        note_window.configure(bg = cream)
        note_window.title("Note Storage")

        #note frame
        note1_frame = tk.Frame(note_window, bg = cream)
        note2_frame = tk.Frame(note_window, bg = cream)
        note3_frame = tk.Frame(note_window, bg = cream)

        #note 1
        if note1r == "yes":
            #text
            note1 = tk.Label(note1_frame, text="01010111 01000001 01001100 01000100 01001111 01001010 01010010", bg = blue, fg = cream)
            note2 = tk.Label(note1_frame, text="01010111 01001001 01001100 01001100 01000010 01000101 01000010", bg = blue, fg = cream) 
            note3 = tk.Label(note1_frame, text="01000001 01000011 01001011 01001001 01001110 00110010 01000100", bg = blue, fg = cream) 
            note4 = tk.Label(note1_frame, text="01000001 01011001 01010011 00101110 01010000 01001001 01000011", bg = blue, fg = cream) 
            note5 = tk.Label(note1_frame, text="01001011 01001000 01001001 01001101 01010101 01010000 01010100", bg = blue, fg = cream) 
            note6 = tk.Label(note1_frame, text="01001111 01000101 01001110 01010011 01010101 01010010 01000101", bg = blue, fg = cream) 
            note7 = tk.Label(note1_frame, text="01010011 01000001 01000110 01000101 01010100 01011001 00101110", bg = blue, fg = cream)

            #packing
            note1.pack()
            note2.pack()
            note3.pack()
            note4.pack()
            note5.pack()
            note6.pack()
            note7.pack()

            note1_frame.pack(side = "left")

        #note2
        if note2r == "yes":
            #text
            note21 = tk.Label(note2_frame, text="01010100 01001000 01000101 01011001 01000001", bg = blue, fg = cream)
            note22 = tk.Label(note2_frame, text="01010010 01000101 01000001 01000110 01010100", bg = blue, fg = cream)
            note23 = tk.Label(note2_frame, text="01000101 01010010 01001101 01000101 00101110", bg = blue, fg = cream)
            note24 = tk.Label(note2_frame, text="01010101 01010011 01000101 01001011 01000101", bg = blue, fg = cream)
            note25 = tk.Label(note2_frame, text="01011001 01001001 01001110 01001111 01000110", bg = blue, fg = cream)
            note26 = tk.Label(note2_frame, text="        01000110 01001001 01000011 01000101         ", bg = blue, fg = cream)

            #packing
            note21.pack()
            note22.pack()
            note23.pack()
            note24.pack()
            note25.pack()
            note26.pack()

            note2_frame.pack(side = "left")

        #note3 
        if note3r == "yes":
            #text
            note3 = tk.Label(note3_frame, text="01001101 01001111 01010110 01000101 01010100",bg = blue, fg = cream, font = text_font)
            note32 = tk.Label(note3_frame, text="01001000 01000101 01000010 01001111 01011000",bg = blue, fg = cream, font = text_font)

            #packing
            note3.pack()
            note32.pack()
            
            note3_frame.pack(side = "left")

#cipher menu section
def cipherwindow():
    #check whether found
    if cipher1r == "yes":
        
        #create window+format
        startw = tk.Toplevel()
        startw.title("Where's Waldo: Last Will and Testament")
        startw.configure(bg = "#6B695E")

    #+++++++++++++++++++++++++ #DIDN'T DO MYSELF, COPIED HOW TO ADD IMAGE FROM INTERNET
        #add image
        bg = tk.PhotoImage(file = "binary code.png")

        #format
        canvas1 = tk.Canvas(startw, width = 780, height = 321)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image( 0,0, image = bg, anchor = "nw")
    #+++++++++++++++++++++++++

        #mainloop()
        tk.mainloop()
    else:
        #if cipher is not collected
        mb.showinfo("!","No ciphers yet")
#-------------------------------------------------
    
#2nd window...........................................................................................       
def intro():
    
    #refresh
    frame1.destroy()
    frame5.destroy()
#menu ------------------------------------------
    menubar = tk.Menu(window)
    file_menu = tk.Menu(menubar)

    
    file_menu.add_command(label='Notes', command=notewindow)
    file_menu.add_command(label='Ciphers', command=cipherwindow)

    menubar.add_cascade(label= "ITEMS", menu=file_menu)

    window.config(menu=menubar)
#-------------------------------------------------
    #format window
    window.geometry("600x250")

    #header
    header_text = tk.Label(frame2, text="INTRODUCTION", bg = cream, fg = blue, font = header_font)

    #body text explaining sitaution
    intro_text = tk.Label(frame2, text="Welcome enquirer! The death of billionaire Waldo Sr has recently made ", bg = cream, fg = blue, font = text_font)
    intro_text2 = tk.Label(frame2, text="headlines. The big businessman died of old age after living a long and proper life,", bg = cream, fg = blue, font = text_font)
    intro_text3 = tk.Label(frame2, text="but the death of his son Waldo Jr around the same time has detectives confused. We ", bg = cream, fg = blue, font = text_font)
    intro_text4 = tk.Label(frame2, text="feel some clues may be located at Waldo Manor, but it appears that detectives have ", bg = cream, fg = blue, font = text_font)
    intro_text5 = tk.Label(frame2, text="not yet considered looking there. Would you be willing to take the risk of exploring ", bg = cream, fg = blue, font = text_font)
    intro_text6 = tk.Label(frame2, text="to discovering the truth?", bg = cream, fg = blue, font = text_font)

    #next button
    userAgreement_button = tk.Button(frame2, text="enter the house", bg = blue, fg = cream, font = button_font, command=stairs)

    #pack elements
    header_text.pack()

    intro_text.pack()
    intro_text2.pack()
    intro_text3.pack()
    intro_text4.pack()
    intro_text5.pack()
    intro_text6.pack()

    userAgreement_button.pack(side = "left")

    frame2.pack()
#starting window..........................................................................
def main():

    #make root window + format
    window.title("Where's Waldo: Last Will & Testament")
    window.geometry("400x120")
    window.configure(bg = cream)

    #make frame
    frame1.configure(bg = cream)
    
    #make title label
    title_label = tk.Label(frame1, text="WHERE'S WALDO", bg = cream, fg = blue, font = title_font)

    #make buttons
    start_button = tk.Button(frame5, text="START", bg = blue, fg = cream, font = button_font, command=intro)
    quit_button = tk.Button(frame5, text="QUIT",  bg = blue, fg = cream, font = button_font, command = window.destroy)

    #pack elements
    title_label.pack()
    start_button.pack(side = "left")
    quit_button.pack(side = "left")

    frame1.pack()
    frame5.pack(side = "bottom")

    #mainloop
    tk.mainloop()
#..............................................................................................
#call main function
main()
