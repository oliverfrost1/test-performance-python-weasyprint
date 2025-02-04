# WeasyPrint PDF Converter Server

A simple Flask server that converts XHTML to PDF using WeasyPrint.

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python app.py
```

The server will start on http://localhost:5000

## Usage

To convert an XHTML file to PDF, send a POST request to:

```
http://localhost:5000/convert-to-pdf
```

The request should be a multipart form-data with a file field named 'file' containing your XHTML document.

### Postman Instructions

1. Open Postman
2. Create a new POST request to `http://localhost:5000/convert-to-pdf`
3. In the request builder:
   - Select the "Body" tab
   - Select "form-data"
   - Add a key named "file"
   - Click the dropdown on the right of the key field and select "File"
   - Click "Select Files" and choose your XHTML file
4. Click "Send" to make the request
5. The response will be your converted PDF file
