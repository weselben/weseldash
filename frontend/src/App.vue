<template>
  <div id="app" class="dashboard-app">
    <!-- Navigation Header -->
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="brand-link">
          <i class="pi pi-home"></i>
          <span>Personal Dashboard</span>
        </router-link>
      </div>
      
      <div class="navbar-menu">
        <router-link to="/" class="nav-item">
          <i class="pi pi-home"></i>
          <span>Dashboard</span>
        </router-link>
        
        <router-link to="/ai-chat" class="nav-item">
          <i class="pi pi-comments"></i>
          <span>AI Chat</span>
        </router-link>
        
        <router-link to="/knowledge" class="nav-item">
          <i class="pi pi-book"></i>
          <span>Knowledge</span>
        </router-link>
        
        <router-link to="/analytics" class="nav-item">
          <i class="pi pi-chart-line"></i>
          <span>Analytics</span>
        </router-link>
        
        <router-link to="/system" class="nav-item">
          <i class="pi pi-cog"></i>
          <span>System</span>
        </router-link>
      </div>
    </nav>

    <!-- Main Content Area -->
    <main class="main-content">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2024 Personal Dashboard - Self-hosted with ❤️</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted() {
    // Check if running as PWA
    if (window.matchMedia('(display-mode: standalone)').matches) {
      console.log('Running as PWA')
    }
  }
}
</script>

<style lang="scss">
.dashboard-app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'Inter', sans-serif;
}

.navbar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);

  .navbar-brand {
    .brand-link {
      display: flex;
      align-items: center;
      color: white;
      text-decoration: none;
      font-size: 1.5rem;
      font-weight: 600;

      i {
        margin-right: 0.5rem;
        font-size: 1.8rem;
      }
    }
  }

  .navbar-menu {
    display: flex;
    gap: 2rem;

    .nav-item {
      display: flex;
      align-items: center;
      color: rgba(255, 255, 255, 0.9);
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 8px;
      transition: all 0.3s ease;

      &:hover {
        background: rgba(255, 255, 255, 0.1);
        color: white;
      }

      &.router-link-active {
        background: rgba(255, 255, 255, 0.2);
        color: white;
      }

      i {
        margin-right: 0.5rem;
      }

      span {
        font-weight: 500;
      }
    }
  }
}

.main-content {
  flex: 1;
  padding: 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  min-height: calc(100vh - 140px);
}

.footer {
  background: #2c3e50;
  color: #ecf0f1;
  text-align: center;
  padding: 1rem;
  
  p {
    margin: 0;
    font-size: 0.9rem;
  }
}

// Responsive design
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    gap: 1rem;
    
    .navbar-menu {
      gap: 1rem;
      flex-wrap: wrap;
      justify-content: center;
    }
  }
  
  .main-content {
    padding: 1rem;
  }
}
</style>