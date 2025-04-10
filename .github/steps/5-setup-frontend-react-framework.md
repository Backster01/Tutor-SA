## Step 5: Setup the frontend React framework, update the components, and start tutoring-sa  app

In this step, we will accomplish the following:

- Setup the tutoring-sa frontend React framework.
- Update the following components to include the React framework:
  - src/App.js
  - src/index.js
  - src/components/CAPS-Aligned_Curriculum.js
  - src/components/Interactive_Learning_Experience.js
  - src/components/Assessment_System.js
  - src/components/Users.js
  - src/components/Progress_Tracking_&_Reporting.js
  - src/components/Content_Management_System
  - src/components/Lesson_Management_System
  - src/components/Assessment_Management_System
  - src/components/Subject_Management_Pages
  - src/components/Content_versioning

- Start the React app and check the output.

1. Open all files in the `docs` folder and keep this file open in the editor throughout this exercise.
    1.  agent mode uses `tutor-sa.md` and `tutor-sa_story.md` as a reference to create the application
2. Copy and paste the following prompt(s) in the GitHub Copilot Chat and select the "Agent" instead of "Ask" or "Edit" from the drop down where you are inserting the prompt.

> 🪧 **Note:** 
- Do not change the model from GPT-4o this will be an optional activity at the end of the course.
- Keep in mind that the Copilot agent mode is conversational so it may ask you questions and you can ask it questions too.
- Wait a moment for the Copilot to respond and press the continue button to execute commands presented by Copilot agent mode.
- Keep files created and updated by Copilot agent mode until it is finished.
- Agent mode has the ability to evaluate your code base and execute commands and add/refactor/delete parts of your code base and automatically self heal if it or you makes a mistake in the process.

### :keyboard: Activity: Install the tutoring-sa frontend React framework

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Based on the example tutoring sa app in the docs/tutor-sa.md file and use tutoring-sa as the name for schools app. Let's setup codespace for the tutoring-sa frontend React framework.
>
> 1. Make the tutoring-sa/frontend directory.
> 2. Create the react app in the tutoring-sa/frontend directory.
> 3. Install stable versions of React framework and modules based on docs/tutor-sa.md.
> 4. Install stable bootstrap in the tutoring-sa/frontend directory.
> 5. Import bootstrap css in the src/index.js file.
> 6. Install the stable react-router-dom in the tutoring-sa/frontend directory.
> 7. Don't change .gitignore file
>
> Don't proceed with the next activity until all of these steps are completed.
>```

### :keyboard: Activity: Update the tutoring-sa frontend React components

> 🪧 **Note:** 
- Make sure to replace [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME] with your codespace name.
  - ex. redesigned-spork-g6pj46rr9hpp6x
- You can get the codespace name by running the following command in the terminal: `echo $CODESPACE_NAME`.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Based on the example tutoring-sa app in the docs/tutor-sa.md file and use tutoring-sa as the name for schools app. Let's update the tutoring-sa frontend React components.
>
> - Update the following components to include the React framework to point to the backend API:
>   - src/App.js
  - src/index.js
  - src/components/CAPS-Aligned_Curriculum.js
  - src/components/Interactive_Learning_Experience.js
  - src/components/Assessment_System.js
  - src/components/Users.js
  - src/components/Progress_Tracking_&_Reporting.js
  - src/components/Content_Management_System
  - src/components/Lesson_Management_System
  - src/components/Assessment_Management_System
  - src/components/Subject_Management_Pages
  - src/components/Content_versioning
> - In each component replace the fetch url with the codespace url https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/api/<component> for the Django rest framework backend.
> - Make sure to use the correct port and protocol http or https.
> - Update src/App.js to include the main navigation for all components.
> - Make sure react-router-dom is used for the navigation menu.
> - The react app should show the navigation menu and the components.
>
> Don't proceed with the next activity until all of these steps are completed.
> ```

> ❕ **Important:**
- Make sure to replace [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME] with your codespace name.
  - ex. redesigned-spork-g6pj46rr9hpp6x
- You can get the codespace name by running the following command in the terminal: `echo $CODESPACE_NAME`.

### :keyboard: Activity: Start the react app and check the output

Now, let's actually try running the react application! In the left sidebar, select the `Run and Debug` tab and then press the **Start Debugging** icon.

<img src="https://github.com/user-attachments/assets/8ab08e4e-539a-4ca9-8270-be4b1f0df176"  width=30% height=30%>

### :keyboard: Activity: Let's add some formatting, structuring, and styling to the tutoring-sa  app

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Based on the example tutoring-sa app in the docs/tutor-sa.md file and use tutoring-sa as the name for schools app. Let's style this like App.css and make it look nice.
>
> - Let's make the App.js and all components javascript files in the app are consistent with the following:
>   - Use bootstrap tables for the data in all javascript components.
>   - Use bootstrap buttons for the buttons.
>   - Use bootstrap headings for the headings.
>   - Use bootstrap links for the links.
>   - Use bootstrap navigation for the navigation menu.
>   - Use bootstrap forms for the forms.
>   - Use bootstrap cards for the cards.
>   - Use bootstrap modals for the modals.
>
> Don't proceed with the next activity until all of these steps are completed.
>```

### :keyboard: Optional Activity: Let's make the tutoring-sa  app look nice, pretty, and add some color

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Based on the example tutoring-sa app in the docs/tutor-sa.md file and use tutoring-sa as the name for schools app. Let's style this like App.css and make it look nice.
> 
> -  Edit the App.css file to do the following:
>   - Add some color to the background.
>   - Add some color to the text.
>   - Add some color to the tables.
>   - Add some color to the buttons.
>   - Add some color to the headings.
>   - Add some color to the links.
>   - Add some color to the navigation menu.
> - Add the tutoring-sa-small logo justified to the left to the app and make it look nice.
> - Add a favicon to the app and make it look nice.
>
>Don't proceed with the next activity until all of these steps are completed.
>```

### :keyboard: Optional Activity: Iterate on the appearance and try different models

> 🧪 **Try this:**
- Try creating your own prompts to change the application appearance, add features, and try different models.
- Once you are happy with the application you can commit the changes and push them to your branch `build-tutoring-sa-app`.

1. Now that we have created the REACT frontend for all application components let's check our changes in to our `build-tutoring-sa-app` branch.

1. With our new changes complete, please **commit** and **push** the changes to GitHub.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson so we can keep working!

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your commit changes were made for the following files to the branch `build-tutoring-sa-app` and pushed/synchronized to GitHub:
  - `tutoring-sa/frontend/src/components/Dashboard interfaces.js` and it contains `-8000.app.github.dev/api/Dashboard interfaces/`
  - `tutoring-sa/frontend/src/components/CAPS curriculum structure.js` and it contains `-8000.app.github.dev/api/CAPS curriculum structure/`
  - `tutoring-sa/frontend/src/components/assesments.js` and it contains `-8000.app.github.dev/api/assesments/`
  - `tutoring-sa/frontend/src/components/Users.js` and it contains `-8000.app.github.dev/api/users/`
  - `tutoring-sa/frontend/src/components/assessment reports.js` and it contains `-8000.app.github.dev/api/assessment reports/`
- If Mona found a mistake, simply make a correction and push your changes again. Mona will check your work as many times as needed.

</details>
