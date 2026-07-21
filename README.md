STEPS TO PERSONALIZE YOUR CODE.

Assuming you are following the steps in the documentation file (shown above as documentation.txt), you have reached the point where you imported the repository from our own. Now, in order to get these files working for you, you must make some slight, and very simple changes. The first is creating two "secrets" in GitHub. Secrets in GitHub are essentially names that store a secret value such as password or API keys that should not be visible to the public, and they will be used here to store your OpenET API key, and your MongoDB connection string. Here is how it will work. In your repository click on settings 
<img width="975" height="410" alt="image" src="https://github.com/user-attachments/assets/d1a91129-40e4-4137-9522-ddf934aca11d" />

then on the setting page, scroll down until you see the “secrets and variables” dropdown. Click it, then click “Actions”
<img width="975" height="418" alt="image" src="https://github.com/user-attachments/assets/98bb8cba-7008-4e95-9c9b-263dd8b44bbb" />

 
This will take you to the secrets and variables page. Here you will click on the green “New repository secret.” (NOT “new environment variable/secret”) For the first time, we will do the OpenET API key, name it OPEN_ET_KEY exactly, then paste your unique OpenET API key exactly as it is into the box that says “secret.” Make sure when you paste it that there are no spaces before or after the string of characters and numbers, it must be exact. Repeat this process for the MongoDB connection string, naming it MDB_STRING exactly. Make sure to include the _ underscore signs instead of spaces for both names.
Now go back to the home page of the repository. Now that we have created our secrets it is now time to adjust the code. Start by clicking on the CODE_FOR_ET.py file. Click on the pencil icon on the top right to edit the code, 
<img width="975" height="373" alt="image" src="https://github.com/user-attachments/assets/c8b0957a-5d0b-4862-95cb-769c153b029a" />

 and follow the instructions in the grayed out “comments” (the text that appears after the # sign. If it gives you an instruction, follow it exactly, if it does not, then it is information for programmers that you do not have to understand, but keep reading as it may lead to understandable instructions. Once you are done editing, press the green “commit changes” button at the top, write a message for yourself in the message box about what you changed, and press “commit.” 
Now go to the home page again and click on the .github/workflows file. Click on the automation_script.yml and again click on the pencil to edit. Read through the text after the # signs. Make any adjustments it tells you to make. When it tells you to put the name of your script, insert CODE_FOR_ET.py exactly. Once you are done editing, press the green “commit changes” button at the top, write a message for yourself about what you changed, and press “commit.” 

TESTING YOUR CODE
On your browser, log into MongoDB and access the database that your connection string is going to. Have it ready to refresh, as, if our code works, you will see new ET data going into your database. 
Go to your repository, and on the homepage, click “Actions.” 
<img width="975" height="419" alt="image" src="https://github.com/user-attachments/assets/ca090d7c-15ca-485a-bc7d-9750cb881978" />

 
Once there, on the left hand side of the screen, you should see a button that says “Run My Daily Script” or whatever you named it inside our automation_script.yml file. Click on it.
<img width="975" height="414" alt="image" src="https://github.com/user-attachments/assets/a762505a-8d7a-4d21-9c9b-d9471e074436" />

 
On the right, find the button that says “run workflow” press it, then press the button under it that says “run workflow.” This should activate your code.
If it succeeds, (it may take a while), refresh your MongoDB database, and you should see some new data there. If it does not work, you will see the “run-my-script-job” box with a red X sign on it. Like this:
<img width="975" height="413" alt="image" src="https://github.com/user-attachments/assets/b4add8cf-44be-4e23-b5d4-75322745b1e5" />

 
Click on that X and you will be able to investigate what went wrong. The code we wrote contains some error handling which might be able to give you some clues as to anything that happened. 
