# WeasyPrint PDF Converter Server

A simple Flask server that converts XHTML to PDF using WeasyPrint.

## Setup

### 1. Install System Dependencies

For Amazon Linux/RHEL/CentOS, run the following commands to install required system packages:

```bash
# Install the EPEL repository
sudo yum install -y epel-release

# Install system dependencies
sudo yum install -y \
    cairo-devel \
    pango-devel \
    pangomm \
    libffi-devel \
    redhat-rpm-config \
    python3-devel \
    gcc \
    gcc-c++ \
    make \
    pkgconfig \
    zlib-devel \
    libjpeg-turbo-devel \
    libpng-devel

# For Amazon Linux 2, you might also need
sudo amazon-linux-extras install epel -y
```

For Ubuntu/Debian:

```bash
sudo apt-get install -y \
    python3-dev \
    python3-pip \
    python3-cffi \
    build-essential \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info
```

### 2. Install Python Dependencies

After installing the system packages, install the Python requirements:

```bash
pip install -r requirements.txt
```

### 3. Run the Server

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

## Troubleshooting

If you encounter any issues with missing libraries, make sure all system dependencies are properly installed. The error message about `libpango-1.0-0` typically indicates missing system packages. Run the appropriate installation commands for your system as listed above.

For more detailed troubleshooting, refer to the official WeasyPrint documentation:

- [Installation Guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)
- [Troubleshooting Guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#troubleshooting)
