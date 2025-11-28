from flask import Blueprint, render_template, request, redirect, url_for, flash
from myapp.core import services
from myapp.data.models import FuelType 


ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/', methods=['GET', 'POST'])
def index():
    
    message = None

    if request.method == 'POST':
        location = request.form.get('location')
        fuel_type = request.form.get('fuel_type')
        quantity_str = request.form.get('quantity_liters')

        try:
            quantity = float(quantity_str)
            if fuel_type not in FuelType.__args__:
                 raise ValueError("Nevažeća vrsta goriva.")

            services.record_distribution(location, fuel_type, quantity)
            message = {"type": "success", "text": "Novi zapis uspješno dodan!"}
        
        except ValueError as e:
            message = {"type": "error", "text": f"Greška kod unosa: {e}"}
        except Exception as e:
            message = {"type": "error", "text": f"Došlo je do neočekivane greške: {e}"}
            
    records = services.get_distribution_data()
    summary = services.get_summary_statistics()
    
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
        flash("Zapis uspješno obrisan!", 'success')
    else:
        flash("Greška: Zapis nije pronađen!", 'error')
        
    # Preusmjeravanje natrag na glavnu stranicu
    return redirect(url_for('ui.index'))