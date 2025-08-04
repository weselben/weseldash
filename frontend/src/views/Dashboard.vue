<template>
  <div class="dashboard">
    <div class="dashboard-header">
      <h1>Personal Dashboard</h1>
      <p>Welcome to your self-hosted personal hub</p>
    </div>

    <div class="dashboard-grid">
      <!-- AI Chat Widget -->
      <div class="dashboard-card">
        <div class="card-header">
          <i class="pi pi-comments"></i>
          <h3>AI Assistant</h3>
        </div>
        <div class="card-content">
          <p>Chat with your personal AI assistant</p>
          <router-link to="/ai-chat" class="card-button">
            Open Chat
          </router-link>
        </div>
      </div>

      <!-- Knowledge Widget -->
      <div class="dashboard-card">
        <div class="card-header">
          <i class="pi pi-book"></i>
          <h3>Knowledge</h3>
        </div>
        <div class="card-content">
          <p>Manage your wiki, RSS feeds, and bookmarks</p>
          <div class="stats">
            <span>{{ knowledgeStats.notes }} Notes</span>
            <span>{{ knowledgeStats.feeds }} RSS Feeds</span>
            <span>{{ knowledgeStats.bookmarks }} Bookmarks</span>
          </div>
          <router-link to="/knowledge" class="card-button">
            Explore Knowledge
          </router-link>
        </div>
      </div>

      <!-- Analytics Widget -->
      <div class="dashboard-card">
        <div class="card-header">
          <i class="pi pi-chart-line"></i>
          <h3>Analytics</h3>
        </div>
        <div class="card-content">
          <p>Track habits, media, and daily insights</p>
          <div class="stats">
            <span>{{ analyticsStats.habits }} Active Habits</span>
            <span>{{ analyticsStats.mediaItems }} Media Items</span>
          </div>
          <router-link to="/analytics" class="card-button">
            View Analytics
          </router-link>
        </div>
      </div>

      <!-- System Widget -->
      <div class="dashboard-card">
        <div class="card-header">
          <i class="pi pi-server"></i>
          <h3>System Status</h3>
        </div>
        <div class="card-content">
          <div class="system-stats" v-if="systemStats">
            <div class="stat-item">
              <span class="label">CPU:</span>
              <div class="progress-bar">
                <div class="progress" :style="{ width: systemStats.cpu + '%' }"></div>
              </div>
              <span class="value">{{ systemStats.cpu }}%</span>
            </div>
            <div class="stat-item">
              <span class="label">Memory:</span>
              <div class="progress-bar">
                <div class="progress" :style="{ width: systemStats.memory + '%' }"></div>
              </div>
              <span class="value">{{ systemStats.memory }}%</span>
            </div>
            <div class="stat-item">
              <span class="label">Disk:</span>
              <div class="progress-bar">
                <div class="progress" :style="{ width: systemStats.disk + '%' }"></div>
              </div>
              <span class="value">{{ systemStats.disk }}%</span>
            </div>
          </div>
          <router-link to="/system" class="card-button">
            System Management
          </router-link>
        </div>
      </div>

      <!-- Recent Activity Widget -->
      <div class="dashboard-card full-width">
        <div class="card-header">
          <i class="pi pi-clock"></i>
          <h3>Recent Activity</h3>
        </div>
        <div class="card-content">
          <div class="activity-list">
            <div v-for="activity in recentActivity" :key="activity.id" class="activity-item">
              <i :class="activity.icon"></i>
              <div class="activity-details">
                <span class="activity-description">{{ activity.description }}</span>
                <span class="activity-time">{{ formatTime(activity.timestamp) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import apiService from '../services/api'

export default {
  name: 'Dashboard',
  setup() {
    const knowledgeStats = ref({
      notes: 0,
      feeds: 0,
      bookmarks: 0
    })

    const analyticsStats = ref({
      habits: 0,
      mediaItems: 0
    })

    const systemStats = ref(null)

    const recentActivity = ref([
      {
        id: 1,
        icon: 'pi pi-book',
        description: 'Created new wiki note: "Vue.js Best Practices"',
        timestamp: new Date(Date.now() - 1000 * 60 * 30)
      },
      {
        id: 2,
        icon: 'pi pi-check',
        description: 'Completed habit: "Morning Exercise"',
        timestamp: new Date(Date.now() - 1000 * 60 * 60 * 2)
      },
      {
        id: 3,
        icon: 'pi pi-bookmark',
        description: 'Saved new bookmark: "Interesting article about AI"',
        timestamp: new Date(Date.now() - 1000 * 60 * 60 * 4)
      }
    ])

    const loadDashboardData = async () => {
      try {
        // Load knowledge stats
        const [notesResponse, feedsResponse, bookmarksResponse] = await Promise.all([
          apiService.get('/knowledge/wiki/notes'),
          apiService.get('/knowledge/rss/feeds'),
          apiService.get('/knowledge/bookmarks')
        ])
        
        knowledgeStats.value = {
          notes: notesResponse.data.length || 0,
          feeds: feedsResponse.data.length || 0,
          bookmarks: bookmarksResponse.data.length || 0
        }

        // Load analytics stats
        const [habitsResponse, mediaResponse] = await Promise.all([
          apiService.get('/analytics/habits'),
          apiService.get('/analytics/media-logs')
        ])

        analyticsStats.value = {
          habits: habitsResponse.data.filter(h => h.is_active).length || 0,
          mediaItems: mediaResponse.data.length || 0
        }

        // Load system stats
        const systemResponse = await apiService.get('/system/stats/latest')
        if (systemResponse.data.length > 0) {
          const latest = systemResponse.data[0]
          systemStats.value = {
            cpu: Math.round(latest.cpu_percent),
            memory: Math.round(latest.memory_percent),
            disk: Math.round(latest.disk_percent)
          }
        }
      } catch (error) {
        console.error('Error loading dashboard data:', error)
        // Set default values for demo
        systemStats.value = {
          cpu: 25,
          memory: 60,
          disk: 45
        }
      }
    }

    const formatTime = (timestamp) => {
      const now = new Date()
      const diff = now - timestamp
      const minutes = Math.floor(diff / (1000 * 60))
      const hours = Math.floor(diff / (1000 * 60 * 60))
      const days = Math.floor(diff / (1000 * 60 * 60 * 24))

      if (days > 0) return `${days}d ago`
      if (hours > 0) return `${hours}h ago`
      if (minutes > 0) return `${minutes}m ago`
      return 'Just now'
    }

    onMounted(() => {
      loadDashboardData()
    })

    return {
      knowledgeStats,
      analyticsStats,
      systemStats,
      recentActivity,
      formatTime
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 2rem;

  h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 0.5rem;
  }

  p {
    font-size: 1.1rem;
    color: #7f8c8d;
  }
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;

  .full-width {
    grid-column: 1 / -1;
  }
}

.dashboard-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  }

  .card-header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;

    i {
      font-size: 1.5rem;
      color: #667eea;
      margin-right: 0.75rem;
    }

    h3 {
      font-size: 1.3rem;
      color: #2c3e50;
      margin: 0;
    }
  }

  .card-content {
    p {
      color: #7f8c8d;
      margin-bottom: 1rem;
    }

    .stats {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1rem;

      span {
        background: #f8f9fa;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        color: #495057;
        font-weight: 500;
      }
    }

    .card-button {
      display: inline-block;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 0.75rem 1.5rem;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 500;
      transition: all 0.3s ease;

      &:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
      }
    }
  }
}

.system-stats {
  .stat-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.75rem;

    .label {
      min-width: 60px;
      font-weight: 500;
      color: #495057;
    }

    .progress-bar {
      flex: 1;
      height: 8px;
      background: #e9ecef;
      border-radius: 4px;
      overflow: hidden;

      .progress {
        height: 100%;
        background: linear-gradient(90deg, #28a745 0%, #ffc107 70%, #dc3545 100%);
        transition: width 0.3s ease;
      }
    }

    .value {
      min-width: 40px;
      text-align: right;
      font-weight: 600;
      color: #495057;
    }
  }
}

.activity-list {
  .activity-item {
    display: flex;
    align-items: center;
    padding: 1rem 0;
    border-bottom: 1px solid #e9ecef;

    &:last-child {
      border-bottom: none;
    }

    i {
      font-size: 1.2rem;
      color: #667eea;
      margin-right: 1rem;
      min-width: 20px;
    }

    .activity-details {
      flex: 1;

      .activity-description {
        display: block;
        color: #495057;
        font-weight: 500;
      }

      .activity-time {
        display: block;
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 0.25rem;
      }
    }
  }
}
</style>