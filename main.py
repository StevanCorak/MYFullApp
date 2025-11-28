
from myapp import create_app
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    app = create_app()
    
  
    app.run(host='0.0.0.0', port=5100, debug=True)