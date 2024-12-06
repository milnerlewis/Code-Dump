import time

import easygui

# Opening statement ~-~

easygui.msgbox("Welcome to the Computer Storage Quiz!\n\nPlease note that spelling does matter in this test and marks can be lost for misspelt words or phrases.\n\nPlease press the 'ok' button to begin, I wish you luck!")

# # # End of opening statement ~-~


# Placeholder variable ~-~

questions_num = "20"

correct_answers = int(0)

# # End of Placeholder variable ~-~

# Questions ~-~

answer_1 = easygui.textbox('\n\nWhat is a type of "main memory"?')

answer_2 = easygui.textbox('\nWhat does "Volatile" mean? ')

answer_3 = easygui.textbox('\nIs "RAM" Volatile? ')

answer_4 = easygui.textbox('\nWhat is cheeper per GB, RAM or a HDD? ')

answer_5 = easygui.textbox('\nWhat does "ROM" stand for? ')

answer_6 = easygui.textbox('\nIs the "ROM" wiped when a system is shut down/turned off? ')

answer_7 = easygui.textbox('\nCan you Read and Write to the "RAM"? ')

answer_8 = easygui.textbox('\nWhat does "WAN" mean? ')

answer_9 = easygui.textbox('\nWhat does "PAN" mean? ')

answer_10 = easygui.textbox('\nTrue or False, a "WAN" is cheaper to set up than a "LAN". ')

answer_11 = easygui.textbox('\nTrue or False, a "PAN" can be used to control devices. ')

answer_12 = easygui.textbox('\nTrue or False, a "LAN" needs wires to work. ')

answer_13 = easygui.textbox('\nA network covers two buildings, the buildings are connected without crossing a road. Is this a "LAN", "WAN" or a "PAN"? ')

answer_14 = easygui.textbox('\nYour smartwatch connects to your phone. Is this "LAN", "WAN" or a "PAN"? ')

answer_15 = easygui.textbox('\nIs the World Wide Web a network? If yes then what network "LAN", "WAN" or "PAN"? ')

answer_16 = easygui.textbox('\n!!!THIS QUESTION IS MULTIPLE CHOICE, PLEASE SELECT THE NUMBER OF THE ANSWER THAT YOU WISH TO SELECT!!!\nWhich of the below is a True statement about networks:\n\n1. Does not need any hardware.\n2. Can be stand-alone.\n3. Can control devices.\n4. If a central device goes down, the network still works.\n\nYour answer (Number of point): ')

answer_17 = easygui.textbox('\nWhat does "P2P" stand for in networking? ')

answer_18 = easygui.textbox('\nHow are clients connected in a "Client-server" network? ')

answer_19 = easygui.textbox('\nName the network which contains clients with no local storage or processing. ')

answer_20 = easygui.textbox('\nTrue or False:\n\nA Thin client network costs more than a Client-server network due to having smaller, more expensive components inside.')

# # # End of Questions ~-~


# Marking section ~-~

answer_1 = answer_1.lower()

if "hdd" in answer_1 or "ram" in answer_1 or "rom" in answer_1:

    correct_answers += 1

    answer_1 = "Correct"

else:

    answer_1 = "Incorrect"

# # # # # Question spacer ~-~

answer_2 = answer_2.lower()

if ("data" in answer_2 and "removed" in answer_2) or ("data" in answer_2 and "wiped" in answer_2) or ("data" in answer_2 and "lost" in answer_2):

    correct_answers += 1

    answer_2 = "Correct"

else:

    answer_2 = "Incorrect"

# # # # # Question spacer ~-~

answer_3 = answer_3.lower()

if "ye" in answer_3 or "yes" in answer_3:

    correct_answers += 1

    answer_3 = "Correct"

else:

    answer_3 = "Incorrect"

# # # # # Question spacer ~-~

answer_4 = answer_4.lower()

if "hdd" in answer_4:

    correct_answers += 1

    answer_4 = "Correct"

else:

    answer_4 = "Incorrect"

# # # # # Question spacer ~-~

answer_5 = answer_5.lower()

if "read" in answer_5 and "only" in answer_5 and "memory" in answer_5:

    correct_answers += 1

    answer_5 = "Correct"

else:

    answer_5 = "Incorrect"

# # # # # Question spacer ~-~

answer_6 = answer_6.lower()

if "no" in answer_6:

    correct_answers += 1

    answer_6 = "Correct"

else:

    answer_6 = "Incorrect"

# # # # # Question spacer ~-~

answer_7 = answer_7.lower()

if "ye" in answer_7:

    correct_answers += 1

    answer_7 = "Correct"

else:

    answer_7 = "Incorrect"

# # # # # Question spacer ~-~

answer_8 = answer_8.lower()

if "wide" in answer_8 and "area" in answer_8 and "network" in answer_8:

    correct_answers += 1

    answer_8 = "Correct"

else:

    answer_8 = "Incorrect"

# # # # # Question spacer ~-~

answer_9 = answer_9.lower()

if "personal" in answer_9 and "area" in answer_9 and "network" in answer_9:

    correct_answers += 1

    answer_9 = "Correct"

else:

    answer_9 = "Incorrect"

# # # # # Question spacer ~-~

answer_10 = answer_10.lower()

if "fal" in answer_10:

    correct_answers += 1

    answer_10 = "Correct"

else:

    answer_10 = "Incorrect"

# # # # # Question spacer ~-~

answer_11 = answer_11.lower()

if "tr" in answer_11:

    correct_answers += 1

    answer_11 = "Correct"

else:

    answer_11 = "Incorrect"

# # # # # Question spacer ~-~

answer_12 = answer_12.lower()

if "fal" in answer_12:

    correct_answers += 1

    answer_12 = "Correct"

else:

    answer_12 = "Incorrect"

# # # # # Question spacer ~-~

answer_13 = answer_13.lower()

if "lan" in answer_13:

    correct_answers += 1

    answer_13 = "Correct"

else:

    answer_13 = "Incorrect"

# # # # # Question spacer ~-~

answer_14 = answer_14.lower()

if "pan" in answer_14:

    correct_answers += 1

    answer_14 = "Correct"

else:

    answer_14 = "Incorrect"

# # # # # Question spacer ~-~

answer_15 = answer_15.lower()

if "wan" in answer_15:

    correct_answers += 1

    answer_15 = "Correct"

else:

    answer_15 = "Incorrect"

# # # # # Question spacer ~-~

answer_16 = answer_16.lower()

if "3" in answer_16 or "three" in answer_16:

    correct_answers += 1

    answer_16 = "Correct"

else:

    answer_16 = "Incorrect"

# # # # # Question spacer ~-~

answer_17 = answer_17.lower()

if "peer" in answer_17 and "to" in answer_17:

    correct_answers += 1

    answer_17 = "Correct"

else:

    answer_17 = "Incorrect"

# # # # # Question spacer ~-~

answer_18 = answer_18.lower()

if "server" in answer_18 or "connect" in answer_18:

    correct_answers += 1

    answer_18 = "Correct"

else:

    answer_18 = "Incorrect"

# # # # # Question spacer ~-~

answer_19 = answer_19.lower()

if "thin" in answer_19 and "client" in answer_19:

    correct_answers += 1

    answer_19 = "Correct"

else:

    answer_19 = "Incorrect"

# # # # # Question spacer ~-~

answer_20 = answer_20.lower()

if "false" in answer_20:

    correct_answers += 1

    answer_20 = "Correct"

else:

    answer_20 = "Incorrect"

# # # End of Marking section ~-~


# Results section ~-~

easygui.msgbox(f"\n\n\n\n\nYou got {correct_answers}/{questions_num} correct.")

if int(correct_answers) < 8:

    easygui.msgbox("\nYou should revise more often so you can get more questions right.")

if int(correct_answers) > 8 and int(correct_answers) < 12:

    easygui.msgbox("\nYou did good and have great core knowledge, maybe try to test yourself more and aim to focus on the areas which you dont get correct.")

if int(correct_answers) > 12:

    easygui.msgbox("\nGreat job! Keep up your current levels of revision and testing and you'll only get better from here!")

deep_results = easygui.textbox("\n\nWould you like to see your in depth results (y/n)? ")

deep_results = deep_results.lower()

if "y" in deep_results:

    easygui.msgbox(f"\n\n\n\n\nHere is your results for each individual question:\n1.  {answer_1}\n2.  {answer_2}\n3.  {answer_3}\n4.  {answer_4}\n5.  {answer_5}\n6.  {answer_6}\n7.  {answer_7}\n8.  {answer_8}\n9.  {answer_9}\n10. {answer_10}\n11. {answer_11}\n12. {answer_12}\n13. {answer_13}\n14. {answer_14}\n15. {answer_15}\n16. {answer_16}\n17. {answer_17}\n18. {answer_18}\n19. {answer_19}\n20. {answer_20}")

easygui.msgbox("Thank you for taking the test.")# # End of Results section ~-~