# WeasyPrint PDF Converter Server

A simple Flask server that converts XHTML to PDF using WeasyPrint.

## Quick Start (Development)

1. Install Git:

```bash
sudo yum install -y git
```

2. Clone and enter repository:

```bash
git clone REPOURL
cd REPO
```

3. Install Python and pip:

```bash
sudo yum install -y python
sudo yum install -y pip
```

4. Install system dependencies:

```bash
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
```

5. Install Python dependencies:

```bash
pip install -r requirements.txt
```

6. Run the server:

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

With more workers:

```bash
gunicorn --bind 0.0.0.0:5000 --workers 3 app:app
```

The server will start on IP:5000

7. Open port:

Add port 5000 to the Amazon EC2 instance security group TCP inbound traffic.

**OBS: Dette er uden reverse proxy og HTTPS**
