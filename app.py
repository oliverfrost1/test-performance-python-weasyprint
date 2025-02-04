from flask import Flask, send_file, request
from weasyprint import HTML
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    print("Received request")
    if 'file' not in request.files:
        return {'error': 'No file provided'}, 400
        
    file = request.files['file']
    if file.filename == '':
        return {'error': 'No file selected'}, 400
        
    # Create temporary files for both input and output
    with tempfile.NamedTemporaryFile(suffix='.xhtml', delete=False) as xhtml_temp:
        # Save uploaded file
        file.save(xhtml_temp.name)
        
        # Create temporary PDF file path
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as pdf_temp:
            # Convert XHTML to PDF
            HTML(filename=xhtml_temp.name).write_pdf(pdf_temp.name)
            
            # Send the PDF file
            response = send_file(
                pdf_temp.name,
                mimetype='application/pdf',
                as_attachment=True,
                download_name='converted.pdf'
            )
            
            # Clean up temporary files after sending
            @response.call_on_close
            def cleanup():
                os.unlink(xhtml_temp.name)
                os.unlink(pdf_temp.name)
                
            return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 