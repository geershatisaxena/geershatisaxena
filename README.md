<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Geershati Saxena — Profile</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Rajdhani:wght@300;400;600&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --neon-cyan:#00f5ff;
  --neon-pink:#ff006e;
  --neon-purple:#b400ff;
  --neon-green:#00ff88;
  --neon-gold:#ffd700;
  --dark-bg:#050510;
  --card-bg:#0a0a1a;
  --card-border:#1a1a3a;
}
html{scroll-behavior:smooth}
body{
  background:#050510;
  min-height:100vh;
  font-family:'Rajdhani',sans-serif;
  color:#e0e0ff;
  overflow-x:hidden;
}

/* ── SCANLINES ── */
body::before{
  content:'';
  position:fixed;top:0;left:0;width:100%;height:100%;
  background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,245,255,.012) 2px,rgba(0,245,255,.012) 4px);
  pointer-events:none;z-index:0;
  animation:scanroll 10s linear infinite;
}
@keyframes scanroll{0%{background-position:0 0}100%{background-position:0 120px}}

/* ── GRID BG ── */
.grid-bg{
  position:fixed;top:0;left:0;width:100%;height:100%;
  background-image:
    linear-gradient(rgba(0,245,255,.035) 1px,transparent 1px),
    linear-gradient(90deg,rgba(0,245,255,.035) 1px,transparent 1px);
  background-size:44px 44px;
  pointer-events:none;z-index:0;
}

/* ── CORNER DECORATIONS ── */
.corner{position:fixed;width:56px;height:56px;z-index:10;pointer-events:none}
.corner.tl{top:14px;left:14px;border-top:2px solid var(--neon-cyan);border-left:2px solid var(--neon-cyan)}
.corner.tr{top:14px;right:14px;border-top:2px solid var(--neon-cyan);border-right:2px solid var(--neon-cyan)}
.corner.bl{bottom:14px;left:14px;border-bottom:2px solid var(--neon-purple);border-left:2px solid var(--neon-purple)}
.corner.br{bottom:14px;right:14px;border-bottom:2px solid var(--neon-purple);border-right:2px solid var(--neon-purple)}

/* ── WRAPPER ── */
.wrap{
  position:relative;z-index:1;
  max-width:900px;
  margin:0 auto;
  padding:0 24px 80px;
}

/* ══════════════════════════════
   HEADER
══════════════════════════════ */
header{text-align:center;padding:70px 20px 44px}

.avatar-ring{
  width:96px;height:96px;border-radius:50%;
  margin:0 auto 20px;
  background:linear-gradient(135deg,var(--neon-cyan),var(--neon-purple),var(--neon-pink));
  display:flex;align-items:center;justify-content:center;
  font-family:'Orbitron',monospace;
  font-size:30px;font-weight:900;color:#000;
  animation:ring-pulse 2.8s ease-in-out infinite;
}
@keyframes ring-pulse{
  0%{box-shadow:0 0 0 0 rgba(0,245,255,.5)}
  70%{box-shadow:0 0 0 16px rgba(0,245,255,0)}
  100%{box-shadow:0 0 0 0 rgba(0,245,255,0)}
}

.glitch-name{
  font-family:'Orbitron',monospace;
  font-size:clamp(22px,5vw,44px);
  font-weight:900;
  color:#fff;
  letter-spacing:5px;
  text-transform:uppercase;
  position:relative;
  display:inline-block;
  animation:glitch 5s infinite;
}
.glitch-name::before,.glitch-name::after{
  content:attr(data-text);
  position:absolute;top:0;left:0;width:100%;
}
.glitch-name::before{
  color:var(--neon-cyan);
  clip-path:polygon(0 0,100% 0,100% 38%,0 38%);
  animation:gb 5s infinite;
}
.glitch-name::after{
  color:var(--neon-pink);
  clip-path:polygon(0 62%,100% 62%,100% 100%,0 100%);
  animation:ga 5s infinite;
}
@keyframes glitch{0%,88%,100%{transform:translate(0)}90%{transform:translate(-2px,1px)}92%{transform:translate(2px,-1px)}94%{transform:translate(-1px,2px)}}
@keyframes gb{0%,88%,100%{transform:translate(0)}90%{transform:translate(-4px,0)}92%{transform:translate(4px,0)}}
@keyframes ga{0%,88%,100%{transform:translate(0)}90%{transform:translate(4px,0)}92%{transform:translate(-4px,0)}}

.typewriter{
  display:inline-block;
  font-family:'Share Tech Mono',monospace;
  font-size:15px;
  color:var(--neon-cyan);
  letter-spacing:2px;
  margin-top:14px;
  overflow:hidden;
  white-space:nowrap;
  border-right:2px solid var(--neon-cyan);
  animation:typing 3s steps(50,end) .8s both, blink .8s step-end infinite;
  max-width:480px;
}
@keyframes typing{from{width:0}to{width:100%}}
@keyframes blink{50%{border-color:transparent}}

.header-bar{
  width:220px;height:2px;margin:22px auto 0;
  background:linear-gradient(90deg,transparent,var(--neon-cyan),var(--neon-pink),transparent);
  animation:barpulse 2.5s ease-in-out infinite;
}
@keyframes barpulse{0%,100%{opacity:.5;transform:scaleX(.8)}50%{opacity:1;transform:scaleX(1)}}

/* ── STATUS BADGES ── */
.status-row{
  display:flex;gap:10px;justify-content:center;flex-wrap:wrap;
  padding:20px 0 0;
}
.badge{
  background:rgba(0,245,255,.06);
  border:1px solid var(--neon-cyan);
  border-radius:20px;padding:6px 18px;
  font-family:'Share Tech Mono',monospace;
  font-size:12px;color:var(--neon-cyan);letter-spacing:1px;
  transition:all .3s;
  animation:fadeup .6s ease both;
}
.badge:hover{background:rgba(0,245,255,.18);box-shadow:0 0 14px var(--neon-cyan);transform:translateY(-2px)}
.badge.pink{border-color:var(--neon-pink);color:var(--neon-pink);background:rgba(255,0,110,.06)}
.badge.pink:hover{background:rgba(255,0,110,.2);box-shadow:0 0 14px var(--neon-pink)}
.badge.green{border-color:var(--neon-green);color:var(--neon-green);background:rgba(0,255,136,.06)}
.badge.green:hover{background:rgba(0,255,136,.2);box-shadow:0 0 14px var(--neon-green)}
.badge:nth-child(1){animation-delay:.1s}.badge:nth-child(2){animation-delay:.2s}
.badge:nth-child(3){animation-delay:.3s}.badge:nth-child(4){animation-delay:.4s}

/* ══════════════════════════════
   SECTION HEADERS
══════════════════════════════ */
.sec-head{
  font-family:'Orbitron',monospace;
  font-size:clamp(12px,2.5vw,17px);
  font-weight:700;letter-spacing:3px;text-transform:uppercase;
  margin:36px 0 16px;
  display:flex;align-items:center;gap:12px;
  animation:fadeup .6s ease both;
}
.sec-head::before{
  content:'';width:4px;height:22px;border-radius:2px;
  background:currentColor;flex-shrink:0;
  box-shadow:0 0 8px currentColor;
}
.sec-head::after{
  content:'';flex:1;height:1px;
  background:linear-gradient(90deg,currentColor,transparent);
  opacity:.4;
}
.cyan{color:var(--neon-cyan)}
.pink{color:var(--neon-pink)}
.purple{color:var(--neon-purple)}
.green{color:var(--neon-green)}
.gold{color:var(--neon-gold)}

/* ══════════════════════════════
   ABOUT
══════════════════════════════ */
.about-card{
  background:rgba(10,10,26,.85);
  border:1px solid var(--card-border);
  border-left:3px solid var(--neon-cyan);
  border-radius:10px;
  padding:26px 30px;
  animation:fadeup .8s ease .3s both;
  position:relative;overflow:hidden;
}
.about-card::after{
  content:'';
  position:absolute;top:0;right:0;
  width:120px;height:120px;
  background:radial-gradient(circle,rgba(0,245,255,.05) 0%,transparent 70%);
  pointer-events:none;
}
.code-comment{
  font-family:'Share Tech Mono',monospace;
  font-size:12px;color:rgba(0,245,255,.5);
  letter-spacing:1px;margin-bottom:12px;
}
.about-card p{font-size:16px;line-height:1.75;color:#c0c0e0;font-weight:300}
.about-card strong{color:var(--neon-pink);font-weight:600}

/* ══════════════════════════════
   SOCIALS
══════════════════════════════ */
.social-row{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px}
.soc{
  display:flex;align-items:center;gap:9px;
  background:rgba(10,10,26,.9);
  border:1px solid var(--card-border);border-radius:8px;
  padding:11px 18px;text-decoration:none;
  font-family:'Share Tech Mono',monospace;font-size:13px;color:#9090b0;
  transition:all .3s;animation:fadeup .6s ease both;
}
.soc:hover{transform:translateY(-4px);color:#fff}
.soc-dot{width:9px;height:9px;border-radius:50%;flex-shrink:0}
.soc.ig:hover{border-color:#E4405F;box-shadow:0 6px 18px rgba(228,64,95,.35)}
.soc.li:hover{border-color:#0077B5;box-shadow:0 6px 18px rgba(0,119,181,.35)}
.soc.pi:hover{border-color:#E60023;box-shadow:0 6px 18px rgba(230,0,35,.35)}
.soc.em:hover{border-color:#D14836;box-shadow:0 6px 18px rgba(209,72,54,.35)}
.soc:nth-child(1){animation-delay:.1s}.soc:nth-child(2){animation-delay:.2s}
.soc:nth-child(3){animation-delay:.3s}.soc:nth-child(4){animation-delay:.4s}

/* ══════════════════════════════
   TECH SKILLS
══════════════════════════════ */
.cat-legend{
  display:flex;gap:16px;flex-wrap:wrap;margin-bottom:14px;
}
.leg{display:flex;align-items:center;gap:6px}
.leg-dot{width:8px;height:8px;border-radius:2px}
.leg span{font-family:'Share Tech Mono',monospace;font-size:11px;color:#606080}

.skills-grid{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px}
.tag{
  background:rgba(10,10,30,.85);
  border:1px solid rgba(0,245,255,.2);
  border-radius:6px;padding:5px 13px;
  font-family:'Share Tech Mono',monospace;
  font-size:11px;color:#7090b0;letter-spacing:.5px;
  transition:all .3s;cursor:default;
  animation:fadeup .5s ease both;
}
.tag:hover{border-color:var(--neon-cyan);color:var(--neon-cyan);background:rgba(0,245,255,.07);transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,245,255,.18)}
.tag.d{border-color:rgba(180,0,255,.25)}
.tag.d:hover{border-color:var(--neon-purple);color:var(--neon-purple);background:rgba(180,0,255,.07);box-shadow:0 4px 12px rgba(180,0,255,.2)}
.tag.a{border-color:rgba(255,0,110,.25)}
.tag.a:hover{border-color:var(--neon-pink);color:var(--neon-pink);background:rgba(255,0,110,.07);box-shadow:0 4px 12px rgba(255,0,110,.2)}
.tag.t{border-color:rgba(0,255,136,.25)}
.tag.t:hover{border-color:var(--neon-green);color:var(--neon-green);background:rgba(0,255,136,.07);box-shadow:0 4px 12px rgba(0,255,136,.18)}
.tag.b{border-color:rgba(255,215,0,.25)}
.tag.b:hover{border-color:var(--neon-gold);color:var(--neon-gold);background:rgba(255,215,0,.07);box-shadow:0 4px 12px rgba(255,215,0,.18)}

/* ══════════════════════════════
   STATS
══════════════════════════════ */
.stats-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
  gap:14px;margin-bottom:10px;
}
.stat-card{
  background:rgba(10,10,26,.9);
  border:1px solid var(--card-border);border-radius:10px;
  padding:16px;overflow:hidden;position:relative;
  transition:all .3s;animation:fadeup .7s ease both;
}
.stat-card::before{
  content:'';
  position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--neon-cyan),transparent);
  animation:scanline 4s ease-in-out infinite;
}
.stat-card:nth-child(2)::before{background:linear-gradient(90deg,transparent,var(--neon-pink),transparent);animation-delay:.8s}
.stat-card:nth-child(3)::before{background:linear-gradient(90deg,transparent,var(--neon-purple),transparent);animation-delay:1.6s}
@keyframes scanline{0%,100%{opacity:0}50%{opacity:1}}
.stat-card:hover{border-color:rgba(0,245,255,.35);transform:translateY(-5px);box-shadow:0 10px 28px rgba(0,245,255,.1)}
.stat-card img{width:100%;border-radius:5px;display:block}
.stat-card:nth-child(1){animation-delay:.1s}
.stat-card:nth-child(2){animation-delay:.2s}
.stat-card:nth-child(3){animation-delay:.3s}

/* ══════════════════════════════
   SOFT SKILLS
══════════════════════════════ */
.soft-grid{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:10px}
.pill{
  background:rgba(180,0,255,.06);
  border:1px solid rgba(180,0,255,.2);
  border-radius:20px;padding:4px 13px;
  font-size:11px;font-family:'Share Tech Mono',monospace;
  color:#8050a0;letter-spacing:.5px;
  transition:all .3s;cursor:default;
  animation:fadeup .5s ease both;
}
.pill:hover{
  background:rgba(180,0,255,.18);border-color:var(--neon-purple);
  color:#d080ff;transform:scale(1.06);box-shadow:0 4px 12px rgba(180,0,255,.2);
}

/* ══════════════════════════════
   QUOTE
══════════════════════════════ */
.quote-wrap{
  border:1px solid var(--card-border);border-radius:10px;
  overflow:hidden;animation:fadeup .7s ease both;
}
.quote-wrap img{width:100%;display:block}

/* ══════════════════════════════
   FOOTER
══════════════════════════════ */
footer{text-align:center;padding:30px 0 0}
footer img{border-radius:6px}
.footer-txt{
  font-family:'Share Tech Mono',monospace;
  font-size:12px;color:rgba(0,245,255,.35);
  margin-top:16px;letter-spacing:2px;
}

/* ── DIVIDER ── */
.divider{
  height:1px;margin:30px 0;
  background:linear-gradient(90deg,transparent,rgba(0,245,255,.25),rgba(180,0,255,.25),transparent);
}

/* ── SHARED ANIMATION ── */
@keyframes fadeup{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}

/* ══════════════════════════════
   FLOATING PARTICLES
══════════════════════════════ */
.particles{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden}
.p{
  position:absolute;border-radius:50%;
  animation:float linear infinite;
  opacity:0;
}
@keyframes float{
  0%{transform:translateY(100vh) rotate(0deg);opacity:0}
  10%{opacity:.6}
  90%{opacity:.3}
  100%{transform:translateY(-10vh) rotate(720deg);opacity:0}
}

/* ══════════════════════════════
   SCROLL REVEAL
══════════════════════════════ */
.reveal{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}
.reveal.visible{opacity:1;transform:none}

/* ══════════════════════════════
   RESPONSIVE
══════════════════════════════ */
@media(max-width:600px){
  .glitch-name{font-size:22px;letter-spacing:2px}
  .typewriter{font-size:12px}
  .stats-grid{grid-template-columns:1fr}
  .about-card{padding:18px 20px}
  header{padding:50px 10px 30px}
}
</style>
</head>
<body>

<div class="grid-bg"></div>
<div class="particles" id="particles"></div>
<div class="corner tl"></div>
<div class="corner tr"></div>
<div class="corner bl"></div>
<div class="corner br"></div>

<div class="wrap">

  <!-- ══ HEADER ══ -->
  <header>
    <div class="avatar-ring">GS</div>
    <div class="glitch-name" data-text="GEERSHATI SAXENA">GEERSHATI SAXENA</div>
    <br>
    <div class="typewriter">&gt;_ BCA Student · Data Science · AI Enthusiast</div>
    <div class="header-bar"></div>
    <div class="status-row">
      <span class="badge">◈ BCA Undergraduate</span>
      <span class="badge pink">◈ Data Science</span>
      <span class="badge green">◈ AI / ML Explorer</span>
      <span class="badge">◈ Open to Opportunities</span>
    </div>
  </header>

  <!-- ══ ABOUT ══ -->
  <div class="reveal">
    <div class="sec-head cyan">About Me</div>
    <div class="about-card">
      <div class="code-comment">// init: about_me.py</div>
      <p>
        Hello! I'm a <strong>dynamic and forward-thinking</strong> student pursuing a
        <strong>Bachelor of Computer Application (B.C.A)</strong> with a keen interest
        in the fascinating realms of <strong>Data Science</strong> and
        <strong>Artificial Intelligence</strong>. I thrive at the intersection of
        analytical thinking and creative problem-solving — turning raw data into
        actionable insights and building AI-powered solutions.
      </p>
    </div>
  </div>

  <div class="divider"></div>

  <!-- ══ SOCIALS ══ -->
  <div class="reveal">
    <div class="sec-head cyan">Socials</div>
    <div class="social-row">
      <a class="soc ig" href="https://instagram.com/geershati_saxena" target="_blank">
        <span class="soc-dot" style="background:#E4405F"></span>Instagram
      </a>
      <a class="soc li" href="https://linkedin.com/in/geershati-saxena" target="_blank">
        <span class="soc-dot" style="background:#0077B5"></span>LinkedIn
      </a>
      <a class="soc pi" href="https://pinterest.com/geershati" target="_blank">
        <span class="soc-dot" style="background:#E60023"></span>Pinterest
      </a>
      <a class="soc em" href="mailto:geershatisaxena110@gmail.com">
        <span class="soc-dot" style="background:#D14836"></span>Email
      </a>
    </div>
  </div>

  <div class="divider"></div>

  <!-- ══ TECH STACK ══ -->
  <div class="reveal">
    <div class="sec-head cyan">Tech Stack</div>
    <div class="cat-legend">
      <div class="leg"><div class="leg-dot" style="background:rgba(0,245,255,.8)"></div><span>Web / Core</span></div>
      <div class="leg"><div class="leg-dot" style="background:rgba(180,0,255,.8)"></div><span>Data Science</span></div>
      <div class="leg"><div class="leg-dot" style="background:rgba(255,0,110,.8)"></div><span>AI Tools</span></div>
      <div class="leg"><div class="leg-dot" style="background:rgba(0,255,136,.8)"></div><span>Dev Tools</span></div>
      <div class="leg"><div class="leg-dot" style="background:rgba(255,215,0,.8)"></div><span>Deploy / BI</span></div>
    </div>
    <div class="skills-grid">
      <!-- Web/Core — cyan -->
      <span class="tag">HTML5</span>
      <span class="tag">CSS3</span>
      <span class="tag">JavaScript</span>
      <span class="tag">Animate.css</span>
      <span class="tag">SQL</span>
      <span class="tag">MySQL</span>
      <span class="tag">Python</span>
      <span class="tag">Python Turtle</span>
      <!-- Data Science — purple -->
      <span class="tag d">Pandas</span>
      <span class="tag d">NumPy</span>
      <span class="tag d">Matplotlib</span>
      <span class="tag d">Seaborn</span>
      <span class="tag d">Plotly</span>
      <span class="tag d">Scikit-learn</span>
      <span class="tag d">Data Cleaning</span>
      <span class="tag d">Data Visualization</span>
      <span class="tag d">Exploratory Data Analysis</span>
      <span class="tag d">Statistical Analysis</span>
      <span class="tag d">IBM Cognos Analytics</span>
      <span class="tag d">IBM SPSS Modeler</span>
      <!-- AI — pink -->
      <span class="tag a">ChatGPT</span>
      <span class="tag a">GPT-4</span>
      <span class="tag a">DALL·E</span>
      <span class="tag a">Google Bard</span>
      <span class="tag a">Anthropic Claude</span>
      <span class="tag a">GitHub Copilot</span>
      <span class="tag a">DeepSeek</span>
      <!-- Dev Tools — green -->
      <span class="tag t">Jupyter</span>
      <span class="tag t">Google Colab</span>
      <span class="tag t">Anaconda</span>
      <span class="tag t">Miniconda</span>
      <span class="tag t">VS Code</span>
      <span class="tag t">Streamlit</span>
      <!-- Deploy/BI — gold -->
      <span class="tag b">Vercel</span>
      <span class="tag b">Render</span>
      <span class="tag b">Power BI</span>
      <span class="tag b">Excel</span>
      <span class="tag b">Google Sheets</span>
      <span class="tag b">PowerPoint</span>
      <span class="tag b">Business Intelligence</span>
      <span class="tag b">Data-Driven Decisions</span>
    </div>
  </div>

  <div class="divider"></div>

  <!-- ══ GITHUB STATS ══ -->
  <div class="reveal">
    <div class="sec-head cyan">GitHub Stats</div>
    <div class="stats-grid">
      <div class="stat-card">
        <img src="https://github-readme-stats.vercel.app/api?username=geershatisaxena&theme=dark&hide_border=true&include_all_commits=true&count_private=true&bg_color=0a0a1a&title_color=00f5ff&text_color=c0c0e0&icon_color=b400ff" alt="GitHub Stats" loading="lazy">
      </div>
      <div class="stat-card">
        <img src="https://nirzak-streak-stats.vercel.app/?user=geershatisaxena&theme=dark&hide_border=true&background=0a0a1a&ring=00f5ff&fire=ff006e&currStreakLabel=00f5ff" alt="Streak Stats" loading="lazy">
      </div>
      <div class="stat-card">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=geershatisaxena&theme=dark&hide_border=true&include_all_commits=true&count_private=true&layout=compact&bg_color=0a0a1a&title_color=b400ff&text_color=c0c0e0" alt="Top Languages" loading="lazy">
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- ══ SOFT SKILLS ══ -->
  <div class="reveal">
    <div class="sec-head purple">Soft Skills</div>
    <div class="soft-grid" id="softGrid"></div>
  </div>

  <div class="divider"></div>

  <!-- ══ QUOTE ══ -->
  <div class="reveal">
    <div class="sec-head pink">Dev Quote</div>
    <div class="quote-wrap">
      <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" alt="Dev Quote" loading="lazy">
    </div>
  </div>

  <!-- ══ FOOTER ══ -->
  <footer>
    <a href="https://visitcount.itsvg.in" target="_blank">
      <img src="https://visitcount.itsvg.in/api?id=geershatisaxena&icon=0&color=6" alt="Visitor Count">
    </a>
    <div class="footer-txt">// built with passion · data · and a lot of caffeine ☕</div>
  </footer>

</div><!-- /wrap -->

<script>
/* ── Floating Particles ── */
(function(){
  const container=document.getElementById('particles');
  const colors=['#00f5ff','#ff006e','#b400ff','#00ff88','#ffd700'];
  for(let i=0;i<28;i++){
    const p=document.createElement('div');
    p.className='p';
    const size=Math.random()*4+2;
    const color=colors[Math.floor(Math.random()*colors.length)];
    p.style.cssText=`
      left:${Math.random()*100}%;
      width:${size}px;height:${size}px;
      background:${color};
      box-shadow:0 0 ${size*3}px ${color};
      animation-duration:${Math.random()*18+12}s;
      animation-delay:${Math.random()*12}s;
    `;
    container.appendChild(p);
  }
})();

/* ── Soft Skills ── */
(function(){
  const skills=[
    "Communication","Teamwork","Leadership","Problem Solving","Critical Thinking",
    "Adaptability","Creativity","Time Management","Work Ethic","Attention to Detail",
    "Empathy","Conflict Resolution","Active Listening","Public Speaking","Negotiation",
    "Decision Making","Positive Attitude","Self-Motivation","Responsibility","Collaboration",
    "Emotional Intelligence","Growth Mindset","Initiative","Flexibility","Stress Management",
    "Interpersonal Skills","Dependability","Confidence","Integrity","Curiosity",
    "Goal Orientation","Perseverance","Learning Agility","Open-mindedness","Accountability",
    "Respectfulness","Professionalism","Self-awareness","Multitasking","Resilience",
    "Self-Discipline","Mentoring","Learning from Feedback","Ownership","Remote Collaboration",
    "Cross-functional Communication","Agile Mindset","Strategic Thinking","Proactive Attitude",
    "Inclusivity","Tolerance","Diplomacy","Work-Life Balance","Ethical Mindset",
    "Organizational Skills","Openness to Criticism"
  ];
  const grid=document.getElementById('softGrid');
  skills.forEach((s,i)=>{
    const el=document.createElement('span');
    el.className='pill';
    el.textContent=s;
    el.style.animationDelay=(0.04+i*0.012)+'s';
    grid.appendChild(el);
  });
})();

/* ── Scroll Reveal ── */
(function(){
  const els=document.querySelectorAll('.reveal');
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('visible');
        obs.unobserve(e.target);
      }
    });
  },{threshold:.12});
  els.forEach(el=>obs.observe(el));
})();

/* ── Stagger skill tag animations on scroll ── */
(function(){
  const grids=document.querySelectorAll('.skills-grid,.soft-grid');
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.querySelectorAll('.tag,.pill').forEach((el,i)=>{
          el.style.animationDelay=(i*0.018)+'s';
          el.style.animationPlayState='running';
        });
      }
    });
  },{threshold:.05});
  grids.forEach(g=>obs.observe(g));
})();
</script>
</body>
</html>
