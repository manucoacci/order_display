ISTRUZIONI:

1. Installare Flask sul Raspberry:
   pip3 install flask

2. Avviare il server:
   python3 app.py

3. Collegarsi:
   - Pagina visualizzazione (TV): http://IP_DEL_RASPBERRY:5000
   - Pagina admin: http://IP_DEL_RASPBERRY:5000/admin

mappatura delle chiamate:
- GET /check_orders
   ritorna un array di stringhe in json, sono tutti gli ordini disponibili
- GET /
   ritorna la pagina display.html (pagina TV)
- GET /admin
   se autenticato ritorna la pagina admin.html per la gestione degli ordini (tablet dietro il banco)
- POST /admin
   rimuove/aggiunge ordini se autorizzato, accetta in entrata i parametri:
   order_name, add?, remove?
   a seconda che siano presenti il parametro add o il parametro remove, lui agisce di conseguenza
      add --> aggiunge order_name alla lista degli ordini
      remove --> rimuove, se presente, order_name dalla lista degli ordini
- GET, POST /login
   pagina di login