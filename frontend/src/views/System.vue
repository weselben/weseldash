<template>
  <div class="system">
    <div class="system-header">
      <h1>System Management</h1>
      <p>Monitor system stats, manage subscriptions, and track inventory</p>
    </div>
    
    <div class="system-modules">
      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-server"></i>
          <h3>System Monitor</h3>
        </div>
        <div class="module-content">
          <p>Real-time monitoring of your servers and devices.</p>
          <div class="placeholder-features">
            <span>CPU/Memory/Disk usage</span>
            <span>Multi-host support</span>
            <span>Historical data</span>
            <span>Alerts & notifications</span>
          </div>
        </div>
      </div>

      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-credit-card"></i>
          <h3>Subscription Tracker</h3>
        </div>
        <div class="module-content">
          <p>Keep track of all your recurring subscriptions and expenses.</p>
          <div class="placeholder-features">
            <span>Billing reminders</span>
            <span>Cost analysis</span>
            <span>Usage tracking</span>
            <span>Cancellation alerts</span>
          </div>
        </div>
      </div>

      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-list"></i>
          <h3>Home Inventory</h3>
        </div>
        <div class="module-content">
          <p>Catalog and manage your personal belongings with photos.</p>
          <div class="placeholder-features">
            <span>Photo management</span>
            <span>Warranty tracking</span>
            <span>Purchase history</span>
            <span>Location organization</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'System'
}
</script>

<style lang="scss" scoped>
.system {
  max-width: 1200px;
  margin: 0 auto;
}

.system-header {
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

.system-modules {
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