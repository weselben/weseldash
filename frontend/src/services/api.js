import axios from 'axios'

// Create axios instance with default configuration
const apiClient = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem('auth_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
apiClient.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    // Handle common errors
    if (error.response?.status === 401) {
      // Unauthorized - clear token and redirect to login
      localStorage.removeItem('auth_token')
      // Could redirect to login page here
    }
    
    console.error('API Error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

// API service methods
const apiService = {
  // Generic HTTP methods
  get: (url, config = {}) => apiClient.get(url, config),
  post: (url, data = {}, config = {}) => apiClient.post(url, data, config),
  put: (url, data = {}, config = {}) => apiClient.put(url, data, config),
  delete: (url, config = {}) => apiClient.delete(url, config),

  // AI Chat methods
  chat: {
    sendMessage: (messages, model = null) => 
      apiClient.post('/ai/chat', { messages, model }),
    getModels: () => 
      apiClient.get('/ai/models')
  },

  // Knowledge management methods
  knowledge: {
    // Wiki notes
    getNotes: () => apiClient.get('/knowledge/wiki/notes'),
    getNote: (id) => apiClient.get(`/knowledge/wiki/notes/${id}`),
    createNote: (note) => apiClient.post('/knowledge/wiki/notes', note),
    updateNote: (id, note) => apiClient.put(`/knowledge/wiki/notes/${id}`, note),
    deleteNote: (id) => apiClient.delete(`/knowledge/wiki/notes/${id}`),
    searchNotes: (query) => apiClient.post('/knowledge/wiki/search', { query }),

    // RSS feeds
    getFeeds: () => apiClient.get('/knowledge/rss/feeds'),
    createFeed: (feed) => apiClient.post('/knowledge/rss/feeds', feed),
    getRSSItems: (feedId = null) => 
      apiClient.get('/knowledge/rss/items', { params: { feed_id: feedId } }),

    // Bookmarks
    getBookmarks: () => apiClient.get('/knowledge/bookmarks'),
    createBookmark: (bookmark) => apiClient.post('/knowledge/bookmarks', bookmark)
  },

  // Analytics methods
  analytics: {
    // Media logs
    getMediaLogs: (mediaType = null, status = null) => 
      apiClient.get('/analytics/media-logs', { params: { media_type: mediaType, status } }),
    createMediaLog: (mediaLog) => apiClient.post('/analytics/media-logs', mediaLog),
    updateMediaLog: (id, mediaLog) => apiClient.put(`/analytics/media-logs/${id}`, mediaLog),

    // Habits
    getHabits: (activeOnly = true) => 
      apiClient.get('/analytics/habits', { params: { active_only: activeOnly } }),
    createHabit: (habit) => apiClient.post('/analytics/habits', habit),
    logHabitCompletion: (habitId, log) => 
      apiClient.post(`/analytics/habits/${habitId}/log`, log),
    getHabitLogs: (habitId) => apiClient.get(`/analytics/habits/${habitId}/logs`),

    // Journals
    getJournals: () => apiClient.get('/analytics/journals'),
    getJournalByDate: (date) => apiClient.get(`/analytics/journals/${date}`),
    generateJournal: (date = null) => 
      apiClient.post('/analytics/journals/generate', { date })
  },

  // System methods
  system: {
    // System stats
    getStats: (hostname = null, limit = 100) => 
      apiClient.get('/system/stats', { params: { hostname, limit } }),
    getLatestStats: () => apiClient.get('/system/stats/latest'),
    submitStats: (stats) => apiClient.post('/system/stats', stats),

    // Subscriptions
    getSubscriptions: (activeOnly = true) => 
      apiClient.get('/system/subscriptions', { params: { active_only: activeOnly } }),
    createSubscription: (subscription) => 
      apiClient.post('/system/subscriptions', subscription),
    updateSubscription: (id, subscription) => 
      apiClient.put(`/system/subscriptions/${id}`, subscription),
    cancelSubscription: (id) => apiClient.delete(`/system/subscriptions/${id}`),

    // Inventory
    getInventory: (category = null, location = null) => 
      apiClient.get('/system/inventory', { params: { category, location } }),
    createInventoryItem: (item) => apiClient.post('/system/inventory', item),
    updateInventoryItem: (id, item) => apiClient.put(`/system/inventory/${id}`, item),
    deleteInventoryItem: (id) => apiClient.delete(`/system/inventory/${id}`),
    getInventoryCategories: () => apiClient.get('/system/inventory/categories'),
    getInventoryLocations: () => apiClient.get('/system/inventory/locations')
  },

  // Health check
  health: () => apiClient.get('/health', { baseURL: '' })
}

export default apiService