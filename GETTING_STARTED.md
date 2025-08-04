# Getting Started with Personal Dashboard

Welcome to the Personal Dashboard project! This guide will help you get up and running quickly.

## 🚀 Quick Setup (5 minutes)

### 1. Prerequisites
Ensure you have these installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

### 2. Clone and Start
```bash
# Clone the repository
git clone <your-repo-url>
cd personal-dashboard

# Copy environment configuration
cp .env .env.local  # Backup original
# Edit .env with your API keys (optional for initial testing)

# Start all services
docker-compose up -d

# Check if services are running
docker-compose ps
```

### 3. Access Your Dashboard
- 🌐 **Web App**: http://localhost:3000
- 🔧 **API Docs**: http://localhost:8000/docs
- 📊 **Health Check**: http://localhost:8000/health

## 🔑 First Steps

### Configure API Keys (Optional)
Edit `.env` to add your AI service keys:
```bash
# AI Configuration (optional for testing)
OPENAI_API_KEY=sk-your-openai-key-here
GEMINI_API_KEY=your-gemini-key-here
OPENROUTER_API_KEY=your-openrouter-key-here
```

### Create Your First Content
1. **📝 Add a Wiki Note**: Go to Knowledge → Wiki and create your first note
2. **📰 Add RSS Feed**: Subscribe to your favorite RSS feeds
3. **📚 Log Media**: Track a book you're reading or movie you watched
4. **✅ Create Habit**: Set up a habit you want to track

## 🛠️ Development Setup

### Backend Development
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload
```

### Frontend Development
```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run serve
```

### Database Access
```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U dashboard_user -d dashboard

# Run migrations
docker-compose exec backend alembic upgrade head
```

## 📁 Key Files to Know

- `.env` - Environment configuration
- `docker-compose.yml` - Service orchestration
- `backend/main.py` - FastAPI application entry point
- `frontend/src/App.vue` - Vue.js main component
- `backend/database/models.py` - Database schema
- `frontend/src/services/api.js` - API service layer

## 🔍 Exploring the Codebase

### Backend Structure
```
backend/
├── main.py              # FastAPI app
├── database/
│   ├── models.py        # SQLAlchemy models
│   └── database.py      # DB configuration
├── routers/             # API endpoints
│   ├── ai_chat.py       # AI chat routes
│   ├── knowledge.py     # Knowledge management
│   ├── analytics.py     # Personal analytics
│   └── system.py        # System management
└── alembic/             # Database migrations
```

### Frontend Structure
```
frontend/src/
├── main.js              # Vue.js entry point
├── App.vue              # Main app component
├── router/              # Vue Router
├── views/               # Page components
├── services/            # API services
└── assets/              # Static assets
```

## 🐛 Common Issues

### Services Won't Start
```bash
# Check what's running on your ports
netstat -tulpn | grep -E ':(3000|8000|5432|8080)'

# Stop conflicting services or change ports in docker-compose.yml
```

### Database Connection Issues
```bash
# Check PostgreSQL logs
docker-compose logs postgres

# Restart database
docker-compose restart postgres
```

### Frontend Build Issues
```bash
# Clear and reinstall dependencies
cd frontend
rm -rf node_modules package-lock.json
npm install
```

## 🎯 What to Build Next

### Beginner Tasks
- Add a new field to an existing model
- Create a new Vue component
- Add a new API endpoint
- Improve styling/UI

### Intermediate Tasks
- Implement semantic search for wiki notes
- Add email notifications for habits
- Create data visualization charts
- Add user authentication

### Advanced Tasks
- Implement real-time updates with WebSockets
- Add AI-powered content suggestions
- Create mobile app with React Native
- Add automated testing suite

## 📚 Learning Resources

### Technologies Used
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vue.js 3 Guide](https://vuejs.org/guide/)
- [PostgreSQL Tutorial](https://www.postgresql.org/docs/)
- [Docker Compose Guide](https://docs.docker.com/compose/)

### Best Practices
- [Conventional Commits](https://www.conventionalcommits.org/)
- [REST API Design](https://restfulapi.net/)
- [Vue.js Style Guide](https://vuejs.org/style-guide/)
- [Python PEP 8](https://pep8.org/)

## 💬 Getting Help

1. **Check the logs**: `docker-compose logs [service-name]`
2. **Read the full README.md** for detailed documentation
3. **Search existing issues** in the repository
4. **Ask questions** by creating a new issue

## 🎉 You're Ready!

You now have a working Personal Dashboard! Start exploring the features and consider contributing to make it even better.

**Next Steps:**
1. Customize the dashboard to your needs
2. Add your personal data (notes, habits, etc.)
3. Explore the API documentation
4. Consider contributing a feature or improvement

Happy coding! 🚀