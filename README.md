<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <title>Geershati Saxena · Cyberpunk Data Science README</title>
  <!-- Google Fonts + Font Awesome (premium icons) -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: radial-gradient(circle at 20% 30%, #0a0f1f, #03050b);
      font-family: 'Inter', 'Space Grotesk', system-ui, -apple-system, sans-serif;
      color: #eef5ff;
      line-height: 1.5;
      padding: 2rem 1.5rem;
    }

    /* custom scrollbar (neon touch) */
    ::-webkit-scrollbar {
      width: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0e1429;
      border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
      background: #0affbc;
      border-radius: 10px;
      box-shadow: 0 0 5px #0affbc;
    }

    /* main container — glassmorphism card style */
    .readme-container {
      max-width: 1300px;
      margin: 0 auto;
      background: rgba(12, 20, 35, 0.45);
      backdrop-filter: blur(14px);
      border-radius: 2rem;
      border: 1px solid rgba(10, 255, 186, 0.25);
      box-shadow: 0 25px 45px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(10, 255, 186, 0.1) inset;
      padding: 2rem 2rem 2.5rem;
      transition: all 0.3s ease;
    }

    /* glitch effect for main title */
    .glitch {
      font-size: 3rem;
      font-weight: 800;
      font-family: 'Space Grotesk', monospace;
      text-transform: uppercase;
      position: relative;
      text-shadow: 0.05em 0 0 #ff00c1, -0.05em -0.025em 0 #00fff9;
      animation: glitch-shake 0.3s infinite alternate;
      letter-spacing: -0.02em;
    }
    @keyframes glitch-shake {
      0% { text-shadow: 0.03em 0 0 #ff00c1, -0.03em -0.02em 0 #0affbc; }
      100% { text-shadow: -0.03em 0.02em 0 #ff00c1, 0.04em -0.01em 0 #0affbc; }
    }

    .neon-sub {
      font-size: 1.1rem;
      background: linear-gradient(135deg, #c0e0ff, #a0f0e8);
      background-clip: text;
      -webkit-background-clip: text;
      color: transparent;
      font-weight: 500;
      letter-spacing: 0.3px;
      border-left: 3px solid #0affbc;
      padding-left: 1rem;
    }

    /* animated gradient border for cards */
    .card-neon {
      background: rgba(5, 12, 24, 0.6);
      backdrop-filter: blur(8px);
      border-radius: 1.5rem;
      border: 1px solid rgba(10, 255, 186, 0.3);
      transition: transform 0.25s ease, box-shadow 0.3s;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }
    .card-neon:hover {
      transform: translateY(-4px);
      box-shadow: 0 15px 30px rgba(0, 255, 200, 0.1), 0 0 12px rgba(10, 255, 186, 0.4);
      border-color: #0affbc;
    }

    /* tech stack & soft skills badges — dynamic hover & scaling */
    .badge-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
      margin-top: 1rem;
    }
    .tech-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(0, 255, 200, 0.08);
      backdrop-filter: blur(4px);
      padding: 0.5rem 1rem;
      border-radius: 40px;
      font-size: 0.85rem;
      font-weight: 500;
      font-family: 'Inter', monospace;
      letter-spacing: 0.3px;
      border: 1px solid rgba(10, 255, 186, 0.5);
      transition: all 0.2s cubic-bezier(0.2, 0.9, 0.4, 1.1);
      color: #d4f5ff;
      text-decoration: none;
    }
    .tech-badge i, .tech-badge svg {
      font-size: 1rem;
      filter: drop-shadow(0 0 2px cyan);
    }
    .tech-badge:hover {
      background: rgba(10, 255, 186, 0.2);
      border-color: #0affbc;
      transform: scale(1.05);
      box-shadow: 0 0 12px rgba(10, 255, 186, 0.5);
      color: white;
    }

    /* social icon row — animated neon pulse */
    .social-links {
      display: flex;
      flex-wrap: wrap;
      gap: 1.2rem;
      margin: 1rem 0 0.5rem;
    }
    .social-icon {
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(8px);
      padding: 0.5rem 1.2rem;
      border-radius: 2rem;
      font-size: 1.1rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: 0.2s;
      border: 1px solid rgba(10, 255, 186, 0.4);
      color: #eef2ff;
      text-decoration: none;
    }
    .social-icon i {
      font-size: 1.4rem;
      transition: transform 0.2s;
    }
    .social-icon:hover {
      background: #0affbc20;
      border-color: #0affbc;
      box-shadow: 0 0 15px #0affbc60;
      transform: translateY(-3px);
    }
    .social-icon:hover i {
      transform: scale(1.1);
      text-shadow: 0 0 6px cyan;
    }

    /* stats container: animated glow counters (minimal) */
    .stats-wrapper {
      display: flex;
      flex-wrap: wrap;
      gap: 2rem;
      justify-content: space-between;
      margin: 2rem 0;
    }
    .stat-card {
      flex: 1;
      min-width: 220px;
      background: rgba(2, 8, 18, 0.7);
      border-radius: 1.2rem;
      padding: 1rem;
      text-align: center;
      backdrop-filter: blur(5px);
      border: 1px solid rgba(0, 255, 200, 0.4);
      transition: all 0.2s;
    }
    .stat-card img {
      max-width: 100%;
      border-radius: 12px;
      filter: drop-shadow(0 0 6px #0affbc80);
      transition: transform 0.3s;
    }
    .stat-card:hover img {
      transform: scale(1.02);
    }

    /* section titles */
    .section-title {
      font-size: 1.8rem;
      font-weight: 700;
      background: linear-gradient(120deg, #fff, #0affbc);
      background-clip: text;
      -webkit-background-clip: text;
      color: transparent;
      margin-bottom: 1rem;
      letter-spacing: -0.3px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      border-bottom: 2px solid #0affbc70;
      padding-bottom: 5px;
    }

    hr {
      border: none;
      height: 1px;
      background: linear-gradient(90deg, transparent, #0affbc, #ff00c1, transparent);
      margin: 1.5rem 0;
    }

    /* quote block animation */
    .quote-block {
      background: linear-gradient(145deg, #0b1120, #03070f);
      padding: 1.5rem;
      border-radius: 2rem;
      text-align: center;
      font-size: 1.1rem;
      font-style: italic;
      border-left: 6px solid #ff00c1;
      border-right: 2px solid #0affbc40;
      animation: pulse-glow 3s infinite alternate;
    }
    @keyframes pulse-glow {
      0% { box-shadow: 0 0 2px #0affbc30; border-left-color: #ff00c1; }
      100% { box-shadow: 0 0 20px #0affbc60; border-left-color: #0affbc; }
    }

    .visit-badge {
      display: flex;
      justify-content: flex-end;
      margin-top: 1rem;
    }

    /* responsiveness */
    @media (max-width: 780px) {
      .readme-container {
        padding: 1.3rem;
      }
      .glitch {
        font-size: 2rem;
      }
      .stats-wrapper {
        flex-direction: column;
      }
    }

    /* additional shiny animations for badges container */
    @keyframes fadeSlideUp {
      from { opacity: 0; transform: translateY(15px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .animated-section {
      animation: fadeSlideUp 0.5s ease-out forwards;
      opacity: 0;
    }
    .delay-1 { animation-delay: 0.1s; }
    .delay-2 { animation-delay: 0.2s; }
    .delay-3 { animation-delay: 0.3s; }
    .delay-4 { animation-delay: 0.4s; }
  </style>
</head>
<body>
<div class="readme-container">
  
  <!-- Hero Section with Glitch + animated typing vibe -->
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
    <div>
      <h1 class="glitch">✦ GEERSHATI SAXENA ✦</h1>
      <div class="neon-sub" style="margin-top: 12px;">
        <i class="fas fa-brain" style="color:#0affbc; margin-right: 8px;"></i> Data Science · AI · Futurist
      </div>
      <div style="margin-top: 1rem; max-width: 700px;">
        <p style="font-size: 1rem; font-weight: 400; background: rgba(0,0,0,0.3); border-radius: 20px; padding: 0.7rem 1rem; backdrop-filter: blur(4px);">
          🔥 Hello there! I'm <strong class="neon-text" style="color:#b0f3ff;">Geershati Saxena</strong>, a dynamic and forward-thinking student 
          pursuing <strong>Bachelor of Computer Application (B.C.A)</strong> with a keen interest in the fascinating realms of 
          <span style="color:#0affbc;">Data Science</span> and <span style="color:#ff44cc;">Artificial Intelligence</span>. 
          I architect insights from data and build intelligent systems that push boundaries.
        </p>
      </div>
    </div>
    <!-- small decorative pulse -->
    <div style="font-size: 2rem; background: radial-gradient(circle, #0affbc20, transparent); padding: 0.8rem; border-radius: 50%;">
      <i class="fas fa-microchip" style="color:#0affbc; filter: drop-shadow(0 0 5px cyan);"></i>
    </div>
  </div>

  <!-- Socials with animated neon icons -->
  <div class="animated-section delay-1">
    <div class="section-title"><i class="fas fa-share-alt"></i> NEON NETWORK</div>
    <div class="social-links">
      <a href="https://instagram.com/geershati_saxena" target="_blank" class="social-icon"><i class="fab fa-instagram"></i> Instagram</a>
      <a href="https://linkedin.com/in/geershati-saxena" target="_blank" class="social-icon"><i class="fab fa-linkedin-in"></i> LinkedIn</a>
      <a href="https://pinterest.com/geershati" target="_blank" class="social-icon"><i class="fab fa-pinterest"></i> Pinterest</a>
      <a href="mailto:geershatisaxena110@gmail.com" class="social-icon"><i class="fas fa-envelope"></i> Email</a>
    </div>
  </div>

  <hr>

  <!-- GitHub Stats: Cards with dynamic hover and animation -->
  <div class="stats-wrapper animated-section delay-2">
    <div class="stat-card">
      <img src="https://github-readme-stats.vercel.app/api?username=geershatisaxena&theme=radical&hide_border=true&include_all_commits=true&count_private=true&bg_color=00000000&title_color=0affbc&icon_color=ff44cc&text_color=ddddff" alt="GitHub Stats" loading="lazy">
    </div>
    <div class="stat-card">
      <img src="https://nirzak-streak-stats.vercel.app/?user=geershatisaxena&theme=radical&hide_border=true&background=00000000&stroke=0affbc&ring=ff44cc&fire=0affbc&currStreakNum=ffffff" alt="Streak Stats">
    </div>
    <div class="stat-card">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=geershatisaxena&theme=radical&hide_border=true&layout=compact&bg_color=00000000&title_color=0affbc&text_color=c0c0ff" alt="Top Languages">
    </div>
  </div>

  <!-- Tech Stack / Tools section (premium animated badges) -->
  <div class="animated-section delay-3">
    <div class="section-title"><i class="fas fa-cogs"></i> ⚡ CYBER DECK · TECH STACK</div>
    <div class="badge-grid">
      <!-- icons from fontawesome and custom brand representation: we'll keep original style but add animation and icons-->
      <span class="tech-badge"><i class="fab fa-python"></i> Python</span>
      <span class="tech-badge"><i class="fas fa-database"></i> SQL</span>
      <span class="tech-badge"><i class="fas fa-chart-line"></i> Pandas</span>
      <span class="tech-badge"><i class="fas fa-chart-bar"></i> NumPy</span>
      <span class="tech-badge"><i class="fas fa-chart-pie"></i> Matplotlib</span>
      <span class="tech-badge"><i class="fas fa-chart-simple"></i> Seaborn</span>
      <span class="tech-badge"><i class="fas fa-chart-scatter"></i> Plotly</span>
      <span class="tech-badge"><i class="fas fa-microchip"></i> Scikit-learn</span>
      <span class="tech-badge"><i class="fas fa-code"></i> HTML5/CSS3/JS</span>
      <span class="tech-badge"><i class="fab fa-js"></i> JavaScript</span>
      <span class="tech-badge"><i class="fas fa-cloud"></i> Vercel / Render</span>
      <span class="tech-badge"><i class="fas fa-chalkboard-user"></i> Power BI</span>
      <span class="tech-badge"><i class="fas fa-file-excel"></i> Excel / Sheets</span>
      <span class="tech-badge"><i class="fab fa-jupyter"></i> Jupyter/Colab</span>
      <span class="tech-badge"><i class="fas fa-chart-line"></i> Streamlit</span>
      <span class="tech-badge"><i class="fas fa-robot"></i> ChatGPT / GPT-4</span>
      <span class="tech-badge"><i class="fas fa-robot"></i> DALL·E / Bard</span>
      <span class="tech-badge"><i class="fas fa-code-branch"></i> GitHub Copilot</span>
      <span class="tech-badge"><i class="fas fa-chart-network"></i> IBM Cognos / SPSS</span>
      <span class="tech-badge"><i class="fas fa-chart-simple"></i> Data Cleaning · EDA</span>
      <span class="tech-badge"><i class="fas fa-brain"></i> BI & DDDM</span>
      <span class="tech-badge"><i class="fas fa-turtle"></i> Python Turtle</span>
    </div>
  </div>

  <hr>

  <!-- Soft Skills - premium showcase with animated badge grid (massive set, condensed style but high end) -->
  <div class="animated-section delay-4">
    <div class="section-title"><i class="fas fa-heart"></i> ✦ SOFT SYNAPSE · CORE SKILLS</div>
    <div class="badge-grid" style="gap: 0.6rem;">
      <span class="tech-badge"><i class="fas fa-comments"></i> Communication</span>
      <span class="tech-badge"><i class="fas fa-users"></i> Teamwork</span>
      <span class="tech-badge"><i class="fas fa-crown"></i> Leadership</span>
      <span class="tech-badge"><i class="fas fa-puzzle-piece"></i> Problem Solving</span>
      <span class="tech-badge"><i class="fas fa-brain"></i> Critical Thinking</span>
      <span class="tech-badge"><i class="fas fa-sync-alt"></i> Adaptability</span>
      <span class="tech-badge"><i class="fas fa-lightbulb"></i> Creativity</span>
      <span class="tech-badge"><i class="fas fa-clock"></i> Time Management</span>
      <span class="tech-badge"><i class="fas fa-briefcase"></i> Work Ethic</span>
      <span class="tech-badge"><i class="fas fa-search"></i> Attention to Detail</span>
      <span class="tech-badge"><i class="fas fa-hand-holding-heart"></i> Empathy</span>
      <span class="tech-badge"><i class="fas fa-handshake"></i> Conflict Resolution</span>
      <span class="tech-badge"><i class="fas fa-ear-listen"></i> Active Listening</span>
      <span class="tech-badge"><i class="fas fa-microphone-alt"></i> Public Speaking</span>
      <span class="tech-badge"><i class="fas fa-gavel"></i> Negotiation</span>
      <span class="tech-badge"><i class="fas fa-chart-line"></i> Decision Making</span>
      <span class="tech-badge"><i class="fas fa-smile"></i> Positive Attitude</span>
      <span class="tech-badge"><i class="fas fa-battery-full"></i> Self-Motivation</span>
      <span class="tech-badge"><i class="fas fa-tasks"></i> Responsibility</span>
      <span class="tech-badge"><i class="fas fa-people-arrows"></i> Collaboration</span>
      <span class="tech-badge"><i class="fas fa-heartbeat"></i> Emotional Intelligence</span>
      <span class="tech-badge"><i class="fas fa-seedling"></i> Growth Mindset</span>
      <span class="tech-badge"><i class="fas fa-rocket"></i> Initiative</span>
      <span class="tech-badge"><i class="fas fa-dumbbell"></i> Resilience</span>
      <span class="tech-badge"><i class="fas fa-chalkboard"></i> Mentoring</span>
      <span class="tech-badge"><i class="fas fa-comment-dots"></i> Cross-functional Comm</span>
      <span class="tech-badge"><i class="fas fa-chart-simple"></i> Strategic Thinking</span>
      <span class="tech-badge"><i class="fas fa-globe"></i> Remote Collaboration</span>
      <span class="tech-badge"><i class="fas fa-balance-scale"></i> Ethical Mindset</span>
      <span class="tech-badge"><i class="fas fa-notebook"></i> Organizational Skills</span>
    </div>
  </div>

  <hr>

  <!-- Random Dev Quote with animated border + smooth transitions -->
  <div class="quote-block animated-section">
    <i class="fas fa-quote-left" style="color:#0affbc; margin-right: 10px;"></i> 
    <strong>✦ RANDOM DEV QUOTE ✦</strong><br>
    <!-- dynamic quote via API but also fallback to static random-ish? we use github-readme quotes API? We'll embed via iframe or image, but better to embed standard widget as image to keep dynamic? We'll use standard markdown compatible image but it's HTML, so we can embed the quotes API url as an img -->
    <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" alt="Random Dev Quote" style="max-width:100%; margin-top: 12px; border-radius: 20px; background: #00000040; padding: 5px;">
  </div>

  <!-- Visit counter + github info with futuristic badge -->
  <div class="visit-badge animated-section delay-2" style="justify-content: space-between; align-items: center; flex-wrap: wrap;">
    <div style="display: flex; gap: 12px;">
      <span class="tech-badge" style="background: #0affbc10;"><i class="fas fa-eye"></i> 
        <img src="https://visitcount.itsvg.in/api?id=geershatisaxena&icon=5&color=12" alt="visit counter" style="display: inline-block; margin-left: 6px; vertical-align: middle;">
      </span>
      <span class="tech-badge"><i class="fab fa-github"></i> @geershatisaxena</span>
    </div>
    <div style="font-size: 0.75rem; color: #0affbc80;">
      <i class="fas fa-shield-alt"></i> cyberpunk • data alchemy
    </div>
  </div>

  <!-- subtle footer note: "Proudly created with enhanced neon design" but keep original credit vibe -->
  <div style="text-align: center; margin-top: 2rem; font-size: 0.75rem; opacity: 0.6; border-top: 1px dashed #0affbc30; padding-top: 1rem;">
    <i class="fas fa-bolt"></i> 2026 • Geershati Saxena | Glassmorphism/Cyberdeck Interface • AI & Data Science Aspirant
  </div>
</div>

<!-- add a bit of JavaScript to simulate dynamic glitch or neon flicker? optional small effect -->
<script>
  // small console trick: no heavy load, just ensure images lazy load?
  // Additionally we add dynamic glow class toggles for a futuristic feel 
  const badges = document.querySelectorAll('.tech-badge');
  setInterval(() => {
    badges.forEach((badge, idx) => {
      if (Math.random() > 0.97) {
        badge.style.boxShadow = '0 0 12px #0affbc';
        setTimeout(() => { badge.style.boxShadow = ''; }, 200);
      }
    });
  }, 1800);
</script>
</body>
</html>
