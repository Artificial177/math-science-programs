HAI 1.2
CAN HAS STDIO?
    OBTW
       Essentially, the final grade for my chemistry class was supposed to be 
       2/9 * each quarter grade + 1/9 * the final exam. With the final exam removed,
       this (nonsensical) script calculates the value that the fourth quarter needs to 
       be (after the final exam has been administered) to allow the actual final grade
       to be the same with each quarter being a quarter of the final grade.
    TLDR
       
    I HAS A FIRSTQ ITZ A YARN
    I HAS A SECONDQ ITZ A YARN
    I HAS A THIRDQ ITZ A YARN
    I HAS A FOURTHQ ITZ A YARN
    I HAS A FINALEXAM ITZ A YARN
       
    VISIBLE "ENTER Q1 GRADE"
    GIMMEH FIRSTQ BTW GET INPUT (INT) INTO VARIABLE
    VISIBLE "ENTER Q2 GRADE"
    GIMMEH SECONDQ BTW GET INPUT (INT) INTO VARIABLE
    VISIBLE "ENTER Q3 GRADE"
    GIMMEH THIRDQ BTW GET INPUT (INT) INTO VARIABLE
    VISIBLE "ENTER Q4 GRADE"
    GIMMEH FOURTHQ BTW GET INPUT (INT) INTO VARIABLE
    VISIBLE "ENTER FINAL EXAM GRADE"
    GIMMEH FINALEXAM BTW GET INPUT (INT) INTO VARIABLE
       
    I HAS A FIRSTINC ITZ 0.111111111111
    I HAS A SECONDINC ITZ 0.222222222222
       
    I HAS A TRADITIONALFINAL ITZ PRODUKT OF FIRSTQ AN SECONDINC
    I HAS A TEMP ITZ PRODUKT OF SECONDQ AN SECONDINC
    TRADITIONALFINAL R SUM OF TRADITIONALFINAL AN TEMP
    TEMP R PRODUKT OF THIRDQ AN SECONDINC
    TRADITIONALFINAL R SUM OF TRADITIONALFINAL AN TEMP
    TEMP R PRODUKT OF FOURTHQ AN SECONDINC
    TRADITIONALFINAL R SUM OF TRADITIONALFINAL AN TEMP
    TEMP R PRODUKT OF FINALEXAM AN FIRSTINC
    TRADITIONALFINAL R SUM OF TRADITIONALFINAL AN TEMP
   
    TRADITIONALFINAL R PRODUKT OF TRADITIONALFINAL AN 4
    I HAS A NECESSARYGRADE ITZ DIFF OF TRADITIONALFINAL AN FIRSTQ
    NECESSARYGRADE R DIFF OF NECESSARYGRADE AN SECONDQ
    NECESSARYGRADE R DIFF OF NECESSARYGRADE AN THIRDQ
    
    I HAS A OUTPUTGRADE ITZ A YARN
    OUTPUTGRADE R NECESSARYGRADE
    VISIBLE SMOOSH "Calculated Q4 Grade: " OUTPUTGRADE MKAY
KTHXBYE

