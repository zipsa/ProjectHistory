# Design Document

**Author**:

## TEAM 62<br/>

|Name	|Gatech ID|Gatech email|
|---	|---	|---	|
|Hyun Yong Jin|hjin85|hjin85@gatech.edu|
|Stephen Sanchez|ssanchez42|ssanchez42@gatech.edu|
|Vineeth Karayil Sekharan|vsekharan3|vsekharan3@gatech.edu|
|Benjamin Hurtado Meza|bhm6|benja.hur@gatech.edu|

<br/>

## 1 Design Considerations

### 1.1 Assumptions

1. The user can only have one current job at a time. There is no concept of the user having multiple current jobs.
2. The user will be in charge of adding the location of the job, with its relevant information about cost of living. There will not be a source of truth about the cost of living for a particular city-state.
3. The application will only be used in US. The list of states will only contain US states and the user won't be able to specify another country.
4. The logic to compare jobs will be the same (ranking) when comparing two jobs or comparing multiple jobs.
5. The value for all offer numbers is going to be an Integer number.

### 1.2 Constraints

1. The application will only work on the Android operating system. The required minimum API is 28.
2. The data of the application will be stored in the device itself. There will not be a remote database or API connections.
3. The application will be used by only one user. There is no implementation for switching between users, only the person that has the application installed will be adding jobs offers.
4. For all numbers in the offer/current job, we only accept Integers.

### 1.3 System Environment

#### 1.3.1 Hardware

The application will run in Smartphone devices. Specifically, the application will run in Android devices.

#### 1.3.2 Software

The application will run in the Android Operating System. The minimum required API is 28, that the application is going to support. 

## 2 Architectural Design

### 2.1 Component Diagram

![](./figs/ComponentDiagram.png?raw=true "Component Diagram")

### 2.2 Deployment Diagram

![](./figs/DeploymentDiagram.png?raw=true "Deployment Diagram")

## 3 Low-Level Design

### 3.1 Class Diagram

![](./figs/ClassDiagram.png?raw=true "Class Diagram")

## 4 User Interface Design

![](./figs/UiDiagram.png?raw=true "UI Diagram")