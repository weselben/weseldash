<template>
  <div class="knowledge">
    <div class="knowledge-header">
      <h1>Knowledge Management</h1>
      <p>Manage your digital garden, RSS feeds, and bookmarks</p>
    </div>
    
    <div class="knowledge-modules">
      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-book"></i>
          <h3>Personal Wiki</h3>
        </div>
        <div class="module-content">
          <p>Create and organize your digital garden with interconnected notes.</p>
          <ul>
            <li>Markdown-based notes</li>
            <li>Semantic search</li>
            <li>Note linking</li>
            <li>Vector embeddings</li>
          </ul>
        </div>
      </div>

      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-rss"></i>
          <h3>RSS Reader</h3>
        </div>
        <div class="module-content">
          <p>Subscribe to and manage your favorite RSS feeds.</p>
          <ul>
            <li>Feed management</li>
            <li>Article reading</li>
            <li>Automatic updates</li>
            <li>Reading progress</li>
          </ul>
        </div>
      </div>

      <div class="module-card">
        <div class="module-header">
          <i class="pi pi-bookmark"></i>
          <h3>Wayback Bookmarks</h3>
        </div>
        <div class="module-content">
          <p>Save and archive web pages with full HTML snapshots.</p>
          <ul>
            <li>Full page archiving</li>
            <li>Historical versions</li>
            <li>Search archived content</li>
            <li>Change tracking</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Knowledge'
}
</script>

<style lang="scss" scoped>
.knowledge {
  max-width: 1200px;
  margin: 0 auto;
}

.knowledge-header {
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

.knowledge-modules {
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
      margin-bottom: 1rem;
      line-height: 1.6;
    }

    ul {
      color: #495057;
      
      li {
        margin-bottom: 0.5rem;
        position: relative;
        padding-left: 1rem;

        &::before {
          content: '•';
          color: #667eea;
          font-weight: bold;
          position: absolute;
          left: 0;
        }
      }
    }
  }
}
</style>