from flask import Blueprint, render_template, request, redirect, url_for, flash
from myapp.core import services
from myapp.data.models import FuelType # Uvoz za tipove goriva

# Stvaranje Blueprinta za UI
ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Glavna ruta. Prikazuje sve zapise i omogućuje dodavanje novog zapisa.
    """
    message = None

    if request.method == 'POST':
        # Dohvaćanje podataka iz forme
        location = request.form.get('location')
        fuel_type = request.form.get('fuel_type')
        quantity_str = request.form.get('quantity_liters')

        try:
            quantity = float(quantity_str)
            # Validacija vrste goriva (iako je pokrivena u HTML-u)
            if fuel_type not in FuelType.__args__:
                 raise ValueError("Nevažeća vrsta goriva.")

            # Poziv poslovne logike za spremanje
            services.record_distribution(location, fuel_type, quantity)
            message = {"type": "success", "text": "Novi zapis uspješno dodan!"}
        
        except ValueError as e:
            message = {"type": "error", "text": f"Greška kod unosa: {e}"}
        except Exception as e:
            message = {"type": "error", "text": f"Došlo je do neočekivane greške: {e}"}
            
    # Dohvaćanje svih zapisa i statistike za prikaz
    records = services.get_distribution_data()
    summary = services.get_summary_statistics()
    
    # Sortiranje zapisa po vremenu obrnutim redoslijedom
    records.sort(key=lambda x: x.timestamp, reverse=True)

    return render_template(
        'index.html', 
        records=records, 
        summary=summary,
        fuel_types=FuelType.__args__,
        message=message
    )

@ui_bp.route('/delete/<string:record_id>', methods=['POST'])
def delete_record_route(record_id):
    """
    Ruta za brisanje zapisa (poziva se iz forme).
    """
    if services.remove_distribution_record(record_id):
        # Koristimo flash poruku koja će biti prikazana nakon preusmjeravanja
        flash("Zapis uspješno obrisan!", 'success')
    else:
        flash("Greška: Zapis nije pronađen!", 'error')
        
    # Preusmjeravanje natrag na glavnu stranicu
    return redirect(url_for('ui.index'))