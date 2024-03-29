# Automated testing challenge 🤖

## Task 1️⃣

The goal of this task was to:
- execute exploratory testing,
- learn which programs are necessary to start automated testing,
- create a GIT repository,
- clone the repo and set up a working environment,
- format a README file.

### Subtask 1️⃣: Why did you decide to take part in the challenge?

I am pursuing postgraduate studies in Python programming. I had Selenium and Robot Framework classes there and I liked them so much that I decided to take part in the test automation challenge.

[//]: <> (Jestem w trakcie studiów podyplomowych na kierunku "Programista Python Developer" w WSB. Na jednym ze zjazdów miałam zajęcia z Selenium i Robot Framework, które tak mi się spodobały że podstanowiłam poszerzyć swoją wiedzę na ten temat biorąc udział w wyzwaniu Dare IT.)

### Optional task: "PURPUROWY" test from GET ISTQB website

Result: 9/14

## Task 2️⃣

The goal of this task was to:
- learn what selectors are,
- learn where to find selectors,
- learn how to write XPaths, 
- understand how to choose the best selectors.

List all elements located on the website and three selectors relative to each of them.

#### Scouts Panel</br>
- //*[@id="__next"]/form/div/div[1]/h5</br>
- //*[text()="Scouts Panel"]</br>
- //*[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"]</br>

#### Login Input</br>
- //*[@id="login"]</br>
- //*[text()="Login"]</br>
- //*[@name="login"]</br>

#### Password</br>
- //*[@id="password"]</br>
- //*[@name="password"]</br>
- //*[contains(@type,"password")]</br>

#### Remind password</br>
- //*[@id="__next"]/form/div/div[1]/a</br>
- //*[text()="Remind Password"]</br>
- //child::div/a</br>

#### Polski</br>
- //*[@id="menu-"]/div[3]/ul/li[1]</br>
- //*[text()="Polski"]</br>
- //*[contains(@data-value, "pl")]</br>

#### English</br>
- //*[@id="menu-"]/div[3]/ul/li[2]</br>
- //*[text()="English"]</br>
- //*[contains(@data-value, "en")]</br>

#### Sign In</br>
- //*[@id="__next"]/form/div/div[2]/button/span[1]</br>
- //*[contains(@type,"submit")]</br>
- //*[text()="Sign in"]</br>

## Task 3️⃣

The goal of this task was to:
- learn unittest framework,
- click on elements of the website,
- fill in the fields,
- use "assert",
- run the test.

## Task 4️⃣

The goal of this task was to:
- refactor the code,
- learn how to work with debugger,
- write test cases, 
- automate the webpage on the basis of test cases.

Google Drive: [click here](https://drive.google.com/drive/folders/1X0jLapKF8UmqdAVsQ_BPGTm_n6Tubutz?usp=share_link).

## Task 5️⃣

The goal of this task was to:
- learn what Smoke Tests are,
- learn how to configure Suite Test,
- learn a new framework (Robot Framework),
- automatically generate a report.

You can find the solution of this task [here](https://github.com/marta-rakowska/panelscout_robotframework).

## Task 6️⃣

The goal of this task was to:
- learn how to find bugs,
- learn how to report bugs,
- learn how to write a test report.

You can find the solution of this task [here](https://drive.google.com/drive/folders/1DU61ovsgWxocZU52_CEFXh79J4YJABHq).

## Requirements

To run the tests you need to download chromedriver compatible with your version of Chrome.








