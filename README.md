# Party Planner - Guest Table Arranger

A web application that helps you organize your guest list into tables for networking events. The app accepts CSV file uploads with guest information and creates visual circular table arrangements showing where each person will be seated.

## Features

- 📁 Easy CSV file upload with drag & drop support
- 📋 Parse guest information from name and message columns
- ✅ Interactive guest selection with checkboxes
- 🎯 Smart table arrangement algorithm
- 🎨 Visual circular table layouts with seating positions
- 📱 Responsive design for mobile and desktop
- 🎨 Modern, intuitive UI

## Prerequisites

- Python 3.7 or higher
- Web browser

## Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd LinkedInParty
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**
   ```bash
   python3 app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Prepare your CSV file**
   Your CSV should have exactly 2 columns:
   - **First column**: guest names
   - **Second column**: descriptions, roles, or messages

4. **Upload your guest list**
   - Click "Upload Guest List" or drag and drop your CSV file
   - The app will parse and display up to 100 guests

5. **Select guests for your event**
   - Click on guest cards to select/deselect them
   - You can select up to 30 guests (3 tables × 10 people)
   - The stats panel shows your selection progress

6. **Arrange tables**
   - Click "Arrange Tables" to automatically organize your selected guests
   - The app will create three visual circular tables
   - Each table shows seating positions with guest initials
   - Hover over seats to see full names and descriptions

## CSV Format Example

```csv
name,message
John Smith,Software Engineer at TechCorp
Sarah Johnson,Marketing Director at Creative Agency
Michael Brown,CEO of StartupXYZ
Emily Davis,Data Scientist at AI Labs
David Wilson,Product Manager at Innovation Inc
```

## Visual Table Layout

The app creates beautiful circular table visualizations:
- 🟢 **Green circles** represent individual seats
- 🔵 **Blue center** shows the table number
- 👤 **Initials** displayed on each seat
- 💬 **Hover tooltips** show full names and descriptions
- 🎯 **Smart positioning** arranges seats evenly around the table

## How it Works

### CSV Processing
- Supports multiple CSV delimiters (comma, semicolon, tab)
- Automatically detects column headers
- Reads first column for names and second column for descriptions
- Handles various encoding formats

### Table Arrangement Algorithm
The app uses a smart distribution algorithm:
1. Categorizes guests by industry/role type based on message content
2. Distributes major categories evenly across 3 tables
3. Ensures each table has a maximum of 10 people
4. Balances the number of people per table

### Smart Categorization
Based on message content, guests are categorized as:
- **Tech**: engineer, developer, programmer, software, tech, it, data, ai, ml, technology, scientist
- **Business**: manager, director, ceo, founder, executive, business, strategy, operations, consultant, product
- **Creative**: designer, creative, marketing, content, writer, artist, media, communications, strategist
- **Sales**: sales, account, client, business development, partnership, account manager
- **Finance**: finance, accounting, investment, banking, financial, analyst, cfo
- **Other**: any roles not matching the above categories

### Visual Seating Layout
- **Circular tables** with realistic seating arrangements
- **Even distribution** of seats around each table
- **Interactive elements** with hover effects
- **Responsive design** that works on all devices

## Troubleshooting

### Common Issues

1. **CSV Format Problems**
   - Ensure your CSV has exactly 2 columns (name and message)
   - Check that the first column contains guest names
   - Verify the second column contains role descriptions

2. **File Upload Issues**
   - Make sure you're uploading a .csv file
   - Check that the file isn't corrupted or empty
   - Try a smaller file first to test the format

3. **Parsing Errors**
   - The app will try different delimiters automatically
   - If parsing fails, check your CSV format in a text editor
   - Ensure there are no special characters causing issues

### Performance Tips

- The app can handle up to 100 guests efficiently
- Larger files may take a moment to process
- Keep your CSV file under 1MB for best performance

## Technical Details

### Backend (Flask)
- `app.py`: Main Flask application with CSV processing
- Uses Python's built-in CSV module for parsing
- RESTful API endpoints for frontend communication

### Frontend (HTML/CSS/JavaScript)
- Modern responsive design
- Drag & drop file upload
- Interactive guest selection
- Circular table visualization with CSS positioning
- Real-time statistics updates

### Dependencies
- `flask`: Web framework
- `flask-cors`: Cross-origin resource sharing
- `werkzeug`: File upload handling

## Limitations

- Maximum 30 guests can be arranged (3 tables × 10 people)
- Maximum 100 guests can be loaded from CSV
- CSV files only (no Excel or other formats)
- Guest data is not persistent between sessions

## Future Enhancements

- [ ] Support for Excel files (.xlsx, .xls)
- [ ] Save/load table arrangements
- [ ] Export to CSV/PDF
- [ ] Custom table sizes
- [ ] Guest filtering by industry/company
- [ ] Integration with calendar systems
- [ ] Email invitations to guests
- [ ] 3D table visualization
- [ ] Drag & drop seating arrangements

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is for educational and personal use purposes. 