---
layout: default
title: Главная
description: Блог о настольных ролевых играх, программировании и медиа
---

<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
<link rel="stylesheet" href="/assets/css/home.css">

<main class="home-container">
  <section class="hero-section">
    <div class="hero-content">
      <h1 class="hero-title">🎲 Добро пожаловать в мой блог! 🎮</h1>
      <p class="hero-subtitle">Здесь я делюсь мыслями о настольных ролевых играх, программировании и медиа</p>
      
      <div class="hero-cta">
        <a href="#recent-posts" class="btn">Читать статьи</a>
        <a href="/about" class="btn btn-outline">Обо мне</a>
      </div>
    </div>
  </section>

  <section id="recent-posts" class="posts-section">
    <h2 class="section-title">Последние публикации</h2>
    
    <div class="posts-grid">
      {% for post in site.posts limit:6 %}
      <article class="post-card">
        <div class="post-card-content">
          <h3 class="post-card-title">
            <a href="{{ post.url }}">{{ post.title }}</a>
          </h3>
          
          <div class="post-meta">
            <time datetime="{{ post.date | date_to_xmlschema }}">
              {{ post.date | date: "%d.%m.%Y" }}
            </time>
            <span class="reading-time">
              {% assign words = post.content | number_of_words %}
              {% if words < 360 %}1 мин{% else %}{{ words | divided_by:180 }} мин{% endif %}
            </span>
          </div>
          
          <p class="post-excerpt">
            {{ post.excerpt | strip_html | truncate: 140 }}
          </p>
          
          {% if post.tags.size > 0 %}
          <div class="post-tags">
            {% for tag in post.tags limit:3 %}
            <span class="tag">{{ tag }}</span>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
    
    <div class="all-posts-link">
      <a href="/_posts" class="btn">Все статьи →</a>
    </div>
  </section>


</main>

<style>
  :root {
    --primary: #6e41e2;
    --primary-dark: #5835b0;
    --text: #2d3748;
    --text-light: #4a5568;
    --bg: #f7fafc;
    --card-bg: #ffffff;
    --border: #e2e8f0;
  }
  
  .home-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }
  
  .hero-section {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    padding: 4rem 1rem;
    border-radius: 0.5rem;
    margin: 2rem 0;
    text-align: center;
  }
  
  .hero-title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    max-width: 700px;
    margin: 0 auto 2rem;
    opacity: 0.9;
  }
  
  .hero-cta {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }
  
  .btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: white;
    color: var(--primary);
    border-radius: 0.25rem;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s;
  }
  
  .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }
  
  .btn-outline {
    background: transparent;
    border: 2px solid white;
    color: white;
  }
  
  .section-title {
    text-align: center;
    margin: 3rem 0 2rem;
    font-size: 2rem;
    color: var(--text);
  }
  
  .posts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
  }
  
  .post-card {
    background: var(--card-bg);
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    transition: transform 0.2s;
  }
  
  .post-card:hover {
    transform: translateY(-5px);
  }
  
  .post-card-content {
    padding: 1.5rem;
  }
  
  .post-card-title {
    margin: 0 0 0.5rem;
    font-size: 1.25rem;
  }
  
  .post-card-title a {
    color: var(--text);
    text-decoration: none;
  }
  
  .post-meta {
    display: flex;
    gap: 1rem;
    font-size: 0.875rem;
    color: var(--text-light);
    margin-bottom: 0.75rem;
  }
  
  .post-excerpt {
    color: var(--text-light);
    margin: 0.5rem 0 1rem;
    font-size: 0.9375rem;
  }
  
  .post-tags {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  
  .tag {
    background: var(--bg);
    color: var(--text-light);
    padding: 0.25rem 0.5rem;
    border-radius: 9999px;
    font-size: 0.75rem;
  }
  
  .all-posts-link {
    text-align: center;
    margin: 2rem 0;
  }
  
  .categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0 4rem;
  }
  
  .category-card {
    background: var(--card-bg);
    border-radius: 0.5rem;
    padding: 1.5rem;
    text-align: center;
    text-decoration: none;
    color: var(--text);
    border: 1px solid var(--border);
    transition: all 0.2s;
  }
  
  .category-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
  }
  
  .category-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  .category-card h3 {
    margin: 0.5rem 0;
  }
  
  .category-card p {
    color: var(--text-light);
    font-size: 0.9375rem;
    margin: 0;
  }
  
  @media (max-width: 768px) {
    .hero-title {
      font-size: 2rem;
    }
    
    .hero-subtitle {
      font-size: 1.1rem;
    }
    
    .hero-cta {
      flex-direction: column;
      align-items: center;
    }
    
    .btn {
      width: 100%;
      max-width: 250px;
    }
  }
</style>
