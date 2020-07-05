# Use Case Model

**Author**:

|Name	|Gatech ID|Gatech email|
|---	|---	|---	|
|Hyun Yong Jin|hjin85|hjin85@gatech.edu|
|Stephen Sanchez|ssanchez42|ssanchez42@gatech.edu|
|Vineeth Karayil Sekharan|vsekharan3|vsekharan3@gatech.edu|
|Benjamin Hurtado Meza|bhm6|benja.hur@gatech.edu|

<br/>

## 1. Use Case Diagram

![](./figs/UseCaseModel.png?raw=true "Use Case Diagram")

## 2. Use Case Descriptions

### 2.1. Overview.
- Requirements: This is single-user app. Only one player (the User) is required.
- Pre-conditions, post-conditions and Scenarios: See below for details.

### 2.1 Use Case: Entering Current Job.
- Requirements: The user should fill up all necessary information including job title, name of company, location (city and state), yearly salary, cost of living (expressed as an index), yearly bonus, sining bonus, retirement benefits and leave time for storing current job information. No missing values are allowed.
- Pre-conditions: No pre-conditions. The user is able to freshly store current job or update the job information.  
- Post-conditions: The entered job is stored in SQLite database in the app and is able to be accessed by user in "Compare" page. The current job is clearly indicated in the page and distinguishable from other offered jobs.
- Scenarios: In the normal scenario, the user has current job and is able to access to each field to enter all necessary job details by typing or to select options from a drop down menu. In an alternative scenario, the user may not have current job and it is allowed to skip storing current job. In an exceptional scenario, user may have only partial information for the job. In this case, user is still needed to provide all information as far as he or she can as no missing values are allowed. When some information is missing, the app will generate a warning message to ask user to fill up all necessary  information.   

### 2.2 Use Case: Entering Offers.
- Requirements, pre-conditions and post-conditions: The same requirement, pre-conditions and post-conditions are applied as use case of "Entering Current Job".
- Scenarios: In the normal scenario, the user is able to enter multiple jobs. In an alternative scenario, the user may skip to store any offered jobs. However, user will need to store the minimum of two jobs to use "Compare" function of the application.

### 2.3 Use Case: Compare Job Offers.
- Requirements: It is required to have minimum of two jobs stored in the database to compare.
- Pre-conditions: Valid jobs should be stored in the app.
- Post-conditions: The selected two jobs are compared side-by-side and the app will display which job is the best based on the internal ranking algorithm.
- Scenarios: In the normal scenario, the user is able to select two jobs (either between a current job and an offered job or between offered jobs) and rank the offers. In the alternative scenario, The user may compare multiple jobs by selecting two jobs for multiple times or investigate ordered list (rank) of jobs displayed in "Compare page".

### 2.4 Use Case: Update Settings.
- Requirements: All the five parameters for calculating job rank (yearly salary, yearly bonus, signing bonus, leave time and retirement benefits) should be entered. Only zero or positive integers are allowed to enter. No negative or decimal values are allowed.
- Pre-conditions: All settings have the same weight by default (1).
- Post-conditions: Based on the weights set in "Settings", the ranking algorithm calculates scores for stored jobs and display the jobs ranking from best to worst in the "Compare" page. When update the weights, it will apply to all the job stored in the database and re-calculate the rank based on the updated settings.
- Scenarios: In the normal scenario, user may leave the settings as it is and the app will use the default settings for calculating rank for the stored jobs. In an alternative scenario, user may update the weights of a particular setting(e.g., yearly salary). This will affects the score of each job and the ranking algorithm re-calculate the scores of each job.
