Please install the following before running our code:
1) googletrans (sudo pip install googletrans)

We have also used TKinter to make the GUI. Usually TKinter comes pre-installed with python. If you don't have TKinter, please install that too.

To run our code, cd to the repository and execute "python GUI.py'. The values printed to the console are for testing purposes only. The GUI will pop up in a separate window. Please use the GUI only to interact with our app. Ignore anything in the console. It takes around 50 seconds for the data to train. The GUI is generated only after the data is trained. Please be patient!

ABOUT OUR PROJECT:

We have built a python app to help people who don't know English very well. Many times, bilinguals(good at native language, intermediate level at english) know the word they want to use in their native language, but don't know its English translation. There are also times when bilinguals would like to know what English word should come next. Our app gives the user suggestions in their native language and when the users select the word in their native language, the English word is inserted in the textbox.



VISUAL REACH(Parth Aggarwal and Jacob Rockwell):

For the visual reach, we have implemented a GUI. The GUI allows users to select their native language using a drop box. Then it prompts the user to type in a text box. After the user types a few words and presses a space, the GUI takes these words and passes it to the data reach part of the project which returns suggestions for the next words. Suggestions start appearing only after a few words have been typed and there is a space between the last word and the cursor. These suggestions are translated to the user's native language using the googletrans api. The suggestions in the native language are then printed on the buttons. The user can click one of the buttons to insert the suggestion. When the user clicks a button, the English word is inserted in the text box. The user can also press numbers 1,2, or 3 to insert the corresponding suggestions. 

DATA REACH(Abhinav Saksena and Reuben Gutmann):

We have trained our models on the following two datasets: 1) The Santa Barbara corpus: a collection of conversations in English amounting to 249000 words and 2) The Cornell Movie-Dialogues corpus: A collection of 220000 fictional conversations taken from movie scripts. We first cleaned the data in these datasets using a modified version of the loadLyrics() helper function. We then trained all the models using our trainModel() functions implemented in the core. After this, we ranked the choice of words in the candidate dictionary, and returned the top three choices. In order to ensure that there were no conflicts with GUI, we wrote a function in generate.py that switches to the next best model depending on the number of choices the preferred model produces in case the number of choices is less than three. 

