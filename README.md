# Personal Dashboard

A self-hosted, privacy-focused personal hub that integrates all aspects of your digital life. This Progressive Web App (PWA) empowers you to manage your data, knowledge, and daily activities from a single, private, and powerful interface.

## 🌟 Features

### 🤖 AI Chat Module
- Chat interface with personal AI assistant
- Primary/fallback AI model support (Gemini → OpenRouter)
- Integration with other modules via dedicated API functions
- Context-aware conversations

### 📚 Knowledge Management Module
- **Personal Wiki/Digital Garden**: Interconnected notes with semantic search
- **RSS Feed Reader**: Full-featured feed management and reading
- **Wayback Bookmark Manager**: URL archiving with historical snapshots

### 📊 Personal Analytics & Wellness Module
- **AI Journaling**: Automated daily journal generation
- **Media Consumption Log**: Track books, movies, music
- **Habit Tracker**: Visual habit tracking and progress monitoring

### 🏠 System & Home Management Module
- **System Stats Monitor**: Real-time server monitoring
- **Subscription Tracker**: Recurring expense management
- **Home Inventory**: Personal item cataloging with photos

## 🏗️ Architecture

### Technology Stack
- **Backend**: Python 3.10+ with FastAPI
- **Frontend**: Vue.js 3 with Node.js (Progressive Web App)
- **Database**: PostgreSQL with extensions support
- **Image Processing**: imgproxy for on-the-fly image optimization
- **Vector Search**: ChromaDB for semantic search
- **Orchestration**: Docker Compose

### Service Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   PostgreSQL    │
│   (Vue.js PWA)  │◄──►│   (FastAPI)     │◄──►│   Database      │
│   Port: 3000    │    │   Port: 8000    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                       │
        │              ┌─────────────────┐
        └─────────────►│   imgproxy      │
                       │   Port: 8080    │
                       └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd personal-dashboard
```

2. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start the services**
```bash
docker-compose up -d
```

4. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## ⚙️ Configuration

### Environment Variables

Edit the `.env` file to configure your setup:

```bash
# Database Configuration
POSTGRES_DB=dashboard
POSTGRES_USER=dashboard_user
POSTGRES_PASSWORD=your_secure_password_here

# AI Configuration
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Security
SECRET_KEY=your_secret_key_here_change_this_in_production

# API Configuration
RSS_FEED_UPDATE_INTERVAL=3600
AUTO_JOURNAL_TIME=22:00
```

### Database Setup

The application uses PostgreSQL with several extensions:

```sql
-- Automatically enabled extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";      -- UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";       -- Encryption functions
CREATE EXTENSION IF NOT EXISTS "unaccent";       -- Full-text search
```

### Database Migrations

Use Alembic for database migrations:

```bash
# Generate a new migration
docker-compose exec backend alembic revision --autogenerate -m "Description"

# Apply migrations
docker-compose exec backend alembic upgrade head

# Downgrade migration
docker-compose exec backend alembic downgrade -1
```

## 📁 Project Structure

```
personal-dashboard/
├── backend/                    # FastAPI backend
│   ├── alembic/               # Database migrations
│   ├── database/              # Database models and config
│   ├── routers/               # API route handlers
│   ├── Dockerfile             # Backend container config
│   ├── main.py                # FastAPI application
│   └── requirements.txt       # Python dependencies
├── frontend/                   # Vue.js frontend
│   ├── public/                # Static assets
│   ├── src/                   # Vue.js source code
│   │   ├── components/        # Reusable components
│   │   ├── views/             # Page components
│   │   ├── services/          # API service layer
│   │   └── router/            # Vue Router config
│   ├── Dockerfile             # Frontend container config
│   ├── vue.config.js          # Vue.js configuration
│   └── package.json           # Node.js dependencies
├── postgres-init/             # PostgreSQL initialization
├── data/                      # Persistent data volumes
├── docker-compose.yml         # Service orchestration
├── .env                       # Environment configuration
└── README.md                  # This file
```

## 🔧 Development

### Development Setup

1. **Backend Development**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. **Frontend Development**
```bash
cd frontend
npm install
npm run serve
```

3. **Database Development**
```bash
# Start only PostgreSQL
docker-compose up postgres -d

# Connect to database
docker-compose exec postgres psql -U dashboard_user -d dashboard
```

### API Development

The API follows RESTful principles with the following endpoints:

- **AI Chat**: `/api/ai/*`
- **Knowledge Management**: `/api/knowledge/*`
- **Personal Analytics**: `/api/analytics/*`
- **System Management**: `/api/system/*`

API documentation is automatically generated and available at `/docs`.

### Frontend Development

The frontend is a Vue.js 3 SPA with:
- **Vue Router** for navigation
- **Pinia** for state management
- **PrimeVue** for UI components
- **Axios** for API communication
- **PWA** capabilities for offline usage

## 📱 Progressive Web App (PWA)

The frontend is configured as a PWA with:
- Offline capability
- App-like experience
- Push notifications (future feature)
- Install prompt for mobile/desktop

To install as an app:
1. Visit the application in your browser
2. Look for the "Install" or "Add to Home Screen" option
3. Follow the prompts to install

## 🔒 Security Considerations

1. **Change default passwords** in `.env`
2. **Set strong SECRET_KEY** for JWT tokens
3. **Configure HTTPS** in production
4. **Enable PostgreSQL SSL** for production
5. **Review CORS settings** in production
6. **Set proper file permissions** for data directories

## 📊 Monitoring & Logging

### System Monitoring
The system monitoring module can track:
- CPU, Memory, Disk usage
- Multiple host support
- Historical data storage
- Custom alerts (future feature)

### Application Logs
- Backend logs via FastAPI/Uvicorn
- Frontend logs via browser console
- Database logs via PostgreSQL
- Container logs via Docker

## 🔄 Backup & Maintenance

### Database Backup
```bash
# Create backup
docker-compose exec postgres pg_dump -U dashboard_user dashboard > backup.sql

# Restore backup
docker-compose exec -T postgres psql -U dashboard_user dashboard < backup.sql
```

### File System Backup
```bash
# Backup data directory
tar -czf dashboard-backup-$(date +%Y%m%d).tar.gz data/
```

### Updates
```bash
# Update containers
docker-compose pull
docker-compose up -d

# Update dependencies (development)
cd backend && pip install -r requirements.txt --upgrade
cd frontend && npm update
```

## 🐛 Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 3000, 8000, 5432, 8080 are available
2. **Permission issues**: Check Docker permissions and file ownership
3. **Database connection**: Verify PostgreSQL is running and credentials are correct
4. **API errors**: Check backend logs with `docker-compose logs backend`
5. **Frontend build issues**: Clear node_modules and reinstall dependencies

### Debug Mode

Enable debug mode by setting `DEBUG=true` in `.env`.

### Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
docker-compose logs postgres
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Commit Message Convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(ai): add gemini model support
fix(database): resolve connection timeout issue
docs(readme): update installation instructions
refactor(frontend): restructure component hierarchy
```

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes following the coding standards
4. Write tests for new functionality
5. Update documentation as needed
6. Commit with conventional commit messages
7. Push to your fork and submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with modern web technologies
- Inspired by the self-hosting and privacy communities
- Special thanks to all open-source contributors

## 📞 Support

For support, please:
1. Check the troubleshooting section
2. Search existing issues
3. Create a new issue with detailed information
4. Include logs and configuration (without sensitive data)

---

**Happy self-hosting! 🏠✨**