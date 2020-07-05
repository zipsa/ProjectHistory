
# UserManual

**version1.2**

**Author**:


## TEAM 62<br/>

|Name	|Gatech ID|Gatech email|
|---	|---	|---	|
|Hyun Yong Jin|hjin85|hjin85@gatech.edu|
|Stephen Sanchez|ssanchez42|ssanchez42@gatech.edu|
|Vineeth Karayil Sekharan|vsekharan3|vsekharan3@gatech.edu|
|Benjamin Hurtado Meza|bhm6|benja.hur@gatech.edu|

<br/>

## Overview
This is a single-user job offer comparison app that ranks user's current job and offered jobs based on parameters such as yearly salary, singing bonus, yearly bonus, retirement benefits, leave time and cost of living. User may also customize ranking algorithm by setting up weights of yearly salary, signing bonus, yearly bonus, retirement benefits and leave time. The app displays and compares the jobs ranked from best to worst, and user is able to pick up two jobs to compare side-by-side.

## 1 Main Menu

<img src="./figs/manual/MainMenu.png" alt="Main Menu" width="150" height="315"/>

Main page displayed when the app is started. From this main menu, you may access to four options: Job, Offers, Compare, Settings.

---

## 2 Job


<img src="./figs/manual/Job1.png" alt="Entering Job" width="150" height="315"/>

Click on Job icon from Main Menu to enter Job.

---
<img src="./figs/manual/Job2.png" alt="Job Menu" width="150" height="315"/>

Job page.  

---
<p float="left">
  <img src="./figs/manual/Job3a.png" alt="Enter Job Information" width="150" height="315"/>
  <img src="./figs/manual/Job3b.png" alt="Enter Job Information" width="150" height="315"/>
  <img src="./figs/manual/Job3c.png" alt="Enter Job Information" width="150" height="315"/>
</p>


Please enter current job information:
>- Title
>- Company
>- City and State
>- Yearly Salary
>- CLI (Cost of living index)
>- Yearly Bonus
>- Signing Bonus
>- Retirement Benefits (as percentage matched)
>- Leave Time (as number of days)

Select the state from drop down menu.
No missing values are allowed. When there are missing values, there will be a pop-up message showing what is missing and what format is required to put.

---

<img src="./figs/manual/Job4.png" alt="Store Job" width="150" height="315"/>

Press 'Save' icon to store current job and return to Main Menu.

---
<img src="./figs/manual/Job5.png" alt="Go Back To Main Menu" width="150" height="315"/>

Press 'Go Back' icon to return to main menu without saving it.

---

<img src="./figs/manual/Job6.png" alt="Saved job" width="150" height="315"/>

In a scenario when you restart the app and enter into Job, the saved current job information persists and displayed in Job page.


---

## 3 Offers

<img src="./figs/manual/Offers1.png" alt="Entering Offers" width="150" height="315"/>

Click on Offers icon from Main Menu to enter new job offers.

---
<p float="left">
  <img src="./figs/manual/Offers2a.png" alt="Offers Menu" width="150" height="315"/>
  <img src="./figs/manual/Offers2b.png" alt="Offers Menu with info" width="150" height="315"/>
  <img src="./figs/manual/Offers2c.png" alt="Offers Menu with info" width="150" height="315"/>
</p>

Offers page.
Please enter new job offers as same format as current job described above.
No missing values are allowed. When there are missing values, there will be a pop-up message showing what is missing and what format is required to put.

---
<img src="./figs/manual/Offers3.png" alt="Save an offer" width="150" height="315"/>

Press 'Save' icon to save current offer and return to main page. You may repeat this to save multiple offers.

---
<p float="left">
  <img src="./figs/manual/Offers4a.png" alt="Save and compare offers" width="150" height="315"/>
  <img src="./figs/manual/Offers4b.png" alt="Save and compare offers" width="150" height="315"/>
</p>

Press 'Save and Compare' icon to save current offer and directly jump to compare page. This will directly bring you to the compare page, where the current job and entered offer is displayed side-by-side.

---
<img src="./figs/manual/Offers5.png" alt="Go Back To Main Menu" width="150" height="315"/>

Press 'Go Back' icon to return to main menu without saving current offer.

---

## 4 Compare

<img src="./figs/manual/Compare1.png" alt="Entering Compare" width="150" height="315"/>

Click on Compare icon from Main Menu to see the list of stored jobs.

---
<img src="./figs/manual/Compare2.png" alt="Display Jobs" width="150" height="315"/>

This page displays all jobs stored in app. Current job is clearly highlighted with a 'person icon' and displayed on the top. Other jobs were sorted based on rank from the best to worst.

---
<img src="./figs/manual/Compare3.png" alt="Select Jobs" width="150" height="315"/>

You can select two jobs to compare by clicking on them. The selected jobs were highlighted with green. You may unselect jobs by clicking on the selected jobs. The app allows to select maximum two jobs, not any more.

---
<p float="left">
  <img src="./figs/manual/Compare4a.png" alt="Compare icon" width="150" height="315"/>
  <img src="./figs/manual/Compare4b.png" alt="Compare two job page" width="150" height="315"/>
  <img src="./figs/manual/Compare4c.png" alt="Error Toast" width="150" height="315"/>
</p>

After selecting two jobs, click on "Compare Icon" to compare selected jobs side-by-side in the next page. In the page, the best job based on ranking algorithm is indicated. When less than two jobs were selected at the moment when you click on "Compare Icon", the app will generate a pop-up message indicating selecting two jobs is required.


---
<p float="left">
  <img src="./figs/manual/Compare6a.png" alt="Compare icon" width="150" height="315"/>
  <img src="./figs/manual/Compare6b.png" alt="Return to previous" width="150" height="315"/>
</p>

Click on "Compare Icon" to return to previous page where you can select two jobs to compare. Previous selections are not saved when returned.


---

<p float="left">
  <img src="./figs/manual/Compare5.png" alt="Return to main" width="150" height="315"/>
  <img src="./figs/manual/Compare7.png" alt="Return to main" width="150" height="315"/>
</p>

You may directly return to main menu by pressing 'Go Back' icon from any pages from downstream of compare pages.


## 5 Settings

<img src="./figs/manual/Settings1.png" alt="Entering Settings" width="150" height="315"/>

Click on Settings icon from Main Menu to enter compare settings.

---
<img src="./figs/manual/Settings2.png" alt="Settings Page" width="150" height="315"/>

Settings page. Default value(1) for each criteria has been set.

---
<p float="left">
  <img src="./figs/manual/Settings3a.png" alt="Enter comparison settings" width="150" height="315"/>
  <img src="./figs/manual/Settings3b.png" alt="Enter comparison settings" width="150" height="315"/>
</p>


Please enter user-defined comparison settings (optional). The weights defined here is used to calculate the ranking of your jobs. Please put zero or positive integers only. Negative values or decimal points are not allowed and you will not able to enter such a value. Higher number indicates more important criteria.  

>- Yearly Salary
>- Yearly Bonus
>- Signing Bonus
>- Leave Time
>- Retirement Benefits

No missing values are allowed. When there are missing values, there will be a pop-up message showing what is missing and what format is required to put.

---
<img src="./figs/manual/Settings4.png" alt="Store Settings" width="150" height="315"/>

Press check icon to store current settings. This new setting persists unless you update new values.

---
<img src="./figs/manual/Settings5.png" alt="Go Back To Main Menu" width="150" height="315"/>

Press go back icon to return to main menu.

---

This is it! Please enjoy Team62's Job Offer Comparison App!
