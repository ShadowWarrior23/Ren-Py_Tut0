# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lucy", color="#ff0000")
define sh = Character("Shadow_Warrior0", color='#00ffff')


transform leftish:
    xalign 0.75
    yalign 1.0

transform rightish:
    xalign 0.25
    yalign 1.0

label start:

    "Wow, It's really really dark in here."

    l "Better watch out. You don't want to be eaten by a Grue."

    l "Why are you trying to put words into my mouth? And who are you calling \"it\"?"

    l "What's more, what are you going to do about the Grue problem? Are you just going to leave me here?"
 


# The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg stars

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lucy happy at right

    # These display lines of dialogue.

    sh "You've created a new Ren'Py game."

    show ShW questioned at center
    

    sh "Do you wish to advance?"

    # This ends the game.

    menu:

        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        hide Lucy happy

        l "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

        

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        show ShW neutral at left

        sh "Games without menus are called kinetic novels, and there are dozens of them available to play."

        

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 

    return
