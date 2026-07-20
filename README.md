# ET_DOC
test database for openET documentation

Readme:

STEPS TO PERSONALIZE YOUR CODE.

Assuming you are following the steps in the documentation file (shown above as documentation.txt), you have reached the point where you imported the repository from our own. Now, in order to get these files working for you, you must make some slight, and very easy changes. The first is creating two "secrets" in GitHub. Secrets in GitHub are essentially names that store a secret value, and they will be used here to store your OpenET API key, and your MongoDB connection string. Here is how it will work. In your repository click on settings 
<img width="975" height="410" alt="image" src="https://github.com/user-attachments/assets/549a8b17-b4fe-47d3-ab0c-3dd25fa32e7a" />

then on the setting page, scroll down until you see the “secrets and variables” dropdown. Click it, then click “Actions”
<img width="975" height="418" alt="image" src="https://github.com/user-attachments/assets/953eab1b-a6cf-4f35-9b2c-1542a5fc628c" />

 
This will take you to the secrets and variables page. Here you will click on the green “New repository secret.” For the first one, we will do the OpenET API key, name it OPEN_ET_KEY exactly, then paste the api key exactly as it is into the box that says “secret.” Repeat this process for the MongoDB connection string, naming it MDB_STRING Make a note of what you have named these secrets.
Now go back to the home page of the repository. Now that we have created our secrets it is now time to adjust the code. Start by clicking on the CODE_FOR_ET.py file. Click on the pencil icon on the top right to edit the code, and follow the instructions in the grayed out “comments” (the text that appears after the # sign. If it gives you an instruction, follow it exactly, if it does not, then it is information for programmers that you do not have to understand, but keep reading as it may lead to understandable instructions). Once you are done editing, press the green “commit changes” button at the top, write a message for yourself about what you changed, and press “commit.” 
Now go to the home page again and click on the .github/workflows file. Click on the automation_script.yml and again click on the pencil to edit. Read through the text after the # signs. Make any adjustments you need. When it tells you to put the name of your script, insert CODE_FOR_ET.py exactly. Once you are done editing, press the green “commit changes” button at the top, write a message for yourself about what you changed, and press “commit.” 

TESTING YOUR CODE
On your browser, log into MongoDB and access the database that your connection string is going to. Have it ready to refresh, as, if our code works, you will see new ET data going into your database. 
Go to your repository, and on the homepage, click “Actions.” 
<img width="975" height="419" alt="image" src="https://github.com/user-attachments/assets/0c34ce96-4dc4-44e3-89d3-d260aa0ffe0c" />

 
Once there, on the left hand side of the screen, you should see a button that says “Run My Daily Script” or whatever you named it inside our automation_script.yml file. Click on it.
<img width="975" height="414" alt="image" src="https://github.com/user-attachments/assets/777de8a8-2e4d-47ae-90c4-ab43ff9033bf" />

 
On the right, find the button that says “run workflow” press it, then press the button under it that says “run workflow.” This should activate your code.
If it succeeds, (it may take a while), refresh your MongoDB database, and you should see some new data there.
