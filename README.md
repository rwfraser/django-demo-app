# Django Demo App 🚀

A simple Django demonstration application showcasing modern web development practices and cloud deployment to Fly.io.

## 🌟 Features

- **Modern Django Framework**: Built with Django 4.2.24
- **Beautiful UI**: Responsive design with gradient backgrounds and clean styling
- **System Information**: Real-time display of server and runtime information
- **Health Check API**: Built-in monitoring endpoints
- **Production Ready**: Environment-based configuration with security settings
- **Cloud Deployment**: Optimized for Fly.io deployment
- **Docker Support**: Containerized application for consistent deployments

## 🛠️ Technology Stack

- **Backend**: Django 4.2.24 (Python Web Framework)
- **Frontend**: HTML5, CSS3 with responsive design
- **Database**: SQLite (development) / PostgreSQL (production)
- **WSGI Server**: Gunicorn for production
- **Static Files**: WhiteNoise for efficient static file serving
- **Deployment**: Docker + Fly.io
- **Version Control**: Git with GitHub integration

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/django-demo-app.git
   cd django-demo-app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**: http://127.0.0.1:8000

### Docker Development

1. **Build and run with Docker**
   ```bash
   docker build -t django-demo-app .
   docker run -p 8000:8000 django-demo-app
   ```

## 🌐 API Endpoints

- `/` - Main application homepage
- `/about/` - Detailed information about the application
- `/api/status/` - JSON health check endpoint (returns application status)
- `/admin/` - Django admin interface

## 📦 Deployment to Fly.io

### Prerequisites

1. Install [Fly.io CLI](https://fly.io/docs/hands-on/install-flyctl/)
2. Sign up for a Fly.io account: `flyctl auth signup`

### Deploy

1. **Initialize Fly app**
   ```bash
   flyctl apps create django-demo-app
   ```

2. **Set secrets**
   ```bash
   flyctl secrets set SECRET_KEY=your-secret-key-here
   flyctl secrets set DEBUG=False
   ```

3. **Deploy application**
   ```bash
   flyctl deploy
   ```

4. **Open deployed app**
   ```bash
   flyctl open
   ```

## 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | Auto-generated |
| `DEBUG` | Enable/disable debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `127.0.0.1,localhost,.fly.dev` |

## 📁 Project Structure

```
django-demo-app/
├── demo/                   # Main Django app
│   ├── templates/         # HTML templates
│   ├── views.py          # View functions
│   ├── urls.py           # URL configuration
│   └── ...
├── demosite/             # Django project settings
│   ├── settings.py       # Main settings file
│   ├── urls.py          # Root URL configuration
│   └── ...
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── fly.toml            # Fly.io deployment configuration
├── manage.py           # Django management script
└── README.md           # This file
```

## 🔍 Health Monitoring

The application includes a health check endpoint at `/api/status/` that returns:

```json
{
  "status": "ok",
  "message": "Django Demo App is running!"
}
```

This endpoint is used by Fly.io for application health monitoring.

## 🎨 UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern Styling**: Beautiful gradient backgrounds and clean typography
- **Interactive Navigation**: Smooth transitions and hover effects
- **Information Cards**: Organized display of system and application information
- **Status Indicators**: Visual feedback for different application states

## 🚦 Development Workflow

1. **Local Development**: Use Django's development server for rapid iteration
2. **Version Control**: Commit changes to Git repository
3. **Testing**: Run tests and validate functionality
4. **Docker Build**: Test containerized version locally
5. **Deployment**: Deploy to Fly.io with automatic health checks
6. **Monitoring**: Monitor application health and performance

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/django-demo-app/issues).

## 📞 Support

If you have any questions or need help with deployment, please open an issue or contact the development team.

---

**Happy coding!** 🎉