# Simple script for finding times for National ID/Passport in Stockholm

## Dependencies
The script requires BeautifullSoup to parse the server responses. With Python and pip install BeautifullSoup can be installed via pip as follows. 

pip install beautifulsoup4

## Use:
* Authenticate to https://bokapass.nemoq.se/Booking/Booking/Index/stockholm in your browser.
* When you reach the page allowing you to search for times copy the value of session cookie ASP.NET_VentusBooking_SessionId from the developer tools.
* If the value of the cookie ASP.NET_VentusBooking_SessionIdRun is foobar123 and you would like to find time in the week including 2022-12-24 you run the script as follows:

python pass.py foobar123 2022-12-24

Currently the script is hardcoded to search for times in Stockholm city (Bergsgatan). In order to search for another location modify the value of SectionId parameter of the variable data on line 12. According to the following:

*"38"-Flemingsberg
*"40"-Globen
*"46"-Haninge
*"113"-Järva (Rinkeby)
*"45"-Nacka
*"44"-Norrtälje
*"43"-Sollentuna
*"42"-Solna
*"41"-Sthlm City
*"47"-Södertälje
*"48"-Södra Roslagen (Täby)