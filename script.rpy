# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Diane")
define pov = Character("[povname]")


# The game starts here.

label start: 

    "20 de Abril de 2023"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music collegueintro loop

    scene escola

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show diane


    # These display lines of dialogue.

    e "Hola."

    e "Por fin llegas."

    e "Mi nombre es Diane y soy un NPC de prueba."

    e "Este es el primer juego en el que aparezco, asi que estoy algo nerviosa, creo que nunca he estado en uno.
    O bueno lo maximo que he llegado ha sido a la libreta de algun dibujante argentino."

    e "Es algo asombroso, finalmente puedo expresarme. Aprovechando la situacion, quiero decirte que hoy te ves muy bien.
    Gracias por acompañarte en este primer test."

    e "Tiene mucho valor para un personaje de ficcion nuevo que se atreve a incursionar en este mundo."


    show escola
    hide diane

    e "Asi que este sera nuestro escenario..."

    e "Se ve enorme!"

    e "Vaya! Espero que cualquier cosa que pase aqui, al menos sea divertida para ti."

    show diane
    e "Bien, cuentame algo de ti."

    e "Es la primera vez que nos vemos?"

    show diane at left

    menu:
        "Si, ya nos hemos conocido antes":
         jump choice1_yes

        "No, de hecho es la primera vez que hablamos":
         jump choice1_no

    # This ends the game.

    return
    
    
    label choice1_yes:
        e "No creo que nos hayamos conocido antes, ya que es la primera vez que hablo con una persona desde que fui 
        concebida."
        jump choice1_done
        return

        label choice1_no:
        e "Oh bueno, el placer es mio entonces, es agradable estar hablando con alguien, me sentia atrapada en esa libreta."
        jump choice1_done
        return

        label choice1_done:
        e "Fabuloso."

        jump phase1
        return


    label phase1:
        e "Como ha estado tu dia?"

        e "Espero que bien, mi creador insiste en que debo aprender mucho todavia."

        e "Por cierto, gracias por ayudarme con esta introducción sobre mi misma, mi concepción fue bastante inesperada."

        $ povname = renpy.input("Por cierto... cual es tu nombre?", length=32)
        pov "Mi nombre es [povname]."

        e "Mucho gusto en conocerte [povname], espero que podamos vivir muchas aventuras juntos."

        e "Aparentemente todo esta llendo de maravilla, el poder hablar y conectar con alguien es asombroso. Me pregunto que tipo de historias
        nos esperan"

        e ""
        return