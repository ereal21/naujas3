# Telegram shop
This is an example Telegram shop bot.
this is a fairly simple template, but at the same time it is quite effective for selling something directly in the telegram  
## Example:  
### admin pov  
![](assets/admin_pov.gif)
### user pov:
![](assets/user_pov.gif)
## What can it do?
- `/start` - needed to start the bot
### Menu
  the menu for the user looks like this (the administrator has an "admin panel" button in the menu):  

  ![](assets/menu_picture.png)  

  ![](assets/menu_as_admin_picture.png)

### Catalog
  The catalog consists of categories and positions. The user can buy goods from the positions, and the administrator can manage them  
  ![](assets/categories_picture.png)  

  ![](assets/positions_picture.png)  

  ![](assets/position_description_picture.png)

### Admin panel
There are a couple of buttons in the admin panel to control all processes in the bot.

  ![](assets/admin_menu_picture.png)

  ![](assets/shop_menu_picture.png)

  ![](assets/user_menu_picture.png)
### Other
  The bot has configured logging that reports errors or actions of administrators  
## Tech Stack 💻
- #### Languages:
  - Python 3.10

- #### Telegram:
    - Aiogram

- #### Database:
    - SQLite3
    - Sqlalchemy

- #### Payment:
    - Yoomoney
    - NOWPayments (crypto)

- #### Debug:
    - logger

## Installation 💾
[QUICK START](markdown/quick_start.md)

For local testing of NOWPayments webhooks you need to run the IPN server and expose it with **ngrok**:

```bash
python ipn.py
# in another terminal
ngrok http 5000
```

Use the HTTPS URL as `NOWPAYMENTS_IPN_URL` in your environment so NOWPayments can

reach your webhook endpoint. Include the `/nowpayments-ipn` path, e.g.:

```
NOWPAYMENTS_IPN_URL=https://xxxx.ngrok-free.app/nowpayments-ipn
```
=======
reach your webhook endpoint.

Create a `.env` file with all required keys (see `markdown/quick_start.md`) and then run the bot:

```bash
python run.py
```
