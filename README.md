# Zadanie 1️⃣

## Podzadanie 1️⃣: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?

Jestem w trakcie studiów podyplomowych na kierunku "Programista Python Developer" w WSB. Na jednym ze zjazdów miałam zajęcia z Selenium i Robot Framework, które tak mi się spodobały że podstanowiłam poszerzyć swoją wiedzę na ten temat biorąc udział w wyzwaniu Dare IT.

## Zadanie dla chętnych: test "PURPUROWY" ze strony GET ISTQB

Wynik: "UDZIELONO ODPOWIEDZI DOBRZE NA 9 Z 14"

# Zadanie 2️⃣: selektory

Wymień wszystkie elementy znajdujące się na stronie, a następnie pod każdym z nich wymień 3 działające selektory.

Scouts Panel</br>
//*[@id="__next"]/form/div/div[1]/h5</br>
//*[text()="Scouts Panel"]</br>
//*[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"]</br>

Login</br>
//*[@id="login"]</br>
//*[text()="Login"]</br>
//*[@name="login"]</br>

Password</br>
//*[@id="password"]</br>
//*[@name="password"]</br>
//*[contains(@type,"password")]</br>

Remind password</br>
//*[@id="__next"]/form/div/div[1]/a</br>
//*[text()="Remind Password"]</br>
//child::div/a</br>

Polski</br>
//*[@id="menu-"]/div[3]/ul/li[1]</br>
//*[text()="Polski"]</br>
//*[contains(@data-value, "pl")]</br>

English</br>
//*[@id="menu-"]/div[3]/ul/li[2]</br>
//*[text()="English"]</br>
//*[contains(@data-value, "en")]</br>

Sign In</br>
//*[@id="__next"]/form/div/div[2]/button/span[1]</br>
//*[contains(@type,"submit")]</br>
//*[text()="Sign in"]</br>








