import java.util.Scanner;
import java.util.Arrays;
import java.lang.String;
import java.lang.Object;
import java.lang.Character;

/*
Console-based Hangman, with multiple difficulty settings.
*/

public class Main {
  public static void main(String[] args) throws InterruptedException{
    Scanner reader = new Scanner(System.in);

    System.out.println("HANGMAN");
    int startGame = 0;
    int gameMustStart = 0;

    while(startGame == 0)
    {
      System.out.println("\nWelcome to Hangman! Choose your difficulty: (Easy) (Medium) (Hard) (Insane) (Do Not Enter)");
      String dif = reader.nextLine();
      gameMustStart = difChoose(dif);

      if(gameMustStart > 30)
        System.out.println("Sorry, I didn't understand that! Please enter \"Easy\", \"Medium\", \"Hard\", \"Insane\", or \"Do Not Enter\".");
      else
        startGame = 66;
    }

    String theWord = wordChoose(gameMustStart);
    
    if(gameMustStart == 5)
      System.out.println("\nWell, you were warned!");
    else
      System.out.println("\nExcellent!");
    Thread.sleep(900);
    System.out.print("Choosing a word");
    Thread.sleep(900);
    System.out.print(".");
    Thread.sleep(900);
    System.out.print(".");
    Thread.sleep(900);
    System.out.println(".");
    Thread.sleep(900);
    
    int gameDone = 6;
    int turnRound = 0;
    int wordLength = theWord.length();
    String letters = "";
    char guesses[] = new char [wordLength];
    char wordParallel[] = new char [wordLength];
    int theGameIsOver = 0;
    int userGameDone = 15;

    System.out.println("\nWord Found!");
    Thread.sleep(900);
    System.out.println("Here's your word: ");
    for (int i = 0; i < wordLength; i++)
    {
      guesses[i] = '_';
      System.out.print(guesses[i] + " ");
    }
    System.out.println("\n\nYou are allowed 6 missed letters before you lose. Start guessing!");
    Thread.sleep(900);

    String theLowerWord = theWord.toLowerCase();

    for (int i = 0; i < guesses.length; i++)
    {
      guesses[i] = '_';
      wordParallel[i] = theLowerWord.charAt(i);
    }

    //System.out.println("\n\n\n\n" + theWord + "\n\n\n\n"); 
    //To play the game while knowing the word, uncomment the above line so that it prints out your word.
    while (userGameDone != 0)
    {
      theWord = wordChoose(gameMustStart);
      int userScore = 0;
      gameDone = 6;
      System.out.print("Choosing a word");
      Thread.sleep(900);
      System.out.print(".");
      Thread.sleep(900);
      System.out.print(".");
      Thread.sleep(900);
      System.out.println(".");
      Thread.sleep(900);
      System.out.println("\nWord Found!");
      Thread.sleep(900);
      System.out.println("Here's your word: ");
      for (int i = 0; i < wordLength; i++)
      {
        guesses[i] = '_';
        System.out.print(guesses[i] + " ");
      }
      System.out.println();
    
      while (gameDone != 0)
      {
        System.out.println("Misses Left: " + gameDone);
        System.out.print("Letters Guessed: " + letters);
        System.out.println("");
        System.out.println("Your Guess: ");
        char theSomewhatGuess = reader.next().charAt(0);
        char theGuess = Character.toLowerCase(theSomewhatGuess);
        letters += theGuess;
        letters += " ";
        turnRound++;

        int roundTotalGuess = 0;

        for (int i = 0; i < wordLength; i++)
        {
          if (theGuess == wordParallel[i])
          {
            guesses [i] = wordParallel[i];
            roundTotalGuess++;
          } 
        }

        int totalBlanks = 0;

        for(int i = 0; i < wordLength; i++)
        {
          if (guesses[i] == ('_'))
            totalBlanks++;
        }

        if (roundTotalGuess == 0 && gameDone != 0)
        {
          System.out.println(theGuess + " was not in the word! Try Again!");
          gameDone--;
        }
        else if (roundTotalGuess == 0 && gameDone == 0)
        {
          System.out.println(theGuess + " was not in the word!\nYou've Been Hung! The correct word was " + theWord);
          theGameIsOver = 5;
        }
        else if (roundTotalGuess > 0 && totalBlanks == 0)
        {
          System.out.println(theGuess + " was in the word!\nYou've Guessed the Word Correctly! Congratulations!");
          gameDone = 0;
          theGameIsOver = 5;
          userScore++;
        }
        else if (roundTotalGuess > 0 && totalBlanks > 0 && gameDone == 0)
        {
          System.out.println(theGuess + " was in the word!\nYou've Been Hung! The correct word was " + theWord);
        }
        else if (roundTotalGuess > 0 && totalBlanks > 0 && gameDone != 0)
        {
          System.out.println(theGuess + " was in the word!\nContinue Guessing and see if you can find the word!");
        }

        System.out.println();

        if (theGameIsOver != 5)
        {
          for (int i = 0; i < wordLength; i++)
          {
            System.out.print(guesses[i] + " ");
          }
        }

        System.out.println("\n\n");

      }

      System.out.println("Would you like to play again? (yes) or (no)");
      reader.nextLine();
      String userChoiceNow = reader.nextLine();
      if(userChoiceNow.equalsIgnoreCase("yes"))
      {
        System.out.println("Great!");
        System.out.println("Your score is: " + userScore);
      }
      else if (userChoiceNow.equalsIgnoreCase("no"))
      {
        System.out.println("Your final score was: " + userScore);
        System.exit(0);
      }

    }

  }

  public static int difChoose (String thestring)
  {
    int returner = 0;
    if (thestring.equalsIgnoreCase("Easy"))
      returner = 1;
    else if (thestring.equalsIgnoreCase("Medium"))
      returner = 2;
    else if (thestring.equalsIgnoreCase("Hard"))
      returner = 3;
    else if (thestring.equalsIgnoreCase("Insane"))
      returner = 4;
    else if (thestring.equalsIgnoreCase("Do Not Enter"))
      returner = 5;
    else
      returner = 45;

    return returner;
  }

  public static String wordChoose (int thedif)
  {
    int theRandom = (int)(Math.random()*10);
    String thereturner = "Hello";
    String easy[] = {"Damp", "Reading", "Apple", "Bucket", "Closing", "Tissue", "Laptop", "Forest", "Pencil", "Bread"};
    String medium[] = {"Events", "Driver", "Butterfly", "Clover", "Computer", "Toothbrush", "Textbook", "Futuristic", "Program", "Mousepad"};  
    String hard[] = {"Flounder", "Psychic", "Jester", "Strength", "Kangaroo", "Motionless", "Carpenter", "Corkboard", "Finale", "Anteater"};
    String insane[] = {"Aardvark", "Paradox", "Xylophone", "Supernova", "Ganache", "Projectile", "Finesse", "Unabashed", "Environment", "Flourish"};
    String doNotEnter[] = {"Paraphernalia", "Stoichiometry", "Pterodactyl", "Ganache", "Fractal", "Sophistication", "Rhinovirus", "Labyrinth", "Poltergeist", "Phantasmal" };

    if (thedif == 1)
      thereturner = easy[theRandom];
    else if (thedif == 2)
      thereturner = medium[theRandom];
    else if (thedif == 3)
      thereturner = hard[theRandom];
    else if (thedif == 4)
      thereturner = insane[theRandom];
    else if (thedif == 5)
      thereturner = doNotEnter[theRandom];

    return thereturner;
  }

  
}
