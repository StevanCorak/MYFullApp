# ⛽ MYFULLAPP: Sustav za Evidenciju Raspodjele Goriva

## 🌟 Opis Aplikacije

`MYFULLAPP` je jednostavna, samostalna (standalone) web aplikacija izgrađena pomoću **Python Flask** okvira. Glavna svrha aplikacije je omogućiti korisnicima **evidenciju, praćenje i analizu raspodjele goriva** na različitim lokacijama.

Aplikacija koristi datoteke `services.py` za poslovnu logiku i `models.py` za strukturu podataka, dok se svi podaci trajno pohranjuju u lokalnu **JSON datoteku (`fuel_distribution_data.json`)**.

---

## 🚀 Instalacija i Pokretanje

Slijedite ove korake za postavljanje i pokretanje aplikacije.

### 1. Klonirajte repozitorij 

### 2. Instalirajte Pakete
```bash
pip install -r requirements.txt
```

### 3. Pokrenite aplikaciju
```bash
python main.py