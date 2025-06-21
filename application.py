from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import csv
import io
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Configure upload settings
UPLOAD_FOLDER = '/tmp/uploads'  # Use /tmp for AWS Lambda compatibility
ALLOWED_EXTENSIONS = {'csv'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_csv_file(file_content):
    """Parse CSV content and extract guest information from name and message columns"""
    try:
        # Decode the file content
        if isinstance(file_content, bytes):
            file_content = file_content.decode('utf-8')
        
        # Create a StringIO object to read the CSV
        csv_file = io.StringIO(file_content)
        
        # Read CSV with different possible delimiters
        for delimiter in [',', ';', '\t']:
            try:
                csv_file.seek(0)  # Reset file pointer
                reader = csv.DictReader(csv_file, delimiter=delimiter)
                
                # Get the header row
                headers = reader.fieldnames
                if not headers or len(headers) < 2:
                    continue
                
                # Use the first two columns: name and message
                name_column = headers[0]
                message_column = headers[1]
                
                # Parse the data and filter out entries with blank names or descriptions
                guests = []
                for i, row in enumerate(reader):
                    name = row.get(name_column, '').strip()
                    title = row.get(message_column, '').strip()
                    
                    # Only add if both name and description are not blank
                    if name and title:
                        guests.append({
                            'id': i,
                            'name': name,
                            'title': title
                        })
                
                if guests:
                    return {'success': True, 'guests': guests, 'total': len(guests)}
                    
            except Exception as e:
                continue
        
        return {'success': False, 'error': 'Could not parse CSV file. Please ensure it has at least 2 columns (name and message).'}
        
    except Exception as e:
        return {'success': False, 'error': f'Error parsing CSV: {str(e)}'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    """Handle CSV file upload"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'})
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'})
        
        if not allowed_file(file.filename):
            return jsonify({'success': False, 'error': 'Please upload a CSV file'})
        
        # Read file content
        file_content = file.read()
        
        # Parse CSV
        result = parse_csv_file(file_content)
        
        if result['success']:
            return jsonify({
                'success': True,
                'guests': result['guests'],
                'total': result['total'],
                'message': f'Successfully loaded {result["total"]} guests from CSV (filtered out entries with blank names or descriptions)'
            })
        else:
            return jsonify(result)
            
    except Exception as e:
        return jsonify({'success': False, 'error': f'Upload error: {str(e)}'})

@app.route('/arrange-tables', methods=['POST'])
def arrange_tables():
    data = request.get_json()
    selected_guests = data.get('selected_guests', [])
    
    if not selected_guests:
        return jsonify({'success': False, 'error': 'No guests selected for arrangement'})
    
    # Smart arrangement algorithm - create unlimited tables of 10
    tables = arrange_guests_into_tables(selected_guests)
    
    return jsonify({'success': True, 'tables': tables})

def arrange_guests_into_tables(guests):
    """Arrange guests into tables of 10 people each with smart distribution"""
    if not guests:
        return []
    
    # Categorize guests by industry/role type based on message content
    categories = {
        'tech': ['engineer', 'developer', 'programmer', 'software', 'tech', 'it', 'data', 'ai', 'ml', 'technology', 'scientist'],
        'business': ['manager', 'director', 'ceo', 'founder', 'executive', 'business', 'strategy', 'operations', 'consultant', 'product'],
        'creative': ['designer', 'creative', 'marketing', 'content', 'writer', 'artist', 'media', 'communications', 'strategist'],
        'sales': ['sales', 'account', 'client', 'business development', 'partnership', 'account manager'],
        'finance': ['finance', 'accounting', 'investment', 'banking', 'financial', 'analyst', 'cfo'],
        'other': []
    }
    
    categorized_guests = {cat: [] for cat in categories.keys()}
    
    # Categorize each guest based on their message/description
    for guest in guests:
        title_lower = guest['title'].lower()
        categorized = False
        
        for category, keywords in categories.items():
            if category == 'other':
                continue
            if any(keyword in title_lower for keyword in keywords):
                categorized_guests[category].append(guest)
                categorized = True
                break
        
        if not categorized:
            categorized_guests['other'].append(guest)
    
    # Calculate how many tables we need
    total_guests = len(guests)
    num_tables = (total_guests + 9) // 10  # Ceiling division to get number of tables needed
    
    # Initialize tables
    tables = [[] for _ in range(num_tables)]
    
    # Distribute guests strategically across all tables
    # First, distribute major categories evenly
    major_categories = ['tech', 'business', 'creative', 'sales']
    
    for category in major_categories:
        guests_in_category = categorized_guests[category]
        if guests_in_category:
            # Distribute evenly across all tables
            for i, guest in enumerate(guests_in_category):
                table_index = i % num_tables
                if len(tables[table_index]) < 10:
                    tables[table_index].append(guest)
    
    # Then distribute remaining guests (finance, other)
    remaining_guests = []
    for category in ['finance', 'other']:
        remaining_guests.extend(categorized_guests[category])
    
    # Also add any guests that didn't fit in the first round
    for table in tables:
        for guest in guests:
            if guest not in [g for table_guests in tables for g in table_guests]:
                if len(table) < 10:
                    table.append(guest)
                    break
    
    # Fill remaining slots with any leftover guests
    for guest in guests:
        if guest not in [g for table_guests in tables for g in table_guests]:
            for table in tables:
                if len(table) < 10:
                    table.append(guest)
                    break
    
    return tables

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 