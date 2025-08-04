<template>
  <div class="analytics">
    <div class="analytics-header">
      <h1>Personal Analytics</h1>
      <p>Track your habits, media consumption, and daily insights</p>
    </div>
    
    <div class="analytics-modules">
      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-check-circle"></i>
          <h3>Habit Tracker</h3>
        </div>
        <div class="module-content">
          <p>Build and maintain positive habits with visual tracking.</p>
          <div class="placeholder-features">
            <span>Daily/Weekly/Monthly habits</span>
            <span>Progress visualization</span>
            <span>Streak counting</span>
            <span>Goal setting</span>
          </div>
        </div>
      </div>

      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-video"></i>
          <h3>Media Log</h3>
        </div>
        <div class="module-content">
          <p>Track books, movies, music, and other media consumption.</p>
          <div class="placeholder-features">
            <span>Reading lists</span>
            <span>Watch history</span>
            <span>Rating system</span>
            <span>Auto-sync integrations</span>
          </div>
        </div>
      </div>

      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-book"></i>
          <h3>AI Journaling</h3>
        </div>
        <div class="module-content">
          <p>Automated daily journal generation based on your activities.</p>
          <div class="placeholder-features">
            <span>Daily summaries</span>
            <span>Mood tracking</span>
            <span>Activity correlation</span>
            <span>Insights generation</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Analytics'
}
</script>

<style lang="scss" scoped>
.analytics {
  max-width: 1200px;
  margin: 0 auto;
}

.analytics-header {
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

.analytics-modules {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.module-card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  }

  .module-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;

    i {
      font-size: 2rem;
      color: #667eea;
      margin-right: 1rem;
    }

    h3 {
      font-size: 1.5rem;
      color: #2c3e50;
      margin: 0;
    }
  }

  .module-content {
    p {
      color: #7f8c8d;
      margin-bottom: 1.5rem;
      line-height: 1.6;
    }

    .placeholder-features {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;

      span {
        background: #f8f9fa;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        color: #495057;
        font-weight: 500;
      }
    }
  }
}
</style>