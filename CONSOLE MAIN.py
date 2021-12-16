import pyttsx3
import os
from os import system , name

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()
 pass
def menu():
    speak("OPENING MENU")
    print("\t MAIN MENU \n INCREASE (I)")
    speak("PRESS I TO INCREASE THE POINT OF THE PLAYER")
    print("\t\tDECREASE (D)")
    speak("PRESS D TO DECREASE THE POINT OF THE PLAYER")
    print("\t\t\t\tSHOW (S)")
    speak("PRESS S TO SHOW SCORE BOARD")
    print("\t\t\t\t\t POSITION (P)")
    speak("PRESS P TO CHECK THE POSITION OF ALL PLAYERS")
    print("\t\t\t\t\t\t\t MEDAL (M)")
    speak("PRESS M TO GIVE THE MEDAL TO ANY PLAYER")
def medmenu():
     speak("OPENING MEDAL MENU")
     print("\t MEDAL MENU \n PLATINUM (P)")
     speak("PRESS P TO GIVE PLATINUM MEDAL")
     print("\t\tGOLD (G)")
     speak("PRESS G TO GIVE GOLD MEDAL")
     print("\t\t\tSILVER (S)")
     speak("PRESS S TO GIVE SILVER MEDAL")
     print("\t\t\t\t BRONZE (B)")
     speak("PRESS B TO GIVE BRONZE MEDAL")
if __name__ == "__main__":
  speak("hello,WELCOME to the console")
  speak("THIS PROGRAM IS CREATED BY Dishant khaattee")
  print("\t\tTHIS PROGRAM IS CREATED BY DK")
  speak("please note that only 4 players can play") 
  system("cls") 
  speak("ENTER THE 1st PLAYER NAME : ")     
  pl1=input("ENTER THE 1st PLAYER NAME : ") 
  speak("ENTER THE 2nd PLAYER NAME : ")     
  pl2=input("ENTER THE 2nd PLAYER NAME : ") 
  speak("ENTER THE 3rd PLAYER NAME : ")     
  pl3=input("ENTER THE 3rd PLAYER NAME : ") 
  speak("ENTER THE 4th PLAYER NAME : ")     
  pl4=input("ENTER THE 4th PLAYER NAME : ") 
  hk="n"  
  system("cls")
  p1=0
  p2=0 
  p3=0
  p4=0
  MG1=0
  MP1=0
  MB1=0
  MS1=0
  MG2=0
  MP2=0
  MB2=0
  MS2=0
  MG3=0
  MP3=0
  MB3=0
  MS3=0
  MG4=0
  MP4=0
  MB4=0
  MS4=0
  menu()
  speak("opening gaming console") 
  os.startfile(r"E:\DB DRIVE\FILES\MY PROJECTS\MY PROGRAMS\PYTHON\CONSOLE\CONSOLEG.py")
  while hk=="n" or hk=="N":
      CHK=input("ENTER YOUR CHOICE : ")
      if CHK=="I" or CHK=="i":
          system("cls")
          speak("enter the player name whose point you want to increase") 
          pl=input("enter the player name whose point you want to increase : ")
          if pl==pl1 :
              speak("current point is")
              speak(p1)
              speak("enter the points")
              p=input("enter the points : ")
              p1=int(p1)+int(p)
              print("NOW POINT",p1)
          elif pl==pl2 :
              speak("current point is")
              speak(p2)
              speak("enter the points")
              p=input("enter the points : ")
              p2=int(p2)+int(p)
              print("NOW POINT : ",p2)
          elif pl==pl3 :
              speak("current point is")
              speak(p3)
              speak("enter the points")
              p=input("enter the points : ")
              p3=int(p3)+int(p)
              print("NOW POINT : ",p3)
          elif pl==pl4 :
              speak("current point is")
              speak(p4)
              speak("enter the points")
              p=input("enter the points : ")
              p4=int(p4)+int(p)
              print("NOW POINT : ",p4)
      elif CHK=="D" or CHK=="d" :
          system("cls")
          speak("enter the player name whose point you want to deccrease") 
          pl=input("enter the player name whose point you want to decrease : ")
          if pl==pl1 :
              speak("current point is")
              speak(p1)
              speak("enter the points")
              p=input("enter the points : ")
              p1=int(p1)-int(p)
              print("NOW POINT : ",p1)
          elif pl==pl2 :
              speak("current point is")
              speak(p2)
              speak("enter the points")
              p=input("enter the points : ")
              p2=int(p2)-int(p)
              print("NOW POINT : ",p2)
          elif pl==pl3 :
              speak("current point is")
              speak(p3)
              speak("enter the points")
              p=input("enter the points : ")
              p3=int(p3)-int(p)
              print("NOW POINT : ",p3)
          elif pl==pl4 :
              speak("current point is")
              speak(p4)
              speak("enter the points")
              p=input("enter the points : ")
              p4=int(p4)-int(p)
              print("NOW POINT : ",p4)
      elif CHK=="s" or CHK=="S" :
          system("cls")
          speak("starting SCORE BOARD")
          print("\t\tSCOREBOARD\n\n player 1 : ",pl1,"\n\n\n\tscore : ",p1,"\n\n\nMEDALS: \n\n\tPLATINUM: ",MP1,"\n\n\tGOLD: ",MG1,"\n\n\n\tSILVER: ",MS1,"\n\n\tBRONZE: ",MB1)
          print("\n\n\t\t\t\t player 2 : ",pl2,"\n\n\t\t\t\t\tscore : ",p2,"\n\n\n\t\t\t\tMEDALS: \n\n\t\t\t\t\tPLATINUM: ",MP2,"\n\n\t\t\t\t\tGOLD: ",MG2,"\n\n\n\t\t\t\t\tSILVER: ",MS2,"\n\n\t\t\t\t\tBRONZE: ",MB2)
          print("\n\n player 3 : ",pl3,"\n\n\tscore : ",p3,"\n\n\nMEDALS: \n\n\tPLATINUM: ",MP3,"\n\n\tGOLD: ",MG3,"\n\n\n\tSILVER: ",MS3,"\n\n\tBRONZE: ",MB3)
          print("\n\n\t\t\t\t player 4 : ",pl4,"\n\n\t\t\t\t\tscore : ",p4,"\n\n\t\t\t\t\nMEDALS: \n\n\t\t\t\t\tPLATINUM: ",MP4,"\n\n\t\t\t\t\tGOLD: ",MG4,"\n\n\n\t\t\t\t\tSILVER: ",MS4,"\n\n\t\t\t\t\tBRONZE: ",MB4)
      elif CHK=="p" or CHK=="P" :
          system("cls")
          speak("positioning all players")
          print("POSITION BOARD")
          if int(p2) > int(p1) and int(p2) > int(p3) and int(p2) > int(p4) :
              pla = pl2
              if int(p1) > int(p3) and int(p1) > int(p4) :
                  plb=pl2
                  if int(p3) > int(p4) :
                      plc=pl3
                      pld=pl4
                  elif int(p3) < int(p4) :
                      plc=pl4
                      pld=pl3    
              elif int(p3) > int(p1) and int(p3) > int(p4) :
                  plb=pl3
                  if int(p1) > int(p4) :
                      plc=pl1
                      pld=pl4
                  elif int(p1) < int(p4) :
                      plc=pl4
                      pld=pl1
              elif int(p4) > int(p1) and int(p4) > int(p3) :
                  plb=pl4
                  if int(p1) > int(p3) :
                      plc=pl1
                      pld=pl3
                  elif int(p1) < int(p3) :
                      plc=pl3
                      pld=pl1
          elif int(p3) > int(p2) and int(p3) > int(p1) and int(p3) >int(p4) :
              pla=pl3
              if int(p1) > int(p2) and int(p1) > int(p4) :
                  plb=pl1
                  if int(p2) > int(p4) :
                      plc=pl2
                      pld=pl4
                  elif int(p2) < int(p4) :
                      plc=pl4
                      pld=pl2    
              elif int(p2) > int(p1) and int(p2) >int(p4) :
                  plb=pl2
                  if int(p1) > int(p4) :
                      plc=pl1
                      pld=pl4
                  elif int(p1) < int(p4) :
                      plc=pl4
                      pld=pl1
              elif int(p4) > int(p1) and int(p4) > int(p2) :
                  plb=pl4
                  if p1>p2 :
                      plc=pl1
                      pld=pl2
                  elif int(p1) < int(p2) :
                      plc=pl2
                      pld=pl1    
          elif int(p4) > int(p2) and int(p4) > int(p1) and int(p4) > int(p3) :
              pla=pl4
              if int(p1) > int(p3) and int(p1) > int(p2) :
                  plb=pl1
                  if int(p3) > int(p2) :
                      plc=pl3
                      pld=pl2
                  elif int(p3) < int(p2) :
                      plc=pl2
                      pld=pl3    
              elif int(p3) > int(p1) and int(p3) > int(p2) :
                  plb=pl3
                  if int(p1) > int(p2) :
                      plc=pl1
                      pld=pl2
                  elif int(p1) < int(p2) :
                      plc=pl2
                      pld=pl1
              elif int(p2) > int(p1) and int(p2) > int(p3) :
                  plb=pl2
                  if int(p1) > int(p3) :
                      plc=pl1
                      pld=pl3
                  elif int(p1) < int(p3) :
                      plc=pl3
                      pld=pl1
          else:
             system("cls")
             speak("all have equal points using their place to position")
             pla=pl1
             plb=pl2
             plc=pl3
             pld=pl4          
          print("1st ",pla,"  WINNER") 
          print("2nd ",plb,"  RUNNER-UP")
          print("3rd ",plc,"  QUALIFIER")
          print("4th ",pld,"  LEAST-QUALIFIER") 
      elif CHK=="m" or CHK=="M":
          system("cls")
          k="y"
          while(k=="y" or k=="Y"):
             medmenu()
             CH=input("ENTER YOUR CHOICE : ")
             if CH=="P" or CH=="p" :
                  play=input("enter the player name: ")
                  if play==pl1:
                      MP1=MP1+1
                  elif play==pl2:
                      MP2=MP2+1
                  elif play==pl3:
                      MP3=MP3+1
                  elif play==pl4:
                      MP4=MP4+1
             if CH=="G" or CH=="g" :
                  play=input("enter the player name: ")
                  if play==pl1:
                      MG1=MG1+1
                  elif play==pl2:
                      MG2=MG2+1
                  elif play==pl3:
                      MG3=MG3+1
                  elif play==pl4:
                      MG4=MG4+1
             if CH=="S" or CH=="s" :
                  play=input("enter the player name: ")
                  if play==pl1:
                      MS1=MS1+1
                  elif play==pl2:
                      MS2=MS2+1
                  elif play==pl3:
                      MS3=MS3+1
                  elif play==pl4:
                      MS4=MS4+1
             if CH=="b" or CH=="B" :
                  play=input("enter the player name: ")
                  if play==pl1:
                      MB1=MB1+1
                  elif play==pl2:
                      MB2=MB2+1
                  elif play==pl3:
                      MB3=MB3+1
                  elif play==pl4:
                      MPB4=MB4+1
             k=("WANT TO ENTER MORE (y/n)")                                    
      else :
          system("cls")
          speak("WRONG INPUT!!!")
          print("INPUT: ",CHK," DOES NOT EXIST")
      speak("want to exit the console")
      hk=input("want to exit (y/n) : ")
      if hk=="N" or hk=="n" :
          system("cls")
          speak("REOPENING MENU")
          print("\t MAIN MENU \n INCREASE (I)")
          print("\t\tDECREASE (D)")
          print("\t\t\t\tSHOW (S)")
          print("\t\t\t\t\t POSITION (P)")
          print("\t\t\t\t\t\t\t MEDAL (M)")
  speak("QUITING CONSOLE")
  speak("good bye")    