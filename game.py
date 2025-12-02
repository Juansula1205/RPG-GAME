import random

print("Welcome to CastleSurvival! An rpg game in which your decisions will determine either your faith or success.")
print("Here is how it works:")
print("Along the game, you will be facing enemies troughout choises. Each enemy would have different hp and damage, just like the coices you are going to make.")
print("So for example you are facing an skeleton, so the game would show you its hp and attack, and also the game will make you coose 2 or more options to attack the enemy: like bow, sword, or potion.")
print("Depending of what you choose, you will be able to defeat the enemy or not")
print("As long as you continue the game, i will explain you other things.")
print("Good luck!!!!")
print("")
play = input("Press enter to start")
print("")
print("* * * *       *         * * * * *   * * * * *    *             * * * * * ") 
print("*            *  *       *               *        *             *         ")
print("*           ******      * * * * *       *        *             * * * * * ")
print("*          *      *             *       *        *             *         ")
print("* * * *   *        *    * * * * *       *        * * * * *     * * * * * ")
print("")
print("")
print("* * * * *    *       *    * * * *     *         *   * * * * *   *         *     *        *                     ***     ")
print("*            *       *    *       *    *       *        *        *       *     *  *      *                    *****    ")
print("* * * * *    *       *    * * * *       *     *         *         *     *     ******     *                **  *****  **")
print("        *    *       *    *      *       *   *          *          *   *     *      *    *                **  *****  **")
print("* * * * *    * * * * *    *        *       *        * * * * *        *      *        *   * * * * *        *************")
print("")
print("")
print("")
input("Press Enter")
print("")
print("")
print("")
print("The sun dips low over the rolling hills, painting the sky in shades of gold and crimson. ")
print("Your armor, dented from battles past, gleams faintly as you fasten your sword at your side. You are Sir Aldric.")
print("A knight, Looking for the infamous castle: The Chamber Of The Glorious Dark Passenger")
print("The road ahead winds through forests shrouded in mist and across bridges where shadows linger.")
print("Each step draws you closer to the towering gates of the castle… and to a destiny you cannot yet fathom.")
print("Your journey begins now. Will you rise as the glorious savior, or be lost to the darkness that awaits within?")
print("")
input("Press Enter")
print("")
print("You see yourself near a bridge, but it is facing towards the sky. You get closer and see a panel with a hole. There is something missing")
print("")
input("Task1: find the missing lever")
print("")
print("You will need to answer with numbers")
print("")
search = int(input("look under the rock(1),  look near the trees(2),  or look inside the pit(3): "))
while search !=3:
  search=int(input("Nop, its noth in there. \n look under the rock(1),  look near the trees(2),  or look inside the pit(3): ")) 
else:
  print("")
  print("You found the lever")
print("")
input("Press Enter")
print("")
print("The knight walks onto the old stone bridge, the sound of boots tapping on the wet surface. Below, dark water rushes quickly, making the air cool and damp.")
print("A light wind tugs at the knight’s cloak as they keep moving forward. At the end of the bridge, the tall gates of the castle rise ahead, dark and strong.")
print("Two torches burn on each side, marking the entrance. The knight takes a deep breath and steps toward the castle doors.")
print("")
input("Press Enter")
print("")
print("You enter the glorious castle")
print("Tall pillars rise into the shadows, their shapes barely visible. A tattered banner hangs from the ceiling, its colors faded and edges torn.")
print("The knight’s boots click softly on the stone floor, each step echoing through the empty space. From somewhere deep inside the castle, a faint drip of water breaks the silence.")
print("The sound of it is slow, steady… and strangely loud in the stillness.")
print("The knight’s hand rests on the sword’s hilt. Every shadow feels alive, and the air is thick with the sense that someone — or something — is watching.")
print("")
input("Press Enter")
print("")
print("You open your bag, and see a little reliquary, inside it, there is a photo of a young woman with kind eyes, golden hair, and a spirit unbroken despite her captivity.")
print("You save it and bring up a torch.")
print("You look down and see a path of stones that may guide you to something")
print("")
print("")
print("The knight moves steadily down the long stone hall, each step ringing softly against the cold floor.")
print("His armor glints in the dim light of the torch, and the soft creak of leather straps mixes with the echo of his boots.")
print("")
input("Press Enter")
print("")
print("He then hears a strange noise coming out of a room. ")
print("It was a wet, choking rasp, broken by sudden bursts of shrill, inhuman screeches. ")
print("A sound that seemed to crawl inside the ears, scratching and gnawing, as if it wanted to tear its way into the mind and never leave.")
print("")
print("")
print("The sound came from the room next door.")
print("")

continue_game = False

while not continue_game:

      choice = int(input("Go chech the noise(1),  ignore it and continue the path(2)"))
      print("")

      if choice == 1:
          print("He enters the room, but inside there was a horryifing creature ")
          print("The eyes of the creature where glowing with malice, jaws dripping with blackened saliva. ")
          print("Before the knight could raise his sword, claws like shattered bones tore through his armor, ripping flesh and sinew with sickening ease.")
          print("His screams echoed into the darkness as the beast dragged him down, devouring every last shred until silence swallowed the hall forever.")
          print("")
          print("")
          print("YOU DIED")
          print("")

          input("Press enter to choose again ")
          print("")

      elif choice == 2:
          path = (input("You ignored the sound and continue the path"))

          continue_game = True
          print("")
          print("")

battle = input("As you continue the stone path, you see in the distance a thin skeleton walking towards you, without another choice, you prepare your weapons and wait for the battle")
print("")
print("")
print("")
print("*Battle music starts playing*")
print("")
print("Knight: HP: 100")
print("")
print("Skeleton: HP: 120   ATT:  3-8")
def battle_scene(sword = 30, knight = 100, skeleton = 120, bow = random.randint(25,35), sbow = random.randint(3,8)):
    while True:
      try: #Usamos try para manejar errores de entrada, osea si el usuario no ingresa un numero
        attack= int(input("Use: Sword: Damage 30 (1)  Bow: Damage 25-35 (2)"))
      except ValueError: 
         print("Invalid input. Please enter 1 or 2.")
         continue


      if attack == 1:
          print("*SWORD ATTACK -30HP")
          skeleton = (skeleton - sword)
          print(f"Skeleton {skeleton} HP")

      elif attack == 2: 
            print(f"*BOW ATTACK* - {bow} HP")
            skeleton = (skeleton - bow)
            print(f"Skeleton: {skeleton} HP")
        
      else:
         print("Selección inválida. Pierdes tu turno.")


      if skeleton <= 0:
            print("He died")
            print("You won")
            return knight

      print("") 
      ske = input("TURN OF SKELETON")
      print("")
      print("The skeleton aims his bow and shoots at you.")
      knight = (knight - sbow)
      print(f"*KNIGHT - {sbow} HP")
      print(f"Knight: {knight} HP")
      print("")
      print("")

      if knight <= 0:
            print("You died")
            print("Game Over")
            return knight


life_knight = battle_scene()

print(f"Knight's remaining life: {life_knight}")

print("The knight emerged victorious over the skeleton, his blade still glowing with courage. " \
"With the foe defeated, he pressed onward into the castle's depths. Each step echoing his resolve to face whatever darkness lay ahead")

input("Press Enter to continue your adventure...")

print("The knight stepped through the quiet castle hall.In the dim torchlight, he spotted a small dusty chest resting at the far end of the corridor, waiting to be opened.")
cofre = input("Do you want to open the chest? Yes(1) No(2)")
if cofre == "1":
  print("You opened the chest, inside you found a health potion that restores 10 HP")
  if life_knight <=90:
    life_knight +=10
  else:
    life_knight =100
  print(f"Your HP is now: {life_knight}") 
else:
   print("You walked away")

