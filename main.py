
from myapp import create_app
import logging

# Postavljanje logiranja na DEBUG razinu kako bi se vidjeli svi izlazi
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    # Stvaranje Flask aplikacije
    app = create_app()
    
    # Pokretanje aplikacije. Host '0.0.0.0' omogućuje pristup izvan lokalnog računala.
    # U debug modu Flask automatski ponovno učitava kod nakon promjene.
    app.run(host='0.0.0.0', port=5000, debug=True)