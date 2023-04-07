# Zadanie 1️⃣

## Podzadanie 1️⃣: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?

Jestem w trakcie studiów podyplomowych na kierunku "Programista Python Developer" w WSB. Na jednym ze zjazdów miałam zajęcia z Selenium i Robot Framework, które tak mi się spodobały że podstanowiłam poszerzyć swoją wiedzę na ten temat biorąc udział w wyzwaniu Dare IT.

## Zadanie dla chętnych: test "PURPUROWY" ze strony GET ISTQB

Wynik: "UDZIELONO ODPOWIEDZI DOBRZE NA 9 Z 14"

# Zadanie 2️⃣: selektory

Wymień wszystkie elementy znajdujące się na stronie, a następnie pod każdym z nich wymień 3 działające selektory.

Scouts Panel
//*[@id="__next"]/form/div/div[1]/h5
//*[text()="Scouts Panel"]
//*[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"]

Login
//*[@id="login"]
//*[text()="Login"]
//*[@name="login"]

Password
//*[@id="password"]
//*[@name="password"]
//*[contains(@type,"password")]

Remind password
//*[@id="__next"]/form/div/div[1]/a
//*[text()="Remind Password"]
//child::div/a

Polski
//*[@id="menu-"]/div[3]/ul/li[1]
//*[text()="Polski"]
//*[contains(@data-value, "pl")]

English
//*[@id="menu-"]/div[3]/ul/li[2]
//*[text()="English"]
//*[contains(@data-value, "en")]

Sign In
//*[@id="__next"]/form/div/div[2]/button/span[1]
//*[contains(@type,"submit")]
//*[text()="Sign in"]








