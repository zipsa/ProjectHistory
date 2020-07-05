# Test Plan

**Author**:

## TEAM 62<br/>

|Name	|Gatech ID|Gatech email|
|---	|---	|---	|
|Hyun Yong Jin|hjin85|hjin85@gatech.edu|
|Stephen Sanchez|ssanchez42|ssanchez42@gatech.edu|
|Vineeth Karayil Sekharan|vsekharan3|vsekharan3@gatech.edu|
|Benjamin Hurtado Meza|bhm6|benja.hur@gatech.edu|

<br/>

## 1 Testing Strategy

### 1.1 Overall strategy

Our testing strategy will consist of unit-, integration-, and regression-testing strategies, explained below.

#### 1.1.1 Unit Tests

We will start from a TDD approach in which will define all the unit tests for our plain objects used through the application and defined in the UML class diagram. Particularly, we will focus on testing the individually testable actions of the application, such as all comparison settings equal, rank job logic, job score logic, etc., but we will also test validating data that the user inputs into the system. We plan to use JUnit for this section. Below is a table with all our unit tests.

#### 1.1.2 Integration Tests

Once the development is finalized (our unit tests are TDD, our integration is to fully tests the functionality of the developed app) we will add tests for validating both the flow of the application and the persistence level. We plan to use Espresso for integration tests or possibly Selenium.

#### 1.1.3 Regression Testing

Whenever we add new functionality to the application or do simple refactoring of the different feature/modules, we'll make sure to execute the unit and integration tests accordingly. Unit tests are faster to execute to confirm that the features we are adding are "working as expected". Integration tests will depend on the level of completeness of the flow of the app (described in the integration tests section).

### 1.2 Test Selection

For the most part, our unit- and integration- tests are white-box. We will generate the steps of each individual test to perform and to validate everything is working as expected. If down the road we find techniques as validating UI through screenshots or something similar (automated UI checks), we could potentially
incorporate some black-box techniques.

### 1.3 Adequacy Criterion

Our integration tests will focus on the functional aspect of our coverage. They will, at the very least, validate that all minimum requirements of the user are covered (the ones provided in the use case diagram). 

Our unit tests will cover the algorithms behind the code, and everything related to the business objects of our application. We should have an acceptable level of coverage.

### 1.4 Bug Tracking

We are not planning to use any bug tracking system at this moment (e.g., Atlassian). However, we are planning to do PRs and Code reviews on the repository in Github. Doing so gives us the flexibility to discuss about potential issues on the PRs/Code reviews, execute unit tests and integration tests while the code is in PR and additionally marking the PR with some useful tags such as bug if we found it to cause an issue.

### 1.5 Technology

As described above we will use JUnit for our unit tests and we will use Espresso for our Integration tests (possibly Selenium). If we find a better tool down the road, we will update accordingly.

## 2 Test Cases

### 2.1 Unit Tests

| Test Case No  |      Purpose      |  Steps |  Expected Result |  Actual Result |  Status |
|---------------|-----------------|-------|------------------|--------------|--------|
| 1             | Check that all properties of the Job object are correct | Generate a Job object and populate all props through the constructor | Compare all props are correct | All props were correct and all asserts succeeded | COMPLETED/SUCCESS |
| 2             | Check that all properties of the Comparison Settings (default settings) are correct | Generate a Comparisons Settings object through the default constructor | Compare all props are correctly defaulted to 1 | All props were correct (value of 1) and all asserts succeded | COMPLETED/SUCCESS |
| 3             | Check that all properties of the Comparison Settings (custom settings) are correct | Generate a Comparison Settings object and populate all props through the constructor | Compare all props are correct | All props were correct and asserts succeded | COMPLETED/SUCCESS |
| 4             | Check that the sum of all Comparison Settings is correct | Generate a Comparison Settings object, populate all props through constructor and get sum | The total should equal the sum of all Comparison Setting values | Sum was correct | COMPLETED/SUCCESS |
| 5             | Check if all Comparison Settings are equal | Generate a Comparison Settings object, populate all props (with equal value) through constructor and run equals check | All checks should be equal | All settings were equal and asserts succeded | COMPLETED/SUCCESS |
| 6             | Check if Comparison Settings are not equal | Generate a Comparison Settings object, populate all props (with different values) through constructor and run equals check | Equals check should return false | Equals check returned false | COMPLETED/SUCCESS |
| 7             | Validates that the list of US states is correct, all values | Pull the complete list of states from the enum | Count of all states should be correct | Count was correct | COMPLETED/SUCCESS |
| 8             | Validates that correct state enum is returned from text | Call the StateEnum getValue from string, passing a state string (E.g., "California") | Correct State enum should be returned (E.g., CALIFORNIA) | Correct State enum was returned | COMPLETED/SUCCESS |
| 9             | Validates that incorrect state enum is returned (null) from invalid text | Call the StateEnum getValue from string, passing an invalid state string (E.g., "Invalid State") | Null should be returned | null was returned | COMPLETED/SUCCESS |
| 10             | Check tht all properties of the JobScore object are correct | Generate a JobScore object and popualte all props through the constructor (passing also a generated Job) | Compare all props are correct | All props were correct and asserts succeeded | COMPLETED/SUCCESS |
| 11             | Check Job sort/rank with equals Comparison Settings | Pass two jobs to the JobComparator one with double the yearly salary, Comparison Settings should be the same | Job with double yearly salary should be ranked at the top | Job with double the yearly salary was ranked at the top | COMPLETED/SUCCESS |
| 12             | Check Job sort/rank with equal Comparison Settings and equal Jobs | Pass two jobs to the JobComparator, both jobs and settings exactly the same | The score of both jobs should be the same | Score of both jobs was exactly the same | COMPLETED/SUCCESS |
| 13             | Check Job sort/rank with not equal Comparison Settings (Retirement Benefits more important) | Pass two jobs to the JobComparator, one job has slightly better retirement benefits, comparison settings are preferring retirement benefits | Job with better retirement benefits should be at the top | Job with better retirement benefits was at the top | COMPLETED/SUCCESS |
| 14             | Utils class - Valid Number test | Pass a valid number to utils class valid number method | Success, is a valid number | Was successfull | COMPLETED/SUCCESS |
| 15             | Utils class - Invalid Number test | Pass an invalid number to utils class valid number method | Fail, is an invalid number | Succeeded on failing | COMPLETED/SUCCESS |
| 16             | Utils class - Valid Double test | Pass a valid double to utils class valid double method | Success, is a valid double | Was successfull | COMPLETED/SUCCESS |
| 17             | Utils class - Invalid Double test | | Pass an invalid double to utils class valid double method | Fail, is an invalid double | Succeeded on failing | COMPLETED/SUCCESS |
| 18             | Utils class - Valid required field test | Pass any value to a utils class is required field method | Success, contains a value | Was successful | COMPLETED/SUCCESS |
| 19             | Utils class - Invalid required field test | Pass null to a utils class is required field method | Fail, does not contain a value | Succeded on failing | COMPLETED/SUCCESS |
| 20             | Utils class - Invalid required field test (spaces) | Pass a string with white spaces to a utils class is required field method | Fail, does not contain a value after trimming | Succeded on failing | COMPLETED/SUCCESS |

### 2.2 Integration Tests (IN PROGRESS, FINAL WEEK OF FLOW TESTING)

| Purpose | Steps | Expected Result | Actual Result | Status |

| Test Case No  |      Purpose      |  Steps |  Expected Result |  Actual Result |  Status |
|---------------|-----------------|-------|------------------|--------------|--------|
| 1             | Check main menu you can go to Current job | From main menu, click on "Job" | Get to the Current Job view, if you already have a current job stored see the information (persistent) | We are able to get to the current job from main menu, information persists | COMPLETED/SUCCESS |
| 2             | Check main menu you can go to Add Job Offer | From main menu, click on "Offers" | Get to the Offer Job view | We are able to get to the offer view from main menu | COMPLETED/SUCCESS |
| 3             | Check main menu you can go to Adjust Comparison Settings | From main menu, click on "Settings" | Get to the Settings view, if you already have settings stored see the information (persistent). Otherwise they should be default 1 | We are able to get to the current job from main menu, information persists | COMPLETED/SUCCESS |
| 4             | Check main menu you can go to Compare all Job Offers (to select two) | From main menu, click on "Compare" | Get to the Compare view, if you already have job offers or current job created you should see all the information (with a clear indicator of the current job) | We are able to get to the current job from main menu, we see all jobs of the system | COMPLETED/SUCCESS |
| 5             | From "Job" view save current job | From job view, click on save icon when ready to save | Current job saved, see message, return to main menu | We save the current job data, we display a message, we return to main menu | COMPLETED/SUCCESS |
| 6             | From "Job" view return to main menu | From job view, click on return icon | Return to main menu, do not perform save | We return to main menu, we don't perform any saving | COMPLETED/SUCCESS |
| 7             | From "Job" view trigger required field errors | From job view, click on the save button without adding data | Required field errors should appear | We correctly displayed required field errors | COMPLETED/SUCCESS |
| 8             | From "Offer" view save offer | From offer view, click on the save icon when ready to save | Offer saved, see message, return to main menu | We save the offer data, we display a message, we return to main menu | COMPLETED/SUCCESS |
| 9             | From "Offer" view return to main menu | From offer view, click on return icon | Return to main menu, do not perform save | We return to main menu, we don't perform any saving | COMPLETED/SUCCESS |
| 10             | From "Offer" view compare with current job | From offer view, click on the save & compare icon when ready to save | Save, see the save message, go to comparison page with new offer and current job offer | We save, we see the message, we redirect to two job copmarison view with right jobs | COMPLETED/SUCCESS |
| 11            | From "Settings" view save settings | From settings view, click on the save icon when ready to save | Save settings, see message, return to main menu | We save the settings, see a message, return to main menu | COMPLETED/SUCCESS |
| 12            | From "Settings" view return to main menu| From settings view, click on return icon | Return to main menu, do not perform save | We return to main menu, no saving | COMPLETED/SUCCESS |
| 13            | From "Settings" view confirm default settings | From settings view, make sure all settings are 1s by default | Make sure all settings are 1s by default | All settings are 1s | COMPLETED/SUCCESS |
| 14            | From "Settings" view trigger required field errors| From settings view, click on the save button without adding data | Required field errors should appear | We correctly displayed required field errors | COMPLETED/SUCCESS |
| 15            | From "Select for Comparison" view return to main menu | From select for comparison view, click on the return icon | Return to main menu | We return to main menu | COMPLETED/SUCCESS |
| 16            | From "Select for Comparison" view compare two jobs | From select for comparison view, select two jobs and click compare | Go to comparison view | We go to the comparison view | COMPLETED/SUCCESS  |
| 17            | From "Comparison" view return to main menu | From comparison view, click on the return icon | Return to main menu | We return to main menu | COMPLETED/SUCCESS  |
| 18            | From "Comparison" return to select for comparison | From comparison view, click on compare others | Go to select for comparison view | We go to the select for comparison view | COMPLETED/SUCCESS  |
| 19            | From "Select for Comparison" trigger error when not selecting two jobs | From select for comparison view, try to compare without two jobs selected | Stay on the select for comparison view | We stayed on the select for comparison view | COMPLETED/SUCCESS|

### 2.3 Regression Tests

Execute all tests under sections 2.1 and 2.2 and perform manual UI testing.