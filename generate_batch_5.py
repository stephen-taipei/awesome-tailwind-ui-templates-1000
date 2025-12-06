import os
import subprocess
import time

# Base HTML Template
BASE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{description}">
  <title>{id}: {title} | Tailwind UI Templates</title>

  <!-- Tailwind CSS v4 via stephen.taipei CDN -->
  <script src="https://stephen.taipei/tailwindcss-browser.js"></script>

  <!-- Custom Theme Variables -->
  <style type="text/tailwindcss">
    @theme {{
      --color-primary-500: oklch(0.55 0.20 250);
      --color-primary-600: oklch(0.48 0.22 250);
      --color-secondary-600: oklch(0.45 0.02 250);
      --color-secondary-700: oklch(0.37 0.02 250);
    }}
  </style>
</head>
<body class="bg-slate-50">

  <!-- ============================================
       {id}: {title}
       {description}
       ============================================ -->

  {content}

</body>
</html>
"""

# Template Definitions
TEMPLATES = [
    # Hero Sections 013-050
    {
        "id": "hero-013",
        "title": "Looping Video Hero",
        "description": "Seamless looping background video",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden">
    <video autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-waves-in-the-water-1164-large.mp4" type="video/mp4">
    </video>
    <div class="absolute inset-0 bg-black/30"></div>
    <div class="relative z-10 flex h-full items-center justify-center text-center text-white">
      <h1 class="text-5xl font-bold">Seamless Loops</h1>
    </div>
  </div>"""
    },
    {
        "id": "hero-014",
        "title": "Video with Text Overlay",
        "description": "Video with prominent text",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden">
    <video autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-stars-in-space-1610-large.mp4" type="video/mp4">
    </video>
    <div class="absolute inset-0 bg-black/50"></div>
    <div class="relative z-10 flex h-full items-center justify-center">
      <div class="z-10 relative text-center text-white max-w-4xl px-4">
        <h1 class="text-6xl font-extrabold tracking-tight">The Future is Now</h1>
        <p class="mt-4 text-xl text-slate-200">Experience the next generation of web design.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-015",
        "title": "Video Hero with CTA",
        "description": "Video background with call-to-action",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden">
    <video autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-forest-stream-in-the-sunlight-529-large.mp4" type="video/mp4">
    </video>
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="relative z-10 flex h-full flex-col items-center justify-center text-white">
      <h1 class="text-5xl font-bold mb-8">Explore Nature</h1>
      <div class="flex gap-4">
        <a href="#" class="px-8 py-4 bg-primary-600 rounded-lg font-bold hover:bg-primary-500 transition">Get Started</a>
        <a href="#" class="px-8 py-4 bg-white/20 backdrop-blur rounded-lg font-bold hover:bg-white/30 transition">Learn More</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-016",
        "title": "Split Video/Content Hero",
        "description": "Side-by-side video and content",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen">
    <div class="flex items-center justify-center bg-white p-12">
      <div class="max-w-lg">
        <h1 class="text-4xl font-bold text-slate-900">Modern Split Layout</h1>
        <p class="mt-4 text-lg text-slate-600">Combine rich media with compelling copy in this split screen design.</p>
        <button class="mt-8 px-6 py-3 bg-slate-900 text-white rounded-md">Action</button>
      </div>
    </div>
    <div class="relative h-64 lg:h-full overflow-hidden">
      <video autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-abstract-video-of-ink-in-water-2444-large.mp4" type="video/mp4">
      </video>
    </div>
  </div>"""
    },
    {
        "id": "hero-017",
        "title": "Video with Gradient Overlay",
        "description": "Video with gradient fade",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden">
    <video autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-sky-with-stars-at-night-1609-large.mp4" type="video/mp4">
    </video>
    <div class="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-transparent"></div>
    <div class="relative z-10 flex h-full items-center px-12">
      <div class="max-w-2xl text-white">
        <h1 class="text-5xl font-bold">Gradient Fade</h1>
        <p class="mt-4 text-xl text-primary-100">Seamlessly blend video with your brand colors.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-018",
        "title": "Video Carousel Hero",
        "description": "Multiple video backgrounds",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden bg-black">
    <div class="absolute inset-0 flex items-center justify-center text-white z-20 pointer-events-none">
      <h1 class="text-4xl font-bold">Video Carousel (Placeholder)</h1>
    </div>
    <!-- Placeholder for carousel logic -->
    <video autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover opacity-50">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-white-sand-beach-background-1564-large.mp4" type="video/mp4">
    </video>
  </div>"""
    },
    {
        "id": "hero-019",
        "title": "Video with Sound Toggle",
        "description": "Video with audio control",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden">
    <video id="hero-video" autoplay loop muted playsinline class="absolute inset-0 h-full w-full object-cover">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-waves-coming-to-the-beach-5016-large.mp4" type="video/mp4">
    </video>
    <button onclick="document.getElementById('hero-video').muted = !document.getElementById('hero-video').muted" class="absolute bottom-8 right-8 z-20 p-4 bg-white/20 backdrop-blur rounded-full text-white hover:bg-white/30">
      Sound Toggle
    </button>
  </div>"""
    },
    {
        "id": "hero-020",
        "title": "YouTube/Vimeo Embed Hero",
        "description": "Embedded video service hero",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen w-full overflow-hidden flex items-center justify-center bg-black">
    <div class="aspect-video w-full max-w-6xl">
      <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1&controls=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>"""
    },
    {
        "id": "hero-021",
        "title": "Linear Gradient Hero",
        "description": "Simple linear gradient background",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-r from-blue-600 to-purple-600 text-white">
    <h1 class="text-6xl font-bold">Linear Gradient</h1>
  </div>"""
    },
    {
        "id": "hero-022",
        "title": "Radial Gradient Hero",
        "description": "Radial gradient background",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-gray-700 via-gray-900 to-black text-white">
    <h1 class="text-6xl font-bold">Radial Gradient</h1>
  </div>"""
    },
    {
        "id": "hero-023",
        "title": "Multi-Color Gradient Hero",
        "description": "Complex multi-stop gradient",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-br from-red-500 via-yellow-500 to-blue-500 text-white">
    <h1 class="text-6xl font-bold">Multi-Color</h1>
  </div>"""
    },
    {
        "id": "hero-024",
        "title": "Animated Gradient Hero",
        "description": "Moving/shifting gradient",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 animate-pulse text-white">
    <h1 class="text-6xl font-bold">Animated Gradient</h1>
  </div>"""
    },
    {
        "id": "hero-025",
        "title": "Gradient with Pattern",
        "description": "Gradient + decorative pattern",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-r from-indigo-500 to-purple-500 relative">
    <div class="absolute inset-0 opacity-10" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 20px 20px;"></div>
    <h1 class="text-6xl font-bold text-white relative z-10">Patterned Gradient</h1>
  </div>"""
    },
    {
        "id": "hero-026",
        "title": "Mesh Gradient Hero",
        "description": "Mesh/blob gradient effect",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-slate-900 relative overflow-hidden">
    <div class="absolute top-0 left-0 w-96 h-96 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-blob"></div>
    <div class="absolute top-0 right-0 w-96 h-96 bg-yellow-500 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-blob animation-delay-2000"></div>
    <div class="absolute -bottom-8 left-20 w-96 h-96 bg-pink-500 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-blob animation-delay-4000"></div>
    <h1 class="text-6xl font-bold text-white relative z-10">Mesh Gradient</h1>
  </div>"""
    },
    {
        "id": "hero-027",
        "title": "Gradient with Noise Texture",
        "description": "Gradient + noise overlay",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-tr from-slate-800 to-slate-900 relative">
    <div class="absolute inset-0 opacity-20" style="filter: contrast(320%) brightness(100%); background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MDAiIGhlaWdodD0iNTAwIj48ZmlsdGVyIGlkPSJub2lzZSI+PHZlVHVyYnVsZW5jZSB0eXBlPSJmcmFjdGFsTm9pc2UiIGJhc2VGcmVxdWVuY3k9IjAuNjUiIG51bU9jdGF2ZXM9IjMiIHN0aXRjaFRpbGVzPSJzdGl0Y2giLz48L2ZpbHRlcj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWx0ZXI9InVybCgjbm9pc2UpIiBvcGFjaXR5PSIwLjUiLz48L3N2Zz4=');"></div>
    <h1 class="text-6xl font-bold text-white relative z-10">Noise Texture</h1>
  </div>"""
    },
    {
        "id": "hero-028",
        "title": "Dark Gradient Hero",
        "description": "Dark color gradient",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-b from-slate-900 to-black text-white">
    <h1 class="text-6xl font-bold">Dark Mode</h1>
  </div>"""
    },
    {
        "id": "hero-029",
        "title": "Pastel Gradient Hero",
        "description": "Soft pastel gradient",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-gradient-to-r from-pink-100 via-purple-100 to-cyan-100 text-slate-800">
    <h1 class="text-6xl font-bold">Pastel Dreams</h1>
  </div>"""
    },
    {
        "id": "hero-030",
        "title": "Gradient Border Hero",
        "description": "Hero with gradient border accent",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full flex items-center justify-center bg-white">
    <div class="p-1 rounded-2xl bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500">
      <div class="bg-white p-12 rounded-xl">
        <h1 class="text-5xl font-bold text-slate-900">Gradient Border</h1>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-031",
        "title": "Image Left, Content Right",
        "description": "Classic split layout hero",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen">
    <div class="h-64 lg:h-full">
      <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=2000&q=80" class="w-full h-full object-cover" alt="Team">
    </div>
    <div class="flex items-center justify-center p-12 bg-white">
      <div class="max-w-lg">
        <h1 class="text-4xl font-bold">Split Layout</h1>
        <p class="mt-4 text-slate-600">Image on the left, content on the right.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-032",
        "title": "Content Left, Image Right",
        "description": "Reversed split layout",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen">
    <div class="flex items-center justify-center p-12 bg-white order-2 lg:order-1">
      <div class="max-w-lg">
        <h1 class="text-4xl font-bold">Reversed Split</h1>
        <p class="mt-4 text-slate-600">Content on the left, image on the right.</p>
      </div>
    </div>
    <div class="h-64 lg:h-full order-1 lg:order-2">
      <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=2000&q=80" class="w-full h-full object-cover" alt="Meeting">
    </div>
  </div>"""
    },
    {
        "id": "hero-033",
        "title": "Split with Angled Divider",
        "description": "Diagonal split between sections",
        "dir": "templates/02-hero-sections",
        "content": """<div class="relative h-screen bg-white overflow-hidden">
    <div class="absolute top-0 right-0 w-2/3 h-full bg-slate-900" style="clip-path: polygon(20% 0, 100% 0, 100% 100%, 0% 100%);"></div>
    <div class="relative z-10 h-full flex items-center px-12">
      <h1 class="text-6xl font-bold text-slate-900 mix-blend-difference text-white">Angled Split</h1>
    </div>
  </div>"""
    },
    {
        "id": "hero-034",
        "title": "Split with Overlapping Image",
        "description": "Image overlaps into content area",
        "dir": "templates/02-hero-sections",
        "content": """<div class="min-h-screen flex items-center bg-slate-50">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center px-4">
      <div class="bg-white p-12 shadow-xl rounded-lg z-10">
        <h1 class="text-4xl font-bold">Overlap</h1>
        <p class="mt-4 text-slate-600">Content box overlapping the image.</p>
      </div>
      <div class="-ml-12 lg:-ml-24">
        <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1000&q=80" class="rounded-lg shadow-2xl" alt="Working">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-035",
        "title": "Split with Background Color",
        "description": "Different background colors per side",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 md:grid-cols-2 h-screen">
    <div class="bg-primary-600 flex items-center justify-center text-white p-12">
      <h1 class="text-5xl font-bold">Primary</h1>
    </div>
    <div class="bg-slate-900 flex items-center justify-center text-white p-12">
      <h1 class="text-5xl font-bold">Dark</h1>
    </div>
  </div>"""
    },
    {
        "id": "hero-036",
        "title": "Split with Stats",
        "description": "Split layout with statistics",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen bg-white">
    <div class="flex flex-col justify-center p-12">
      <h1 class="text-4xl font-bold">Our Impact</h1>
      <p class="mt-4 text-slate-600">We deliver results.</p>
    </div>
    <div class="bg-slate-50 flex items-center justify-center p-12">
      <div class="grid grid-cols-2 gap-8">
        <div class="text-center"><div class="text-4xl font-bold text-primary-600">10k+</div><div class="text-slate-500">Users</div></div>
        <div class="text-center"><div class="text-4xl font-bold text-primary-600">99%</div><div class="text-slate-500">Uptime</div></div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-037",
        "title": "Split with Form",
        "description": "Content + form split",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen bg-white">
    <div class="flex items-center justify-center p-12 bg-primary-600 text-white">
      <div>
        <h1 class="text-4xl font-bold">Join Us</h1>
        <p class="mt-4">Sign up today.</p>
      </div>
    </div>
    <div class="flex items-center justify-center p-12">
      <form class="w-full max-w-md space-y-4">
        <input type="email" placeholder="Email" class="w-full p-3 border rounded">
        <button class="w-full p-3 bg-primary-600 text-white rounded">Sign Up</button>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "hero-038",
        "title": "Split with Video",
        "description": "Content + video split",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen">
    <div class="flex items-center justify-center p-12 bg-white">
      <h1 class="text-4xl font-bold">Watch This</h1>
    </div>
    <div class="bg-black flex items-center justify-center">
      <div class="aspect-video w-full">
        <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0"></iframe>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "hero-039",
        "title": "Three Column Split",
        "description": "Triple column hero layout",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 md:grid-cols-3 h-screen text-white">
    <div class="bg-primary-600 flex items-center justify-center p-8"><h2 class="text-3xl font-bold">Design</h2></div>
    <div class="bg-secondary-600 flex items-center justify-center p-8"><h2 class="text-3xl font-bold">Build</h2></div>
    <div class="bg-slate-900 flex items-center justify-center p-8"><h2 class="text-3xl font-bold">Launch</h2></div>
  </div>"""
    },
    {
        "id": "hero-040",
        "title": "Split with App Mockup",
        "description": "Content + device mockup",
        "dir": "templates/02-hero-sections",
        "content": """<div class="grid grid-cols-1 lg:grid-cols-2 h-screen bg-white overflow-hidden">
    <div class="flex items-center justify-center p-12">
      <div class="max-w-md">
        <h1 class="text-4xl font-bold">Mobile First</h1>
        <p class="mt-4 text-slate-600">Download our app.</p>
      </div>
    </div>
    <div class="bg-slate-100 flex items-end justify-center pt-12">
      <div class="w-64 h-96 bg-black rounded-t-3xl border-8 border-black border-b-0 shadow-2xl"></div>
    </div>
  </div>"""
    },
    {
        "id": "hero-041",
        "title": "Particle Animation Hero",
        "description": "Animated particles background",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-slate-900 flex items-center justify-center relative">
    <div class="absolute inset-0 opacity-50">
      <!-- Placeholder for particles.js or canvas -->
      <div class="w-full h-full bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9InfffIiAvPjwvc3ZnPg==')]"></div>
    </div>
    <h1 class="text-6xl font-bold text-white z-10">Particles</h1>
  </div>"""
    },
    {
        "id": "hero-042",
        "title": "Typing Animation Hero",
        "description": "Typewriter text effect",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-white flex items-center justify-center">
    <h1 class="text-6xl font-bold text-slate-900">We build <span class="text-primary-600 border-r-4 border-primary-600 animate-pulse">Websites</span></h1>
  </div>"""
    },
    {
        "id": "hero-043",
        "title": "Scroll-Triggered Hero",
        "description": "Animations on scroll",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-slate-50 flex flex-col items-center justify-center">
    <h1 class="text-6xl font-bold text-slate-900 animate-bounce">Scroll Down</h1>
    <div class="mt-8 text-4xl">⬇️</div>
  </div>"""
    },
    {
        "id": "hero-044",
        "title": "3D Tilt Effect Hero",
        "description": "Mouse-following 3D tilt",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-slate-900 flex items-center justify-center perspective-1000">
    <div class="bg-gradient-to-br from-primary-500 to-secondary-500 p-12 rounded-2xl shadow-2xl transform rotate-y-12 rotate-x-12 hover:rotate-0 transition-transform duration-500">
      <h1 class="text-6xl font-bold text-white">3D Tilt</h1>
    </div>
  </div>"""
    },
    {
        "id": "hero-045",
        "title": "Floating Elements Hero",
        "description": "Floating animated decorations",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-white flex items-center justify-center relative overflow-hidden">
    <div class="absolute top-20 left-20 w-20 h-20 bg-primary-200 rounded-full animate-bounce"></div>
    <div class="absolute bottom-20 right-20 w-32 h-32 bg-secondary-200 rounded-full animate-pulse"></div>
    <h1 class="text-6xl font-bold text-slate-900 z-10">Floating Elements</h1>
  </div>"""
    },
    {
        "id": "hero-046",
        "title": "Counter Animation Hero",
        "description": "Animated number counters",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-slate-900 flex items-center justify-center text-white">
    <div class="text-center">
      <div class="text-8xl font-bold text-primary-500">1,234</div>
      <div class="text-2xl mt-4">Projects Completed</div>
    </div>
  </div>"""
    },
    {
        "id": "hero-047",
        "title": "Morphing Shape Hero",
        "description": "SVG shape morphing animation",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-white flex items-center justify-center relative overflow-hidden">
    <div class="absolute w-96 h-96 bg-primary-300 rounded-[30%_70%_70%_30%_/_30%_30%_70%_70%] animate-[spin_10s_linear_infinite]"></div>
    <h1 class="text-6xl font-bold text-slate-900 z-10">Morphing</h1>
  </div>"""
    },
    {
        "id": "hero-048",
        "title": "Glitch Effect Hero",
        "description": "Glitch/distortion text effect",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-black flex items-center justify-center">
    <h1 class="text-8xl font-bold text-white relative">
      <span class="absolute top-0 left-0 -ml-1 text-red-500 opacity-70 animate-pulse">GLITCH</span>
      <span class="absolute top-0 left-0 ml-1 text-blue-500 opacity-70 animate-pulse animation-delay-75">GLITCH</span>
      GLITCH
    </h1>
  </div>"""
    },
    {
        "id": "hero-049",
        "title": "Parallax Layers Hero",
        "description": "Multi-layer parallax scrolling",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-slate-100 overflow-y-auto perspective-1">
    <div class="h-screen flex items-center justify-center transform translate-z-0">
      <h1 class="text-6xl font-bold">Parallax</h1>
    </div>
    <div class="absolute top-0 left-0 w-full h-full transform translate-z-[-1px] scale-2 bg-slate-300 -z-10"></div>
  </div>"""
    },
    {
        "id": "hero-050",
        "title": "Interactive Hero",
        "description": "User interaction responsive hero",
        "dir": "templates/02-hero-sections",
        "content": """<div class="h-screen w-full bg-white flex items-center justify-center">
    <button class="px-12 py-6 text-2xl font-bold text-white bg-primary-600 rounded-full hover:scale-110 active:scale-95 transition-transform shadow-xl hover:shadow-2xl">
      Click Me
    </button>
  </div>"""
    },
    # Features 001-012
    {
        "id": "feat-001",
        "title": "3-Column Feature Grid",
        "description": "Standard three feature highlight",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
        <div class="text-center">
          <div class="w-12 h-12 bg-primary-100 text-primary-600 rounded-lg flex items-center justify-center mx-auto mb-4">1</div>
          <h3 class="text-xl font-bold">Feature One</h3>
          <p class="mt-2 text-slate-600">Description for feature one.</p>
        </div>
        <div class="text-center">
          <div class="w-12 h-12 bg-primary-100 text-primary-600 rounded-lg flex items-center justify-center mx-auto mb-4">2</div>
          <h3 class="text-xl font-bold">Feature Two</h3>
          <p class="mt-2 text-slate-600">Description for feature two.</p>
        </div>
        <div class="text-center">
          <div class="w-12 h-12 bg-primary-100 text-primary-600 rounded-lg flex items-center justify-center mx-auto mb-4">3</div>
          <h3 class="text-xl font-bold">Feature Three</h3>
          <p class="mt-2 text-slate-600">Description for feature three.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-002",
        "title": "4-Column Feature Grid",
        "description": "Four feature display",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="font-bold">Feature A</h3>
          <p class="text-sm text-slate-500 mt-2">Details here.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="font-bold">Feature B</h3>
          <p class="text-sm text-slate-500 mt-2">Details here.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="font-bold">Feature C</h3>
          <p class="text-sm text-slate-500 mt-2">Details here.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="font-bold">Feature D</h3>
          <p class="text-sm text-slate-500 mt-2">Details here.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-003",
        "title": "6-Column Feature Grid",
        "description": "Many small features",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6 text-center">
        <div class="p-4 border rounded">Item 1</div>
        <div class="p-4 border rounded">Item 2</div>
        <div class="p-4 border rounded">Item 3</div>
        <div class="p-4 border rounded">Item 4</div>
        <div class="p-4 border rounded">Item 5</div>
        <div class="p-4 border rounded">Item 6</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-004",
        "title": "Feature Grid with Images",
        "description": "Image-based feature grid",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="rounded-lg overflow-hidden shadow-lg">
        <img src="https://via.placeholder.com/400x200" class="w-full h-48 object-cover">
        <div class="p-6"><h3 class="font-bold">Visual Feature</h3></div>
      </div>
      <div class="rounded-lg overflow-hidden shadow-lg">
        <img src="https://via.placeholder.com/400x200" class="w-full h-48 object-cover">
        <div class="p-6"><h3 class="font-bold">Visual Feature</h3></div>
      </div>
      <div class="rounded-lg overflow-hidden shadow-lg">
        <img src="https://via.placeholder.com/400x200" class="w-full h-48 object-cover">
        <div class="p-6"><h3 class="font-bold">Visual Feature</h3></div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-005",
        "title": "Feature Grid with Numbers",
        "description": "Numbered feature steps",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="flex gap-4">
        <div class="w-10 h-10 rounded-full bg-primary-600 text-white flex items-center justify-center font-bold shrink-0">1</div>
        <div><h3 class="font-bold">Step One</h3><p class="text-slate-600">Start here.</p></div>
      </div>
      <div class="flex gap-4">
        <div class="w-10 h-10 rounded-full bg-primary-600 text-white flex items-center justify-center font-bold shrink-0">2</div>
        <div><h3 class="font-bold">Step Two</h3><p class="text-slate-600">Then do this.</p></div>
      </div>
      <div class="flex gap-4">
        <div class="w-10 h-10 rounded-full bg-primary-600 text-white flex items-center justify-center font-bold shrink-0">3</div>
        <div><h3 class="font-bold">Step Three</h3><p class="text-slate-600">Finish here.</p></div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-006",
        "title": "Feature Grid Centered",
        "description": "Centered text feature grid",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
      <div><h3 class="text-xl font-bold">Centered</h3><p class="mt-2">All content aligned to center.</p></div>
      <div><h3 class="text-xl font-bold">Balanced</h3><p class="mt-2">Symmetrical layout.</p></div>
      <div><h3 class="text-xl font-bold">Focused</h3><p class="mt-2">Easy to read.</p></div>
    </div>
  </div>"""
    },
    {
        "id": "feat-007",
        "title": "Feature Grid with Background",
        "description": "Colored background feature grid",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-primary-50 p-8 rounded-xl"><h3 class="font-bold text-primary-900">Tinted</h3></div>
      <div class="bg-secondary-50 p-8 rounded-xl"><h3 class="font-bold text-secondary-900">Tinted</h3></div>
      <div class="bg-slate-50 p-8 rounded-xl"><h3 class="font-bold text-slate-900">Tinted</h3></div>
    </div>
  </div>"""
    },
    {
        "id": "feat-008",
        "title": "Feature Grid with Hover Effects",
        "description": "Interactive hover states",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-100">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow transition hover:scale-105 hover:shadow-xl cursor-pointer">
        <h3 class="font-bold">Hover Me</h3>
      </div>
      <div class="bg-white p-8 rounded-xl shadow transition hover:scale-105 hover:shadow-xl cursor-pointer">
        <h3 class="font-bold">Hover Me</h3>
      </div>
      <div class="bg-white p-8 rounded-xl shadow transition hover:scale-105 hover:shadow-xl cursor-pointer">
        <h3 class="font-bold">Hover Me</h3>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-009",
        "title": "Masonry Feature Grid",
        "description": "Pinterest-style masonry layout",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 columns-1 md:columns-3 gap-8 space-y-8">
      <div class="bg-slate-100 p-6 rounded-lg break-inside-avoid h-64">Item 1</div>
      <div class="bg-slate-100 p-6 rounded-lg break-inside-avoid h-32">Item 2</div>
      <div class="bg-slate-100 p-6 rounded-lg break-inside-avoid h-48">Item 3</div>
      <div class="bg-slate-100 p-6 rounded-lg break-inside-avoid h-56">Item 4</div>
      <div class="bg-slate-100 p-6 rounded-lg break-inside-avoid h-40">Item 5</div>
    </div>
  </div>"""
    },
    {
        "id": "feat-010",
        "title": "Bento Grid Features",
        "description": "Bento box style varied sizes",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-4 grid-rows-2 gap-4 h-[600px]">
      <div class="bg-white p-6 rounded-2xl shadow md:col-span-2 md:row-span-2">Big Feature</div>
      <div class="bg-white p-6 rounded-2xl shadow">Small</div>
      <div class="bg-white p-6 rounded-2xl shadow">Small</div>
      <div class="bg-white p-6 rounded-2xl shadow md:col-span-2">Wide Feature</div>
    </div>
  </div>"""
    },
    {
        "id": "feat-011",
        "title": "Simple Feature List",
        "description": "Vertical feature list",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6 space-y-8">
      <div class="p-6 border rounded-lg">
        <h3 class="text-xl font-bold">Feature One</h3>
        <p class="text-slate-600">Description goes here.</p>
      </div>
      <div class="p-6 border rounded-lg">
        <h3 class="text-xl font-bold">Feature Two</h3>
        <p class="text-slate-600">Description goes here.</p>
      </div>
      <div class="p-6 border rounded-lg">
        <h3 class="text-xl font-bold">Feature Three</h3>
        <p class="text-slate-600">Description goes here.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-012",
        "title": "Feature List with Checkmarks",
        "description": "Checklist style features",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-xl mx-auto px-6">
      <ul class="space-y-4">
        <li class="flex items-center gap-3">
          <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          <span class="text-lg">Verified Secure</span>
        </li>
        <li class="flex items-center gap-3">
          <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          <span class="text-lg">Fast Performance</span>
        </li>
        <li class="flex items-center gap-3">
          <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          <span class="text-lg">24/7 Support</span>
        </li>
      </ul>
    </div>
  </div>"""
    }
]

def generate_and_push():
    for tmpl in TEMPLATES:
        # Create directory if not exists
        os.makedirs(tmpl['dir'], exist_ok=True)

        # File path
        file_path = os.path.join(tmpl['dir'], f"{tmpl['id']}.html")

        # Generate content
        html_content = BASE_HTML.format(
            id=tmpl['id'],
            title=tmpl['title'],
            description=tmpl['description'],
            content=tmpl['content']
        )

        # Write file
        with open(file_path, 'w') as f:
            f.write(html_content)

        print(f"Generated {file_path}")

        # Git operations
        try:
            subprocess.run(['git', 'add', file_path], check=True)
            subprocess.run(['git', 'commit', '-m', f"feat: implement {tmpl['id']} template"], check=True)
            subprocess.run(['git', 'push', 'origin', 'dev'], check=True)
            print(f"Pushed {tmpl['id']}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {tmpl['id']}: {e}")
            # Continue to next item even if git fails (though it shouldn't)

if __name__ == "__main__":
    generate_and_push()
