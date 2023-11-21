import random
def print_color(text, color):
  colors = {
      'reset': '\033[0m',
      'green': '\033[92m',
      'red': '\033[91m',
      'yellow': '\033[93m',
      'blue': '\033[94m',
      'purple': '\033[95m',
      'cyan': '\033[96m',
      'bright_green': '\033[1;92m',
      'bright_red': '\033[1;91m',
      'bright_yellow': '\033[1;93m',
      'bright_blue': '\033[1;94m',
      'bright_purple': '\033[1;95m',
      'bright_cyan': '\033[1;96m'



  }
  print(colors[color] + text + colors['reset'])


def juste_prix():
  def ask_int(message):
      while True:
          try:
              nombre = int(input(message))
              return nombre
          except ValueError:
              print_color("Erreur : Veuillez entrer un nombre valide.", 'red')

  def play_again():
      print_color("☆:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆" + "\n", 'purple')
      print_color("Bienvenue au jeu du Plus ou Moins!"+ "\n", 'yellow')

      print_color("☆:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆" + "\n", 'purple')
      print_color("Le but du jeu est de trouver le nombre mystère en moins de coups possibles.", 'yellow')
      a = ask_int("Choisissez le numéro minimum de la fourchette : ")
      b = ask_int("Choisissez le numéro maximum de la fourchette : ")

      nbessaie = 0
      nombre_aleatoire = random.randint(a, b)
      guess = 0

      while guess != nombre_aleatoire and nbessaie < 10:
          nbessaie += 1
          guess = ask_int("Entrez un nombre entre " + str(a) + " et " + str(b) + " : ")

          if guess < nombre_aleatoire:
              print_color("C'est plus que" + " " + str(guess), 'green')
          elif guess > nombre_aleatoire:
              print_color("C'est moins que" + " " + str(guess), 'red')

      if guess == nombre_aleatoire and nbessaie<=10:
          print_color("Bravo, vous avez trouvé le nombre !", 'green')
          print_color("Le nombre était bel et bien" + " " + str(nombre_aleatoire), 'green')
          print_color("Vous avez trouvé en : " + str(nbessaie) + " essais.", 'green')
      else:
          print_color("PERDU ! Vous avez dépassé les 10 essais.", 'red')

      return input("Voulez-vous rejouer ? (Oui/Non) : ").lower() == "oui"

  while play_again():
      pass
juste_prix()