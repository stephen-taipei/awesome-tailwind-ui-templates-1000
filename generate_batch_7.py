import os
import subprocess

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

# Part 1: Content 013-030
TEMPLATES_CONTENT_1 = [
    {
        "id": "content-013",
        "title": "Image Gallery Grid",
        "description": "Multiple image grid",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <img src="https://via.placeholder.com/400" class="w-full h-64 object-cover rounded-lg" alt="Gallery 1">
        <img src="https://via.placeholder.com/400" class="w-full h-64 object-cover rounded-lg" alt="Gallery 2">
        <img src="https://via.placeholder.com/400" class="w-full h-64 object-cover rounded-lg" alt="Gallery 3">
        <img src="https://via.placeholder.com/400" class="w-full h-64 object-cover rounded-lg" alt="Gallery 4">
        <img src="https://via.placeholder.com/400" class="w-full h-64 object-cover rounded-lg" alt="Gallery 5">
        <img src="https://via.placeholder.com/400" class="w-full h-64 object-cover rounded-lg" alt="Gallery 6">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-014",
        "title": "Side-by-Side Images",
        "description": "Two images comparison",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="space-y-4">
        <img src="https://via.placeholder.com/600x400" class="w-full rounded-xl shadow-lg" alt="Before">
        <h3 class="text-center font-bold text-slate-900">Before</h3>
      </div>
      <div class="space-y-4">
        <img src="https://via.placeholder.com/600x400" class="w-full rounded-xl shadow-lg" alt="After">
        <h3 class="text-center font-bold text-slate-900">After</h3>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-015",
        "title": "Image with Text Overlay",
        "description": "Text overlaid on image",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative rounded-2xl overflow-hidden">
        <img src="https://via.placeholder.com/1200x600" class="w-full object-cover" alt="Background">
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-8">
          <div class="text-white">
            <h3 class="text-2xl font-bold">Overlay Title</h3>
            <p class="mt-2 text-slate-200">Description text overlaid on the image.</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-016",
        "title": "Video Section",
        "description": "Embedded video content",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-900">
    <div class="max-w-5xl mx-auto px-6">
      <div class="aspect-video bg-black rounded-2xl overflow-hidden shadow-2xl">
        <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen></iframe>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-017",
        "title": "Video with Thumbnail",
        "description": "Video preview thumbnail",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative group cursor-pointer rounded-2xl overflow-hidden shadow-xl">
        <img src="https://via.placeholder.com/1200x675" class="w-full" alt="Video Thumbnail">
        <div class="absolute inset-0 bg-black/30 flex items-center justify-center group-hover:bg-black/40 transition-colors">
          <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center pl-1 shadow-lg group-hover:scale-110 transition-transform">
            <svg class="w-8 h-8 text-primary-600" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-018",
        "title": "Before/After Image Slider",
        "description": "Image comparison slider",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative w-full aspect-video rounded-xl overflow-hidden select-none cursor-ew-resize group">
        <img src="https://via.placeholder.com/1200x675/333/fff?text=After" class="absolute inset-0 w-full h-full object-cover" alt="After">
        <div class="absolute inset-0 w-1/2 overflow-hidden border-r-2 border-white bg-white">
          <img src="https://via.placeholder.com/1200x675/ccc/000?text=Before" class="absolute inset-0 w-[200%] max-w-none h-full object-cover" alt="Before">
        </div>
        <div class="absolute inset-0 flex items-center justify-center pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity">
          <div class="bg-white/80 px-4 py-2 rounded-full text-sm font-bold">Drag to compare</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-019",
        "title": "Image Carousel",
        "description": "Sliding image gallery",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-6xl mx-auto px-6">
      <div class="flex gap-4 overflow-x-auto pb-8 snap-x">
        <div class="snap-center shrink-0 w-80 md:w-96">
          <img src="https://via.placeholder.com/400x300" class="w-full rounded-xl shadow-md" alt="Slide 1">
        </div>
        <div class="snap-center shrink-0 w-80 md:w-96">
          <img src="https://via.placeholder.com/400x300" class="w-full rounded-xl shadow-md" alt="Slide 2">
        </div>
        <div class="snap-center shrink-0 w-80 md:w-96">
          <img src="https://via.placeholder.com/400x300" class="w-full rounded-xl shadow-md" alt="Slide 3">
        </div>
        <div class="snap-center shrink-0 w-80 md:w-96">
          <img src="https://via.placeholder.com/400x300" class="w-full rounded-xl shadow-md" alt="Slide 4">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-020",
        "title": "Lightbox Gallery",
        "description": "Click-to-expand images",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="aspect-square cursor-pointer hover:opacity-90 transition-opacity">
        <img src="https://via.placeholder.com/400" class="w-full h-full object-cover rounded-lg" alt="Thumb 1">
      </div>
      <div class="aspect-square cursor-pointer hover:opacity-90 transition-opacity">
        <img src="https://via.placeholder.com/400" class="w-full h-full object-cover rounded-lg" alt="Thumb 2">
      </div>
      <div class="aspect-square cursor-pointer hover:opacity-90 transition-opacity">
        <img src="https://via.placeholder.com/400" class="w-full h-full object-cover rounded-lg" alt="Thumb 3">
      </div>
      <div class="aspect-square cursor-pointer hover:opacity-90 transition-opacity">
        <img src="https://via.placeholder.com/400" class="w-full h-full object-cover rounded-lg" alt="Thumb 4">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-021",
        "title": "Single Large Stat",
        "description": "Hero stat number",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-primary-600 text-white text-center">
    <div class="max-w-4xl mx-auto px-6">
      <div class="text-8xl font-bold tracking-tight">10M+</div>
      <div class="mt-4 text-2xl font-medium text-primary-100">Downloads Worldwide</div>
      <p class="mt-4 text-primary-200 max-w-xl mx-auto">Join the millions of users who trust our platform for their daily needs.</p>
    </div>
  </div>"""
    },
    {
        "id": "content-022",
        "title": "Stats Row",
        "description": "Horizontal stats display",
        "dir": "templates/04-content",
        "content": """<div class="py-16 bg-white border-y border-slate-100">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-x divide-slate-100">
        <div>
          <div class="text-4xl font-bold text-primary-600">99%</div>
          <div class="mt-2 text-sm text-slate-500 uppercase tracking-wide">Uptime</div>
        </div>
        <div>
          <div class="text-4xl font-bold text-primary-600">24/7</div>
          <div class="mt-2 text-sm text-slate-500 uppercase tracking-wide">Support</div>
        </div>
        <div>
          <div class="text-4xl font-bold text-primary-600">500+</div>
          <div class="mt-2 text-sm text-slate-500 uppercase tracking-wide">Integrations</div>
        </div>
        <div>
          <div class="text-4xl font-bold text-primary-600">100k</div>
          <div class="mt-2 text-sm text-slate-500 uppercase tracking-wide">Users</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-023",
        "title": "Stats Grid",
        "description": "Grid of statistics",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-xl shadow-sm">
          <div class="text-3xl font-bold text-slate-900">$50M</div>
          <div class="mt-2 text-slate-600">Revenue Generated</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-sm">
          <div class="text-3xl font-bold text-slate-900">150+</div>
          <div class="mt-2 text-slate-600">Countries Served</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-sm">
          <div class="text-3xl font-bold text-slate-900">1M</div>
          <div class="mt-2 text-slate-600">Transactions Daily</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-sm">
          <div class="text-3xl font-bold text-slate-900">4.9</div>
          <div class="mt-2 text-slate-600">App Store Rating</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-sm">
          <div class="text-3xl font-bold text-slate-900">0.1s</div>
          <div class="mt-2 text-slate-600">Average Latency</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-sm">
          <div class="text-3xl font-bold text-slate-900">99.99%</div>
          <div class="mt-2 text-slate-600">SLA Guarantee</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-024",
        "title": "Stats with Icons",
        "description": "Stats with visual icons",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
      <div class="flex flex-col items-center">
        <div class="h-12 w-12 text-primary-600 mb-4">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
        </div>
        <div class="text-4xl font-bold text-slate-900">5,000+</div>
        <div class="mt-2 text-slate-600">Happy Customers</div>
      </div>
      <div class="flex flex-col items-center">
        <div class="h-12 w-12 text-primary-600 mb-4">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        </div>
        <div class="text-4xl font-bold text-slate-900">100%</div>
        <div class="mt-2 text-slate-600">Satisfaction Rate</div>
      </div>
      <div class="flex flex-col items-center">
        <div class="h-12 w-12 text-primary-600 mb-4">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <div class="text-4xl font-bold text-slate-900">24h</div>
        <div class="mt-2 text-slate-600">Average Setup Time</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-025",
        "title": "Animated Counter Stats",
        "description": "Count-up animation stats",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-900 text-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
      <div>
        <div class="text-5xl font-bold tabular-nums">1,234</div>
        <div class="mt-2 text-slate-400">Projects Completed</div>
      </div>
      <div>
        <div class="text-5xl font-bold tabular-nums">850</div>
        <div class="mt-2 text-slate-400">Clients Served</div>
      </div>
      <div>
        <div class="text-5xl font-bold tabular-nums">15</div>
        <div class="mt-2 text-slate-400">Years Experience</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-026",
        "title": "Stats with Progress Bars",
        "description": "Stats with visual progress",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6 space-y-8">
      <div>
        <div class="flex justify-between mb-2">
          <span class="font-bold text-slate-900">Customer Satisfaction</span>
          <span class="text-slate-600">98%</span>
        </div>
        <div class="w-full bg-slate-100 rounded-full h-4">
          <div class="bg-green-500 h-4 rounded-full" style="width: 98%"></div>
        </div>
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <span class="font-bold text-slate-900">On-Time Delivery</span>
          <span class="text-slate-600">95%</span>
        </div>
        <div class="w-full bg-slate-100 rounded-full h-4">
          <div class="bg-blue-500 h-4 rounded-full" style="width: 95%"></div>
        </div>
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <span class="font-bold text-slate-900">Budget Adherence</span>
          <span class="text-slate-600">92%</span>
        </div>
        <div class="w-full bg-slate-100 rounded-full h-4">
          <div class="bg-purple-500 h-4 rounded-full" style="width: 92%"></div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-027",
        "title": "Stats Cards",
        "description": "Stats in card containers",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow border border-slate-100">
        <div class="text-sm text-slate-500 font-medium">Total Revenue</div>
        <div class="mt-2 text-3xl font-bold text-slate-900">$45,231</div>
        <div class="mt-2 text-sm text-green-600 flex items-center">
          <svg class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
          +20.1%
        </div>
      </div>
      <div class="bg-white p-6 rounded-lg shadow border border-slate-100">
        <div class="text-sm text-slate-500 font-medium">Active Users</div>
        <div class="mt-2 text-3xl font-bold text-slate-900">2,345</div>
        <div class="mt-2 text-sm text-green-600 flex items-center">
          <svg class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
          +15.3%
        </div>
      </div>
      <div class="bg-white p-6 rounded-lg shadow border border-slate-100">
        <div class="text-sm text-slate-500 font-medium">Bounce Rate</div>
        <div class="mt-2 text-3xl font-bold text-slate-900">42.3%</div>
        <div class="mt-2 text-sm text-red-600 flex items-center">
          <svg class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"/></svg>
          -4.1%
        </div>
      </div>
      <div class="bg-white p-6 rounded-lg shadow border border-slate-100">
        <div class="text-sm text-slate-500 font-medium">Avg. Session</div>
        <div class="mt-2 text-3xl font-bold text-slate-900">4m 12s</div>
        <div class="mt-2 text-sm text-slate-500">
          No change
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-028",
        "title": "Stats with Comparison",
        "description": "Before/after or vs stats",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <h2 class="text-center text-3xl font-bold text-slate-900 mb-12">Performance Comparison</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="bg-slate-50 p-8 rounded-2xl text-center">
          <h3 class="text-lg font-bold text-slate-500">Competitor A</h3>
          <div class="mt-4 text-4xl font-bold text-slate-400">2.5s</div>
          <p class="mt-2 text-slate-500">Load Time</p>
        </div>
        <div class="bg-primary-50 p-8 rounded-2xl text-center border-2 border-primary-500 relative overflow-hidden">
          <div class="absolute top-0 right-0 bg-primary-500 text-white text-xs font-bold px-3 py-1 rounded-bl-lg">WINNER</div>
          <h3 class="text-lg font-bold text-primary-700">Our Solution</h3>
          <div class="mt-4 text-4xl font-bold text-primary-600">0.4s</div>
          <p class="mt-2 text-primary-700">Load Time</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-029",
        "title": "Stats with Trend Indicators",
        "description": "Stats with up/down arrows",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="flex items-center gap-4">
        <div class="p-3 bg-green-100 text-green-600 rounded-full">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
        </div>
        <div>
          <div class="text-2xl font-bold text-slate-900">24%</div>
          <div class="text-sm text-slate-500">Increase in Sales</div>
        </div>
      </div>
      <div class="flex items-center gap-4">
        <div class="p-3 bg-red-100 text-red-600 rounded-full">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"/></svg>
        </div>
        <div>
          <div class="text-2xl font-bold text-slate-900">12%</div>
          <div class="text-sm text-slate-500">Decrease in Churn</div>
        </div>
      </div>
      <div class="flex items-center gap-4">
        <div class="p-3 bg-green-100 text-green-600 rounded-full">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
        </div>
        <div>
          <div class="text-2xl font-bold text-slate-900">45%</div>
          <div class="text-sm text-slate-500">Growth in Traffic</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-030",
        "title": "Stats Timeline",
        "description": "Stats along timeline",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-5xl mx-auto px-6">
      <div class="relative">
        <div class="absolute top-1/2 left-0 right-0 h-1 bg-slate-100 -translate-y-1/2 hidden md:block"></div>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 relative">
          <div class="bg-white p-4 text-center relative z-10">
            <div class="w-4 h-4 bg-primary-600 rounded-full mx-auto mb-4 border-4 border-white shadow"></div>
            <div class="text-xl font-bold text-slate-900">2020</div>
            <div class="text-sm text-slate-500">Founded</div>
          </div>
          <div class="bg-white p-4 text-center relative z-10">
            <div class="w-4 h-4 bg-primary-600 rounded-full mx-auto mb-4 border-4 border-white shadow"></div>
            <div class="text-xl font-bold text-slate-900">2021</div>
            <div class="text-sm text-slate-500">100 Clients</div>
          </div>
          <div class="bg-white p-4 text-center relative z-10">
            <div class="w-4 h-4 bg-primary-600 rounded-full mx-auto mb-4 border-4 border-white shadow"></div>
            <div class="text-xl font-bold text-slate-900">2022</div>
            <div class="text-sm text-slate-500">$1M Revenue</div>
          </div>
          <div class="bg-white p-4 text-center relative z-10">
            <div class="w-4 h-4 bg-primary-600 rounded-full mx-auto mb-4 border-4 border-white shadow"></div>
            <div class="text-xl font-bold text-slate-900">2023</div>
            <div class="text-sm text-slate-500">Global Expansion</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]

# Part 2: Content 031-050
TEMPLATES_CONTENT_2 = [
    {
        "id": "content-031",
        "title": "Simple Blockquote",
        "description": "Basic quote styling",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6">
      <blockquote class="border-l-4 border-primary-600 pl-6 italic text-xl text-slate-700">
        "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle."
      </blockquote>
    </div>
  </div>"""
    },
    {
        "id": "content-032",
        "title": "Blockquote with Attribution",
        "description": "Quote + author citation",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6">
      <figure>
        <blockquote class="text-2xl font-medium text-slate-900 text-center">
          "Innovation distinguishes between a leader and a follower."
        </blockquote>
        <figcaption class="mt-6 flex items-center justify-center space-x-3">
          <div class="text-base font-semibold text-slate-900">Steve Jobs</div>
          <svg viewBox="0 0 2 2" width="3" height="3" aria-hidden="true" class="fill-slate-900"><circle cx="1" cy="1" r="1" /></svg>
          <div class="text-base text-slate-500">Co-founder, Apple Inc.</div>
        </figcaption>
      </figure>
    </div>
  </div>"""
    },
    {
        "id": "content-033",
        "title": "Large Pull Quote",
        "description": "Editorial pull quote",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <blockquote class="text-4xl md:text-6xl font-serif font-bold text-slate-900 leading-tight">
        "Design is not just what it looks like and feels like. Design is how it works."
      </blockquote>
    </div>
  </div>"""
    },
    {
        "id": "content-034",
        "title": "Quote with Photo",
        "description": "Quote + author photo",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <div class="flex flex-col md:flex-row items-center gap-8">
        <img src="https://via.placeholder.com/150" class="w-24 h-24 rounded-full object-cover shadow-lg" alt="Author">
        <blockquote class="text-xl text-slate-700">
          <p>"Simplicity is the ultimate sophistication. It takes a lot of hard work to make something simple, to truly understand the underlying challenges and come up with elegant solutions."</p>
          <footer class="mt-4 font-bold text-slate-900">- Leonardo da Vinci</footer>
        </blockquote>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-035",
        "title": "Quote Card",
        "description": "Quote in card container",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white p-8 rounded-2xl shadow-xl relative">
        <svg class="absolute top-4 left-4 w-8 h-8 text-primary-200 transform -translate-x-2 -translate-y-2" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.896 14.325 16.053 14.941 15.471C15.556 14.89 16.519 14.6 17.83 14.6L19 14.6V10.4L17.83 10.4C16.403 10.4 15.344 10.083 14.651 9.45C13.959 8.817 13.613 7.9 13.613 6.7L13.613 2.6L19 2.6V7.1C19 7.633 18.896 8.058 18.688 8.375C18.48 8.692 18.167 8.85 17.75 8.85L17.4 8.85L17.4 11.85L17.75 11.85C19.167 11.85 20.25 12.183 21 12.85C21.75 13.517 22.125 14.433 22.125 15.6L22.125 21L14.017 21ZM5.01697 21L5.01697 18C5.01697 16.896 5.32497 16.053 5.94097 15.471C6.55697 14.89 7.51897 14.6 8.82997 14.6L9.99997 14.6V10.4L8.82997 10.4C7.40297 10.4 6.34397 10.083 5.65097 9.45C4.95897 8.817 4.61297 7.9 4.61297 6.7L4.61297 2.6L9.99997 2.6V7.1C9.99997 7.633 9.89597 8.058 9.68797 8.375C9.47997 8.692 9.16697 8.85 8.74997 8.85L8.39997 8.85L8.39997 11.85L8.74997 11.85C10.167 11.85 11.25 12.183 12 12.85C12.75 13.517 13.125 14.433 13.125 15.6L13.125 21L5.01697 21Z"/></svg>
        <p class="relative z-10 text-lg text-slate-700 italic">
          "Quality is not an act, it is a habit. We are what we repeatedly do. Excellence, then, is not an act, but a habit."
        </p>
        <div class="mt-6 font-bold text-slate-900">- Aristotle</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-036",
        "title": "Centered Quote",
        "description": "Center-aligned quote",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6 text-center">
      <div class="w-16 h-1 bg-primary-600 mx-auto mb-8"></div>
      <blockquote class="text-3xl font-light text-slate-900 leading-relaxed">
        "Creativity is intelligence having fun."
      </blockquote>
      <div class="mt-8 text-sm font-bold tracking-widest uppercase text-slate-500">Albert Einstein</div>
    </div>
  </div>"""
    },
    {
        "id": "content-037",
        "title": "Quote with Background Image",
        "description": "Quote over image",
        "dir": "templates/04-content",
        "content": """<div class="relative py-32 bg-slate-900">
    <div class="absolute inset-0 overflow-hidden">
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80" class="w-full h-full object-cover opacity-30" alt="Background">
    </div>
    <div class="relative max-w-4xl mx-auto px-6 text-center text-white">
      <blockquote class="text-3xl md:text-5xl font-bold leading-tight">
        "The best way to predict the future is to create it."
      </blockquote>
      <div class="mt-8 text-xl font-medium text-white/80">- Peter Drucker</div>
    </div>
  </div>"""
    },
    {
        "id": "content-038",
        "title": "Quote Carousel",
        "description": "Rotating quotes",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <div class="relative">
        <blockquote class="text-2xl text-slate-700">
          "First, solve the problem. Then, write the code."
        </blockquote>
        <div class="mt-6 font-bold text-slate-900">- John Johnson</div>

        <div class="mt-12 flex justify-center gap-2">
          <button class="w-3 h-3 rounded-full bg-primary-600"></button>
          <button class="w-3 h-3 rounded-full bg-slate-300"></button>
          <button class="w-3 h-3 rounded-full bg-slate-300"></button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-039",
        "title": "Side Quote",
        "description": "Quote alongside content",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 clearfix">
      <div class="prose prose-slate prose-lg text-slate-600">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <aside class="md:float-right md:w-1/3 md:ml-8 mb-8 p-6 bg-slate-50 border-l-4 border-primary-500 italic text-slate-800">
          "This is a key takeaway that deserves special attention."
        </aside>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
        <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-040",
        "title": "Quote Grid",
        "description": "Multiple quotes grid",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow-sm">
        <p class="italic text-slate-600">"Great things in business are never done by one person."</p>
        <div class="mt-4 font-bold text-slate-900">- Steve Jobs</div>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-sm">
        <p class="italic text-slate-600">"Success is not final; failure is not fatal: It is the courage to continue that counts."</p>
        <div class="mt-4 font-bold text-slate-900">- Winston Churchill</div>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-sm">
        <p class="italic text-slate-600">"It always seems impossible until it's done."</p>
        <div class="mt-4 font-bold text-slate-900">- Nelson Mandela</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-041",
        "title": "Text + Image Section",
        "description": "Standard content + visual",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Visual Storytelling</h2>
        <p class="text-lg text-slate-600 mb-6">
          Images can communicate complex ideas faster than text alone. Use high-quality visuals to support your message and engage your audience.
        </p>
        <ul class="space-y-4 text-slate-600">
          <li class="flex items-center"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> High resolution</li>
          <li class="flex items-center"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Relevant context</li>
          <li class="flex items-center"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Emotional connection</li>
        </ul>
      </div>
      <div>
        <img src="https://via.placeholder.com/600x400" class="w-full rounded-2xl shadow-xl" alt="Visual Storytelling">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-042",
        "title": "Text + Video Section",
        "description": "Content + embedded video",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <div class="order-2 md:order-1">
        <div class="aspect-video bg-black rounded-xl overflow-hidden shadow-lg">
          <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen></iframe>
        </div>
      </div>
      <div class="order-1 md:order-2">
        <h2 class="text-3xl font-bold text-slate-900 mb-6">See It in Action</h2>
        <p class="text-lg text-slate-600">
          Watch our product walkthrough to see how easy it is to get started. In just 2 minutes, you'll learn everything you need to know.
        </p>
        <div class="mt-8">
          <a href="#" class="text-primary-600 font-bold hover:text-primary-700 flex items-center">
            View full documentation <svg class="w-4 h-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-043",
        "title": "Text + Stats Section",
        "description": "Content + statistics",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Proven Results</h2>
        <p class="text-lg text-slate-600 mb-8">
          We deliver measurable impact for our clients. Our data-driven approach ensures that every decision is backed by solid evidence.
        </p>
        <a href="#" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700">
          Read Case Studies
        </a>
      </div>
      <div class="grid grid-cols-2 gap-6">
        <div class="bg-slate-50 p-6 rounded-xl text-center">
          <div class="text-4xl font-bold text-primary-600">2x</div>
          <div class="mt-2 text-sm text-slate-600">Revenue Growth</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-xl text-center">
          <div class="text-4xl font-bold text-primary-600">50%</div>
          <div class="mt-2 text-sm text-slate-600">Cost Reduction</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-xl text-center">
          <div class="text-4xl font-bold text-primary-600">3x</div>
          <div class="mt-2 text-sm text-slate-600">Faster Delivery</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-xl text-center">
          <div class="text-4xl font-bold text-primary-600">99%</div>
          <div class="mt-2 text-sm text-slate-600">Client Retention</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-044",
        "title": "Content with Code Block",
        "description": "Technical content + code",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-12">
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Easy Integration</h2>
        <p class="text-lg text-slate-600 mb-6">
          Get up and running in minutes with our simple API. Just copy and paste the code snippet to start using our services.
        </p>
        <p class="text-slate-600">
          Our SDK handles authentication, error handling, and retries automatically, so you can focus on building your application.
        </p>
      </div>
      <div class="bg-slate-900 rounded-xl p-6 overflow-x-auto shadow-2xl">
        <pre class="text-sm text-slate-300 font-mono"><code>// Initialize the client
const client = new APIClient({
  apiKey: 'YOUR_API_KEY',
  environment: 'production'
});

// Fetch data
async function getData() {
  try {
    const response = await client.users.list();
    console.log(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
}

getData();</code></pre>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-045",
        "title": "Content with Embed",
        "description": "Content + third-party embed",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-8">Listen to Our Podcast</h2>
      <div class="w-full bg-slate-100 rounded-xl p-4">
        <div class="h-40 flex items-center justify-center text-slate-500">
          [Podcast Player Embed Placeholder]
        </div>
      </div>
      <p class="mt-6 text-slate-600">
        New episodes every Tuesday. Subscribe on your favorite platform.
      </p>
    </div>
  </div>"""
    },
    {
        "id": "content-046",
        "title": "Content with Timeline",
        "description": "History/process content",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 mb-12 text-center">Our Journey</h2>
      <div class="border-l-2 border-slate-200 ml-3 space-y-12">
        <div class="pl-8 relative">
          <div class="absolute -left-[9px] top-0 h-4 w-4 rounded-full bg-primary-600 ring-4 ring-white"></div>
          <div class="text-sm font-bold text-primary-600 mb-1">2018</div>
          <h3 class="text-xl font-bold text-slate-900">Founded</h3>
          <p class="mt-2 text-slate-600">Started in a garage with a vision to change the world.</p>
        </div>
        <div class="pl-8 relative">
          <div class="absolute -left-[9px] top-0 h-4 w-4 rounded-full bg-slate-300 ring-4 ring-white"></div>
          <div class="text-sm font-bold text-slate-500 mb-1">2020</div>
          <h3 class="text-xl font-bold text-slate-900">Series A Funding</h3>
          <p class="mt-2 text-slate-600">Raised $10M to scale operations and hire talent.</p>
        </div>
        <div class="pl-8 relative">
          <div class="absolute -left-[9px] top-0 h-4 w-4 rounded-full bg-slate-300 ring-4 ring-white"></div>
          <div class="text-sm font-bold text-slate-500 mb-1">2022</div>
          <h3 class="text-xl font-bold text-slate-900">Global Expansion</h3>
          <p class="mt-2 text-slate-600">Opened offices in London, Tokyo, and Singapore.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-047",
        "title": "Content with Map",
        "description": "Location-based content",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12">
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Visit Us</h2>
        <div class="space-y-4 text-slate-600">
          <p class="font-bold text-slate-900">Headquarters</p>
          <p>123 Innovation Drive<br>Tech City, TC 90210</p>
          <p>
            <a href="mailto:hello@example.com" class="text-primary-600 hover:underline">hello@example.com</a><br>
            <a href="tel:+15551234567" class="text-primary-600 hover:underline">+1 (555) 123-4567</a>
          </p>
          <p>
            <strong>Hours:</strong><br>
            Mon-Fri: 9am - 6pm<br>
            Sat-Sun: Closed
          </p>
        </div>
      </div>
      <div class="h-96 bg-slate-200 rounded-xl overflow-hidden">
        <div class="w-full h-full flex items-center justify-center text-slate-500 bg-slate-100">
          [Map Embed Placeholder]
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-048",
        "title": "Content with Data Table",
        "description": "Content + tabular data",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-5xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 mb-8">Technical Specifications</h2>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-slate-200">
              <th class="py-4 px-4 font-bold text-slate-900">Feature</th>
              <th class="py-4 px-4 font-bold text-slate-900">Standard</th>
              <th class="py-4 px-4 font-bold text-slate-900">Pro</th>
              <th class="py-4 px-4 font-bold text-slate-900">Enterprise</th>
            </tr>
          </thead>
          <tbody class="text-slate-600">
            <tr class="border-b border-slate-100">
              <td class="py-4 px-4">Storage</td>
              <td class="py-4 px-4">10 GB</td>
              <td class="py-4 px-4">100 GB</td>
              <td class="py-4 px-4">Unlimited</td>
            </tr>
            <tr class="border-b border-slate-100">
              <td class="py-4 px-4">Bandwidth</td>
              <td class="py-4 px-4">1 TB</td>
              <td class="py-4 px-4">10 TB</td>
              <td class="py-4 px-4">Unlimited</td>
            </tr>
            <tr class="border-b border-slate-100">
              <td class="py-4 px-4">Users</td>
              <td class="py-4 px-4">1</td>
              <td class="py-4 px-4">5</td>
              <td class="py-4 px-4">Unlimited</td>
            </tr>
            <tr>
              <td class="py-4 px-4">Support</td>
              <td class="py-4 px-4">Email</td>
              <td class="py-4 px-4">Priority</td>
              <td class="py-4 px-4">24/7 Dedicated</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-049",
        "title": "Content with Infographic",
        "description": "Content + visual data",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-12">How It Works</h2>
      <div class="relative">
        <div class="absolute top-1/2 left-0 right-0 h-1 bg-slate-100 -translate-y-1/2 -z-10 hidden md:block"></div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-white p-6">
            <div class="w-16 h-16 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">1</div>
            <h3 class="text-xl font-bold text-slate-900">Sign Up</h3>
            <p class="mt-2 text-slate-600">Create your free account in seconds.</p>
          </div>
          <div class="bg-white p-6">
            <div class="w-16 h-16 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">2</div>
            <h3 class="text-xl font-bold text-slate-900">Connect</h3>
            <p class="mt-2 text-slate-600">Link your data sources securely.</p>
          </div>
          <div class="bg-white p-6">
            <div class="w-16 h-16 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">3</div>
            <h3 class="text-xl font-bold text-slate-900">Analyze</h3>
            <p class="mt-2 text-slate-600">Get insights instantly.</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-050",
        "title": "Rich Media Content",
        "description": "Multi-media content section",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 space-y-12">
      <div class="text-center">
        <h2 class="text-3xl font-bold text-slate-900">Immersive Storytelling</h2>
        <p class="mt-4 text-xl text-slate-600">Combining text, images, and video for maximum impact.</p>
      </div>

      <img src="https://via.placeholder.com/1200x600" class="w-full rounded-2xl shadow-lg" alt="Wide Image">

      <div class="prose prose-slate prose-lg mx-auto">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <img src="https://via.placeholder.com/600x400" class="w-full rounded-xl shadow-md" alt="Detail 1">
        <img src="https://via.placeholder.com/600x400" class="w-full rounded-xl shadow-md" alt="Detail 2">
      </div>

      <div class="bg-slate-50 p-8 rounded-2xl text-center">
        <h3 class="text-2xl font-bold text-slate-900 mb-4">Ready to start?</h3>
        <button class="bg-primary-600 text-white px-8 py-3 rounded-full font-bold hover:bg-primary-700 transition-colors">Get Started Now</button>
      </div>
    </div>
  </div>"""
    }
]
# Part 3: CTA 001-025
TEMPLATES_CTA_1 = [
    {
        "id": "cta-001",
        "title": "Simple Centered CTA",
        "description": "Basic centered call to action",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Ready to dive in?</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Start your free trial today. No credit card required.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Get started</a>
        <a href="#" class="text-sm font-semibold leading-6 text-slate-900">Learn more <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-002",
        "title": "Simple Left-Aligned CTA",
        "description": "Left-aligned call to action",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Boost your productivity.<br>Start using our app today.</h2>
      <div class="mt-10 flex items-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Get started</a>
        <a href="#" class="text-sm font-semibold leading-6 text-slate-900">Learn more <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-003",
        "title": "Simple Right-Aligned CTA",
        "description": "Right-aligned call to action",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 flex flex-col items-end text-right">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Join the revolution.<br>Experience the future.</h2>
      <p class="mt-6 max-w-xl text-lg leading-8 text-slate-600">Don't get left behind. Upgrade your workflow with our cutting-edge tools.</p>
      <div class="mt-10 flex items-center gap-x-6">
        <a href="#" class="text-sm font-semibold leading-6 text-slate-900"><span aria-hidden="true">←</span> Learn more</a>
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Get started</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-004",
        "title": "CTA with Button and Link",
        "description": "Primary button and secondary link",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Ready to get started?</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Join thousands of satisfied customers who are already using our platform.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Sign up for free</a>
        <a href="#" class="text-sm font-semibold leading-6 text-slate-900">Contact sales <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-005",
        "title": "CTA with Two Buttons",
        "description": "Two primary/secondary buttons",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Choose your path</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Whether you're an individual or a team, we have a plan for you.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">For Individuals</a>
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 hover:bg-slate-50">For Teams</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-006",
        "title": "CTA with Input Field",
        "description": "Newsletter signup style",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 lg:flex lg:items-center lg:justify-between">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Sign up for our newsletter.<br>Stay up to date.</h2>
      <form class="mt-10 w-full max-w-md lg:mt-0">
        <div class="flex gap-x-4">
          <label for="email-address" class="sr-only">Email address</label>
          <input id="email-address" name="email" type="email" autocomplete="email" required class="min-w-0 flex-auto rounded-md border-0 px-3.5 py-2 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6" placeholder="Enter your email">
          <button type="submit" class="flex-none rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Subscribe</button>
        </div>
        <p class="mt-4 text-sm leading-6 text-slate-600">We care about your data. Read our <a href="#" class="font-semibold text-primary-600 hover:text-primary-500">privacy policy</a>.</p>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "cta-007",
        "title": "CTA with Image",
        "description": "Split layout with image",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white">
    <div class="mx-auto max-w-7xl py-24 sm:px-6 sm:py-32 lg:px-8">
      <div class="relative isolate overflow-hidden bg-slate-900 px-6 pt-16 shadow-2xl sm:rounded-3xl sm:px-16 md:pt-24 lg:flex lg:gap-x-20 lg:px-24 lg:pt-0">
        <div class="mx-auto max-w-md text-center lg:mx-0 lg:flex-auto lg:py-32 lg:text-left">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Boost your productivity.<br>Start using our app today.</h2>
          <p class="mt-6 text-lg leading-8 text-slate-300">Ac euismod vel sit maecenas id pellentesque eu sed consectetur. Malesuada adipiscing sagittis vel nulla.</p>
          <div class="mt-10 flex items-center justify-center gap-x-6 lg:justify-start">
            <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
            <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
          </div>
        </div>
        <div class="relative mt-16 h-80 lg:mt-8">
          <img class="absolute left-0 top-0 w-[57rem] max-w-none rounded-md bg-white/5 ring-1 ring-white/10" src="https://tailwindui.com/img/component-images/dark-project-app-screenshot.png" alt="App screenshot" width="1824" height="1080">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-008",
        "title": "CTA with Background Image",
        "description": "Full width background image",
        "dir": "templates/05-cta",
        "content": """<div class="relative bg-slate-900 py-32 sm:py-40">
    <div class="absolute inset-0 overflow-hidden">
      <img src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&crop=focalpoint&fp-y=.8&w=2830&h=1500&q=80&blend=111827&sat=-100&exp=15&blend-mode=multiply" alt="" class="h-full w-full object-cover object-center">
    </div>
    <div class="relative mx-auto max-w-7xl px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Work with us</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-300">Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Open roles</a>
        <a href="#" class="text-sm font-semibold leading-6 text-white">Our values <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-009",
        "title": "CTA with Dark Background",
        "description": "Dark theme CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Ready to dive in?</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-300">Start your free trial today. No credit card required.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
        <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-010",
        "title": "CTA with Gradient Background",
        "description": "Gradient background CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-gradient-to-r from-primary-600 to-secondary-600 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Ready to dive in?</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-primary-100">Start your free trial today. No credit card required.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-primary-600 shadow-sm hover:bg-primary-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
        <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-011",
        "title": "CTA with Pattern Background",
        "description": "Patterned background CTA",
        "dir": "templates/05-cta",
        "content": """<div class="relative bg-primary-700 py-24">
    <div class="absolute inset-0 opacity-10" style="background-image: url('data:image/svg+xml,%3Csvg width=\\'20\\' height=\\'20\\' viewBox=\\'0 0 20 20\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cg fill=\\'%23ffffff\\' fill-opacity=\\'1\\' fill-rule=\\'evenodd\\'%3E%3Ccircle cx=\\'3\\' cy=\\'3\\' r=\\'3\\'/%3E%3Ccircle cx=\\'13\\' cy=\\'13\\' r=\\'3\\'/%3E%3C/g%3E%3C/svg%3E');"></div>
    <div class="relative max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Ready to dive in?</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-primary-100">Start your free trial today. No credit card required.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-primary-600 shadow-sm hover:bg-primary-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
        <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-012",
        "title": "CTA with Split Layout",
        "description": "50/50 split layout",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white">
    <div class="grid grid-cols-1 lg:grid-cols-2">
      <div class="flex items-center justify-center bg-primary-600 px-6 py-24 sm:px-12 lg:px-24">
        <div class="max-w-md text-center lg:text-left">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Ready to dive in?</h2>
          <p class="mt-6 text-lg leading-8 text-primary-100">Start your free trial today. No credit card required.</p>
          <div class="mt-10 flex items-center justify-center gap-x-6 lg:justify-start">
            <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-primary-600 shadow-sm hover:bg-primary-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
            <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
          </div>
        </div>
      </div>
      <div class="relative h-64 lg:h-auto">
        <img class="absolute inset-0 h-full w-full object-cover" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1471&q=80" alt="Office">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-013",
        "title": "CTA with Card Layout",
        "description": "Card style CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-xl overflow-hidden">
        <div class="px-6 py-12 sm:px-12 sm:py-16 lg:flex lg:items-center lg:justify-between">
          <div>
            <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Ready to dive in?</h2>
            <p class="mt-6 text-lg leading-8 text-slate-600">Start your free trial today. No credit card required.</p>
          </div>
          <div class="mt-10 flex items-center gap-x-6 lg:mt-0 lg:flex-shrink-0">
            <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Get started</a>
            <a href="#" class="text-sm font-semibold leading-6 text-slate-900">Learn more <span aria-hidden="true">→</span></a>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-014",
        "title": "CTA with Floating Card",
        "description": "Floating card effect",
        "dir": "templates/05-cta",
        "content": """<div class="bg-primary-700 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="relative isolate overflow-hidden bg-slate-900 px-6 py-24 text-center shadow-2xl sm:rounded-3xl sm:px-16">
        <h2 class="mx-auto max-w-2xl text-3xl font-bold tracking-tight text-white sm:text-4xl">Boost your productivity today.</h2>
        <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-300">Incididunt sint fugiat pariatur cupidatat consectetur sit cillum anim id veniam aliqua proident excepteur commodo do ea.</p>
        <div class="mt-10 flex items-center justify-center gap-x-6">
          <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
          <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
        </div>
        <svg viewBox="0 0 1024 1024" class="absolute left-1/2 top-1/2 -z-10 h-[64rem] w-[64rem] -translate-x-1/2 [mask-image:radial-gradient(closest-side,white,transparent)]" aria-hidden="true">
          <circle cx="512" cy="512" r="512" fill="url(#827591b1-ce8c-4110-b064-7cb85a0b1217)" fill-opacity="0.7" />
          <defs>
            <radialGradient id="827591b1-ce8c-4110-b064-7cb85a0b1217">
              <stop stop-color="#7775D6" />
              <stop offset="1" stop-color="#E935C1" />
            </radialGradient>
          </defs>
        </svg>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-015",
        "title": "CTA with App Store Buttons",
        "description": "Mobile app download CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Get the app</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Download our mobile app and stay connected wherever you go.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="inline-block">
          <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Download_on_the_App_Store_Badge.svg" alt="Download on the App Store" class="h-12">
        </a>
        <a href="#" class="inline-block">
          <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" alt="Get it on Google Play" class="h-12">
        </a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-016",
        "title": "CTA with Social Proof",
        "description": "CTA with user avatars",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Join the community</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Over 10,000 developers are already building with us.</p>
      <div class="mt-8 flex justify-center -space-x-2 overflow-hidden">
        <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
        <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
        <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt=""/>
        <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
      </div>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Get started</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-017",
        "title": "CTA with Countdown",
        "description": "Urgency countdown timer",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Limited Time Offer</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-300">Get 50% off your first year. Offer ends soon.</p>
      <div class="mt-8 flex justify-center gap-4 text-white">
        <div class="flex flex-col items-center bg-slate-800 p-4 rounded-lg min-w-[80px]">
          <span class="text-3xl font-bold">02</span>
          <span class="text-xs uppercase text-slate-400">Days</span>
        </div>
        <div class="flex flex-col items-center bg-slate-800 p-4 rounded-lg min-w-[80px]">
          <span class="text-3xl font-bold">14</span>
          <span class="text-xs uppercase text-slate-400">Hours</span>
        </div>
        <div class="flex flex-col items-center bg-slate-800 p-4 rounded-lg min-w-[80px]">
          <span class="text-3xl font-bold">35</span>
          <span class="text-xs uppercase text-slate-400">Minutes</span>
        </div>
        <div class="flex flex-col items-center bg-slate-800 p-4 rounded-lg min-w-[80px]">
          <span class="text-3xl font-bold">12</span>
          <span class="text-xs uppercase text-slate-400">Seconds</span>
        </div>
      </div>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Claim Offer</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-018",
        "title": "CTA with Video Background",
        "description": "Video background CTA",
        "dir": "templates/05-cta",
        "content": """<div class="relative py-32 sm:py-40">
    <div class="absolute inset-0 overflow-hidden">
      <video class="h-full w-full object-cover" autoplay muted loop playsinline poster="https://via.placeholder.com/1920x1080">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-stars-in-space-1610-large.mp4" type="video/mp4">
      </video>
      <div class="absolute inset-0 bg-slate-900/70 mix-blend-multiply"></div>
    </div>
    <div class="relative mx-auto max-w-7xl px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Experience the impossible</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-300">Push the boundaries of what's possible with our advanced technology.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Explore now</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-019",
        "title": "CTA with Modal Trigger",
        "description": "CTA that opens a modal",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Have questions?</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Our team is here to help you get started.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <button type="button" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" onclick="alert('Modal would open here')">Contact Support</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-020",
        "title": "CTA with Form",
        "description": "Inline form CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="bg-slate-900 rounded-3xl p-8 sm:p-16 lg:flex lg:items-center lg:justify-between">
        <div class="lg:w-1/2">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Get a free consultation</h2>
          <p class="mt-4 text-lg text-slate-300">Fill out the form and our team will get back to you within 24 hours.</p>
        </div>
        <div class="mt-10 lg:mt-0 lg:w-1/2 lg:pl-16">
          <form class="space-y-4">
            <div>
              <label for="name" class="sr-only">Name</label>
              <input type="text" name="name" id="name" class="block w-full rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-white sm:text-sm sm:leading-6" placeholder="Name">
            </div>
            <div>
              <label for="email" class="sr-only">Email</label>
              <input type="email" name="email" id="email" class="block w-full rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-white sm:text-sm sm:leading-6" placeholder="Email">
            </div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Request Consultation</button>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-021",
        "title": "CTA with Newsletter Signup",
        "description": "Newsletter focus CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Subscribe to our newsletter</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Get the latest news and updates delivered straight to your inbox.</p>
      <form class="mx-auto mt-10 flex max-w-md gap-x-4">
        <label for="email-address" class="sr-only">Email address</label>
        <input id="email-address" name="email" type="email" autocomplete="email" required class="min-w-0 flex-auto rounded-md border-0 bg-white px-3.5 py-2 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6" placeholder="Enter your email">
        <button type="submit" class="flex-none rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Subscribe</button>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "cta-022",
        "title": "CTA with Discount Code",
        "description": "Discount offer CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-primary-600 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Get 20% off your first order</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-primary-100">Use code <span class="font-mono font-bold bg-white/20 px-2 py-1 rounded">WELCOME20</span> at checkout.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-primary-600 shadow-sm hover:bg-primary-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Shop Now</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-023",
        "title": "CTA with Guarantee",
        "description": "Risk-free guarantee CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Try it risk-free</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">30-day money-back guarantee. No questions asked.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Start Free Trial</a>
      </div>
      <div class="mt-8 flex justify-center items-center gap-2 text-sm text-slate-500">
        <svg class="h-5 w-5 text-green-500" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
        <span>No credit card required</span>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-024",
        "title": "CTA with Testimonial",
        "description": "CTA with user quote",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Join thousands of happy customers</h2>
        <p class="mt-6 text-lg leading-8 text-slate-600">See why leading companies trust us to power their business.</p>
        <div class="mt-10 flex items-center gap-x-6">
          <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Get started</a>
          <a href="#" class="text-sm font-semibold leading-6 text-slate-900">Read stories <span aria-hidden="true">→</span></a>
        </div>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm">
        <blockquote class="text-lg font-medium text-slate-900">
          "This platform has completely transformed how we work. I can't imagine going back to the old way."
        </blockquote>
        <div class="mt-6 flex items-center gap-x-4">
          <img class="h-10 w-10 rounded-full bg-slate-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div>
            <div class="font-semibold">Sarah Smith</div>
            <div class="text-sm text-slate-500">CEO, TechCorp</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-025",
        "title": "CTA with FAQ Link",
        "description": "CTA with help link",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Ready to get started?</h2>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Sign up now</a>
      </div>
      <p class="mt-10 text-sm text-slate-500">
        Still have questions? <a href="#" class="font-semibold text-primary-600 hover:text-primary-500">Check out our FAQ</a> or <a href="#" class="font-semibold text-primary-600 hover:text-primary-500">contact support</a>.
      </p>
    </div>
  </div>"""
    }
]
# Part 4: CTA 026-050
TEMPLATES_CTA_2 = [
    {
        "id": "cta-026",
        "title": "CTA with Pricing Preview",
        "description": "CTA showing pricing options",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 lg:flex lg:items-center lg:justify-between lg:gap-12">
      <div class="lg:w-1/2">
        <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Simple, transparent pricing</h2>
        <p class="mt-4 text-lg text-slate-600">No hidden fees. Cancel anytime.</p>
        <div class="mt-8">
          <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">View full pricing</a>
        </div>
      </div>
      <div class="mt-10 lg:mt-0 lg:w-1/2 bg-slate-50 rounded-2xl p-8 border border-slate-200">
        <div class="flex items-baseline gap-2">
          <span class="text-4xl font-bold text-slate-900">$29</span>
          <span class="text-slate-600">/month</span>
        </div>
        <p class="mt-2 text-sm text-slate-500">for the Pro plan</p>
        <ul class="mt-6 space-y-3 text-sm text-slate-600">
          <li class="flex items-center"><svg class="w-4 h-4 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited projects</li>
          <li class="flex items-center"><svg class="w-4 h-4 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Priority support</li>
          <li class="flex items-center"><svg class="w-4 h-4 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Analytics dashboard</li>
        </ul>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-027",
        "title": "CTA with Feature List",
        "description": "CTA highlighting key features",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 lg:flex lg:items-center lg:justify-between">
      <div class="lg:w-1/2">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Everything you need</h2>
        <p class="mt-4 text-lg text-slate-300">All the tools to build your next big thing.</p>
        <div class="mt-8 flex gap-x-6">
          <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started</a>
        </div>
      </div>
      <div class="mt-10 lg:mt-0 lg:w-1/2">
        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-6 text-white">
          <li class="flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-white/10">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
            </div>
            <span>Fast performance</span>
          </li>
          <li class="flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-white/10">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
            </div>
            <span>Secure by default</span>
          </li>
          <li class="flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-white/10">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
            </div>
            <span>Modular design</span>
          </li>
          <li class="flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-white/10">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
            </div>
            <span>Developer friendly</span>
          </li>
        </ul>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-028",
        "title": "CTA with Steps",
        "description": "CTA showing process steps",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Get started in 3 easy steps</h2>
      <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="relative">
          <div class="flex items-center justify-center w-12 h-12 bg-primary-100 text-primary-600 font-bold rounded-full mx-auto mb-4">1</div>
          <h3 class="text-lg font-bold text-slate-900">Create Account</h3>
          <p class="mt-2 text-sm text-slate-600">Sign up in seconds.</p>
        </div>
        <div class="relative">
          <div class="flex items-center justify-center w-12 h-12 bg-primary-100 text-primary-600 font-bold rounded-full mx-auto mb-4">2</div>
          <h3 class="text-lg font-bold text-slate-900">Install SDK</h3>
          <p class="mt-2 text-sm text-slate-600">Add one line of code.</p>
        </div>
        <div class="relative">
          <div class="flex items-center justify-center w-12 h-12 bg-primary-100 text-primary-600 font-bold rounded-full mx-auto mb-4">3</div>
          <h3 class="text-lg font-bold text-slate-900">Launch</h3>
          <p class="mt-2 text-sm text-slate-600">Go live instantly.</p>
        </div>
      </div>
      <div class="mt-12">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Start Now</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-029",
        "title": "CTA with Tabs",
        "description": "CTA with tabbed content",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl mb-8">Choose your role</h2>
      <div class="border-b border-slate-200">
        <nav class="-mb-px flex justify-center space-x-8" aria-label="Tabs">
          <a href="#" class="border-primary-500 text-primary-600 whitespace-nowrap border-b-2 py-4 px-1 text-sm font-medium" aria-current="page">Developers</a>
          <a href="#" class="border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700 whitespace-nowrap border-b-2 py-4 px-1 text-sm font-medium">Designers</a>
          <a href="#" class="border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700 whitespace-nowrap border-b-2 py-4 px-1 text-sm font-medium">Managers</a>
        </nav>
      </div>
      <div class="mt-8">
        <p class="text-lg text-slate-600 mb-8">
          Build faster with our robust API and extensive documentation.
        </p>
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Start Coding</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-030",
        "title": "CTA with Slider",
        "description": "CTA with interactive slider",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl mb-8">Calculate your savings</h2>
      <div class="bg-slate-50 p-8 rounded-2xl">
        <label for="users-range" class="block mb-2 text-sm font-medium text-slate-900">Number of Users: <span id="user-count" class="font-bold text-primary-600">50</span></label>
        <input id="users-range" type="range" min="1" max="100" value="50" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary-600">
        <div class="mt-8">
          <p class="text-lg text-slate-600">Estimated Savings:</p>
          <p class="text-4xl font-bold text-slate-900">$<span id="savings-amount">500</span>/mo</p>
        </div>
        <div class="mt-8">
          <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Start Saving</a>
        </div>
      </div>
    </div>
    <script>
      const slider = document.getElementById('users-range');
      const count = document.getElementById('user-count');
      const amount = document.getElementById('savings-amount');
      slider.addEventListener('input', (e) => {
        const val = e.target.value;
        count.textContent = val;
        amount.textContent = val * 10;
      });
    </script>
  </div>"""
    },
    {
        "id": "cta-031",
        "title": "CTA with Map Background",
        "description": "Map background CTA",
        "dir": "templates/05-cta",
        "content": """<div class="relative py-24 bg-slate-100">
    <div class="absolute inset-0 opacity-20" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg'); background-size: cover; background-position: center;"></div>
    <div class="relative max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Available Worldwide</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-600">Join our global network of partners and customers.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Find a Partner</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-032",
        "title": "CTA with 3D Element",
        "description": "CTA with 3D visual",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24 overflow-hidden">
    <div class="max-w-7xl mx-auto px-6 lg:flex lg:items-center lg:justify-between">
      <div class="lg:w-1/2 z-10">
        <h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">Next Dimension</h2>
        <p class="mt-4 text-lg text-slate-600">Experience depth like never before.</p>
        <div class="mt-8">
          <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Enter 3D World</a>
        </div>
      </div>
      <div class="mt-10 lg:mt-0 lg:w-1/2 flex justify-center perspective-1000">
        <div class="w-64 h-64 bg-gradient-to-br from-primary-400 to-primary-600 rounded-2xl shadow-2xl transform rotate-y-12 rotate-x-12 hover:rotate-y-0 hover:rotate-x-0 transition-transform duration-500 flex items-center justify-center text-white text-4xl font-bold">
          3D
        </div>
      </div>
    </div>
    <style>
      .perspective-1000 { perspective: 1000px; }
      .rotate-y-12 { transform: rotateY(12deg); }
      .rotate-x-12 { transform: rotateX(12deg); }
    </style>
  </div>"""
    },
    {
        "id": "cta-033",
        "title": "CTA with Floating Elements",
        "description": "Animated floating elements",
        "dir": "templates/05-cta",
        "content": """<div class="relative bg-slate-900 py-24 overflow-hidden">
    <div class="absolute top-10 left-10 w-20 h-20 bg-primary-500 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob"></div>
    <div class="absolute top-10 right-10 w-20 h-20 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-2000"></div>
    <div class="absolute -bottom-8 left-20 w-20 h-20 bg-pink-500 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-4000"></div>
    <div class="relative max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Magic in the air</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-slate-300">Create stunning visuals with our design tools.</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Start Creating</a>
      </div>
    </div>
    <style>
      @keyframes blob {
        0% { transform: translate(0px, 0px) scale(1); }
        33% { transform: translate(30px, -50px) scale(1.1); }
        66% { transform: translate(-20px, 20px) scale(0.9); }
        100% { transform: translate(0px, 0px) scale(1); }
      }
      .animate-blob { animation: blob 7s infinite; }
      .animation-delay-2000 { animation-delay: 2s; }
      .animation-delay-4000 { animation-delay: 4s; }
    </style>
  </div>"""
    },
    {
        "id": "cta-034",
        "title": "CTA with Sticky Footer",
        "description": "Fixed bottom CTA",
        "dir": "templates/05-cta",
        "content": """<div class="min-h-[50vh] bg-slate-50 flex items-center justify-center">
    <p class="text-slate-500">Scroll down to see the sticky footer CTA.</p>
    <div class="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-4 shadow-lg z-50">
      <div class="max-w-7xl mx-auto px-6 flex items-center justify-between">
        <div>
          <p class="font-bold text-slate-900">Don't miss out!</p>
          <p class="text-sm text-slate-600 hidden sm:block">Get 50% off if you sign up today.</p>
        </div>
        <a href="#" class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Claim Offer</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-035",
        "title": "CTA with Sticky Header",
        "description": "Fixed top CTA bar",
        "dir": "templates/05-cta",
        "content": """<div class="min-h-[50vh] bg-slate-50 pt-16">
    <div class="fixed top-0 left-0 right-0 bg-primary-600 text-white p-3 z-50">
      <div class="max-w-7xl mx-auto px-6 flex items-center justify-center gap-4 text-sm">
        <span class="font-bold">New Feature Alert!</span>
        <span class="hidden sm:inline">Check out our latest update.</span>
        <a href="#" class="underline hover:text-primary-100">Learn more</a>
      </div>
    </div>
    <div class="flex items-center justify-center h-full">
      <p class="text-slate-500">Content goes here...</p>
    </div>
  </div>"""
    },
    {
        "id": "cta-036",
        "title": "CTA with Sidebar",
        "description": "Sidebar layout CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row gap-12">
      <div class="md:w-2/3">
        <h2 class="text-3xl font-bold text-slate-900 mb-4">Main Content</h2>
        <p class="text-slate-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
      <div class="md:w-1/3">
        <div class="bg-slate-50 p-6 rounded-xl border border-slate-200 sticky top-6">
          <h3 class="text-lg font-bold text-slate-900 mb-2">Subscribe</h3>
          <p class="text-sm text-slate-600 mb-4">Get the latest updates.</p>
          <input type="email" placeholder="Email address" class="w-full mb-3 rounded-md border-slate-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 sm:text-sm">
          <button class="w-full rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500">Subscribe</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-037",
        "title": "CTA with Overlay",
        "description": "Full screen overlay CTA",
        "dir": "templates/05-cta",
        "content": """<div class="relative h-96 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');">
    <div class="absolute inset-0 bg-black/60 flex items-center justify-center">
      <div class="text-center text-white px-6">
        <h2 class="text-4xl font-bold mb-4">Focus on what matters</h2>
        <p class="text-xl text-slate-200 mb-8">We handle the rest.</p>
        <a href="#" class="rounded-full bg-white text-slate-900 px-8 py-3 font-bold hover:bg-slate-100 transition-colors">Get Started</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-038",
        "title": "CTA with Parallax",
        "description": "Parallax background CTA",
        "dir": "templates/05-cta",
        "content": """<div class="h-96 bg-fixed bg-center bg-cover flex items-center justify-center" style="background-image: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1952&q=80');">
    <div class="bg-white/90 backdrop-blur-sm p-12 rounded-2xl text-center shadow-2xl max-w-lg mx-4">
      <h2 class="text-3xl font-bold text-slate-900 mb-4">Parallax Effect</h2>
      <p class="text-slate-600 mb-8">Create depth and immersion with fixed backgrounds.</p>
      <a href="#" class="rounded-md bg-primary-600 px-6 py-3 text-sm font-semibold text-white shadow-sm hover:bg-primary-500">Try it out</a>
    </div>
  </div>"""
    },
    {
        "id": "cta-039",
        "title": "CTA with Zoom Effect",
        "description": "Hover zoom effect CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 flex justify-center">
      <div class="group relative overflow-hidden rounded-2xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1504384308090-c54be3855463?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full max-w-2xl transition-transform duration-500 group-hover:scale-110" alt="Zoom">
        <div class="absolute inset-0 bg-black/40 flex items-center justify-center transition-opacity duration-300 group-hover:bg-black/50">
          <div class="text-center text-white">
            <h2 class="text-3xl font-bold mb-2">Explore</h2>
            <p class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 transform translate-y-4 group-hover:translate-y-0">Click to discover more</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-040",
        "title": "CTA with Hover Effect",
        "description": "Button hover animation",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-8">Interactive Buttons</h2>
      <div class="flex justify-center gap-6">
        <a href="#" class="relative px-6 py-3 font-bold text-white rounded-lg group">
          <span class="absolute inset-0 w-full h-full transition duration-300 transform -translate-x-1 -translate-y-1 bg-primary-600 ease opacity-80 group-hover:translate-x-0 group-hover:translate-y-0"></span>
          <span class="absolute inset-0 w-full h-full transition duration-300 transform translate-x-1 translate-y-1 bg-primary-800 ease opacity-80 group-hover:translate-x-0 group-hover:translate-y-0 mix-blend-screen"></span>
          <span class="relative">Hover Me</span>
        </a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-041",
        "title": "CTA with Typing Effect",
        "description": "Typewriter text effect",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-white sm:text-4xl mb-8">
        We build <span class="text-primary-500 border-r-4 border-primary-500 animate-pulse">websites</span>
      </h2>
      <a href="#" class="rounded-md bg-white px-6 py-3 text-sm font-semibold text-slate-900 shadow-sm hover:bg-slate-100">Start Project</a>
    </div>
  </div>"""
    },
    {
        "id": "cta-042",
        "title": "CTA with Particle Effect",
        "description": "Static particle background",
        "dir": "templates/05-cta",
        "content": """<div class="relative bg-black py-24 overflow-hidden">
    <div class="absolute inset-0 opacity-50">
       <div class="absolute top-1/4 left-1/4 w-2 h-2 bg-white rounded-full"></div>
       <div class="absolute top-3/4 left-1/3 w-3 h-3 bg-primary-500 rounded-full"></div>
       <div class="absolute top-1/2 right-1/4 w-2 h-2 bg-white rounded-full"></div>
       <div class="absolute bottom-1/4 right-1/3 w-4 h-4 bg-secondary-500 rounded-full"></div>
       <!-- More static 'particles' -->
    </div>
    <div class="relative max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-white sm:text-4xl">Universe of Possibilities</h2>
      <div class="mt-10">
        <a href="#" class="rounded-full border border-white text-white px-8 py-3 hover:bg-white hover:text-black transition-colors">Explore</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-043",
        "title": "CTA with Wave Effect",
        "description": "SVG wave divider",
        "dir": "templates/05-cta",
        "content": """<div class="relative bg-primary-600 pt-24 pb-48">
    <div class="max-w-7xl mx-auto px-6 text-center text-white">
      <h2 class="text-3xl font-bold sm:text-4xl">Smooth Transitions</h2>
      <p class="mt-4 text-primary-100">Use waves to create organic section breaks.</p>
    </div>
    <div class="absolute bottom-0 left-0 right-0">
      <svg class="w-full h-24 fill-white" viewBox="0 0 1440 320" preserveAspectRatio="none">
        <path fill-opacity="1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,112C672,96,768,96,864,112C960,128,1056,160,1152,160C1248,160,1344,128,1392,112L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
      </svg>
    </div>
  </div>"""
    },
    {
        "id": "cta-044",
        "title": "CTA with Blob Effect",
        "description": "Organic blob shapes",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24 overflow-hidden relative">
    <div class="absolute -left-20 top-0 w-96 h-96 bg-primary-200 rounded-full mix-blend-multiply filter blur-3xl opacity-70"></div>
    <div class="absolute -right-20 bottom-0 w-96 h-96 bg-secondary-200 rounded-full mix-blend-multiply filter blur-3xl opacity-70"></div>
    <div class="relative max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 sm:text-4xl">Organic Shapes</h2>
      <p class="mt-4 text-slate-600">Soft, friendly, and approachable design.</p>
      <div class="mt-8">
        <a href="#" class="rounded-md bg-slate-900 px-6 py-3 text-white hover:bg-slate-800">Get Started</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-045",
        "title": "CTA with Glitch Effect",
        "description": "Glitch text effect",
        "dir": "templates/05-cta",
        "content": """<div class="bg-black py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-4xl font-bold text-white relative inline-block glitch" data-text="CYBERPUNK">
        CYBERPUNK
      </h2>
      <div class="mt-10">
        <a href="#" class="border border-primary-500 text-primary-500 px-8 py-3 hover:bg-primary-500 hover:text-black transition-colors uppercase tracking-widest">Enter System</a>
      </div>
    </div>
    <style>
      .glitch { position: relative; }
      .glitch::before, .glitch::after {
        content: attr(data-text);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }
      .glitch::before {
        left: 2px;
        text-shadow: -1px 0 red;
        clip: rect(24px, 550px, 90px, 0);
        animation: glitch-anim-1 2.5s infinite linear alternate-reverse;
      }
      .glitch::after {
        left: -2px;
        text-shadow: -1px 0 blue;
        clip: rect(85px, 550px, 140px, 0);
        animation: glitch-anim-2 3s infinite linear alternate-reverse;
      }
      @keyframes glitch-anim-1 {
        0% { clip: rect(20px, 9999px, 80px, 0); }
        100% { clip: rect(50px, 9999px, 120px, 0); }
      }
      @keyframes glitch-anim-2 {
        0% { clip: rect(100px, 9999px, 150px, 0); }
        100% { clip: rect(10px, 9999px, 60px, 0); }
      }
    </style>
  </div>"""
    },
    {
        "id": "cta-046",
        "title": "CTA with Neon Effect",
        "description": "Glowing neon text/button",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-violet-500 drop-shadow-[0_0_10px_rgba(236,72,153,0.5)]">
        Neon Nights
      </h2>
      <div class="mt-12">
        <a href="#" class="px-8 py-3 rounded-lg border border-pink-500 text-pink-500 shadow-[0_0_15px_rgba(236,72,153,0.5)] hover:bg-pink-500 hover:text-white hover:shadow-[0_0_25px_rgba(236,72,153,0.8)] transition-all duration-300">
          Glow Up
        </a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-047",
        "title": "CTA with Glassmorphism",
        "description": "Frosted glass effect",
        "dir": "templates/05-cta",
        "content": """<div class="relative py-32 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1557683316-973673baf926?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white/20 backdrop-blur-lg border border-white/30 p-12 rounded-2xl shadow-xl text-center">
        <h2 class="text-3xl font-bold text-white mb-4">Glassmorphism</h2>
        <p class="text-white/90 mb-8">Modern, sleek, and beautiful.</p>
        <a href="#" class="rounded-md bg-white/30 border border-white/50 px-6 py-3 text-white font-bold hover:bg-white/40 transition-colors">Learn More</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-048",
        "title": "CTA with Neomorphism",
        "description": "Soft UI effect",
        "dir": "templates/05-cta",
        "content": """<div class="bg-slate-200 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <div class="inline-block p-12 rounded-3xl bg-slate-200 shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]">
        <h2 class="text-3xl font-bold text-slate-700 mb-8">Soft UI</h2>
        <a href="#" class="px-8 py-4 rounded-xl bg-slate-200 text-slate-700 font-bold shadow-[5px_5px_10px_#bebebe,-5px_-5px_10px_#ffffff] hover:shadow-[inset_5px_5px_10px_#bebebe,inset_-5px_-5px_10px_#ffffff] transition-shadow duration-300">
          Press Me
        </a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "cta-049",
        "title": "CTA with Retro Style",
        "description": "Retro/Pixel art style",
        "dir": "templates/05-cta",
        "content": """<div class="bg-yellow-100 py-24 font-mono">
    <div class="max-w-4xl mx-auto px-6 text-center border-4 border-black p-8 bg-white shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
      <h2 class="text-3xl font-bold text-black mb-4 uppercase">Retro Vibes</h2>
      <p class="text-black mb-8">Back to the 80s.</p>
      <a href="#" class="inline-block bg-red-500 text-white border-2 border-black px-6 py-3 font-bold shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all active:translate-x-[4px] active:translate-y-[4px] active:shadow-none">
        START GAME
      </a>
    </div>
  </div>"""
    },
    {
        "id": "cta-050",
        "title": "CTA with Minimalist Style",
        "description": "Clean and simple CTA",
        "dir": "templates/05-cta",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-4xl font-light text-slate-900 tracking-tight">Less is more.</h2>
      <div class="mt-12">
        <a href="#" class="text-slate-900 border-b border-slate-900 pb-1 hover:text-slate-600 hover:border-slate-600 transition-colors">Discover Collection</a>
      </div>
    </div>
  </div>"""
    }
]
# Part 5: Price 001-025
TEMPLATES_PRICE_1 = [
    {
        "id": "price-001",
        "title": "Simple Pricing Cards",
        "description": "Basic 3-column pricing",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900 sm:text-4xl">Simple, transparent pricing</h2>
        <p class="mt-4 text-lg text-slate-600">Choose the plan that's right for you.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Basic -->
        <div class="border border-slate-200 rounded-2xl p-8 shadow-sm hover:shadow-md transition-shadow">
          <h3 class="text-lg font-semibold text-slate-900">Basic</h3>
          <p class="mt-4 text-sm text-slate-500">Essential features for individuals.</p>
          <div class="mt-6 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900">$9</span>
            <span class="ml-1 text-slate-500">/mo</span>
          </div>
          <ul class="mt-6 space-y-4 text-sm text-slate-600">
            <li class="flex"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 5 Projects</li>
            <li class="flex"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 1GB Storage</li>
            <li class="flex"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Basic Support</li>
          </ul>
          <a href="#" class="mt-8 block w-full bg-slate-100 text-slate-900 font-semibold py-3 px-4 rounded-lg text-center hover:bg-slate-200 transition-colors">Get Started</a>
        </div>
        <!-- Pro -->
        <div class="border border-primary-200 bg-primary-50 rounded-2xl p-8 shadow-md relative">
          <div class="absolute top-0 right-0 bg-primary-600 text-white text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg">POPULAR</div>
          <h3 class="text-lg font-semibold text-primary-900">Pro</h3>
          <p class="mt-4 text-sm text-primary-700">Perfect for growing teams.</p>
          <div class="mt-6 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900">$29</span>
            <span class="ml-1 text-slate-500">/mo</span>
          </div>
          <ul class="mt-6 space-y-4 text-sm text-slate-600">
            <li class="flex"><svg class="w-5 h-5 text-primary-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited Projects</li>
            <li class="flex"><svg class="w-5 h-5 text-primary-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 10GB Storage</li>
            <li class="flex"><svg class="w-5 h-5 text-primary-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Priority Support</li>
            <li class="flex"><svg class="w-5 h-5 text-primary-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Analytics</li>
          </ul>
          <a href="#" class="mt-8 block w-full bg-primary-600 text-white font-semibold py-3 px-4 rounded-lg text-center hover:bg-primary-700 transition-colors">Get Started</a>
        </div>
        <!-- Enterprise -->
        <div class="border border-slate-200 rounded-2xl p-8 shadow-sm hover:shadow-md transition-shadow">
          <h3 class="text-lg font-semibold text-slate-900">Enterprise</h3>
          <p class="mt-4 text-sm text-slate-500">For large scale organizations.</p>
          <div class="mt-6 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900">$99</span>
            <span class="ml-1 text-slate-500">/mo</span>
          </div>
          <ul class="mt-6 space-y-4 text-sm text-slate-600">
            <li class="flex"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited Everything</li>
            <li class="flex"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Dedicated Support</li>
            <li class="flex"><svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> SSO & Security</li>
          </ul>
          <a href="#" class="mt-8 block w-full bg-slate-100 text-slate-900 font-semibold py-3 px-4 rounded-lg text-center hover:bg-slate-200 transition-colors">Contact Sales</a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-002",
        "title": "Pricing with Highlighted Plan",
        "description": "Center plan highlighted",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-white sm:text-4xl">Pricing Plans</h2>
        <p class="mt-4 text-lg text-slate-400">Flexible options for every budget.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
        <!-- Starter -->
        <div class="bg-slate-800 rounded-2xl p-8 border border-slate-700">
          <h3 class="text-xl font-semibold text-white">Starter</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-white">$0</span>
            <span class="ml-1 text-slate-400">/mo</span>
          </div>
          <p class="mt-4 text-sm text-slate-400">Forever free for individuals.</p>
          <a href="#" class="mt-8 block w-full bg-slate-700 text-white font-semibold py-3 px-4 rounded-lg text-center hover:bg-slate-600 transition-colors">Sign Up Free</a>
        </div>
        <!-- Pro (Highlighted) -->
        <div class="bg-primary-600 rounded-2xl p-10 shadow-2xl transform scale-105 border border-primary-500 relative z-10">
          <h3 class="text-xl font-semibold text-white">Professional</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-5xl font-bold text-white">$49</span>
            <span class="ml-1 text-primary-100">/mo</span>
          </div>
          <p class="mt-4 text-sm text-primary-100">Most popular choice for businesses.</p>
          <ul class="mt-8 space-y-4 text-sm text-white">
            <li class="flex items-center"><svg class="w-5 h-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> All Starter features</li>
            <li class="flex items-center"><svg class="w-5 h-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Advanced analytics</li>
            <li class="flex items-center"><svg class="w-5 h-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 24/7 Support</li>
          </ul>
          <a href="#" class="mt-8 block w-full bg-white text-primary-600 font-bold py-4 px-4 rounded-lg text-center hover:bg-slate-50 transition-colors">Get Started</a>
        </div>
        <!-- Business -->
        <div class="bg-slate-800 rounded-2xl p-8 border border-slate-700">
          <h3 class="text-xl font-semibold text-white">Business</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-white">$99</span>
            <span class="ml-1 text-slate-400">/mo</span>
          </div>
          <p class="mt-4 text-sm text-slate-400">For scaling teams and agencies.</p>
          <a href="#" class="mt-8 block w-full bg-slate-700 text-white font-semibold py-3 px-4 rounded-lg text-center hover:bg-slate-600 transition-colors">Contact Sales</a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-003",
        "title": "Pricing with Toggle",
        "description": "Monthly/Yearly toggle",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24" x-data="{ annual: false }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900 sm:text-4xl">Simple Pricing</h2>
        <div class="mt-6 flex items-center justify-center gap-4">
          <span class="text-sm font-medium" :class="!annual ? 'text-slate-900' : 'text-slate-500'">Monthly</span>
          <button type="button" class="relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-primary-600 focus:ring-offset-2" :class="annual ? 'bg-primary-600' : 'bg-slate-200'" @click="annual = !annual">
            <span class="sr-only">Use setting</span>
            <span aria-hidden="true" class="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out" :class="annual ? 'translate-x-5' : 'translate-x-0'"></span>
          </button>
          <span class="text-sm font-medium" :class="annual ? 'text-slate-900' : 'text-slate-500'">Yearly <span class="text-primary-600 font-bold">(-20%)</span></span>
        </div>
      </div>

      <!-- Alpine.js is required for interactivity, adding script here for standalone template -->
      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Plan 1 -->
        <div class="border border-slate-200 rounded-2xl p-8">
          <h3 class="text-lg font-semibold text-slate-900">Freelancer</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900" x-text="annual ? '$12' : '$15'">$15</span>
            <span class="ml-1 text-slate-500">/mo</span>
          </div>
          <p class="mt-2 text-sm text-slate-500" x-show="annual">Billed $144 yearly</p>
          <a href="#" class="mt-8 block w-full bg-slate-900 text-white font-semibold py-3 px-4 rounded-lg text-center hover:bg-slate-800">Buy Now</a>
        </div>
        <!-- Plan 2 -->
        <div class="border border-primary-500 ring-2 ring-primary-500 rounded-2xl p-8">
          <h3 class="text-lg font-semibold text-slate-900">Startup</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900" x-text="annual ? '$39' : '$49'">$49</span>
            <span class="ml-1 text-slate-500">/mo</span>
          </div>
          <p class="mt-2 text-sm text-slate-500" x-show="annual">Billed $468 yearly</p>
          <a href="#" class="mt-8 block w-full bg-primary-600 text-white font-semibold py-3 px-4 rounded-lg text-center hover:bg-primary-700">Buy Now</a>
        </div>
        <!-- Plan 3 -->
        <div class="border border-slate-200 rounded-2xl p-8">
          <h3 class="text-lg font-semibold text-slate-900">Enterprise</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900" x-text="annual ? '$79' : '$99'">$99</span>
            <span class="ml-1 text-slate-500">/mo</span>
          </div>
          <p class="mt-2 text-sm text-slate-500" x-show="annual">Billed $948 yearly</p>
          <a href="#" class="mt-8 block w-full bg-slate-900 text-white font-semibold py-3 px-4 rounded-lg text-center hover:bg-slate-800">Buy Now</a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-004",
        "title": "Pricing Table",
        "description": "Detailed feature comparison table",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Compare Plans</h2>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr>
              <th class="p-4 border-b-2 border-slate-100 min-w-[200px]"></th>
              <th class="p-4 border-b-2 border-slate-100 min-w-[150px] text-center">
                <div class="text-lg font-bold text-slate-900">Basic</div>
                <div class="text-2xl font-bold mt-2">$19</div>
              </th>
              <th class="p-4 border-b-2 border-primary-600 min-w-[150px] text-center bg-primary-50 rounded-t-xl">
                <div class="text-lg font-bold text-primary-700">Pro</div>
                <div class="text-2xl font-bold mt-2 text-primary-700">$49</div>
              </th>
              <th class="p-4 border-b-2 border-slate-100 min-w-[150px] text-center">
                <div class="text-lg font-bold text-slate-900">Enterprise</div>
                <div class="text-2xl font-bold mt-2">$99</div>
              </th>
            </tr>
          </thead>
          <tbody class="text-sm text-slate-600">
            <tr>
              <td class="p-4 border-b border-slate-100 font-medium">Users</td>
              <td class="p-4 border-b border-slate-100 text-center">1</td>
              <td class="p-4 border-b border-slate-100 text-center bg-primary-50/30 font-bold text-slate-900">5</td>
              <td class="p-4 border-b border-slate-100 text-center">Unlimited</td>
            </tr>
            <tr>
              <td class="p-4 border-b border-slate-100 font-medium">Storage</td>
              <td class="p-4 border-b border-slate-100 text-center">5GB</td>
              <td class="p-4 border-b border-slate-100 text-center bg-primary-50/30 font-bold text-slate-900">50GB</td>
              <td class="p-4 border-b border-slate-100 text-center">1TB</td>
            </tr>
            <tr>
              <td class="p-4 border-b border-slate-100 font-medium">API Access</td>
              <td class="p-4 border-b border-slate-100 text-center text-slate-300">
                <svg class="w-5 h-5 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
              </td>
              <td class="p-4 border-b border-slate-100 text-center bg-primary-50/30 text-green-500">
                <svg class="w-5 h-5 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
              </td>
              <td class="p-4 border-b border-slate-100 text-center text-green-500">
                <svg class="w-5 h-5 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
              </td>
            </tr>
            <tr>
              <td class="p-4 font-medium">Support</td>
              <td class="p-4 text-center">Email</td>
              <td class="p-4 text-center bg-primary-50/30 font-bold text-slate-900">Priority Email</td>
              <td class="p-4 text-center">24/7 Phone</td>
            </tr>
            <tr>
              <td class="p-4"></td>
              <td class="p-4 text-center"><button class="px-4 py-2 rounded-lg border border-slate-300 hover:bg-slate-50">Choose</button></td>
              <td class="p-4 text-center bg-primary-50/30 rounded-b-xl"><button class="px-4 py-2 rounded-lg bg-primary-600 text-white hover:bg-primary-700">Choose</button></td>
              <td class="p-4 text-center"><button class="px-4 py-2 rounded-lg border border-slate-300 hover:bg-slate-50">Choose</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-005",
        "title": "Pricing with Feature Comparison",
        "description": "Cards with detailed feature lists",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <div class="bg-white rounded-2xl shadow-lg p-8">
          <h3 class="text-2xl font-bold text-slate-900">Standard</h3>
          <p class="mt-2 text-slate-600">For small teams and startups.</p>
          <div class="mt-6 text-4xl font-bold text-slate-900">$29<span class="text-base font-normal text-slate-500">/mo</span></div>
          <a href="#" class="mt-8 block w-full bg-slate-100 text-slate-900 font-bold py-3 rounded-lg text-center hover:bg-slate-200">Get Standard</a>
          <div class="mt-8">
            <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wide">Features</h4>
            <ul class="mt-4 space-y-3">
              <li class="flex items-center text-slate-600"><svg class="w-5 h-5 text-green-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Up to 5 users</li>
              <li class="flex items-center text-slate-600"><svg class="w-5 h-5 text-green-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Basic analytics</li>
              <li class="flex items-center text-slate-600"><svg class="w-5 h-5 text-green-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 24-hour support response</li>
            </ul>
          </div>
        </div>
        <div class="bg-slate-900 rounded-2xl shadow-lg p-8 text-white">
          <h3 class="text-2xl font-bold">Premium</h3>
          <p class="mt-2 text-slate-400">For growing businesses.</p>
          <div class="mt-6 text-4xl font-bold">$79<span class="text-base font-normal text-slate-400">/mo</span></div>
          <a href="#" class="mt-8 block w-full bg-primary-600 text-white font-bold py-3 rounded-lg text-center hover:bg-primary-500">Get Premium</a>
          <div class="mt-8">
            <h4 class="text-sm font-bold text-slate-400 uppercase tracking-wide">Everything in Standard, plus:</h4>
            <ul class="mt-4 space-y-3">
              <li class="flex items-center text-slate-300"><svg class="w-5 h-5 text-primary-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited users</li>
              <li class="flex items-center text-slate-300"><svg class="w-5 h-5 text-primary-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Advanced reporting</li>
              <li class="flex items-center text-slate-300"><svg class="w-5 h-5 text-primary-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 1-hour support response</li>
              <li class="flex items-center text-slate-300"><svg class="w-5 h-5 text-primary-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Custom integrations</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-006",
        "title": "Single Plan Pricing",
        "description": "Focus on one main plan",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 sm:text-4xl">One simple price</h2>
      <p class="mt-4 text-lg text-slate-600">Everything you need to grow your business.</p>

      <div class="mt-12 bg-slate-50 rounded-3xl p-8 border border-slate-200 shadow-sm">
        <div class="flex items-center justify-center gap-2">
          <span class="text-6xl font-bold text-slate-900">$49</span>
          <span class="text-xl text-slate-500">/month</span>
        </div>
        <p class="mt-4 text-slate-600">Includes all features, unlimited users, and priority support.</p>
        <div class="mt-8">
          <a href="#" class="inline-block bg-primary-600 text-white font-bold py-4 px-8 rounded-full hover:bg-primary-700 transition-colors shadow-lg hover:shadow-xl">Start 14-Day Free Trial</a>
        </div>
        <p class="mt-4 text-sm text-slate-500">No credit card required.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-007",
        "title": "Pricing with Badges",
        "description": "Plans with feature badges",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <!-- Basic -->
      <div class="bg-white rounded-xl shadow-sm p-6 border border-slate-100">
        <div class="inline-block px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-bold mb-4">BASIC</div>
        <h3 class="text-2xl font-bold text-slate-900">$19</h3>
        <p class="text-slate-500 text-sm mb-6">Per user/month</p>
        <a href="#" class="block w-full py-2 px-4 border border-slate-300 rounded-lg text-center text-slate-700 hover:bg-slate-50 font-medium">Select Plan</a>
      </div>
      <!-- Pro -->
      <div class="bg-white rounded-xl shadow-md p-6 border-2 border-primary-500 relative">
        <div class="inline-block px-3 py-1 rounded-full bg-primary-100 text-primary-700 text-xs font-bold mb-4">RECOMMENDED</div>
        <h3 class="text-2xl font-bold text-slate-900">$49</h3>
        <p class="text-slate-500 text-sm mb-6">Per user/month</p>
        <a href="#" class="block w-full py-2 px-4 bg-primary-600 rounded-lg text-center text-white hover:bg-primary-700 font-medium">Select Plan</a>
      </div>
      <!-- Enterprise -->
      <div class="bg-white rounded-xl shadow-sm p-6 border border-slate-100">
        <div class="inline-block px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-xs font-bold mb-4">ENTERPRISE</div>
        <h3 class="text-2xl font-bold text-slate-900">$99</h3>
        <p class="text-slate-500 text-sm mb-6">Per user/month</p>
        <a href="#" class="block w-full py-2 px-4 border border-slate-300 rounded-lg text-center text-slate-700 hover:bg-slate-50 font-medium">Select Plan</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-008",
        "title": "Pricing with Slider",
        "description": "Interactive pricing slider",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24" x-data="{ users: 10, pricePerUser: 15 }">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-12">Scale with your team</h2>

      <!-- Alpine.js required -->
      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="bg-slate-50 p-10 rounded-3xl border border-slate-200">
        <div class="flex items-center justify-between mb-8">
          <div class="text-left">
            <p class="text-sm font-bold text-slate-500 uppercase">Team Size</p>
            <p class="text-3xl font-bold text-slate-900"><span x-text="users">10</span> Users</p>
          </div>
          <div class="text-right">
            <p class="text-sm font-bold text-slate-500 uppercase">Estimated Cost</p>
            <p class="text-3xl font-bold text-primary-600">$<span x-text="users * pricePerUser">150</span><span class="text-lg text-slate-400 font-normal">/mo</span></p>
          </div>
        </div>

        <input type="range" min="1" max="100" x-model="users" class="w-full h-3 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary-600">

        <div class="mt-12">
          <a href="#" class="inline-block bg-slate-900 text-white font-bold py-3 px-8 rounded-lg hover:bg-slate-800">Start Free Trial</a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-009",
        "title": "Dark Mode Pricing",
        "description": "Dark themed pricing",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-black py-24 text-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">Transparent Pricing</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-slate-900 p-8 rounded-2xl border border-slate-800">
          <h3 class="text-xl font-bold">Hobby</h3>
          <div class="my-6 text-4xl font-bold">$0</div>
          <ul class="space-y-3 text-slate-400 text-sm mb-8">
            <li>Feature 1</li>
            <li>Feature 2</li>
          </ul>
          <button class="w-full py-3 rounded-lg border border-slate-700 hover:bg-slate-800">Join</button>
        </div>
        <div class="bg-slate-900 p-8 rounded-2xl border border-primary-500 shadow-[0_0_30px_rgba(var(--color-primary-500),0.3)]">
          <h3 class="text-xl font-bold text-primary-400">Pro</h3>
          <div class="my-6 text-4xl font-bold">$29</div>
          <ul class="space-y-3 text-slate-300 text-sm mb-8">
            <li>Everything in Hobby</li>
            <li>Feature 3</li>
            <li>Feature 4</li>
          </ul>
          <button class="w-full py-3 rounded-lg bg-primary-600 hover:bg-primary-500 font-bold">Join Pro</button>
        </div>
        <div class="bg-slate-900 p-8 rounded-2xl border border-slate-800">
          <h3 class="text-xl font-bold">Team</h3>
          <div class="my-6 text-4xl font-bold">$99</div>
          <ul class="space-y-3 text-slate-400 text-sm mb-8">
            <li>Everything in Pro</li>
            <li>Feature 5</li>
          </ul>
          <button class="w-full py-3 rounded-lg border border-slate-700 hover:bg-slate-800">Contact</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-010",
        "title": "Pricing with FAQ",
        "description": "Pricing cards + FAQ section",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 mb-24">
        <div class="border border-slate-200 p-8 rounded-2xl">
          <h3 class="text-2xl font-bold text-slate-900">Monthly</h3>
          <p class="text-4xl font-bold mt-4">$29<span class="text-base font-normal text-slate-500">/mo</span></p>
          <button class="mt-8 w-full bg-slate-100 py-3 rounded-lg font-bold text-slate-900">Choose Monthly</button>
        </div>
        <div class="border border-primary-200 bg-primary-50 p-8 rounded-2xl">
          <h3 class="text-2xl font-bold text-primary-900">Yearly</h3>
          <p class="text-4xl font-bold mt-4 text-primary-900">$290<span class="text-base font-normal text-primary-700">/yr</span></p>
          <p class="text-sm text-green-600 font-bold mt-1">Save 2 months</p>
          <button class="mt-7 w-full bg-primary-600 py-3 rounded-lg font-bold text-white">Choose Yearly</button>
        </div>
      </div>

      <div class="max-w-3xl mx-auto">
        <h3 class="text-2xl font-bold text-slate-900 mb-8 text-center">Frequently Asked Questions</h3>
        <div class="space-y-6">
          <div>
            <h4 class="font-bold text-slate-900">Can I cancel anytime?</h4>
            <p class="mt-2 text-slate-600">Yes, you can cancel your subscription at any time. You will continue to have access until the end of your billing period.</p>
          </div>
          <div>
            <h4 class="font-bold text-slate-900">Do you offer refunds?</h4>
            <p class="mt-2 text-slate-600">We offer a 30-day money-back guarantee for all new subscriptions.</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-011",
        "title": "Pricing with Checkmarks",
        "description": "List style pricing",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-5xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-xl overflow-hidden">
        <div class="grid grid-cols-1 md:grid-cols-2">
          <div class="p-12 bg-slate-900 text-white flex flex-col justify-center">
            <h3 class="text-3xl font-bold">Lifetime Access</h3>
            <p class="mt-4 text-slate-300">Pay once, own it forever.</p>
            <div class="mt-8 text-5xl font-bold">$149</div>
            <button class="mt-8 bg-white text-slate-900 font-bold py-3 px-6 rounded-lg hover:bg-slate-100">Get Access Now</button>
          </div>
          <div class="p-12 bg-white">
            <h4 class="text-lg font-bold text-slate-900 mb-6">What's included:</h4>
            <ul class="space-y-4">
              <li class="flex items-start">
                <svg class="w-6 h-6 text-green-500 mr-3 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span class="text-slate-600">Unlimited updates</span>
              </li>
              <li class="flex items-start">
                <svg class="w-6 h-6 text-green-500 mr-3 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span class="text-slate-600">Access to community</span>
              </li>
              <li class="flex items-start">
                <svg class="w-6 h-6 text-green-500 mr-3 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span class="text-slate-600">Premium support</span>
              </li>
              <li class="flex items-start">
                <svg class="w-6 h-6 text-green-500 mr-3 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span class="text-slate-600">Commercial license</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-012",
        "title": "Pricing with Gradient",
        "description": "Gradient border/background",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative p-1 rounded-3xl bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500">
        <div class="bg-white rounded-[20px] p-12 text-center">
          <h3 class="text-sm font-bold tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-yellow-500 uppercase mb-4">Special Offer</h3>
          <h2 class="text-4xl font-bold text-slate-900 mb-6">All-Access Pass</h2>
          <div class="text-6xl font-bold text-slate-900 mb-8">$299</div>
          <p class="text-lg text-slate-600 mb-10 max-w-xl mx-auto">Get access to our entire library of resources, plus all future updates for one low price.</p>
          <button class="bg-gradient-to-r from-pink-500 to-yellow-500 text-white font-bold py-4 px-10 rounded-full hover:shadow-lg hover:scale-105 transition-transform">Unlock Everything</button>
        </div>
      </div>
    </div>
  </div>"""
    }
]
# Placeholder for Price 013-025
# Part 5 continued: Price 013-025
TEMPLATES_PRICE_1_PART_2 = [
    {
        "id": "price-013",
        "title": "Pricing with Hover Effects",
        "description": "Cards scale on hover",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Interactive Pricing</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 border border-slate-100">
          <h3 class="text-xl font-bold text-slate-900">Basic</h3>
          <div class="my-6 text-4xl font-bold text-slate-900">$19</div>
          <ul class="space-y-3 text-slate-600 mb-8">
            <li>Feature A</li>
            <li>Feature B</li>
          </ul>
          <button class="w-full py-3 rounded-lg border border-slate-200 hover:bg-slate-50 font-bold transition-colors">Select</button>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 border border-slate-100">
          <h3 class="text-xl font-bold text-slate-900">Pro</h3>
          <div class="my-6 text-4xl font-bold text-slate-900">$49</div>
          <ul class="space-y-3 text-slate-600 mb-8">
            <li>Feature A</li>
            <li>Feature B</li>
            <li>Feature C</li>
          </ul>
          <button class="w-full py-3 rounded-lg bg-primary-600 text-white hover:bg-primary-700 font-bold transition-colors">Select</button>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 border border-slate-100">
          <h3 class="text-xl font-bold text-slate-900">Enterprise</h3>
          <div class="my-6 text-4xl font-bold text-slate-900">$99</div>
          <ul class="space-y-3 text-slate-600 mb-8">
            <li>All Features</li>
            <li>Priority Support</li>
          </ul>
          <button class="w-full py-3 rounded-lg border border-slate-200 hover:bg-slate-50 font-bold transition-colors">Select</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-014",
        "title": "Pricing with Annual Savings",
        "description": "Highlight annual savings",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Save with Annual Billing</h2>
        <p class="mt-4 text-green-600 font-bold">Get 2 months free when you pay annually!</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="border border-slate-200 rounded-2xl p-8 relative overflow-hidden">
          <h3 class="text-lg font-bold text-slate-900">Starter</h3>
          <div class="mt-4">
            <span class="text-3xl font-bold text-slate-900">$10</span>
            <span class="text-slate-500">/mo</span>
          </div>
          <div class="mt-2 text-sm text-slate-500">Billed $100 yearly</div>
          <div class="mt-2 text-xs font-bold text-green-600 bg-green-50 inline-block px-2 py-1 rounded">Save $20</div>
          <button class="mt-8 w-full py-2 border border-slate-300 rounded-lg hover:bg-slate-50">Choose Starter</button>
        </div>
        <div class="border border-primary-500 rounded-2xl p-8 relative overflow-hidden ring-1 ring-primary-500">
          <h3 class="text-lg font-bold text-slate-900">Growth</h3>
          <div class="mt-4">
            <span class="text-3xl font-bold text-slate-900">$25</span>
            <span class="text-slate-500">/mo</span>
          </div>
          <div class="mt-2 text-sm text-slate-500">Billed $250 yearly</div>
          <div class="mt-2 text-xs font-bold text-green-600 bg-green-50 inline-block px-2 py-1 rounded">Save $50</div>
          <button class="mt-8 w-full py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700">Choose Growth</button>
        </div>
        <div class="border border-slate-200 rounded-2xl p-8 relative overflow-hidden">
          <h3 class="text-lg font-bold text-slate-900">Scale</h3>
          <div class="mt-4">
            <span class="text-3xl font-bold text-slate-900">$50</span>
            <span class="text-slate-500">/mo</span>
          </div>
          <div class="mt-2 text-sm text-slate-500">Billed $500 yearly</div>
          <div class="mt-2 text-xs font-bold text-green-600 bg-green-50 inline-block px-2 py-1 rounded">Save $100</div>
          <button class="mt-8 w-full py-2 border border-slate-300 rounded-lg hover:bg-slate-50">Choose Scale</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-015",
        "title": "Pricing with Custom Icons",
        "description": "Plans with illustrative icons",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-2xl shadow-sm text-center">
        <div class="w-16 h-16 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Personal</h3>
        <p class="text-slate-500 mt-2">For hobbyists.</p>
        <div class="text-3xl font-bold text-slate-900 mt-4">$5</div>
        <button class="mt-6 w-full py-2 bg-blue-50 text-blue-600 font-bold rounded-lg hover:bg-blue-100">Start</button>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm text-center border-t-4 border-primary-500">
        <div class="w-16 h-16 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Professional</h3>
        <p class="text-slate-500 mt-2">For experts.</p>
        <div class="text-3xl font-bold text-slate-900 mt-4">$25</div>
        <button class="mt-6 w-full py-2 bg-primary-600 text-white font-bold rounded-lg hover:bg-primary-700">Start</button>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm text-center">
        <div class="w-16 h-16 bg-purple-100 text-purple-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Business</h3>
        <p class="text-slate-500 mt-2">For teams.</p>
        <div class="text-3xl font-bold text-slate-900 mt-4">$50</div>
        <button class="mt-6 w-full py-2 bg-purple-50 text-purple-600 font-bold rounded-lg hover:bg-purple-100">Start</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-016",
        "title": "Pricing with Background Image",
        "description": "Pricing over image background",
        "dir": "templates/06-pricing",
        "content": """<div class="relative py-24 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');">
    <div class="absolute inset-0 bg-slate-900/80"></div>
    <div class="relative max-w-7xl mx-auto px-6">
      <div class="text-center mb-16 text-white">
        <h2 class="text-3xl font-bold">Premium Plans</h2>
        <p class="mt-4 text-slate-300">Unlock your full potential.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white/10 backdrop-blur-md border border-white/20 p-8 rounded-2xl text-white">
          <h3 class="text-xl font-bold">Silver</h3>
          <div class="my-4 text-4xl font-bold">$29</div>
          <button class="w-full py-3 bg-white/20 hover:bg-white/30 rounded-lg font-bold transition-colors">Choose</button>
        </div>
        <div class="bg-primary-600/90 backdrop-blur-md border border-primary-500 p-8 rounded-2xl text-white transform scale-105 shadow-2xl">
          <h3 class="text-xl font-bold">Gold</h3>
          <div class="my-4 text-4xl font-bold">$59</div>
          <button class="w-full py-3 bg-white text-primary-600 hover:bg-slate-100 rounded-lg font-bold transition-colors">Choose</button>
        </div>
        <div class="bg-white/10 backdrop-blur-md border border-white/20 p-8 rounded-2xl text-white">
          <h3 class="text-xl font-bold">Platinum</h3>
          <div class="my-4 text-4xl font-bold">$99</div>
          <button class="w-full py-3 bg-white/20 hover:bg-white/30 rounded-lg font-bold transition-colors">Choose</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-017",
        "title": "Pricing with Floating Cards",
        "description": "Overlapping cards layout",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 pt-24 pb-48">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900">Choose your plan</h2>
      <p class="mt-4 text-slate-600 max-w-2xl mx-auto">Start small and upgrade as you grow.</p>
    </div>
  </div>
  <div class="max-w-7xl mx-auto px-6 -mt-32 pb-24">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-slate-300">
        <h3 class="text-xl font-bold text-slate-900">Basic</h3>
        <p class="text-3xl font-bold mt-4">$19</p>
        <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-xl border-t-4 border-primary-600 transform -translate-y-4">
        <h3 class="text-xl font-bold text-slate-900">Pro</h3>
        <p class="text-3xl font-bold mt-4">$49</p>
        <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Select</button>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-slate-300">
        <h3 class="text-xl font-bold text-slate-900">Expert</h3>
        <p class="text-3xl font-bold mt-4">$99</p>
        <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-018",
        "title": "Pricing with Tooltips",
        "description": "Features with info tooltips",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6">
      <div class="border border-slate-200 rounded-2xl overflow-hidden">
        <div class="bg-slate-50 p-6 border-b border-slate-200 text-center">
          <h3 class="text-2xl font-bold text-slate-900">Standard Plan</h3>
          <div class="text-4xl font-bold mt-2">$29</div>
        </div>
        <div class="p-8">
          <ul class="space-y-4">
            <li class="flex items-center justify-between">
              <span class="flex items-center">
                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                API Requests
              </span>
              <div class="relative group cursor-help">
                <svg class="w-5 h-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <div class="absolute bottom-full right-0 mb-2 w-48 bg-slate-800 text-white text-xs rounded p-2 hidden group-hover:block z-10">
                  10,000 requests per month included.
                </div>
              </div>
            </li>
            <li class="flex items-center justify-between">
              <span class="flex items-center">
                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                Data Retention
              </span>
              <div class="relative group cursor-help">
                <svg class="w-5 h-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <div class="absolute bottom-full right-0 mb-2 w-48 bg-slate-800 text-white text-xs rounded p-2 hidden group-hover:block z-10">
                  30 days of data history.
                </div>
              </div>
            </li>
          </ul>
          <button class="mt-8 w-full bg-primary-600 text-white py-3 rounded-lg font-bold hover:bg-primary-700">Subscribe</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-019",
        "title": "Pricing with Comparison Toggle",
        "description": "Toggle between different plan types",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24" x-data="{ type: 'personal' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex justify-center mb-12">
        <div class="bg-white p-1 rounded-lg border border-slate-200 inline-flex">
          <button class="px-6 py-2 rounded-md text-sm font-medium transition-colors" :class="type === 'personal' ? 'bg-slate-900 text-white' : 'text-slate-600 hover:text-slate-900'" @click="type = 'personal'">Personal</button>
          <button class="px-6 py-2 rounded-md text-sm font-medium transition-colors" :class="type === 'business' ? 'bg-slate-900 text-white' : 'text-slate-600 hover:text-slate-900'" @click="type = 'business'">Business</button>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Plan 1 -->
        <div class="bg-white p-8 rounded-2xl shadow-sm">
          <h3 class="text-xl font-bold text-slate-900">Tier 1</h3>
          <div class="mt-4 text-3xl font-bold" x-text="type === 'personal' ? '$0' : '$49'">$0</div>
          <p class="text-slate-500 text-sm mt-1">per month</p>
          <button class="mt-6 w-full py-2 border border-slate-200 rounded-lg hover:bg-slate-50">Select</button>
        </div>
        <!-- Plan 2 -->
        <div class="bg-white p-8 rounded-2xl shadow-md border border-primary-100">
          <h3 class="text-xl font-bold text-slate-900">Tier 2</h3>
          <div class="mt-4 text-3xl font-bold" x-text="type === 'personal' ? '$15' : '$99'">$15</div>
          <p class="text-slate-500 text-sm mt-1">per month</p>
          <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700">Select</button>
        </div>
        <!-- Plan 3 -->
        <div class="bg-white p-8 rounded-2xl shadow-sm">
          <h3 class="text-xl font-bold text-slate-900">Tier 3</h3>
          <div class="mt-4 text-3xl font-bold" x-text="type === 'personal' ? '$30' : '$299'">$30</div>
          <p class="text-slate-500 text-sm mt-1">per month</p>
          <button class="mt-6 w-full py-2 border border-slate-200 rounded-lg hover:bg-slate-50">Select</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-020",
        "title": "Pricing with Discount Badge",
        "description": "Discount badge on card",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12">
      <div class="border border-slate-200 rounded-2xl p-8">
        <h3 class="text-2xl font-bold text-slate-900">Regular</h3>
        <div class="mt-4 text-4xl font-bold">$49</div>
        <button class="mt-8 w-full py-3 border border-slate-300 rounded-lg hover:bg-slate-50">Choose Regular</button>
      </div>
      <div class="border-2 border-red-500 rounded-2xl p-8 relative">
        <div class="absolute -top-4 right-8 bg-red-500 text-white px-3 py-1 rounded-full text-sm font-bold shadow-sm">SAVE 50%</div>
        <h3 class="text-2xl font-bold text-slate-900">Special</h3>
        <div class="mt-4 flex items-baseline gap-2">
          <span class="text-4xl font-bold text-red-600">$24.50</span>
          <span class="text-xl text-slate-400 line-through">$49</span>
        </div>
        <p class="text-sm text-red-600 mt-2 font-medium">Limited time offer!</p>
        <button class="mt-6 w-full py-3 bg-red-600 text-white rounded-lg hover:bg-red-700 font-bold">Claim Offer</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-021",
        "title": "Pricing with Minimalist Design",
        "description": "Clean, whitespace-heavy pricing",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-slate-200 border border-slate-200 rounded-lg overflow-hidden">
        <div class="bg-white p-12 text-center hover:bg-slate-50 transition-colors">
          <h3 class="font-bold text-slate-900 uppercase tracking-widest text-sm">Basic</h3>
          <div class="mt-6 text-5xl font-light text-slate-900">$10</div>
          <p class="mt-6 text-slate-500 leading-relaxed">Essential features for starters.</p>
          <a href="#" class="mt-8 inline-block text-primary-600 font-bold hover:text-primary-700">Get Started &rarr;</a>
        </div>
        <div class="bg-white p-12 text-center hover:bg-slate-50 transition-colors">
          <h3 class="font-bold text-slate-900 uppercase tracking-widest text-sm">Pro</h3>
          <div class="mt-6 text-5xl font-light text-slate-900">$20</div>
          <p class="mt-6 text-slate-500 leading-relaxed">Advanced tools for professionals.</p>
          <a href="#" class="mt-8 inline-block text-primary-600 font-bold hover:text-primary-700">Get Started &rarr;</a>
        </div>
        <div class="bg-white p-12 text-center hover:bg-slate-50 transition-colors">
          <h3 class="font-bold text-slate-900 uppercase tracking-widest text-sm">Max</h3>
          <div class="mt-6 text-5xl font-light text-slate-900">$30</div>
          <p class="mt-6 text-slate-500 leading-relaxed">Complete suite for enterprises.</p>
          <a href="#" class="mt-8 inline-block text-primary-600 font-bold hover:text-primary-700">Get Started &rarr;</a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-022",
        "title": "Pricing with Bold Typography",
        "description": "Large fonts and strong contrast",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-900 py-24 text-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-5xl font-black tracking-tight mb-6">PRICING<br>PLANS</h2>
        <p class="text-xl text-slate-400">Choose the power you need.</p>
      </div>
      <div class="space-y-6">
        <div class="bg-slate-800 p-6 flex items-center justify-between rounded-lg border border-slate-700 hover:border-white transition-colors cursor-pointer group">
          <div>
            <h3 class="text-2xl font-bold group-hover:text-primary-400 transition-colors">Lite</h3>
            <p class="text-slate-400">Basic access</p>
          </div>
          <div class="text-3xl font-bold">$9</div>
        </div>
        <div class="bg-slate-800 p-6 flex items-center justify-between rounded-lg border border-slate-700 hover:border-white transition-colors cursor-pointer group">
          <div>
            <h3 class="text-2xl font-bold group-hover:text-primary-400 transition-colors">Pro</h3>
            <p class="text-slate-400">Full access</p>
          </div>
          <div class="text-3xl font-bold">$29</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-023",
        "title": "Pricing with Soft Shadows",
        "description": "Elegant soft shadow design",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="bg-white rounded-[2rem] p-8 shadow-[0_20px_50px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.1)] transition-shadow">
        <h3 class="text-xl font-bold text-slate-900">Start</h3>
        <div class="mt-4 text-4xl font-bold text-slate-900">$19</div>
        <button class="mt-8 w-full py-3 rounded-xl bg-slate-100 text-slate-900 font-bold hover:bg-slate-200">Join</button>
      </div>
      <div class="bg-white rounded-[2rem] p-8 shadow-[0_20px_50px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.1)] transition-shadow relative z-10">
        <h3 class="text-xl font-bold text-slate-900">Grow</h3>
        <div class="mt-4 text-4xl font-bold text-primary-600">$49</div>
        <button class="mt-8 w-full py-3 rounded-xl bg-primary-600 text-white font-bold hover:bg-primary-700 shadow-lg shadow-primary-600/30">Join</button>
      </div>
      <div class="bg-white rounded-[2rem] p-8 shadow-[0_20px_50px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.1)] transition-shadow">
        <h3 class="text-xl font-bold text-slate-900">Scale</h3>
        <div class="mt-4 text-4xl font-bold text-slate-900">$99</div>
        <button class="mt-8 w-full py-3 rounded-xl bg-slate-100 text-slate-900 font-bold hover:bg-slate-200">Join</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-024",
        "title": "Pricing with Border Accent",
        "description": "Top border accent cards",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white shadow-lg rounded-lg overflow-hidden border-t-4 border-slate-300">
        <div class="p-8">
          <h3 class="text-xl font-bold text-slate-900">Basic</h3>
          <div class="mt-4 text-3xl font-bold">$29</div>
          <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Choose</button>
        </div>
      </div>
      <div class="bg-white shadow-xl rounded-lg overflow-hidden border-t-4 border-primary-600 transform scale-105">
        <div class="p-8">
          <h3 class="text-xl font-bold text-slate-900">Pro</h3>
          <div class="mt-4 text-3xl font-bold">$59</div>
          <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Choose</button>
        </div>
      </div>
      <div class="bg-white shadow-lg rounded-lg overflow-hidden border-t-4 border-slate-300">
        <div class="p-8">
          <h3 class="text-xl font-bold text-slate-900">Enterprise</h3>
          <div class="mt-4 text-3xl font-bold">$99</div>
          <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Choose</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-025",
        "title": "Pricing with Grid Layout",
        "description": "Grid of features",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="grid grid-cols-1 md:grid-cols-4 divide-y md:divide-y-0 md:divide-x divide-slate-200">
          <div class="p-8 text-center bg-slate-50 md:bg-white flex flex-col justify-center">
            <h3 class="text-2xl font-bold text-slate-900">All Plans Include</h3>
          </div>
          <div class="p-8 text-center">
            <h4 class="font-bold text-slate-900">Starter</h4>
            <div class="text-2xl font-bold mt-2">$19</div>
            <ul class="mt-6 space-y-2 text-sm text-slate-600">
              <li>Feature 1</li>
              <li>Feature 2</li>
            </ul>
            <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Buy</button>
          </div>
          <div class="p-8 text-center bg-primary-50/30">
            <h4 class="font-bold text-primary-700">Growth</h4>
            <div class="text-2xl font-bold mt-2 text-primary-700">$49</div>
            <ul class="mt-6 space-y-2 text-sm text-slate-600">
              <li>Everything in Starter</li>
              <li>Feature 3</li>
            </ul>
            <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Buy</button>
          </div>
          <div class="p-8 text-center">
            <h4 class="font-bold text-slate-900">Scale</h4>
            <div class="text-2xl font-bold mt-2">$99</div>
            <ul class="mt-6 space-y-2 text-sm text-slate-600">
              <li>Everything in Growth</li>
              <li>Feature 4</li>
            </ul>
            <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Buy</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
# Part 6: Price 026-050
TEMPLATES_PRICE_2 = [
    {
        "id": "price-026",
        "title": "Pricing with Currency Toggle",
        "description": "Switch between currencies",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24" x-data="{ currency: 'USD', rate: 1 }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900">Global Pricing</h2>
        <div class="mt-6 inline-flex bg-slate-100 p-1 rounded-lg">
          <button class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="currency === 'USD' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-900'" @click="currency = 'USD'; rate = 1">USD</button>
          <button class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="currency === 'EUR' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-900'" @click="currency = 'EUR'; rate = 0.92">EUR</button>
          <button class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="currency === 'GBP' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-900'" @click="currency = 'GBP'; rate = 0.79">GBP</button>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="border border-slate-200 rounded-2xl p-8">
          <h3 class="text-lg font-bold text-slate-900">Basic</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900" x-text="currency === 'USD' ? '$' : (currency === 'EUR' ? '€' : '£')"></span>
            <span class="text-4xl font-bold text-slate-900" x-text="Math.round(10 * rate)">10</span>
          </div>
          <button class="mt-8 w-full py-2 border border-slate-300 rounded-lg hover:bg-slate-50">Select</button>
        </div>
        <div class="border border-primary-500 rounded-2xl p-8 ring-1 ring-primary-500">
          <h3 class="text-lg font-bold text-slate-900">Pro</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900" x-text="currency === 'USD' ? '$' : (currency === 'EUR' ? '€' : '£')"></span>
            <span class="text-4xl font-bold text-slate-900" x-text="Math.round(29 * rate)">29</span>
          </div>
          <button class="mt-8 w-full py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700">Select</button>
        </div>
        <div class="border border-slate-200 rounded-2xl p-8">
          <h3 class="text-lg font-bold text-slate-900">Enterprise</h3>
          <div class="mt-4 flex items-baseline">
            <span class="text-4xl font-bold text-slate-900" x-text="currency === 'USD' ? '$' : (currency === 'EUR' ? '€' : '£')"></span>
            <span class="text-4xl font-bold text-slate-900" x-text="Math.round(99 * rate)">99</span>
          </div>
          <button class="mt-8 w-full py-2 border border-slate-300 rounded-lg hover:bg-slate-50">Select</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-027",
        "title": "Pricing with Sale Timer",
        "description": "Countdown timer for offer",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-900 py-24 text-white">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold mb-4">Flash Sale Ends In:</h2>
      <div class="flex justify-center gap-4 text-4xl font-mono font-bold mb-12" x-data="{ time: 86400 }" x-init="setInterval(() => time = time > 0 ? time - 1 : 0, 1000)">
        <div class="bg-slate-800 p-4 rounded-lg">
          <span x-text="String(Math.floor(time / 3600)).padStart(2, '0')">24</span>
          <span class="text-xs block font-sans font-normal text-slate-400 mt-1">Hours</span>
        </div>
        <div class="bg-slate-800 p-4 rounded-lg">
          <span x-text="String(Math.floor((time % 3600) / 60)).padStart(2, '0')">00</span>
          <span class="text-xs block font-sans font-normal text-slate-400 mt-1">Mins</span>
        </div>
        <div class="bg-slate-800 p-4 rounded-lg">
          <span x-text="String(time % 60).padStart(2, '0')">00</span>
          <span class="text-xs block font-sans font-normal text-slate-400 mt-1">Secs</span>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="max-w-md mx-auto bg-gradient-to-br from-pink-500 to-orange-500 p-1 rounded-2xl">
        <div class="bg-slate-900 p-8 rounded-xl">
          <h3 class="text-2xl font-bold">Lifetime Deal</h3>
          <div class="mt-4 flex items-center justify-center gap-4">
            <span class="text-5xl font-bold">$49</span>
            <span class="text-2xl text-slate-500 line-through">$499</span>
          </div>
          <p class="mt-4 text-slate-300">Get access to everything forever.</p>
          <button class="mt-8 w-full py-3 bg-white text-slate-900 font-bold rounded-lg hover:bg-slate-100">Grab Deal</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-028",
        "title": "Pricing with User Slider",
        "description": "Dynamic price calculation",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24" x-data="{ users: 5 }">
    <div class="max-w-4xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900">Pay as you grow</h2>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="bg-slate-50 p-12 rounded-3xl border border-slate-200">
        <div class="mb-8">
          <label for="users" class="block text-sm font-medium text-slate-700 mb-2">How many users?</label>
          <input type="range" id="users" min="1" max="50" x-model="users" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary-600">
          <div class="mt-2 text-center font-bold text-slate-900"><span x-text="users">5</span> Users</div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="bg-white p-6 rounded-xl border border-slate-200">
            <h3 class="font-bold text-slate-900">Standard</h3>
            <div class="mt-2 text-3xl font-bold text-slate-900">$<span x-text="users * 10">50</span><span class="text-sm font-normal text-slate-500">/mo</span></div>
            <p class="text-sm text-slate-500 mt-1">$10 per user</p>
            <button class="mt-4 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Choose Standard</button>
          </div>
          <div class="bg-white p-6 rounded-xl border border-primary-200 ring-1 ring-primary-200">
            <h3 class="font-bold text-slate-900">Premium</h3>
            <div class="mt-2 text-3xl font-bold text-slate-900">$<span x-text="users * 20">100</span><span class="text-sm font-normal text-slate-500">/mo</span></div>
            <p class="text-sm text-slate-500 mt-1">$20 per user</p>
            <button class="mt-4 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Choose Premium</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-029",
        "title": "Pricing with Feature Tabs",
        "description": "Tabs to switch categories",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24" x-data="{ tab: 'marketing' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900">Tailored Solutions</h2>
        <div class="mt-6 inline-flex bg-slate-100 p-1 rounded-lg">
          <button class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="tab === 'marketing' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-900'" @click="tab = 'marketing'">Marketing</button>
          <button class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="tab === 'sales' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-900'" @click="tab = 'sales'">Sales</button>
          <button class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="tab === 'dev' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-900'" @click="tab = 'dev'">Developers</button>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="max-w-md mx-auto bg-white border border-slate-200 rounded-2xl p-8 shadow-sm">
        <div x-show="tab === 'marketing'">
          <h3 class="text-xl font-bold text-slate-900">Marketing Suite</h3>
          <p class="text-slate-500 mt-2">All the tools for growth.</p>
          <div class="mt-6 text-4xl font-bold text-slate-900">$49<span class="text-base font-normal text-slate-500">/mo</span></div>
          <ul class="mt-6 space-y-3 text-slate-600">
            <li>Email Automation</li>
            <li>Social Scheduling</li>
            <li>Analytics Dashboard</li>
          </ul>
        </div>
        <div x-show="tab === 'sales'" style="display: none;">
          <h3 class="text-xl font-bold text-slate-900">Sales CRM</h3>
          <p class="text-slate-500 mt-2">Close more deals faster.</p>
          <div class="mt-6 text-4xl font-bold text-slate-900">$69<span class="text-base font-normal text-slate-500">/mo</span></div>
          <ul class="mt-6 space-y-3 text-slate-600">
            <li>Lead Management</li>
            <li>Pipeline Tracking</li>
            <li>Call Recording</li>
          </ul>
        </div>
        <div x-show="tab === 'dev'" style="display: none;">
          <h3 class="text-xl font-bold text-slate-900">Developer API</h3>
          <p class="text-slate-500 mt-2">Build custom integrations.</p>
          <div class="mt-6 text-4xl font-bold text-slate-900">$99<span class="text-base font-normal text-slate-500">/mo</span></div>
          <ul class="mt-6 space-y-3 text-slate-600">
            <li>Unlimited API Calls</li>
            <li>Webhooks</li>
            <li>Dedicated Support</li>
          </ul>
        </div>
        <button class="mt-8 w-full py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800">Get Started</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-030",
        "title": "Pricing with Testimonials",
        "description": "Social proof alongside pricing",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
      <div>
        <h2 class="text-3xl font-bold text-slate-900">Loved by thousands</h2>
        <div class="mt-8 space-y-6">
          <blockquote class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <p class="text-slate-600 italic">"This tool has completely transformed how we work. Worth every penny."</p>
            <footer class="mt-4 font-bold text-slate-900">- Jane Doe, CEO</footer>
          </blockquote>
          <blockquote class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <p class="text-slate-600 italic">"The best investment we made this year. Support is amazing."</p>
            <footer class="mt-4 font-bold text-slate-900">- John Smith, CTO</footer>
          </blockquote>
        </div>
      </div>
      <div>
        <div class="bg-white p-8 rounded-2xl shadow-lg border border-slate-200">
          <h3 class="text-2xl font-bold text-slate-900">Pro Plan</h3>
          <div class="mt-4 text-5xl font-bold text-primary-600">$49</div>
          <p class="text-slate-500 mt-2">per month, billed annually</p>
          <ul class="mt-8 space-y-4 text-slate-600">
            <li class="flex items-center"><svg class="w-5 h-5 text-green-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited Users</li>
            <li class="flex items-center"><svg class="w-5 h-5 text-green-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> All Features</li>
            <li class="flex items-center"><svg class="w-5 h-5 text-green-500 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Priority Support</li>
          </ul>
          <button class="mt-8 w-full py-4 bg-primary-600 text-white rounded-xl font-bold hover:bg-primary-700 shadow-lg shadow-primary-600/30">Start Free Trial</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-031",
        "title": "Pricing with FAQ Accordion",
        "description": "Pricing and collapsible FAQs",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
        <div class="lg:col-span-1">
          <h2 class="text-3xl font-bold text-slate-900">Simple Pricing</h2>
          <p class="mt-4 text-slate-600">One plan, everything included.</p>
          <div class="mt-8 bg-slate-50 p-8 rounded-2xl border border-slate-200">
            <div class="text-4xl font-bold text-slate-900">$29</div>
            <p class="text-slate-500 mt-2">per month</p>
            <button class="mt-6 w-full py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800">Get Started</button>
          </div>
        </div>
        <div class="lg:col-span-2" x-data="{ active: null }">
          <h3 class="text-xl font-bold text-slate-900 mb-6">Frequently Asked Questions</h3>

          <script src="https://unpkg.com/alpinejs" defer></script>

          <div class="space-y-4">
            <div class="border border-slate-200 rounded-lg">
              <button class="flex items-center justify-between w-full p-4 text-left font-medium text-slate-900" @click="active = active === 1 ? null : 1">
                <span>What payment methods do you accept?</span>
                <svg class="w-5 h-5 transform transition-transform" :class="active === 1 ? 'rotate-180' : ''" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="p-4 pt-0 text-slate-600" x-show="active === 1" style="display: none;">
                We accept all major credit cards, PayPal, and bank transfers for annual plans.
              </div>
            </div>
            <div class="border border-slate-200 rounded-lg">
              <button class="flex items-center justify-between w-full p-4 text-left font-medium text-slate-900" @click="active = active === 2 ? null : 2">
                <span>Can I change plans later?</span>
                <svg class="w-5 h-5 transform transition-transform" :class="active === 2 ? 'rotate-180' : ''" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="p-4 pt-0 text-slate-600" x-show="active === 2" style="display: none;">
                Yes, you can upgrade or downgrade your plan at any time from your account settings.
              </div>
            </div>
             <div class="border border-slate-200 rounded-lg">
              <button class="flex items-center justify-between w-full p-4 text-left font-medium text-slate-900" @click="active = active === 3 ? null : 3">
                <span>Is there a free trial?</span>
                <svg class="w-5 h-5 transform transition-transform" :class="active === 3 ? 'rotate-180' : ''" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="p-4 pt-0 text-slate-600" x-show="active === 3" style="display: none;">
                Yes, we offer a 14-day free trial with no credit card required.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-032",
        "title": "Pricing with Video Background",
        "description": "Pricing over video",
        "dir": "templates/06-pricing",
        "content": """<div class="relative py-24 overflow-hidden">
    <video autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-cover opacity-20">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-abstract-technology-network-connection-lines-background-2838-large.mp4" type="video/mp4">
    </video>
    <div class="absolute inset-0 bg-slate-900/80"></div>
    <div class="relative max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-white mb-12">Future Proof Pricing</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white/10 backdrop-blur-sm border border-white/10 p-8 rounded-2xl text-white hover:bg-white/20 transition-colors">
          <h3 class="text-xl font-bold">Basic</h3>
          <div class="mt-4 text-3xl font-bold">$29</div>
          <button class="mt-6 w-full py-2 border border-white/30 rounded hover:bg-white/10">Select</button>
        </div>
        <div class="bg-primary-600/80 backdrop-blur-sm border border-primary-500 p-8 rounded-2xl text-white hover:bg-primary-600/90 transition-colors transform scale-105 shadow-2xl">
          <h3 class="text-xl font-bold">Pro</h3>
          <div class="mt-4 text-3xl font-bold">$59</div>
          <button class="mt-6 w-full py-2 bg-white text-primary-600 rounded hover:bg-slate-100 font-bold">Select</button>
        </div>
        <div class="bg-white/10 backdrop-blur-sm border border-white/10 p-8 rounded-2xl text-white hover:bg-white/20 transition-colors">
          <h3 class="text-xl font-bold">Max</h3>
          <div class="mt-4 text-3xl font-bold">$99</div>
          <button class="mt-6 w-full py-2 border border-white/30 rounded hover:bg-white/10">Select</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-033",
        "title": "Pricing with Glassmorphism",
        "description": "Frosted glass cards",
        "dir": "templates/06-pricing",
        "content": """<div class="py-24 bg-gradient-to-br from-purple-500 via-pink-500 to-red-500">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white/20 backdrop-blur-lg border border-white/30 p-8 rounded-2xl text-white shadow-xl">
        <h3 class="text-xl font-bold">Starter</h3>
        <div class="mt-4 text-4xl font-bold">$19</div>
        <p class="mt-2 text-white/80">Perfect for beginners.</p>
        <button class="mt-8 w-full py-3 bg-white/20 hover:bg-white/30 rounded-xl font-bold border border-white/30 transition-colors">Get Started</button>
      </div>
      <div class="bg-white/40 backdrop-blur-lg border border-white/50 p-8 rounded-2xl text-white shadow-2xl transform scale-105">
        <h3 class="text-xl font-bold">Professional</h3>
        <div class="mt-4 text-4xl font-bold">$49</div>
        <p class="mt-2 text-white/90">For serious creators.</p>
        <button class="mt-8 w-full py-3 bg-white text-purple-600 rounded-xl font-bold hover:bg-slate-50 transition-colors shadow-lg">Get Started</button>
      </div>
      <div class="bg-white/20 backdrop-blur-lg border border-white/30 p-8 rounded-2xl text-white shadow-xl">
        <h3 class="text-xl font-bold">Agency</h3>
        <div class="mt-4 text-4xl font-bold">$99</div>
        <p class="mt-2 text-white/80">For large teams.</p>
        <button class="mt-8 w-full py-3 bg-white/20 hover:bg-white/30 rounded-xl font-bold border border-white/30 transition-colors">Get Started</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-034",
        "title": "Pricing with Neomorphism",
        "description": "Soft UI pricing cards",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-200 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="rounded-3xl bg-slate-200 p-8 shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]">
        <h3 class="text-xl font-bold text-slate-700">Basic</h3>
        <div class="mt-4 text-3xl font-bold text-slate-700">$29</div>
        <button class="mt-8 w-full py-3 rounded-xl bg-slate-200 text-slate-700 font-bold shadow-[5px_5px_10px_#bebebe,-5px_-5px_10px_#ffffff] hover:shadow-[inset_5px_5px_10px_#bebebe,inset_-5px_-5px_10px_#ffffff] transition-shadow">Select</button>
      </div>
      <div class="rounded-3xl bg-slate-200 p-8 shadow-[inset_20px_20px_60px_#bebebe,inset_-20px_-20px_60px_#ffffff]">
        <h3 class="text-xl font-bold text-primary-600">Pro</h3>
        <div class="mt-4 text-3xl font-bold text-primary-600">$59</div>
        <button class="mt-8 w-full py-3 rounded-xl bg-primary-600 text-white font-bold shadow-[5px_5px_10px_#bebebe,-5px_-5px_10px_#ffffff] hover:bg-primary-700 transition-colors">Select</button>
      </div>
      <div class="rounded-3xl bg-slate-200 p-8 shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]">
        <h3 class="text-xl font-bold text-slate-700">Max</h3>
        <div class="mt-4 text-3xl font-bold text-slate-700">$99</div>
        <button class="mt-8 w-full py-3 rounded-xl bg-slate-200 text-slate-700 font-bold shadow-[5px_5px_10px_#bebebe,-5px_-5px_10px_#ffffff] hover:shadow-[inset_5px_5px_10px_#bebebe,inset_-5px_-5px_10px_#ffffff] transition-shadow">Select</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-035",
        "title": "Pricing with Retro Style",
        "description": "Pixel art/Retro gaming style",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-yellow-100 py-24 font-mono">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
        <h3 class="text-xl font-bold text-black uppercase">Player 1</h3>
        <div class="mt-4 text-3xl font-bold text-black">$10</div>
        <ul class="mt-6 space-y-2 text-sm">
          <li>> 1 Life</li>
          <li>> Basic Gear</li>
        </ul>
        <button class="mt-8 w-full py-2 border-2 border-black bg-green-400 text-black font-bold hover:bg-green-500 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:shadow-none active:translate-x-[4px] active:translate-y-[4px] transition-all">START</button>
      </div>
      <div class="bg-white border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] transform -translate-y-4">
        <h3 class="text-xl font-bold text-black uppercase">Player 2</h3>
        <div class="mt-4 text-3xl font-bold text-black">$20</div>
        <ul class="mt-6 space-y-2 text-sm">
          <li>> 3 Lives</li>
          <li>> Power Ups</li>
        </ul>
        <button class="mt-8 w-full py-2 border-2 border-black bg-blue-400 text-black font-bold hover:bg-blue-500 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:shadow-none active:translate-x-[4px] active:translate-y-[4px] transition-all">START</button>
      </div>
      <div class="bg-white border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
        <h3 class="text-xl font-bold text-black uppercase">Boss Mode</h3>
        <div class="mt-4 text-3xl font-bold text-black">$50</div>
        <ul class="mt-6 space-y-2 text-sm">
          <li>> Infinite Lives</li>
          <li>> God Mode</li>
        </ul>
        <button class="mt-8 w-full py-2 border-2 border-black bg-red-400 text-black font-bold hover:bg-red-500 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:shadow-none active:translate-x-[4px] active:translate-y-[4px] transition-all">START</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-036",
        "title": "Pricing with Cyberpunk Style",
        "description": "High tech/Cyberpunk aesthetic",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-black py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-slate-900 border border-cyan-500 p-8 relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-16 h-16 bg-cyan-500/20 rounded-bl-full"></div>
        <h3 class="text-xl font-bold text-cyan-500 font-mono">NETRUNNER</h3>
        <div class="mt-4 text-3xl font-bold text-white">¥2000</div>
        <button class="mt-8 w-full py-2 border border-cyan-500 text-cyan-500 hover:bg-cyan-500 hover:text-black transition-colors uppercase tracking-widest font-bold">Connect</button>
      </div>
      <div class="bg-slate-900 border border-pink-500 p-8 relative overflow-hidden group shadow-[0_0_20px_rgba(236,72,153,0.3)]">
        <div class="absolute top-0 right-0 w-16 h-16 bg-pink-500/20 rounded-bl-full"></div>
        <h3 class="text-xl font-bold text-pink-500 font-mono">STREET SAMURAI</h3>
        <div class="mt-4 text-3xl font-bold text-white">¥5000</div>
        <button class="mt-8 w-full py-2 bg-pink-500 text-black hover:bg-pink-400 transition-colors uppercase tracking-widest font-bold">Connect</button>
      </div>
      <div class="bg-slate-900 border border-yellow-500 p-8 relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-16 h-16 bg-yellow-500/20 rounded-bl-full"></div>
        <h3 class="text-xl font-bold text-yellow-500 font-mono">CORPORATE</h3>
        <div class="mt-4 text-3xl font-bold text-white">¥9000</div>
        <button class="mt-8 w-full py-2 border border-yellow-500 text-yellow-500 hover:bg-yellow-500 hover:text-black transition-colors uppercase tracking-widest font-bold">Connect</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-037",
        "title": "Pricing with Neon Glow",
        "description": "Dark mode with neon accents",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="bg-slate-800 p-8 rounded-2xl shadow-[0_0_15px_rgba(59,130,246,0.5)] border border-blue-500/30 hover:shadow-[0_0_25px_rgba(59,130,246,0.7)] transition-shadow">
        <h3 class="text-xl font-bold text-blue-400">Blue Neon</h3>
        <div class="mt-4 text-3xl font-bold text-white">$29</div>
        <button class="mt-8 w-full py-2 rounded-lg border border-blue-500 text-blue-400 hover:bg-blue-500 hover:text-white transition-colors shadow-[0_0_10px_rgba(59,130,246,0.5)]">Glow</button>
      </div>
      <div class="bg-slate-800 p-8 rounded-2xl shadow-[0_0_15px_rgba(168,85,247,0.5)] border border-purple-500/30 hover:shadow-[0_0_25px_rgba(168,85,247,0.7)] transition-shadow transform scale-105">
        <h3 class="text-xl font-bold text-purple-400">Purple Neon</h3>
        <div class="mt-4 text-3xl font-bold text-white">$59</div>
        <button class="mt-8 w-full py-2 rounded-lg bg-purple-600 text-white hover:bg-purple-500 transition-colors shadow-[0_0_15px_rgba(168,85,247,0.8)]">Glow</button>
      </div>
      <div class="bg-slate-800 p-8 rounded-2xl shadow-[0_0_15px_rgba(236,72,153,0.5)] border border-pink-500/30 hover:shadow-[0_0_25px_rgba(236,72,153,0.7)] transition-shadow">
        <h3 class="text-xl font-bold text-pink-400">Pink Neon</h3>
        <div class="mt-4 text-3xl font-bold text-white">$99</div>
        <button class="mt-8 w-full py-2 rounded-lg border border-pink-500 text-pink-400 hover:bg-pink-500 hover:text-white transition-colors shadow-[0_0_10px_rgba(236,72,153,0.5)]">Glow</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-038",
        "title": "Pricing with 3D Cards",
        "description": "Cards with 3D perspective",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-100 py-24 perspective-1000">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="bg-white p-8 rounded-2xl shadow-xl transform rotate-y-12 hover:rotate-y-0 transition-transform duration-500 border-r-4 border-b-4 border-slate-300">
        <h3 class="text-xl font-bold text-slate-900">Left</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$29</div>
        <button class="mt-8 w-full py-2 bg-slate-100 hover:bg-slate-200 rounded-lg font-bold text-slate-900">Select</button>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-2xl transform hover:scale-105 transition-transform duration-500 border-r-4 border-b-4 border-primary-600 z-10">
        <h3 class="text-xl font-bold text-primary-600">Center</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$59</div>
        <button class="mt-8 w-full py-2 bg-primary-600 hover:bg-primary-700 rounded-lg font-bold text-white">Select</button>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-xl transform -rotate-y-12 hover:rotate-y-0 transition-transform duration-500 border-l-4 border-b-4 border-slate-300">
        <h3 class="text-xl font-bold text-slate-900">Right</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$99</div>
        <button class="mt-8 w-full py-2 bg-slate-100 hover:bg-slate-200 rounded-lg font-bold text-slate-900">Select</button>
      </div>
    </div>
    <style>
      .perspective-1000 { perspective: 1000px; }
      .rotate-y-12 { transform: rotateY(12deg); }
      .-rotate-y-12 { transform: rotateY(-12deg); }
    </style>
  </div>"""
    }
]
# Placeholder for Price 039-050
# Part 6 continued: Price 039-050
TEMPLATES_PRICE_2_PART_2 = [
    {
        "id": "price-039",
        "title": "Pricing with Parallax",
        "description": "Parallax scrolling effect",
        "dir": "templates/06-pricing",
        "content": """<div class="relative h-screen overflow-y-auto overflow-x-hidden perspective-1px">
    <div class="absolute inset-0 transform-style-3d -z-10">
      <div class="absolute inset-0 bg-cover bg-center transform translate-z-[-1px] scale-2" style="background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');"></div>
    </div>
    <div class="relative min-h-screen flex items-center justify-center py-24">
      <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8 w-full">
        <div class="bg-white/90 backdrop-blur-sm p-8 rounded-2xl shadow-xl">
          <h3 class="text-xl font-bold text-slate-900">Standard</h3>
          <div class="mt-4 text-3xl font-bold text-slate-900">$29</div>
          <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
        </div>
        <div class="bg-primary-600/90 backdrop-blur-sm p-8 rounded-2xl shadow-2xl transform scale-105 text-white">
          <h3 class="text-xl font-bold">Premium</h3>
          <div class="mt-4 text-3xl font-bold">$59</div>
          <button class="mt-6 w-full py-2 bg-white text-primary-600 rounded hover:bg-slate-100 font-bold">Select</button>
        </div>
        <div class="bg-white/90 backdrop-blur-sm p-8 rounded-2xl shadow-xl">
          <h3 class="text-xl font-bold text-slate-900">Ultimate</h3>
          <div class="mt-4 text-3xl font-bold text-slate-900">$99</div>
          <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
        </div>
      </div>
    </div>
    <style>
      .perspective-1px { perspective: 1px; }
      .transform-style-3d { transform-style: preserve-3d; }
      .translate-z-\[-1px\] { transform: translateZ(-1px); }
      .scale-2 { transform: scale(2); }
    </style>
  </div>"""
    },
    {
        "id": "price-040",
        "title": "Pricing with Sticky Header",
        "description": "Header stays visible",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 h-96 overflow-y-auto relative border border-slate-200 rounded-xl">
    <div class="sticky top-0 bg-white shadow-sm z-10 p-4 flex justify-between items-center border-b border-slate-200">
      <h2 class="text-xl font-bold text-slate-900">Pricing Plans</h2>
      <button class="px-4 py-2 bg-primary-600 text-white rounded text-sm font-bold hover:bg-primary-700">Contact Sales</button>
    </div>
    <div class="p-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded-xl border border-slate-200">
          <h3 class="font-bold text-slate-900">Basic</h3>
          <div class="mt-2 text-2xl font-bold">$19</div>
          <p class="mt-4 text-slate-600 text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
          <button class="mt-4 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Choose</button>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200">
          <h3 class="font-bold text-slate-900">Pro</h3>
          <div class="mt-2 text-2xl font-bold">$49</div>
          <p class="mt-4 text-slate-600 text-sm">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
          <button class="mt-4 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Choose</button>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200">
          <h3 class="font-bold text-slate-900">Enterprise</h3>
          <div class="mt-2 text-2xl font-bold">$99</div>
          <p class="mt-4 text-slate-600 text-sm">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
          <button class="mt-4 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Choose</button>
        </div>
        <!-- More content to enable scrolling -->
        <div class="col-span-full mt-8">
          <h3 class="font-bold text-slate-900 mb-4">Detailed Comparison</h3>
          <p class="text-slate-600 mb-4">Lorem ipsum dolor sit amet...</p>
          <p class="text-slate-600 mb-4">Consectetur adipiscing elit...</p>
          <p class="text-slate-600 mb-4">Sed do eiusmod tempor...</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-041",
        "title": "Pricing with Sticky Footer",
        "description": "Call to action always visible",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white relative h-96 overflow-y-auto border border-slate-200 rounded-xl">
    <div class="p-8 pb-24">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-slate-900">Flexible Plans</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="border border-slate-200 p-6 rounded-lg">
          <h3 class="font-bold">Plan A</h3>
          <div class="text-2xl font-bold mt-2">$10</div>
          <ul class="mt-4 text-sm text-slate-600 space-y-2">
            <li>Feature 1</li>
            <li>Feature 2</li>
            <li>Feature 3</li>
            <li>Feature 4</li>
            <li>Feature 5</li>
          </ul>
        </div>
        <div class="border border-slate-200 p-6 rounded-lg">
          <h3 class="font-bold">Plan B</h3>
          <div class="text-2xl font-bold mt-2">$20</div>
          <ul class="mt-4 text-sm text-slate-600 space-y-2">
            <li>Feature 1</li>
            <li>Feature 2</li>
            <li>Feature 3</li>
            <li>Feature 4</li>
            <li>Feature 5</li>
          </ul>
        </div>
        <div class="border border-slate-200 p-6 rounded-lg">
          <h3 class="font-bold">Plan C</h3>
          <div class="text-2xl font-bold mt-2">$30</div>
          <ul class="mt-4 text-sm text-slate-600 space-y-2">
            <li>Feature 1</li>
            <li>Feature 2</li>
            <li>Feature 3</li>
            <li>Feature 4</li>
            <li>Feature 5</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="sticky bottom-0 bg-white border-t border-slate-200 p-4 flex justify-between items-center shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.1)]">
      <div>
        <p class="font-bold text-slate-900">Ready to start?</p>
        <p class="text-sm text-slate-500">14-day free trial on all plans.</p>
      </div>
      <button class="px-6 py-2 bg-primary-600 text-white rounded-lg font-bold hover:bg-primary-700">Get Started</button>
    </div>
  </div>"""
    },
    {
        "id": "price-042",
        "title": "Pricing with Sidebar",
        "description": "Vertical layout with sidebar",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-12">
    <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row gap-8">
      <div class="md:w-1/4">
        <div class="sticky top-8">
          <h2 class="text-2xl font-bold text-slate-900 mb-4">Pricing</h2>
          <nav class="space-y-2">
            <a href="#" class="block px-4 py-2 bg-white rounded-lg shadow-sm font-medium text-primary-600 border-l-4 border-primary-600">Monthly Plans</a>
            <a href="#" class="block px-4 py-2 text-slate-600 hover:bg-white hover:shadow-sm rounded-lg transition-all">Annual Plans</a>
            <a href="#" class="block px-4 py-2 text-slate-600 hover:bg-white hover:shadow-sm rounded-lg transition-all">Enterprise</a>
          </nav>
        </div>
      </div>
      <div class="md:w-3/4 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
          <h3 class="text-lg font-bold text-slate-900">Starter</h3>
          <div class="mt-2 text-3xl font-bold text-slate-900">$29</div>
          <p class="mt-4 text-slate-600 text-sm">Great for individuals.</p>
          <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
          <h3 class="text-lg font-bold text-slate-900">Team</h3>
          <div class="mt-2 text-3xl font-bold text-slate-900">$99</div>
          <p class="mt-4 text-slate-600 text-sm">Perfect for small teams.</p>
          <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Select</button>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
          <h3 class="text-lg font-bold text-slate-900">Business</h3>
          <div class="mt-2 text-3xl font-bold text-slate-900">$199</div>
          <p class="mt-4 text-slate-600 text-sm">For growing companies.</p>
          <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
        </div>
        <div class="bg-slate-900 p-6 rounded-xl shadow-sm text-white">
          <h3 class="text-lg font-bold">Custom</h3>
          <div class="mt-2 text-3xl font-bold">Contact</div>
          <p class="mt-4 text-slate-400 text-sm">Tailored solutions.</p>
          <button class="mt-6 w-full py-2 bg-white text-slate-900 rounded hover:bg-slate-100 font-bold">Contact Us</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-043",
        "title": "Pricing with Modal",
        "description": "Details in modal",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24" x-data="{ open: false, plan: '' }">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-12">Select a Plan</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="border border-slate-200 p-8 rounded-2xl">
          <h3 class="text-xl font-bold">Basic</h3>
          <div class="mt-4 text-3xl font-bold">$19</div>
          <button class="mt-6 px-6 py-2 border border-slate-300 rounded hover:bg-slate-50" @click="open = true; plan = 'Basic'">View Details</button>
        </div>
        <div class="border border-primary-500 p-8 rounded-2xl ring-1 ring-primary-500">
          <h3 class="text-xl font-bold">Pro</h3>
          <div class="mt-4 text-3xl font-bold">$49</div>
          <button class="mt-6 px-6 py-2 bg-primary-600 text-white rounded hover:bg-primary-700" @click="open = true; plan = 'Pro'">View Details</button>
        </div>
        <div class="border border-slate-200 p-8 rounded-2xl">
          <h3 class="text-xl font-bold">Max</h3>
          <div class="mt-4 text-3xl font-bold">$99</div>
          <button class="mt-6 px-6 py-2 border border-slate-300 rounded hover:bg-slate-50" @click="open = true; plan = 'Max'">View Details</button>
        </div>
      </div>
    </div>

    <script src="https://unpkg.com/alpinejs" defer></script>

    <!-- Modal -->
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm" x-show="open" style="display: none;">
      <div class="bg-white rounded-2xl p-8 max-w-md w-full mx-4 shadow-2xl" @click.away="open = false">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-2xl font-bold text-slate-900" x-text="plan + ' Plan Details'"></h3>
          <button @click="open = false" class="text-slate-400 hover:text-slate-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </div>
        <div class="space-y-4 text-slate-600">
          <p>Here are the full details for the <span x-text="plan"></span> plan.</p>
          <ul class="list-disc pl-5 space-y-2">
            <li>Feature A included</li>
            <li>Feature B included</li>
            <li>24/7 Support</li>
          </ul>
        </div>
        <div class="mt-8 flex gap-4">
          <button class="flex-1 py-3 bg-primary-600 text-white rounded-lg font-bold hover:bg-primary-700">Subscribe Now</button>
          <button class="px-6 py-3 border border-slate-300 rounded-lg hover:bg-slate-50" @click="open = false">Close</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-044",
        "title": "Pricing with Popover",
        "description": "Hover for more info",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-2xl shadow-sm relative group">
        <h3 class="text-xl font-bold text-slate-900">Starter</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$29</div>
        <button class="mt-6 w-full py-2 border border-slate-200 rounded hover:bg-slate-50">Select</button>

        <!-- Popover -->
        <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-4 w-64 bg-slate-800 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10">
          <div class="font-bold mb-2">Includes:</div>
          <ul class="list-disc pl-4 space-y-1">
            <li>1 User</li>
            <li>5 Projects</li>
            <li>Basic Support</li>
          </ul>
          <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-800"></div>
        </div>
      </div>

      <div class="bg-white p-8 rounded-2xl shadow-md border border-primary-100 relative group">
        <h3 class="text-xl font-bold text-slate-900">Growth</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$59</div>
        <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Select</button>

        <!-- Popover -->
        <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-4 w-64 bg-slate-800 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10">
          <div class="font-bold mb-2">Includes:</div>
          <ul class="list-disc pl-4 space-y-1">
            <li>5 Users</li>
            <li>Unlimited Projects</li>
            <li>Priority Support</li>
          </ul>
          <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-800"></div>
        </div>
      </div>

      <div class="bg-white p-8 rounded-2xl shadow-sm relative group">
        <h3 class="text-xl font-bold text-slate-900">Scale</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$99</div>
        <button class="mt-6 w-full py-2 border border-slate-200 rounded hover:bg-slate-50">Select</button>

        <!-- Popover -->
        <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-4 w-64 bg-slate-800 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10">
          <div class="font-bold mb-2">Includes:</div>
          <ul class="list-disc pl-4 space-y-1">
            <li>Unlimited Users</li>
            <li>Advanced Analytics</li>
            <li>Dedicated Manager</li>
          </ul>
          <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-800"></div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-045",
        "title": "Pricing with Tooltip Hover",
        "description": "Detailed tooltips on features",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6 border border-slate-200 rounded-2xl p-8">
      <h2 class="text-2xl font-bold text-slate-900 mb-8 text-center">Compare Plans</h2>
      <table class="w-full text-left">
        <thead>
          <tr class="border-b border-slate-200">
            <th class="py-4 font-medium text-slate-500">Feature</th>
            <th class="py-4 font-bold text-slate-900 text-center">Basic</th>
            <th class="py-4 font-bold text-primary-600 text-center">Pro</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-200">
          <tr>
            <td class="py-4">
              <span class="border-b border-dotted border-slate-400 cursor-help relative group">
                Storage
                <span class="absolute bottom-full left-0 mb-2 w-48 bg-slate-900 text-white text-xs p-2 rounded hidden group-hover:block z-10">Cloud storage space for your files.</span>
              </span>
            </td>
            <td class="py-4 text-center">10 GB</td>
            <td class="py-4 text-center font-bold">1 TB</td>
          </tr>
          <tr>
            <td class="py-4">
              <span class="border-b border-dotted border-slate-400 cursor-help relative group">
                Bandwidth
                <span class="absolute bottom-full left-0 mb-2 w-48 bg-slate-900 text-white text-xs p-2 rounded hidden group-hover:block z-10">Monthly data transfer limit.</span>
              </span>
            </td>
            <td class="py-4 text-center">100 GB</td>
            <td class="py-4 text-center font-bold">Unlimited</td>
          </tr>
          <tr>
            <td class="py-4">
              <span class="border-b border-dotted border-slate-400 cursor-help relative group">
                Support
                <span class="absolute bottom-full left-0 mb-2 w-48 bg-slate-900 text-white text-xs p-2 rounded hidden group-hover:block z-10">Access to our customer support team.</span>
              </span>
            </td>
            <td class="py-4 text-center">Email</td>
            <td class="py-4 text-center font-bold">24/7 Live Chat</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>"""
    },
    {
        "id": "price-046",
        "title": "Pricing with Animated Background",
        "description": "Subtle animated gradient",
        "dir": "templates/06-pricing",
        "content": """<div class="py-24 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 bg-[length:200%_200%] animate-gradient">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white/90 backdrop-blur p-8 rounded-2xl shadow-xl">
        <h3 class="text-xl font-bold text-slate-900">Standard</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$29</div>
        <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-2xl transform scale-105">
        <h3 class="text-xl font-bold text-slate-900">Premium</h3>
        <div class="mt-4 text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">$59</div>
        <button class="mt-6 w-full py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded hover:shadow-lg transition-shadow font-bold">Select</button>
      </div>
      <div class="bg-white/90 backdrop-blur p-8 rounded-2xl shadow-xl">
        <h3 class="text-xl font-bold text-slate-900">Ultimate</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$99</div>
        <button class="mt-6 w-full py-2 border border-slate-300 rounded hover:bg-slate-50">Select</button>
      </div>
    </div>
    <style>
      @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
      }
      .animate-gradient {
        animation: gradient 6s ease infinite;
      }
    </style>
  </div>"""
    },
    {
        "id": "price-047",
        "title": "Pricing with Particle Effect",
        "description": "CSS particles background",
        "dir": "templates/06-pricing",
        "content": """<div class="relative py-24 bg-slate-900 overflow-hidden">
    <!-- Particles (simulated with absolute divs) -->
    <div class="absolute top-10 left-10 w-2 h-2 bg-blue-500 rounded-full opacity-50 animate-pulse"></div>
    <div class="absolute top-20 right-20 w-3 h-3 bg-purple-500 rounded-full opacity-50 animate-bounce"></div>
    <div class="absolute bottom-10 left-1/3 w-2 h-2 bg-pink-500 rounded-full opacity-50 animate-ping"></div>
    <div class="absolute top-1/2 right-1/4 w-1 h-1 bg-white rounded-full opacity-70"></div>
    <div class="absolute bottom-20 right-10 w-4 h-4 bg-blue-400 rounded-full opacity-30 blur-sm"></div>

    <div class="relative max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-slate-800/50 backdrop-blur border border-slate-700 p-8 rounded-2xl text-white">
        <h3 class="text-xl font-bold">Star</h3>
        <div class="mt-4 text-3xl font-bold">$19</div>
        <button class="mt-6 w-full py-2 border border-slate-600 rounded hover:bg-slate-700">Select</button>
      </div>
      <div class="bg-slate-800/80 backdrop-blur border border-primary-500 p-8 rounded-2xl text-white shadow-[0_0_30px_rgba(79,70,229,0.3)]">
        <h3 class="text-xl font-bold text-primary-400">Nebula</h3>
        <div class="mt-4 text-3xl font-bold">$49</div>
        <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-500 font-bold">Select</button>
      </div>
      <div class="bg-slate-800/50 backdrop-blur border border-slate-700 p-8 rounded-2xl text-white">
        <h3 class="text-xl font-bold">Galaxy</h3>
        <div class="mt-4 text-3xl font-bold">$99</div>
        <button class="mt-6 w-full py-2 border border-slate-600 rounded hover:bg-slate-700">Select</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-048",
        "title": "Pricing with Wave Divider",
        "description": "Wave shape separator",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white relative pt-24 pb-48">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900">Simple Pricing</h2>
      <p class="mt-4 text-slate-600">No hidden fees.</p>
    </div>
    <div class="absolute bottom-0 left-0 right-0">
      <svg viewBox="0 0 1440 320" class="w-full h-auto text-slate-100 fill-current"><path d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,112C672,96,768,96,864,112C960,128,1056,160,1152,160C1248,160,1344,128,1392,112L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>
    </div>
  </div>
  <div class="bg-slate-100 pb-24">
    <div class="max-w-7xl mx-auto px-6 -mt-32 relative z-10">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-2xl shadow-lg">
          <h3 class="text-xl font-bold text-slate-900">Basic</h3>
          <div class="mt-4 text-3xl font-bold">$29</div>
          <button class="mt-6 w-full py-2 border border-slate-200 rounded hover:bg-slate-50">Select</button>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-xl border-t-4 border-primary-600 transform -translate-y-4">
          <h3 class="text-xl font-bold text-slate-900">Pro</h3>
          <div class="mt-4 text-3xl font-bold">$59</div>
          <button class="mt-6 w-full py-2 bg-primary-600 text-white rounded hover:bg-primary-700">Select</button>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-lg">
          <h3 class="text-xl font-bold text-slate-900">Max</h3>
          <div class="mt-4 text-3xl font-bold">$99</div>
          <button class="mt-6 w-full py-2 border border-slate-200 rounded hover:bg-slate-50">Select</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "price-049",
        "title": "Pricing with Blob Shapes",
        "description": "Organic blob backgrounds",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-white py-24 relative overflow-hidden">
    <!-- Blobs -->
    <div class="absolute top-0 left-0 w-64 h-64 bg-purple-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob"></div>
    <div class="absolute top-0 right-0 w-64 h-64 bg-yellow-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-2000"></div>
    <div class="absolute -bottom-8 left-20 w-64 h-64 bg-pink-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-4000"></div>

    <div class="relative max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white/80 backdrop-blur p-8 rounded-2xl shadow-lg border border-white">
        <h3 class="text-xl font-bold text-slate-900">Seed</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$19</div>
        <button class="mt-6 w-full py-2 border border-slate-200 rounded hover:bg-white">Select</button>
      </div>
      <div class="bg-white/80 backdrop-blur p-8 rounded-2xl shadow-xl border border-white transform scale-105">
        <h3 class="text-xl font-bold text-slate-900">Sprout</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$49</div>
        <button class="mt-6 w-full py-2 bg-slate-900 text-white rounded hover:bg-slate-800">Select</button>
      </div>
      <div class="bg-white/80 backdrop-blur p-8 rounded-2xl shadow-lg border border-white">
        <h3 class="text-xl font-bold text-slate-900">Bloom</h3>
        <div class="mt-4 text-3xl font-bold text-slate-900">$99</div>
        <button class="mt-6 w-full py-2 border border-slate-200 rounded hover:bg-white">Select</button>
      </div>
    </div>
    <style>
      @keyframes blob {
        0% { transform: translate(0px, 0px) scale(1); }
        33% { transform: translate(30px, -50px) scale(1.1); }
        66% { transform: translate(-20px, 20px) scale(0.9); }
        100% { transform: translate(0px, 0px) scale(1); }
      }
      .animate-blob {
        animation: blob 7s infinite;
      }
      .animation-delay-2000 {
        animation-delay: 2s;
      }
      .animation-delay-4000 {
        animation-delay: 4s;
      }
    </style>
  </div>"""
    },
    {
        "id": "price-050",
        "title": "Pricing with Glitch Effect",
        "description": "Glitch hover effect",
        "dir": "templates/06-pricing",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-slate-800 p-8 rounded-lg border border-slate-700 group relative overflow-hidden">
        <h3 class="text-xl font-bold text-white relative z-10">Hacker</h3>
        <div class="mt-4 text-3xl font-bold text-white relative z-10">$13.37</div>
        <button class="mt-6 w-full py-2 border border-green-500 text-green-500 hover:bg-green-500 hover:text-black font-mono font-bold relative z-10 transition-colors">INITIATE</button>
        <div class="absolute inset-0 bg-green-500/10 transform translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
      </div>

      <div class="bg-slate-800 p-8 rounded-lg border border-slate-700 group relative overflow-hidden">
        <h3 class="text-xl font-bold text-white relative z-10">Coder</h3>
        <div class="mt-4 text-3xl font-bold text-white relative z-10">$42.00</div>
        <button class="mt-6 w-full py-2 bg-green-500 text-black font-mono font-bold relative z-10 hover:bg-green-400 transition-colors shadow-[4px_4px_0px_#000]">COMPILE</button>
        <div class="absolute inset-0 bg-green-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-100 flex items-center justify-center pointer-events-none">
          <span class="text-green-500 font-mono text-4xl font-bold opacity-20 select-none">101010</span>
        </div>
      </div>

      <div class="bg-slate-800 p-8 rounded-lg border border-slate-700 group relative overflow-hidden">
        <h3 class="text-xl font-bold text-white relative z-10">SysAdmin</h3>
        <div class="mt-4 text-3xl font-bold text-white relative z-10">$99.99</div>
        <button class="mt-6 w-full py-2 border border-green-500 text-green-500 hover:bg-green-500 hover:text-black font-mono font-bold relative z-10 transition-colors">SUDO DO</button>
        <div class="absolute inset-0 bg-green-500/10 transform -translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
      </div>
    </div>
  </div>"""
    }
]
# Part 7: Testimonials 001-025
TEMPLATES_TEST_1 = [
    {
        "id": "test-001",
        "title": "Testimonials Grid",
        "description": "Grid layout of testimonials",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">What our customers say</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
          <div class="flex items-center mb-4">
            <div class="text-yellow-400 flex">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            </div>
          </div>
          <p class="text-slate-600 mb-6">"This product has completely changed my workflow. I can't imagine working without it now. Highly recommended!"</p>
          <div class="font-bold text-slate-900">Sarah Johnson</div>
          <div class="text-sm text-slate-500">Product Manager</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
          <div class="flex items-center mb-4">
            <div class="text-yellow-400 flex">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            </div>
          </div>
          <p class="text-slate-600 mb-6">"The customer support is outstanding. They went above and beyond to help me solve my issue. 10/10 service."</p>
          <div class="font-bold text-slate-900">Michael Chen</div>
          <div class="text-sm text-slate-500">Developer</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
          <div class="flex items-center mb-4">
            <div class="text-yellow-400 flex">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            </div>
          </div>
          <p class="text-slate-600 mb-6">"Simple, intuitive, and powerful. Exactly what I was looking for. I've already recommended it to all my colleagues."</p>
          <div class="font-bold text-slate-900">Emily Davis</div>
          <div class="text-sm text-slate-500">Designer</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-002",
        "title": "Testimonials with Avatars",
        "description": "Testimonials with user photos",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="bg-slate-50 p-8 rounded-2xl flex flex-col md:flex-row gap-6 items-start">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full object-cover">
          <div>
            <p class="text-slate-600 italic mb-4">"I was blown away by the quality of the product. It exceeded all my expectations and has become an essential part of my daily routine."</p>
            <div class="font-bold text-slate-900">Alice Smith</div>
            <div class="text-sm text-slate-500">Marketing Director</div>
          </div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl flex flex-col md:flex-row gap-6 items-start">
          <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full object-cover">
          <div>
            <p class="text-slate-600 italic mb-4">"The team behind this is incredible. They listen to feedback and constantly improve the platform. A truly customer-centric company."</p>
            <div class="font-bold text-slate-900">Bob Williams</div>
            <div class="text-sm text-slate-500">CTO</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-003",
        "title": "Testimonials Carousel",
        "description": "Sliding testimonials",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24 text-white" x-data="{ active: 0, testimonials: [
      { text: 'This is the best service I have ever used. Period.', author: 'John Doe', role: 'CEO' },
      { text: 'Amazing experience from start to finish.', author: 'Jane Smith', role: 'Designer' },
      { text: 'Highly recommended for anyone looking to scale.', author: 'Mike Johnson', role: 'Founder' }
    ] }">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <div class="relative overflow-hidden min-h-[200px]">
        <template x-for="(testimonial, index) in testimonials" :key="index">
          <div x-show="active === index"
               x-transition:enter="transition ease-out duration-300"
               x-transition:enter-start="opacity-0 transform translate-x-10"
               x-transition:enter-end="opacity-100 transform translate-x-0"
               x-transition:leave="transition ease-in duration-300"
               x-transition:leave-start="opacity-100 transform translate-x-0"
               x-transition:leave-end="opacity-0 transform -translate-x-10"
               class="absolute inset-0 flex flex-col justify-center items-center">
            <p class="text-2xl md:text-4xl font-serif italic mb-8" x-text="'&ldquo;' + testimonial.text + '&rdquo;'"></p>
            <div>
              <div class="font-bold text-lg" x-text="testimonial.author"></div>
              <div class="text-slate-400" x-text="testimonial.role"></div>
            </div>
          </div>
        </template>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="flex justify-center gap-2 mt-8">
        <template x-for="(testimonial, index) in testimonials" :key="index">
          <button @click="active = index" class="w-3 h-3 rounded-full transition-colors" :class="active === index ? 'bg-white' : 'bg-slate-700 hover:bg-slate-600'"></button>
        </template>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-004",
        "title": "Testimonials with Star Ratings",
        "description": "Emphasis on ratings",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <div class="inline-block bg-yellow-50 text-yellow-700 px-4 py-2 rounded-full font-bold mb-8">
        Rated 4.9/5 by 10,000+ customers
      </div>
      <h2 class="text-3xl font-bold text-slate-900 mb-16">Don't just take our word for it</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-xl shadow-lg border border-slate-100">
          <div class="flex justify-center text-yellow-400 mb-4">
            ★★★★★
          </div>
          <h3 class="font-bold text-lg mb-2">"Game Changer"</h3>
          <p class="text-slate-600">"I've tried many alternatives, but this one stands out. The features are exactly what I needed."</p>
          <div class="mt-6 text-sm font-bold text-slate-900">- Alex P.</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-lg border border-slate-100">
          <div class="flex justify-center text-yellow-400 mb-4">
            ★★★★★
          </div>
          <h3 class="font-bold text-lg mb-2">"Worth Every Penny"</h3>
          <p class="text-slate-600">"The ROI on this tool is incredible. It paid for itself in the first week of use."</p>
          <div class="mt-6 text-sm font-bold text-slate-900">- Sarah M.</div>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-lg border border-slate-100">
          <div class="flex justify-center text-yellow-400 mb-4">
            ★★★★★
          </div>
          <h3 class="font-bold text-lg mb-2">"Stellar Support"</h3>
          <p class="text-slate-600">"Whenever I have a question, the support team responds within minutes. Truly impressive."</p>
          <div class="mt-6 text-sm font-bold text-slate-900">- David K.</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-005",
        "title": "Testimonials with Video",
        "description": "Video testimonials",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">See it in action</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="bg-white p-4 rounded-2xl shadow-sm">
          <div class="aspect-video bg-slate-200 rounded-xl relative group cursor-pointer overflow-hidden">
            <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Video thumbnail" class="w-full h-full object-cover transition-transform group-hover:scale-105">
            <div class="absolute inset-0 flex items-center justify-center bg-black/20 group-hover:bg-black/30 transition-colors">
              <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-lg">
                <svg class="w-8 h-8 text-primary-600 ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/></svg>
              </div>
            </div>
          </div>
          <div class="mt-6 px-4 pb-2">
            <blockquote class="text-lg font-medium text-slate-900">"It's simply the best tool for the job."</blockquote>
            <div class="mt-2 text-slate-500">- Mark Zuckerberg (Not really)</div>
          </div>
        </div>
        <div class="bg-white p-4 rounded-2xl shadow-sm">
          <div class="aspect-video bg-slate-200 rounded-xl relative group cursor-pointer overflow-hidden">
            <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Video thumbnail" class="w-full h-full object-cover transition-transform group-hover:scale-105">
            <div class="absolute inset-0 flex items-center justify-center bg-black/20 group-hover:bg-black/30 transition-colors">
              <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-lg">
                <svg class="w-8 h-8 text-primary-600 ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/></svg>
              </div>
            </div>
          </div>
          <div class="mt-6 px-4 pb-2">
            <blockquote class="text-lg font-medium text-slate-900">"Our team productivity doubled overnight."</blockquote>
            <div class="mt-2 text-slate-500">- Bill Gates (Also not really)</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-006",
        "title": "Testimonials with Company Logos",
        "description": "Logos of companies",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <p class="text-slate-500 font-bold uppercase tracking-widest mb-8">Trusted by innovative teams</p>
      <div class="flex flex-wrap justify-center gap-12 opacity-50 grayscale">
        <img src="https://tailwindui.com/img/logos/transistor-logo-gray-900.svg" alt="Transistor" class="h-8">
        <img src="https://tailwindui.com/img/logos/mirage-logo-gray-900.svg" alt="Mirage" class="h-8">
        <img src="https://tailwindui.com/img/logos/tuple-logo-gray-900.svg" alt="Tuple" class="h-8">
        <img src="https://tailwindui.com/img/logos/laravel-logo-gray-900.svg" alt="Laravel" class="h-8">
        <img src="https://tailwindui.com/img/logos/statamic-logo-gray-900.svg" alt="Statamic" class="h-8">
      </div>
      <div class="mt-16 max-w-3xl mx-auto">
        <blockquote class="text-2xl font-medium text-slate-900">
          "We use this platform for everything. It has streamlined our entire operation and saved us countless hours of manual work."
        </blockquote>
        <div class="mt-6 font-bold text-slate-900">Jennifer Wu</div>
        <div class="text-slate-500">VP of Operations, Tuple</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-007",
        "title": "Testimonials with Quote Icon",
        "description": "Large quote icon design",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-primary-600 py-24 text-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
      <div>
        <svg class="w-24 h-24 text-primary-400 opacity-50 mb-8" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
        <h2 class="text-4xl font-bold leading-tight">"The most flexible and powerful solution we have found."</h2>
        <div class="mt-8">
          <div class="font-bold text-xl">Marcus Aurelius</div>
          <div class="text-primary-200">Emperor of Rome</div>
        </div>
      </div>
      <div class="bg-primary-700 p-8 rounded-2xl border border-primary-500">
        <p class="text-lg text-primary-100 mb-6">"I was skeptical at first, but after the demo, I was sold. The implementation was smooth, and the results were immediate. I highly recommend this to anyone looking to improve their efficiency."</p>
        <div class="flex items-center gap-4">
          <div class="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center font-bold text-xl">MA</div>
          <div>
            <div class="font-bold">Marcus Aurelius</div>
            <div class="text-sm text-primary-300">Emperor</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-008",
        "title": "Testimonials Masonry",
        "description": "Masonry grid layout",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 columns-1 md:columns-3 gap-8 space-y-8">
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Short and sweet. Love it."</p>
        <div class="font-bold text-slate-900">- User A</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"This is a longer testimonial to show how the masonry layout handles different heights. It's really quite flexible and looks great with varied content lengths."</p>
        <div class="font-bold text-slate-900">- User B</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Another great review here. Five stars!"</p>
        <div class="font-bold text-slate-900">- User C</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"I use this every day. It's indispensable."</p>
        <div class="font-bold text-slate-900">- User D</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"The design is beautiful and the code is clean. A pleasure to work with."</p>
        <div class="font-bold text-slate-900">- User E</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Highly recommended."</p>
        <div class="font-bold text-slate-900">- User F</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-009",
        "title": "Testimonials with Background Image",
        "description": "Testimonial over image",
        "dir": "templates/07-testimonials",
        "content": """<div class="relative py-32 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');">
    <div class="absolute inset-0 bg-slate-900/80"></div>
    <div class="relative max-w-4xl mx-auto px-6 text-center text-white">
      <svg class="w-16 h-16 mx-auto text-white/30 mb-8" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
      <blockquote class="text-3xl md:text-5xl font-bold leading-tight mb-12">
        "It's rare to find a product that delivers exactly what it promises. This is one of those rare finds."
      </blockquote>
      <div class="flex items-center justify-center gap-4">
        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full border-2 border-white">
        <div class="text-left">
          <div class="font-bold">James Wilson</div>
          <div class="text-sm text-slate-300">Director of Sales</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-010",
        "title": "Testimonials with Slider",
        "description": "Horizontal scroll slider",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24 overflow-hidden">
    <div class="max-w-7xl mx-auto px-6 mb-12 flex justify-between items-end">
      <h2 class="text-3xl font-bold text-slate-900">Community Feedback</h2>
      <div class="flex gap-2">
        <button class="p-2 rounded-full border border-slate-300 hover:bg-slate-50 text-slate-600"><svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg></button>
        <button class="p-2 rounded-full border border-slate-300 hover:bg-slate-50 text-slate-600"><svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></button>
      </div>
    </div>
    <div class="flex gap-6 overflow-x-auto pb-8 px-6 snap-x snap-mandatory">
      <div class="min-w-[300px] md:min-w-[400px] bg-slate-50 p-8 rounded-2xl snap-center border border-slate-100">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 mb-6">"Absolutely fantastic. I use it every day."</p>
        <div class="font-bold text-slate-900">User 1</div>
      </div>
      <div class="min-w-[300px] md:min-w-[400px] bg-slate-50 p-8 rounded-2xl snap-center border border-slate-100">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 mb-6">"Saved me hours of work. Highly recommend."</p>
        <div class="font-bold text-slate-900">User 2</div>
      </div>
      <div class="min-w-[300px] md:min-w-[400px] bg-slate-50 p-8 rounded-2xl snap-center border border-slate-100">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 mb-6">"Great value for money. The best in class."</p>
        <div class="font-bold text-slate-900">User 3</div>
      </div>
      <div class="min-w-[300px] md:min-w-[400px] bg-slate-50 p-8 rounded-2xl snap-center border border-slate-100">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 mb-6">"Customer support is top notch."</p>
        <div class="font-bold text-slate-900">User 4</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-011",
        "title": "Testimonials with Card Design",
        "description": "Clean card layout",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-100 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div class="flex items-center gap-4 mb-4">
            <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-bold">JD</div>
            <div>
              <div class="font-bold text-slate-900">John Doe</div>
              <div class="text-xs text-slate-500">@johndoe</div>
            </div>
          </div>
          <p class="text-slate-600">"Just tried out this new tool and I'm impressed. The UI is clean and it's super fast."</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div class="flex items-center gap-4 mb-4">
            <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center text-green-600 font-bold">AS</div>
            <div>
              <div class="font-bold text-slate-900">Alice Smith</div>
              <div class="text-xs text-slate-500">@alicesmith</div>
            </div>
          </div>
          <p class="text-slate-600">"Finally a solution that actually works as advertised. Kudos to the team!"</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div class="flex items-center gap-4 mb-4">
            <div class="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 font-bold">MJ</div>
            <div>
              <div class="font-bold text-slate-900">Mike Jones</div>
              <div class="text-xs text-slate-500">@mikejones</div>
            </div>
          </div>
          <p class="text-slate-600">"I've been using this for a month now and I can't go back. It's that good."</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-012",
        "title": "Testimonials with Minimalist Design",
        "description": "Simple text focus",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6 text-center space-y-16">
      <div>
        <p class="text-xl md:text-2xl font-serif italic text-slate-800 mb-6">"The simplicity of the design is what caught my eye, but the functionality is what kept me."</p>
        <div class="font-bold text-slate-900 uppercase tracking-widest text-sm">Sarah Connor</div>
      </div>
      <hr class="border-slate-100 w-24 mx-auto">
      <div>
        <p class="text-xl md:text-2xl font-serif italic text-slate-800 mb-6">"I've never seen a team move this fast. They ship updates weekly and always listen to feedback."</p>
        <div class="font-bold text-slate-900 uppercase tracking-widest text-sm">John Connor</div>
      </div>
      <hr class="border-slate-100 w-24 mx-auto">
      <div>
        <p class="text-xl md:text-2xl font-serif italic text-slate-800 mb-6">"It just works. No fuss, no complications. Exactly what I needed."</p>
        <div class="font-bold text-slate-900 uppercase tracking-widest text-sm">Kyle Reese</div>
      </div>
    </div>
  </div>"""
    }
]
# Placeholder for Testimonials 013-025
# Part 7 continued: Testimonials 013-025
TEMPLATES_TEST_1_PART_2 = [
    {
        "id": "test-013",
        "title": "Testimonials with Dark Mode",
        "description": "Dark themed testimonials",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24 text-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">Loved by developers</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700">
          <p class="text-slate-300 mb-6">"The API is a joy to work with. Well documented and consistent."</p>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center font-bold">DV</div>
            <div>
              <div class="font-bold">Dev One</div>
              <div class="text-sm text-slate-400">Senior Engineer</div>
            </div>
          </div>
        </div>
        <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700">
          <p class="text-slate-300 mb-6">"Performance is incredible. We saw a 50% reduction in load times."</p>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center font-bold">DV</div>
            <div>
              <div class="font-bold">Dev Two</div>
              <div class="text-sm text-slate-400">Tech Lead</div>
            </div>
          </div>
        </div>
        <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700">
          <p class="text-slate-300 mb-6">"The support team really knows their stuff. Solved my issue in minutes."</p>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-purple-500 rounded-full flex items-center justify-center font-bold">DV</div>
            <div>
              <div class="font-bold">Dev Three</div>
              <div class="text-sm text-slate-400">CTO</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-014",
        "title": "Testimonials with Gradient Background",
        "description": "Colorful gradient background",
        "dir": "templates/07-testimonials",
        "content": """<div class="py-24 bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl text-white border border-white/20">
          <svg class="w-10 h-10 text-white/50 mb-6" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          <p class="text-xl font-medium mb-6">"The most beautiful and functional UI kit I've ever used. It makes building stunning interfaces a breeze."</p>
          <div class="font-bold">Sarah Jenkins</div>
          <div class="text-white/70 text-sm">UI/UX Designer</div>
        </div>
        <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl text-white border border-white/20">
          <svg class="w-10 h-10 text-white/50 mb-6" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          <p class="text-xl font-medium mb-6">"I was able to launch my startup in record time thanks to these templates. Highly recommended!"</p>
          <div class="font-bold">Mike Ross</div>
          <div class="text-white/70 text-sm">Founder</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-015",
        "title": "Testimonials with Social Proof",
        "description": "Numbers and stats",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
        <div>
          <h2 class="text-3xl font-bold text-slate-900 mb-6">Trusted by over 50,000 developers worldwide</h2>
          <p class="text-slate-600 text-lg mb-8">Join the community of creators building the future of the web with our tools.</p>
          <div class="grid grid-cols-2 gap-8">
            <div>
              <div class="text-4xl font-bold text-primary-600">99%</div>
              <div class="text-slate-500">Customer Satisfaction</div>
            </div>
            <div>
              <div class="text-4xl font-bold text-primary-600">24/7</div>
              <div class="text-slate-500">Support Availability</div>
            </div>
            <div>
              <div class="text-4xl font-bold text-primary-600">100+</div>
              <div class="text-slate-500">Countries Served</div>
            </div>
            <div>
              <div class="text-4xl font-bold text-primary-600">5M+</div>
              <div class="text-slate-500">API Requests Daily</div>
            </div>
          </div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
          <div class="flex gap-4 mb-6">
            <img src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full">
            <div>
              <div class="font-bold text-slate-900">Adam Sandler</div>
              <div class="text-sm text-slate-500">CEO, BigTech</div>
            </div>
          </div>
          <p class="text-slate-600 text-lg">"We switched to this platform last year and haven't looked back. The reliability and scalability are unmatched in the industry."</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-016",
        "title": "Testimonials with Twitter Style",
        "description": "Tweet-like cards",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Wall of Love</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-start mb-4">
            <div class="flex gap-3">
              <div class="w-10 h-10 bg-slate-200 rounded-full overflow-hidden">
                <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-full h-full object-cover">
              </div>
              <div>
                <div class="font-bold text-slate-900">Elon Musk</div>
                <div class="text-slate-500 text-sm">@elonmusk</div>
              </div>
            </div>
            <svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
          </div>
          <p class="text-slate-800">This product is fire! 🔥🚀 Can't believe I didn't find it sooner.</p>
          <div class="mt-4 text-slate-500 text-sm">10:42 AM · Oct 25, 2023</div>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-start mb-4">
            <div class="flex gap-3">
              <div class="w-10 h-10 bg-slate-200 rounded-full overflow-hidden">
                <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-full h-full object-cover">
              </div>
              <div>
                <div class="font-bold text-slate-900">Jeff Bezos</div>
                <div class="text-slate-500 text-sm">@jeffbezos</div>
              </div>
            </div>
            <svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
          </div>
          <p class="text-slate-800">Just shipped our new feature using this tool. Development time cut in half. Amazing work team! 👏</p>
          <div class="mt-4 text-slate-500 text-sm">2:15 PM · Oct 24, 2023</div>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-start mb-4">
            <div class="flex gap-3">
              <div class="w-10 h-10 bg-slate-200 rounded-full overflow-hidden">
                <img src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-full h-full object-cover">
              </div>
              <div>
                <div class="font-bold text-slate-900">Tim Cook</div>
                <div class="text-slate-500 text-sm">@tim_cook</div>
              </div>
            </div>
            <svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
          </div>
          <p class="text-slate-800">Good morning! Starting my day with this incredible dashboard. The UX is top notch. ☕️💻</p>
          <div class="mt-4 text-slate-500 text-sm">8:00 AM · Oct 26, 2023</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-017",
        "title": "Testimonials with LinkedIn Style",
        "description": "Professional post style",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-100 py-24">
    <div class="max-w-2xl mx-auto px-6 space-y-8">
      <div class="bg-white p-6 rounded-lg border border-slate-200 shadow-sm">
        <div class="flex gap-4 mb-4">
          <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full">
          <div>
            <div class="font-bold text-slate-900">Satya Nadella</div>
            <div class="text-sm text-slate-500">CEO at Microsoft</div>
            <div class="text-xs text-slate-400">2d • Edited</div>
          </div>
        </div>
        <p class="text-slate-800 mb-4">I'm thrilled to announce our partnership with this amazing platform. It has revolutionized how we approach cloud computing. The efficiency gains are undeniable. #Cloud #Innovation #Tech</p>
        <div class="border-t border-slate-100 pt-4 flex gap-6 text-slate-500 text-sm font-medium">
          <button class="flex items-center gap-2 hover:bg-slate-50 px-2 py-1 rounded"><span class="text-xl">👍</span> Like</button>
          <button class="flex items-center gap-2 hover:bg-slate-50 px-2 py-1 rounded"><span class="text-xl">💬</span> Comment</button>
          <button class="flex items-center gap-2 hover:bg-slate-50 px-2 py-1 rounded"><span class="text-xl">↗️</span> Share</button>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg border border-slate-200 shadow-sm">
        <div class="flex gap-4 mb-4">
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full">
          <div>
            <div class="font-bold text-slate-900">Sheryl Sandberg</div>
            <div class="text-sm text-slate-500">COO at Meta</div>
            <div class="text-xs text-slate-400">1w</div>
          </div>
        </div>
        <p class="text-slate-800 mb-4">Lean in to the future of work with this tool. It empowers teams to collaborate seamlessly, no matter where they are in the world. A must-have for any modern organization. #FutureOfWork #RemoteWork</p>
        <div class="border-t border-slate-100 pt-4 flex gap-6 text-slate-500 text-sm font-medium">
          <button class="flex items-center gap-2 hover:bg-slate-50 px-2 py-1 rounded"><span class="text-xl">👍</span> Like</button>
          <button class="flex items-center gap-2 hover:bg-slate-50 px-2 py-1 rounded"><span class="text-xl">💬</span> Comment</button>
          <button class="flex items-center gap-2 hover:bg-slate-50 px-2 py-1 rounded"><span class="text-xl">↗️</span> Share</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-018",
        "title": "Testimonials with Case Study Link",
        "description": "Link to full story",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
        <div class="bg-slate-100 rounded-2xl p-8 h-full flex flex-col justify-center">
          <img src="https://tailwindui.com/img/logos/workcation-logo-indigo-600.svg" alt="Workcation" class="h-8 mb-8 self-start">
          <blockquote class="text-2xl font-medium text-slate-900 mb-8">
            "We were able to increase our conversion rate by 300% within the first month of using this platform. The results speak for themselves."
          </blockquote>
          <div class="flex items-center gap-4 mb-8">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full">
            <div>
              <div class="font-bold text-slate-900">Judith Black</div>
              <div class="text-slate-500">CEO of Workcation</div>
            </div>
          </div>
          <a href="#" class="text-primary-600 font-bold hover:text-primary-700 flex items-center gap-2">
            Read the full case study
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </a>
        </div>
        <div class="space-y-8">
          <div class="border-l-4 border-slate-200 pl-6 py-2">
            <p class="text-slate-600 italic mb-4">"The onboarding process was seamless. We were up and running in days, not months."</p>
            <div class="font-bold text-slate-900">CTO, TechCorp</div>
            <a href="#" class="text-primary-600 text-sm font-bold mt-2 inline-block">Read story &rarr;</a>
          </div>
          <div class="border-l-4 border-slate-200 pl-6 py-2">
            <p class="text-slate-600 italic mb-4">"Our team loves the intuitive interface. Training time was minimal."</p>
            <div class="font-bold text-slate-900">HR Director, GlobalInc</div>
            <a href="#" class="text-primary-600 text-sm font-bold mt-2 inline-block">Read story &rarr;</a>
          </div>
          <div class="border-l-4 border-slate-200 pl-6 py-2">
            <p class="text-slate-600 italic mb-4">"The analytics provided are deep and actionable. We make better decisions now."</p>
            <div class="font-bold text-slate-900">VP Marketing, GrowthCo</div>
            <a href="#" class="text-primary-600 text-sm font-bold mt-2 inline-block">Read story &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-019",
        "title": "Testimonials with Audio Player",
        "description": "Audio testimonial",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="bg-white p-8 rounded-2xl shadow-lg flex flex-col md:flex-row items-center gap-8">
        <div class="flex-shrink-0">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-32 h-32 rounded-full object-cover border-4 border-slate-100">
        </div>
        <div class="flex-grow w-full">
          <h3 class="text-xl font-bold text-slate-900 mb-2">Listen to what John has to say</h3>
          <p class="text-slate-500 mb-6">John Smith, Creative Director at DesignStudio</p>

          <div class="bg-slate-100 rounded-full p-4 flex items-center gap-4">
            <button class="w-10 h-10 bg-primary-600 rounded-full flex items-center justify-center text-white hover:bg-primary-700 flex-shrink-0">
              <svg class="w-5 h-5 ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/></svg>
            </button>
            <div class="flex-grow h-2 bg-slate-300 rounded-full overflow-hidden relative">
              <div class="absolute top-0 left-0 h-full w-1/3 bg-primary-500"></div>
            </div>
            <div class="text-xs font-mono text-slate-500">0:45 / 2:15</div>
          </div>

          <div class="mt-6 p-4 bg-slate-50 rounded-lg border border-slate-100">
            <p class="text-slate-600 italic text-sm">"I just wanted to record this quick message to say how much I appreciate the work you guys have done..."</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-020",
        "title": "Testimonials with Before/After",
        "description": "Comparison testimonial",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Real Results</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
          <div class="flex items-center gap-4 mb-6">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full">
            <div>
              <div class="font-bold text-slate-900">Jane Doe</div>
              <div class="text-sm text-slate-500">Fitness Coach</div>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4 mb-6">
            <div class="bg-red-50 p-4 rounded-lg border border-red-100">
              <div class="text-xs font-bold text-red-600 uppercase mb-1">Before</div>
              <div class="text-slate-700 text-sm">Manual scheduling, missed appointments, chaos.</div>
            </div>
            <div class="bg-green-50 p-4 rounded-lg border border-green-100">
              <div class="text-xs font-bold text-green-600 uppercase mb-1">After</div>
              <div class="text-slate-700 text-sm">Automated booking, zero no-shows, peace of mind.</div>
            </div>
          </div>
          <p class="text-slate-600">"This software completely transformed my business. I went from being overwhelmed to having free time again."</p>
        </div>

        <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
          <div class="flex items-center gap-4 mb-6">
            <img src="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-12 h-12 rounded-full">
            <div>
              <div class="font-bold text-slate-900">Tom Brown</div>
              <div class="text-sm text-slate-500">E-commerce Owner</div>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4 mb-6">
            <div class="bg-red-50 p-4 rounded-lg border border-red-100">
              <div class="text-xs font-bold text-red-600 uppercase mb-1">Before</div>
              <div class="text-slate-700 text-sm">1% Conversion Rate, High Cart Abandonment.</div>
            </div>
            <div class="bg-green-50 p-4 rounded-lg border border-green-100">
              <div class="text-xs font-bold text-green-600 uppercase mb-1">After</div>
              <div class="text-slate-700 text-sm">4% Conversion Rate, Record Sales Month.</div>
            </div>
          </div>
          <p class="text-slate-600">"The optimization tools are incredible. We saw an immediate uplift in sales after implementing them."</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-021",
        "title": "Testimonials with Verified Badge",
        "description": "Verified purchase badge",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="flex items-center gap-2 text-green-600 text-xs font-bold uppercase tracking-wider mb-4">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          Verified Purchase
        </div>
        <div class="flex text-yellow-400 mb-2">★★★★★</div>
        <h3 class="font-bold text-slate-900 mb-2">Excellent Quality</h3>
        <p class="text-slate-600 text-sm mb-4">"The material is premium and feels great. Delivery was super fast too. Will definitely buy again."</p>
        <div class="text-xs text-slate-400">By Customer123 on Oct 12, 2023</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="flex items-center gap-2 text-green-600 text-xs font-bold uppercase tracking-wider mb-4">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          Verified Purchase
        </div>
        <div class="flex text-yellow-400 mb-2">★★★★★</div>
        <h3 class="font-bold text-slate-900 mb-2">Best in class</h3>
        <p class="text-slate-600 text-sm mb-4">"I compared several options before choosing this one. It's by far the best value for money."</p>
        <div class="text-xs text-slate-400">By TechGuru on Oct 15, 2023</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="flex items-center gap-2 text-green-600 text-xs font-bold uppercase tracking-wider mb-4">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          Verified Purchase
        </div>
        <div class="flex text-yellow-400 mb-2">★★★★★</div>
        <h3 class="font-bold text-slate-900 mb-2">Highly Recommended</h3>
        <p class="text-slate-600 text-sm mb-4">"Does exactly what it says on the tin. Very happy with my purchase."</p>
        <div class="text-xs text-slate-400">By HappyUser on Oct 18, 2023</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-022",
        "title": "Testimonials with Hover Effect",
        "description": "Interactive cards",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700 hover:border-primary-500 hover:bg-slate-750 transition-all duration-300 group cursor-default">
        <div class="w-12 h-12 bg-slate-700 rounded-full mb-6 group-hover:bg-primary-600 transition-colors flex items-center justify-center text-white font-bold">1</div>
        <p class="text-slate-400 group-hover:text-white transition-colors mb-6">"The attention to detail in this product is astounding. Every interaction feels polished."</p>
        <div class="font-bold text-white">User One</div>
      </div>
      <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700 hover:border-primary-500 hover:bg-slate-750 transition-all duration-300 group cursor-default">
        <div class="w-12 h-12 bg-slate-700 rounded-full mb-6 group-hover:bg-primary-600 transition-colors flex items-center justify-center text-white font-bold">2</div>
        <p class="text-slate-400 group-hover:text-white transition-colors mb-6">"I've never been more productive. It cuts out all the noise and lets me focus."</p>
        <div class="font-bold text-white">User Two</div>
      </div>
      <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700 hover:border-primary-500 hover:bg-slate-750 transition-all duration-300 group cursor-default">
        <div class="w-12 h-12 bg-slate-700 rounded-full mb-6 group-hover:bg-primary-600 transition-colors flex items-center justify-center text-white font-bold">3</div>
        <p class="text-slate-400 group-hover:text-white transition-colors mb-6">"Simple, elegant, and effective. I recommend it to everyone I know."</p>
        <div class="font-bold text-white">User Three</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-023",
        "title": "Testimonials with Tooltip",
        "description": "Hover for user details",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-12">Loved by experts</h2>
      <div class="flex flex-wrap justify-center gap-8">
        <div class="relative group">
          <img src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full border-2 border-white shadow-md cursor-help hover:scale-110 transition-transform">
          <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-64 bg-slate-900 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10 text-left">
            <p class="italic mb-2">"Incredible tool. Saved us months of dev time."</p>
            <div class="font-bold">Adam Sandler</div>
            <div class="text-slate-400 text-xs">CTO, TechCo</div>
            <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-900"></div>
          </div>
        </div>

        <div class="relative group">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full border-2 border-white shadow-md cursor-help hover:scale-110 transition-transform">
          <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-64 bg-slate-900 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10 text-left">
            <p class="italic mb-2">"Beautifully designed and easy to use."</p>
            <div class="font-bold">Emily Blunt</div>
            <div class="text-slate-400 text-xs">Designer, Studio</div>
            <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-900"></div>
          </div>
        </div>

        <div class="relative group">
          <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full border-2 border-white shadow-md cursor-help hover:scale-110 transition-transform">
          <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-64 bg-slate-900 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10 text-left">
            <p class="italic mb-2">"A game changer for our workflow."</p>
            <div class="font-bold">Mark Wahlberg</div>
            <div class="text-slate-400 text-xs">PM, AgileCorp</div>
            <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-900"></div>
          </div>
        </div>

        <div class="relative group">
          <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full border-2 border-white shadow-md cursor-help hover:scale-110 transition-transform">
          <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-64 bg-slate-900 text-white text-sm rounded-lg p-4 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10 text-left">
            <p class="italic mb-2">"Highly recommended for startups."</p>
            <div class="font-bold">Chris Evans</div>
            <div class="text-slate-400 text-xs">Founder, CapInc</div>
            <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 rotate-45 w-3 h-3 bg-slate-900"></div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-024",
        "title": "Testimonials with Modal",
        "description": "Click to read full review",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24" x-data="{ open: false, review: '', author: '' }">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-2xl shadow-sm cursor-pointer hover:shadow-md transition-shadow" @click="open = true; review = 'This is the full detailed review text that would be too long to show on the card itself. It goes into great detail about how the product helped solve specific problems and improved efficiency across the board. Highly recommended for anyone in a similar situation.'; author = 'User A'">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 line-clamp-3 mb-4">"This is the full detailed review text that would be too long to show on the card itself..."</p>
        <div class="font-bold text-slate-900">Read full review &rarr;</div>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm cursor-pointer hover:shadow-md transition-shadow" @click="open = true; review = 'Another long review here. The customer support was fantastic and helped me set everything up. The features are robust and the interface is intuitive. I have already recommended this to several colleagues.'; author = 'User B'">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 line-clamp-3 mb-4">"Another long review here. The customer support was fantastic and helped me set everything up..."</p>
        <div class="font-bold text-slate-900">Read full review &rarr;</div>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm cursor-pointer hover:shadow-md transition-shadow" @click="open = true; review = 'I was skeptical at first, but the free trial convinced me. The ROI has been positive from day one. It integrates perfectly with our existing stack and the API is very well documented.'; author = 'User C'">
        <div class="flex text-yellow-400 mb-4">★★★★★</div>
        <p class="text-slate-600 line-clamp-3 mb-4">"I was skeptical at first, but the free trial convinced me. The ROI has been positive from day one..."</p>
        <div class="font-bold text-slate-900">Read full review &rarr;</div>
      </div>
    </div>

    <script src="https://unpkg.com/alpinejs" defer></script>

    <!-- Modal -->
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm" x-show="open" style="display: none;">
      <div class="bg-white rounded-2xl p-8 max-w-lg w-full mx-4 shadow-2xl" @click.away="open = false">
        <div class="flex justify-between items-start mb-6">
          <div class="flex text-yellow-400 text-xl">★★★★★</div>
          <button @click="open = false" class="text-slate-400 hover:text-slate-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </div>
        <p class="text-slate-700 text-lg leading-relaxed mb-8" x-text="review"></p>
        <div class="font-bold text-slate-900" x-text="author"></div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-025",
        "title": "Testimonials with Sidebar",
        "description": "Sidebar layout",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-12">
    <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row gap-12">
      <div class="md:w-1/3">
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Why people love us</h2>
        <p class="text-slate-600 mb-8">We're proud to support thousands of customers around the world. Here's what they have to say about their experience.</p>
        <button class="px-6 py-3 bg-slate-900 text-white rounded-lg font-bold hover:bg-slate-800">Read more stories</button>
      </div>
      <div class="md:w-2/3 space-y-6">
        <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
          <p class="text-slate-700 mb-4">"The best decision we made this year was switching to this platform."</p>
          <div class="font-bold text-slate-900">- Company A</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
          <p class="text-slate-700 mb-4">"Incredible value for money. The features are top-notch."</p>
          <div class="font-bold text-slate-900">- Company B</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
          <p class="text-slate-700 mb-4">"Support is fast and helpful. They really care about their customers."</p>
          <div class="font-bold text-slate-900">- Company C</div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
# Part 8: Testimonials 026-038
TEMPLATES_TEST_2 = [
    {
        "id": "test-026",
        "title": "Testimonials with Quote Mark Background",
        "description": "Large quote mark design",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24 relative overflow-hidden">
    <div class="absolute top-0 left-0 text-slate-100 transform -translate-x-1/4 -translate-y-1/4">
      <svg class="w-96 h-96" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
    </div>
    <div class="relative max-w-4xl mx-auto px-6 text-center">
      <blockquote class="text-3xl md:text-5xl font-bold text-slate-900 leading-tight mb-12">
        "This is the single most important tool in our stack. It has completely transformed how we operate."
      </blockquote>
      <div class="flex items-center justify-center gap-4">
        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-16 h-16 rounded-full border-4 border-white shadow-lg">
        <div class="text-left">
          <div class="font-bold text-slate-900 text-lg">David Miller</div>
          <div class="text-slate-500">VP of Engineering</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-027",
        "title": "Testimonials with Zigzag Layout",
        "description": "Alternating layout",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="md:w-1/2">
          <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Team" class="rounded-2xl shadow-xl">
        </div>
        <div class="md:w-1/2">
          <svg class="w-12 h-12 text-primary-600 mb-6" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          <blockquote class="text-2xl font-bold text-slate-900 mb-6">
            "Our team collaboration has improved significantly. We are shipping faster and with fewer bugs."
          </blockquote>
          <div class="font-bold text-slate-900">Sarah Lee</div>
          <div class="text-slate-500">Product Manager</div>
        </div>
      </div>

      <div class="flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="md:w-1/2">
          <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Team" class="rounded-2xl shadow-xl">
        </div>
        <div class="md:w-1/2">
          <svg class="w-12 h-12 text-primary-600 mb-6" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          <blockquote class="text-2xl font-bold text-slate-900 mb-6">
            "The analytics dashboard gives us insights we never had before. It's a game changer for our strategy."
          </blockquote>
          <div class="font-bold text-slate-900">Mark Johnson</div>
          <div class="text-slate-500">Director of Marketing</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-028",
        "title": "Testimonials with Overlapping Images",
        "description": "Creative image layout",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center gap-16">
      <div class="md:w-1/2 relative">
        <div class="absolute top-0 left-0 w-64 h-64 bg-primary-100 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob"></div>
        <div class="absolute top-0 right-0 w-64 h-64 bg-purple-100 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-2000"></div>
        <div class="relative grid grid-cols-2 gap-4">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" alt="User" class="rounded-2xl shadow-lg transform translate-y-8">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" alt="User" class="rounded-2xl shadow-lg">
          <img src="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" alt="User" class="rounded-2xl shadow-lg transform translate-y-8">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" alt="User" class="rounded-2xl shadow-lg">
        </div>
      </div>
      <div class="md:w-1/2">
        <h2 class="text-3xl font-bold text-slate-900 mb-8">Join thousands of happy customers</h2>
        <div class="space-y-8">
          <div class="bg-slate-50 p-6 rounded-xl border-l-4 border-primary-600">
            <p class="text-slate-600 italic mb-4">"I can't imagine running my business without this. It handles everything."</p>
            <div class="font-bold text-slate-900">Jessica White</div>
          </div>
          <div class="bg-slate-50 p-6 rounded-xl border-l-4 border-purple-600">
            <p class="text-slate-600 italic mb-4">"The best investment we've made this year. The ROI is incredible."</p>
            <div class="font-bold text-slate-900">Robert Green</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-029",
        "title": "Testimonials with Vertical Slider",
        "description": "Vertical scrolling testimonials",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24 text-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center gap-16">
      <div class="md:w-1/2">
        <h2 class="text-4xl font-bold mb-6">Don't take our word for it</h2>
        <p class="text-slate-400 text-lg mb-8">See what our customers have to say about their experience using our platform to scale their businesses.</p>
        <button class="px-8 py-3 bg-primary-600 text-white rounded-lg font-bold hover:bg-primary-700 transition-colors">Read all reviews</button>
      </div>
      <div class="md:w-1/2 h-96 relative overflow-hidden mask-image-linear-gradient">
        <div class="absolute inset-0 animate-scroll-vertical space-y-6">
          <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <p class="text-slate-300 mb-4">"Absolutely amazing tool. Highly recommended!"</p>
            <div class="font-bold">User A</div>
          </div>
          <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <p class="text-slate-300 mb-4">"Saved us so much time and money."</p>
            <div class="font-bold">User B</div>
          </div>
          <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <p class="text-slate-300 mb-4">"Great support and even better product."</p>
            <div class="font-bold">User C</div>
          </div>
          <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <p class="text-slate-300 mb-4">"I use it every single day."</p>
            <div class="font-bold">User D</div>
          </div>
          <!-- Duplicate for seamless loop -->
          <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <p class="text-slate-300 mb-4">"Absolutely amazing tool. Highly recommended!"</p>
            <div class="font-bold">User A</div>
          </div>
          <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <p class="text-slate-300 mb-4">"Saved us so much time and money."</p>
            <div class="font-bold">User B</div>
          </div>
        </div>
      </div>
    </div>
    <style>
      @keyframes scroll-vertical {
        0% { transform: translateY(0); }
        100% { transform: translateY(-50%); }
      }
      .animate-scroll-vertical {
        animation: scroll-vertical 20s linear infinite;
      }
      .mask-image-linear-gradient {
        mask-image: linear-gradient(to bottom, transparent, black 10%, black 90%, transparent);
      }
    </style>
  </div>"""
    },
    {
        "id": "test-030",
        "title": "Testimonials with Tabbed Interface",
        "description": "Tabs for categories",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24" x-data="{ tab: 'developers' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900 mb-8">Feedback from everyone</h2>
        <div class="inline-flex bg-slate-100 rounded-lg p-1">
          <button @click="tab = 'developers'" :class="tab === 'developers' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-700'" class="px-6 py-2 rounded-md font-medium transition-all">Developers</button>
          <button @click="tab = 'designers'" :class="tab === 'designers' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-700'" class="px-6 py-2 rounded-md font-medium transition-all">Designers</button>
          <button @click="tab = 'managers'" :class="tab === 'managers' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-500 hover:text-slate-700'" class="px-6 py-2 rounded-md font-medium transition-all">Managers</button>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div x-show="tab === 'developers'" class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"The API is clean and well documented. A pleasure to integrate."</p>
          <div class="font-bold text-slate-900">Dev A</div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"Webhooks are reliable and fast. Great DX."</p>
          <div class="font-bold text-slate-900">Dev B</div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"CLI tool saves me hours every week."</p>
          <div class="font-bold text-slate-900">Dev C</div>
        </div>
      </div>

      <div x-show="tab === 'designers'" class="grid grid-cols-1 md:grid-cols-3 gap-8" style="display: none;">
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"The component library is beautiful and easy to customize."</p>
          <div class="font-bold text-slate-900">Designer A</div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"Figma kit is synced perfectly with the code."</p>
          <div class="font-bold text-slate-900">Designer B</div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"Love the attention to detail in the animations."</p>
          <div class="font-bold text-slate-900">Designer C</div>
        </div>
      </div>

      <div x-show="tab === 'managers'" class="grid grid-cols-1 md:grid-cols-3 gap-8" style="display: none;">
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"Reporting features give me the visibility I need."</p>
          <div class="font-bold text-slate-900">Manager A</div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"Team management is intuitive and secure."</p>
          <div class="font-bold text-slate-900">Manager B</div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <p class="text-slate-600 mb-6">"Billing is transparent and fair."</p>
          <div class="font-bold text-slate-900">Manager C</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-031",
        "title": "Testimonials with Video Modal",
        "description": "Video popup",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24" x-data="{ open: false, videoUrl: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-white">Watch their stories</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="relative group cursor-pointer" @click="open = true; videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ'">
          <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Thumbnail" class="rounded-xl w-full h-64 object-cover opacity-80 group-hover:opacity-100 transition-opacity">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-16 h-16 bg-white/20 backdrop-blur rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-white ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-4 left-4 text-white font-bold">Success Story: Acme Corp</div>
        </div>
        <div class="relative group cursor-pointer" @click="open = true; videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ'">
          <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Thumbnail" class="rounded-xl w-full h-64 object-cover opacity-80 group-hover:opacity-100 transition-opacity">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-16 h-16 bg-white/20 backdrop-blur rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-white ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-4 left-4 text-white font-bold">Success Story: Beta Inc</div>
        </div>
        <div class="relative group cursor-pointer" @click="open = true; videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ'">
          <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Thumbnail" class="rounded-xl w-full h-64 object-cover opacity-80 group-hover:opacity-100 transition-opacity">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-16 h-16 bg-white/20 backdrop-blur rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-white ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-4 left-4 text-white font-bold">Success Story: Gamma Ltd</div>
        </div>
      </div>
    </div>

    <script src="https://unpkg.com/alpinejs" defer></script>

    <!-- Modal -->
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-sm" x-show="open" style="display: none;">
      <div class="relative w-full max-w-4xl mx-4 aspect-video bg-black rounded-xl overflow-hidden shadow-2xl" @click.away="open = false">
        <button @click="open = false" class="absolute top-4 right-4 text-white/50 hover:text-white z-10">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
        <iframe :src="videoUrl" class="w-full h-full" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-032",
        "title": "Testimonials with Rating Bars",
        "description": "Detailed rating breakdown",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-16">
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Customer Reviews</h2>
        <div class="flex items-center gap-4 mb-8">
          <div class="text-5xl font-bold text-slate-900">4.8</div>
          <div>
            <div class="flex text-yellow-400 text-xl">★★★★★</div>
            <div class="text-slate-500">Based on 1,234 reviews</div>
          </div>
        </div>
        <div class="space-y-3">
          <div class="flex items-center gap-4">
            <div class="w-12 text-sm font-bold text-slate-600">5 star</div>
            <div class="flex-grow h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-yellow-400 w-[80%]"></div>
            </div>
            <div class="w-12 text-sm text-slate-500 text-right">80%</div>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-12 text-sm font-bold text-slate-600">4 star</div>
            <div class="flex-grow h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-yellow-400 w-[15%]"></div>
            </div>
            <div class="w-12 text-sm text-slate-500 text-right">15%</div>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-12 text-sm font-bold text-slate-600">3 star</div>
            <div class="flex-grow h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-yellow-400 w-[3%]"></div>
            </div>
            <div class="w-12 text-sm text-slate-500 text-right">3%</div>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-12 text-sm font-bold text-slate-600">2 star</div>
            <div class="flex-grow h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-yellow-400 w-[1%]"></div>
            </div>
            <div class="w-12 text-sm text-slate-500 text-right">1%</div>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-12 text-sm font-bold text-slate-600">1 star</div>
            <div class="flex-grow h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-yellow-400 w-[1%]"></div>
            </div>
            <div class="w-12 text-sm text-slate-500 text-right">1%</div>
          </div>
        </div>
      </div>
      <div class="space-y-6">
        <div class="border-b border-slate-100 pb-6">
          <div class="flex justify-between items-start mb-2">
            <div class="font-bold text-slate-900">Great product</div>
            <div class="text-slate-400 text-sm">2 days ago</div>
          </div>
          <div class="flex text-yellow-400 text-sm mb-2">★★★★★</div>
          <p class="text-slate-600">"Exactly what I was looking for. Works perfectly."</p>
        </div>
        <div class="border-b border-slate-100 pb-6">
          <div class="flex justify-between items-start mb-2">
            <div class="font-bold text-slate-900">Good value</div>
            <div class="text-slate-400 text-sm">1 week ago</div>
          </div>
          <div class="flex text-yellow-400 text-sm mb-2">★★★★☆</div>
          <p class="text-slate-600">"Very good for the price. Missing one minor feature but otherwise great."</p>
        </div>
        <div class="border-b border-slate-100 pb-6">
          <div class="flex justify-between items-start mb-2">
            <div class="font-bold text-slate-900">Excellent support</div>
            <div class="text-slate-400 text-sm">2 weeks ago</div>
          </div>
          <div class="flex text-yellow-400 text-sm mb-2">★★★★★</div>
          <p class="text-slate-600">"Had an issue and they fixed it immediately."</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-033",
        "title": "Testimonials with Circular Progress",
        "description": "Visual stats",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
      <div class="bg-white p-8 rounded-2xl shadow-sm">
        <div class="relative w-32 h-32 mx-auto mb-6">
          <svg class="w-full h-full transform -rotate-90">
            <circle cx="64" cy="64" r="60" stroke="currentColor" stroke-width="8" fill="transparent" class="text-slate-100" />
            <circle cx="64" cy="64" r="60" stroke="currentColor" stroke-width="8" fill="transparent" stroke-dasharray="377" stroke-dashoffset="37" class="text-green-500" />
          </svg>
          <div class="absolute inset-0 flex items-center justify-center text-3xl font-bold text-slate-900">90%</div>
        </div>
        <h3 class="text-xl font-bold text-slate-900 mb-2">Efficiency Increase</h3>
        <p class="text-slate-600">"Our team is working 90% faster since we switched."</p>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm">
        <div class="relative w-32 h-32 mx-auto mb-6">
          <svg class="w-full h-full transform -rotate-90">
            <circle cx="64" cy="64" r="60" stroke="currentColor" stroke-width="8" fill="transparent" class="text-slate-100" />
            <circle cx="64" cy="64" r="60" stroke="currentColor" stroke-width="8" fill="transparent" stroke-dasharray="377" stroke-dashoffset="18" class="text-blue-500" />
          </svg>
          <div class="absolute inset-0 flex items-center justify-center text-3xl font-bold text-slate-900">95%</div>
        </div>
        <h3 class="text-xl font-bold text-slate-900 mb-2">Customer Satisfaction</h3>
        <p class="text-slate-600">"Our customers love the new interface."</p>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow-sm">
        <div class="relative w-32 h-32 mx-auto mb-6">
          <svg class="w-full h-full transform -rotate-90">
            <circle cx="64" cy="64" r="60" stroke="currentColor" stroke-width="8" fill="transparent" class="text-slate-100" />
            <circle cx="64" cy="64" r="60" stroke="currentColor" stroke-width="8" fill="transparent" stroke-dasharray="377" stroke-dashoffset="0" class="text-purple-500" />
          </svg>
          <div class="absolute inset-0 flex items-center justify-center text-3xl font-bold text-slate-900">100%</div>
        </div>
        <h3 class="text-xl font-bold text-slate-900 mb-2">Uptime</h3>
        <p class="text-slate-600">"Rock solid reliability we can count on."</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-034",
        "title": "Testimonials with Timeline",
        "description": "Customer journey timeline",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 text-center mb-16">A Customer's Journey</h2>
      <div class="relative border-l-2 border-slate-200 ml-4 md:ml-0 space-y-12">
        <div class="relative pl-8 md:pl-0">
          <div class="absolute top-0 left-[-9px] w-4 h-4 rounded-full bg-primary-600 border-4 border-white shadow-sm"></div>
          <div class="md:flex items-start justify-between group">
            <div class="md:w-5/12 md:text-right md:pr-8 order-1">
              <div class="font-bold text-slate-900 text-lg">Day 1: Discovery</div>
              <div class="text-slate-500 text-sm mb-2">Jan 1, 2023</div>
              <p class="text-slate-600 italic">"I stumbled upon this tool while searching for a solution to my scheduling nightmare. The landing page spoke directly to my pain points."</p>
            </div>
            <div class="md:w-5/12 md:pl-8 order-2"></div>
          </div>
        </div>
        <div class="relative pl-8 md:pl-0">
          <div class="absolute top-0 left-[-9px] w-4 h-4 rounded-full bg-primary-600 border-4 border-white shadow-sm"></div>
          <div class="md:flex items-start justify-between group">
            <div class="md:w-5/12 md:text-right md:pr-8 order-1"></div>
            <div class="md:w-5/12 md:pl-8 order-2">
              <div class="font-bold text-slate-900 text-lg">Day 7: Implementation</div>
              <div class="text-slate-500 text-sm mb-2">Jan 7, 2023</div>
              <p class="text-slate-600 italic">"Setup was surprisingly easy. I imported my data and was up and running in less than an hour. The support team answered my one question instantly."</p>
            </div>
          </div>
        </div>
        <div class="relative pl-8 md:pl-0">
          <div class="absolute top-0 left-[-9px] w-4 h-4 rounded-full bg-primary-600 border-4 border-white shadow-sm"></div>
          <div class="md:flex items-start justify-between group">
            <div class="md:w-5/12 md:text-right md:pr-8 order-1">
              <div class="font-bold text-slate-900 text-lg">Day 30: Results</div>
              <div class="text-slate-500 text-sm mb-2">Jan 30, 2023</div>
              <p class="text-slate-600 italic">"I've saved over 20 hours of manual work this month alone. My clients love the new booking system. I'm a customer for life."</p>
            </div>
            <div class="md:w-5/12 md:pl-8 order-2"></div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-035",
        "title": "Testimonials with Map",
        "description": "Global customer base",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24 relative overflow-hidden">
    <div class="absolute inset-0 opacity-20">
      <!-- Simplified World Map SVG Background -->
      <svg class="w-full h-full text-slate-500" fill="currentColor" viewBox="0 0 1000 500"><path d="M... (Map path would go here) ..." /></svg>
      <div class="w-full h-full bg-[url('https://upload.wikimedia.org/wikipedia/commons/8/80/World_map_-_low_resolution.svg')] bg-cover bg-center opacity-30 grayscale"></div>
    </div>
    <div class="relative max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-white">Loved around the world</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-slate-800/80 backdrop-blur p-6 rounded-xl border border-slate-700">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-2xl">🇺🇸</span>
            <div class="font-bold text-white">New York, USA</div>
          </div>
          <p class="text-slate-300">"The best tool for remote teams, hands down."</p>
        </div>
        <div class="bg-slate-800/80 backdrop-blur p-6 rounded-xl border border-slate-700">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-2xl">🇬🇧</span>
            <div class="font-bold text-white">London, UK</div>
          </div>
          <p class="text-slate-300">"Brilliant service and support."</p>
        </div>
        <div class="bg-slate-800/80 backdrop-blur p-6 rounded-xl border border-slate-700">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-2xl">🇯🇵</span>
            <div class="font-bold text-white">Tokyo, Japan</div>
          </div>
          <p class="text-slate-300">"Very reliable and efficient."</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-036",
        "title": "Testimonials with Filter",
        "description": "Filter by category",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24" x-data="{ filter: 'all' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex flex-col md:flex-row justify-between items-center mb-12 gap-4">
        <h2 class="text-3xl font-bold text-slate-900">Success Stories</h2>
        <div class="flex gap-2">
          <button @click="filter = 'all'" :class="filter === 'all' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-full text-sm font-medium transition-colors">All</button>
          <button @click="filter = 'tech'" :class="filter === 'tech' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-full text-sm font-medium transition-colors">Tech</button>
          <button @click="filter = 'marketing'" :class="filter === 'marketing' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-full text-sm font-medium transition-colors">Marketing</button>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div x-show="filter === 'all' || filter === 'tech'" class="bg-slate-50 p-8 rounded-2xl">
          <div class="text-xs font-bold text-blue-600 uppercase mb-2">Tech</div>
          <p class="text-slate-600 mb-4">"Great for developers."</p>
          <div class="font-bold text-slate-900">User A</div>
        </div>
        <div x-show="filter === 'all' || filter === 'marketing'" class="bg-slate-50 p-8 rounded-2xl">
          <div class="text-xs font-bold text-green-600 uppercase mb-2">Marketing</div>
          <p class="text-slate-600 mb-4">"Boosted our SEO."</p>
          <div class="font-bold text-slate-900">User B</div>
        </div>
        <div x-show="filter === 'all' || filter === 'tech'" class="bg-slate-50 p-8 rounded-2xl">
          <div class="text-xs font-bold text-blue-600 uppercase mb-2">Tech</div>
          <p class="text-slate-600 mb-4">"Clean code."</p>
          <div class="font-bold text-slate-900">User C</div>
        </div>
        <div x-show="filter === 'all' || filter === 'marketing'" class="bg-slate-50 p-8 rounded-2xl">
          <div class="text-xs font-bold text-green-600 uppercase mb-2">Marketing</div>
          <p class="text-slate-600 mb-4">"High conversion."</p>
          <div class="font-bold text-slate-900">User D</div>
        </div>
        <div x-show="filter === 'all' || filter === 'tech'" class="bg-slate-50 p-8 rounded-2xl">
          <div class="text-xs font-bold text-blue-600 uppercase mb-2">Tech</div>
          <p class="text-slate-600 mb-4">"Scalable architecture."</p>
          <div class="font-bold text-slate-900">User E</div>
        </div>
        <div x-show="filter === 'all' || filter === 'marketing'" class="bg-slate-50 p-8 rounded-2xl">
          <div class="text-xs font-bold text-green-600 uppercase mb-2">Marketing</div>
          <p class="text-slate-600 mb-4">"Easy to use."</p>
          <div class="font-bold text-slate-900">User F</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-037",
        "title": "Testimonials with Search",
        "description": "Searchable reviews",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24" x-data="{ search: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="max-w-xl mx-auto mb-12">
        <div class="relative">
          <input type="text" x-model="search" placeholder="Search reviews (e.g., 'support', 'fast', 'easy')..." class="w-full px-6 py-4 rounded-full border border-slate-200 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500">
          <svg class="w-6 h-6 text-slate-400 absolute right-4 top-1/2 transform -translate-y-1/2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-2xl shadow-sm" x-show="'Great support team'.toLowerCase().includes(search.toLowerCase()) || search === ''">
          <p class="text-slate-600 mb-4">"Great support team. They helped me solve my issue in minutes."</p>
          <div class="font-bold text-slate-900">User 1</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm" x-show="'Fast and reliable'.toLowerCase().includes(search.toLowerCase()) || search === ''">
          <p class="text-slate-600 mb-4">"Fast and reliable service. I've never had any downtime."</p>
          <div class="font-bold text-slate-900">User 2</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm" x-show="'Easy to use'.toLowerCase().includes(search.toLowerCase()) || search === ''">
          <p class="text-slate-600 mb-4">"Easy to use interface. My grandmother could use this."</p>
          <div class="font-bold text-slate-900">User 3</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm" x-show="'Affordable pricing'.toLowerCase().includes(search.toLowerCase()) || search === ''">
          <p class="text-slate-600 mb-4">"Affordable pricing for the value you get. Highly recommended."</p>
          <div class="font-bold text-slate-900">User 4</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm" x-show="'Feature rich'.toLowerCase().includes(search.toLowerCase()) || search === ''">
          <p class="text-slate-600 mb-4">"Feature rich platform. It has everything I need and more."</p>
          <div class="font-bold text-slate-900">User 5</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm" x-show="'Beautiful design'.toLowerCase().includes(search.toLowerCase()) || search === ''">
          <p class="text-slate-600 mb-4">"Beautiful design. It makes my work look professional."</p>
          <div class="font-bold text-slate-900">User 6</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-038",
        "title": "Testimonials with Pagination",
        "description": "Paginated reviews",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24" x-data="{ page: 1 }">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 text-center mb-12">Latest Reviews</h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        <!-- Page 1 -->
        <template x-if="page === 1">
          <div class="contents">
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 1 Review A. Excellent."</p>
              <div class="font-bold">User 1A</div>
            </div>
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 1 Review B. Superb."</p>
              <div class="font-bold">User 1B</div>
            </div>
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 1 Review C. Outstanding."</p>
              <div class="font-bold">User 1C</div>
            </div>
          </div>
        </template>

        <!-- Page 2 -->
        <template x-if="page === 2">
          <div class="contents">
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 2 Review A. Fantastic."</p>
              <div class="font-bold">User 2A</div>
            </div>
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 2 Review B. Brilliant."</p>
              <div class="font-bold">User 2B</div>
            </div>
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 2 Review C. Wonderful."</p>
              <div class="font-bold">User 2C</div>
            </div>
          </div>
        </template>

        <!-- Page 3 -->
        <template x-if="page === 3">
          <div class="contents">
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 3 Review A. Amazing."</p>
              <div class="font-bold">User 3A</div>
            </div>
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 3 Review B. Great."</p>
              <div class="font-bold">User 3B</div>
            </div>
            <div class="bg-slate-50 p-8 rounded-2xl border border-slate-100">
              <p class="text-slate-600 mb-4">"Page 3 Review C. Good."</p>
              <div class="font-bold">User 3C</div>
            </div>
          </div>
        </template>
      </div>

      <script src="https://unpkg.com/alpinejs" defer></script>

      <div class="flex justify-center gap-2">
        <button @click="page = 1" :class="page === 1 ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="w-10 h-10 rounded-full font-bold transition-colors">1</button>
        <button @click="page = 2" :class="page === 2 ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="w-10 h-10 rounded-full font-bold transition-colors">2</button>
        <button @click="page = 3" :class="page === 3 ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="w-10 h-10 rounded-full font-bold transition-colors">3</button>
      </div>
    </div>
  </div>"""
    }
]
# Placeholder for Testimonials 039-050
# Part 8 continued: Testimonials 039-050
TEMPLATES_TEST_2_PART_2 = [
    {
        "id": "test-039",
        "title": "Testimonials with Masonry Layout",
        "description": "Masonry grid layout",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 columns-1 md:columns-3 gap-8 space-y-8">
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Short and sweet review."</p>
        <div class="font-bold text-slate-900">User A</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"This is a much longer review that spans multiple lines. It goes into detail about how the product helped them achieve their goals and why they would recommend it to others. The masonry layout handles this variable height perfectly."</p>
        <div class="font-bold text-slate-900">User B</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Medium length review here. Good product, good service."</p>
        <div class="font-bold text-slate-900">User C</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Another short one."</p>
        <div class="font-bold text-slate-900">User D</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"And another long one to balance things out. The design is really flexible and looks great on all devices. I'm very happy with the purchase."</p>
        <div class="font-bold text-slate-900">User E</div>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm break-inside-avoid">
        <p class="text-slate-600 mb-4">"Just perfect."</p>
        <div class="font-bold text-slate-900">User F</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-040",
        "title": "Testimonials with Sticky Header",
        "description": "Sticky section header",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row gap-16">
      <div class="md:w-1/3">
        <div class="sticky top-8">
          <h2 class="text-4xl font-bold text-slate-900 mb-6">What our clients say</h2>
          <p class="text-slate-600 text-lg mb-8">We are trusted by the world's most innovative companies.</p>
          <a href="#" class="text-primary-600 font-bold hover:text-primary-700 flex items-center gap-2">
            Read all 500+ reviews
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </a>
        </div>
      </div>
      <div class="md:w-2/3 space-y-12">
        <div class="bg-slate-50 p-8 rounded-2xl">
          <div class="flex text-yellow-400 mb-4">★★★★★</div>
          <p class="text-slate-700 text-lg mb-6">"The platform is incredibly robust. We've thrown everything at it and it hasn't flinched."</p>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-slate-200 rounded-full"></div>
            <div>
              <div class="font-bold text-slate-900">John Doe</div>
              <div class="text-slate-500 text-sm">CTO, TechCorp</div>
            </div>
          </div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <div class="flex text-yellow-400 mb-4">★★★★★</div>
          <p class="text-slate-700 text-lg mb-6">"Customer service is top notch. They really go above and beyond to help you succeed."</p>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-slate-200 rounded-full"></div>
            <div>
              <div class="font-bold text-slate-900">Jane Smith</div>
              <div class="text-slate-500 text-sm">VP Sales, GrowthCo</div>
            </div>
          </div>
        </div>
        <div class="bg-slate-50 p-8 rounded-2xl">
          <div class="flex text-yellow-400 mb-4">★★★★★</div>
          <p class="text-slate-700 text-lg mb-6">"I would recommend this to anyone looking to scale their business efficiently."</p>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-slate-200 rounded-full"></div>
            <div>
              <div class="font-bold text-slate-900">Mike Johnson</div>
              <div class="text-slate-500 text-sm">Founder, StartupInc</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-041",
        "title": "Testimonials with Floating Avatars",
        "description": "Avatars floating around text",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-32 overflow-hidden relative">
    <div class="absolute inset-0 flex items-center justify-center">
      <div class="w-[800px] h-[800px] bg-primary-900/20 rounded-full blur-3xl"></div>
    </div>
    <div class="relative max-w-4xl mx-auto px-6 text-center z-10">
      <h2 class="text-4xl md:text-6xl font-bold text-white mb-8">Loved by thousands of creators</h2>
      <p class="text-xl text-slate-400 mb-12 max-w-2xl mx-auto">Join the community that is building the future of the web.</p>
      <button class="px-8 py-4 bg-white text-slate-900 rounded-full font-bold hover:bg-slate-100 transition-colors">Get Started</button>
    </div>

    <!-- Floating Avatars (Positioned absolutely) -->
    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="absolute top-20 left-10 w-16 h-16 rounded-full border-2 border-slate-800 animate-float" style="animation-delay: 0s;">
    <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="absolute top-40 right-20 w-20 h-20 rounded-full border-2 border-slate-800 animate-float" style="animation-delay: 2s;">
    <img src="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="absolute bottom-20 left-1/4 w-14 h-14 rounded-full border-2 border-slate-800 animate-float" style="animation-delay: 4s;">
    <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="absolute bottom-40 right-1/3 w-18 h-18 rounded-full border-2 border-slate-800 animate-float" style="animation-delay: 1s;">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="absolute top-1/3 left-10 w-12 h-12 rounded-full border-2 border-slate-800 animate-float" style="animation-delay: 3s;">

    <style>
      @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
      }
      .animate-float {
        animation: float 6s ease-in-out infinite;
      }
    </style>
  </div>"""
    },
    {
        "id": "test-042",
        "title": "Testimonials with Chat Bubbles",
        "description": "Conversation style",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-3xl mx-auto px-6 space-y-8">
      <div class="flex items-end gap-4">
        <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-10 h-10 rounded-full mb-1">
        <div class="bg-white p-4 rounded-2xl rounded-bl-none shadow-sm max-w-md">
          <p class="text-slate-700">Hey, have you tried the new update yet?</p>
        </div>
      </div>
      <div class="flex items-end gap-4 flex-row-reverse">
        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-10 h-10 rounded-full mb-1">
        <div class="bg-primary-600 p-4 rounded-2xl rounded-br-none shadow-sm max-w-md text-white">
          <p>Yes! It's incredible. The new features are exactly what we needed.</p>
        </div>
      </div>
      <div class="flex items-end gap-4">
        <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-10 h-10 rounded-full mb-1">
        <div class="bg-white p-4 rounded-2xl rounded-bl-none shadow-sm max-w-md">
          <p class="text-slate-700">I know right? It's going to save us so much time.</p>
        </div>
      </div>
      <div class="flex items-end gap-4 flex-row-reverse">
        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-10 h-10 rounded-full mb-1">
        <div class="bg-primary-600 p-4 rounded-2xl rounded-br-none shadow-sm max-w-md text-white">
          <p>Absolutely. Best investment we've made this year. 🚀</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-043",
        "title": "Testimonials with Video Background",
        "description": "Immersive video background",
        "dir": "templates/07-testimonials",
        "content": """<div class="relative py-32 overflow-hidden">
    <div class="absolute inset-0">
      <video class="w-full h-full object-cover" autoplay muted loop playsinline>
        <source src="https://assets.mixkit.co/videos/preview/mixkit-people-working-in-a-modern-office-4348-large.mp4" type="video/mp4">
      </video>
      <div class="absolute inset-0 bg-slate-900/80"></div>
    </div>
    <div class="relative max-w-4xl mx-auto px-6 text-center text-white" x-data="{ active: 0, testimonials: [
      { text: 'This platform has completely revolutionized our workflow. We are faster, more efficient, and happier.', author: 'Sarah Jenkins', role: 'CEO, TechStart' },
      { text: 'The best decision we made was switching to this tool. The ROI was immediate.', author: 'Mike Ross', role: 'Founder, GrowthLabs' },
      { text: 'Incredible support and a rock-solid product. Highly recommended.', author: 'Jessica Pearson', role: 'Managing Partner, Pearson Hardman' }
    ] }">
      <div class="mb-12">
        <svg class="w-16 h-16 mx-auto text-primary-500 mb-8" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
        <template x-for="(t, index) in testimonials" :key="index">
          <div x-show="active === index" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform scale-95" x-transition:enter-end="opacity-100 transform scale-100">
            <blockquote class="text-3xl md:text-5xl font-bold leading-tight mb-8" x-text="'&quot;' + t.text + '&quot;'"></blockquote>
            <div class="font-bold text-xl" x-text="t.author"></div>
            <div class="text-slate-400" x-text="t.role"></div>
          </div>
        </template>
      </div>
      <div class="flex justify-center gap-4">
        <template x-for="(t, index) in testimonials" :key="index">
          <button @click="active = index" :class="active === index ? 'bg-white w-8' : 'bg-white/30 w-4 hover:bg-white/50'" class="h-2 rounded-full transition-all duration-300"></button>
        </template>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "test-044",
        "title": "Testimonials with Parallax",
        "description": "Parallax scrolling effect",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
      <div class="space-y-8">
        <div class="bg-white p-8 rounded-2xl shadow-lg transform hover:-translate-y-2 transition-transform duration-300">
          <p class="text-slate-600 mb-6">"The design quality is unmatched. Every pixel is perfect."</p>
          <div class="font-bold text-slate-900">Designer One</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-lg transform translate-x-8 hover:-translate-y-2 transition-transform duration-300">
          <p class="text-slate-600 mb-6">"Code is clean, modular, and easy to extend. A developer's dream."</p>
          <div class="font-bold text-slate-900">Developer Two</div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-lg transform hover:-translate-y-2 transition-transform duration-300">
          <p class="text-slate-600 mb-6">"Support helped me launch in record time. Forever grateful."</p>
          <div class="font-bold text-slate-900">Founder Three</div>
        </div>
      </div>
      <div class="relative">
        <div class="absolute inset-0 bg-gradient-to-tr from-primary-500 to-purple-500 rounded-full blur-3xl opacity-20 animate-pulse"></div>
        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Team" class="relative rounded-2xl shadow-2xl transform rotate-3 hover:rotate-0 transition-transform duration-500">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-045",
        "title": "Testimonials with 3D Cards",
        "description": "3D tilt effect",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24 perspective-1000">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="group h-96 w-full [perspective:1000px]">
        <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
          <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-800 p-8 flex flex-col items-center justify-center text-center [backface-visibility:hidden]">
            <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-24 h-24 rounded-full mb-6 border-4 border-primary-500">
            <h3 class="text-xl font-bold text-white mb-2">John Doe</h3>
            <p class="text-slate-400">CEO, TechCorp</p>
            <p class="mt-6 text-primary-400 font-bold">Hover to read review &rarr;</p>
          </div>
          <div class="absolute inset-0 h-full w-full rounded-xl bg-primary-600 p-8 flex items-center justify-center text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden]">
            <p class="text-lg">"This product has completely transformed our workflow. We are 3x more productive now."</p>
          </div>
        </div>
      </div>

      <div class="group h-96 w-full [perspective:1000px]">
        <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
          <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-800 p-8 flex flex-col items-center justify-center text-center [backface-visibility:hidden]">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-24 h-24 rounded-full mb-6 border-4 border-primary-500">
            <h3 class="text-xl font-bold text-white mb-2">Jane Smith</h3>
            <p class="text-slate-400">Designer, CreativeStudio</p>
            <p class="mt-6 text-primary-400 font-bold">Hover to read review &rarr;</p>
          </div>
          <div class="absolute inset-0 h-full w-full rounded-xl bg-primary-600 p-8 flex items-center justify-center text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden]">
            <p class="text-lg">"The attention to detail is amazing. It's rare to find such high quality work."</p>
          </div>
        </div>
      </div>

      <div class="group h-96 w-full [perspective:1000px]">
        <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
          <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-800 p-8 flex flex-col items-center justify-center text-center [backface-visibility:hidden]">
            <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-24 h-24 rounded-full mb-6 border-4 border-primary-500">
            <h3 class="text-xl font-bold text-white mb-2">Mike Johnson</h3>
            <p class="text-slate-400">Dev, CodeHouse</p>
            <p class="mt-6 text-primary-400 font-bold">Hover to read review &rarr;</p>
          </div>
          <div class="absolute inset-0 h-full w-full rounded-xl bg-primary-600 p-8 flex items-center justify-center text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden]">
            <p class="text-lg">"Clean code, great documentation, and excellent support. What more could you ask for?"</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-046",
        "title": "Testimonials with Spotlight",
        "description": "Spotlight hover effect",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="group relative rounded-2xl bg-slate-800 p-8 border border-white/10 hover:border-white/20 transition-colors overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-r from-primary-500/20 to-purple-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
        <div class="relative z-10">
          <div class="text-primary-400 mb-4">
            <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          </div>
          <p class="text-slate-300 mb-6">"A game changer for our business. Highly recommended."</p>
          <div class="font-bold text-white">User One</div>
        </div>
      </div>
      <div class="group relative rounded-2xl bg-slate-800 p-8 border border-white/10 hover:border-white/20 transition-colors overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-r from-primary-500/20 to-purple-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
        <div class="relative z-10">
          <div class="text-primary-400 mb-4">
            <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          </div>
          <p class="text-slate-300 mb-6">"Incredible value for money. Best in class."</p>
          <div class="font-bold text-white">User Two</div>
        </div>
      </div>
      <div class="group relative rounded-2xl bg-slate-800 p-8 border border-white/10 hover:border-white/20 transition-colors overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-r from-primary-500/20 to-purple-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
        <div class="relative z-10">
          <div class="text-primary-400 mb-4">
            <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21L14.017 18C14.017 16.0547 15.372 15.5547 16.3945 15.5547C17.3281 15.5547 18.2617 16.293 18.2617 18.2617C18.2617 19.832 17.168 21 16.0312 21H14.017ZM8 21L8 18C8 16.0547 9.35547 15.5547 10.3789 15.5547C11.3125 15.5547 12.2461 16.293 12.2461 18.2617C12.2461 19.832 11.1523 21 10.0156 21H8ZM10.3789 3C7.68359 3 4 6.71484 4 13H10.3789C10.3789 11.332 11.6602 10.0508 13.3281 10.0508C14.9961 10.0508 16.2773 11.332 16.2773 13H19.9062C19.9062 6.71484 16.2227 3 13.5273 3H10.3789Z"/></svg>
          </div>
          <p class="text-slate-300 mb-6">"Support is fantastic. They really care."</p>
          <div class="font-bold text-white">User Three</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-047",
        "title": "Testimonials with Glassmorphism",
        "description": "Frosted glass effect",
        "dir": "templates/07-testimonials",
        "content": """<div class="py-24 bg-gradient-to-br from-blue-500 to-purple-600">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl border border-white/20 text-white shadow-xl">
        <p class="text-lg mb-6">"The glassmorphism effect is stunning. It adds a modern touch to our site."</p>
        <div class="flex items-center gap-4">
          <div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center font-bold">A</div>
          <div class="font-bold">Alex</div>
        </div>
      </div>
      <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl border border-white/20 text-white shadow-xl">
        <p class="text-lg mb-6">"Looks great on dark backgrounds too. Very versatile template."</p>
        <div class="flex items-center gap-4">
          <div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center font-bold">B</div>
          <div class="font-bold">Ben</div>
        </div>
      </div>
      <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl border border-white/20 text-white shadow-xl">
        <p class="text-lg mb-6">"Easy to implement and customize. Saved me hours of CSS work."</p>
        <div class="flex items-center gap-4">
          <div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center font-bold">C</div>
          <div class="font-bold">Charlie</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-048",
        "title": "Testimonials with Neomorphism",
        "description": "Soft UI design",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-slate-200 py-24">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="p-8 rounded-2xl bg-slate-200 shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]">
        <p class="text-slate-600 mb-6">"The soft UI look is so clean and pleasing to the eye. Love it!"</p>
        <div class="font-bold text-slate-800">User X</div>
      </div>
      <div class="p-8 rounded-2xl bg-slate-200 shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]">
        <p class="text-slate-600 mb-6">"It stands out from the flat design trend. Very unique."</p>
        <div class="font-bold text-slate-800">User Y</div>
      </div>
      <div class="p-8 rounded-2xl bg-slate-200 shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]">
        <p class="text-slate-600 mb-6">"Great attention to detail with the shadows and highlights."</p>
        <div class="font-bold text-slate-800">User Z</div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-049",
        "title": "Testimonials with Retro Style",
        "description": "Pixel art / retro vibe",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-yellow-50 py-24 font-mono">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 mb-12 text-center uppercase tracking-widest">User Feedback</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
          <p class="text-slate-900 mb-4">"THIS IS RAD! FEELS LIKE THE 90S BUT WORKS LIKE 2024."</p>
          <div class="font-bold text-slate-900 uppercase">- RETRO FAN</div>
        </div>
        <div class="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
          <p class="text-slate-900 mb-4">"SUPER FAST. SUPER COOL. 10/10 WOULD RECOMMEND."</p>
          <div class="font-bold text-slate-900 uppercase">- SPEED RUNNER</div>
        </div>
        <div class="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
          <p class="text-slate-900 mb-4">"NO BUGS. JUST FEATURES. INSERT COIN TO CONTINUE."</p>
          <div class="font-bold text-slate-900 uppercase">- GAMER PRO</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "test-050",
        "title": "Testimonials with Minimalist Grid",
        "description": "Clean lines and typography",
        "dir": "templates/07-testimonials",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 border-t border-l border-slate-200">
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Minimalism at its finest."</p>
          <div class="font-bold text-slate-900 text-sm">User 1</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Less is more. Perfect execution."</p>
          <div class="font-bold text-slate-900 text-sm">User 2</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Clean, fast, and effective."</p>
          <div class="font-bold text-slate-900 text-sm">User 3</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Exactly what I needed."</p>
          <div class="font-bold text-slate-900 text-sm">User 4</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"No clutter, just content."</p>
          <div class="font-bold text-slate-900 text-sm">User 5</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Typography is on point."</p>
          <div class="font-bold text-slate-900 text-sm">User 6</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Great use of whitespace."</p>
          <div class="font-bold text-slate-900 text-sm">User 7</div>
        </div>
        <div class="p-8 border-r border-b border-slate-200 hover:bg-slate-50 transition-colors">
          <p class="text-slate-600 text-sm mb-4">"Highly functional design."</p>
          <div class="font-bold text-slate-900 text-sm">User 8</div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
# Part 9: Team 001-012
TEMPLATES_TEAM = [
    {
        "id": "team-001",
        "title": "Simple Team Grid",
        "description": "Grid of team members",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-12">Meet our team</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
        <div class="space-y-4">
          <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="space-y-2">
            <div class="text-lg leading-6 font-medium space-y-1">
              <h3 class="text-slate-900">Michael Foster</h3>
              <p class="text-primary-600">Co-Founder / CTO</p>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="space-y-2">
            <div class="text-lg leading-6 font-medium space-y-1">
              <h3 class="text-slate-900">Dries Vincent</h3>
              <p class="text-primary-600">Manager, Business Relations</p>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="space-y-2">
            <div class="text-lg leading-6 font-medium space-y-1">
              <h3 class="text-slate-900">Lindsay Walton</h3>
              <p class="text-primary-600">Front-end Developer</p>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="space-y-2">
            <div class="text-lg leading-6 font-medium space-y-1">
              <h3 class="text-slate-900">Courtney Henry</h3>
              <p class="text-primary-600">Designer</p>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="space-y-2">
            <div class="text-lg leading-6 font-medium space-y-1">
              <h3 class="text-slate-900">Tom Cook</h3>
              <p class="text-primary-600">Director of Product</p>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="space-y-2">
            <div class="text-lg leading-6 font-medium space-y-1">
              <h3 class="text-slate-900">Whitney Francis</h3>
              <p class="text-primary-600">Copywriter</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-002",
        "title": "Team with Large Images",
        "description": "Full width images",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Leadership</h2>
        <p class="mt-4 text-lg text-slate-500">We're a dynamic group of individuals who are passionate about what we do.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="relative rounded-2xl overflow-hidden group">
          <img class="w-full h-96 object-cover transition-transform duration-500 group-hover:scale-105" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
          <div class="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/40 to-transparent"></div>
          <div class="absolute bottom-0 left-0 p-8 text-white">
            <h3 class="text-2xl font-bold">Leonard Krasner</h3>
            <p class="text-primary-300">Senior Designer</p>
            <p class="mt-2 text-slate-300 text-sm">Leonard leads our design team with over 10 years of experience in UI/UX.</p>
          </div>
        </div>
        <div class="relative rounded-2xl overflow-hidden group">
          <img class="w-full h-96 object-cover transition-transform duration-500 group-hover:scale-105" src="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
          <div class="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/40 to-transparent"></div>
          <div class="absolute bottom-0 left-0 p-8 text-white">
            <h3 class="text-2xl font-bold">Floyd Miles</h3>
            <p class="text-primary-300">Principal Engineer</p>
            <p class="mt-2 text-slate-300 text-sm">Floyd is the architect behind our core platform infrastructure.</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-003",
        "title": "Team with Social Links",
        "description": "Social media icons",
        "dir": "templates/08-team",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Our People</h2>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-32 h-32 rounded-full mx-auto mb-4 object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
          <h3 class="text-lg font-bold text-slate-900">Leslie Alexander</h3>
          <p class="text-primary-600 mb-4">Co-Founder / CEO</p>
          <div class="flex justify-center space-x-4">
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-32 h-32 rounded-full mx-auto mb-4 object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
          <h3 class="text-lg font-bold text-slate-900">Michael Foster</h3>
          <p class="text-primary-600 mb-4">Co-Founder / CTO</p>
          <div class="flex justify-center space-x-4">
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-32 h-32 rounded-full mx-auto mb-4 object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
          <h3 class="text-lg font-bold text-slate-900">Dries Vincent</h3>
          <p class="text-primary-600 mb-4">Manager, Business Relations</p>
          <div class="flex justify-center space-x-4">
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-32 h-32 rounded-full mx-auto mb-4 object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
          <h3 class="text-lg font-bold text-slate-900">Lindsay Walton</h3>
          <p class="text-primary-600 mb-4">Front-end Developer</p>
          <div class="flex justify-center space-x-4">
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-slate-400 hover:text-slate-500">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-004",
        "title": "Team with Bio",
        "description": "Detailed bio cards",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="space-y-12">
        <div class="text-center">
          <h2 class="text-3xl font-bold text-slate-900">Our Experts</h2>
          <p class="mt-4 text-lg text-slate-500">Meet the brains behind the operation.</p>
        </div>
        <ul class="space-y-12 lg:grid lg:grid-cols-2 lg:items-start lg:gap-x-8 lg:gap-y-12 lg:space-y-0">
          <li>
            <div class="space-y-4 sm:grid sm:grid-cols-3 sm:gap-6 sm:space-y-0 lg:gap-8">
              <div class="h-0 aspect-w-3 aspect-h-2 sm:aspect-w-3 sm:aspect-h-4">
                <img class="object-cover shadow-lg rounded-lg" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
              </div>
              <div class="sm:col-span-2">
                <div class="space-y-4">
                  <div class="text-lg leading-6 font-medium space-y-1">
                    <h3 class="text-slate-900">Whitney Francis</h3>
                    <p class="text-primary-600">Copywriter</p>
                  </div>
                  <div class="text-lg">
                    <p class="text-slate-500">Whitney is a master wordsmith who can turn complex technical concepts into engaging stories. She has written for major tech publications.</p>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li>
            <div class="space-y-4 sm:grid sm:grid-cols-3 sm:gap-6 sm:space-y-0 lg:gap-8">
              <div class="h-0 aspect-w-3 aspect-h-2 sm:aspect-w-3 sm:aspect-h-4">
                <img class="object-cover shadow-lg rounded-lg" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
              </div>
              <div class="sm:col-span-2">
                <div class="space-y-4">
                  <div class="text-lg leading-6 font-medium space-y-1">
                    <h3 class="text-slate-900">Leonard Krasner</h3>
                    <p class="text-primary-600">Senior Designer</p>
                  </div>
                  <div class="text-lg">
                    <p class="text-slate-500">Leonard brings a unique visual style to everything he touches. His work has been featured in design annuals around the world.</p>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li>
            <div class="space-y-4 sm:grid sm:grid-cols-3 sm:gap-6 sm:space-y-0 lg:gap-8">
              <div class="h-0 aspect-w-3 aspect-h-2 sm:aspect-w-3 sm:aspect-h-4">
                <img class="object-cover shadow-lg rounded-lg" src="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
              </div>
              <div class="sm:col-span-2">
                <div class="space-y-4">
                  <div class="text-lg leading-6 font-medium space-y-1">
                    <h3 class="text-slate-900">Floyd Miles</h3>
                    <p class="text-primary-600">Principal Engineer</p>
                  </div>
                  <div class="text-lg">
                    <p class="text-slate-500">Floyd is a coding wizard who loves solving hard problems. He contributes to several open source projects in his spare time.</p>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li>
            <div class="space-y-4 sm:grid sm:grid-cols-3 sm:gap-6 sm:space-y-0 lg:gap-8">
              <div class="h-0 aspect-w-3 aspect-h-2 sm:aspect-w-3 sm:aspect-h-4">
                <img class="object-cover shadow-lg rounded-lg" src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
              </div>
              <div class="sm:col-span-2">
                <div class="space-y-4">
                  <div class="text-lg leading-6 font-medium space-y-1">
                    <h3 class="text-slate-900">Emily Selman</h3>
                    <p class="text-primary-600">VP, User Experience</p>
                  </div>
                  <div class="text-lg">
                    <p class="text-slate-500">Emily is obsessed with user research and testing. She ensures that every product decision is backed by data.</p>
                  </div>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-005",
        "title": "Team with Hover Effect",
        "description": "Overlay on hover",
        "dir": "templates/08-team",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-white">The Dream Team</h2>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="group relative rounded-2xl overflow-hidden aspect-w-3 aspect-h-4 cursor-pointer">
          <img class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-110" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
          <div class="absolute inset-0 bg-primary-600/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center text-center p-6">
            <h3 class="text-2xl font-bold text-white transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">Anna Smith</h3>
            <p class="text-white/90 mb-4 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-75">Creative Director</p>
            <p class="text-white/80 text-sm transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-100">"Creativity is intelligence having fun."</p>
          </div>
        </div>
        <div class="group relative rounded-2xl overflow-hidden aspect-w-3 aspect-h-4 cursor-pointer">
          <img class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-110" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
          <div class="absolute inset-0 bg-primary-600/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center text-center p-6">
            <h3 class="text-2xl font-bold text-white transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">James Wilson</h3>
            <p class="text-white/90 mb-4 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-75">Lead Developer</p>
            <p class="text-white/80 text-sm transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-100">"Code is poetry."</p>
          </div>
        </div>
        <div class="group relative rounded-2xl overflow-hidden aspect-w-3 aspect-h-4 cursor-pointer">
          <img class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-110" src="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
          <div class="absolute inset-0 bg-primary-600/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center text-center p-6">
            <h3 class="text-2xl font-bold text-white transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">Maria Garcia</h3>
            <p class="text-white/90 mb-4 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-75">Marketing Head</p>
            <p class="text-white/80 text-sm transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-100">"Connecting people with products."</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-006",
        "title": "Team with Circular Avatars",
        "description": "Minimal circular design",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Meet the Crew</h2>
      </div>
      <div class="flex flex-wrap justify-center gap-12">
        <div class="text-center w-48">
          <div class="relative w-32 h-32 mx-auto mb-4">
            <div class="absolute inset-0 rounded-full border-2 border-dashed border-primary-300 animate-spin-slow"></div>
            <img class="w-full h-full rounded-full object-cover p-1" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Sarah</h3>
          <p class="text-slate-500 text-sm">CEO</p>
        </div>
        <div class="text-center w-48">
          <div class="relative w-32 h-32 mx-auto mb-4">
            <div class="absolute inset-0 rounded-full border-2 border-dashed border-primary-300 animate-spin-slow" style="animation-delay: -1s;"></div>
            <img class="w-full h-full rounded-full object-cover p-1" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Mark</h3>
          <p class="text-slate-500 text-sm">CTO</p>
        </div>
        <div class="text-center w-48">
          <div class="relative w-32 h-32 mx-auto mb-4">
            <div class="absolute inset-0 rounded-full border-2 border-dashed border-primary-300 animate-spin-slow" style="animation-delay: -2s;"></div>
            <img class="w-full h-full rounded-full object-cover p-1" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Jessica</h3>
          <p class="text-slate-500 text-sm">COO</p>
        </div>
        <div class="text-center w-48">
          <div class="relative w-32 h-32 mx-auto mb-4">
            <div class="absolute inset-0 rounded-full border-2 border-dashed border-primary-300 animate-spin-slow" style="animation-delay: -3s;"></div>
            <img class="w-full h-full rounded-full object-cover p-1" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          </div>
          <h3 class="text-lg font-bold text-slate-900">David</h3>
          <p class="text-slate-500 text-sm">CFO</p>
        </div>
        <div class="text-center w-48">
          <div class="relative w-32 h-32 mx-auto mb-4">
            <div class="absolute inset-0 rounded-full border-2 border-dashed border-primary-300 animate-spin-slow" style="animation-delay: -4s;"></div>
            <img class="w-full h-full rounded-full object-cover p-1" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Emily</h3>
          <p class="text-slate-500 text-sm">CMO</p>
        </div>
      </div>
    </div>
    <style>
      @keyframes spin-slow {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }
      .animate-spin-slow {
        animation: spin-slow 10s linear infinite;
      }
    </style>
  </div>"""
    }
]
# Placeholder for Team 007-012
# Part 9 continued: Team 007-012
TEMPLATES_TEAM_PART_2 = [
    {
        "id": "team-007",
        "title": "Team with Skills",
        "description": "Skill bars",
        "dir": "templates/08-team",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Our Specialists</h2>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-2xl shadow-sm">
          <div class="flex items-center gap-4 mb-6">
            <img class="w-16 h-16 rounded-full object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div>
              <h3 class="font-bold text-slate-900">Michael Foster</h3>
              <p class="text-primary-600 text-sm">Frontend Dev</p>
            </div>
          </div>
          <div class="space-y-4">
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-600">React</span>
                <span class="font-bold text-slate-900">95%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2">
                <div class="bg-primary-500 h-2 rounded-full" style="width: 95%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-600">Vue</span>
                <span class="font-bold text-slate-900">85%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2">
                <div class="bg-primary-500 h-2 rounded-full" style="width: 85%"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm">
          <div class="flex items-center gap-4 mb-6">
            <img class="w-16 h-16 rounded-full object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div>
              <h3 class="font-bold text-slate-900">Dries Vincent</h3>
              <p class="text-primary-600 text-sm">Backend Dev</p>
            </div>
          </div>
          <div class="space-y-4">
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-600">Python</span>
                <span class="font-bold text-slate-900">90%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2">
                <div class="bg-primary-500 h-2 rounded-full" style="width: 90%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-600">Go</span>
                <span class="font-bold text-slate-900">80%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2">
                <div class="bg-primary-500 h-2 rounded-full" style="width: 80%"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm">
          <div class="flex items-center gap-4 mb-6">
            <img class="w-16 h-16 rounded-full object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div>
              <h3 class="font-bold text-slate-900">Lindsay Walton</h3>
              <p class="text-primary-600 text-sm">Designer</p>
            </div>
          </div>
          <div class="space-y-4">
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-600">Figma</span>
                <span class="font-bold text-slate-900">98%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2">
                <div class="bg-primary-500 h-2 rounded-full" style="width: 98%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-600">Adobe CC</span>
                <span class="font-bold text-slate-900">92%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2">
                <div class="bg-primary-500 h-2 rounded-full" style="width: 92%"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-008",
        "title": "Team with Modal",
        "description": "Click for details",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24" x-data="{ open: false, activeMember: null, members: [
    { name: 'Tom Cook', role: 'Director of Product', image: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', bio: 'Tom is responsible for the strategic direction of our product line. He has over 15 years of experience in product management.' },
    { name: 'Whitney Francis', role: 'Copywriter', image: 'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', bio: 'Whitney crafts the voice of our brand. She is an award-winning writer with a passion for storytelling.' },
    { name: 'Leonard Krasner', role: 'Senior Designer', image: 'https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', bio: 'Leonard leads our visual design efforts. He believes that good design is invisible.' },
    { name: 'Floyd Miles', role: 'Principal Engineer', image: 'https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', bio: 'Floyd ensures our systems are scalable and reliable. He is an expert in distributed systems.' }
  ] }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Click to meet us</h2>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <template x-for="(member, index) in members" :key="index">
          <div @click="activeMember = member; open = true" class="cursor-pointer group text-center">
            <div class="relative w-40 h-40 mx-auto mb-4 rounded-full overflow-hidden ring-4 ring-transparent group-hover:ring-primary-300 transition-all">
              <img :src="member.image" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
              <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                <span class="text-white font-bold text-sm">View Bio</span>
              </div>
            </div>
            <h3 class="text-lg font-bold text-slate-900" x-text="member.name"></h3>
            <p class="text-primary-600" x-text="member.role"></p>
          </div>
        </template>
      </div>
    </div>

    <!-- Modal -->
    <div x-show="open" class="fixed inset-0 z-50 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true" style="display: none;">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div x-show="open" x-transition:enter="ease-out duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="ease-in duration-200" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" class="fixed inset-0 bg-slate-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="open = false"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div x-show="open" x-transition:enter="ease-out duration-300" x-transition:enter-start="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" x-transition:enter-end="opacity-100 translate-y-0 sm:scale-100" x-transition:leave="ease-in duration-200" x-transition:leave-start="opacity-100 translate-y-0 sm:scale-100" x-transition:leave-end="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
          <div class="sm:flex sm:items-start">
            <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-primary-100 sm:mx-0 sm:h-10 sm:w-10">
              <svg class="h-6 w-6 text-primary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
            </div>
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left" x-data>
              <h3 class="text-lg leading-6 font-medium text-slate-900" id="modal-title" x-text="activeMember?.name"></h3>
              <p class="text-sm text-primary-600 mb-2" x-text="activeMember?.role"></p>
              <div class="mt-2">
                <p class="text-sm text-slate-500" x-text="activeMember?.bio"></p>
              </div>
            </div>
          </div>
          <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
            <button type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-primary-600 text-base font-medium text-white hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 sm:ml-3 sm:w-auto sm:text-sm" @click="open = false">Close</button>
          </div>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "team-009",
        "title": "Team with Tabs",
        "description": "Categorized team",
        "dir": "templates/08-team",
        "content": """<div class="bg-slate-50 py-24" x-data="{ activeTab: 'leadership' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900 mb-8">Our Organization</h2>
        <div class="inline-flex rounded-lg bg-slate-200 p-1">
          <button @click="activeTab = 'leadership'" :class="activeTab === 'leadership' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-600 hover:text-slate-900'" class="px-6 py-2 rounded-md font-medium transition-all">Leadership</button>
          <button @click="activeTab = 'engineering'" :class="activeTab === 'engineering' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-600 hover:text-slate-900'" class="px-6 py-2 rounded-md font-medium transition-all">Engineering</button>
          <button @click="activeTab = 'design'" :class="activeTab === 'design' ? 'bg-white shadow-sm text-slate-900' : 'text-slate-600 hover:text-slate-900'" class="px-6 py-2 rounded-md font-medium transition-all">Design</button>
        </div>
      </div>

      <div x-show="activeTab === 'leadership'" class="grid grid-cols-1 md:grid-cols-3 gap-8" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform scale-95" x-transition:enter-end="opacity-100 transform scale-100">
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Leslie Alexander</h3>
          <p class="text-slate-500">CEO</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Michael Foster</h3>
          <p class="text-slate-500">CTO</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Dries Vincent</h3>
          <p class="text-slate-500">COO</p>
        </div>
      </div>

      <div x-show="activeTab === 'engineering'" class="grid grid-cols-1 md:grid-cols-3 gap-8" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform scale-95" x-transition:enter-end="opacity-100 transform scale-100" style="display: none;">
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Floyd Miles</h3>
          <p class="text-slate-500">Lead Engineer</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Emily Selman</h3>
          <p class="text-slate-500">Senior Dev</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Kristin Watson</h3>
          <p class="text-slate-500">DevOps</p>
        </div>
      </div>

      <div x-show="activeTab === 'design'" class="grid grid-cols-1 md:grid-cols-3 gap-8" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform scale-95" x-transition:enter-end="opacity-100 transform scale-100" style="display: none;">
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Leonard Krasner</h3>
          <p class="text-slate-500">Lead Designer</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Courtney Henry</h3>
          <p class="text-slate-500">UX Designer</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-sm text-center">
          <img class="w-24 h-24 rounded-full mx-auto mb-4" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
          <h3 class="font-bold text-slate-900">Whitney Francis</h3>
          <p class="text-slate-500">Visual Designer</p>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "team-010",
        "title": "Team with Timeline",
        "description": "Joining timeline",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Our Growth</h2>
      </div>
      <div class="relative border-l-4 border-primary-200 ml-6 space-y-12">
        <div class="relative pl-12">
          <div class="absolute -left-[14px] top-0 w-6 h-6 bg-primary-500 rounded-full border-4 border-white"></div>
          <div class="flex flex-col sm:flex-row gap-6 items-start">
            <img class="w-24 h-24 rounded-xl object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
            <div>
              <span class="text-sm font-bold text-primary-600">2018</span>
              <h3 class="text-xl font-bold text-slate-900">Leslie Alexander Founded the Company</h3>
              <p class="text-slate-600 mt-2">Started with a vision to revolutionize the industry.</p>
            </div>
          </div>
        </div>
        <div class="relative pl-12">
          <div class="absolute -left-[14px] top-0 w-6 h-6 bg-primary-500 rounded-full border-4 border-white"></div>
          <div class="flex flex-col sm:flex-row gap-6 items-start">
            <img class="w-24 h-24 rounded-xl object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
            <div>
              <span class="text-sm font-bold text-primary-600">2019</span>
              <h3 class="text-xl font-bold text-slate-900">Michael Foster Joined as CTO</h3>
              <p class="text-slate-600 mt-2">Brought technical expertise to scale the platform.</p>
            </div>
          </div>
        </div>
        <div class="relative pl-12">
          <div class="absolute -left-[14px] top-0 w-6 h-6 bg-primary-500 rounded-full border-4 border-white"></div>
          <div class="flex flex-col sm:flex-row gap-6 items-start">
            <img class="w-24 h-24 rounded-xl object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
            <div>
              <span class="text-sm font-bold text-primary-600">2020</span>
              <h3 class="text-xl font-bold text-slate-900">Dries Vincent Leads Operations</h3>
              <p class="text-slate-600 mt-2">Streamlined processes and expanded the team.</p>
            </div>
          </div>
        </div>
        <div class="relative pl-12">
          <div class="absolute -left-[14px] top-0 w-6 h-6 bg-primary-500 rounded-full border-4 border-white"></div>
          <div class="flex flex-col sm:flex-row gap-6 items-start">
            <div class="w-24 h-24 rounded-xl bg-slate-100 flex items-center justify-center text-slate-400 font-bold text-xl">+50</div>
            <div>
              <span class="text-sm font-bold text-primary-600">2024</span>
              <h3 class="text-xl font-bold text-slate-900">Now a Team of 50+</h3>
              <p class="text-slate-600 mt-2">Growing stronger every day.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "team-011",
        "title": "Team with Hexagons",
        "description": "Geometric layout",
        "dir": "templates/08-team",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-white mb-16">The Hive Mind</h2>
      <div class="flex flex-wrap justify-center gap-4">
        <div class="w-32 h-36 relative clip-hexagon bg-slate-800 hover:bg-primary-600 transition-colors group cursor-pointer">
          <img class="absolute inset-1 w-[calc(100%-8px)] h-[calc(100%-8px)] object-cover clip-hexagon opacity-70 group-hover:opacity-100 transition-opacity" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
        </div>
        <div class="w-32 h-36 relative clip-hexagon bg-slate-800 hover:bg-primary-600 transition-colors group cursor-pointer mt-16">
          <img class="absolute inset-1 w-[calc(100%-8px)] h-[calc(100%-8px)] object-cover clip-hexagon opacity-70 group-hover:opacity-100 transition-opacity" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
        </div>
        <div class="w-32 h-36 relative clip-hexagon bg-slate-800 hover:bg-primary-600 transition-colors group cursor-pointer">
          <img class="absolute inset-1 w-[calc(100%-8px)] h-[calc(100%-8px)] object-cover clip-hexagon opacity-70 group-hover:opacity-100 transition-opacity" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
        </div>
        <div class="w-32 h-36 relative clip-hexagon bg-slate-800 hover:bg-primary-600 transition-colors group cursor-pointer mt-16">
          <img class="absolute inset-1 w-[calc(100%-8px)] h-[calc(100%-8px)] object-cover clip-hexagon opacity-70 group-hover:opacity-100 transition-opacity" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
        </div>
        <div class="w-32 h-36 relative clip-hexagon bg-slate-800 hover:bg-primary-600 transition-colors group cursor-pointer">
          <img class="absolute inset-1 w-[calc(100%-8px)] h-[calc(100%-8px)] object-cover clip-hexagon opacity-70 group-hover:opacity-100 transition-opacity" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80">
        </div>
      </div>
    </div>
    <style>
      .clip-hexagon {
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
      }
    </style>
  </div>"""
    },
    {
        "id": "team-012",
        "title": "Team with Flip Cards",
        "description": "Flip to reveal info",
        "dir": "templates/08-team",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Flip to Meet</h2>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="group h-80 w-full [perspective:1000px]">
          <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
            <div class="absolute inset-0 h-full w-full rounded-xl [backface-visibility:hidden]">
              <img class="h-full w-full object-cover rounded-xl" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="">
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4">
                <h3 class="text-xl font-bold text-white">Leslie Alexander</h3>
                <p class="text-primary-300">CEO</p>
              </div>
            </div>
            <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-900 p-8 text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden] flex flex-col items-center justify-center">
              <h3 class="text-xl font-bold text-white mb-2">Leslie Alexander</h3>
              <p class="text-primary-400 mb-4">CEO</p>
              <p class="text-sm">"Visionary leader with a passion for innovation and growth."</p>
              <div class="mt-6 flex gap-4">
                <a href="#" class="text-white hover:text-primary-400">Twitter</a>
                <a href="#" class="text-white hover:text-primary-400">LinkedIn</a>
              </div>
            </div>
          </div>
        </div>

        <div class="group h-80 w-full [perspective:1000px]">
          <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
            <div class="absolute inset-0 h-full w-full rounded-xl [backface-visibility:hidden]">
              <img class="h-full w-full object-cover rounded-xl" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="">
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4">
                <h3 class="text-xl font-bold text-white">Michael Foster</h3>
                <p class="text-primary-300">CTO</p>
              </div>
            </div>
            <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-900 p-8 text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden] flex flex-col items-center justify-center">
              <h3 class="text-xl font-bold text-white mb-2">Michael Foster</h3>
              <p class="text-primary-400 mb-4">CTO</p>
              <p class="text-sm">"Tech enthusiast ensuring our platform is always ahead of the curve."</p>
              <div class="mt-6 flex gap-4">
                <a href="#" class="text-white hover:text-primary-400">Twitter</a>
                <a href="#" class="text-white hover:text-primary-400">LinkedIn</a>
              </div>
            </div>
          </div>
        </div>

        <div class="group h-80 w-full [perspective:1000px]">
          <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
            <div class="absolute inset-0 h-full w-full rounded-xl [backface-visibility:hidden]">
              <img class="h-full w-full object-cover rounded-xl" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="">
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4">
                <h3 class="text-xl font-bold text-white">Dries Vincent</h3>
                <p class="text-primary-300">COO</p>
              </div>
            </div>
            <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-900 p-8 text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden] flex flex-col items-center justify-center">
              <h3 class="text-xl font-bold text-white mb-2">Dries Vincent</h3>
              <p class="text-primary-400 mb-4">COO</p>
              <p class="text-sm">"Operational wizard keeping everything running smoothly."</p>
              <div class="mt-6 flex gap-4">
                <a href="#" class="text-white hover:text-primary-400">Twitter</a>
                <a href="#" class="text-white hover:text-primary-400">LinkedIn</a>
              </div>
            </div>
          </div>
        </div>

        <div class="group h-80 w-full [perspective:1000px]">
          <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
            <div class="absolute inset-0 h-full w-full rounded-xl [backface-visibility:hidden]">
              <img class="h-full w-full object-cover rounded-xl" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="">
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4">
                <h3 class="text-xl font-bold text-white">Lindsay Walton</h3>
                <p class="text-primary-300">Designer</p>
              </div>
            </div>
            <div class="absolute inset-0 h-full w-full rounded-xl bg-slate-900 p-8 text-center text-slate-100 [transform:rotateY(180deg)] [backface-visibility:hidden] flex flex-col items-center justify-center">
              <h3 class="text-xl font-bold text-white mb-2">Lindsay Walton</h3>
              <p class="text-primary-400 mb-4">Designer</p>
              <p class="text-sm">"Creative mind crafting beautiful and intuitive user experiences."</p>
              <div class="mt-6 flex gap-4">
                <a href="#" class="text-white hover:text-primary-400">Twitter</a>
                <a href="#" class="text-white hover:text-primary-400">LinkedIn</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]

# Combine all templates
TEMPLATES = TEMPLATES_CONTENT_1 + TEMPLATES_CONTENT_2 + TEMPLATES_CTA_1 + TEMPLATES_CTA_2 + TEMPLATES_PRICE_1 + TEMPLATES_PRICE_1_PART_2 + TEMPLATES_PRICE_2 + TEMPLATES_PRICE_2_PART_2 + TEMPLATES_TEST_1 + TEMPLATES_TEST_1_PART_2 + TEMPLATES_TEST_2 + TEMPLATES_TEST_2_PART_2 + TEMPLATES_TEAM + TEMPLATES_TEAM_PART_2

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

if __name__ == "__main__":
    generate_and_push()
