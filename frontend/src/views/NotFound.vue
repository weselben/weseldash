<template>
  <div class="not-found">
    <div class="not-found-content">
      <div class="error-icon">
        <i class="pi pi-exclamation-triangle"></i>
      </div>
      <h1>404 - Page Not Found</h1>
      <p>The page you're looking for doesn't exist or has been moved.</p>
      <router-link to="/" class="home-button">
        <i class="pi pi-home"></i>
        Go to Dashboard
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound'
}
</script>

<style lang="scss" scoped>
.not-found {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.not-found-content {
  text-align: center;
  background: white;
  padding: 3rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

  .error-icon {
    margin-bottom: 2rem;

    i {
      font-size: 4rem;
      color: #f39c12;
    }
  }

  h1 {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 1rem;
  }

  p {
    color: #7f8c8d;
    margin-bottom: 2rem;
    font-size: 1.1rem;
  }

  .home-button {
    display: inline-flex;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem 2rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }

    i {
      margin-right: 0.5rem;
    }
  }
}
</style>