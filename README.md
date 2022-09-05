# Ali-Instock
This is a short script designed to do two things.

1) regularly check the status of an Aliexpress webpage for an out of stock (OOS) item.
2) notify a user via text message when the item is in stock.

**PLEASE NOTE:**
There are a few limitations to what this script can achieve as it is currently written. 
Namely, this scrtipt will only notify you if every item available for sale on the webpage is in stock.
This behavior expected and is due to the script specifically looking for _any_ instance of a particular 
JavaScript marker which indicates an OOS status. Therefore, if you're looking at a store page with more
than one variant of the item, and multiple variants are out of stock, you won't recieve a notification
until everything is back in stock, even if the particulat variant you desired has been in stock for 
days. Obviously this can be undrsireable, but I can't really be bothered to improve this behavior and
my understanding of JS webpage functionality at this point wouldn't allow me to if I could.

## setup

In order for this script to execute correctly, you should: 

1) Ensure you're running python version > 3.5 and have Google Chrome installed.
2) Install the dependencies in requirements.txt into your venv via pip (_you can find out how to do this_
_with a quick google search_).
3) Create a free twilio account and edit the secrets.py file and  place all of the required 
information into the variables found there. You can find guides to locating your Account SID, 
Twilio number, and Auth Token on Youtube.
4) Edit the Ali-Instock.py file and replace the text message variable and default URL
(currently the Miyoo Mini game system) to reflect the product you're looking to purchase.
5) If it isnt obvious, when you run the script, you must run the script in the background 
(i.e "nohup python3 Al\_instock.py &") or leave it running in the terminal.

That should be everything.

I hope you find this as useful as I did,

-_S_
