import os
import subprocess

# Base HTML template
BASE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Awesome Tailwind UI Templates</title>
  <meta name="description" content="{description}">
  <script src="https://stephen.taipei/tailwindcss-browser.js"></script>
  <style type="text/tailwindcss">
    @theme {{
      --color-primary-50: #eff6ff;
      --color-primary-100: #dbeafe;
      --color-primary-200: #bfdbfe;
      --color-primary-300: #93c5fd;
      --color-primary-400: #60a5fa;
      --color-primary-500: #3b82f6;
      --color-primary-600: #2563eb;
      --color-primary-700: #1d4ed8;
      --color-primary-800: #1e40af;
      --color-primary-900: #1e3a8a;
      --color-primary-950: #172554;
    }}
  </style>
</head>
<body class="bg-gray-50 text-slate-900">
  {content}
</body>
</html>"""

# Part 1: Gallery 001-012
TEMPLATES_GALLERY_1 = [
    {
        "id": "gallery-001",
        "title": "Basic 3 Column Grid",
        "description": "Simple image grid",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold text-slate-900">Our Gallery</h2>
        <p class="text-slate-600 mt-4">A collection of our best moments.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="aspect-w-4 aspect-h-3 rounded-lg overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="" class="object-cover w-full h-full hover:scale-105 transition-transform duration-300">
        </div>
        <div class="aspect-w-4 aspect-h-3 rounded-lg overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="" class="object-cover w-full h-full hover:scale-105 transition-transform duration-300">
        </div>
        <div class="aspect-w-4 aspect-h-3 rounded-lg overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="" class="object-cover w-full h-full hover:scale-105 transition-transform duration-300">
        </div>
        <div class="aspect-w-4 aspect-h-3 rounded-lg overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="" class="object-cover w-full h-full hover:scale-105 transition-transform duration-300">
        </div>
        <div class="aspect-w-4 aspect-h-3 rounded-lg overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="" class="object-cover w-full h-full hover:scale-105 transition-transform duration-300">
        </div>
        <div class="aspect-w-4 aspect-h-3 rounded-lg overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="" class="object-cover w-full h-full hover:scale-105 transition-transform duration-300">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-002",
        "title": "4 Column Grid",
        "description": "Dense image grid",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" class="w-full h-full object-cover hover:opacity-75 transition-opacity">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-003",
        "title": "2 Column Grid",
        "description": "Large image showcase",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="group relative overflow-hidden rounded-2xl">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" class="w-full h-[500px] object-cover transition-transform duration-500 group-hover:scale-110">
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-8">
            <h3 class="text-white text-2xl font-bold">Portrait Photography</h3>
          </div>
        </div>
        <div class="group relative overflow-hidden rounded-2xl">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" class="w-full h-[500px] object-cover transition-transform duration-500 group-hover:scale-110">
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-8">
            <h3 class="text-white text-2xl font-bold">Urban Lifestyle</h3>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-004",
        "title": "Grid with Gap",
        "description": "Spacious layout",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-16">
        <div class="space-y-4">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full rounded-lg shadow-lg shadow-primary-500/20">
          <h3 class="text-white font-medium text-lg">Project Alpha</h3>
        </div>
        <div class="space-y-4 md:mt-16">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full rounded-lg shadow-lg shadow-primary-500/20">
          <h3 class="text-white font-medium text-lg">Project Beta</h3>
        </div>
        <div class="space-y-4 md:mt-32">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full rounded-lg shadow-lg shadow-primary-500/20">
          <h3 class="text-white font-medium text-lg">Project Gamma</h3>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-005",
        "title": "Grid with Captions",
        "description": "Images with text",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-12">
        <div>
          <div class="rounded-xl overflow-hidden mb-4">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Summer Collection</h3>
          <p class="text-slate-500 text-sm mt-1">Photography by Jane Doe</p>
        </div>
        <div>
          <div class="rounded-xl overflow-hidden mb-4">
            <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Winter Series</h3>
          <p class="text-slate-500 text-sm mt-1">Photography by John Smith</p>
        </div>
        <div>
          <div class="rounded-xl overflow-hidden mb-4">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="text-lg font-bold text-slate-900">Urban Life</h3>
          <p class="text-slate-500 text-sm mt-1">Photography by Mike Ross</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-006",
        "title": "Grid with Hover Overlay",
        "description": "Interactive gallery",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-1">
        <div class="group relative aspect-square overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
            <button class="bg-white text-slate-900 px-6 py-2 rounded-full font-medium transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">View Project</button>
          </div>
        </div>
        <div class="group relative aspect-square overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
            <button class="bg-white text-slate-900 px-6 py-2 rounded-full font-medium transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">View Project</button>
          </div>
        </div>
        <div class="group relative aspect-square overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
            <button class="bg-white text-slate-900 px-6 py-2 rounded-full font-medium transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">View Project</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-007",
        "title": "Grid with Categories",
        "description": "Categorized images",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex justify-center gap-6 mb-12">
        <button class="text-primary-600 font-bold border-b-2 border-primary-600 pb-1">All</button>
        <button class="text-slate-500 hover:text-slate-900 pb-1">Nature</button>
        <button class="text-slate-500 hover:text-slate-900 pb-1">Urban</button>
        <button class="text-slate-500 hover:text-slate-900 pb-1">People</button>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
          <div class="bg-white p-4">
            <span class="text-xs font-bold text-primary-600 uppercase tracking-wider">People</span>
            <h3 class="font-bold text-slate-900 mt-1">Portrait Session</h3>
          </div>
        </div>
        <div class="rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
          <div class="bg-white p-4">
            <span class="text-xs font-bold text-primary-600 uppercase tracking-wider">Urban</span>
            <h3 class="font-bold text-slate-900 mt-1">City Lights</h3>
          </div>
        </div>
        <div class="rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
          <div class="bg-white p-4">
            <span class="text-xs font-bold text-primary-600 uppercase tracking-wider">Nature</span>
            <h3 class="font-bold text-slate-900 mt-1">Forest Walk</h3>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-008",
        "title": "Filterable Grid",
        "description": "Interactive filtering",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ filter: 'all' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex flex-wrap justify-center gap-4 mb-12">
        <button @click="filter = 'all'" :class="filter === 'all' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-6 py-2 rounded-full transition-colors">All</button>
        <button @click="filter = 'design'" :class="filter === 'design' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-6 py-2 rounded-full transition-colors">Design</button>
        <button @click="filter = 'dev'" :class="filter === 'dev' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-6 py-2 rounded-full transition-colors">Development</button>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div x-show="filter === 'all' || filter === 'design'" class="bg-gray-100 rounded-xl aspect-video overflow-hidden" x-transition>
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
        <div x-show="filter === 'all' || filter === 'dev'" class="bg-gray-100 rounded-xl aspect-video overflow-hidden" x-transition>
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
        <div x-show="filter === 'all' || filter === 'design'" class="bg-gray-100 rounded-xl aspect-video overflow-hidden" x-transition>
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-009",
        "title": "Infinite Scroll Grid",
        "description": "Load more button",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ items: [1, 2, 3, 4, 5, 6] }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-12">
        <template x-for="item in items" :key="item">
          <div class="aspect-square bg-slate-100 rounded-lg overflow-hidden animate-fadeIn">
            <img :src="`https://source.unsplash.com/random/400x400?sig=${item}`" class="w-full h-full object-cover">
          </div>
        </template>
      </div>
      <div class="text-center">
        <button @click="items.push(items.length + 1, items.length + 2, items.length + 3)" class="inline-flex items-center gap-2 px-8 py-3 bg-white border border-slate-300 rounded-lg font-medium text-slate-700 hover:bg-slate-50 transition-colors">
          <span>Load More</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
        </button>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
    <style>
      @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
      .animate-fadeIn { animation: fadeIn 0.5s ease-out; }
    </style>
  </div>"""
    },
    {
        "id": "gallery-010",
        "title": "Grid with Zoom",
        "description": "Zoom on hover",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="overflow-hidden rounded-xl cursor-zoom-in">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-125 transition-transform duration-700">
        </div>
        <div class="overflow-hidden rounded-xl cursor-zoom-in">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-125 transition-transform duration-700">
        </div>
        <div class="overflow-hidden rounded-xl cursor-zoom-in">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-125 transition-transform duration-700">
        </div>
        <div class="overflow-hidden rounded-xl cursor-zoom-in">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover hover:scale-125 transition-transform duration-700">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-011",
        "title": "Basic Masonry",
        "description": "Masonry layout",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-2 lg:columns-3 gap-8 space-y-8">
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=800&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=600&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=500&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=700&q=80" class="w-full object-cover">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-012",
        "title": "Masonry with Captions",
        "description": "Masonry with text",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-6 space-y-6">
        <div class="break-inside-avoid bg-white rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover">
          <div class="p-4">
            <h3 class="font-bold text-slate-900">Portrait</h3>
            <p class="text-slate-500 text-sm">Studio session</p>
          </div>
        </div>
        <div class="break-inside-avoid bg-white rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=800&q=80" class="w-full object-cover">
          <div class="p-4">
            <h3 class="font-bold text-slate-900">Lifestyle</h3>
            <p class="text-slate-500 text-sm">Urban living</p>
          </div>
        </div>
        <div class="break-inside-avoid bg-white rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80" class="w-full object-cover">
          <div class="p-4">
            <h3 class="font-bold text-slate-900">Nature</h3>
            <p class="text-slate-500 text-sm">Outdoor adventure</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]

# Placeholder for Gallery 013-025
# Part 1 continued: Gallery 013-025
TEMPLATES_GALLERY_1_PART_2 = [
    {
        "id": "gallery-013",
        "title": "Masonry Filterable",
        "description": "Filtered masonry",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ filter: 'all' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex justify-center gap-4 mb-12">
        <button @click="filter = 'all'" :class="filter === 'all' ? 'text-slate-900 font-bold' : 'text-slate-500'" class="transition-colors">All</button>
        <button @click="filter = 'art'" :class="filter === 'art' ? 'text-slate-900 font-bold' : 'text-slate-500'" class="transition-colors">Art</button>
        <button @click="filter = 'photo'" :class="filter === 'photo' ? 'text-slate-900 font-bold' : 'text-slate-500'" class="transition-colors">Photography</button>
      </div>
      <div class="columns-1 md:columns-3 gap-8 space-y-8">
        <div x-show="filter === 'all' || filter === 'photo'" class="break-inside-avoid rounded-xl overflow-hidden" x-transition>
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover">
        </div>
        <div x-show="filter === 'all' || filter === 'art'" class="break-inside-avoid rounded-xl overflow-hidden" x-transition>
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=800&q=80" class="w-full object-cover">
        </div>
        <div x-show="filter === 'all' || filter === 'photo'" class="break-inside-avoid rounded-xl overflow-hidden" x-transition>
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80" class="w-full object-cover">
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-014",
        "title": "Masonry with Load More",
        "description": "Expandable masonry",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-6 space-y-6 mb-12">
        <div class="break-inside-avoid rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=500&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=700&q=80" class="w-full object-cover">
        </div>
      </div>
      <div class="text-center">
        <button class="px-8 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 transition-colors">Load More</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-015",
        "title": "Masonry with Hover",
        "description": "Hover effects",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-8 space-y-8">
        <div class="break-inside-avoid group relative rounded-xl overflow-hidden cursor-pointer">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover transition-transform duration-500 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
            <span class="text-white font-bold text-lg">View Details</span>
          </div>
        </div>
        <div class="break-inside-avoid group relative rounded-xl overflow-hidden cursor-pointer">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=800&q=80" class="w-full object-cover transition-transform duration-500 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
            <span class="text-white font-bold text-lg">View Details</span>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-016",
        "title": "Mixed Media Masonry",
        "description": "Images and video",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-6 space-y-6">
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden relative group">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=600&q=80" class="w-full object-cover opacity-80">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6 text-slate-900 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden">
          <div class="bg-slate-800 p-8 text-center h-64 flex flex-col justify-center items-center">
            <h3 class="text-white text-xl font-bold mb-2">Quote of the Day</h3>
            <p class="text-slate-400 italic">"Creativity is intelligence having fun."</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-017",
        "title": "Masonry with Lightbox",
        "description": "Click to expand",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ open: false, img: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-6 space-y-6">
        <div class="break-inside-avoid rounded-xl overflow-hidden cursor-pointer" @click="open = true; img = 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover hover:opacity-90 transition-opacity">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden cursor-pointer" @click="open = true; img = 'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=800&q=80" class="w-full object-cover hover:opacity-90 transition-opacity">
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4" @click="open = false" style="display: none;">
      <img :src="img" class="max-w-full max-h-full rounded-lg shadow-2xl" @click.stop>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-018",
        "title": "Animated Masonry",
        "description": "Fade in items",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-6 space-y-6">
        <div class="break-inside-avoid rounded-xl overflow-hidden animate-fade-in-up" style="animation-delay: 0ms;">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden animate-fade-in-up" style="animation-delay: 100ms;">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=700&q=80" class="w-full object-cover">
        </div>
        <div class="break-inside-avoid rounded-xl overflow-hidden animate-fade-in-up" style="animation-delay: 200ms;">
          <img src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=500&q=80" class="w-full object-cover">
        </div>
      </div>
    </div>
    <style>
      @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
      .animate-fade-in-up { animation: fadeInUp 0.6s ease-out forwards; opacity: 0; }
    </style>
  </div>"""
    },
    {
        "id": "gallery-019",
        "title": "Masonry Portfolio",
        "description": "Project showcase",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-2 gap-12 space-y-12">
        <div class="break-inside-avoid">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full rounded-lg mb-4">
          <h3 class="text-2xl font-bold text-slate-900">Brand Identity</h3>
          <p class="text-slate-600 mt-2">Rebranding for a major tech startup.</p>
        </div>
        <div class="break-inside-avoid">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=1000&q=80" class="w-full rounded-lg mb-4">
          <h3 class="text-2xl font-bold text-slate-900">Editorial Design</h3>
          <p class="text-slate-600 mt-2">Magazine layout and typography.</p>
        </div>
        <div class="break-inside-avoid">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=600&q=80" class="w-full rounded-lg mb-4">
          <h3 class="text-2xl font-bold text-slate-900">Web Development</h3>
          <p class="text-slate-600 mt-2">Responsive website for a non-profit.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-020",
        "title": "Masonry Blog",
        "description": "Article grid",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="columns-1 md:columns-3 gap-8 space-y-8">
        <div class="break-inside-avoid bg-white p-6 rounded-xl shadow-sm">
          <span class="text-primary-600 text-sm font-bold uppercase">Design</span>
          <h3 class="text-xl font-bold text-slate-900 mt-2 mb-4">The Future of UI</h3>
          <p class="text-slate-600">Exploring upcoming trends in user interface design.</p>
        </div>
        <div class="break-inside-avoid bg-white rounded-xl shadow-sm overflow-hidden">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover">
          <div class="p-6">
            <span class="text-primary-600 text-sm font-bold uppercase">Tech</span>
            <h3 class="text-xl font-bold text-slate-900 mt-2 mb-4">AI Revolution</h3>
            <p class="text-slate-600">How artificial intelligence is changing everything.</p>
          </div>
        </div>
        <div class="break-inside-avoid bg-slate-900 p-6 rounded-xl shadow-sm text-white">
          <span class="text-primary-400 text-sm font-bold uppercase">Quote</span>
          <h3 class="text-xl font-bold mt-2 mb-4">"Design is not just what it looks like and feels like. Design is how it works."</h3>
          <p class="text-slate-400">- Steve Jobs</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-021",
        "title": "Basic Carousel",
        "description": "Simple slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-4xl mx-auto px-6 relative">
      <div class="overflow-hidden rounded-xl aspect-video relative">
        <template x-for="(slide, index) in slides" :key="index">
          <div x-show="active === index" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform translate-x-full" x-transition:enter-end="opacity-100 transform translate-x-0" x-transition:leave="transition ease-in duration-300" x-transition:leave-start="opacity-100 transform translate-x-0" x-transition:leave-end="opacity-0 transform -translate-x-full" class="absolute inset-0">
            <img :src="slide" class="w-full h-full object-cover">
          </div>
        </template>
      </div>
      <button @click="active = active === 0 ? slides.length - 1 : active - 1" class="absolute top-1/2 left-8 transform -translate-y-1/2 bg-white/80 p-2 rounded-full hover:bg-white transition-colors">
        <svg class="w-6 h-6 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
      </button>
      <button @click="active = active === slides.length - 1 ? 0 : active + 1" class="absolute top-1/2 right-8 transform -translate-y-1/2 bg-white/80 p-2 rounded-full hover:bg-white transition-colors">
        <svg class="w-6 h-6 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-022",
        "title": "Carousel with Thumbnails",
        "description": "Slider with preview",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-4xl mx-auto px-6">
      <div class="overflow-hidden rounded-xl aspect-video mb-4">
        <img :src="slides[active]" class="w-full h-full object-cover transition-opacity duration-300">
      </div>
      <div class="grid grid-cols-4 gap-4">
        <template x-for="(slide, index) in slides" :key="index">
          <button @click="active = index" :class="active === index ? 'ring-2 ring-primary-500' : 'opacity-70 hover:opacity-100'" class="rounded-lg overflow-hidden aspect-video transition-all">
            <img :src="slide" class="w-full h-full object-cover">
          </button>
        </template>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-023",
        "title": "Carousel Full Width",
        "description": "Edge-to-edge slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80',
    'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80'
  ] }">
    <div class="relative h-[600px] overflow-hidden">
      <template x-for="(slide, index) in slides" :key="index">
        <div x-show="active === index" class="absolute inset-0 transition-opacity duration-700">
          <img :src="slide" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/30"></div>
        </div>
      </template>
      <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex gap-2">
        <template x-for="(slide, index) in slides" :key="index">
          <button @click="active = index" :class="active === index ? 'bg-white w-8' : 'bg-white/50 w-2 hover:bg-white'" class="h-2 rounded-full transition-all duration-300"></button>
        </template>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-024",
        "title": "Carousel with Captions",
        "description": "Slider with text",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24" x-data="{ active: 0, slides: [
    { img: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80', title: 'Urban Exploration', desc: 'Discovering the city secrets.' },
    { img: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80', title: 'Natural Wonders', desc: 'Beauty of the wild.' }
  ] }">
    <div class="max-w-5xl mx-auto px-6">
      <div class="relative rounded-2xl overflow-hidden aspect-[2/1]">
        <template x-for="(slide, index) in slides" :key="index">
          <div x-show="active === index" class="absolute inset-0">
            <img :src="slide.img" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-12">
              <div>
                <h2 class="text-3xl font-bold text-white mb-2" x-text="slide.title"></h2>
                <p class="text-slate-300 text-lg" x-text="slide.desc"></p>
              </div>
            </div>
          </div>
        </template>
        <div class="absolute bottom-12 right-12 flex gap-4">
          <button @click="active = active === 0 ? slides.length - 1 : active - 1" class="w-12 h-12 rounded-full border border-white/30 text-white flex items-center justify-center hover:bg-white hover:text-slate-900 transition-all">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
          </button>
          <button @click="active = active === slides.length - 1 ? 0 : active + 1" class="w-12 h-12 rounded-full border border-white/30 text-white flex items-center justify-center hover:bg-white hover:text-slate-900 transition-all">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-025",
        "title": "Auto-Play Carousel",
        "description": "Automatic slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ], timer: null }" x-init="timer = setInterval(() => { active = active === slides.length - 1 ? 0 : active + 1 }, 3000)">
    <div class="max-w-4xl mx-auto px-6">
      <div class="overflow-hidden rounded-xl aspect-video relative group">
        <template x-for="(slide, index) in slides" :key="index">
          <div x-show="active === index" x-transition:enter="transition ease-out duration-500" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-500" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" class="absolute inset-0">
            <img :src="slide" class="w-full h-full object-cover">
          </div>
        </template>
        <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2">
          <template x-for="(slide, index) in slides" :key="index">
            <button @click="active = index; clearInterval(timer); timer = setInterval(() => { active = active === slides.length - 1 ? 0 : active + 1 }, 3000)" :class="active === index ? 'bg-white w-6' : 'bg-white/50 w-2'" class="h-2 rounded-full transition-all duration-300"></button>
          </template>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    }
]
# Placeholder for Gallery 026-050
# Part 2: Gallery 026-038
TEMPLATES_GALLERY_2 = [
    {
        "id": "gallery-026",
        "title": "Fade Carousel",
        "description": "Fade transition slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative overflow-hidden rounded-xl aspect-video shadow-lg">
        <template x-for="(slide, index) in slides" :key="index">
          <div x-show="active === index" x-transition:enter="transition ease-out duration-1000" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-1000" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" class="absolute inset-0">
            <img :src="slide" class="w-full h-full object-cover">
          </div>
        </template>
        <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2 z-10">
          <template x-for="(slide, index) in slides" :key="index">
            <button @click="active = index" :class="active === index ? 'bg-white w-3 h-3' : 'bg-white/50 w-3 h-3 hover:bg-white'" class="rounded-full transition-colors"></button>
          </template>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-027",
        "title": "3D Carousel",
        "description": "Perspective slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24 overflow-hidden" x-data="{ active: 1, slides: [
    'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80'
  ] }">
    <div class="max-w-6xl mx-auto px-6">
      <div class="flex items-center justify-center h-[400px] perspective-1000">
        <template x-for="(slide, index) in slides" :key="index">
          <div @click="active = index" class="absolute w-[300px] md:w-[500px] aspect-video rounded-xl overflow-hidden shadow-2xl transition-all duration-500 cursor-pointer border-4 border-slate-800"
               :class="{
                 'z-20 scale-100 opacity-100 translate-x-0': active === index,
                 'z-10 scale-75 opacity-60 -translate-x-[60%]': index === active - 1 || (active === 0 && index === slides.length - 1),
                 'z-10 scale-75 opacity-60 translate-x-[60%]': index === active + 1 || (active === slides.length - 1 && index === 0)
               }">
            <img :src="slide" class="w-full h-full object-cover">
          </div>
        </template>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
    <style>
      .perspective-1000 { perspective: 1000px; }
    </style>
  </div>"""
    },
    {
        "id": "gallery-028",
        "title": "Carousel with Counter",
        "description": "Numbered slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-4xl mx-auto px-6">
      <div class="flex justify-between items-end mb-4">
        <h2 class="text-2xl font-bold text-slate-900">Featured Work</h2>
        <div class="text-lg font-mono text-slate-500">
          <span class="text-slate-900 font-bold" x-text="active + 1"></span> / <span x-text="slides.length"></span>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-xl aspect-video bg-slate-100">
        <template x-for="(slide, index) in slides" :key="index">
          <div x-show="active === index" class="absolute inset-0 transition-opacity duration-300">
            <img :src="slide" class="w-full h-full object-cover">
          </div>
        </template>
        <div class="absolute bottom-0 right-0 bg-white p-4 rounded-tl-xl flex gap-4">
          <button @click="active = active === 0 ? slides.length - 1 : active - 1" class="text-slate-900 hover:text-primary-600 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
          </button>
          <button @click="active = active === slides.length - 1 ? 0 : active + 1" class="text-slate-900 hover:text-primary-600 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-029",
        "title": "Multi-Row Carousel",
        "description": "Grid slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ active: 0, pages: [
    [
      'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80',
      'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80',
      'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80',
      'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80'
    ],
    [
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80',
      'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80',
      'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80',
      'https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80'
    ]
  ] }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="relative overflow-hidden">
        <template x-for="(page, index) in pages" :key="index">
          <div x-show="active === index" class="grid grid-cols-2 md:grid-cols-4 gap-4" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform translate-x-8" x-transition:enter-end="opacity-100 transform translate-x-0">
            <template x-for="img in page" :key="img">
              <div class="aspect-square rounded-xl overflow-hidden">
                <img :src="img" class="w-full h-full object-cover hover:scale-110 transition-transform duration-500">
              </div>
            </template>
          </div>
        </template>
      </div>
      <div class="flex justify-center gap-4 mt-8">
        <button @click="active = active === 0 ? pages.length - 1 : active - 1" class="p-2 rounded-full bg-white shadow-sm hover:bg-slate-50 text-slate-600">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>
        <button @click="active = active === pages.length - 1 ? 0 : active + 1" class="p-2 rounded-full bg-white shadow-sm hover:bg-slate-50 text-slate-600">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </button>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-030",
        "title": "Vertical Carousel",
        "description": "Up/down slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ active: 0, slides: [
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row gap-8 h-[500px]">
      <div class="flex-1 relative overflow-hidden rounded-2xl">
        <template x-for="(slide, index) in slides" :key="index">
          <div x-show="active === index" class="absolute inset-0 transition-opacity duration-500">
            <img :src="slide" class="w-full h-full object-cover">
          </div>
        </template>
      </div>
      <div class="w-full md:w-64 flex flex-row md:flex-col gap-4 overflow-auto">
        <template x-for="(slide, index) in slides" :key="index">
          <button @click="active = index" :class="active === index ? 'ring-2 ring-primary-500 opacity-100' : 'opacity-60 hover:opacity-100'" class="flex-shrink-0 w-32 md:w-full aspect-video rounded-lg overflow-hidden transition-all">
            <img :src="slide" class="w-full h-full object-cover">
          </button>
        </template>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-031",
        "title": "Basic Lightbox",
        "description": "Simple image modal",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ open: false, src: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="aspect-square rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity" @click="open = true; src = 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity" @click="open = true; src = 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity" @click="open = true; src = 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
        <div class="aspect-square rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity" @click="open = true; src = 'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4" @click="open = false" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-200" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" style="display: none;">
      <img :src="src" class="max-w-full max-h-full rounded shadow-2xl" @click.stop>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-032",
        "title": "Lightbox with Captions",
        "description": "Modal with text",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ open: false, src: '', caption: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="group cursor-pointer" @click="open = true; src = 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'; caption = 'Portrait Session'">
          <div class="rounded-xl overflow-hidden mb-3">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="font-bold text-slate-900">Portrait Session</h3>
        </div>
        <div class="group cursor-pointer" @click="open = true; src = 'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'; caption = 'Urban Lifestyle'">
          <div class="rounded-xl overflow-hidden mb-3">
            <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="font-bold text-slate-900">Urban Lifestyle</h3>
        </div>
        <div class="group cursor-pointer" @click="open = true; src = 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'; caption = 'Nature Walk'">
          <div class="rounded-xl overflow-hidden mb-3">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="font-bold text-slate-900">Nature Walk</h3>
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex flex-col items-center justify-center p-4" @click="open = false" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-200" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" style="display: none;">
      <img :src="src" class="max-w-full max-h-[80vh] rounded shadow-2xl mb-4" @click.stop>
      <p class="text-white text-xl font-medium" x-text="caption" @click.stop></p>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-033",
        "title": "Lightbox Gallery",
        "description": "Navigate between images",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24" x-data="{ open: false, active: 0, images: [
    'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <template x-for="(img, index) in images" :key="index">
          <div class="aspect-video rounded-xl overflow-hidden cursor-pointer border border-slate-700 hover:border-primary-500 transition-colors" @click="open = true; active = index">
            <img :src="img" class="w-full h-full object-cover">
          </div>
        </template>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex items-center justify-center" @click="open = false" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" style="display: none;">
      <div class="relative w-full max-w-5xl px-12" @click.stop>
        <img :src="images[active]" class="w-full max-h-[80vh] object-contain rounded-lg">
        <button class="absolute left-0 top-1/2 transform -translate-y-1/2 text-white hover:text-primary-400 p-4" @click="active = active === 0 ? images.length - 1 : active - 1">
          <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>
        <button class="absolute right-0 top-1/2 transform -translate-y-1/2 text-white hover:text-primary-400 p-4" @click="active = active === images.length - 1 ? 0 : active + 1">
          <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </button>
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-034",
        "title": "Lightbox with Zoom",
        "description": "Pan and zoom image",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ open: false, src: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="aspect-square rounded-xl overflow-hidden cursor-pointer" @click="open = true; src = 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80'">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover hover:scale-110 transition-transform duration-500">
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex items-center justify-center overflow-hidden" @click="open = false" style="display: none;">
      <div class="relative w-full h-full flex items-center justify-center" x-data="{ scale: 1, x: 0, y: 0, panning: false, startX: 0, startY: 0 }" @click.stop>
        <img :src="src" class="max-w-full max-h-full transition-transform duration-100 cursor-move"
             :style="`transform: translate(${x}px, ${y}px) scale(${scale})`"
             @wheel.prevent="scale = Math.min(Math.max(1, scale + $event.deltaY * -0.01), 4)"
             @mousedown="panning = true; startX = $event.clientX - x; startY = $event.clientY - y"
             @mousemove="if(panning) { x = $event.clientX - startX; y = $event.clientY - startY }"
             @mouseup="panning = false"
             @mouseleave="panning = false">
      </div>
      <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 text-white bg-black/50 px-4 py-2 rounded-full text-sm">
        Scroll to zoom, drag to pan
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-035",
        "title": "Lightbox with Navigation",
        "description": "Keyboard nav support",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ open: false, active: 0, images: [
    'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }" @keydown.escape.window="open = false" @keydown.arrow-left.window="active = active === 0 ? images.length - 1 : active - 1" @keydown.arrow-right.window="active = active === images.length - 1 ? 0 : active + 1">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <template x-for="(img, index) in images" :key="index">
          <div class="aspect-video rounded-xl overflow-hidden cursor-pointer hover:shadow-lg transition-shadow" @click="open = true; active = index">
            <img :src="img" class="w-full h-full object-cover">
          </div>
        </template>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex items-center justify-center" style="display: none;">
      <div class="relative w-full max-w-5xl px-12">
        <img :src="images[active]" class="w-full max-h-[80vh] object-contain rounded-lg shadow-2xl">
      </div>
      <div class="absolute bottom-8 text-white text-sm">
        Use arrow keys to navigate, ESC to close
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-036",
        "title": "Lightbox with Thumbnails",
        "description": "Thumbnails in modal",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ open: false, active: 0, images: [
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
  ] }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <template x-for="(img, index) in images" :key="index">
          <div class="aspect-square rounded-xl overflow-hidden cursor-pointer" @click="open = true; active = index">
            <img :src="img" class="w-full h-full object-cover hover:opacity-80 transition-opacity">
          </div>
        </template>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex flex-col items-center justify-center p-8" @click="open = false" style="display: none;">
      <div class="flex-1 flex items-center justify-center w-full mb-8" @click.stop>
        <img :src="images[active]" class="max-w-full max-h-full rounded-lg shadow-2xl">
      </div>
      <div class="h-20 flex gap-4 overflow-x-auto max-w-full px-4" @click.stop>
        <template x-for="(img, index) in images" :key="index">
          <button @click="active = index" :class="active === index ? 'ring-2 ring-white opacity-100' : 'opacity-50 hover:opacity-100'" class="h-full aspect-square rounded-lg overflow-hidden transition-all flex-shrink-0">
            <img :src="img" class="w-full h-full object-cover">
          </button>
        </template>
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-037",
        "title": "Lightbox Full Screen",
        "description": "Immersive view",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24" x-data="{ open: false, src: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="rounded-xl overflow-hidden cursor-pointer" @click="open = true; src = 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80'">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-64 object-cover">
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black flex items-center justify-center" @click="open = false" style="display: none;">
      <img :src="src" class="w-full h-full object-contain">
      <button class="absolute top-6 right-6 text-white/50 hover:text-white transition-colors" @click="open = false">
        <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-038",
        "title": "Lightbox with Video",
        "description": "Video support",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ open: false }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="max-w-md mx-auto">
        <div class="relative rounded-xl overflow-hidden cursor-pointer group" @click="open = true">
          <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-64 object-cover">
          <div class="absolute inset-0 bg-black/30 flex items-center justify-center group-hover:bg-black/40 transition-colors">
            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-primary-600 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4" @click="open = false" style="display: none;">
      <div class="w-full max-w-4xl aspect-video bg-black rounded-xl overflow-hidden shadow-2xl" @click.stop>
        <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    }
]
# Part 2 continued: Gallery 039-044
TEMPLATES_GALLERY_2_PART_2 = [
    {
        "id": "gallery-039",
        "title": "Lightbox with Info Panel",
        "description": "Detailed view",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ open: false, active: 0, images: [
    { src: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80', title: 'Portrait Session', desc: 'Studio photography with natural lighting.', date: 'Oct 24, 2023', author: 'Jane Doe' },
    { src: 'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80', title: 'Urban Lifestyle', desc: 'Capturing the essence of city life.', date: 'Nov 12, 2023', author: 'John Smith' }
  ] }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <template x-for="(item, index) in images" :key="index">
          <div class="rounded-xl overflow-hidden cursor-pointer bg-white shadow-sm hover:shadow-md transition-shadow" @click="open = true; active = index">
            <img :src="item.src" class="w-full h-64 object-cover">
            <div class="p-4">
              <h3 class="font-bold text-slate-900" x-text="item.title"></h3>
              <p class="text-slate-500 text-sm" x-text="item.desc"></p>
            </div>
          </div>
        </template>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex items-center justify-center p-4 md:p-12" @click="open = false" style="display: none;">
      <div class="bg-white w-full max-w-6xl h-[80vh] rounded-xl overflow-hidden flex flex-col md:flex-row" @click.stop>
        <div class="flex-1 bg-black flex items-center justify-center relative">
          <img :src="images[active].src" class="max-w-full max-h-full object-contain">
          <button class="absolute left-4 top-1/2 transform -translate-y-1/2 text-white/50 hover:text-white" @click="active = active === 0 ? images.length - 1 : active - 1">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
          </button>
          <button class="absolute right-4 top-1/2 transform -translate-y-1/2 text-white/50 hover:text-white" @click="active = active === images.length - 1 ? 0 : active + 1">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
        </div>
        <div class="w-full md:w-96 p-8 overflow-y-auto">
          <h2 class="text-2xl font-bold text-slate-900 mb-2" x-text="images[active].title"></h2>
          <p class="text-slate-600 mb-6" x-text="images[active].desc"></p>

          <div class="space-y-4 border-t border-slate-100 pt-6">
            <div>
              <span class="block text-xs font-bold text-slate-400 uppercase tracking-wider">Date</span>
              <span class="text-slate-900" x-text="images[active].date"></span>
            </div>
            <div>
              <span class="block text-xs font-bold text-slate-400 uppercase tracking-wider">Photographer</span>
              <span class="text-slate-900" x-text="images[active].author"></span>
            </div>
            <div>
              <span class="block text-xs font-bold text-slate-400 uppercase tracking-wider">License</span>
              <span class="text-slate-900">Unsplash License</span>
            </div>
          </div>

          <button class="w-full mt-8 px-6 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 transition-colors">Download Image</button>
        </div>
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-040",
        "title": "Lightbox Social Share",
        "description": "Share functionality",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ open: false, src: '' }">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="rounded-xl overflow-hidden cursor-pointer" @click="open = true; src = 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-64 object-cover">
        </div>
      </div>
    </div>

    <div x-show="open" class="fixed inset-0 z-50 bg-black/95 flex items-center justify-center p-4" @click="open = false" style="display: none;">
      <div class="relative max-w-4xl w-full" @click.stop>
        <img :src="src" class="w-full rounded-lg shadow-2xl mb-4">
        <div class="flex justify-center gap-4">
          <button class="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.791-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            Share
          </button>
          <button class="flex items-center gap-2 px-4 py-2 bg-sky-500 text-white rounded-lg hover:bg-sky-600 transition-colors">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.84 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
            Tweet
          </button>
          <button class="flex items-center gap-2 px-4 py-2 bg-slate-700 text-white rounded-lg hover:bg-slate-800 transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
            Copy Link
          </button>
        </div>
      </div>
      <button class="absolute top-4 right-4 text-white hover:text-gray-300" @click="open = false">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-041",
        "title": "Horizontal Scroll Gallery",
        "description": "Side scroll view",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex overflow-x-auto gap-6 pb-8 snap-x snap-mandatory hide-scrollbar">
        <div class="flex-shrink-0 w-80 md:w-96 snap-center">
          <div class="rounded-xl overflow-hidden shadow-sm">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
            <div class="bg-white p-4">
              <h3 class="font-bold text-slate-900">Project One</h3>
            </div>
          </div>
        </div>
        <div class="flex-shrink-0 w-80 md:w-96 snap-center">
          <div class="rounded-xl overflow-hidden shadow-sm">
            <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
            <div class="bg-white p-4">
              <h3 class="font-bold text-slate-900">Project Two</h3>
            </div>
          </div>
        </div>
        <div class="flex-shrink-0 w-80 md:w-96 snap-center">
          <div class="rounded-xl overflow-hidden shadow-sm">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
            <div class="bg-white p-4">
              <h3 class="font-bold text-slate-900">Project Three</h3>
            </div>
          </div>
        </div>
        <div class="flex-shrink-0 w-80 md:w-96 snap-center">
          <div class="rounded-xl overflow-hidden shadow-sm">
            <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
            <div class="bg-white p-4">
              <h3 class="font-bold text-slate-900">Project Four</h3>
            </div>
          </div>
        </div>
        <div class="flex-shrink-0 w-80 md:w-96 snap-center">
          <div class="rounded-xl overflow-hidden shadow-sm">
            <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-64 object-cover">
            <div class="bg-white p-4">
              <h3 class="font-bold text-slate-900">Project Five</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
    <style>
      .hide-scrollbar::-webkit-scrollbar { display: none; }
      .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
  </div>"""
    },
    {
        "id": "gallery-042",
        "title": "Parallax Gallery",
        "description": "Scroll effect",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white">
    <div class="relative h-[600px] bg-fixed bg-center bg-cover flex items-center justify-center" style="background-image: url('https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80');">
      <div class="bg-black/50 p-8 rounded-xl text-center backdrop-blur-sm">
        <h2 class="text-4xl font-bold text-white mb-2">Parallax Effect</h2>
        <p class="text-slate-200">Scroll to see the magic</p>
      </div>
    </div>
    <div class="py-24 max-w-4xl mx-auto px-6 text-center">
      <h3 class="text-2xl font-bold text-slate-900 mb-4">Content Section</h3>
      <p class="text-slate-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
    <div class="relative h-[600px] bg-fixed bg-center bg-cover flex items-center justify-center" style="background-image: url('https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80');">
      <div class="bg-black/50 p-8 rounded-xl text-center backdrop-blur-sm">
        <h2 class="text-4xl font-bold text-white mb-2">Another Section</h2>
        <p class="text-slate-200">Keep scrolling</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-043",
        "title": "Mosaic Gallery",
        "description": "Complex grid",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 grid-rows-4 gap-4 h-[800px]">
        <div class="col-span-2 row-span-2 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
        <div class="col-span-1 row-span-1 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
        <div class="col-span-1 row-span-2 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
        <div class="col-span-1 row-span-1 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
        <div class="col-span-2 row-span-1 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
        <div class="col-span-1 row-span-1 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
        <div class="col-span-1 row-span-1 rounded-xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-044",
        "title": "Polaroid Gallery",
        "description": "Retro style",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-100 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex flex-wrap justify-center gap-8">
        <div class="bg-white p-4 pb-12 shadow-lg transform -rotate-2 hover:rotate-0 transition-transform duration-300 w-64">
          <div class="aspect-square bg-gray-200 mb-4 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-500">
          </div>
          <p class="font-handwriting text-xl text-center text-slate-700">Summer 2023</p>
        </div>
        <div class="bg-white p-4 pb-12 shadow-lg transform rotate-3 hover:rotate-0 transition-transform duration-300 w-64 mt-8">
          <div class="aspect-square bg-gray-200 mb-4 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-500">
          </div>
          <p class="font-handwriting text-xl text-center text-slate-700">City Vibes</p>
        </div>
        <div class="bg-white p-4 pb-12 shadow-lg transform -rotate-1 hover:rotate-0 transition-transform duration-300 w-64">
          <div class="aspect-square bg-gray-200 mb-4 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-500">
          </div>
          <p class="font-handwriting text-xl text-center text-slate-700">Road Trip</p>
        </div>
      </div>
    </div>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');
      .font-handwriting { font-family: 'Indie Flower', cursive; }
    </style>
  </div>"""
    }
]
# Part 2 continued: Gallery 045-050
TEMPLATES_GALLERY_2_PART_3 = [
    {
        "id": "gallery-045",
        "title": "Timeline Gallery",
        "description": "Chronological view",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative border-l-2 border-slate-200 ml-4 md:ml-0 space-y-12">
        <div class="relative pl-8 md:pl-0">
          <div class="absolute top-0 left-[-9px] w-4 h-4 bg-primary-600 rounded-full border-4 border-white"></div>
          <div class="md:flex gap-8 items-start">
            <div class="md:w-1/2 md:text-right md:pr-8 mb-4 md:mb-0">
              <span class="text-primary-600 font-bold">2023</span>
              <h3 class="text-xl font-bold text-slate-900">Project Launch</h3>
              <p class="text-slate-600 mt-2">Initial release of the platform.</p>
            </div>
            <div class="md:w-1/2">
              <div class="rounded-xl overflow-hidden shadow-sm">
                <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover">
              </div>
            </div>
          </div>
        </div>
        <div class="relative pl-8 md:pl-0">
          <div class="absolute top-0 left-[-9px] w-4 h-4 bg-primary-600 rounded-full border-4 border-white"></div>
          <div class="md:flex gap-8 items-start flex-row-reverse">
            <div class="md:w-1/2 md:pl-8 mb-4 md:mb-0">
              <span class="text-primary-600 font-bold">2022</span>
              <h3 class="text-xl font-bold text-slate-900">Development Phase</h3>
              <p class="text-slate-600 mt-2">Building the core infrastructure.</p>
            </div>
            <div class="md:w-1/2">
              <div class="rounded-xl overflow-hidden shadow-sm">
                <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover">
              </div>
            </div>
          </div>
        </div>
        <div class="relative pl-8 md:pl-0">
          <div class="absolute top-0 left-[-9px] w-4 h-4 bg-primary-600 rounded-full border-4 border-white"></div>
          <div class="md:flex gap-8 items-start">
            <div class="md:w-1/2 md:text-right md:pr-8 mb-4 md:mb-0">
              <span class="text-primary-600 font-bold">2021</span>
              <h3 class="text-xl font-bold text-slate-900">Concept Design</h3>
              <p class="text-slate-600 mt-2">Planning and prototyping.</p>
            </div>
            <div class="md:w-1/2">
              <div class="rounded-xl overflow-hidden shadow-sm">
                <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-046",
        "title": "Story Gallery",
        "description": "Narrative layout",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center mb-24">
        <div class="order-2 md:order-1">
          <div class="grid grid-cols-2 gap-4">
            <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="rounded-xl w-full h-64 object-cover mt-12">
            <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="rounded-xl w-full h-64 object-cover">
          </div>
        </div>
        <div class="order-1 md:order-2">
          <span class="text-primary-600 font-bold uppercase tracking-wider">Our Story</span>
          <h2 class="text-4xl font-bold text-slate-900 mt-2 mb-6">Beginning of the Journey</h2>
          <p class="text-slate-600 text-lg leading-relaxed">It started with a simple idea. We wanted to create something that would change the way people interact with technology. Through countless hours of dedication and hard work, we brought our vision to life.</p>
        </div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div>
          <span class="text-primary-600 font-bold uppercase tracking-wider">Growth</span>
          <h2 class="text-4xl font-bold text-slate-900 mt-2 mb-6">Expanding Horizons</h2>
          <p class="text-slate-600 text-lg leading-relaxed">As we grew, so did our ambitions. We reached new markets, connected with more people, and continued to innovate. Every step forward was a lesson learned and a milestone achieved.</p>
        </div>
        <div>
          <div class="grid grid-cols-2 gap-4">
            <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="rounded-xl w-full h-64 object-cover">
            <img src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="rounded-xl w-full h-64 object-cover mt-12">
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-047",
        "title": "Before/After Gallery",
        "description": "Comparison slider",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24" x-data="{ slider: 50 }">
    <div class="max-w-4xl mx-auto px-6">
      <div class="relative w-full aspect-video rounded-xl overflow-hidden select-none cursor-ew-resize" @mousemove="slider = (($event.clientX - $el.getBoundingClientRect().left) / $el.offsetWidth) * 100" @touchmove="slider = (($event.touches[0].clientX - $el.getBoundingClientRect().left) / $el.offsetWidth) * 100">
        <div class="absolute inset-0">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80&sat=-100" class="w-full h-full object-cover grayscale">
          <div class="absolute top-4 left-4 bg-black/50 text-white px-3 py-1 rounded text-sm font-bold">Before</div>
        </div>
        <div class="absolute inset-0 border-r-4 border-white" :style="`width: ${slider}%`">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80" class="w-full h-full object-cover max-w-none" :style="`width: ${$el.parentElement.offsetWidth}px`">
          <div class="absolute top-4 right-4 bg-primary-600/80 text-white px-3 py-1 rounded text-sm font-bold">After</div>
        </div>
        <div class="absolute inset-y-0 w-10 h-10 bg-white rounded-full shadow-lg flex items-center justify-center transform -translate-x-1/2 top-1/2 -mt-5" :style="`left: ${slider}%`">
          <svg class="w-6 h-6 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l4-4 4 4m0 6l-4 4-4-4"></path></svg>
        </div>
      </div>
      <div class="text-center mt-8">
        <h3 class="text-2xl font-bold text-slate-900">Color Correction</h3>
        <p class="text-slate-600 mt-2">Drag the slider to see the difference.</p>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-048",
        "title": "360 View Gallery",
        "description": "Product rotation",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-50 py-24" x-data="{ frame: 0, totalFrames: 36, dragging: false, startX: 0, startFrame: 0 }">
    <div class="max-w-3xl mx-auto px-6">
      <div class="bg-white rounded-xl shadow-lg p-8">
        <div class="aspect-square relative cursor-ew-resize"
             @mousedown="dragging = true; startX = $event.clientX; startFrame = frame"
             @mousemove="if(dragging) { let delta = $event.clientX - startX; frame = (startFrame + Math.floor(delta / 10)) % totalFrames; if(frame < 0) frame += totalFrames; }"
             @mouseup="dragging = false"
             @mouseleave="dragging = false">
          <template x-for="i in totalFrames" :key="i">
            <img :src="`https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80&text=${i}`"
                 x-show="frame === i - 1"
                 class="w-full h-full object-contain pointer-events-none select-none">
          </template>
          <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-slate-900/10 px-4 py-2 rounded-full flex items-center gap-2">
            <svg class="w-5 h-5 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            <span class="text-sm font-medium text-slate-600">Drag to rotate</span>
          </div>
        </div>
        <div class="text-center mt-8">
          <h3 class="text-2xl font-bold text-slate-900">Product 360 View</h3>
          <p class="text-slate-600 mt-2">Interactive product demonstration.</p>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "gallery-049",
        "title": "Video Gallery",
        "description": "Video grid",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="group relative rounded-xl overflow-hidden cursor-pointer">
          <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition-opacity">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center group-hover:bg-primary-600 transition-colors">
              <svg class="w-6 h-6 text-white ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
            <h3 class="text-white font-bold">Nature Documentary</h3>
            <span class="text-slate-300 text-sm">12:45</span>
          </div>
        </div>
        <div class="group relative rounded-xl overflow-hidden cursor-pointer">
          <img src="https://images.unsplash.com/photo-1516035069371-29a1b244cc32?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition-opacity">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center group-hover:bg-primary-600 transition-colors">
              <svg class="w-6 h-6 text-white ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
            <h3 class="text-white font-bold">Tech Review</h3>
            <span class="text-slate-300 text-sm">08:30</span>
          </div>
        </div>
        <div class="group relative rounded-xl overflow-hidden cursor-pointer">
          <img src="https://images.unsplash.com/photo-1536240478700-b869070f9279?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition-opacity">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center group-hover:bg-primary-600 transition-colors">
              <svg class="w-6 h-6 text-white ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
            <h3 class="text-white font-bold">Travel Vlog</h3>
            <span class="text-slate-300 text-sm">15:20</span>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "gallery-050",
        "title": "Mixed Media Gallery",
        "description": "Images, video, audio",
        "dir": "templates/09-gallery",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 auto-rows-[200px]">
        <div class="md:col-span-2 md:row-span-2 rounded-xl overflow-hidden relative group">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover">
          <div class="absolute top-4 right-4 bg-white/90 p-2 rounded-full">
            <svg class="w-5 h-5 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
          </div>
        </div>
        <div class="md:col-span-1 md:row-span-1 rounded-xl overflow-hidden relative group bg-slate-900 flex items-center justify-center">
          <div class="text-center p-4">
            <div class="w-12 h-12 bg-primary-600 rounded-full flex items-center justify-center mx-auto mb-2">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>
            </div>
            <span class="text-white font-bold text-sm">Podcast Ep. 1</span>
          </div>
        </div>
        <div class="md:col-span-1 md:row-span-2 rounded-xl overflow-hidden relative group">
          <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
            <div class="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-primary-600 transition-colors cursor-pointer">
              <svg class="w-6 h-6 text-white ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
        </div>
        <div class="md:col-span-1 md:row-span-1 rounded-xl overflow-hidden relative group bg-slate-100 p-6 flex flex-col justify-center">
          <h3 class="font-bold text-slate-900 text-lg">Article</h3>
          <p class="text-slate-600 text-sm mt-2 line-clamp-3">Read our latest thoughts on design and technology.</p>
        </div>
      </div>
    </div>
  </div>"""
    }
]
# Placeholder for Forms 001-050
# Part 1: Forms 001-006
TEMPLATES_FORMS_1 = [
    {
        "id": "form-001",
        "title": "Simple Contact Form",
        "description": "Basic contact form",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-slate-900">Get in touch</h2>
          <p class="text-slate-600 mt-4">We'd love to hear from you. Send us a message.</p>
        </div>
        <form class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Full Name</label>
            <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="John Doe">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
            <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="john@example.com">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Message</label>
            <textarea rows="4" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="How can we help?"></textarea>
          </div>
          <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Send Message</button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-002",
        "title": "Contact with Map",
        "description": "Split layout with map",
        "dir": "templates/10-forms",
        "content": """<div class="bg-white py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
        <div>
          <h2 class="text-4xl font-bold text-slate-900 mb-6">Let's talk about your project</h2>
          <p class="text-slate-600 text-lg mb-12">We help companies and individuals build out their brand guidelines.</p>

          <form class="space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div>
                <label class="block text-sm font-bold text-slate-900 mb-2">First Name</label>
                <input type="text" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="John">
              </div>
              <div>
                <label class="block text-sm font-bold text-slate-900 mb-2">Last Name</label>
                <input type="text" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Doe">
              </div>
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Email</label>
              <input type="email" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="john@example.com">
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Message</label>
              <textarea rows="4" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Tell us about your project..."></textarea>
            </div>
            <button class="bg-slate-900 text-white font-bold px-8 py-4 rounded-lg hover:bg-slate-800 transition-colors">Send Message</button>
          </form>
        </div>
        <div class="h-[600px] bg-gray-100 rounded-2xl overflow-hidden relative">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.1422937950147!2d-73.98731968482413!3d40.75889497932681!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25855c6480299%3A0x55194ec5a1ae072e!2sTimes+Square!5e0!3m2!1sen!2sus!4v1510522332001" width="100%" height="100%" frameborder="0" style="border:0" allowfullscreen></iframe>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-003",
        "title": "Login Form",
        "description": "Clean login page",
        "dir": "templates/10-forms",
        "content": """<div class="min-h-screen bg-gray-50 flex items-center justify-center py-12 px-6">
    <div class="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 md:p-12">
      <div class="text-center mb-10">
        <div class="w-16 h-16 bg-primary-100 text-primary-600 rounded-xl flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
        </div>
        <h2 class="text-3xl font-bold text-slate-900">Welcome back</h2>
        <p class="text-slate-600 mt-2">Please enter your details to sign in.</p>
      </div>

      <form class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Email</label>
          <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="Enter your email">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Password</label>
          <input type="password" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="••••••••">
        </div>
        <div class="flex items-center justify-between">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" class="w-4 h-4 text-primary-600 rounded border-gray-300 focus:ring-primary-500">
            <span class="text-sm text-slate-600">Remember me</span>
          </label>
          <a href="#" class="text-sm font-medium text-primary-600 hover:text-primary-700">Forgot password?</a>
        </div>
        <button class="w-full bg-slate-900 text-white font-bold py-3 rounded-lg hover:bg-slate-800 transition-colors">Sign in</button>
        <button class="w-full bg-white text-slate-700 font-bold py-3 rounded-lg border border-slate-200 hover:bg-gray-50 transition-colors flex items-center justify-center gap-2">
          <svg class="w-5 h-5" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
          Sign in with Google
        </button>
      </form>
      <p class="text-center text-slate-600 mt-8 text-sm">
        Don't have an account? <a href="#" class="font-bold text-primary-600 hover:text-primary-700">Sign up for free</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "form-004",
        "title": "Registration Form",
        "description": "Sign up page",
        "dir": "templates/10-forms",
        "content": """<div class="min-h-screen bg-white flex">
    <div class="flex-1 flex items-center justify-center px-6 py-12">
      <div class="max-w-md w-full">
        <div class="mb-10">
          <h2 class="text-4xl font-bold text-slate-900">Create an account</h2>
          <p class="text-slate-600 mt-3">Start your 30-day free trial today.</p>
        </div>

        <form class="space-y-5">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Full Name</label>
            <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="John Doe">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
            <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="john@example.com">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Password</label>
            <input type="password" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="Create a password">
            <p class="text-xs text-slate-500 mt-2">Must be at least 8 characters.</p>
          </div>
          <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Create Account</button>
        </form>
        <p class="text-center text-slate-600 mt-8 text-sm">
          Already have an account? <a href="#" class="font-bold text-primary-600 hover:text-primary-700">Log in</a>
        </p>
      </div>
    </div>
    <div class="hidden lg:block w-1/2 bg-primary-600 relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-primary-600 to-primary-900 opacity-90"></div>
      <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="absolute inset-0 w-full h-full object-cover mix-blend-overlay opacity-50">
      <div class="absolute inset-0 flex items-center justify-center p-16 text-white">
        <div>
          <h3 class="text-3xl font-bold mb-6">"This platform has completely transformed how we manage our team workflows."</h3>
          <div class="flex items-center gap-4">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80" class="w-12 h-12 rounded-full border-2 border-white/30">
            <div>
              <div class="font-bold">Sarah Williams</div>
              <div class="text-primary-200 text-sm">CEO at TechFlow</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-005",
        "title": "Newsletter Signup",
        "description": "Minimal signup",
        "dir": "templates/10-forms",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <h2 class="text-3xl md:text-4xl font-bold text-white mb-6">Join our newsletter</h2>
      <p class="text-slate-400 text-lg mb-10 max-w-2xl mx-auto">Get weekly insights on design, coding, and building digital products. No spam, unsubscribe anytime.</p>

      <form class="max-w-md mx-auto flex gap-4">
        <input type="email" class="flex-1 px-6 py-4 rounded-full bg-white/10 border border-white/10 text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:bg-white/20 transition-all" placeholder="Enter your email">
        <button class="bg-primary-600 text-white font-bold px-8 py-4 rounded-full hover:bg-primary-500 transition-colors shadow-lg shadow-primary-500/30">Subscribe</button>
      </form>
      <p class="text-slate-500 text-sm mt-6">We care about your data in our <a href="#" class="underline hover:text-white">privacy policy</a>.</p>
    </div>
  </div>"""
    },
    {
        "id": "form-006",
        "title": "Search Form",
        "description": "Search with filters",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-5xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-6">
        <form class="grid grid-cols-1 md:grid-cols-12 gap-4">
          <div class="md:col-span-5 relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </div>
            <input type="text" class="w-full pl-12 pr-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="Search for properties...">
          </div>
          <div class="md:col-span-3">
            <select class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all bg-white">
              <option>All Locations</option>
              <option>New York</option>
              <option>Los Angeles</option>
              <option>Chicago</option>
            </select>
          </div>
          <div class="md:col-span-2">
            <select class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all bg-white">
              <option>Any Price</option>
              <option>$100k - $200k</option>
              <option>$200k - $500k</option>
              <option>$500k+</option>
            </select>
          </div>
          <div class="md:col-span-2">
            <button class="w-full h-full bg-primary-600 text-white font-bold rounded-xl hover:bg-primary-700 transition-colors">Search</button>
          </div>
        </form>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_FORMS = TEMPLATES_FORMS_1

# Part 2: Forms 007-012
TEMPLATES_FORMS_2 = [
    {
        "id": "form-007",
        "title": "Checkout Form",
        "description": "Payment and shipping",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7">
          <h2 class="text-2xl font-bold text-slate-900 mb-8">Shipping Information</h2>
          <form class="space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">First Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Last Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Address</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">City</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">State</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">ZIP Code</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
            </div>

            <h2 class="text-2xl font-bold text-slate-900 mt-12 mb-8">Payment Details</h2>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Card Number</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="0000 0000 0000 0000">
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Expiration Date</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="MM/YY">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">CVC</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="123">
              </div>
            </div>
          </form>
        </div>
        <div class="lg:col-span-5">
          <div class="bg-white rounded-2xl shadow-lg p-8">
            <h3 class="text-xl font-bold text-slate-900 mb-6">Order Summary</h3>
            <div class="space-y-4 mb-6">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-4">
                  <div class="w-16 h-16 bg-gray-100 rounded-lg"></div>
                  <div>
                    <div class="font-bold text-slate-900">Premium Plan</div>
                    <div class="text-sm text-slate-500">Monthly subscription</div>
                  </div>
                </div>
                <div class="font-bold text-slate-900">$29.00</div>
              </div>
            </div>
            <div class="border-t border-slate-100 pt-4 space-y-2">
              <div class="flex justify-between text-slate-600">
                <span>Subtotal</span>
                <span>$29.00</span>
              </div>
              <div class="flex justify-between text-slate-600">
                <span>Tax</span>
                <span>$2.90</span>
              </div>
              <div class="flex justify-between text-xl font-bold text-slate-900 pt-4 border-t border-slate-100 mt-4">
                <span>Total</span>
                <span>$31.90</span>
              </div>
            </div>
            <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg mt-8 hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Pay Now</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-008",
        "title": "Multi-step Form",
        "description": "Progress indicator",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24" x-data="{ step: 1 }">
    <div class="max-w-3xl mx-auto px-6">
      <!-- Steps -->
      <div class="mb-12">
        <div class="flex items-center justify-between relative">
          <div class="absolute left-0 top-1/2 transform -translate-y-1/2 w-full h-1 bg-gray-200 -z-10"></div>
          <div class="flex flex-col items-center gap-2 bg-gray-50 px-2">
            <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold transition-colors" :class="step >= 1 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-slate-500'">1</div>
            <span class="text-sm font-medium" :class="step >= 1 ? 'text-primary-600' : 'text-slate-500'">Account</span>
          </div>
          <div class="flex flex-col items-center gap-2 bg-gray-50 px-2">
            <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold transition-colors" :class="step >= 2 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-slate-500'">2</div>
            <span class="text-sm font-medium" :class="step >= 2 ? 'text-primary-600' : 'text-slate-500'">Personal</span>
          </div>
          <div class="flex flex-col items-center gap-2 bg-gray-50 px-2">
            <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold transition-colors" :class="step >= 3 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-slate-500'">3</div>
            <span class="text-sm font-medium" :class="step >= 3 ? 'text-primary-600' : 'text-slate-500'">Confirm</span>
          </div>
        </div>
      </div>

      <!-- Form Content -->
      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12">
        <div x-show="step === 1" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform translate-x-4" x-transition:enter-end="opacity-100 transform translate-x-0">
          <h2 class="text-2xl font-bold text-slate-900 mb-6">Account Information</h2>
          <div class="space-y-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Username</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Email</label>
              <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Password</label>
              <input type="password" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
          </div>
          <div class="mt-8 flex justify-end">
            <button @click="step = 2" class="bg-primary-600 text-white font-bold px-8 py-3 rounded-lg hover:bg-primary-700 transition-colors">Next Step</button>
          </div>
        </div>

        <div x-show="step === 2" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform translate-x-4" x-transition:enter-end="opacity-100 transform translate-x-0" style="display: none;">
          <h2 class="text-2xl font-bold text-slate-900 mb-6">Personal Details</h2>
          <div class="space-y-6">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">First Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Last Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Phone Number</label>
              <input type="tel" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
          </div>
          <div class="mt-8 flex justify-between">
            <button @click="step = 1" class="text-slate-600 font-bold px-8 py-3 rounded-lg hover:bg-gray-50 transition-colors">Back</button>
            <button @click="step = 3" class="bg-primary-600 text-white font-bold px-8 py-3 rounded-lg hover:bg-primary-700 transition-colors">Next Step</button>
          </div>
        </div>

        <div x-show="step === 3" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 transform translate-x-4" x-transition:enter-end="opacity-100 transform translate-x-0" style="display: none;">
          <h2 class="text-2xl font-bold text-slate-900 mb-6">Confirmation</h2>
          <div class="bg-primary-50 rounded-xl p-6 mb-8">
            <p class="text-primary-800">Please review your information before submitting.</p>
          </div>
          <div class="space-y-4 text-slate-600">
            <p>By clicking submit, you agree to our Terms of Service and Privacy Policy.</p>
          </div>
          <div class="mt-8 flex justify-between">
            <button @click="step = 2" class="text-slate-600 font-bold px-8 py-3 rounded-lg hover:bg-gray-50 transition-colors">Back</button>
            <button class="bg-primary-600 text-white font-bold px-8 py-3 rounded-lg hover:bg-primary-700 transition-colors">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "form-009",
        "title": "Feedback Form",
        "description": "Rating and comments",
        "dir": "templates/10-forms",
        "content": """<div class="bg-white py-24" x-data="{ rating: 0 }">
    <div class="max-w-xl mx-auto px-6">
      <div class="text-center mb-10">
        <h2 class="text-3xl font-bold text-slate-900">How was your experience?</h2>
        <p class="text-slate-600 mt-2">Your feedback helps us improve.</p>
      </div>

      <div class="bg-gray-50 rounded-2xl p-8 md:p-12">
        <div class="flex justify-center gap-2 mb-8">
          <template x-for="i in 5">
            <button @click="rating = i" class="text-3xl transition-transform hover:scale-110 focus:outline-none" :class="rating >= i ? 'text-yellow-400' : 'text-gray-300'">
              ★
            </button>
          </template>
        </div>

        <form class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">What did you like most?</label>
            <div class="flex gap-4 flex-wrap">
              <label class="cursor-pointer">
                <input type="checkbox" class="peer sr-only">
                <span class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-600 peer-checked:bg-primary-600 peer-checked:text-white peer-checked:border-primary-600 transition-all text-sm font-medium">Design</span>
              </label>
              <label class="cursor-pointer">
                <input type="checkbox" class="peer sr-only">
                <span class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-600 peer-checked:bg-primary-600 peer-checked:text-white peer-checked:border-primary-600 transition-all text-sm font-medium">Features</span>
              </label>
              <label class="cursor-pointer">
                <input type="checkbox" class="peer sr-only">
                <span class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-600 peer-checked:bg-primary-600 peer-checked:text-white peer-checked:border-primary-600 transition-all text-sm font-medium">Ease of use</span>
              </label>
              <label class="cursor-pointer">
                <input type="checkbox" class="peer sr-only">
                <span class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-600 peer-checked:bg-primary-600 peer-checked:text-white peer-checked:border-primary-600 transition-all text-sm font-medium">Support</span>
              </label>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Additional Comments</label>
            <textarea rows="4" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all bg-white" placeholder="Tell us more..."></textarea>
          </div>

          <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-lg hover:bg-slate-800 transition-colors">Submit Feedback</button>
        </form>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "form-010",
        "title": "Support Ticket",
        "description": "File upload support",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <h2 class="text-2xl font-bold text-slate-900 mb-8">Submit a Ticket</h2>

        <form class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Name</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Email</label>
              <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Department</label>
            <select class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all bg-white">
              <option>Technical Support</option>
              <option>Billing</option>
              <option>Sales</option>
              <option>General Inquiry</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Priority</label>
            <div class="flex gap-4">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="priority" class="w-4 h-4 text-primary-600 focus:ring-primary-500">
                <span class="text-slate-600">Low</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="priority" class="w-4 h-4 text-primary-600 focus:ring-primary-500" checked>
                <span class="text-slate-600">Medium</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="priority" class="w-4 h-4 text-primary-600 focus:ring-primary-500">
                <span class="text-slate-600">High</span>
              </label>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Description</label>
            <textarea rows="5" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Attachments</label>
            <div class="border-2 border-dashed border-slate-200 rounded-lg p-8 text-center hover:border-primary-500 transition-colors cursor-pointer">
              <svg class="w-8 h-8 text-slate-400 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
              <p class="text-sm text-slate-600">Click to upload or drag and drop</p>
              <p class="text-xs text-slate-400 mt-1">SVG, PNG, JPG or GIF (max. 800x400px)</p>
            </div>
          </div>

          <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Submit Ticket</button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-011",
        "title": "Reservation Form",
        "description": "Booking form",
        "dir": "templates/10-forms",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="bg-white rounded-2xl overflow-hidden shadow-2xl flex flex-col md:flex-row">
        <div class="md:w-1/3 bg-primary-600 p-8 text-white flex flex-col justify-between">
          <div>
            <h3 class="text-2xl font-bold mb-4">Book a Table</h3>
            <p class="text-primary-100">Reserve your spot for an unforgettable dining experience.</p>
          </div>
          <div class="space-y-4 mt-8">
            <div class="flex items-center gap-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
              <span>+1 (555) 123-4567</span>
            </div>
            <div class="flex items-center gap-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              <span>reservations@example.com</span>
            </div>
          </div>
        </div>
        <div class="md:w-2/3 p-8 md:p-12">
          <form class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-bold text-slate-900 mb-2">Date</label>
                <input type="date" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all">
              </div>
              <div>
                <label class="block text-sm font-bold text-slate-900 mb-2">Time</label>
                <input type="time" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all">
              </div>
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Guests</label>
              <select class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all">
                <option>2 People</option>
                <option>3 People</option>
                <option>4 People</option>
                <option>5+ People</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Special Requests</label>
              <textarea rows="3" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Allergies, seating preference..."></textarea>
            </div>
            <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-lg hover:bg-slate-800 transition-colors">Confirm Reservation</button>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-012",
        "title": "Survey Form",
        "description": "Detailed survey",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-3xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 md:p-12">
        <div class="mb-10">
          <span class="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm font-bold uppercase tracking-wider">Survey</span>
          <h2 class="text-3xl font-bold text-slate-900 mt-4">Product Research</h2>
          <p class="text-slate-600 mt-2">Help us build a better product for you.</p>
        </div>

        <form class="space-y-8">
          <div class="space-y-4">
            <label class="block text-lg font-bold text-slate-900">How often do you use our product?</label>
            <div class="space-y-2">
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="radio" name="frequency" class="w-5 h-5 text-primary-600 focus:ring-primary-500">
                <span class="text-slate-700">Daily</span>
              </label>
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="radio" name="frequency" class="w-5 h-5 text-primary-600 focus:ring-primary-500">
                <span class="text-slate-700">Weekly</span>
              </label>
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="radio" name="frequency" class="w-5 h-5 text-primary-600 focus:ring-primary-500">
                <span class="text-slate-700">Monthly</span>
              </label>
            </div>
          </div>

          <div class="space-y-4">
            <label class="block text-lg font-bold text-slate-900">Which features are most important to you?</label>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="checkbox" class="w-5 h-5 text-primary-600 rounded focus:ring-primary-500">
                <span class="text-slate-700">Analytics</span>
              </label>
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="checkbox" class="w-5 h-5 text-primary-600 rounded focus:ring-primary-500">
                <span class="text-slate-700">Collaboration</span>
              </label>
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="checkbox" class="w-5 h-5 text-primary-600 rounded focus:ring-primary-500">
                <span class="text-slate-700">Mobile App</span>
              </label>
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
                <input type="checkbox" class="w-5 h-5 text-primary-600 rounded focus:ring-primary-500">
                <span class="text-slate-700">Integrations</span>
              </label>
            </div>
          </div>

          <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Submit Survey</button>
        </form>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_FORMS = TEMPLATES_FORMS_1 + TEMPLATES_FORMS_2

# Part 3: Forms 013-020
TEMPLATES_FORMS_3 = [
    {
        "id": "form-013",
        "title": "File Upload",
        "description": "Drag and drop upload",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24" x-data="{ dragging: false }">
    <div class="max-w-xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12 text-center">
        <h2 class="text-2xl font-bold text-slate-900 mb-2">Upload your files</h2>
        <p class="text-slate-600 mb-8">File should be Jpeg, Png or Gif</p>

        <div class="relative border-2 border-dashed rounded-xl p-12 transition-colors"
             :class="dragging ? 'border-primary-500 bg-primary-50' : 'border-slate-200 hover:border-primary-500'"
             @dragover.prevent="dragging = true"
             @dragleave.prevent="dragging = false"
             @drop.prevent="dragging = false">

          <input type="file" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer">

          <div class="pointer-events-none">
            <svg class="w-12 h-12 text-slate-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
            <p class="text-slate-900 font-medium">Drag & Drop your files here</p>
            <p class="text-slate-500 text-sm mt-2">or <span class="text-primary-600 font-bold">Browse Files</span></p>
          </div>
        </div>

        <div class="mt-8 space-y-4">
          <div class="flex items-center gap-4 p-3 bg-gray-50 rounded-lg">
            <div class="w-10 h-10 bg-white rounded-lg flex items-center justify-center shadow-sm text-xs font-bold text-slate-500">JPG</div>
            <div class="flex-1 text-left">
              <div class="text-sm font-medium text-slate-900">profile_photo.jpg</div>
              <div class="text-xs text-slate-500">2.4 MB</div>
            </div>
            <button class="text-slate-400 hover:text-red-500 transition-colors">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>
        </div>

        <div class="flex gap-4 mt-8">
          <button class="flex-1 bg-white text-slate-700 font-bold py-3 rounded-lg border border-slate-200 hover:bg-gray-50 transition-colors">Cancel</button>
          <button class="flex-1 bg-primary-600 text-white font-bold py-3 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Upload Files</button>
        </div>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    },
    {
        "id": "form-014",
        "title": "Settings Form",
        "description": "User preferences",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg overflow-hidden flex flex-col md:flex-row">
        <div class="md:w-64 bg-slate-50 p-6 border-r border-slate-200">
          <nav class="space-y-1">
            <a href="#" class="block px-4 py-2 rounded-lg bg-white text-primary-600 font-medium shadow-sm">General</a>
            <a href="#" class="block px-4 py-2 rounded-lg text-slate-600 hover:bg-white hover:text-slate-900 transition-colors">Password</a>
            <a href="#" class="block px-4 py-2 rounded-lg text-slate-600 hover:bg-white hover:text-slate-900 transition-colors">Notifications</a>
            <a href="#" class="block px-4 py-2 rounded-lg text-slate-600 hover:bg-white hover:text-slate-900 transition-colors">Billing</a>
            <a href="#" class="block px-4 py-2 rounded-lg text-slate-600 hover:bg-white hover:text-slate-900 transition-colors">Team</a>
          </nav>
        </div>

        <div class="flex-1 p-8 md:p-12">
          <h2 class="text-2xl font-bold text-slate-900 mb-8">General Settings</h2>

          <form class="space-y-8">
            <div class="flex items-center gap-6">
              <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-20 h-20 rounded-full object-cover">
              <div>
                <button type="button" class="bg-white text-slate-700 font-bold px-4 py-2 rounded-lg border border-slate-200 hover:bg-gray-50 transition-colors text-sm">Change Photo</button>
                <p class="text-xs text-slate-500 mt-2">JPG, GIF or PNG. Max size of 800K</p>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">First Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" value="Tom">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Last Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" value="Cook">
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
              <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" value="tom@example.com">
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Bio</label>
              <textarea rows="4" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">Product Designer based in Melbourne.</textarea>
            </div>

            <div class="pt-6 border-t border-slate-100 flex justify-end gap-4">
              <button type="button" class="text-slate-600 font-bold px-6 py-3 rounded-lg hover:bg-gray-50 transition-colors">Cancel</button>
              <button class="bg-primary-600 text-white font-bold px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Save Changes</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-015",
        "title": "Profile Edit",
        "description": "Simple profile form",
        "dir": "templates/10-forms",
        "content": """<div class="bg-white py-24">
    <div class="max-w-2xl mx-auto px-6">
      <div class="mb-10">
        <h2 class="text-3xl font-bold text-slate-900">Edit Profile</h2>
        <p class="text-slate-600 mt-2">Update your personal information.</p>
      </div>

      <form class="space-y-8">
        <div class="space-y-6">
          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Username</label>
            <div class="flex rounded-lg shadow-sm">
              <span class="inline-flex items-center px-4 rounded-l-lg border border-r-0 border-slate-200 bg-gray-50 text-slate-500 text-sm">example.com/</span>
              <input type="text" class="flex-1 min-w-0 block w-full px-4 py-3 rounded-none rounded-r-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="username">
            </div>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">About</label>
            <textarea rows="3" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="Brief description for your profile."></textarea>
            <p class="mt-2 text-sm text-slate-500">Brief description for your profile. URLs are hyperlinked.</p>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Photo</label>
            <div class="flex items-center gap-6">
              <span class="h-12 w-12 rounded-full overflow-hidden bg-gray-100">
                <svg class="h-full w-full text-gray-300" fill="currentColor" viewBox="0 0 24 24"><path d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
              </span>
              <button type="button" class="bg-white py-2 px-4 border border-slate-200 rounded-lg shadow-sm text-sm font-medium text-slate-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500">Change</button>
            </div>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Cover Photo</label>
            <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-slate-200 border-dashed rounded-lg hover:border-primary-500 transition-colors cursor-pointer">
              <div class="space-y-1 text-center">
                <svg class="mx-auto h-12 w-12 text-slate-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true"><path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" /></svg>
                <div class="flex text-sm text-slate-600 justify-center">
                  <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-primary-600 hover:text-primary-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-primary-500">
                    <span>Upload a file</span>
                    <input id="file-upload" name="file-upload" type="file" class="sr-only">
                  </label>
                  <p class="pl-1">or drag and drop</p>
                </div>
                <p class="text-xs text-slate-500">PNG, JPG, GIF up to 10MB</p>
              </div>
            </div>
          </div>
        </div>

        <div class="pt-6 border-t border-slate-100 flex justify-end gap-4">
          <button type="button" class="bg-white py-3 px-6 border border-slate-200 rounded-lg shadow-sm text-sm font-bold text-slate-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500">Cancel</button>
          <button type="submit" class="bg-primary-600 py-3 px-6 border border-transparent rounded-lg shadow-sm text-sm font-bold text-white hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500">Save</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-016",
        "title": "Password Reset",
        "description": "Reset password form",
        "dir": "templates/10-forms",
        "content": """<div class="min-h-screen bg-gray-50 flex items-center justify-center py-12 px-6">
    <div class="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 md:p-12">
      <div class="text-center mb-10">
        <div class="w-16 h-16 bg-primary-100 text-primary-600 rounded-xl flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>
        </div>
        <h2 class="text-3xl font-bold text-slate-900">Reset Password</h2>
        <p class="text-slate-600 mt-2">Enter your email to receive reset instructions.</p>
      </div>

      <form class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
          <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="john@example.com">
        </div>

        <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Send Reset Link</button>
      </form>

      <p class="text-center text-slate-600 mt-8 text-sm">
        Remember your password? <a href="#" class="font-bold text-primary-600 hover:text-primary-700">Log in</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "form-017",
        "title": "Two-Factor Auth",
        "description": "2FA verification",
        "dir": "templates/10-forms",
        "content": """<div class="min-h-screen bg-white flex items-center justify-center py-12 px-6">
    <div class="max-w-md w-full text-center">
      <div class="mb-10">
        <div class="w-20 h-20 bg-primary-50 text-primary-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
        </div>
        <h2 class="text-3xl font-bold text-slate-900">Check your phone</h2>
        <p class="text-slate-600 mt-2">We sent a verification code to +1 (555) ***-4567</p>
      </div>

      <form class="space-y-8">
        <div class="flex justify-center gap-4">
          <input type="text" maxlength="1" class="w-14 h-16 text-center text-2xl font-bold rounded-xl border-2 border-slate-200 focus:border-primary-500 focus:ring-0 outline-none transition-all" value="5">
          <input type="text" maxlength="1" class="w-14 h-16 text-center text-2xl font-bold rounded-xl border-2 border-slate-200 focus:border-primary-500 focus:ring-0 outline-none transition-all" value="2">
          <input type="text" maxlength="1" class="w-14 h-16 text-center text-2xl font-bold rounded-xl border-2 border-primary-500 focus:border-primary-500 focus:ring-0 outline-none transition-all shadow-lg shadow-primary-500/20" autofocus>
          <input type="text" maxlength="1" class="w-14 h-16 text-center text-2xl font-bold rounded-xl border-2 border-slate-200 focus:border-primary-500 focus:ring-0 outline-none transition-all">
        </div>

        <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-xl hover:bg-slate-800 transition-colors">Verify Code</button>
      </form>

      <p class="text-center text-slate-600 mt-8 text-sm">
        Didn't receive the code? <a href="#" class="font-bold text-primary-600 hover:text-primary-700">Resend</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "form-018",
        "title": "Invite Team",
        "description": "Team invitation",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <div class="mb-8">
          <h2 class="text-2xl font-bold text-slate-900">Invite Team Members</h2>
          <p class="text-slate-600 mt-2">Invite your colleagues to collaborate on this project.</p>
        </div>

        <div class="space-y-6">
          <div class="flex gap-4">
            <div class="flex-1">
              <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
              <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="colleague@company.com">
            </div>
            <div class="w-32">
              <label class="block text-sm font-medium text-slate-700 mb-2">Role</label>
              <select class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all bg-white">
                <option>Editor</option>
                <option>Viewer</option>
                <option>Admin</option>
              </select>
            </div>
            <div class="flex items-end">
              <button class="bg-primary-600 text-white font-bold px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors h-[50px]">Send</button>
            </div>
          </div>

          <div class="border-t border-slate-100 pt-6">
            <h3 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4">Pending Invites</h3>
            <div class="space-y-4">
              <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center text-slate-500 font-bold border border-slate-200">JD</div>
                  <div>
                    <div class="font-medium text-slate-900">jane.doe@example.com</div>
                    <div class="text-xs text-slate-500">Invited 2 days ago</div>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <span class="text-sm text-slate-600">Editor</span>
                  <button class="text-red-500 hover:text-red-700 text-sm font-medium">Revoke</button>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-primary-50 rounded-lg p-4 flex gap-3">
            <svg class="w-5 h-5 text-primary-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <p class="text-sm text-primary-800">You have 3 seats remaining on your current plan. <a href="#" class="font-bold underline">Upgrade now</a></p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-019",
        "title": "Comment Form",
        "description": "Blog comment section",
        "dir": "templates/10-forms",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6">
      <h3 class="text-2xl font-bold text-slate-900 mb-8">Leave a Comment</h3>

      <form class="mb-12">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Name</label>
            <input type="text" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="John Doe">
          </div>
          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Email</label>
            <input type="email" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="john@example.com">
          </div>
        </div>
        <div class="mb-6">
          <label class="block text-sm font-bold text-slate-900 mb-2">Comment</label>
          <textarea rows="4" class="w-full px-4 py-3 bg-gray-50 border-0 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Join the discussion..."></textarea>
        </div>
        <div class="flex items-center justify-between">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" class="w-4 h-4 text-primary-600 rounded border-gray-300 focus:ring-primary-500">
            <span class="text-sm text-slate-600">Save my name and email</span>
          </label>
          <button class="bg-slate-900 text-white font-bold px-8 py-3 rounded-lg hover:bg-slate-800 transition-colors">Post Comment</button>
        </div>
      </form>

      <div class="space-y-8">
        <h3 class="text-xl font-bold text-slate-900 border-b border-slate-100 pb-4">2 Comments</h3>

        <div class="flex gap-4">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-12 h-12 rounded-full object-cover">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="font-bold text-slate-900">Sarah Jenkins</span>
              <span class="text-sm text-slate-500">• 2 hours ago</span>
            </div>
            <p class="text-slate-600 leading-relaxed">This is exactly what I was looking for! The explanation about the grid system really cleared things up for me. Thanks for sharing.</p>
            <button class="text-sm font-bold text-primary-600 mt-2 hover:text-primary-700">Reply</button>
          </div>
        </div>

        <div class="flex gap-4 ml-16">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-12 h-12 rounded-full object-cover">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="font-bold text-slate-900">Mike Ross</span>
              <span class="text-sm text-slate-500">• 1 hour ago</span>
            </div>
            <p class="text-slate-600 leading-relaxed">Glad you found it helpful Sarah! Let me know if you have any other questions.</p>
            <button class="text-sm font-bold text-primary-600 mt-2 hover:text-primary-700">Reply</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-020",
        "title": "Review Form",
        "description": "Product review",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24" x-data="{ rating: 0, hoverRating: 0 }">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <div class="flex items-start gap-6 mb-8">
          <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80" class="w-24 h-24 object-cover rounded-lg shadow-md">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Premium Wireless Headphones</h2>
            <p class="text-slate-500 text-sm mt-1">Model: WH-1000XM4</p>
          </div>
        </div>

        <form class="space-y-8">
          <div>
            <label class="block text-sm font-bold text-slate-900 mb-4">Overall Rating</label>
            <div class="flex gap-2" @mouseleave="hoverRating = 0">
              <template x-for="i in 5">
                <button type="button"
                        @click="rating = i"
                        @mouseenter="hoverRating = i"
                        class="focus:outline-none transition-transform hover:scale-110">
                  <svg class="w-10 h-10" :class="(hoverRating || rating) >= i ? 'text-yellow-400' : 'text-gray-200'" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </button>
              </template>
            </div>
            <p class="text-sm text-slate-500 mt-2" x-show="rating > 0" x-text="['Terrible', 'Bad', 'Okay', 'Good', 'Excellent'][rating - 1]"></p>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Review Title</label>
            <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="Summarize your experience">
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Review</label>
            <textarea rows="5" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="What did you like or dislike?"></textarea>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-900 mb-2">Add Photos</label>
            <div class="flex gap-4">
              <div class="w-24 h-24 border-2 border-dashed border-slate-200 rounded-lg flex flex-col items-center justify-center text-slate-400 hover:border-primary-500 hover:text-primary-500 transition-colors cursor-pointer">
                <svg class="w-8 h-8 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                <span class="text-xs font-bold">Add</span>
              </div>
            </div>
          </div>

          <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-lg hover:bg-slate-800 transition-colors">Submit Review</button>
        </form>
      </div>
    </div>
    <script src="https://unpkg.com/alpinejs" defer></script>
  </div>"""
    }
]
TEMPLATES_FORMS = TEMPLATES_FORMS_1 + TEMPLATES_FORMS_2 + TEMPLATES_FORMS_3

# Part 4: Forms 021-030
TEMPLATES_FORMS_4 = [
    {
        "id": "form-021",
        "title": "Application Form",
        "description": "General application",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-3xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <div class="mb-10 text-center">
          <h2 class="text-3xl font-bold text-slate-900">Join our Program</h2>
          <p class="text-slate-600 mt-2">Apply now to be part of our exclusive community.</p>
        </div>

        <form class="space-y-8">
          <div class="space-y-4">
            <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">Personal Information</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">First Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Last Name</label>
                <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Email</label>
              <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Phone</label>
              <input type="tel" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
          </div>

          <div class="space-y-4">
            <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">Experience</h3>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Current Role</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Years of Experience</label>
              <select class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all bg-white">
                <option>0-2 years</option>
                <option>3-5 years</option>
                <option>5-10 years</option>
                <option>10+ years</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">LinkedIn Profile</label>
              <input type="url" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="https://linkedin.com/in/username">
            </div>
          </div>

          <div class="space-y-4">
            <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">Why do you want to join?</h3>
            <textarea rows="5" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"></textarea>
          </div>

          <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Submit Application</button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-022",
        "title": "Donation Form",
        "description": "Charity donation",
        "dir": "templates/10-forms",
        "content": """<div class="bg-slate-900 py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="bg-white rounded-2xl overflow-hidden shadow-2xl flex flex-col md:flex-row">
        <div class="md:w-1/2 relative">
          <img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="absolute inset-0 w-full h-full object-cover">
          <div class="absolute inset-0 bg-primary-900/80 flex items-center justify-center p-12 text-center">
            <div>
              <h3 class="text-3xl font-bold text-white mb-4">Make a Difference</h3>
              <p class="text-primary-100 text-lg">Your contribution helps us provide education to children in need.</p>
            </div>
          </div>
        </div>
        <div class="md:w-1/2 p-8 md:p-12">
          <h2 class="text-2xl font-bold text-slate-900 mb-8">Select Amount</h2>

          <form class="space-y-8">
            <div class="grid grid-cols-3 gap-4">
              <label class="cursor-pointer">
                <input type="radio" name="amount" class="peer sr-only">
                <div class="py-4 text-center rounded-xl border-2 border-slate-200 peer-checked:border-primary-600 peer-checked:bg-primary-50 peer-checked:text-primary-700 font-bold transition-all hover:border-primary-300">
                  $10
                </div>
              </label>
              <label class="cursor-pointer">
                <input type="radio" name="amount" class="peer sr-only" checked>
                <div class="py-4 text-center rounded-xl border-2 border-slate-200 peer-checked:border-primary-600 peer-checked:bg-primary-50 peer-checked:text-primary-700 font-bold transition-all hover:border-primary-300">
                  $25
                </div>
              </label>
              <label class="cursor-pointer">
                <input type="radio" name="amount" class="peer sr-only">
                <div class="py-4 text-center rounded-xl border-2 border-slate-200 peer-checked:border-primary-600 peer-checked:bg-primary-50 peer-checked:text-primary-700 font-bold transition-all hover:border-primary-300">
                  $50
                </div>
              </label>
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Custom Amount</label>
              <div class="relative">
                <span class="absolute left-4 top-1/2 transform -translate-y-1/2 text-slate-500 font-bold">$</span>
                <input type="number" class="w-full pl-8 pr-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" placeholder="Enter amount">
              </div>
            </div>

            <div>
              <label class="flex items-center gap-3 p-4 border border-slate-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors">
                <input type="checkbox" class="w-5 h-5 text-primary-600 rounded focus:ring-primary-500">
                <div>
                  <span class="block font-bold text-slate-900">Make this a monthly donation</span>
                  <span class="block text-sm text-slate-500">Cancel anytime</span>
                </div>
              </label>
            </div>

            <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Donate Now</button>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-023",
        "title": "Poll Form",
        "description": "Voting poll",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <span class="text-primary-600 font-bold tracking-wider text-sm uppercase">Community Poll</span>
        <h2 class="text-2xl font-bold text-slate-900 mt-2 mb-8">What feature should we build next?</h2>

        <form class="space-y-4">
          <label class="flex items-center gap-4 p-4 border-2 border-slate-100 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all group">
            <input type="radio" name="poll" class="w-5 h-5 text-primary-600 focus:ring-primary-500">
            <div class="flex-1">
              <span class="block font-bold text-slate-900 group-hover:text-primary-700">Dark Mode</span>
              <span class="block text-sm text-slate-500">Native dark theme support for all pages</span>
            </div>
            <span class="text-sm font-bold text-slate-400">42%</span>
          </label>

          <label class="flex items-center gap-4 p-4 border-2 border-slate-100 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all group">
            <input type="radio" name="poll" class="w-5 h-5 text-primary-600 focus:ring-primary-500">
            <div class="flex-1">
              <span class="block font-bold text-slate-900 group-hover:text-primary-700">Mobile App</span>
              <span class="block text-sm text-slate-500">iOS and Android applications</span>
            </div>
            <span class="text-sm font-bold text-slate-400">35%</span>
          </label>

          <label class="flex items-center gap-4 p-4 border-2 border-slate-100 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all group">
            <input type="radio" name="poll" class="w-5 h-5 text-primary-600 focus:ring-primary-500">
            <div class="flex-1">
              <span class="block font-bold text-slate-900 group-hover:text-primary-700">API Access</span>
              <span class="block text-sm text-slate-500">Public API for developers</span>
            </div>
            <span class="text-sm font-bold text-slate-400">23%</span>
          </label>

          <div class="pt-6 mt-6 border-t border-slate-100">
            <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-lg hover:bg-slate-800 transition-colors">Submit Vote</button>
          </div>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-024",
        "title": "Quiz Form",
        "description": "Multiple choice quiz",
        "dir": "templates/10-forms",
        "content": """<div class="bg-primary-600 py-24 min-h-screen flex items-center">
    <div class="max-w-2xl mx-auto px-6 w-full">
      <div class="bg-white rounded-2xl shadow-2xl overflow-hidden">
        <div class="bg-slate-50 px-8 py-4 border-b border-slate-200 flex justify-between items-center">
          <span class="font-bold text-slate-500">Question 3 of 10</span>
          <div class="flex items-center gap-2">
            <div class="w-32 h-2 bg-slate-200 rounded-full overflow-hidden">
              <div class="w-1/3 h-full bg-primary-500 rounded-full"></div>
            </div>
            <span class="text-sm font-bold text-primary-600">30%</span>
          </div>
        </div>

        <div class="p-8 md:p-12">
          <h2 class="text-2xl font-bold text-slate-900 mb-8">Which CSS property is used to change the text color of an element?</h2>

          <form class="space-y-4">
            <label class="block p-4 border-2 border-slate-200 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
              <div class="flex items-center gap-4">
                <div class="w-8 h-8 rounded-full border-2 border-slate-300 flex items-center justify-center font-bold text-slate-400 peer-checked:bg-primary-500 peer-checked:text-white peer-checked:border-primary-500">A</div>
                <span class="font-medium text-slate-900">text-color</span>
              </div>
              <input type="radio" name="quiz" class="sr-only">
            </label>

            <label class="block p-4 border-2 border-slate-200 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
              <div class="flex items-center gap-4">
                <div class="w-8 h-8 rounded-full border-2 border-slate-300 flex items-center justify-center font-bold text-slate-400">B</div>
                <span class="font-medium text-slate-900">color</span>
              </div>
              <input type="radio" name="quiz" class="sr-only">
            </label>

            <label class="block p-4 border-2 border-slate-200 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
              <div class="flex items-center gap-4">
                <div class="w-8 h-8 rounded-full border-2 border-slate-300 flex items-center justify-center font-bold text-slate-400">C</div>
                <span class="font-medium text-slate-900">font-color</span>
              </div>
              <input type="radio" name="quiz" class="sr-only">
            </label>

            <label class="block p-4 border-2 border-slate-200 rounded-xl cursor-pointer hover:border-primary-500 hover:bg-primary-50 transition-all">
              <div class="flex items-center gap-4">
                <div class="w-8 h-8 rounded-full border-2 border-slate-300 flex items-center justify-center font-bold text-slate-400">D</div>
                <span class="font-medium text-slate-900">fg-color</span>
              </div>
              <input type="radio" name="quiz" class="sr-only">
            </label>

            <div class="pt-8 flex justify-end">
              <button class="bg-primary-600 text-white font-bold px-8 py-3 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Next Question</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-025",
        "title": "RSVP Form",
        "description": "Event registration",
        "dir": "templates/10-forms",
        "content": """<div class="bg-white py-24">
    <div class="max-w-4xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div>
          <span class="text-primary-600 font-bold tracking-widest uppercase text-sm">You're Invited</span>
          <h2 class="text-4xl font-bold text-slate-900 mt-4 mb-6">Annual Tech Conference 2024</h2>
          <p class="text-slate-600 text-lg mb-8">Join us for a day of innovation, networking, and learning from industry leaders.</p>

          <div class="space-y-4 mb-8">
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-primary-50 rounded-full flex items-center justify-center text-primary-600">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              </div>
              <div>
                <div class="font-bold text-slate-900">October 15, 2024</div>
                <div class="text-slate-500">9:00 AM - 5:00 PM</div>
              </div>
            </div>
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-primary-50 rounded-full flex items-center justify-center text-primary-600">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
              </div>
              <div>
                <div class="font-bold text-slate-900">Moscone Center</div>
                <div class="text-slate-500">San Francisco, CA</div>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-gray-50 rounded-2xl p-8 shadow-lg">
          <h3 class="text-xl font-bold text-slate-900 mb-6">RSVP Now</h3>
          <form class="space-y-6">
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Full Name</label>
              <input type="text" class="w-full px-4 py-3 bg-white border border-slate-200 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all">
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Email</label>
              <input type="email" class="w-full px-4 py-3 bg-white border border-slate-200 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all">
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Will you be attending?</label>
              <select class="w-full px-4 py-3 bg-white border border-slate-200 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all">
                <option>Yes, I'll be there</option>
                <option>No, I can't make it</option>
                <option>Maybe</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-900 mb-2">Dietary Requirements</label>
              <input type="text" class="w-full px-4 py-3 bg-white border border-slate-200 rounded-lg focus:ring-2 focus:ring-primary-500 transition-all" placeholder="None">
            </div>
            <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-lg hover:bg-slate-800 transition-colors">Confirm Registration</button>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-026",
        "title": "Subscription Form",
        "description": "Pricing plan selection",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-5xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900">Choose your plan</h2>
        <p class="text-slate-600 mt-4">Simple pricing for everyone.</p>
      </div>

      <form>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Basic Plan -->
          <label class="relative bg-white rounded-2xl shadow-sm border-2 border-transparent hover:border-primary-500 cursor-pointer transition-all p-8 flex flex-col">
            <input type="radio" name="plan" class="absolute top-8 right-8 w-6 h-6 text-primary-600 focus:ring-primary-500">
            <h3 class="text-xl font-bold text-slate-900">Basic</h3>
            <div class="mt-4 mb-6">
              <span class="text-4xl font-bold text-slate-900">$19</span>
              <span class="text-slate-500">/mo</span>
            </div>
            <ul class="space-y-4 mb-8 flex-1">
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                5 Projects
              </li>
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Basic Analytics
              </li>
              <li class="flex items-center gap-3 text-slate-400">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                Team Collaboration
              </li>
            </ul>
          </label>

          <!-- Pro Plan -->
          <label class="relative bg-white rounded-2xl shadow-xl border-2 border-primary-500 cursor-pointer transition-all p-8 flex flex-col transform md:-translate-y-4">
            <div class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-primary-600 text-white px-4 py-1 rounded-full text-sm font-bold">Popular</div>
            <input type="radio" name="plan" class="absolute top-8 right-8 w-6 h-6 text-primary-600 focus:ring-primary-500" checked>
            <h3 class="text-xl font-bold text-slate-900">Pro</h3>
            <div class="mt-4 mb-6">
              <span class="text-4xl font-bold text-slate-900">$49</span>
              <span class="text-slate-500">/mo</span>
            </div>
            <ul class="space-y-4 mb-8 flex-1">
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Unlimited Projects
              </li>
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Advanced Analytics
              </li>
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Team Collaboration
              </li>
            </ul>
          </label>

          <!-- Enterprise Plan -->
          <label class="relative bg-white rounded-2xl shadow-sm border-2 border-transparent hover:border-primary-500 cursor-pointer transition-all p-8 flex flex-col">
            <input type="radio" name="plan" class="absolute top-8 right-8 w-6 h-6 text-primary-600 focus:ring-primary-500">
            <h3 class="text-xl font-bold text-slate-900">Enterprise</h3>
            <div class="mt-4 mb-6">
              <span class="text-4xl font-bold text-slate-900">$99</span>
              <span class="text-slate-500">/mo</span>
            </div>
            <ul class="space-y-4 mb-8 flex-1">
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Everything in Pro
              </li>
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Dedicated Support
              </li>
              <li class="flex items-center gap-3 text-slate-600">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Custom Integrations
              </li>
            </ul>
          </label>
        </div>

        <div class="mt-12 text-center">
          <button class="bg-primary-600 text-white font-bold px-12 py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Continue to Payment</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-027",
        "title": "Waitlist Form",
        "description": "Early access signup",
        "dir": "templates/10-forms",
        "content": """<div class="bg-slate-900 min-h-screen flex items-center justify-center py-24 px-6 relative overflow-hidden">
    <!-- Background Elements -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden z-0">
      <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-primary-600/20 rounded-full blur-[100px]"></div>
      <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-600/20 rounded-full blur-[100px]"></div>
    </div>

    <div class="max-w-xl w-full relative z-10 text-center">
      <span class="inline-block py-1 px-3 rounded-full bg-primary-500/10 text-primary-400 text-sm font-bold mb-6 border border-primary-500/20">Coming Soon</span>
      <h1 class="text-4xl md:text-5xl font-bold text-white mb-6">Get early access</h1>
      <p class="text-slate-400 text-lg mb-10">We're building something special. Be the first to know when we launch and get exclusive perks.</p>

      <form class="bg-white/5 p-2 rounded-2xl border border-white/10 backdrop-blur-sm flex flex-col sm:flex-row gap-2">
        <input type="email" class="flex-1 bg-transparent border-none text-white placeholder-slate-500 px-6 py-4 focus:ring-0" placeholder="Enter your email address">
        <button class="bg-primary-600 text-white font-bold px-8 py-4 rounded-xl hover:bg-primary-500 transition-colors shadow-lg shadow-primary-500/20">Join Waitlist</button>
      </form>

      <div class="mt-8 flex items-center justify-center gap-2 text-sm text-slate-500">
        <div class="flex -space-x-2">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="w-8 h-8 rounded-full border-2 border-slate-900">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="w-8 h-8 rounded-full border-2 border-slate-900">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=100&h=100&q=80" class="w-8 h-8 rounded-full border-2 border-slate-900">
        </div>
        <span>Join 2,000+ others waiting</span>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-028",
        "title": "Bug Report Form",
        "description": "Issue reporting",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <h2 class="text-2xl font-bold text-slate-900 mb-2">Report a Bug</h2>
        <p class="text-slate-600 mb-8">Help us squash bugs by providing as much detail as possible.</p>

        <form class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Issue Title</label>
            <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-red-500 focus:ring-2 focus:ring-red-200 outline-none transition-all" placeholder="e.g. Navigation menu not working on mobile">
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Browser</label>
              <select class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-red-500 focus:ring-2 focus:ring-red-200 outline-none transition-all bg-white">
                <option>Chrome</option>
                <option>Firefox</option>
                <option>Safari</option>
                <option>Edge</option>
                <option>Other</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Operating System</label>
              <select class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-red-500 focus:ring-2 focus:ring-red-200 outline-none transition-all bg-white">
                <option>Windows</option>
                <option>macOS</option>
                <option>iOS</option>
                <option>Android</option>
                <option>Linux</option>
              </select>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Steps to Reproduce</label>
            <textarea rows="4" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-red-500 focus:ring-2 focus:ring-red-200 outline-none transition-all" placeholder="1. Go to homepage&#10;2. Click on..."></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Expected Behavior</label>
            <textarea rows="2" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-red-500 focus:ring-2 focus:ring-red-200 outline-none transition-all"></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Screenshot (Optional)</label>
            <input type="file" class="block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-red-50 file:text-red-700 hover:file:bg-red-100 transition-colors">
          </div>

          <button class="w-full bg-red-600 text-white font-bold py-4 rounded-lg hover:bg-red-700 transition-colors shadow-lg shadow-red-500/30">Submit Report</button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-029",
        "title": "Feature Request",
        "description": "Suggest features",
        "dir": "templates/10-forms",
        "content": """<div class="bg-gray-50 py-24">
    <div class="max-w-2xl mx-auto px-6">
      <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
        <div class="flex items-center gap-4 mb-8">
          <div class="w-12 h-12 bg-yellow-100 text-yellow-600 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
          </div>
          <div>
            <h2 class="text-2xl font-bold text-slate-900">Suggest a Feature</h2>
            <p class="text-slate-600">Have an idea? We'd love to hear it.</p>
          </div>
        </div>

        <form class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Feature Name</label>
            <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 outline-none transition-all">
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Problem it solves</label>
            <textarea rows="3" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 outline-none transition-all" placeholder="Describe the problem you are facing..."></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Proposed Solution</label>
            <textarea rows="3" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 outline-none transition-all" placeholder="How should this feature work?"></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Impact</label>
            <div class="flex gap-4">
              <label class="flex items-center gap-2 cursor-pointer p-3 border border-slate-200 rounded-lg flex-1 hover:bg-gray-50">
                <input type="radio" name="impact" class="w-4 h-4 text-yellow-600 focus:ring-yellow-500">
                <span class="text-slate-700">Nice to have</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer p-3 border border-slate-200 rounded-lg flex-1 hover:bg-gray-50">
                <input type="radio" name="impact" class="w-4 h-4 text-yellow-600 focus:ring-yellow-500">
                <span class="text-slate-700">Important</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer p-3 border border-slate-200 rounded-lg flex-1 hover:bg-gray-50">
                <input type="radio" name="impact" class="w-4 h-4 text-yellow-600 focus:ring-yellow-500">
                <span class="text-slate-700">Critical</span>
              </label>
            </div>
          </div>

          <button class="w-full bg-slate-900 text-white font-bold py-4 rounded-lg hover:bg-slate-800 transition-colors">Submit Idea</button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-030",
        "title": "Job Application",
        "description": "Career page form",
        "dir": "templates/10-forms",
        "content": """<div class="bg-white py-24">
    <div class="max-w-3xl mx-auto px-6">
      <div class="mb-10">
        <h2 class="text-3xl font-bold text-slate-900">Apply for Senior Frontend Developer</h2>
        <p class="text-slate-600 mt-2">Remote • Full-time • Engineering Team</p>
      </div>

      <form class="space-y-8">
        <div class="space-y-4">
          <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">Contact Info</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">First Name <span class="text-red-500">*</span></label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" required>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Last Name <span class="text-red-500">*</span></label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" required>
            </div>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email <span class="text-red-500">*</span></label>
            <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all" required>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Phone</label>
            <input type="tel" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
          </div>
        </div>

        <div class="space-y-4">
          <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">Resume/CV</h3>
          <div class="border-2 border-dashed border-slate-200 rounded-lg p-8 text-center hover:border-primary-500 transition-colors cursor-pointer bg-gray-50">
            <svg class="w-8 h-8 text-slate-400 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            <p class="text-sm text-slate-600 font-medium">Attach Resume/CV</p>
            <p class="text-xs text-slate-500 mt-1">PDF, DOC, DOCX, TXT, RTF</p>
          </div>
        </div>

        <div class="space-y-4">
          <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">Links</h3>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">LinkedIn URL</label>
            <input type="url" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Portfolio URL</label>
            <input type="url" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all">
          </div>
        </div>

        <div class="pt-4">
          <button class="w-full bg-primary-600 text-white font-bold py-4 rounded-lg hover:bg-primary-700 transition-colors shadow-lg shadow-primary-500/30">Submit Application</button>
        </div>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_FORMS_5 = [
    {
        "id": "form-031",
        "title": "Multi-step Wizard - Account Info",
        "description": "Step 1 of a multi-step wizard: Account Information.",
        "dir": "forms/form-031",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-2xl shadow-xl overflow-hidden">
      <div class="bg-indigo-600 px-8 py-6">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-white">Create Account</h2>
          <span class="text-indigo-200 text-sm">Step 1 of 3</span>
        </div>
        <div class="w-full bg-indigo-900/50 h-2 rounded-full overflow-hidden">
          <div class="w-1/3 h-full bg-white rounded-full"></div>
        </div>
      </div>

      <form class="p-8 space-y-6">
        <div class="space-y-4">
          <h3 class="text-lg font-semibold text-slate-800">Account Credentials</h3>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
            <div class="relative">
              <span class="absolute left-4 top-3.5 text-slate-400">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                </svg>
              </span>
              <input type="email" class="w-full pl-12 pr-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all" placeholder="you@example.com">
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Password</label>
              <div class="relative">
                <span class="absolute left-4 top-3.5 text-slate-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </span>
                <input type="password" class="w-full pl-12 pr-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all" placeholder="••••••••">
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Confirm Password</label>
              <div class="relative">
                <span class="absolute left-4 top-3.5 text-slate-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </span>
                <input type="password" class="w-full pl-12 pr-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all" placeholder="••••••••">
              </div>
            </div>
          </div>
        </div>

        <div class="pt-6 flex justify-end">
          <button type="button" class="px-8 py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-colors flex items-center gap-2">
            Next Step
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-032",
        "title": "Multi-step Wizard - Personal Details",
        "description": "Step 2 of a multi-step wizard: Personal Details.",
        "dir": "forms/form-032",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-2xl shadow-xl overflow-hidden">
      <div class="bg-indigo-600 px-8 py-6">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-white">Personal Details</h2>
          <span class="text-indigo-200 text-sm">Step 2 of 3</span>
        </div>
        <div class="w-full bg-indigo-900/50 h-2 rounded-full overflow-hidden">
          <div class="w-2/3 h-full bg-white rounded-full"></div>
        </div>
      </div>

      <form class="p-8 space-y-6">
        <div class="space-y-4">
          <h3 class="text-lg font-semibold text-slate-800">Your Information</h3>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">First Name</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Last Name</label>
              <input type="text" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all">
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Phone Number</label>
            <input type="tel" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all">
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Date of Birth</label>
            <input type="date" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all">
          </div>
        </div>

        <div class="pt-6 flex justify-between">
          <button type="button" class="px-8 py-3 text-slate-600 font-semibold hover:text-slate-900 transition-colors">
            Back
          </button>
          <button type="button" class="px-8 py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-colors flex items-center gap-2">
            Next Step
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-033",
        "title": "Multi-step Wizard - Confirmation",
        "description": "Step 3 of a multi-step wizard: Review and Confirm.",
        "dir": "forms/form-033",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-2xl shadow-xl overflow-hidden">
      <div class="bg-indigo-600 px-8 py-6">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-white">Confirmation</h2>
          <span class="text-indigo-200 text-sm">Step 3 of 3</span>
        </div>
        <div class="w-full bg-indigo-900/50 h-2 rounded-full overflow-hidden">
          <div class="w-full h-full bg-white rounded-full"></div>
        </div>
      </div>

      <div class="p-8">
        <div class="text-center mb-8">
          <div class="w-16 h-16 bg-green-100 text-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-slate-800">All set!</h3>
          <p class="text-slate-600 mt-2">Please review your information before submitting.</p>
        </div>

        <div class="bg-slate-50 rounded-xl p-6 space-y-4 mb-8">
          <div class="flex justify-between border-b border-slate-200 pb-4">
            <span class="text-slate-500">Email</span>
            <span class="font-medium text-slate-900">john.doe@example.com</span>
          </div>
          <div class="flex justify-between border-b border-slate-200 pb-4">
            <span class="text-slate-500">Name</span>
            <span class="font-medium text-slate-900">John Doe</span>
          </div>
          <div class="flex justify-between border-b border-slate-200 pb-4">
            <span class="text-slate-500">Phone</span>
            <span class="font-medium text-slate-900">+1 (555) 000-0000</span>
          </div>
          <div class="flex items-center gap-2 text-sm text-slate-500">
            <input type="checkbox" class="rounded border-slate-300 text-indigo-600 focus:ring-indigo-500" checked>
            I agree to the Terms of Service and Privacy Policy
          </div>
        </div>

        <div class="flex justify-between">
          <button type="button" class="px-8 py-3 text-slate-600 font-semibold hover:text-slate-900 transition-colors">
            Back
          </button>
          <button type="button" class="px-8 py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-colors shadow-lg shadow-indigo-500/30">
            Complete Registration
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-034",
        "title": "NPS Survey",
        "description": "Net Promoter Score survey form.",
        "dir": "forms/form-034",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-xl w-full bg-white rounded-2xl shadow-lg p-8">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-gray-900 mb-2">How likely are you to recommend us?</h2>
        <p class="text-gray-600">Select a score from 0 (Not Likely) to 10 (Very Likely)</p>
      </div>

      <form class="space-y-8">
        <div class="flex justify-between gap-1 overflow-x-auto pb-4">
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="0" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-red-500 peer-checked:bg-red-50 peer-checked:text-red-600 group-hover:border-red-200 transition-all">0</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="1" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-red-500 peer-checked:bg-red-50 peer-checked:text-red-600 group-hover:border-red-200 transition-all">1</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="2" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-red-500 peer-checked:bg-red-50 peer-checked:text-red-600 group-hover:border-red-200 transition-all">2</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="3" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-orange-500 peer-checked:bg-orange-50 peer-checked:text-orange-600 group-hover:border-orange-200 transition-all">3</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="4" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-orange-500 peer-checked:bg-orange-50 peer-checked:text-orange-600 group-hover:border-orange-200 transition-all">4</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="5" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-orange-500 peer-checked:bg-orange-50 peer-checked:text-orange-600 group-hover:border-orange-200 transition-all">5</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="6" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-yellow-500 peer-checked:bg-yellow-50 peer-checked:text-yellow-600 group-hover:border-yellow-200 transition-all">6</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="7" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-yellow-500 peer-checked:bg-yellow-50 peer-checked:text-yellow-600 group-hover:border-yellow-200 transition-all">7</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="8" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-green-500 peer-checked:bg-green-50 peer-checked:text-green-600 group-hover:border-green-200 transition-all">8</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="9" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-green-500 peer-checked:bg-green-50 peer-checked:text-green-600 group-hover:border-green-200 transition-all">9</div>
          </label>
          <label class="cursor-pointer group">
            <input type="radio" name="nps" value="10" class="peer sr-only">
            <div class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-500 peer-checked:border-green-500 peer-checked:bg-green-50 peer-checked:text-green-600 group-hover:border-green-200 transition-all">10</div>
          </label>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">What is the main reason for your score?</label>
          <textarea rows="4" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all resize-none" placeholder="Tell us about your experience..."></textarea>
        </div>

        <button class="w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition-colors">
          Submit Feedback
        </button>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-035",
        "title": "Product Feedback",
        "description": "Detailed product feedback form with categories.",
        "dir": "forms/form-035",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-xl w-full bg-white rounded-2xl shadow-lg overflow-hidden">
      <div class="bg-slate-900 p-6 text-white">
        <h2 class="text-xl font-bold">Product Feedback</h2>
        <p class="text-slate-400 text-sm mt-1">Help us improve our product</p>
      </div>

      <form class="p-6 space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-3">Which feature are you providing feedback for?</label>
          <select class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-slate-500 focus:ring-2 focus:ring-slate-200 outline-none transition-all bg-white">
            <option>Dashboard</option>
            <option>Analytics</option>
            <option>User Management</option>
            <option>Settings</option>
            <option>Other</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-3">How would you rate your experience?</label>
          <div class="flex gap-4">
            <label class="flex-1 cursor-pointer">
              <input type="radio" name="rating" class="peer sr-only">
              <div class="text-center p-3 rounded-lg border border-slate-200 peer-checked:border-slate-900 peer-checked:bg-slate-900 peer-checked:text-white hover:border-slate-300 transition-all">
                <span class="text-2xl block mb-1">😫</span>
                <span class="text-xs font-medium">Poor</span>
              </div>
            </label>
            <label class="flex-1 cursor-pointer">
              <input type="radio" name="rating" class="peer sr-only">
              <div class="text-center p-3 rounded-lg border border-slate-200 peer-checked:border-slate-900 peer-checked:bg-slate-900 peer-checked:text-white hover:border-slate-300 transition-all">
                <span class="text-2xl block mb-1">😐</span>
                <span class="text-xs font-medium">Okay</span>
              </div>
            </label>
            <label class="flex-1 cursor-pointer">
              <input type="radio" name="rating" class="peer sr-only">
              <div class="text-center p-3 rounded-lg border border-slate-200 peer-checked:border-slate-900 peer-checked:bg-slate-900 peer-checked:text-white hover:border-slate-300 transition-all">
                <span class="text-2xl block mb-1">🤩</span>
                <span class="text-xs font-medium">Great</span>
              </div>
            </label>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Details</label>
          <textarea rows="4" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-slate-500 focus:ring-2 focus:ring-slate-200 outline-none transition-all" placeholder="Please describe your experience in detail..."></textarea>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Can we contact you about this feedback?</label>
          <div class="flex items-center gap-4 mt-2">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="contact" class="text-slate-900 focus:ring-slate-900" checked>
              <span class="text-slate-600">Yes, please</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="contact" class="text-slate-900 focus:ring-slate-900">
              <span class="text-slate-600">No, thanks</span>
            </label>
          </div>
        </div>

        <div class="pt-4">
          <button class="w-full bg-slate-900 text-white font-bold py-3 rounded-lg hover:bg-slate-800 transition-colors">
            Send Feedback
          </button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-036",
        "title": "Event Registration",
        "description": "Conference or event registration form.",
        "dir": "forms/form-036",
        "content": """
  <div class="min-h-screen bg-purple-50 flex items-center justify-center p-4">
    <div class="max-w-3xl w-full bg-white rounded-2xl shadow-xl overflow-hidden flex flex-col md:flex-row">
      <div class="md:w-1/3 bg-purple-600 p-8 text-white flex flex-col justify-between">
        <div>
          <span class="inline-block px-3 py-1 bg-purple-500 rounded-full text-xs font-semibold mb-4">CONF 2024</span>
          <h2 class="text-3xl font-bold mb-2">Design Summit</h2>
          <p class="text-purple-200">Join us for 3 days of inspiration and learning.</p>
        </div>
        <div class="mt-8 md:mt-0">
          <div class="flex items-center gap-3 mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-purple-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            <span>Oct 15-17, 2024</span>
          </div>
          <div class="flex items-center gap-3">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-purple-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>San Francisco, CA</span>
          </div>
        </div>
      </div>

      <div class="md:w-2/3 p-8">
        <h3 class="text-xl font-bold text-gray-900 mb-6">Register Now</h3>
        <form class="space-y-5">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">First Name</label>
              <input type="text" class="w-full px-3 py-2 rounded border border-gray-300 focus:border-purple-500 focus:ring-1 focus:ring-purple-500 outline-none">
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Last Name</label>
              <input type="text" class="w-full px-3 py-2 rounded border border-gray-300 focus:border-purple-500 focus:ring-1 focus:ring-purple-500 outline-none">
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Email Address</label>
            <input type="email" class="w-full px-3 py-2 rounded border border-gray-300 focus:border-purple-500 focus:ring-1 focus:ring-purple-500 outline-none">
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Ticket Type</label>
            <div class="space-y-2 mt-2">
              <label class="flex items-center justify-between p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors">
                <div class="flex items-center gap-3">
                  <input type="radio" name="ticket" class="text-purple-600 focus:ring-purple-500" checked>
                  <div>
                    <span class="block font-medium text-gray-900">General Admission</span>
                    <span class="block text-xs text-gray-500">Access to all talks and expo hall</span>
                  </div>
                </div>
                <span class="font-bold text-gray-900">$299</span>
              </label>
              <label class="flex items-center justify-between p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors">
                <div class="flex items-center gap-3">
                  <input type="radio" name="ticket" class="text-purple-600 focus:ring-purple-500">
                  <div>
                    <span class="block font-medium text-gray-900">VIP Access</span>
                    <span class="block text-xs text-gray-500">Includes workshops and after-party</span>
                  </div>
                </div>
                <span class="font-bold text-gray-900">$599</span>
              </label>
            </div>
          </div>

          <button class="w-full mt-4 bg-purple-600 text-white font-bold py-3 rounded-lg hover:bg-purple-700 transition-colors shadow-lg shadow-purple-500/30">
            Proceed to Payment
          </button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-037",
        "title": "Quick Job Application",
        "description": "Simple job application form with file upload.",
        "dir": "forms/form-037",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-lg w-full bg-white rounded-xl shadow-sm border border-gray-100 p-8">
      <div class="mb-6">
        <h2 class="text-2xl font-bold text-gray-900">Apply for Senior Developer</h2>
        <p class="text-gray-500 mt-1">Remote • Full-time</p>
      </div>

      <form class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
          <input type="text" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition-all">
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input type="email" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition-all">
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Resume / CV</label>
          <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-lg hover:border-blue-400 transition-colors cursor-pointer bg-gray-50">
            <div class="space-y-1 text-center">
              <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <div class="flex text-sm text-gray-600">
                <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-blue-600 hover:text-blue-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-blue-500">
                  <span>Upload a file</span>
                  <input id="file-upload" name="file-upload" type="file" class="sr-only">
                </label>
                <p class="pl-1">or drag and drop</p>
              </div>
              <p class="text-xs text-gray-500">PDF, DOC up to 10MB</p>
            </div>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Cover Letter (Optional)</label>
          <textarea rows="3" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition-all"></textarea>
        </div>

        <div class="pt-2">
          <button class="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition-colors">
            Submit Application
          </button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-038",
        "title": "Comprehensive Job Application",
        "description": "Detailed job application with multiple sections.",
        "dir": "forms/form-038",
        "content": """
  <div class="min-h-screen bg-slate-100 py-12 px-4">
    <div class="max-w-3xl mx-auto">
      <div class="bg-white rounded-xl shadow-sm overflow-hidden">
        <div class="border-b border-slate-200 px-8 py-6">
          <h2 class="text-2xl font-bold text-slate-800">Job Application</h2>
          <p class="text-slate-500 mt-1">Product Designer • Design Team</p>
        </div>

        <form class="divide-y divide-slate-200">
          <div class="px-8 py-6 space-y-6">
            <h3 class="text-lg font-medium text-slate-900">Personal Information</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">First Name</label>
                <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Last Name</label>
                <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-slate-700 mb-1">Email Address</label>
                <input type="email" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-slate-700 mb-1">Portfolio URL</label>
                <div class="flex rounded-md shadow-sm">
                  <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-slate-300 bg-slate-50 text-slate-500 text-sm">http://</span>
                  <input type="text" class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-slate-300 focus:ring-blue-500 focus:border-blue-500">
                </div>
              </div>
            </div>
          </div>

          <div class="px-8 py-6 space-y-6">
            <h3 class="text-lg font-medium text-slate-900">Experience</h3>
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Current Company</label>
                <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              </div>
              <div class="grid grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-slate-700 mb-1">Role</label>
                  <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
                </div>
                <div>
                  <label class="block text-sm font-medium text-slate-700 mb-1">Years of Experience</label>
                  <select class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 bg-white">
                    <option>Less than 1 year</option>
                    <option>1-3 years</option>
                    <option>3-5 years</option>
                    <option>5+ years</option>
                  </select>
                </div>
              </div>
            </div>
          </div>

          <div class="px-8 py-6 space-y-6">
            <h3 class="text-lg font-medium text-slate-900">Additional Questions</h3>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Why do you want to work here?</label>
              <textarea rows="4" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">What is your salary expectation?</label>
              <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
            </div>
          </div>

          <div class="px-8 py-6 bg-slate-50 flex justify-end gap-4">
            <button type="button" class="px-4 py-2 border border-slate-300 shadow-sm text-sm font-medium rounded-md text-slate-700 bg-white hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
              Save Draft
            </button>
            <button type="submit" class="px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
              Submit Application
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-039",
        "title": "Appointment Booking",
        "description": "Medical or professional appointment booking form.",
        "dir": "forms/form-039",
        "content": """
  <div class="min-h-screen bg-teal-50 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full bg-white rounded-2xl shadow-xl overflow-hidden flex flex-col md:flex-row">
      <div class="md:w-1/3 bg-teal-700 p-8 text-white">
        <h2 class="text-2xl font-bold mb-4">Book an Appointment</h2>
        <p class="text-teal-100 mb-8">Schedule a consultation with one of our specialists.</p>

        <div class="space-y-6">
          <div class="flex items-start gap-4">
            <div class="w-10 h-10 rounded-full bg-teal-600 flex items-center justify-center flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h3 class="font-semibold">Flexible Scheduling</h3>
              <p class="text-sm text-teal-200 mt-1">Choose a time that works best for you.</p>
            </div>
          </div>
          <div class="flex items-start gap-4">
            <div class="w-10 h-10 rounded-full bg-teal-600 flex items-center justify-center flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h3 class="font-semibold">Instant Confirmation</h3>
              <p class="text-sm text-teal-200 mt-1">Receive booking details via email immediately.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="md:w-2/3 p-8">
        <form class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Select Service</label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <label class="border rounded-lg p-4 cursor-pointer hover:border-teal-500 hover:bg-teal-50 transition-all">
                <input type="radio" name="service" class="sr-only peer">
                <div class="font-semibold text-gray-900 peer-checked:text-teal-700">General Checkup</div>
                <div class="text-sm text-gray-500 mt-1">30 mins • $50</div>
              </label>
              <label class="border rounded-lg p-4 cursor-pointer hover:border-teal-500 hover:bg-teal-50 transition-all">
                <input type="radio" name="service" class="sr-only peer">
                <div class="font-semibold text-gray-900 peer-checked:text-teal-700">Specialist Consult</div>
                <div class="text-sm text-gray-500 mt-1">60 mins • $120</div>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Date</label>
              <input type="date" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 outline-none transition-all">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Time</label>
              <select class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 outline-none transition-all bg-white">
                <option>09:00 AM</option>
                <option>10:00 AM</option>
                <option>11:00 AM</option>
                <option>02:00 PM</option>
                <option>03:00 PM</option>
              </select>
            </div>
          </div>

          <div class="space-y-4">
            <h3 class="font-medium text-gray-900 border-t pt-4">Your Details</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <input type="text" placeholder="Name" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 outline-none transition-all">
              <input type="tel" placeholder="Phone" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 outline-none transition-all">
            </div>
            <input type="email" placeholder="Email" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 outline-none transition-all">
          </div>

          <button class="w-full bg-teal-600 text-white font-bold py-3.5 rounded-lg hover:bg-teal-700 transition-colors shadow-lg shadow-teal-500/30">
            Confirm Booking
          </button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-040",
        "title": "Restaurant Reservation",
        "description": "Elegant restaurant table reservation form.",
        "dir": "forms/form-040",
        "content": """
  <div class="min-h-screen bg-stone-900 flex items-center justify-center p-4 bg-[url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80')] bg-cover bg-center bg-no-repeat bg-blend-overlay">
    <div class="max-w-md w-full bg-black/80 backdrop-blur-md rounded-none border border-stone-700 p-8 text-stone-100">
      <div class="text-center mb-8">
        <h2 class="text-3xl font-serif text-amber-500 mb-2">LUMIÈRE</h2>
        <p class="text-stone-400 text-sm uppercase tracking-widest">Table Reservation</p>
      </div>

      <form class="space-y-6">
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-xs text-stone-500 uppercase tracking-wider mb-2">Date</label>
            <input type="date" class="w-full bg-stone-800 border-stone-700 text-stone-200 px-4 py-3 rounded-sm focus:border-amber-500 focus:ring-1 focus:ring-amber-500 outline-none transition-all">
          </div>
          <div>
            <label class="block text-xs text-stone-500 uppercase tracking-wider mb-2">Time</label>
            <select class="w-full bg-stone-800 border-stone-700 text-stone-200 px-4 py-3 rounded-sm focus:border-amber-500 focus:ring-1 focus:ring-amber-500 outline-none transition-all">
              <option>18:00</option>
              <option>18:30</option>
              <option>19:00</option>
              <option>19:30</option>
              <option>20:00</option>
              <option>20:30</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-xs text-stone-500 uppercase tracking-wider mb-2">Guests</label>
          <div class="flex gap-2">
            <button type="button" class="flex-1 py-2 border border-stone-700 hover:border-amber-500 hover:text-amber-500 transition-colors rounded-sm">2</button>
            <button type="button" class="flex-1 py-2 border border-stone-700 hover:border-amber-500 hover:text-amber-500 transition-colors rounded-sm bg-amber-500/10 border-amber-500 text-amber-500">4</button>
            <button type="button" class="flex-1 py-2 border border-stone-700 hover:border-amber-500 hover:text-amber-500 transition-colors rounded-sm">6</button>
            <button type="button" class="flex-1 py-2 border border-stone-700 hover:border-amber-500 hover:text-amber-500 transition-colors rounded-sm">8+</button>
          </div>
        </div>

        <div class="space-y-4">
          <input type="text" placeholder="Full Name" class="w-full bg-transparent border-b border-stone-700 text-stone-200 px-0 py-3 focus:border-amber-500 outline-none transition-all placeholder-stone-600">
          <input type="tel" placeholder="Phone Number" class="w-full bg-transparent border-b border-stone-700 text-stone-200 px-0 py-3 focus:border-amber-500 outline-none transition-all placeholder-stone-600">
          <textarea placeholder="Special Requests (Allergies, Occasion)" rows="2" class="w-full bg-transparent border-b border-stone-700 text-stone-200 px-0 py-3 focus:border-amber-500 outline-none transition-all placeholder-stone-600 resize-none"></textarea>
        </div>

        <button class="w-full bg-amber-600 text-black font-bold py-4 rounded-sm hover:bg-amber-500 transition-colors uppercase tracking-wider mt-4">
          Reserve Table
        </button>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_FORMS = TEMPLATES_FORMS_1 + TEMPLATES_FORMS_2 + TEMPLATES_FORMS_3 + TEMPLATES_FORMS_4 + TEMPLATES_FORMS_5

TEMPLATES_FORMS_6_PART_1 = [
    {
        "id": "form-041",
        "title": "Real Estate Inquiry",
        "description": "Property inquiry form for real estate listings.",
        "dir": "forms/form-041",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full bg-white rounded-xl shadow-lg overflow-hidden flex flex-col md:flex-row">
      <div class="md:w-1/2 h-64 md:h-auto relative">
        <img src="https://images.unsplash.com/photo-1600596542815-27b88e35eabd?ixlib=rb-4.0.3&auto=format&fit=crop&w=2075&q=80" alt="Modern Home" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end p-8">
          <div class="text-white">
            <h3 class="text-2xl font-bold">Modern Villa</h3>
            <p class="text-slate-200">Beverly Hills, CA</p>
            <p class="text-xl font-bold mt-2">$4,500,000</p>
          </div>
        </div>
      </div>

      <div class="md:w-1/2 p-8">
        <h2 class="text-2xl font-bold text-slate-800 mb-6">Schedule a Tour</h2>
        <form class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <input type="text" placeholder="First Name" class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 focus:bg-white outline-none transition-all">
            <input type="text" placeholder="Last Name" class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 focus:bg-white outline-none transition-all">
          </div>

          <input type="email" placeholder="Email Address" class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 focus:bg-white outline-none transition-all">
          <input type="tel" placeholder="Phone Number" class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 focus:bg-white outline-none transition-all">

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">I am a...</label>
            <div class="flex gap-4">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="type" class="text-blue-600 focus:ring-blue-500" checked>
                <span class="text-slate-600">Buyer</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="type" class="text-blue-600 focus:ring-blue-500">
                <span class="text-slate-600">Agent</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="type" class="text-blue-600 focus:ring-blue-500">
                <span class="text-slate-600">Investor</span>
              </label>
            </div>
          </div>

          <textarea rows="3" placeholder="Message (Optional)" class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 focus:bg-white outline-none transition-all resize-none"></textarea>

          <button class="w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition-colors shadow-lg shadow-blue-500/30">
            Request Info
          </button>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-042",
        "title": "Donation Form",
        "description": "Charity or non-profit donation form.",
        "dir": "forms/form-042",
        "content": """
  <div class="min-h-screen bg-rose-50 flex items-center justify-center p-4">
    <div class="max-w-lg w-full bg-white rounded-2xl shadow-xl overflow-hidden">
      <div class="bg-rose-600 p-8 text-center text-white">
        <h2 class="text-3xl font-bold mb-2">Support Our Cause</h2>
        <p class="text-rose-100">Your contribution makes a difference.</p>
      </div>

      <form class="p-8 space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-3">Select Amount</label>
          <div class="grid grid-cols-3 gap-3">
            <label class="cursor-pointer">
              <input type="radio" name="amount" class="peer sr-only">
              <div class="py-3 text-center rounded-lg border-2 border-rose-100 font-bold text-rose-600 peer-checked:bg-rose-600 peer-checked:text-white peer-checked:border-rose-600 hover:border-rose-300 transition-all">$10</div>
            </label>
            <label class="cursor-pointer">
              <input type="radio" name="amount" class="peer sr-only" checked>
              <div class="py-3 text-center rounded-lg border-2 border-rose-100 font-bold text-rose-600 peer-checked:bg-rose-600 peer-checked:text-white peer-checked:border-rose-600 hover:border-rose-300 transition-all">$25</div>
            </label>
            <label class="cursor-pointer">
              <input type="radio" name="amount" class="peer sr-only">
              <div class="py-3 text-center rounded-lg border-2 border-rose-100 font-bold text-rose-600 peer-checked:bg-rose-600 peer-checked:text-white peer-checked:border-rose-600 hover:border-rose-300 transition-all">$50</div>
            </label>
            <label class="cursor-pointer">
              <input type="radio" name="amount" class="peer sr-only">
              <div class="py-3 text-center rounded-lg border-2 border-rose-100 font-bold text-rose-600 peer-checked:bg-rose-600 peer-checked:text-white peer-checked:border-rose-600 hover:border-rose-300 transition-all">$100</div>
            </label>
            <div class="col-span-2 relative">
              <span class="absolute left-4 top-3.5 text-gray-400">$</span>
              <input type="number" placeholder="Custom Amount" class="w-full pl-8 pr-4 py-3 rounded-lg border-2 border-rose-100 focus:border-rose-600 outline-none transition-all font-bold text-gray-700">
            </div>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-3">Payment Method</label>
          <div class="space-y-3">
            <div class="relative">
              <input type="text" placeholder="Card Number" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-rose-500 focus:ring-2 focus:ring-rose-200 outline-none transition-all">
              <div class="absolute right-4 top-3.5 flex gap-2">
                <div class="w-8 h-5 bg-gray-200 rounded"></div>
                <div class="w-8 h-5 bg-gray-200 rounded"></div>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <input type="text" placeholder="MM / YY" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-rose-500 focus:ring-2 focus:ring-rose-200 outline-none transition-all">
              <input type="text" placeholder="CVC" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-rose-500 focus:ring-2 focus:ring-rose-200 outline-none transition-all">
            </div>
          </div>
        </div>

        <div class="flex items-center gap-3 p-4 bg-rose-50 rounded-lg">
          <input type="checkbox" class="w-5 h-5 text-rose-600 rounded border-gray-300 focus:ring-rose-500">
          <span class="text-sm text-gray-700">Make this a monthly donation</span>
        </div>

        <button class="w-full bg-rose-600 text-white font-bold py-4 rounded-lg hover:bg-rose-700 transition-colors shadow-lg shadow-rose-500/30">
          Donate Now
        </button>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-043",
        "title": "Waitlist Signup",
        "description": "Viral waitlist signup form for upcoming products.",
        "dir": "forms/form-043",
        "content": """
  <div class="min-h-screen bg-black flex items-center justify-center p-4 relative overflow-hidden">
    <!-- Background Effects -->
    <div class="absolute top-0 left-1/4 w-96 h-96 bg-purple-600/30 rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-600/30 rounded-full blur-3xl"></div>

    <div class="max-w-md w-full relative z-10 text-center">
      <div class="mb-8">
        <span class="inline-block px-3 py-1 bg-white/10 backdrop-blur-sm rounded-full text-xs font-medium text-white mb-4 border border-white/20">Coming Soon</span>
        <h1 class="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight">Future of AI</h1>
        <p class="text-gray-400 text-lg">Join the waitlist to get early access to the next generation of artificial intelligence tools.</p>
      </div>

      <form class="relative group">
        <div class="absolute -inset-1 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg blur opacity-25 group-hover:opacity-75 transition duration-1000 group-hover:duration-200"></div>
        <div class="relative flex bg-black rounded-lg p-1 border border-white/10">
          <input type="email" placeholder="Enter your email address" class="flex-1 bg-transparent text-white px-4 py-3 outline-none placeholder-gray-500">
          <button class="bg-white text-black font-bold px-6 py-3 rounded-md hover:bg-gray-100 transition-colors">
            Join Waitlist
          </button>
        </div>
      </form>

      <div class="mt-8 flex items-center justify-center gap-8 text-gray-500">
        <div class="flex -space-x-2">
          <div class="w-8 h-8 rounded-full bg-gray-800 border-2 border-black"></div>
          <div class="w-8 h-8 rounded-full bg-gray-700 border-2 border-black"></div>
          <div class="w-8 h-8 rounded-full bg-gray-600 border-2 border-black"></div>
        </div>
        <p class="text-sm">Join 2,000+ others</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-044",
        "title": "Customer Support Ticket",
        "description": "Support ticket submission form.",
        "dir": "forms/form-044",
        "content": """
  <div class="min-h-screen bg-slate-100 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-lg shadow-sm border border-slate-200 p-8">
      <div class="border-b border-slate-100 pb-6 mb-6">
        <h2 class="text-2xl font-bold text-slate-800">Submit a Ticket</h2>
        <p class="text-slate-500 mt-1">We typically respond within 24 hours.</p>
      </div>

      <form class="space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Name</label>
            <input type="text" class="w-full px-4 py-2.5 rounded-md border border-slate-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email</label>
            <input type="email" class="w-full px-4 py-2.5 rounded-md border border-slate-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all">
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Department</label>
          <select class="w-full px-4 py-2.5 rounded-md border border-slate-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all bg-white">
            <option>Technical Support</option>
            <option>Billing & Payments</option>
            <option>Feature Request</option>
            <option>General Inquiry</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Priority</label>
          <div class="flex gap-4">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="priority" class="text-blue-600 focus:ring-blue-500" checked>
              <span class="px-2 py-1 bg-slate-100 text-slate-600 rounded text-sm font-medium">Low</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="priority" class="text-blue-600 focus:ring-blue-500">
              <span class="px-2 py-1 bg-yellow-100 text-yellow-700 rounded text-sm font-medium">Medium</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="priority" class="text-blue-600 focus:ring-blue-500">
              <span class="px-2 py-1 bg-red-100 text-red-700 rounded text-sm font-medium">High</span>
            </label>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Subject</label>
          <input type="text" class="w-full px-4 py-2.5 rounded-md border border-slate-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all">
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Description</label>
          <textarea rows="5" class="w-full px-4 py-2.5 rounded-md border border-slate-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all font-mono text-sm"></textarea>
          <p class="text-xs text-slate-500 mt-2">Please include any error messages or steps to reproduce the issue.</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Attachments</label>
          <div class="border-2 border-dashed border-slate-300 rounded-lg p-6 text-center hover:border-blue-500 hover:bg-blue-50 transition-colors cursor-pointer">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-slate-400 mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
            <span class="text-sm text-slate-600">Click to upload or drag and drop</span>
          </div>
        </div>

        <div class="pt-4 flex justify-end gap-4">
          <button type="button" class="px-6 py-2.5 text-slate-600 font-medium hover:text-slate-900 transition-colors">Cancel</button>
          <button class="px-6 py-2.5 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700 transition-colors shadow-sm">Submit Ticket</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "form-045",
        "title": "Newsletter Preferences",
        "description": "Email preference center form.",
        "dir": "forms/form-045",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-lg w-full bg-white rounded-xl shadow-lg overflow-hidden">
      <div class="bg-gray-900 p-8 text-white">
        <h2 class="text-2xl font-bold mb-2">Email Preferences</h2>
        <p class="text-gray-400">Manage what emails you receive from us.</p>
      </div>

      <form class="p-8 space-y-8">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
          <input type="email" value="user@example.com" disabled class="w-full px-4 py-2 bg-gray-100 rounded border border-gray-200 text-gray-500">
        </div>

        <div class="space-y-4">
          <h3 class="font-semibold text-gray-900">Content</h3>

          <label class="flex items-start gap-3 p-4 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors">
            <input type="checkbox" class="mt-1 w-4 h-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500" checked>
            <div>
              <span class="block font-medium text-gray-900">Weekly Newsletter</span>
              <span class="block text-sm text-gray-500 mt-1">Curated top stories and insights, sent every Tuesday.</span>
            </div>
          </label>

          <label class="flex items-start gap-3 p-4 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors">
            <input type="checkbox" class="mt-1 w-4 h-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500" checked>
            <div>
              <span class="block font-medium text-gray-900">Product Updates</span>
              <span class="block text-sm text-gray-500 mt-1">New features, improvements, and changelogs.</span>
            </div>
          </label>

          <label class="flex items-start gap-3 p-4 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors">
            <input type="checkbox" class="mt-1 w-4 h-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
            <div>
              <span class="block font-medium text-gray-900">Marketing & Offers</span>
              <span class="block text-sm text-gray-500 mt-1">Special promotions and partner deals.</span>
            </div>
          </label>
        </div>

        <div class="space-y-4">
          <h3 class="font-semibold text-gray-900">Frequency</h3>
          <div class="flex gap-4">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="freq" class="text-blue-600 focus:ring-blue-500" checked>
              <span class="text-gray-700">Daily</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="freq" class="text-blue-600 focus:ring-blue-500">
              <span class="text-gray-700">Weekly</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="radio" name="freq" class="text-blue-600 focus:ring-blue-500">
              <span class="text-gray-700">Monthly</span>
            </label>
          </div>
        </div>

        <div class="pt-4 border-t border-gray-100 flex justify-between items-center">
          <button type="button" class="text-sm text-red-600 hover:text-red-700 font-medium">Unsubscribe from all</button>
          <button class="bg-gray-900 text-white font-bold px-6 py-2.5 rounded-lg hover:bg-gray-800 transition-colors">
            Save Changes
          </button>
        </div>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_FORMS = TEMPLATES_FORMS_1 + TEMPLATES_FORMS_2 + TEMPLATES_FORMS_3 + TEMPLATES_FORMS_4 + TEMPLATES_FORMS_5 + TEMPLATES_FORMS_6_PART_1

TEMPLATES_FORMS_6_PART_2 = [
    {
        "id": "form-046",
        "title": "User Settings",
        "description": "User profile and account settings form.",
        "dir": "forms/form-046",
        "content": """
  <div class="min-h-screen bg-slate-50 p-4 md:p-8">
    <div class="max-w-4xl mx-auto bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <div class="flex flex-col md:flex-row">
        <!-- Sidebar -->
        <div class="w-full md:w-64 bg-slate-50 border-r border-slate-200 p-6">
          <h2 class="text-lg font-bold text-slate-800 mb-6">Settings</h2>
          <nav class="space-y-1">
            <a href="#" class="flex items-center gap-3 px-3 py-2 bg-white text-blue-600 rounded-lg shadow-sm font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
              Profile
            </a>
            <a href="#" class="flex items-center gap-3 px-3 py-2 text-slate-600 hover:bg-slate-100 rounded-lg transition-colors font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg>
              Notifications
            </a>
            <a href="#" class="flex items-center gap-3 px-3 py-2 text-slate-600 hover:bg-slate-100 rounded-lg transition-colors font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              Security
            </a>
          </nav>
        </div>

        <!-- Content -->
        <div class="flex-1 p-6 md:p-8">
          <div class="mb-8">
            <h1 class="text-2xl font-bold text-slate-800">Public Profile</h1>
            <p class="text-slate-500 mt-1">Manage how others see you on the platform.</p>
          </div>

          <form class="space-y-6">
            <div class="flex items-center gap-6">
              <div class="relative">
                <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Profile" class="w-24 h-24 rounded-full object-cover border-4 border-white shadow-md">
                <button type="button" class="absolute bottom-0 right-0 bg-blue-600 text-white p-2 rounded-full shadow-lg hover:bg-blue-700 transition-colors">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </button>
              </div>
              <div>
                <h3 class="font-medium text-slate-900">Profile Picture</h3>
                <p class="text-sm text-slate-500 mt-1">JPG, GIF or PNG. Max size of 800K</p>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Username</label>
                <div class="flex rounded-md shadow-sm">
                  <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-slate-300 bg-slate-50 text-slate-500 sm:text-sm">example.com/</span>
                  <input type="text" class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-slate-300 focus:ring-blue-500 focus:border-blue-500 sm:text-sm" value="johndoe">
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Display Name</label>
                <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" value="John Doe">
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Bio</label>
              <textarea rows="4" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">Product Designer based in San Francisco. I love building clean and accessible user interfaces.</textarea>
              <p class="mt-2 text-sm text-slate-500">Brief description for your profile. URLs are hyperlinked.</p>
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Website</label>
              <input type="url" class="w-full px-3 py-2 border border-slate-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" placeholder="https://">
            </div>

            <div class="pt-6 border-t border-slate-200 flex justify-end gap-4">
              <button type="button" class="px-4 py-2 border border-slate-300 shadow-sm text-sm font-medium rounded-md text-slate-700 bg-white hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                Cancel
              </button>
              <button type="submit" class="px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                Save Changes
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-047",
        "title": "Checkout Form",
        "description": "E-commerce checkout form with order summary.",
        "dir": "forms/form-047",
        "content": """
  <div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <div class="lg:grid lg:grid-cols-2 lg:gap-x-12 xl:gap-x-16">
        <!-- Order Summary -->
        <div class="mt-10 lg:mt-0 lg:col-start-2">
          <h2 class="text-lg font-medium text-gray-900">Order Summary</h2>
          <div class="mt-4 bg-white border border-gray-200 rounded-lg shadow-sm">
            <ul role="list" class="divide-y divide-gray-200">
              <li class="flex py-6 px-4 sm:px-6">
                <div class="flex-shrink-0">
                  <img src="https://images.unsplash.com/photo-1584917865442-de89df76afd3?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Bag" class="w-20 h-20 rounded-md object-cover">
                </div>
                <div class="ml-6 flex-1 flex flex-col">
                  <div class="flex">
                    <div class="min-w-0 flex-1">
                      <h4 class="text-sm font-medium text-gray-700 hover:text-gray-800">Leather Tote Bag</h4>
                      <p class="mt-1 text-sm text-gray-500">Brown</p>
                    </div>
                    <p class="ml-4 text-sm font-medium text-gray-900">$180.00</p>
                  </div>
                </div>
              </li>
              <li class="flex py-6 px-4 sm:px-6">
                <div class="flex-shrink-0">
                  <img src="https://images.unsplash.com/photo-1591561954557-26941169b49e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Shoes" class="w-20 h-20 rounded-md object-cover">
                </div>
                <div class="ml-6 flex-1 flex flex-col">
                  <div class="flex">
                    <div class="min-w-0 flex-1">
                      <h4 class="text-sm font-medium text-gray-700 hover:text-gray-800">Classic Sneakers</h4>
                      <p class="mt-1 text-sm text-gray-500">White / 42</p>
                    </div>
                    <p class="ml-4 text-sm font-medium text-gray-900">$120.00</p>
                  </div>
                </div>
              </li>
            </ul>
            <dl class="border-t border-gray-200 py-6 px-4 sm:px-6 space-y-4">
              <div class="flex items-center justify-between">
                <dt class="text-sm text-gray-600">Subtotal</dt>
                <dd class="text-sm font-medium text-gray-900">$300.00</dd>
              </div>
              <div class="flex items-center justify-between">
                <dt class="text-sm text-gray-600">Shipping</dt>
                <dd class="text-sm font-medium text-gray-900">$15.00</dd>
              </div>
              <div class="flex items-center justify-between border-t border-gray-200 pt-4">
                <dt class="text-base font-medium text-gray-900">Total</dt>
                <dd class="text-base font-medium text-gray-900">$315.00</dd>
              </div>
            </dl>
          </div>
        </div>

        <!-- Checkout Form -->
        <div class="mt-10 lg:mt-0 lg:col-start-1">
          <form>
            <div class="mb-10">
              <h2 class="text-lg font-medium text-gray-900 mb-6">Contact Information</h2>
              <div class="space-y-4">
                <label class="block text-sm font-medium text-gray-700">Email address</label>
                <input type="email" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
              </div>
            </div>

            <div class="mb-10">
              <h2 class="text-lg font-medium text-gray-900 mb-6">Shipping Address</h2>
              <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
                <div class="sm:col-span-2">
                  <label class="block text-sm font-medium text-gray-700 mb-1">Address</label>
                  <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">City</label>
                  <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Country</label>
                  <select class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border bg-white">
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Mexico</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">State / Province</label>
                  <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Postal code</label>
                  <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                </div>
              </div>
            </div>

            <div class="mb-10">
              <h2 class="text-lg font-medium text-gray-900 mb-6">Payment Details</h2>
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Card number</label>
                  <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                </div>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Expiration date (MM/YY)</label>
                    <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">CVC</label>
                    <input type="text" class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm px-4 py-3 border">
                  </div>
                </div>
              </div>
            </div>

            <button type="submit" class="w-full bg-indigo-600 border border-transparent rounded-md shadow-sm py-4 px-4 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Confirm Order
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-048",
        "title": "Survey with Progress",
        "description": "Multi-page survey with progress bar.",
        "dir": "forms/form-048",
        "content": """
  <div class="min-h-screen bg-emerald-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-2xl shadow-xl overflow-hidden">
      <!-- Header -->
      <div class="bg-emerald-800 p-8 text-white">
        <h1 class="text-2xl font-bold mb-2">Employee Satisfaction Survey</h1>
        <p class="text-emerald-200 text-sm">Help us improve our workplace environment.</p>

        <div class="mt-8">
          <div class="flex justify-between text-xs font-medium uppercase tracking-wider mb-2">
            <span>Progress</span>
            <span>40%</span>
          </div>
          <div class="w-full bg-emerald-900/50 h-2 rounded-full overflow-hidden">
            <div class="w-2/5 h-full bg-emerald-400 rounded-full"></div>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="p-8">
        <form class="space-y-8">
          <div class="space-y-4">
            <h3 class="text-lg font-semibold text-gray-900">Work-Life Balance</h3>

            <div class="space-y-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-3">I feel I have a good work-life balance.</label>
                <div class="flex gap-2">
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q1" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Strongly Disagree</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q1" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Disagree</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q1" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Neutral</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q1" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Agree</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q1" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Strongly Agree</div>
                  </label>
                </div>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-3">My workload is manageable.</label>
                <div class="flex gap-2">
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q2" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Strongly Disagree</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q2" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Disagree</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q2" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Neutral</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q2" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Agree</div>
                  </label>
                  <label class="flex-1 cursor-pointer">
                    <input type="radio" name="q2" class="peer sr-only">
                    <div class="py-3 px-2 text-center text-sm border border-gray-200 rounded-lg hover:bg-gray-50 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 transition-all">Strongly Agree</div>
                  </label>
                </div>
              </div>
            </div>
          </div>

          <div class="flex justify-between pt-6 border-t border-gray-100">
            <button type="button" class="px-6 py-2.5 text-gray-600 font-medium hover:text-gray-900 transition-colors">Previous</button>
            <button type="button" class="px-6 py-2.5 bg-emerald-600 text-white font-medium rounded-lg hover:bg-emerald-700 transition-colors shadow-lg shadow-emerald-500/30">Next Section</button>
          </div>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-049",
        "title": "File Upload",
        "description": "Drag and drop file upload area.",
        "dir": "forms/form-049",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-xl w-full bg-white rounded-xl shadow-lg p-8">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-slate-800">Upload Assets</h2>
        <p class="text-slate-500 mt-1">Upload images, videos or documents.</p>
      </div>

      <div class="border-2 border-dashed border-slate-300 rounded-xl p-10 text-center hover:border-blue-500 hover:bg-blue-50/50 transition-all cursor-pointer group">
        <div class="w-16 h-16 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
        </div>
        <h3 class="text-lg font-semibold text-slate-800 mb-1">Click to upload</h3>
        <p class="text-slate-500 mb-4">or drag and drop files here</p>
        <p class="text-xs text-slate-400 uppercase tracking-wide">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
      </div>

      <div class="mt-8 space-y-4">
        <h4 class="text-sm font-semibold text-slate-900">Uploading...</h4>

        <!-- File Item -->
        <div class="bg-slate-50 rounded-lg p-3 flex items-center gap-3">
          <div class="w-10 h-10 bg-white rounded-lg border border-slate-200 flex items-center justify-center text-slate-400">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
          <div class="flex-1 min-w-0">
            <div class="flex justify-between mb-1">
              <span class="text-sm font-medium text-slate-700 truncate">dashboard-mockup.png</span>
              <span class="text-xs text-slate-500">45%</span>
            </div>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div class="w-[45%] h-full bg-blue-500 rounded-full"></div>
            </div>
          </div>
          <button class="text-slate-400 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- File Item -->
        <div class="bg-slate-50 rounded-lg p-3 flex items-center gap-3">
          <div class="w-10 h-10 bg-white rounded-lg border border-slate-200 flex items-center justify-center text-slate-400">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <div class="flex-1 min-w-0">
            <div class="flex justify-between mb-1">
              <span class="text-sm font-medium text-slate-700 truncate">project-proposal.pdf</span>
              <span class="text-xs text-green-600 font-medium">Completed</span>
            </div>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div class="w-full h-full bg-green-500 rounded-full"></div>
            </div>
          </div>
          <button class="text-slate-400 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </button>
        </div>
      </div>

      <div class="mt-8 flex justify-end gap-3">
        <button class="px-4 py-2 text-slate-600 font-medium hover:text-slate-900 transition-colors">Cancel</button>
        <button class="px-6 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors shadow-sm">Upload Files</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "form-050",
        "title": "Reset Password",
        "description": "Password reset request and confirmation form.",
        "dir": "forms/form-050",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg overflow-hidden">
      <div class="p-8">
        <div class="text-center mb-8">
          <div class="w-16 h-16 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-slate-800">Reset Password</h2>
          <p class="text-slate-500 mt-2">Enter your email address and we'll send you a link to reset your password.</p>
        </div>

        <form class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
            <input type="email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all" placeholder="you@example.com">
          </div>

          <button class="w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition-colors shadow-lg shadow-blue-500/30">
            Send Reset Link
          </button>

          <div class="text-center">
            <a href="#" class="text-sm font-medium text-slate-600 hover:text-blue-600 transition-colors flex items-center justify-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
              Back to Login
            </a>
          </div>
        </form>
      </div>

      <div class="bg-slate-50 px-8 py-4 border-t border-slate-100 text-center">
        <p class="text-sm text-slate-500">Don't have an account? <a href="#" class="font-bold text-blue-600 hover:text-blue-700">Sign up</a></p>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_FORMS = TEMPLATES_FORMS_1 + TEMPLATES_FORMS_2 + TEMPLATES_FORMS_3 + TEMPLATES_FORMS_4 + TEMPLATES_FORMS_5 + TEMPLATES_FORMS_6_PART_1 + TEMPLATES_FORMS_6_PART_2
# Placeholder for Cards 001-050
TEMPLATES_CARDS_1 = [
    {
        "id": "card-001",
        "title": "Basic Product Card",
        "description": "Simple product card with image, title, price, and button.",
        "dir": "cards/card-001",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg overflow-hidden max-w-sm w-full">
      <div class="relative h-64">
        <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Nike Shoes" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-gray-900 shadow-sm">
          New Arrival
        </div>
      </div>
      <div class="p-6">
        <div class="flex justify-between items-start mb-4">
          <div>
            <h3 class="text-xl font-bold text-gray-900">Nike Air Max</h3>
            <p class="text-gray-500 text-sm mt-1">Running Collection</p>
          </div>
          <span class="text-xl font-bold text-blue-600">$129</span>
        </div>
        <p class="text-gray-600 text-sm mb-6 line-clamp-2">
          Experience ultimate comfort and style with the new Air Max collection. Designed for performance and everyday wear.
        </p>
        <div class="flex gap-3">
          <button class="flex-1 bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition-colors shadow-lg shadow-blue-500/30">
            Add to Cart
          </button>
          <button class="p-3 border border-gray-200 rounded-lg hover:bg-gray-50 text-gray-500 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-002",
        "title": "User Profile Card",
        "description": "Profile card with stats and social links.",
        "dir": "cards/card-002",
        "content": """
  <div class="min-h-screen bg-slate-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-sm w-full text-center">
      <div class="h-32 bg-gradient-to-r from-purple-500 to-pink-500"></div>
      <div class="px-6 pb-8">
        <div class="relative -mt-16 mb-6">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Profile" class="w-32 h-32 rounded-full border-4 border-white shadow-lg mx-auto object-cover">
          <div class="absolute bottom-2 right-1/2 translate-x-10 bg-green-500 w-5 h-5 rounded-full border-2 border-white"></div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800">Sarah Johnson</h2>
        <p class="text-slate-500 font-medium mb-6">UI/UX Designer @ Google</p>

        <div class="flex justify-center gap-8 mb-8 border-y border-slate-100 py-6">
          <div>
            <span class="block text-2xl font-bold text-slate-800">1.2k</span>
            <span class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Followers</span>
          </div>
          <div>
            <span class="block text-2xl font-bold text-slate-800">843</span>
            <span class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Following</span>
          </div>
          <div>
            <span class="block text-2xl font-bold text-slate-800">124</span>
            <span class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Projects</span>
          </div>
        </div>

        <div class="flex gap-4 justify-center">
          <button class="bg-slate-900 text-white px-8 py-2.5 rounded-full font-bold hover:bg-slate-800 transition-colors shadow-lg shadow-slate-500/30">
            Follow
          </button>
          <button class="bg-white text-slate-900 border border-slate-200 px-8 py-2.5 rounded-full font-bold hover:bg-slate-50 transition-colors">
            Message
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-003",
        "title": "Article Card",
        "description": "Blog post or news article card.",
        "dir": "cards/card-003",
        "content": """
  <div class="min-h-screen bg-stone-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow-md overflow-hidden max-w-md w-full hover:shadow-xl transition-shadow duration-300">
      <div class="relative h-56">
        <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Office" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute top-4 left-4">
          <span class="bg-blue-600 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide">Technology</span>
        </div>
      </div>
      <div class="p-6">
        <div class="flex items-center gap-3 mb-4 text-sm text-stone-500">
          <div class="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            <span>Oct 24, 2023</span>
          </div>
          <span>•</span>
          <div class="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>5 min read</span>
          </div>
        </div>

        <h3 class="text-xl font-bold text-stone-800 mb-3 leading-tight hover:text-blue-600 transition-colors cursor-pointer">
          The Future of Remote Work: Trends to Watch in 2024
        </h3>

        <p class="text-stone-600 mb-6 line-clamp-3">
          As we move into the new year, the landscape of remote work continues to evolve. From hybrid models to digital nomad visas, here's what you need to know about the changing workplace.
        </p>

        <div class="flex items-center justify-between pt-6 border-t border-stone-100">
          <div class="flex items-center gap-3">
            <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Author" class="w-10 h-10 rounded-full object-cover">
            <div>
              <p class="text-sm font-bold text-stone-800">David Miller</p>
              <p class="text-xs text-stone-500">Editor in Chief</p>
            </div>
          </div>
          <button class="text-stone-400 hover:text-blue-600 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-004",
        "title": "Pricing Card",
        "description": "Subscription pricing plan card.",
        "dir": "cards/card-004",
        "content": """
  <div class="min-h-screen bg-indigo-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-sm w-full relative border-2 border-indigo-600 transform hover:-translate-y-1 transition-transform duration-300">
      <div class="absolute top-0 right-0 bg-indigo-600 text-white text-xs font-bold px-3 py-1 rounded-bl-lg uppercase tracking-wider">
        Most Popular
      </div>

      <div class="p-8 text-center">
        <h3 class="text-lg font-bold text-indigo-900 uppercase tracking-widest mb-2">Pro Plan</h3>
        <p class="text-indigo-400 text-sm mb-6">Perfect for growing businesses</p>

        <div class="flex justify-center items-baseline mb-8">
          <span class="text-5xl font-extrabold text-indigo-900">$49</span>
          <span class="text-indigo-500 ml-2">/month</span>
        </div>

        <ul class="space-y-4 text-left mb-8">
          <li class="flex items-center gap-3 text-gray-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            <span>Unlimited Projects</span>
          </li>
          <li class="flex items-center gap-3 text-gray-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            <span>20GB Storage</span>
          </li>
          <li class="flex items-center gap-3 text-gray-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            <span>Priority Support</span>
          </li>
          <li class="flex items-center gap-3 text-gray-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            <span>Advanced Analytics</span>
          </li>
        </ul>

        <button class="w-full bg-indigo-600 text-white font-bold py-4 rounded-xl hover:bg-indigo-700 transition-colors shadow-lg shadow-indigo-500/30">
          Get Started
        </button>
        <p class="text-xs text-gray-400 mt-4">No credit card required</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-005",
        "title": "Music Player Card",
        "description": "Interactive music player interface.",
        "dir": "cards/card-005",
        "content": """
  <div class="min-h-screen bg-zinc-900 flex items-center justify-center p-4">
    <div class="bg-zinc-800 rounded-3xl shadow-2xl p-6 max-w-sm w-full border border-zinc-700">
      <div class="relative aspect-square rounded-2xl overflow-hidden mb-8 shadow-lg">
        <img src="https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Album Art" class="absolute inset-0 w-full h-full object-cover">
      </div>

      <div class="flex justify-between items-center mb-2">
        <div>
          <h3 class="text-xl font-bold text-white">Midnight City</h3>
          <p class="text-zinc-400">M83</p>
        </div>
        <button class="text-zinc-400 hover:text-rose-500 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
          </svg>
        </button>
      </div>

      <div class="mt-6 mb-8">
        <div class="w-full bg-zinc-700 h-1.5 rounded-full mb-2 cursor-pointer group">
          <div class="w-2/3 h-full bg-white rounded-full relative group-hover:bg-rose-500 transition-colors">
            <div class="absolute right-0 top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full opacity-0 group-hover:opacity-100 transition-opacity shadow-md"></div>
          </div>
        </div>
        <div class="flex justify-between text-xs text-zinc-500 font-medium">
          <span>2:45</span>
          <span>4:03</span>
        </div>
      </div>

      <div class="flex justify-between items-center px-4">
        <button class="text-zinc-400 hover:text-white transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
        </button>
        <button class="text-white hover:text-zinc-300 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="currentColor" viewBox="0 0 24 24">
            <path d="M6 6h2v12H6zm3.5 6l8.5 6V6z"/>
          </svg>
        </button>
        <button class="bg-white text-zinc-900 rounded-full p-4 hover:scale-105 transition-transform shadow-lg shadow-white/10">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8 5v14l11-7z"/>
          </svg>
        </button>
        <button class="text-white hover:text-zinc-300 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="currentColor" viewBox="0 0 24 24">
            <path d="M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z"/>
          </svg>
        </button>
        <button class="text-zinc-400 hover:text-white transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
          </svg>
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-006",
        "title": "Recipe Card",
        "description": "Recipe card with ingredients and instructions.",
        "dir": "cards/card-006",
        "content": """
  <div class="min-h-screen bg-orange-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-md w-full">
      <div class="relative h-64">
        <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Pizza" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-6 pt-20">
          <h3 class="text-2xl font-bold text-white mb-2">Homemade Pepperoni Pizza</h3>
          <div class="flex items-center gap-4 text-white/90 text-sm">
            <div class="flex items-center gap-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>45 min</span>
            </div>
            <div class="flex items-center gap-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
              <span>4 Servings</span>
            </div>
            <div class="flex items-center gap-1 text-yellow-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
              <span class="text-white">4.8</span>
            </div>
          </div>
        </div>
      </div>

      <div class="p-6">
        <div class="flex gap-2 mb-6 overflow-x-auto pb-2 scrollbar-hide">
          <span class="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-xs font-bold whitespace-nowrap">Italian</span>
          <span class="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-xs font-bold whitespace-nowrap">Dinner</span>
          <span class="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-xs font-bold whitespace-nowrap">Comfort Food</span>
        </div>

        <div class="space-y-4">
          <h4 class="font-bold text-gray-800 uppercase tracking-wider text-sm">Ingredients</h4>
          <ul class="space-y-2 text-sm text-gray-600">
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-orange-500"></div>
              <span>Pizza dough</span>
            </li>
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-orange-500"></div>
              <span>Tomato sauce</span>
            </li>
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-orange-500"></div>
              <span>Mozzarella cheese</span>
            </li>
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-orange-500"></div>
              <span>Pepperoni slices</span>
            </li>
          </ul>
        </div>

        <button class="w-full mt-8 bg-orange-600 text-white font-bold py-3 rounded-xl hover:bg-orange-700 transition-colors shadow-lg shadow-orange-500/30 flex items-center justify-center gap-2">
          <span>View Recipe</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-007",
        "title": "Task Card",
        "description": "Kanban style task card with tags and assignees.",
        "dir": "cards/card-007",
        "content": """
  <div class="min-h-screen bg-slate-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 max-w-sm w-full hover:shadow-md transition-shadow cursor-pointer">
      <div class="flex justify-between items-start mb-4">
        <span class="px-2 py-1 bg-purple-100 text-purple-700 rounded text-xs font-bold uppercase tracking-wide">Design System</span>
        <button class="text-slate-400 hover:text-slate-600">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
          </svg>
        </button>
      </div>

      <h3 class="text-lg font-bold text-slate-800 mb-2">Update Color Palette</h3>
      <p class="text-slate-500 text-sm mb-6">
        Review and update the primary and secondary color tokens to match the new brand guidelines.
      </p>

      <div class="flex items-center justify-between pt-4 border-t border-slate-100">
        <div class="flex -space-x-2">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User 1" class="w-8 h-8 rounded-full border-2 border-white">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User 2" class="w-8 h-8 rounded-full border-2 border-white">
          <div class="w-8 h-8 rounded-full border-2 border-white bg-slate-100 flex items-center justify-center text-xs font-bold text-slate-500">+2</div>
        </div>

        <div class="flex items-center gap-3 text-slate-400 text-xs font-medium">
          <div class="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
            <span>4</span>
          </div>
          <div class="flex items-center gap-1 text-red-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>2 days left</span>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-008",
        "title": "Notification Card",
        "description": "Notification item card.",
        "dir": "cards/card-008",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-6 max-w-sm w-full flex gap-4">
      <div class="flex-shrink-0">
        <div class="w-12 h-12 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        </div>
      </div>
      <div class="flex-1">
        <div class="flex justify-between items-start">
          <h4 class="text-base font-bold text-gray-900">New Message</h4>
          <span class="text-xs text-gray-400">2m ago</span>
        </div>
        <p class="text-sm text-gray-600 mt-1 mb-3">
          You have received a new message from <span class="font-bold text-gray-800">Sarah Wilson</span> regarding the project timeline.
        </p>
        <div class="flex gap-3">
          <button class="text-sm font-bold text-blue-600 hover:text-blue-700 transition-colors">Reply</button>
          <button class="text-sm font-bold text-gray-500 hover:text-gray-700 transition-colors">Mark as read</button>
        </div>
      </div>
      <button class="text-gray-400 hover:text-gray-600 -mt-2 -mr-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-009",
        "title": "Stats Card",
        "description": "Dashboard statistic card with trend indicator.",
        "dir": "cards/card-009",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 max-w-xs w-full">
      <div class="flex justify-between items-start mb-4">
        <div class="p-2 bg-indigo-50 text-indigo-600 rounded-lg">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <span class="flex items-center text-sm font-bold text-green-600 bg-green-50 px-2 py-1 rounded-full">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M5.293 9.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 7.414V15a1 1 0 11-2 0V7.414L6.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd" />
          </svg>
          12.5%
        </span>
      </div>

      <p class="text-slate-500 text-sm font-medium mb-1">Total Revenue</p>
      <h3 class="text-3xl font-bold text-slate-900">$48,294</h3>
      <p class="text-slate-400 text-xs mt-4">Compared to $42,930 last month</p>
    </div>
  </div>"""
    },
    {
        "id": "card-010",
        "title": "Testimonial Card",
        "description": "Customer testimonial card with quote.",
        "dir": "cards/card-010",
        "content": """
  <div class="min-h-screen bg-teal-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full relative">
      <div class="absolute -top-4 left-8 text-teal-500 bg-white rounded-full p-2 shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="currentColor" viewBox="0 0 24 24">
          <path d="M14.017 21L14.017 18C14.017 16.8954 14.9124 16 16.017 16H19.017C19.5693 16 20.017 15.5523 20.017 15V9C20.017 8.44772 19.5693 8 19.017 8H15.017C14.4647 8 14.017 8.44772 14.017 9V11C14.017 11.5523 13.5693 12 13.017 12H12.017V5H22.017V15C22.017 18.3137 19.3307 21 16.017 21H14.017ZM5.0166 21L5.0166 18C5.0166 16.8954 5.91203 16 7.0166 16H10.0166C10.5689 16 11.0166 15.5523 11.0166 15V9C11.0166 8.44772 10.5689 8 10.0166 8H6.0166C5.46432 8 5.0166 8.44772 5.0166 9V11C5.0166 11.5523 4.56889 12 4.0166 12H3.0166V5H13.0166V15C13.0166 18.3137 10.3303 21 7.0166 21H5.0166Z" />
        </svg>
      </div>

      <p class="text-gray-600 text-lg leading-relaxed mb-6 italic pt-4">
        "This product has completely transformed how we manage our team's workflow. The intuitive interface and powerful features have saved us countless hours every week. Highly recommended!"
      </p>

      <div class="flex items-center gap-4">
        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Testimonial Author" class="w-12 h-12 rounded-full object-cover">
        <div>
          <h4 class="font-bold text-gray-900">Emily Chen</h4>
          <p class="text-sm text-teal-600 font-medium">Product Manager at TechFlow</p>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_CARDS = TEMPLATES_CARDS_1

TEMPLATES_CARDS_2 = [
    {
        "id": "card-011",
        "title": "Event Card",
        "description": "Event details card with date and location.",
        "dir": "cards/card-011",
        "content": """
  <div class="min-h-screen bg-violet-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-sm w-full group">
      <div class="relative h-48 overflow-hidden">
        <img src="https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Concert" class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
        <div class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-2 rounded-lg text-center shadow-sm">
          <span class="block text-xs font-bold text-violet-600 uppercase">Nov</span>
          <span class="block text-xl font-bold text-gray-900 leading-none">24</span>
        </div>
      </div>

      <div class="p-6">
        <span class="text-xs font-bold text-violet-600 uppercase tracking-wider">Music Festival</span>
        <h3 class="text-xl font-bold text-gray-900 mt-1 mb-2 group-hover:text-violet-600 transition-colors">Neon Nights 2023</h3>

        <div class="space-y-2 mb-6">
          <div class="flex items-center gap-2 text-gray-500 text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>8:00 PM - 2:00 AM</span>
          </div>
          <div class="flex items-center gap-2 text-gray-500 text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>Central Park Arena, NY</span>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex -space-x-2">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Attendee" class="w-8 h-8 rounded-full border-2 border-white">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Attendee" class="w-8 h-8 rounded-full border-2 border-white">
            <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Attendee" class="w-8 h-8 rounded-full border-2 border-white">
            <div class="w-8 h-8 rounded-full border-2 border-white bg-gray-100 flex items-center justify-center text-xs font-bold text-gray-500">+120</div>
          </div>
          <button class="bg-violet-600 text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-violet-700 transition-colors shadow-lg shadow-violet-500/30">
            Book Now
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-012",
        "title": "Team Member Card",
        "description": "Team member profile with role and bio.",
        "dir": "cards/card-012",
        "content": """
  <div class="min-h-screen bg-cyan-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-6 max-w-xs w-full text-center hover:-translate-y-1 transition-transform duration-300">
      <div class="relative w-24 h-24 mx-auto mb-4">
        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Team Member" class="w-full h-full rounded-full object-cover border-4 border-cyan-100">
        <div class="absolute bottom-0 right-0 bg-white rounded-full p-1 shadow-sm border border-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-cyan-500" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
          </svg>
        </div>
      </div>

      <h3 class="text-lg font-bold text-gray-900">Michael Foster</h3>
      <p class="text-cyan-600 font-medium text-sm mb-4">Senior Developer</p>

      <p class="text-gray-500 text-sm mb-6 leading-relaxed">
        Passionate about building scalable web applications and mentoring junior developers. Coffee enthusiast.
      </p>

      <div class="flex justify-center gap-4">
        <a href="#" class="text-gray-400 hover:text-cyan-600 transition-colors">
          <span class="sr-only">Twitter</span>
          <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
          </svg>
        </a>
        <a href="#" class="text-gray-400 hover:text-cyan-600 transition-colors">
          <span class="sr-only">GitHub</span>
          <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
            <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
          </svg>
        </a>
        <a href="#" class="text-gray-400 hover:text-cyan-600 transition-colors">
          <span class="sr-only">LinkedIn</span>
          <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
            <path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-013",
        "title": "Feature Card",
        "description": "Feature highlight card with icon.",
        "dir": "cards/card-013",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-8 max-w-sm w-full hover:shadow-lg hover:border-blue-100 transition-all duration-300 group">
      <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-blue-600 group-hover:text-white transition-all duration-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
        </svg>
      </div>

      <h3 class="text-xl font-bold text-gray-900 mb-3">Lightning Fast</h3>
      <p class="text-gray-500 leading-relaxed mb-6">
        Optimized for speed and performance. Our platform ensures your applications run smoothly with minimal latency.
      </p>

      <a href="#" class="inline-flex items-center text-blue-600 font-bold hover:text-blue-700 transition-colors group-hover:translate-x-1 duration-300">
        Learn more
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
  </div>"""
    },
    {
        "id": "card-014",
        "title": "Video Card",
        "description": "Video thumbnail card with play button.",
        "dir": "cards/card-014",
        "content": """
  <div class="min-h-screen bg-zinc-900 flex items-center justify-center p-4">
    <div class="max-w-md w-full group cursor-pointer">
      <div class="relative rounded-xl overflow-hidden mb-3">
        <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Thumbnail" class="w-full aspect-video object-cover group-hover:scale-105 transition-transform duration-300">
        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
        <div class="absolute bottom-2 right-2 bg-black/80 text-white text-xs font-bold px-1.5 py-0.5 rounded">
          12:45
        </div>
        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
          <div class="w-12 h-12 bg-black/60 rounded-full flex items-center justify-center backdrop-blur-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white ml-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
      </div>

      <div class="flex gap-3">
        <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Channel" class="w-9 h-9 rounded-full object-cover">
        <div>
          <h3 class="text-white font-bold leading-tight mb-1 group-hover:text-blue-400 transition-colors line-clamp-2">
            Exploring the Mountains: A Journey Through the Alps
          </h3>
          <div class="text-zinc-400 text-sm">
            <p class="hover:text-white transition-colors">Adventure Time</p>
            <p>125K views • 2 days ago</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-015",
        "title": "Weather Card",
        "description": "Weather forecast card.",
        "dir": "cards/card-015",
        "content": """
  <div class="min-h-screen bg-sky-100 flex items-center justify-center p-4">
    <div class="bg-gradient-to-br from-sky-400 to-blue-500 rounded-3xl shadow-xl p-8 max-w-sm w-full text-white">
      <div class="flex justify-between items-start mb-8">
        <div>
          <h2 class="text-2xl font-bold">San Francisco</h2>
          <p class="text-sky-100">California, USA</p>
        </div>
        <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium backdrop-blur-sm">Today</span>
      </div>

      <div class="flex flex-col items-center mb-8">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-32 w-32 text-yellow-300 mb-4 animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
        <h1 class="text-6xl font-bold mb-2">72°</h1>
        <p class="text-xl font-medium text-sky-100">Sunny</p>
      </div>

      <div class="grid grid-cols-3 gap-4 text-center">
        <div class="bg-white/10 rounded-xl p-3 backdrop-blur-sm">
          <span class="block text-xs text-sky-100 mb-1">Wind</span>
          <span class="font-bold">8 mph</span>
        </div>
        <div class="bg-white/10 rounded-xl p-3 backdrop-blur-sm">
          <span class="block text-xs text-sky-100 mb-1">Humidity</span>
          <span class="font-bold">42%</span>
        </div>
        <div class="bg-white/10 rounded-xl p-3 backdrop-blur-sm">
          <span class="block text-xs text-sky-100 mb-1">Rain</span>
          <span class="font-bold">0%</span>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-016",
        "title": "Course Card",
        "description": "Online course card with progress.",
        "dir": "cards/card-016",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-md overflow-hidden max-w-sm w-full hover:shadow-lg transition-shadow">
      <div class="bg-indigo-600 p-6 text-white relative overflow-hidden">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-white/10 rounded-full blur-xl"></div>
        <div class="absolute bottom-0 left-0 -mb-4 -ml-4 w-24 h-24 bg-black/10 rounded-full blur-xl"></div>

        <span class="inline-block px-2 py-1 bg-white/20 rounded text-xs font-bold mb-3 backdrop-blur-sm">Development</span>
        <h3 class="text-xl font-bold mb-1">Advanced React Patterns</h3>
        <p class="text-indigo-200 text-sm">Master modern React development</p>
      </div>

      <div class="p-6">
        <div class="flex justify-between text-sm text-gray-500 mb-2">
          <span>Progress</span>
          <span class="font-bold text-indigo-600">65%</span>
        </div>
        <div class="w-full bg-gray-100 rounded-full h-2 mb-6">
          <div class="bg-indigo-600 h-2 rounded-full" style="width: 65%"></div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex -space-x-2">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Student" class="w-8 h-8 rounded-full border-2 border-white">
            <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Student" class="w-8 h-8 rounded-full border-2 border-white">
            <div class="w-8 h-8 rounded-full border-2 border-white bg-gray-100 flex items-center justify-center text-xs font-bold text-gray-500">+8</div>
          </div>
          <button class="text-indigo-600 font-bold text-sm hover:text-indigo-700 transition-colors flex items-center gap-1">
            Continue
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-017",
        "title": "Login Card",
        "description": "Simple login card form.",
        "dir": "cards/card-017",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-8 max-w-sm w-full">
      <div class="text-center mb-8">
        <div class="w-12 h-12 bg-blue-600 rounded-lg mx-auto mb-4 flex items-center justify-center text-white font-bold text-xl">
          A
        </div>
        <h2 class="text-2xl font-bold text-slate-800">Welcome Back</h2>
        <p class="text-slate-500 text-sm mt-1">Please enter your details to sign in.</p>
      </div>

      <form class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Email</label>
          <input type="email" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" placeholder="Enter your email">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Password</label>
          <input type="password" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" placeholder="••••••••">
        </div>

        <div class="flex items-center justify-between text-sm">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" class="rounded border-slate-300 text-blue-600 focus:ring-blue-500">
            <span class="text-slate-600">Remember me</span>
          </label>
          <a href="#" class="text-blue-600 font-medium hover:text-blue-700">Forgot password?</a>
        </div>

        <button class="w-full bg-blue-600 text-white font-bold py-2.5 rounded-lg hover:bg-blue-700 transition-colors shadow-lg shadow-blue-500/30">
          Sign In
        </button>
      </form>

      <div class="mt-6 text-center text-sm text-slate-500">
        Don't have an account? <a href="#" class="text-blue-600 font-bold hover:text-blue-700">Sign up</a>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-018",
        "title": "Credit Card",
        "description": "Realistic credit card design.",
        "dir": "cards/card-018",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="w-96 h-56 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl shadow-2xl p-6 text-white relative overflow-hidden transform hover:scale-105 transition-transform duration-300">
      <!-- Background Pattern -->
      <div class="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-white/5 rounded-full blur-3xl"></div>
      <div class="absolute bottom-0 left-0 -ml-16 -mb-16 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl"></div>

      <div class="relative h-full flex flex-col justify-between">
        <div class="flex justify-between items-start">
          <div class="w-12 h-8 bg-gradient-to-r from-yellow-200 to-yellow-400 rounded-md opacity-80"></div>
          <span class="font-bold text-lg italic tracking-wider">VISA</span>
        </div>

        <div class="space-y-6">
          <div class="flex gap-4 items-center">
            <span class="text-2xl font-mono tracking-widest">4532</span>
            <span class="text-2xl font-mono tracking-widest">••••</span>
            <span class="text-2xl font-mono tracking-widest">••••</span>
            <span class="text-2xl font-mono tracking-widest">9018</span>
          </div>

          <div class="flex justify-between items-end">
            <div>
              <span class="block text-xs text-slate-400 uppercase tracking-wider mb-1">Card Holder</span>
              <span class="font-medium tracking-wide uppercase">John Doe</span>
            </div>
            <div>
              <span class="block text-xs text-slate-400 uppercase tracking-wider mb-1">Expires</span>
              <span class="font-medium tracking-wide">12/25</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-019",
        "title": "Download Card",
        "description": "File download card with details.",
        "dir": "cards/card-019",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-6 max-w-sm w-full">
      <div class="flex items-start gap-4">
        <div class="w-12 h-12 bg-red-50 text-red-500 rounded-lg flex items-center justify-center flex-shrink-0">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
          </svg>
        </div>
        <div class="flex-1 min-w-0">
          <h3 class="text-base font-bold text-slate-900 truncate">Project_Proposal_Final.pdf</h3>
          <p class="text-sm text-slate-500 mt-1">2.4 MB • PDF Document</p>
        </div>
        <button class="text-slate-400 hover:text-slate-600">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
          </svg>
        </button>
      </div>

      <div class="mt-6 p-4 bg-slate-50 rounded-lg border border-slate-100">
        <div class="flex justify-between text-xs font-medium text-slate-500 mb-2">
          <span>Downloading...</span>
          <span>45%</span>
        </div>
        <div class="w-full bg-slate-200 rounded-full h-1.5 overflow-hidden">
          <div class="bg-blue-600 h-full rounded-full animate-pulse" style="width: 45%"></div>
        </div>
      </div>

      <div class="flex gap-3 mt-6">
        <button class="flex-1 bg-white border border-slate-200 text-slate-700 font-bold py-2 rounded-lg hover:bg-slate-50 transition-colors">
          Cancel
        </button>
        <button class="flex-1 bg-blue-600 text-white font-bold py-2 rounded-lg hover:bg-blue-700 transition-colors shadow-sm">
          Pause
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-020",
        "title": "Alert Card",
        "description": "Warning or alert message card.",
        "dir": "cards/card-020",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow-lg border-l-4 border-yellow-500 p-6 max-w-md w-full flex gap-4">
      <div class="flex-shrink-0">
        <div class="w-10 h-10 bg-yellow-100 text-yellow-600 rounded-full flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
      </div>
      <div class="flex-1">
        <h3 class="text-lg font-bold text-gray-900">Storage Almost Full</h3>
        <p class="text-gray-600 text-sm mt-1 mb-4">
          You have used 95% of your available storage space. Please upgrade your plan or delete some files to continue uploading.
        </p>
        <div class="flex gap-4">
          <button class="text-sm font-bold text-yellow-600 hover:text-yellow-700 transition-colors">Upgrade Plan</button>
          <button class="text-sm font-bold text-gray-500 hover:text-gray-700 transition-colors">Dismiss</button>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_CARDS = TEMPLATES_CARDS_1 + TEMPLATES_CARDS_2

TEMPLATES_CARDS_3 = [
    {
        "id": "card-021",
        "title": "Job Card",
        "description": "Job listing card with details and apply button.",
        "dir": "cards/card-021",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 max-w-md w-full hover:border-blue-300 transition-colors">
      <div class="flex justify-between items-start mb-4">
        <div class="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold text-xl">
          F
        </div>
        <span class="bg-green-100 text-green-700 text-xs font-bold px-2 py-1 rounded uppercase tracking-wide">Full Time</span>
      </div>

      <h3 class="text-lg font-bold text-slate-900 mb-1">Senior Frontend Engineer</h3>
      <p class="text-slate-500 text-sm font-medium mb-4">Figma • San Francisco, CA (Remote)</p>

      <div class="flex gap-2 mb-6 flex-wrap">
        <span class="px-2 py-1 bg-slate-100 text-slate-600 rounded text-xs font-medium">React</span>
        <span class="px-2 py-1 bg-slate-100 text-slate-600 rounded text-xs font-medium">TypeScript</span>
        <span class="px-2 py-1 bg-slate-100 text-slate-600 rounded text-xs font-medium">Tailwind CSS</span>
      </div>

      <div class="flex items-center justify-between pt-4 border-t border-slate-100">
        <div class="text-slate-900 font-bold">
          $140k - $180k
          <span class="text-slate-400 font-normal text-xs">/ year</span>
        </div>
        <button class="bg-slate-900 text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-slate-800 transition-colors">
          Apply Now
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-022",
        "title": "Review Card",
        "description": "Product review card with rating breakdown.",
        "dir": "cards/card-022",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-8 max-w-sm w-full">
      <div class="flex items-center gap-4 mb-6">
        <div class="text-center">
          <span class="block text-5xl font-bold text-gray-900">4.8</span>
          <div class="flex text-yellow-400 text-sm mt-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
          </div>
          <span class="text-xs text-gray-400 mt-1 block">1,248 reviews</span>
        </div>

        <div class="flex-1 space-y-2">
          <div class="flex items-center gap-2 text-xs text-gray-500">
            <span class="w-3">5</span>
            <div class="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
              <div class="bg-yellow-400 h-full rounded-full" style="width: 85%"></div>
            </div>
          </div>
          <div class="flex items-center gap-2 text-xs text-gray-500">
            <span class="w-3">4</span>
            <div class="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
              <div class="bg-yellow-400 h-full rounded-full" style="width: 10%"></div>
            </div>
          </div>
          <div class="flex items-center gap-2 text-xs text-gray-500">
            <span class="w-3">3</span>
            <div class="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
              <div class="bg-yellow-400 h-full rounded-full" style="width: 3%"></div>
            </div>
          </div>
          <div class="flex items-center gap-2 text-xs text-gray-500">
            <span class="w-3">2</span>
            <div class="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
              <div class="bg-yellow-400 h-full rounded-full" style="width: 1%"></div>
            </div>
          </div>
          <div class="flex items-center gap-2 text-xs text-gray-500">
            <span class="w-3">1</span>
            <div class="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
              <div class="bg-yellow-400 h-full rounded-full" style="width: 1%"></div>
            </div>
          </div>
        </div>
      </div>

      <button class="w-full border border-gray-200 text-gray-700 font-bold py-2.5 rounded-lg hover:bg-gray-50 transition-colors">
        Write a Review
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-023",
        "title": "Blog Card",
        "description": "Minimal blog post card.",
        "dir": "cards/card-023",
        "content": """
  <div class="min-h-screen bg-stone-50 flex items-center justify-center p-4">
    <div class="bg-white p-8 max-w-md w-full border-l-4 border-stone-800 shadow-sm hover:shadow-md transition-shadow cursor-pointer">
      <span class="text-xs font-bold text-stone-400 uppercase tracking-widest mb-2 block">Design Thinking</span>
      <h3 class="text-2xl font-serif font-bold text-stone-900 mb-4 leading-tight">
        Why Minimalism is More Than Just a Visual Style
      </h3>
      <p class="text-stone-600 leading-relaxed mb-6">
        Minimalism isn't just about white space and clean lines. It's a philosophy that prioritizes content and user needs above all else.
      </p>

      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Author" class="w-8 h-8 rounded-full object-cover grayscale">
          <span class="text-sm font-medium text-stone-900">Sarah Jenkins</span>
        </div>
        <span class="text-sm text-stone-400">Oct 12</span>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-024",
        "title": "Product Grid Card",
        "description": "Product card for grid layouts.",
        "dir": "cards/card-024",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg p-4 max-w-xs w-full group cursor-pointer">
      <div class="relative bg-gray-100 rounded-lg overflow-hidden aspect-square mb-4">
        <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Product" class="absolute inset-0 w-full h-full object-cover mix-blend-multiply group-hover:scale-105 transition-transform duration-300">
        <button class="absolute top-2 right-2 p-2 bg-white rounded-full shadow-sm text-gray-400 hover:text-red-500 transition-colors opacity-0 group-hover:opacity-100">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
          </svg>
        </button>
      </div>

      <h3 class="text-gray-900 font-medium mb-1 truncate">Minimalist Watch</h3>
      <p class="text-gray-500 text-sm mb-3">Accessories</p>

      <div class="flex items-center justify-between">
        <span class="text-lg font-bold text-gray-900">$129.00</span>
        <button class="bg-gray-900 text-white p-2 rounded-lg hover:bg-gray-800 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-025",
        "title": "Settings Card",
        "description": "Settings toggle card.",
        "dir": "cards/card-025",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 max-w-sm w-full">
      <h3 class="text-lg font-bold text-slate-900 mb-1">Notifications</h3>
      <p class="text-slate-500 text-sm mb-6">Manage how you receive notifications.</p>

      <div class="space-y-6">
        <div class="flex items-center justify-between">
          <div>
            <h4 class="text-sm font-medium text-slate-900">Email Notifications</h4>
            <p class="text-xs text-slate-500">Receive daily summaries</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer" checked>
            <div class="w-11 h-6 bg-slate-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="flex items-center justify-between">
          <div>
            <h4 class="text-sm font-medium text-slate-900">Push Notifications</h4>
            <p class="text-xs text-slate-500">Receive real-time alerts</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="w-11 h-6 bg-slate-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="flex items-center justify-between">
          <div>
            <h4 class="text-sm font-medium text-slate-900">SMS Notifications</h4>
            <p class="text-xs text-slate-500">Receive critical alerts</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="w-11 h-6 bg-slate-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-026",
        "title": "Chat Card",
        "description": "Chat message card.",
        "dir": "cards/card-026",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-lg p-6 max-w-sm w-full">
      <div class="flex items-center justify-between mb-6 border-b border-gray-100 pb-4">
        <div class="flex items-center gap-3">
          <div class="relative">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-10 h-10 rounded-full object-cover">
            <div class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full"></div>
          </div>
          <div>
            <h3 class="font-bold text-gray-900">Sarah Johnson</h3>
            <p class="text-xs text-green-500 font-medium">Online</p>
          </div>
        </div>
        <button class="text-gray-400 hover:text-gray-600">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
          </svg>
        </button>
      </div>

      <div class="space-y-4 mb-6">
        <div class="flex gap-3">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-8 h-8 rounded-full object-cover mt-1">
          <div class="bg-gray-100 rounded-2xl rounded-tl-none p-3 text-sm text-gray-700">
            Hey! Did you get a chance to look at the new designs?
          </div>
        </div>

        <div class="flex gap-3 flex-row-reverse">
          <div class="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white text-xs font-bold mt-1">
            Me
          </div>
          <div class="bg-blue-600 text-white rounded-2xl rounded-tr-none p-3 text-sm">
            Yes, they look amazing! I really like the new color palette.
          </div>
        </div>

        <div class="flex gap-3">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-8 h-8 rounded-full object-cover mt-1">
          <div class="bg-gray-100 rounded-2xl rounded-tl-none p-3 text-sm text-gray-700">
            Awesome! Let's schedule a call to discuss the next steps.
          </div>
        </div>
      </div>

      <div class="relative">
        <input type="text" placeholder="Type a message..." class="w-full bg-gray-50 border border-gray-200 rounded-full px-4 py-3 pr-12 text-sm focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500">
        <button class="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
            <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
          </svg>
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-027",
        "title": "Timeline Card",
        "description": "Timeline event card.",
        "dir": "cards/card-027",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full">
      <div class="relative pl-8 border-l-2 border-slate-200 space-y-8">
        <!-- Item 1 -->
        <div class="relative">
          <div class="absolute -left-[41px] top-0 w-5 h-5 bg-blue-600 rounded-full border-4 border-white shadow-sm"></div>
          <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <span class="text-xs font-bold text-blue-600 uppercase tracking-wider mb-1 block">Today</span>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Project Kickoff</h3>
            <p class="text-slate-500 text-sm">
              Initial meeting with the stakeholders to discuss project requirements and timeline.
            </p>
          </div>
        </div>

        <!-- Item 2 -->
        <div class="relative">
          <div class="absolute -left-[41px] top-0 w-5 h-5 bg-slate-300 rounded-full border-4 border-white shadow-sm"></div>
          <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 opacity-75">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1 block">Tomorrow</span>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Design Sprint</h3>
            <p class="text-slate-500 text-sm">
              Three-day design sprint to prototype core features and validate assumptions.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-028",
        "title": "Comparison Card",
        "description": "Product comparison card.",
        "dir": "cards/card-028",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg overflow-hidden max-w-sm w-full border border-gray-200">
      <div class="p-6 text-center border-b border-gray-100">
        <h3 class="text-xl font-bold text-gray-900">Standard</h3>
        <p class="text-gray-500 text-sm mt-1">For small teams</p>
        <div class="mt-4">
          <span class="text-4xl font-bold text-gray-900">$29</span>
          <span class="text-gray-400">/mo</span>
        </div>
      </div>

      <div class="p-6 bg-gray-50/50">
        <ul class="space-y-4 text-sm">
          <li class="flex items-center justify-between">
            <span class="text-gray-600">Users</span>
            <span class="font-bold text-gray-900">Up to 5</span>
          </li>
          <li class="flex items-center justify-between">
            <span class="text-gray-600">Storage</span>
            <span class="font-bold text-gray-900">10 GB</span>
          </li>
          <li class="flex items-center justify-between">
            <span class="text-gray-600">Support</span>
            <span class="font-bold text-gray-900">Email</span>
          </li>
          <li class="flex items-center justify-between">
            <span class="text-gray-600">API Access</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-300" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
          </li>
        </ul>

        <button class="w-full mt-8 bg-white border-2 border-gray-900 text-gray-900 font-bold py-2.5 rounded-lg hover:bg-gray-900 hover:text-white transition-colors">
          Choose Plan
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-029",
        "title": "Balance Card",
        "description": "Wallet balance card.",
        "dir": "cards/card-029",
        "content": """
  <div class="min-h-screen bg-slate-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-6 max-w-sm w-full">
      <div class="flex justify-between items-center mb-6">
        <h3 class="text-lg font-bold text-slate-800">My Wallet</h3>
        <button class="p-2 hover:bg-slate-100 rounded-full transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
          </svg>
        </button>
      </div>

      <div class="bg-slate-900 rounded-xl p-6 text-white mb-6 relative overflow-hidden">
        <div class="absolute top-0 right-0 -mt-8 -mr-8 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
        <p class="text-slate-400 text-sm mb-1">Total Balance</p>
        <h2 class="text-3xl font-bold mb-6">$24,562.00</h2>

        <div class="flex gap-3">
          <button class="flex-1 bg-white/10 hover:bg-white/20 transition-colors py-2 rounded-lg text-sm font-medium flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
            Top Up
          </button>
          <button class="flex-1 bg-white/10 hover:bg-white/20 transition-colors py-2 rounded-lg text-sm font-medium flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
            </svg>
            Transfer
          </button>
        </div>
      </div>

      <div>
        <h4 class="text-sm font-bold text-slate-900 mb-4">Recent Transactions</h4>
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
                </svg>
              </div>
              <div>
                <p class="text-sm font-bold text-slate-900">Shopping</p>
                <p class="text-xs text-slate-500">Today, 10:42 AM</p>
              </div>
            </div>
            <span class="text-sm font-bold text-slate-900">-$120.50</span>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-green-100 text-green-600 rounded-full flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <div>
                <p class="text-sm font-bold text-slate-900">Salary</p>
                <p class="text-xs text-slate-500">Yesterday, 09:00 AM</p>
              </div>
            </div>
            <span class="text-sm font-bold text-green-600">+$4,500.00</span>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-030",
        "title": "Calendar Card",
        "description": "Mini calendar widget card.",
        "dir": "cards/card-030",
        "content": """
  <div class="min-h-screen bg-indigo-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-6 max-w-sm w-full">
      <div class="flex justify-between items-center mb-6">
        <h3 class="text-lg font-bold text-gray-900">October 2023</h3>
        <div class="flex gap-2">
          <button class="p-1 hover:bg-gray-100 rounded-full transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
          <button class="p-1 hover:bg-gray-100 rounded-full transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-7 gap-1 text-center mb-2">
        <span class="text-xs font-bold text-gray-400 py-2">Su</span>
        <span class="text-xs font-bold text-gray-400 py-2">Mo</span>
        <span class="text-xs font-bold text-gray-400 py-2">Tu</span>
        <span class="text-xs font-bold text-gray-400 py-2">We</span>
        <span class="text-xs font-bold text-gray-400 py-2">Th</span>
        <span class="text-xs font-bold text-gray-400 py-2">Fr</span>
        <span class="text-xs font-bold text-gray-400 py-2">Sa</span>
      </div>

      <div class="grid grid-cols-7 gap-1 text-center text-sm">
        <span class="py-2 text-gray-300">29</span>
        <span class="py-2 text-gray-300">30</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">1</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">2</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">3</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">4</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">5</span>

        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">6</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">7</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">8</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">9</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">10</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">11</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">12</span>

        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">13</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">14</span>
        <span class="py-2 text-white bg-indigo-600 rounded-lg shadow-md shadow-indigo-500/30 font-bold">15</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">16</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">17</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">18</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">19</span>

        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">20</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">21</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">22</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">23</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">24</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">25</span>
        <span class="py-2 text-gray-700 hover:bg-gray-100 rounded-lg cursor-pointer">26</span>
      </div>

      <div class="mt-6 pt-4 border-t border-gray-100">
        <div class="flex items-center gap-3">
          <div class="w-1 h-10 bg-indigo-600 rounded-full"></div>
          <div>
            <h4 class="text-sm font-bold text-gray-900">Design Review</h4>
            <p class="text-xs text-gray-500">10:00 AM - 11:30 AM</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_CARDS = TEMPLATES_CARDS_1 + TEMPLATES_CARDS_2 + TEMPLATES_CARDS_3

TEMPLATES_CARDS_4 = [
    {
        "id": "card-031",
        "title": "Recipe Card 2",
        "description": "Recipe card with nutrition info.",
        "dir": "cards/card-031",
        "content": """
  <div class="min-h-screen bg-green-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-sm w-full">
      <div class="relative h-56">
        <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Salad" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute top-4 left-4 bg-green-600 text-white text-xs font-bold px-3 py-1 rounded-full shadow-sm">
          Healthy Choice
        </div>
      </div>

      <div class="p-6">
        <div class="flex justify-between items-start mb-2">
          <h3 class="text-xl font-bold text-gray-900">Quinoa Power Bowl</h3>
          <div class="flex items-center gap-1 text-yellow-400 text-sm font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <span class="text-gray-700">4.9</span>
          </div>
        </div>

        <p class="text-gray-500 text-sm mb-6">
          A nutritious blend of quinoa, avocado, kale, and roasted chickpeas topped with tahini dressing.
        </p>

        <div class="grid grid-cols-3 gap-2 mb-6">
          <div class="bg-green-50 p-2 rounded-lg text-center">
            <span class="block text-xs text-green-600 font-bold uppercase">Cal</span>
            <span class="block text-sm font-bold text-gray-900">320</span>
          </div>
          <div class="bg-green-50 p-2 rounded-lg text-center">
            <span class="block text-xs text-green-600 font-bold uppercase">Pro</span>
            <span class="block text-sm font-bold text-gray-900">12g</span>
          </div>
          <div class="bg-green-50 p-2 rounded-lg text-center">
            <span class="block text-xs text-green-600 font-bold uppercase">Fat</span>
            <span class="block text-sm font-bold text-gray-900">14g</span>
          </div>
        </div>

        <button class="w-full bg-green-600 text-white font-bold py-3 rounded-xl hover:bg-green-700 transition-colors shadow-lg shadow-green-500/30">
          View Recipe
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-032",
        "title": "Podcast Card",
        "description": "Podcast episode card.",
        "dir": "cards/card-032",
        "content": """
  <div class="min-h-screen bg-purple-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-6 max-w-md w-full flex items-center gap-6">
      <div class="relative w-24 h-24 flex-shrink-0">
        <img src="https://images.unsplash.com/photo-1478737270239-2f02b77ac6d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Podcast Cover" class="w-full h-full object-cover rounded-xl shadow-md">
        <div class="absolute inset-0 flex items-center justify-center bg-black/20 rounded-xl opacity-0 hover:opacity-100 transition-opacity cursor-pointer">
          <div class="w-8 h-8 bg-white rounded-full flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-purple-600 ml-0.5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
      </div>

      <div class="flex-1 min-w-0">
        <span class="text-xs font-bold text-purple-600 uppercase tracking-wide">Episode 42</span>
        <h3 class="text-lg font-bold text-gray-900 truncate mb-1">The Future of AI</h3>
        <p class="text-sm text-gray-500 truncate mb-3">Tech Talk Daily • 45 min</p>

        <div class="w-full bg-gray-100 rounded-full h-1.5 mb-2">
          <div class="bg-purple-600 h-1.5 rounded-full" style="width: 35%"></div>
        </div>
        <div class="flex justify-between text-xs text-gray-400 font-medium">
          <span>15:24</span>
          <span>45:00</span>
        </div>
      </div>

      <button class="text-gray-400 hover:text-purple-600 transition-colors">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
        </svg>
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-033",
        "title": "Property Card",
        "description": "Real estate property card.",
        "dir": "cards/card-033",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg overflow-hidden max-w-sm w-full group cursor-pointer">
      <div class="relative h-64">
        <img src="https://images.unsplash.com/photo-1600596542815-2251c3052068?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="House" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-lg text-sm font-bold text-gray-900 shadow-sm">
          For Sale
        </div>
        <button class="absolute top-4 right-4 p-2 bg-white/90 backdrop-blur-sm rounded-full text-gray-500 hover:text-red-500 transition-colors shadow-sm">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
          </svg>
        </button>
      </div>

      <div class="p-6">
        <div class="flex justify-between items-start mb-4">
          <div>
            <h3 class="text-2xl font-bold text-gray-900">$850,000</h3>
            <p class="text-gray-500 text-sm">123 Beverly Drive, Los Angeles</p>
          </div>
        </div>

        <div class="flex items-center gap-6 text-sm text-gray-600 border-t border-gray-100 pt-4">
          <div class="flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <span class="font-bold">4</span> Beds
          </div>
          <div class="flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z" />
            </svg>
            <span class="font-bold">3</span> Baths
          </div>
          <div class="flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
            </svg>
            <span class="font-bold">2,400</span> sqft
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-034",
        "title": "Donation Card",
        "description": "Charity donation card.",
        "dir": "cards/card-034",
        "content": """
  <div class="min-h-screen bg-rose-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-8 max-w-sm w-full text-center">
      <div class="w-16 h-16 bg-rose-100 text-rose-500 rounded-full flex items-center justify-center mx-auto mb-6">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
        </svg>
      </div>

      <h3 class="text-2xl font-bold text-gray-900 mb-2">Support Our Cause</h3>
      <p class="text-gray-500 mb-8">
        Your contribution helps us provide education to children in need around the world.
      </p>

      <div class="grid grid-cols-3 gap-3 mb-6">
        <button class="border-2 border-gray-200 rounded-xl py-2 font-bold text-gray-600 hover:border-rose-500 hover:text-rose-500 hover:bg-rose-50 transition-all">
          $10
        </button>
        <button class="border-2 border-rose-500 bg-rose-50 rounded-xl py-2 font-bold text-rose-500 transition-all">
          $25
        </button>
        <button class="border-2 border-gray-200 rounded-xl py-2 font-bold text-gray-600 hover:border-rose-500 hover:text-rose-500 hover:bg-rose-50 transition-all">
          $50
        </button>
      </div>

      <div class="relative mb-8">
        <span class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500 font-bold">$</span>
        <input type="number" placeholder="Custom Amount" class="w-full pl-8 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:border-rose-500 focus:ring-0 outline-none font-bold text-gray-900 placeholder-gray-400 transition-colors">
      </div>

      <button class="w-full bg-rose-600 text-white font-bold py-3.5 rounded-xl hover:bg-rose-700 transition-colors shadow-lg shadow-rose-500/30">
        Donate Now
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-035",
        "title": "Skill Card",
        "description": "Skill proficiency card.",
        "dir": "cards/card-035",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-6 max-w-xs w-full">
      <div class="flex items-center gap-4 mb-6">
        <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
          <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" class="w-8 h-8">
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Python</h3>
          <p class="text-sm text-slate-500">Backend Development</p>
        </div>
      </div>

      <div class="space-y-4">
        <div>
          <div class="flex justify-between text-xs font-bold text-slate-600 mb-1">
            <span>Proficiency</span>
            <span>90%</span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-2">
            <div class="bg-blue-600 h-2 rounded-full" style="width: 90%"></div>
          </div>
        </div>

        <div>
          <div class="flex justify-between text-xs font-bold text-slate-600 mb-1">
            <span>Experience</span>
            <span>5 Years</span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-2">
            <div class="bg-blue-600 h-2 rounded-full" style="width: 75%"></div>
          </div>
        </div>
      </div>

      <div class="mt-6 pt-4 border-t border-slate-100 flex justify-between items-center">
        <div class="flex -space-x-2">
          <div class="w-6 h-6 rounded-full bg-slate-200 border-2 border-white"></div>
          <div class="w-6 h-6 rounded-full bg-slate-300 border-2 border-white"></div>
          <div class="w-6 h-6 rounded-full bg-slate-400 border-2 border-white"></div>
        </div>
        <span class="text-xs font-bold text-blue-600 cursor-pointer hover:underline">View Projects</span>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-036",
        "title": "Flight Card",
        "description": "Flight ticket details card.",
        "dir": "cards/card-036",
        "content": """
  <div class="min-h-screen bg-sky-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-sm w-full">
      <div class="bg-sky-600 p-6 text-white">
        <div class="flex justify-between items-center mb-4">
          <span class="text-sky-200 text-sm font-bold tracking-widest">BOARDING PASS</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>

        <div class="flex justify-between items-center mb-2">
          <div>
            <span class="text-3xl font-bold">NYC</span>
            <p class="text-sky-200 text-xs uppercase">New York</p>
          </div>
          <div class="flex-1 px-4 text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mx-auto mb-1 transform rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
            </svg>
            <div class="h-0.5 bg-sky-400/50 w-full relative">
              <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 bg-white rounded-full"></div>
            </div>
            <p class="text-sky-200 text-xs mt-1">6h 30m</p>
          </div>
          <div class="text-right">
            <span class="text-3xl font-bold">LHR</span>
            <p class="text-sky-200 text-xs uppercase">London</p>
          </div>
        </div>
      </div>

      <div class="p-6 relative">
        <!-- Perforated Line -->
        <div class="absolute top-0 left-0 right-0 -mt-3 flex justify-between px-2">
          <div class="w-6 h-6 bg-sky-50 rounded-full"></div>
          <div class="w-6 h-6 bg-sky-50 rounded-full"></div>
        </div>

        <div class="grid grid-cols-3 gap-6 mb-6 mt-2">
          <div>
            <span class="block text-xs text-gray-400 uppercase tracking-wider mb-1">Flight</span>
            <span class="block font-bold text-gray-900">BA2490</span>
          </div>
          <div>
            <span class="block text-xs text-gray-400 uppercase tracking-wider mb-1">Gate</span>
            <span class="block font-bold text-gray-900">B24</span>
          </div>
          <div>
            <span class="block text-xs text-gray-400 uppercase tracking-wider mb-1">Seat</span>
            <span class="block font-bold text-gray-900">12A</span>
          </div>
          <div>
            <span class="block text-xs text-gray-400 uppercase tracking-wider mb-1">Date</span>
            <span class="block font-bold text-gray-900">Oct 24</span>
          </div>
          <div class="col-span-2">
            <span class="block text-xs text-gray-400 uppercase tracking-wider mb-1">Boarding Time</span>
            <span class="block font-bold text-gray-900">10:45 AM</span>
          </div>
        </div>

        <div class="border-t border-dashed border-gray-200 pt-6 flex justify-between items-center">
          <div class="space-y-1">
            <span class="block text-xs text-gray-400 uppercase tracking-wider">Passenger</span>
            <span class="block font-bold text-gray-900">John Smith</span>
          </div>
          <div class="h-12 w-12 bg-gray-900 rounded flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v1m6 11h2m-6 0h-2v4h2v-4zM6 11H4v4h2v-4zM6 4v5h12V4M6 11v4h2v-4H6zm10 0v4h2v-4h-2z" />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-037",
        "title": "Upload Card",
        "description": "File upload dropzone card.",
        "dir": "cards/card-037",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-8 max-w-md w-full text-center">
      <div class="border-2 border-dashed border-blue-300 rounded-xl p-8 bg-blue-50 hover:bg-blue-100 transition-colors cursor-pointer group">
        <div class="w-16 h-16 bg-blue-100 text-blue-500 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
        </div>
        <h3 class="text-lg font-bold text-blue-900 mb-2">Upload Files</h3>
        <p class="text-blue-600/80 text-sm mb-4">Drag & drop files here or click to browse</p>
        <span class="text-xs text-blue-400">Supported formats: JPG, PNG, PDF (Max 10MB)</span>
      </div>

      <div class="mt-6 space-y-3">
        <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg border border-gray-100">
          <div class="w-10 h-10 bg-red-100 text-red-500 rounded-lg flex items-center justify-center flex-shrink-0">
            <span class="text-xs font-bold">PDF</span>
          </div>
          <div class="flex-1 min-w-0 text-left">
            <p class="text-sm font-bold text-gray-900 truncate">document_v1.pdf</p>
            <p class="text-xs text-gray-500">2.4 MB</p>
          </div>
          <button class="text-gray-400 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>

      <div class="flex gap-3 mt-6">
        <button class="flex-1 py-2.5 text-gray-500 font-bold hover:text-gray-700 transition-colors">Cancel</button>
        <button class="flex-1 bg-blue-600 text-white font-bold py-2.5 rounded-lg hover:bg-blue-700 transition-colors shadow-lg shadow-blue-500/30">
          Upload
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-038",
        "title": "Invoice Card",
        "description": "Invoice summary card.",
        "dir": "cards/card-038",
        "content": """
  <div class="min-h-screen bg-slate-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 max-w-sm w-full">
      <div class="flex justify-between items-start mb-6">
        <div>
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Invoice</span>
          <h3 class="text-xl font-bold text-slate-900">#INV-2023-001</h3>
        </div>
        <span class="bg-green-100 text-green-700 text-xs font-bold px-2 py-1 rounded uppercase tracking-wide">Paid</span>
      </div>

      <div class="space-y-4 mb-6 border-b border-slate-100 pb-6">
        <div class="flex justify-between text-sm">
          <span class="text-slate-500">Web Design Project</span>
          <span class="font-medium text-slate-900">$2,500.00</span>
        </div>
        <div class="flex justify-between text-sm">
          <span class="text-slate-500">Hosting (1 Year)</span>
          <span class="font-medium text-slate-900">$120.00</span>
        </div>
        <div class="flex justify-between text-sm">
          <span class="text-slate-500">Domain Name</span>
          <span class="font-medium text-slate-900">$15.00</span>
        </div>
      </div>

      <div class="flex justify-between items-center mb-6">
        <span class="text-slate-500 font-medium">Total Amount</span>
        <span class="text-2xl font-bold text-slate-900">$2,635.00</span>
      </div>

      <button class="w-full border border-slate-200 text-slate-700 font-bold py-2.5 rounded-lg hover:bg-slate-50 transition-colors flex items-center justify-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
        </svg>
        Download PDF
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-039",
        "title": "Language Card",
        "description": "Language learning progress card.",
        "dir": "cards/card-039",
        "content": """
  <div class="min-h-screen bg-yellow-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-6 max-w-sm w-full">
      <div class="flex items-center gap-4 mb-6">
        <div class="w-14 h-14 bg-yellow-100 rounded-2xl flex items-center justify-center text-2xl shadow-sm">
          🇪🇸
        </div>
        <div>
          <h3 class="text-lg font-bold text-gray-900">Spanish</h3>
          <p class="text-sm text-gray-500">Intermediate Level</p>
        </div>
        <div class="ml-auto">
          <div class="w-10 h-10 rounded-full border-4 border-yellow-100 border-t-yellow-500 flex items-center justify-center text-xs font-bold text-yellow-600 transform -rotate-45">
            <span class="transform rotate-45">75%</span>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-4 mb-6">
        <div class="bg-gray-50 p-3 rounded-xl">
          <span class="block text-2xl font-bold text-gray-900 mb-1">12</span>
          <span class="text-xs text-gray-500 font-medium uppercase tracking-wide">Day Streak</span>
        </div>
        <div class="bg-gray-50 p-3 rounded-xl">
          <span class="block text-2xl font-bold text-gray-900 mb-1">450</span>
          <span class="text-xs text-gray-500 font-medium uppercase tracking-wide">XP Earned</span>
        </div>
      </div>

      <h4 class="text-sm font-bold text-gray-900 mb-3">Daily Goals</h4>
      <div class="space-y-3 mb-6">
        <div class="flex items-center gap-3">
          <div class="w-6 h-6 bg-green-100 text-green-600 rounded-full flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
          </div>
          <span class="text-sm text-gray-600 line-through">Complete 2 lessons</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="w-6 h-6 border-2 border-gray-200 rounded-full"></div>
          <span class="text-sm text-gray-900">Practice speaking</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="w-6 h-6 border-2 border-gray-200 rounded-full"></div>
          <span class="text-sm text-gray-900">Learn 10 new words</span>
        </div>
      </div>

      <button class="w-full bg-yellow-400 text-yellow-900 font-bold py-3 rounded-xl hover:bg-yellow-500 transition-colors shadow-lg shadow-yellow-400/30">
        Continue Learning
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-040",
        "title": "Maintenance Card",
        "description": "System maintenance status card.",
        "dir": "cards/card-040",
        "content": """
  <div class="min-h-screen bg-slate-900 flex items-center justify-center p-4">
    <div class="bg-slate-800 rounded-xl shadow-2xl p-8 max-w-sm w-full text-center border border-slate-700">
      <div class="w-20 h-20 bg-slate-700/50 rounded-full flex items-center justify-center mx-auto mb-6 animate-pulse">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
      </div>

      <h2 class="text-2xl font-bold text-white mb-2">System Maintenance</h2>
      <p class="text-slate-400 mb-8">
        We're currently performing scheduled maintenance to improve our services. We'll be back shortly.
      </p>

      <div class="bg-slate-700/50 rounded-lg p-4 mb-8 text-left">
        <div class="flex justify-between text-sm mb-2">
          <span class="text-slate-400">Status</span>
          <span class="text-blue-400 font-bold">In Progress</span>
        </div>
        <div class="flex justify-between text-sm">
          <span class="text-slate-400">Est. Completion</span>
          <span class="text-white font-bold">14:00 UTC</span>
        </div>
      </div>

      <button class="text-slate-400 hover:text-white text-sm font-medium transition-colors flex items-center justify-center gap-2 mx-auto">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Check Status
      </button>
    </div>
  </div>"""
    }
]
TEMPLATES_CARDS = TEMPLATES_CARDS_1 + TEMPLATES_CARDS_2 + TEMPLATES_CARDS_3 + TEMPLATES_CARDS_4

TEMPLATES_CARDS_5 = [
    {
        "id": "card-041",
        "title": "Music Album Card",
        "description": "Music album card with track list.",
        "dir": "cards/card-041",
        "content": """
  <div class="min-h-screen bg-neutral-900 flex items-center justify-center p-4">
    <div class="bg-neutral-800 rounded-xl shadow-2xl overflow-hidden max-w-sm w-full border border-neutral-700">
      <div class="relative aspect-square">
        <img src="https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Album Cover" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 via-transparent to-transparent"></div>
        <div class="absolute bottom-6 left-6">
          <h3 class="text-2xl font-bold text-white mb-1">Neon Dreams</h3>
          <p class="text-neutral-400">The Synthetics</p>
        </div>
        <button class="absolute bottom-6 right-6 w-12 h-12 bg-green-500 rounded-full flex items-center justify-center text-black hover:scale-105 transition-transform shadow-lg shadow-green-500/20">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ml-1" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>

      <div class="p-6">
        <div class="space-y-4">
          <div class="flex items-center justify-between group cursor-pointer">
            <div class="flex items-center gap-4">
              <span class="text-neutral-500 font-mono text-sm group-hover:text-green-500">01</span>
              <div>
                <h4 class="text-white font-medium group-hover:text-green-500 transition-colors">Night Drive</h4>
                <p class="text-xs text-neutral-500">The Synthetics</p>
              </div>
            </div>
            <span class="text-xs text-neutral-500">3:45</span>
          </div>

          <div class="flex items-center justify-between group cursor-pointer">
            <div class="flex items-center gap-4">
              <span class="text-green-500 font-mono text-sm">02</span>
              <div>
                <h4 class="text-green-500 font-medium">Cyber City</h4>
                <p class="text-xs text-neutral-500">The Synthetics</p>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <div class="flex gap-0.5 items-end h-3">
                <div class="w-0.5 h-2 bg-green-500 animate-pulse"></div>
                <div class="w-0.5 h-3 bg-green-500 animate-pulse delay-75"></div>
                <div class="w-0.5 h-1 bg-green-500 animate-pulse delay-150"></div>
                <div class="w-0.5 h-2.5 bg-green-500 animate-pulse delay-100"></div>
              </div>
              <span class="text-xs text-white">4:12</span>
            </div>
          </div>

          <div class="flex items-center justify-between group cursor-pointer">
            <div class="flex items-center gap-4">
              <span class="text-neutral-500 font-mono text-sm group-hover:text-green-500">03</span>
              <div>
                <h4 class="text-white font-medium group-hover:text-green-500 transition-colors">Digital Love</h4>
                <p class="text-xs text-neutral-500">The Synthetics</p>
              </div>
            </div>
            <span class="text-xs text-neutral-500">3:58</span>
          </div>

          <div class="flex items-center justify-between group cursor-pointer">
            <div class="flex items-center gap-4">
              <span class="text-neutral-500 font-mono text-sm group-hover:text-green-500">04</span>
              <div>
                <h4 class="text-white font-medium group-hover:text-green-500 transition-colors">Memory Lane</h4>
                <p class="text-xs text-neutral-500">The Synthetics</p>
              </div>
            </div>
            <span class="text-xs text-neutral-500">4:05</span>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-042",
        "title": "Project Card",
        "description": "Project status card with team members.",
        "dir": "cards/card-042",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 max-w-sm w-full hover:shadow-md transition-shadow">
      <div class="flex justify-between items-start mb-4">
        <div class="p-2 bg-indigo-50 text-indigo-600 rounded-lg">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
        </div>
        <button class="text-gray-400 hover:text-gray-600">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
          </svg>
        </button>
      </div>

      <h3 class="text-lg font-bold text-gray-900 mb-2">Website Redesign</h3>
      <p class="text-gray-500 text-sm mb-6 line-clamp-2">
        Revamping the corporate website with new branding guidelines and improved user experience.
      </p>

      <div class="mb-6">
        <div class="flex justify-between text-xs font-bold text-gray-500 mb-2">
          <span>Progress</span>
          <span>75%</span>
        </div>
        <div class="w-full bg-gray-100 rounded-full h-2">
          <div class="bg-indigo-600 h-2 rounded-full" style="width: 75%"></div>
        </div>
      </div>

      <div class="flex items-center justify-between pt-4 border-t border-gray-100">
        <div class="flex -space-x-2">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Member" class="w-8 h-8 rounded-full border-2 border-white">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Member" class="w-8 h-8 rounded-full border-2 border-white">
          <div class="w-8 h-8 rounded-full border-2 border-white bg-gray-100 flex items-center justify-center text-xs font-bold text-gray-500">+3</div>
        </div>

        <div class="flex items-center gap-1 text-xs font-medium text-gray-500 bg-gray-100 px-2 py-1 rounded">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          2 weeks left
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-043",
        "title": "Movie Card",
        "description": "Movie poster card with rating.",
        "dir": "cards/card-043",
        "content": """
  <div class="min-h-screen bg-gray-900 flex items-center justify-center p-4">
    <div class="bg-gray-800 rounded-xl overflow-hidden max-w-xs w-full shadow-2xl group cursor-pointer">
      <div class="relative aspect-[2/3] overflow-hidden">
        <img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Movie Poster" class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-transparent to-transparent opacity-80"></div>

        <div class="absolute top-4 right-4 bg-yellow-500 text-black font-bold text-xs px-2 py-1 rounded shadow-lg">
          IMDb 8.5
        </div>

        <div class="absolute bottom-0 left-0 right-0 p-6">
          <h3 class="text-2xl font-bold text-white mb-1">Inception</h3>
          <p class="text-gray-300 text-sm mb-3">Sci-Fi • Thriller • 2010</p>

          <div class="flex gap-2">
            <button class="flex-1 bg-red-600 text-white text-sm font-bold py-2 rounded hover:bg-red-700 transition-colors">
              Watch Now
            </button>
            <button class="p-2 bg-gray-700 text-white rounded hover:bg-gray-600 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-044",
        "title": "Address Card",
        "description": "Address details card with map preview.",
        "dir": "cards/card-044",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg overflow-hidden max-w-sm w-full">
      <div class="h-40 bg-slate-200 relative">
        <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Map" class="w-full h-full object-cover opacity-80">
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="w-8 h-8 bg-red-500 rounded-full border-4 border-white shadow-lg animate-bounce"></div>
        </div>
      </div>

      <div class="p-6">
        <div class="flex items-start gap-4 mb-6">
          <div class="w-10 h-10 bg-slate-100 rounded-lg flex items-center justify-center flex-shrink-0 text-slate-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <div>
            <h3 class="font-bold text-slate-900">Headquarters</h3>
            <p class="text-slate-500 text-sm mt-1">
              123 Innovation Drive<br>
              Silicon Valley, CA 94025<br>
              United States
            </p>
          </div>
        </div>

        <div class="flex gap-3">
          <button class="flex-1 border border-slate-200 text-slate-700 font-bold py-2 rounded-lg hover:bg-slate-50 transition-colors flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16l2.879-2.879m0 0a3 3 0 104.243-4.242 3 3 0 00-4.243 4.242zM21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Directions
          </button>
          <button class="flex-1 bg-blue-600 text-white font-bold py-2 rounded-lg hover:bg-blue-700 transition-colors flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
            </svg>
            Copy
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-045",
        "title": "Storage Card",
        "description": "Storage usage card.",
        "dir": "cards/card-045",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-6 max-w-sm w-full">
      <div class="flex justify-between items-center mb-6">
        <h3 class="font-bold text-gray-900">Storage Usage</h3>
        <button class="text-blue-600 text-sm font-bold hover:underline">Upgrade</button>
      </div>

      <div class="relative w-48 h-48 mx-auto mb-8">
        <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
          <!-- Background Circle -->
          <path class="text-gray-100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3" />
          <!-- Progress Circle -->
          <path class="text-blue-600" stroke-dasharray="75, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" />
        </svg>
        <div class="absolute inset-0 flex flex-col items-center justify-center">
          <span class="text-3xl font-bold text-gray-900">75%</span>
          <span class="text-xs text-gray-500 uppercase tracking-wide">Used</span>
        </div>
      </div>

      <div class="space-y-4">
        <div class="flex items-center gap-3">
          <div class="w-3 h-3 rounded-full bg-blue-600"></div>
          <span class="text-sm text-gray-600 flex-1">Documents</span>
          <span class="text-sm font-bold text-gray-900">45 GB</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="w-3 h-3 rounded-full bg-blue-400"></div>
          <span class="text-sm text-gray-600 flex-1">Images</span>
          <span class="text-sm font-bold text-gray-900">25 GB</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="w-3 h-3 rounded-full bg-blue-200"></div>
          <span class="text-sm text-gray-600 flex-1">Videos</span>
          <span class="text-sm font-bold text-gray-900">15 GB</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="w-3 h-3 rounded-full bg-gray-200"></div>
          <span class="text-sm text-gray-600 flex-1">Free Space</span>
          <span class="text-sm font-bold text-gray-900">15 GB</span>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-046",
        "title": "Comment Card",
        "description": "User comment card with actions.",
        "dir": "cards/card-046",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 max-w-md w-full">
      <div class="flex gap-4">
        <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User" class="w-10 h-10 rounded-full object-cover flex-shrink-0">
        <div class="flex-1">
          <div class="flex justify-between items-start mb-1">
            <div>
              <h4 class="font-bold text-slate-900">Alex Morgan</h4>
              <p class="text-xs text-slate-500">2 hours ago</p>
            </div>
            <button class="text-slate-400 hover:text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
              </svg>
            </button>
          </div>

          <p class="text-slate-600 text-sm leading-relaxed mb-4">
            This is exactly what I was looking for! The attention to detail in the design is impressive, and the code quality is top-notch. Great work team! 👏
          </p>

          <div class="flex items-center gap-6">
            <button class="flex items-center gap-1.5 text-slate-500 hover:text-blue-600 transition-colors text-sm font-medium group">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 group-hover:scale-110 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
              </svg>
              24
            </button>
            <button class="flex items-center gap-1.5 text-slate-500 hover:text-blue-600 transition-colors text-sm font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              Reply
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-047",
        "title": "Tag Card",
        "description": "Card with tag cloud.",
        "dir": "cards/card-047",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 max-w-sm w-full">
      <h3 class="text-lg font-bold text-gray-900 mb-4">Popular Topics</h3>

      <div class="flex flex-wrap gap-2">
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">Technology</a>
        <a href="#" class="px-3 py-1.5 bg-blue-50 text-blue-600 rounded-lg text-sm font-medium hover:bg-blue-100 transition-colors">Design</a>
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">Development</a>
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">UI/UX</a>
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">Business</a>
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">Marketing</a>
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">Startup</a>
        <a href="#" class="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors">Productivity</a>
        <a href="#" class="px-3 py-1.5 bg-purple-50 text-purple-600 rounded-lg text-sm font-medium hover:bg-purple-100 transition-colors">Innovation</a>
      </div>

      <button class="w-full mt-6 text-blue-600 text-sm font-bold hover:underline">
        View all topics
      </button>
    </div>
  </div>"""
    },
    {
        "id": "card-048",
        "title": "Achievement Card",
        "description": "Achievement unlock card.",
        "dir": "cards/card-048",
        "content": """
  <div class="min-h-screen bg-slate-900 flex items-center justify-center p-4">
    <div class="bg-gradient-to-br from-slate-800 to-slate-900 rounded-xl shadow-2xl p-1 max-w-sm w-full border border-slate-700">
      <div class="bg-slate-800 rounded-lg p-6 text-center relative overflow-hidden">
        <div class="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-10"></div>

        <div class="relative z-10">
          <div class="w-20 h-20 mx-auto mb-4 relative">
            <div class="absolute inset-0 bg-yellow-500 rounded-full blur-xl opacity-50 animate-pulse"></div>
            <div class="relative bg-gradient-to-br from-yellow-300 to-yellow-600 rounded-full w-full h-full flex items-center justify-center shadow-lg border-2 border-yellow-200">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-yellow-900" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd" />
              </svg>
            </div>
          </div>

          <h3 class="text-2xl font-bold text-white mb-1">Power User</h3>
          <p class="text-slate-400 text-sm mb-6">Unlocked for completing 100 tasks</p>

          <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-700 mb-6">
            <div class="flex justify-between text-xs text-slate-400 mb-2">
              <span>Reward</span>
              <span class="text-yellow-500 font-bold">+500 XP</span>
            </div>
            <div class="flex justify-between text-xs text-slate-400">
              <span>Date</span>
              <span class="text-white font-bold">Oct 24, 2023</span>
            </div>
          </div>

          <button class="w-full bg-yellow-500 hover:bg-yellow-400 text-yellow-900 font-bold py-2.5 rounded-lg transition-colors shadow-lg shadow-yellow-500/20">
            Claim Reward
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "card-049",
        "title": "Countdown Card",
        "description": "Event countdown card.",
        "dir": "cards/card-049",
        "content": """
  <div class="min-h-screen bg-indigo-900 flex items-center justify-center p-4">
    <div class="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl p-8 max-w-md w-full text-center border border-white/20">
      <span class="inline-block px-3 py-1 bg-indigo-500/30 text-indigo-200 rounded-full text-xs font-bold uppercase tracking-widest mb-4 border border-indigo-400/30">
        Coming Soon
      </span>

      <h2 class="text-3xl font-bold text-white mb-2">Product Launch</h2>
      <p class="text-indigo-200 mb-8">Get ready for something amazing.</p>

      <div class="flex justify-center gap-4 mb-8">
        <div class="bg-black/30 rounded-xl p-3 w-16 backdrop-blur-sm border border-white/10">
          <span class="block text-2xl font-bold text-white">02</span>
          <span class="text-xs text-indigo-300 uppercase">Days</span>
        </div>
        <div class="bg-black/30 rounded-xl p-3 w-16 backdrop-blur-sm border border-white/10">
          <span class="block text-2xl font-bold text-white">14</span>
          <span class="text-xs text-indigo-300 uppercase">Hrs</span>
        </div>
        <div class="bg-black/30 rounded-xl p-3 w-16 backdrop-blur-sm border border-white/10">
          <span class="block text-2xl font-bold text-white">45</span>
          <span class="text-xs text-indigo-300 uppercase">Mins</span>
        </div>
        <div class="bg-black/30 rounded-xl p-3 w-16 backdrop-blur-sm border border-white/10">
          <span class="block text-2xl font-bold text-white">12</span>
          <span class="text-xs text-indigo-300 uppercase">Secs</span>
        </div>
      </div>

      <form class="flex gap-2">
        <input type="email" placeholder="Enter your email" class="flex-1 bg-white/10 border border-white/20 rounded-lg px-4 py-2.5 text-white placeholder-indigo-300 focus:outline-none focus:border-indigo-400 focus:bg-white/20 transition-all">
        <button class="bg-indigo-500 hover:bg-indigo-400 text-white font-bold px-6 py-2.5 rounded-lg transition-colors shadow-lg shadow-indigo-500/30">
          Notify Me
        </button>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "card-050",
        "title": "Error Card",
        "description": "Error message card.",
        "dir": "cards/card-050",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg p-8 max-w-sm w-full text-center">
      <div class="w-20 h-20 bg-red-100 text-red-500 rounded-full flex items-center justify-center mx-auto mb-6">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
      </div>

      <h3 class="text-xl font-bold text-gray-900 mb-2">Payment Failed</h3>
      <p class="text-gray-500 mb-6">
        We couldn't process your payment. Please check your card details and try again.
      </p>

      <div class="space-y-3">
        <button class="w-full bg-red-600 text-white font-bold py-2.5 rounded-lg hover:bg-red-700 transition-colors shadow-lg shadow-red-500/30">
          Try Again
        </button>
        <button class="w-full bg-white border border-gray-200 text-gray-700 font-bold py-2.5 rounded-lg hover:bg-gray-50 transition-colors">
          Contact Support
        </button>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_CARDS = TEMPLATES_CARDS_1 + TEMPLATES_CARDS_2 + TEMPLATES_CARDS_3 + TEMPLATES_CARDS_4 + TEMPLATES_CARDS_5
TEMPLATES_LISTS_1 = [
    {
        "id": "list-001",
        "title": "Simple List",
        "description": "Basic list with text items.",
        "dir": "lists/list-001",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow max-w-md w-full overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-200">
        <h3 class="text-lg font-medium text-gray-900">Task List</h3>
      </div>
      <ul class="divide-y divide-gray-200">
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex items-center justify-between">
            <span class="text-gray-700">Complete project proposal</span>
            <span class="text-xs text-gray-400">Today</span>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex items-center justify-between">
            <span class="text-gray-700">Review design mockups</span>
            <span class="text-xs text-gray-400">Tomorrow</span>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex items-center justify-between">
            <span class="text-gray-700">Team meeting</span>
            <span class="text-xs text-gray-400">Wed</span>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex items-center justify-between">
            <span class="text-gray-700">Client call</span>
            <span class="text-xs text-gray-400">Thu</span>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex items-center justify-between">
            <span class="text-gray-700">Weekly report</span>
            <span class="text-xs text-gray-400">Fri</span>
          </div>
        </li>
      </ul>
    </div>
  </div>"""
    },
    {
        "id": "list-002",
        "title": "User List",
        "description": "List of users with avatars.",
        "dir": "lists/list-002",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm max-w-md w-full overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-100 flex justify-between items-center">
        <h3 class="font-bold text-gray-900">Team Members</h3>
        <span class="bg-blue-100 text-blue-800 text-xs font-bold px-2.5 py-0.5 rounded-full">5 Active</span>
      </div>
      <ul class="divide-y divide-gray-100">
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <img class="h-10 w-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900 truncate">Leslie Alexander</p>
              <p class="text-sm text-gray-500 truncate">leslie.alexander@example.com</p>
            </div>
            <div class="inline-flex items-center text-base font-semibold text-gray-900">
              <span class="w-2.5 h-2.5 bg-green-400 rounded-full"></span>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <img class="h-10 w-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900 truncate">Michael Foster</p>
              <p class="text-sm text-gray-500 truncate">michael.foster@example.com</p>
            </div>
            <div class="inline-flex items-center text-base font-semibold text-gray-900">
              <span class="w-2.5 h-2.5 bg-green-400 rounded-full"></span>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <img class="h-10 w-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900 truncate">Dries Vincent</p>
              <p class="text-sm text-gray-500 truncate">dries.vincent@example.com</p>
            </div>
            <div class="inline-flex items-center text-base font-semibold text-gray-900">
              <span class="w-2.5 h-2.5 bg-gray-300 rounded-full"></span>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <img class="h-10 w-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900 truncate">Lindsay Walton</p>
              <p class="text-sm text-gray-500 truncate">lindsay.walton@example.com</p>
            </div>
            <div class="inline-flex items-center text-base font-semibold text-gray-900">
              <span class="w-2.5 h-2.5 bg-green-400 rounded-full"></span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>"""
    },
    {
        "id": "list-003",
        "title": "Action List",
        "description": "List with action buttons.",
        "dir": "lists/list-003",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg max-w-lg w-full overflow-hidden border border-slate-200">
      <div class="px-6 py-4 bg-slate-50 border-b border-slate-200">
        <h3 class="text-lg font-bold text-slate-800">Pending Approvals</h3>
      </div>
      <ul class="divide-y divide-slate-100">
        <li class="px-6 py-4 flex items-center justify-between gap-4">
          <div>
            <p class="font-medium text-slate-900">Expense Report #1023</p>
            <p class="text-sm text-slate-500">Submitted by John Doe</p>
          </div>
          <div class="flex gap-2">
            <button class="px-3 py-1.5 text-sm font-medium text-green-700 bg-green-50 hover:bg-green-100 rounded-lg transition-colors">Approve</button>
            <button class="px-3 py-1.5 text-sm font-medium text-red-700 bg-red-50 hover:bg-red-100 rounded-lg transition-colors">Reject</button>
          </div>
        </li>
        <li class="px-6 py-4 flex items-center justify-between gap-4">
          <div>
            <p class="font-medium text-slate-900">Travel Request #445</p>
            <p class="text-sm text-slate-500">Submitted by Sarah Smith</p>
          </div>
          <div class="flex gap-2">
            <button class="px-3 py-1.5 text-sm font-medium text-green-700 bg-green-50 hover:bg-green-100 rounded-lg transition-colors">Approve</button>
            <button class="px-3 py-1.5 text-sm font-medium text-red-700 bg-red-50 hover:bg-red-100 rounded-lg transition-colors">Reject</button>
          </div>
        </li>
        <li class="px-6 py-4 flex items-center justify-between gap-4">
          <div>
            <p class="font-medium text-slate-900">New Hire Onboarding</p>
            <p class="text-sm text-slate-500">Submitted by HR Dept</p>
          </div>
          <div class="flex gap-2">
            <button class="px-3 py-1.5 text-sm font-medium text-green-700 bg-green-50 hover:bg-green-100 rounded-lg transition-colors">Approve</button>
            <button class="px-3 py-1.5 text-sm font-medium text-red-700 bg-red-50 hover:bg-red-100 rounded-lg transition-colors">Reject</button>
          </div>
        </li>
      </ul>
      <div class="px-6 py-4 bg-slate-50 border-t border-slate-200 text-center">
        <button class="text-sm font-medium text-slate-600 hover:text-slate-900">View all requests</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-004",
        "title": "File List",
        "description": "List of files with icons and sizes.",
        "dir": "lists/list-004",
        "content": """
  <div class="min-h-screen bg-blue-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-xl max-w-md w-full overflow-hidden">
      <div class="px-6 py-5 border-b border-gray-100">
        <h3 class="text-xl font-bold text-gray-800">Recent Files</h3>
      </div>
      <ul class="divide-y divide-gray-100">
        <li class="px-6 py-4 hover:bg-blue-50/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-red-100 text-red-500 rounded-lg flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="flex-1">
              <p class="font-medium text-gray-900 group-hover:text-blue-600 transition-colors">Project_Proposal.pdf</p>
              <p class="text-xs text-gray-500">2.4 MB • 2 mins ago</p>
            </div>
            <button class="text-gray-400 hover:text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
              </svg>
            </button>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-blue-50/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-blue-100 text-blue-500 rounded-lg flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="flex-1">
              <p class="font-medium text-gray-900 group-hover:text-blue-600 transition-colors">Design_Mockup.png</p>
              <p class="text-xs text-gray-500">4.1 MB • 1 hour ago</p>
            </div>
            <button class="text-gray-400 hover:text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
              </svg>
            </button>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-blue-50/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-green-100 text-green-500 rounded-lg flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <div class="flex-1">
              <p class="font-medium text-gray-900 group-hover:text-blue-600 transition-colors">Financial_Report.xlsx</p>
              <p class="text-xs text-gray-500">1.2 MB • 3 hours ago</p>
            </div>
            <button class="text-gray-400 hover:text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
              </svg>
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>"""
    },
    {
        "id": "list-005",
        "title": "Notification List",
        "description": "List of notifications with status indicators.",
        "dir": "lists/list-005",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-lg max-w-sm w-full overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-100 flex justify-between items-center">
        <h3 class="font-bold text-gray-900">Notifications</h3>
        <button class="text-xs font-medium text-blue-600 hover:text-blue-800">Mark all as read</button>
      </div>
      <ul class="divide-y divide-gray-100">
        <li class="px-6 py-4 bg-blue-50/30 hover:bg-blue-50 transition-colors cursor-pointer relative">
          <div class="absolute left-0 top-0 bottom-0 w-1 bg-blue-500"></div>
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-blue-500 rounded-full"></div>
            </div>
            <div>
              <p class="text-sm text-gray-800"><span class="font-bold">New comment</span> on your post "Redesigning the dashboard"</p>
              <p class="text-xs text-gray-500 mt-1">10 minutes ago</p>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-transparent rounded-full"></div>
            </div>
            <div>
              <p class="text-sm text-gray-800"><span class="font-bold">System update</span> scheduled for tonight at 2 AM EST</p>
              <p class="text-xs text-gray-500 mt-1">2 hours ago</p>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors cursor-pointer">
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-transparent rounded-full"></div>
            </div>
            <div>
              <p class="text-sm text-gray-800"><span class="font-bold">Welcome aboard!</span> Get started with our quick tutorial.</p>
              <p class="text-xs text-gray-500 mt-1">1 day ago</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>"""
    },
    {
        "id": "list-006",
        "title": "Product List",
        "description": "List of products with prices and ratings.",
        "dir": "lists/list-006",
        "content": """
  <div class="min-h-screen bg-neutral-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl max-w-md w-full overflow-hidden">
      <div class="px-6 py-5 border-b border-neutral-100">
        <h3 class="text-xl font-bold text-neutral-900">Shopping Cart</h3>
      </div>
      <ul class="divide-y divide-neutral-100">
        <li class="p-4 hover:bg-neutral-50 transition-colors">
          <div class="flex gap-4">
            <div class="w-20 h-20 bg-neutral-100 rounded-lg overflow-hidden flex-shrink-0">
              <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Shoe" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <h4 class="font-bold text-neutral-900">Nike Air Max</h4>
                <p class="text-sm text-neutral-500">Size: 10 • Color: Red</p>
              </div>
              <div class="flex justify-between items-end">
                <span class="font-bold text-neutral-900">$129.00</span>
                <div class="flex items-center gap-2">
                  <button class="w-6 h-6 rounded-full border border-neutral-300 flex items-center justify-center text-neutral-500 hover:bg-neutral-100">-</button>
                  <span class="text-sm font-medium">1</span>
                  <button class="w-6 h-6 rounded-full border border-neutral-300 flex items-center justify-center text-neutral-500 hover:bg-neutral-100">+</button>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="p-4 hover:bg-neutral-50 transition-colors">
          <div class="flex gap-4">
            <div class="w-20 h-20 bg-neutral-100 rounded-lg overflow-hidden flex-shrink-0">
              <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Watch" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <h4 class="font-bold text-neutral-900">Apple Watch</h4>
                <p class="text-sm text-neutral-500">Series 7 • Midnight</p>
              </div>
              <div class="flex justify-between items-end">
                <span class="font-bold text-neutral-900">$399.00</span>
                <div class="flex items-center gap-2">
                  <button class="w-6 h-6 rounded-full border border-neutral-300 flex items-center justify-center text-neutral-500 hover:bg-neutral-100">-</button>
                  <span class="text-sm font-medium">1</span>
                  <button class="w-6 h-6 rounded-full border border-neutral-300 flex items-center justify-center text-neutral-500 hover:bg-neutral-100">+</button>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
      <div class="p-6 bg-neutral-50 border-t border-neutral-100">
        <div class="flex justify-between items-center mb-4">
          <span class="text-neutral-500">Total</span>
          <span class="text-2xl font-bold text-neutral-900">$528.00</span>
        </div>
        <button class="w-full bg-black text-white font-bold py-3 rounded-xl hover:bg-neutral-800 transition-colors">
          Checkout
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-007",
        "title": "Music List",
        "description": "Playlist with track duration.",
        "dir": "lists/list-007",
        "content": """
  <div class="min-h-screen bg-zinc-900 flex items-center justify-center p-4">
    <div class="bg-zinc-800 rounded-xl shadow-2xl max-w-md w-full overflow-hidden border border-zinc-700">
      <div class="p-6 bg-gradient-to-b from-indigo-900 to-zinc-800">
        <div class="flex items-end gap-4 mb-4">
          <div class="w-24 h-24 bg-indigo-500 shadow-lg rounded-md flex items-center justify-center text-white text-4xl font-bold">
            ♫
          </div>
          <div>
            <p class="text-xs font-bold text-white uppercase tracking-wider mb-1">Playlist</p>
            <h2 class="text-2xl font-bold text-white mb-2">Chill Vibes</h2>
            <p class="text-zinc-400 text-sm">Created by Stephen • 50 songs</p>
          </div>
        </div>
      </div>
      <ul class="divide-y divide-zinc-700/50">
        <li class="px-4 py-3 hover:bg-white/5 transition-colors group cursor-pointer flex items-center gap-4">
          <span class="text-zinc-500 font-mono w-6 text-center group-hover:text-white">1</span>
          <div class="flex-1">
            <h4 class="text-white font-medium">Midnight City</h4>
            <p class="text-xs text-zinc-400">M83</p>
          </div>
          <span class="text-xs text-zinc-500">4:03</span>
        </li>
        <li class="px-4 py-3 hover:bg-white/5 transition-colors group cursor-pointer flex items-center gap-4 bg-white/5">
          <span class="text-green-500 font-mono w-6 text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mx-auto animate-pulse" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </span>
          <div class="flex-1">
            <h4 class="text-green-500 font-medium">Instant Crush</h4>
            <p class="text-xs text-zinc-400">Daft Punk</p>
          </div>
          <span class="text-xs text-white">5:37</span>
        </li>
        <li class="px-4 py-3 hover:bg-white/5 transition-colors group cursor-pointer flex items-center gap-4">
          <span class="text-zinc-500 font-mono w-6 text-center group-hover:text-white">3</span>
          <div class="flex-1">
            <h4 class="text-white font-medium">The Less I Know The Better</h4>
            <p class="text-xs text-zinc-400">Tame Impala</p>
          </div>
          <span class="text-xs text-zinc-500">3:36</span>
        </li>
        <li class="px-4 py-3 hover:bg-white/5 transition-colors group cursor-pointer flex items-center gap-4">
          <span class="text-zinc-500 font-mono w-6 text-center group-hover:text-white">4</span>
          <div class="flex-1">
            <h4 class="text-white font-medium">Heat Waves</h4>
            <p class="text-xs text-zinc-400">Glass Animals</p>
          </div>
          <span class="text-xs text-zinc-500">3:58</span>
        </li>
      </ul>
    </div>
  </div>"""
    },
    {
        "id": "list-008",
        "title": "Contact List",
        "description": "Alphabetical contact list.",
        "dir": "lists/list-008",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 max-w-sm w-full overflow-hidden h-[500px] flex flex-col">
      <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
        <input type="text" placeholder="Search contacts..." class="w-full bg-white border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500">
      </div>
      <div class="flex-1 overflow-y-auto">
        <div class="px-6 py-2 bg-gray-50 text-xs font-bold text-gray-500 uppercase sticky top-0">A</div>
        <ul class="divide-y divide-gray-100">
          <li class="px-6 py-3 hover:bg-gray-50 cursor-pointer flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center font-bold text-xs">AB</div>
            <span class="text-gray-900 font-medium">Alice Brown</span>
          </li>
          <li class="px-6 py-3 hover:bg-gray-50 cursor-pointer flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold text-xs">AC</div>
            <span class="text-gray-900 font-medium">Andrew Clark</span>
          </li>
        </ul>

        <div class="px-6 py-2 bg-gray-50 text-xs font-bold text-gray-500 uppercase sticky top-0">B</div>
        <ul class="divide-y divide-gray-100">
          <li class="px-6 py-3 hover:bg-gray-50 cursor-pointer flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-green-100 text-green-600 flex items-center justify-center font-bold text-xs">BB</div>
            <span class="text-gray-900 font-medium">Bob Baker</span>
          </li>
          <li class="px-6 py-3 hover:bg-gray-50 cursor-pointer flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold text-xs">BW</div>
            <span class="text-gray-900 font-medium">Bruce Wayne</span>
          </li>
        </ul>

        <div class="px-6 py-2 bg-gray-50 text-xs font-bold text-gray-500 uppercase sticky top-0">C</div>
        <ul class="divide-y divide-gray-100">
          <li class="px-6 py-3 hover:bg-gray-50 cursor-pointer flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-red-100 text-red-600 flex items-center justify-center font-bold text-xs">CK</div>
            <span class="text-gray-900 font-medium">Clark Kent</span>
          </li>
        </ul>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-009",
        "title": "Feature List",
        "description": "List of features with checkmarks.",
        "dir": "lists/list-009",
        "content": """
  <div class="min-h-screen bg-indigo-900 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl max-w-sm w-full overflow-hidden p-8">
      <div class="text-center mb-8">
        <h3 class="text-2xl font-bold text-gray-900">Pro Plan</h3>
        <div class="mt-4 flex items-baseline justify-center">
          <span class="text-5xl font-extrabold text-gray-900">$29</span>
          <span class="ml-1 text-xl text-gray-500">/mo</span>
        </div>
        <p class="mt-4 text-sm text-gray-500">Perfect for growing businesses and small teams.</p>
      </div>

      <ul class="space-y-4 mb-8">
        <li class="flex items-start">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-green-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <p class="ml-3 text-base text-gray-700">Unlimited projects</p>
        </li>
        <li class="flex items-start">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-green-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <p class="ml-3 text-base text-gray-700">Analytics dashboard</p>
        </li>
        <li class="flex items-start">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-green-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <p class="ml-3 text-base text-gray-700">24/7 priority support</p>
        </li>
        <li class="flex items-start">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-green-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <p class="ml-3 text-base text-gray-700">Custom domain</p>
        </li>
        <li class="flex items-start">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-gray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
          <p class="ml-3 text-base text-gray-400">White labeling</p>
        </li>
      </ul>

      <button class="w-full bg-indigo-600 text-white font-bold py-3 rounded-xl hover:bg-indigo-700 transition-colors shadow-lg shadow-indigo-500/30">
        Get Started
      </button>
    </div>
  </div>"""
    },
    {
        "id": "list-010",
        "title": "Leaderboard List",
        "description": "Ranked list with scores.",
        "dir": "lists/list-010",
        "content": """
  <div class="min-h-screen bg-violet-600 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden">
      <div class="bg-violet-800 p-6 text-center">
        <h3 class="text-2xl font-bold text-white mb-1">Leaderboard</h3>
        <p class="text-violet-200 text-sm">Weekly Top Performers</p>
      </div>

      <div class="px-6 -mt-6 mb-4">
        <div class="bg-white rounded-xl shadow-lg p-4 flex items-center justify-between border border-violet-100">
          <div class="flex items-center gap-4">
            <div class="w-8 h-8 bg-yellow-400 rounded-full flex items-center justify-center text-yellow-900 font-bold shadow-sm">1</div>
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="w-10 h-10 rounded-full border-2 border-white shadow-sm">
            <div>
              <p class="font-bold text-gray-900">Sarah Jenkins</p>
              <p class="text-xs text-gray-500">2,450 pts</p>
            </div>
          </div>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
          </svg>
        </div>
      </div>

      <ul class="divide-y divide-gray-100">
        <li class="px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <div class="w-8 h-8 text-gray-400 font-bold flex items-center justify-center">2</div>
            <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="w-10 h-10 rounded-full">
            <div>
              <p class="font-bold text-gray-900">Tom Cook</p>
              <p class="text-xs text-gray-500">2,100 pts</p>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <div class="w-8 h-8 text-gray-400 font-bold flex items-center justify-center">3</div>
            <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="w-10 h-10 rounded-full">
            <div>
              <p class="font-bold text-gray-900">Katy Perry</p>
              <p class="text-xs text-gray-500">1,950 pts</p>
            </div>
          </div>
        </li>
        <li class="px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors">
          <div class="flex items-center gap-4">
            <div class="w-8 h-8 text-gray-400 font-bold flex items-center justify-center">4</div>
            <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="w-10 h-10 rounded-full">
            <div>
              <p class="font-bold text-gray-900">David Miller</p>
              <p class="text-xs text-gray-500">1,820 pts</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_2 = [
    {
        "id": "list-011",
        "title": "Comment List",
        "description": "List of comments with nested replies.",
        "dir": "lists/list-011",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 max-w-2xl w-full p-6">
      <h3 class="text-lg font-bold text-gray-900 mb-6">Discussion (3)</h3>

      <div class="space-y-6">
        <!-- Comment 1 -->
        <div class="flex gap-4">
          <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-1">
            <div class="bg-gray-50 rounded-lg p-4">
              <div class="flex justify-between items-center mb-2">
                <h4 class="font-bold text-gray-900">Samantha Jones</h4>
                <span class="text-xs text-gray-500">2 hours ago</span>
              </div>
              <p class="text-gray-700 text-sm">This is exactly what I was looking for! The design is clean and the code is easy to understand. Great job on this template.</p>
            </div>
            <div class="flex items-center gap-4 mt-2 ml-2">
              <button class="text-xs font-medium text-gray-500 hover:text-blue-600">Like</button>
              <button class="text-xs font-medium text-gray-500 hover:text-blue-600">Reply</button>
            </div>

            <!-- Reply -->
            <div class="flex gap-4 mt-4">
              <img class="w-8 h-8 rounded-full object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="flex-1">
                <div class="bg-gray-50 rounded-lg p-4">
                  <div class="flex justify-between items-center mb-2">
                    <h4 class="font-bold text-gray-900">Alex Smith</h4>
                    <span class="text-xs text-gray-500">1 hour ago</span>
                  </div>
                  <p class="text-gray-700 text-sm">Glad you like it, Samantha! Let me know if you have any questions.</p>
                </div>
                <div class="flex items-center gap-4 mt-2 ml-2">
                  <button class="text-xs font-medium text-gray-500 hover:text-blue-600">Like</button>
                  <button class="text-xs font-medium text-gray-500 hover:text-blue-600">Reply</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Comment 2 -->
        <div class="flex gap-4">
          <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-1">
            <div class="bg-gray-50 rounded-lg p-4">
              <div class="flex justify-between items-center mb-2">
                <h4 class="font-bold text-gray-900">Michael Brown</h4>
                <span class="text-xs text-gray-500">5 hours ago</span>
              </div>
              <p class="text-gray-700 text-sm">Does this support dark mode out of the box? I'm trying to integrate it into my existing project.</p>
            </div>
            <div class="flex items-center gap-4 mt-2 ml-2">
              <button class="text-xs font-medium text-gray-500 hover:text-blue-600">Like</button>
              <button class="text-xs font-medium text-gray-500 hover:text-blue-600">Reply</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-012",
        "title": "Kanban List",
        "description": "Draggable task list card.",
        "dir": "lists/list-012",
        "content": """
  <div class="min-h-screen bg-blue-50 flex items-center justify-center p-4">
    <div class="bg-gray-100 rounded-xl p-4 w-80 shadow-md">
      <div class="flex justify-between items-center mb-4">
        <h3 class="font-bold text-gray-700">In Progress</h3>
        <span class="bg-gray-200 text-gray-600 text-xs font-bold px-2 py-1 rounded">3</span>
      </div>

      <div class="space-y-3">
        <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
          <div class="flex justify-between items-start mb-2">
            <span class="bg-red-100 text-red-800 text-[10px] font-bold px-2 py-0.5 rounded-full">High</span>
            <button class="text-gray-400 hover:text-gray-600">•••</button>
          </div>
          <p class="text-sm font-medium text-gray-800 mb-3">Fix navigation bug on mobile devices</p>
          <div class="flex justify-between items-center">
            <div class="flex -space-x-2">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </div>
            <div class="flex items-center text-gray-400 text-xs gap-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              <span>2</span>
            </div>
          </div>
        </div>

        <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
          <div class="flex justify-between items-start mb-2">
            <span class="bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-0.5 rounded-full">Design</span>
            <button class="text-gray-400 hover:text-gray-600">•••</button>
          </div>
          <p class="text-sm font-medium text-gray-800 mb-3">Create new icons for dashboard</p>
          <div class="flex justify-between items-center">
            <div class="flex -space-x-2">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </div>
            <div class="flex items-center text-gray-400 text-xs gap-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              <span>5</span>
            </div>
          </div>
        </div>

        <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
          <div class="flex justify-between items-start mb-2">
            <span class="bg-green-100 text-green-800 text-[10px] font-bold px-2 py-0.5 rounded-full">Low</span>
            <button class="text-gray-400 hover:text-gray-600">•••</button>
          </div>
          <p class="text-sm font-medium text-gray-800 mb-3">Update documentation</p>
          <div class="flex justify-between items-center">
            <div class="flex -space-x-2">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </div>
            <div class="flex items-center text-gray-400 text-xs gap-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              <span>0</span>
            </div>
          </div>
        </div>
      </div>

      <button class="w-full mt-4 py-2 flex items-center justify-center gap-2 text-gray-500 hover:bg-gray-200 rounded-lg transition-colors text-sm font-medium">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Add Task
      </button>
    </div>
  </div>"""
    },
    {
        "id": "list-013",
        "title": "Transaction List",
        "description": "Financial transaction history.",
        "dir": "lists/list-013",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 max-w-md w-full overflow-hidden">
      <div class="px-6 py-5 border-b border-gray-100 flex justify-between items-center">
        <h3 class="font-bold text-gray-900">Recent Transactions</h3>
        <button class="text-blue-600 text-sm font-medium hover:underline">View All</button>
      </div>

      <ul class="divide-y divide-gray-100">
        <li class="px-6 py-4 hover:bg-gray-50 transition-colors flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 rounded-full bg-orange-100 flex items-center justify-center text-orange-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
              </svg>
            </div>
            <div>
              <p class="font-bold text-gray-900">Amazon Purchase</p>
              <p class="text-xs text-gray-500">Shopping • Today, 2:30 PM</p>
            </div>
          </div>
          <span class="font-bold text-gray-900">-$129.00</span>
        </li>

        <li class="px-6 py-4 hover:bg-gray-50 transition-colors flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <p class="font-bold text-gray-900">Salary Deposit</p>
              <p class="text-xs text-gray-500">Income • Yesterday</p>
            </div>
          </div>
          <span class="font-bold text-green-600">+$3,450.00</span>
        </li>

        <li class="px-6 py-4 hover:bg-gray-50 transition-colors flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <div>
              <p class="font-bold text-gray-900">Electric Bill</p>
              <p class="text-xs text-gray-500">Utilities • Oct 24</p>
            </div>
          </div>
          <span class="font-bold text-gray-900">-$85.20</span>
        </li>

        <li class="px-6 py-4 hover:bg-gray-50 transition-colors flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 rounded-full bg-purple-100 flex items-center justify-center text-purple-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
            </div>
            <div>
              <p class="font-bold text-gray-900">Rent Payment</p>
              <p class="text-xs text-gray-500">Housing • Oct 01</p>
            </div>
          </div>
          <span class="font-bold text-gray-900">-$1,200.00</span>
        </li>
      </ul>
    </div>
  </div>"""
    },
    {
        "id": "list-014",
        "title": "Article List",
        "description": "Blog post list with thumbnails.",
        "dir": "lists/list-014",
        "content": """
  <div class="min-h-screen bg-white flex items-center justify-center p-4">
    <div class="max-w-2xl w-full">
      <div class="flex justify-between items-end mb-8 border-b border-gray-100 pb-4">
        <h2 class="text-3xl font-bold text-gray-900">Latest Stories</h2>
        <a href="#" class="text-indigo-600 font-medium hover:text-indigo-800">View all</a>
      </div>

      <div class="space-y-8">
        <article class="flex gap-6 group cursor-pointer">
          <div class="w-1/3 overflow-hidden rounded-lg">
            <img src="https://images.unsplash.com/photo-1496128858413-b36217c2ce36?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="w-full h-32 object-cover transform group-hover:scale-105 transition-transform duration-300">
          </div>
          <div class="w-2/3 flex flex-col justify-center">
            <div class="flex items-center gap-2 mb-2">
              <span class="text-xs font-bold text-indigo-600 uppercase tracking-wide">Technology</span>
              <span class="text-gray-300">•</span>
              <span class="text-xs text-gray-500">Oct 24, 2023</span>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">The Future of AI in Web Development</h3>
            <p class="text-gray-600 text-sm line-clamp-2">Artificial Intelligence is revolutionizing how we build and interact with the web. Here's what you need to know to stay ahead.</p>
          </div>
        </article>

        <article class="flex gap-6 group cursor-pointer">
          <div class="w-1/3 overflow-hidden rounded-lg">
            <img src="https://images.unsplash.com/photo-1547586696-ea22b4d4235d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="w-full h-32 object-cover transform group-hover:scale-105 transition-transform duration-300">
          </div>
          <div class="w-2/3 flex flex-col justify-center">
            <div class="flex items-center gap-2 mb-2">
              <span class="text-xs font-bold text-pink-600 uppercase tracking-wide">Design</span>
              <span class="text-gray-300">•</span>
              <span class="text-xs text-gray-500">Oct 22, 2023</span>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-pink-600 transition-colors">10 UI Trends to Watch in 2024</h3>
            <p class="text-gray-600 text-sm line-clamp-2">From glassmorphism to neo-brutalism, we explore the visual styles that will define the next year of digital product design.</p>
          </div>
        </article>

        <article class="flex gap-6 group cursor-pointer">
          <div class="w-1/3 overflow-hidden rounded-lg">
            <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="w-full h-32 object-cover transform group-hover:scale-105 transition-transform duration-300">
          </div>
          <div class="w-2/3 flex flex-col justify-center">
            <div class="flex items-center gap-2 mb-2">
              <span class="text-xs font-bold text-green-600 uppercase tracking-wide">Business</span>
              <span class="text-gray-300">•</span>
              <span class="text-xs text-gray-500">Oct 20, 2023</span>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-green-600 transition-colors">Scaling Your Startup: Lessons Learned</h3>
            <p class="text-gray-600 text-sm line-clamp-2">We interviewed 50 founders about their biggest challenges and successes when growing from seed to Series A.</p>
          </div>
        </article>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-015",
        "title": "Settings List",
        "description": "Settings menu with toggles.",
        "dir": "lists/list-015",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 max-w-md w-full overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-100">
        <h3 class="font-bold text-gray-900">Privacy Settings</h3>
        <p class="text-sm text-gray-500">Manage how your data is shared.</p>
      </div>

      <div class="divide-y divide-gray-100">
        <div class="px-6 py-4 flex items-center justify-between">
          <div>
            <p class="font-medium text-gray-900">Profile Visibility</p>
            <p class="text-xs text-gray-500 max-w-[200px]">Allow others to find your profile in search results.</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer" checked>
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="px-6 py-4 flex items-center justify-between">
          <div>
            <p class="font-medium text-gray-900">Activity Status</p>
            <p class="text-xs text-gray-500 max-w-[200px]">Show when you are active on the platform.</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer" checked>
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="px-6 py-4 flex items-center justify-between">
          <div>
            <p class="font-medium text-gray-900">Read Receipts</p>
            <p class="text-xs text-gray-500 max-w-[200px]">Let others know when you've seen their messages.</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="px-6 py-4 flex items-center justify-between">
          <div>
            <p class="font-medium text-gray-900">Data Sharing</p>
            <p class="text-xs text-gray-500 max-w-[200px]">Allow sharing usage data to improve the service.</p>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-016",
        "title": "FAQ List",
        "description": "Accordion style FAQ list.",
        "dir": "lists/list-016",
        "content": """
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full">
      <h2 class="text-3xl font-bold text-slate-900 text-center mb-8">Frequently Asked Questions</h2>

      <div class="space-y-4">
        <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-slate-900">How do I reset my password?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500 transform transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="px-6 pb-4 text-slate-600">
            You can reset your password by clicking on the "Forgot Password" link on the login page. We'll send you an email with instructions to create a new one.
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-slate-900">Can I cancel my subscription anytime?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500 transform -rotate-90 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="hidden px-6 pb-4 text-slate-600">
            Yes, you can cancel your subscription at any time from your account settings. You will continue to have access until the end of your current billing period.
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-slate-900">Do you offer a free trial?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500 transform -rotate-90 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="hidden px-6 pb-4 text-slate-600">
            Yes, we offer a 14-day free trial for all new users. No credit card is required to sign up.
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-slate-900">How can I contact support?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500 transform -rotate-90 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="hidden px-6 pb-4 text-slate-600">
            Our support team is available 24/7. You can reach us via email at support@example.com or use the live chat widget in the bottom right corner.
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-017",
        "title": "Ingredient List",
        "description": "Recipe ingredient list.",
        "dir": "lists/list-017",
        "content": """
  <div class="min-h-screen bg-orange-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl max-w-md w-full overflow-hidden">
      <div class="relative h-48">
        <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Pizza" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-6">
          <h2 class="text-2xl font-bold text-white">Homemade Pizza</h2>
        </div>
      </div>

      <div class="p-6">
        <div class="flex justify-between items-center mb-6 text-sm text-gray-500">
          <div class="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>45 mins</span>
          </div>
          <div class="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
            <span>2 servings</span>
          </div>
          <div class="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9c0 .768.293 1.536.879 2.121z" />
            </svg>
            <span>Easy</span>
          </div>
        </div>

        <h3 class="font-bold text-gray-900 mb-4">Ingredients</h3>
        <ul class="space-y-3">
          <li class="flex items-center gap-3">
            <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-orange-500 focus:ring-orange-500">
            <span class="text-gray-700">2 cups all-purpose flour</span>
          </li>
          <li class="flex items-center gap-3">
            <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-orange-500 focus:ring-orange-500">
            <span class="text-gray-700">1 packet instant yeast</span>
          </li>
          <li class="flex items-center gap-3">
            <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-orange-500 focus:ring-orange-500">
            <span class="text-gray-700">1 tsp sugar</span>
          </li>
          <li class="flex items-center gap-3">
            <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-orange-500 focus:ring-orange-500">
            <span class="text-gray-700">1/2 cup tomato sauce</span>
          </li>
          <li class="flex items-center gap-3">
            <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-orange-500 focus:ring-orange-500">
            <span class="text-gray-700">2 cups mozzarella cheese</span>
          </li>
          <li class="flex items-center gap-3">
            <input type="checkbox" class="w-5 h-5 rounded border-gray-300 text-orange-500 focus:ring-orange-500">
            <span class="text-gray-700">Fresh basil leaves</span>
          </li>
        </ul>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-018",
        "title": "Timeline List",
        "description": "Vertical timeline list.",
        "dir": "lists/list-018",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full">
      <h2 class="text-2xl font-bold text-gray-900 mb-8 ml-4">Order Tracking</h2>

      <div class="relative border-l-2 border-gray-200 ml-6 space-y-8">
        <div class="relative pl-8">
          <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-green-500 border-2 border-white shadow"></div>
          <div>
            <h3 class="font-bold text-gray-900 text-lg">Delivered</h3>
            <p class="text-sm text-gray-500 mb-1">Oct 24, 2:30 PM</p>
            <p class="text-gray-600">Package was handed to resident.</p>
          </div>
        </div>

        <div class="relative pl-8">
          <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-gray-200 border-2 border-white shadow"></div>
          <div>
            <h3 class="font-bold text-gray-900 text-lg">Out for Delivery</h3>
            <p class="text-sm text-gray-500 mb-1">Oct 24, 8:15 AM</p>
            <p class="text-gray-600">Driver is on the way to your location.</p>
          </div>
        </div>

        <div class="relative pl-8">
          <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-gray-200 border-2 border-white shadow"></div>
          <div>
            <h3 class="font-bold text-gray-900 text-lg">Arrived at Facility</h3>
            <p class="text-sm text-gray-500 mb-1">Oct 23, 6:45 PM</p>
            <p class="text-gray-600">Package arrived at local distribution center.</p>
          </div>
        </div>

        <div class="relative pl-8">
          <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-gray-200 border-2 border-white shadow"></div>
          <div>
            <h3 class="font-bold text-gray-900 text-lg">Shipped</h3>
            <p class="text-sm text-gray-500 mb-1">Oct 22, 10:00 AM</p>
            <p class="text-gray-600">Package has left the warehouse.</p>
          </div>
        </div>

        <div class="relative pl-8">
          <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-gray-200 border-2 border-white shadow"></div>
          <div>
            <h3 class="font-bold text-gray-900 text-lg">Order Placed</h3>
            <p class="text-sm text-gray-500 mb-1">Oct 21, 3:25 PM</p>
            <p class="text-gray-600">We have received your order.</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-019",
        "title": "Skill List",
        "description": "List of skills with progress bars.",
        "dir": "lists/list-019",
        "content": """
  <div class="min-h-screen bg-slate-900 flex items-center justify-center p-4">
    <div class="bg-slate-800 rounded-xl shadow-2xl max-w-md w-full p-8 border border-slate-700">
      <h3 class="text-2xl font-bold text-white mb-6">Professional Skills</h3>

      <div class="space-y-6">
        <div>
          <div class="flex justify-between items-end mb-2">
            <span class="font-medium text-slate-200">Web Design</span>
            <span class="text-sm text-cyan-400 font-bold">90%</span>
          </div>
          <div class="w-full bg-slate-700 rounded-full h-2.5">
            <div class="bg-cyan-500 h-2.5 rounded-full" style="width: 90%"></div>
          </div>
        </div>

        <div>
          <div class="flex justify-between items-end mb-2">
            <span class="font-medium text-slate-200">HTML/CSS</span>
            <span class="text-sm text-cyan-400 font-bold">95%</span>
          </div>
          <div class="w-full bg-slate-700 rounded-full h-2.5">
            <div class="bg-cyan-500 h-2.5 rounded-full" style="width: 95%"></div>
          </div>
        </div>

        <div>
          <div class="flex justify-between items-end mb-2">
            <span class="font-medium text-slate-200">JavaScript</span>
            <span class="text-sm text-cyan-400 font-bold">85%</span>
          </div>
          <div class="w-full bg-slate-700 rounded-full h-2.5">
            <div class="bg-cyan-500 h-2.5 rounded-full" style="width: 85%"></div>
          </div>
        </div>

        <div>
          <div class="flex justify-between items-end mb-2">
            <span class="font-medium text-slate-200">React</span>
            <span class="text-sm text-cyan-400 font-bold">80%</span>
          </div>
          <div class="w-full bg-slate-700 rounded-full h-2.5">
            <div class="bg-cyan-500 h-2.5 rounded-full" style="width: 80%"></div>
          </div>
        </div>

        <div>
          <div class="flex justify-between items-end mb-2">
            <span class="font-medium text-slate-200">UI/UX</span>
            <span class="text-sm text-cyan-400 font-bold">75%</span>
          </div>
          <div class="w-full bg-slate-700 rounded-full h-2.5">
            <div class="bg-cyan-500 h-2.5 rounded-full" style="width: 75%"></div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-020",
        "title": "Device List",
        "description": "List of connected devices.",
        "dir": "lists/list-020",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 max-w-md w-full overflow-hidden">
      <div class="px-6 py-5 border-b border-gray-100">
        <h3 class="text-xl font-bold text-gray-900">Connected Devices</h3>
        <p class="text-sm text-gray-500">Manage devices logged into your account.</p>
      </div>

      <ul class="divide-y divide-gray-100">
        <li class="px-6 py-4 flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900">MacBook Pro</p>
              <div class="flex items-center gap-2 text-xs text-gray-500">
                <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                <span>Active now • San Francisco, US</span>
              </div>
            </div>
          </div>
        </li>

        <li class="px-6 py-4 flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900">iPhone 13 Pro</p>
              <div class="flex items-center gap-2 text-xs text-gray-500">
                <span>2 hours ago • San Francisco, US</span>
              </div>
            </div>
          </div>
          <button class="text-gray-400 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
          </button>
        </li>

        <li class="px-6 py-4 flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900">iPad Air</p>
              <div class="flex items-center gap-2 text-xs text-gray-500">
                <span>3 days ago • New York, US</span>
              </div>
            </div>
          </div>
          <button class="text-gray-400 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
          </button>
        </li>

        <li class="px-6 py-4 flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900">Windows PC</p>
              <div class="flex items-center gap-2 text-xs text-gray-500">
                <span>1 week ago • London, UK</span>
              </div>
            </div>
          </div>
          <button class="text-gray-400 hover:text-red-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
          </button>
        </li>
      </ul>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_3_PART_1 = [
    {
        "id": "list-021",
        "title": "Event List",
        "description": "List of upcoming events.",
        "dir": "lists/list-021",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-sm overflow-hidden">
      <div class="p-6 border-b border-gray-100 flex justify-between items-center">
        <h2 class="text-xl font-bold text-gray-900">Upcoming Events</h2>
        <button class="text-indigo-600 text-sm font-medium hover:text-indigo-800">View Calendar</button>
      </div>

      <div class="divide-y divide-gray-100">
        <div class="p-6 flex gap-4 hover:bg-gray-50 transition-colors cursor-pointer group">
          <div class="flex-shrink-0 w-16 text-center bg-indigo-50 rounded-lg p-2 group-hover:bg-indigo-100 transition-colors">
            <span class="block text-xs font-bold text-indigo-600 uppercase">Oct</span>
            <span class="block text-2xl font-bold text-gray-900">24</span>
          </div>
          <div>
            <h3 class="font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">Product Launch Party</h3>
            <p class="text-sm text-gray-500 mb-2">6:00 PM • The Grand Hotel</p>
            <div class="flex -space-x-2">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="flex items-center justify-center w-6 h-6 rounded-full border-2 border-white bg-gray-100 text-[10px] font-medium text-gray-500">+12</span>
            </div>
          </div>
        </div>

        <div class="p-6 flex gap-4 hover:bg-gray-50 transition-colors cursor-pointer group">
          <div class="flex-shrink-0 w-16 text-center bg-indigo-50 rounded-lg p-2 group-hover:bg-indigo-100 transition-colors">
            <span class="block text-xs font-bold text-indigo-600 uppercase">Nov</span>
            <span class="block text-2xl font-bold text-gray-900">02</span>
          </div>
          <div>
            <h3 class="font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">Design Workshop</h3>
            <p class="text-sm text-gray-500 mb-2">10:00 AM • Creative Studio</p>
            <div class="flex -space-x-2">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="flex items-center justify-center w-6 h-6 rounded-full border-2 border-white bg-gray-100 text-[10px] font-medium text-gray-500">+5</span>
            </div>
          </div>
        </div>

        <div class="p-6 flex gap-4 hover:bg-gray-50 transition-colors cursor-pointer group">
          <div class="flex-shrink-0 w-16 text-center bg-indigo-50 rounded-lg p-2 group-hover:bg-indigo-100 transition-colors">
            <span class="block text-xs font-bold text-indigo-600 uppercase">Nov</span>
            <span class="block text-2xl font-bold text-gray-900">15</span>
          </div>
          <div>
            <h3 class="font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">Team Building</h3>
            <p class="text-sm text-gray-500 mb-2">9:00 AM • Central Park</p>
            <div class="flex -space-x-2">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="flex items-center justify-center w-6 h-6 rounded-full border-2 border-white bg-gray-100 text-[10px] font-medium text-gray-500">+20</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-022",
        "title": "Message List",
        "description": "Chat message list.",
        "dir": "lists/list-022",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-sm overflow-hidden h-[600px] flex flex-col">
      <div class="p-4 border-b border-gray-100 flex justify-between items-center bg-white sticky top-0 z-10">
        <h2 class="text-lg font-bold text-gray-900">Messages</h2>
        <button class="p-2 hover:bg-gray-100 rounded-full text-gray-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
        </button>
      </div>

      <div class="flex-1 overflow-y-auto">
        <div class="divide-y divide-gray-100">
          <div class="p-4 hover:bg-gray-50 cursor-pointer flex gap-3 relative">
            <div class="relative">
              <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full"></span>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex justify-between items-baseline mb-1">
                <h3 class="font-bold text-gray-900 truncate">Jane Cooper</h3>
                <span class="text-xs text-gray-500">2m ago</span>
              </div>
              <p class="text-sm text-gray-900 font-medium truncate">Hey, are we still on for lunch?</p>
            </div>
            <div class="absolute right-4 top-1/2 transform -translate-y-1/2 w-2 h-2 bg-blue-500 rounded-full"></div>
          </div>

          <div class="p-4 hover:bg-gray-50 cursor-pointer flex gap-3">
            <div class="relative">
              <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="absolute bottom-0 right-0 w-3 h-3 bg-gray-300 border-2 border-white rounded-full"></span>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex justify-between items-baseline mb-1">
                <h3 class="font-bold text-gray-900 truncate">Wade Warren</h3>
                <span class="text-xs text-gray-500">1h ago</span>
              </div>
              <p class="text-sm text-gray-500 truncate">The project files have been updated.</p>
            </div>
          </div>

          <div class="p-4 hover:bg-gray-50 cursor-pointer flex gap-3">
            <div class="relative">
              <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full"></span>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex justify-between items-baseline mb-1">
                <h3 class="font-bold text-gray-900 truncate">Esther Howard</h3>
                <span class="text-xs text-gray-500">3h ago</span>
              </div>
              <p class="text-sm text-gray-500 truncate">Can you send me the latest report?</p>
            </div>
          </div>

          <div class="p-4 hover:bg-gray-50 cursor-pointer flex gap-3">
            <div class="relative">
              <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <span class="absolute bottom-0 right-0 w-3 h-3 bg-gray-300 border-2 border-white rounded-full"></span>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex justify-between items-baseline mb-1">
                <h3 class="font-bold text-gray-900 truncate">Cameron Williamson</h3>
                <span class="text-xs text-gray-500">1d ago</span>
              </div>
              <p class="text-sm text-gray-500 truncate">Thanks for your help yesterday!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-023",
        "title": "Crypto List",
        "description": "Cryptocurrency price list.",
        "dir": "lists/list-023",
        "content": """
  <div class="min-h-screen bg-slate-900 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-slate-800 rounded-xl shadow-2xl overflow-hidden border border-slate-700">
      <div class="p-6 border-b border-slate-700">
        <h2 class="text-xl font-bold text-white">Market</h2>
      </div>

      <div class="divide-y divide-slate-700">
        <div class="p-4 flex items-center justify-between hover:bg-slate-700/50 transition-colors cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-orange-500 rounded-full flex items-center justify-center text-white font-bold">₿</div>
            <div>
              <h3 class="font-bold text-white">Bitcoin</h3>
              <p class="text-xs text-slate-400">BTC</p>
            </div>
          </div>
          <div class="text-right">
            <p class="font-bold text-white">$34,250.00</p>
            <p class="text-xs text-green-400">+2.4%</p>
          </div>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-slate-700/50 transition-colors cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-indigo-500 rounded-full flex items-center justify-center text-white font-bold">Ξ</div>
            <div>
              <h3 class="font-bold text-white">Ethereum</h3>
              <p class="text-xs text-slate-400">ETH</p>
            </div>
          </div>
          <div class="text-right">
            <p class="font-bold text-white">$1,850.00</p>
            <p class="text-xs text-green-400">+1.8%</p>
          </div>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-slate-700/50 transition-colors cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold">S</div>
            <div>
              <h3 class="font-bold text-white">Solana</h3>
              <p class="text-xs text-slate-400">SOL</p>
            </div>
          </div>
          <div class="text-right">
            <p class="font-bold text-white">$32.40</p>
            <p class="text-xs text-red-400">-0.5%</p>
          </div>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-slate-700/50 transition-colors cursor-pointer">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-pink-500 rounded-full flex items-center justify-center text-white font-bold">P</div>
            <div>
              <h3 class="font-bold text-white">Polkadot</h3>
              <p class="text-xs text-slate-400">DOT</p>
            </div>
          </div>
          <div class="text-right">
            <p class="font-bold text-white">$4.20</p>
            <p class="text-xs text-green-400">+5.2%</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-024",
        "title": "Video List",
        "description": "Video playlist with thumbnails.",
        "dir": "lists/list-024",
        "content": """
  <div class="min-h-screen bg-gray-900 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full bg-gray-800 rounded-xl shadow-2xl overflow-hidden border border-gray-700 flex flex-col md:flex-row">
      <!-- Main Video Area (Placeholder) -->
      <div class="md:w-2/3 bg-black p-4 flex items-center justify-center min-h-[300px]">
        <div class="text-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 text-gray-600 mx-auto mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-gray-500">Select a video to play</p>
        </div>
      </div>

      <!-- Playlist -->
      <div class="md:w-1/3 border-l border-gray-700 flex flex-col h-[500px]">
        <div class="p-4 border-b border-gray-700 bg-gray-800">
          <h3 class="font-bold text-white">Up Next</h3>
        </div>

        <div class="flex-1 overflow-y-auto">
          <div class="divide-y divide-gray-700">
            <div class="p-3 hover:bg-gray-700/50 cursor-pointer flex gap-3 group">
              <div class="relative w-24 h-16 flex-shrink-0">
                <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=60" alt="" class="w-full h-full object-cover rounded">
                <span class="absolute bottom-1 right-1 bg-black/80 text-white text-[10px] px-1 rounded">12:45</span>
              </div>
              <div>
                <h4 class="text-sm font-bold text-white line-clamp-2 group-hover:text-blue-400 transition-colors">Amazing Mountain Landscapes 4K</h4>
                <p class="text-xs text-gray-400 mt-1">Nature Channel</p>
              </div>
            </div>

            <div class="p-3 hover:bg-gray-700/50 cursor-pointer flex gap-3 group">
              <div class="relative w-24 h-16 flex-shrink-0">
                <img src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=60" alt="" class="w-full h-full object-cover rounded">
                <span class="absolute bottom-1 right-1 bg-black/80 text-white text-[10px] px-1 rounded">8:30</span>
              </div>
              <div>
                <h4 class="text-sm font-bold text-white line-clamp-2 group-hover:text-blue-400 transition-colors">Morning Yoga Routine for Beginners</h4>
                <p class="text-xs text-gray-400 mt-1">Wellness Daily</p>
              </div>
            </div>

            <div class="p-3 hover:bg-gray-700/50 cursor-pointer flex gap-3 group">
              <div class="relative w-24 h-16 flex-shrink-0">
                <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=60" alt="" class="w-full h-full object-cover rounded">
                <span class="absolute bottom-1 right-1 bg-black/80 text-white text-[10px] px-1 rounded">15:20</span>
              </div>
              <div>
                <h4 class="text-sm font-bold text-white line-clamp-2 group-hover:text-blue-400 transition-colors">Productivity Hacks for Remote Workers</h4>
                <p class="text-xs text-gray-400 mt-1">Work Smart</p>
              </div>
            </div>

            <div class="p-3 hover:bg-gray-700/50 cursor-pointer flex gap-3 group">
              <div class="relative w-24 h-16 flex-shrink-0">
                <img src="https://images.unsplash.com/photo-1493770348161-369560ae357d?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=60" alt="" class="w-full h-full object-cover rounded">
                <span class="absolute bottom-1 right-1 bg-black/80 text-white text-[10px] px-1 rounded">10:15</span>
              </div>
              <div>
                <h4 class="text-sm font-bold text-white line-clamp-2 group-hover:text-blue-400 transition-colors">Healthy Breakfast Ideas</h4>
                <p class="text-xs text-gray-400 mt-1">Foodie Life</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-025",
        "title": "Review List",
        "description": "Customer reviews with stars.",
        "dir": "lists/list-025",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100 flex items-center gap-4">
        <div class="text-4xl font-bold text-gray-900">4.8</div>
        <div>
          <div class="flex text-yellow-400 mb-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
          </div>
          <p class="text-sm text-gray-500">Based on 128 reviews</p>
        </div>
      </div>

      <div class="divide-y divide-gray-100">
        <div class="p-6">
          <div class="flex justify-between items-start mb-2">
            <div class="flex items-center gap-3">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div>
                <h4 class="font-bold text-gray-900">Joseph McFall</h4>
                <div class="flex text-yellow-400 text-xs">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
            </div>
            <span class="text-xs text-gray-500">3 days ago</span>
          </div>
          <p class="text-gray-600 text-sm">Absolutely love this product! It has completely transformed how I work. The interface is intuitive and the features are exactly what I needed.</p>
        </div>

        <div class="p-6">
          <div class="flex justify-between items-start mb-2">
            <div class="flex items-center gap-3">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div>
                <h4 class="font-bold text-gray-900">Sarah Wilson</h4>
                <div class="flex text-yellow-400 text-xs">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
            </div>
            <span class="text-xs text-gray-500">1 week ago</span>
          </div>
          <p class="text-gray-600 text-sm">Great value for money. The customer support team was also very helpful when I had questions during setup.</p>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_3_PART_2 = [
    {
        "id": "list-026",
        "title": "Job List",
        "description": "Job listing with tags.",
        "dir": "lists/list-026",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-3xl w-full">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-900">Open Positions</h2>
        <span class="bg-gray-200 text-gray-700 text-xs font-bold px-2 py-1 rounded-full">12 Available</span>
      </div>

      <div class="space-y-4">
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow cursor-pointer">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center text-indigo-600 flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-900">Senior Frontend Developer</h3>
                <p class="text-gray-500 text-sm mb-2">Engineering • Remote</p>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-blue-50 text-blue-700 text-xs px-2 py-1 rounded border border-blue-100">React</span>
                  <span class="bg-blue-50 text-blue-700 text-xs px-2 py-1 rounded border border-blue-100">TypeScript</span>
                  <span class="bg-blue-50 text-blue-700 text-xs px-2 py-1 rounded border border-blue-100">Tailwind CSS</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-4 md:flex-col md:items-end">
              <span class="text-gray-900 font-bold">$120k - $160k</span>
              <span class="text-xs text-gray-500">Posted 2 days ago</span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow cursor-pointer">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-900">Product Designer</h3>
                <p class="text-gray-500 text-sm mb-2">Design • New York, NY</p>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-purple-50 text-purple-700 text-xs px-2 py-1 rounded border border-purple-100">Figma</span>
                  <span class="bg-purple-50 text-purple-700 text-xs px-2 py-1 rounded border border-purple-100">UI/UX</span>
                  <span class="bg-purple-50 text-purple-700 text-xs px-2 py-1 rounded border border-purple-100">Prototyping</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-4 md:flex-col md:items-end">
              <span class="text-gray-900 font-bold">$100k - $140k</span>
              <span class="text-xs text-gray-500">Posted 1 week ago</span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow cursor-pointer">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center text-green-600 flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-900">Marketing Manager</h3>
                <p class="text-gray-500 text-sm mb-2">Marketing • London, UK</p>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-green-50 text-green-700 text-xs px-2 py-1 rounded border border-green-100">SEO</span>
                  <span class="bg-green-50 text-green-700 text-xs px-2 py-1 rounded border border-green-100">Content</span>
                  <span class="bg-green-50 text-green-700 text-xs px-2 py-1 rounded border border-green-100">Social Media</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-4 md:flex-col md:items-end">
              <span class="text-gray-900 font-bold">$80k - $110k</span>
              <span class="text-xs text-gray-500">Posted 3 days ago</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-027",
        "title": "Gallery List",
        "description": "Image gallery list.",
        "dir": "lists/list-027",
        "content": """
  <div class="min-h-screen bg-black flex items-center justify-center p-4">
    <div class="max-w-4xl w-full">
      <h2 class="text-2xl font-bold text-white mb-6">My Collection</h2>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <div class="group relative aspect-square overflow-hidden rounded-lg bg-gray-800 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1516035069371-29a1b244cc32?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <div class="text-center">
              <p class="text-white font-bold">Camera Lens</p>
              <p class="text-gray-300 text-xs">Photography</p>
            </div>
          </div>
        </div>

        <div class="group relative aspect-square overflow-hidden rounded-lg bg-gray-800 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1550684848-fac1c5b4e853?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <div class="text-center">
              <p class="text-white font-bold">Retro Vibes</p>
              <p class="text-gray-300 text-xs">Abstract</p>
            </div>
          </div>
        </div>

        <div class="group relative aspect-square overflow-hidden rounded-lg bg-gray-800 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1558655146-d09347e92766?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <div class="text-center">
              <p class="text-white font-bold">Workspace</p>
              <p class="text-gray-300 text-xs">Lifestyle</p>
            </div>
          </div>
        </div>

        <div class="group relative aspect-square overflow-hidden rounded-lg bg-gray-800 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <div class="text-center">
              <p class="text-white font-bold">Portrait</p>
              <p class="text-gray-300 text-xs">People</p>
            </div>
          </div>
        </div>

        <div class="group relative aspect-square overflow-hidden rounded-lg bg-gray-800 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="" class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110">
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <div class="text-center">
              <p class="text-white font-bold">Landscape</p>
              <p class="text-gray-300 text-xs">Nature</p>
            </div>
          </div>
        </div>

        <div class="group relative aspect-square overflow-hidden rounded-lg bg-gray-800 cursor-pointer flex items-center justify-center border-2 border-dashed border-gray-700 hover:border-gray-500 hover:bg-gray-800/50 transition-colors">
          <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-gray-500 mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
            <p class="text-gray-500 font-medium">Add New</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-028",
        "title": "Download List",
        "description": "List of downloadable items.",
        "dir": "lists/list-028",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100">
        <h2 class="text-xl font-bold text-gray-900">Downloads</h2>
        <p class="text-sm text-gray-500">Your purchased digital assets.</p>
      </div>

      <div class="divide-y divide-gray-100">
        <div class="p-4 hover:bg-gray-50 flex items-center justify-between group">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-gray-900 text-sm">UI Kit Bundle.zip</h3>
              <p class="text-xs text-gray-500">128 MB • Purchased today</p>
            </div>
          </div>
          <button class="text-gray-400 hover:text-blue-600 p-2 rounded-full hover:bg-blue-50 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </button>
        </div>

        <div class="p-4 hover:bg-gray-50 flex items-center justify-between group">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-gray-900 text-sm">Icon Pack v2.0.zip</h3>
              <p class="text-xs text-gray-500">45 MB • Purchased yesterday</p>
            </div>
          </div>
          <button class="text-gray-400 hover:text-purple-600 p-2 rounded-full hover:bg-purple-50 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </button>
        </div>

        <div class="p-4 hover:bg-gray-50 flex items-center justify-between group">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center text-green-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-gray-900 text-sm">Stock Photos.zip</h3>
              <p class="text-xs text-gray-500">1.2 GB • Purchased last week</p>
            </div>
          </div>
          <button class="text-gray-400 hover:text-green-600 p-2 rounded-full hover:bg-green-50 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </button>
        </div>

        <div class="p-4 hover:bg-gray-50 flex items-center justify-between group">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center text-red-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-gray-900 text-sm">Invoice #1024.pdf</h3>
              <p class="text-xs text-gray-500">245 KB • Purchased last month</p>
            </div>
          </div>
          <button class="text-gray-400 hover:text-red-600 p-2 rounded-full hover:bg-red-50 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-029",
        "title": "Integration List",
        "description": "List of app integrations.",
        "dir": "lists/list-029",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full">
      <h2 class="text-2xl font-bold text-gray-900 mb-6">Integrations</h2>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200 flex items-start justify-between">
          <div class="flex gap-4">
            <div class="w-12 h-12 bg-blue-500 rounded-lg flex items-center justify-center text-white font-bold text-xl">S</div>
            <div>
              <h3 class="font-bold text-gray-900">Stripe</h3>
              <p class="text-sm text-gray-500 mb-3">Payments infrastructure for the internet.</p>
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                <span class="text-xs font-medium text-green-600">Connected</span>
              </div>
            </div>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer" checked>
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200 flex items-start justify-between">
          <div class="flex gap-4">
            <div class="w-12 h-12 bg-black rounded-lg flex items-center justify-center text-white font-bold text-xl">N</div>
            <div>
              <h3 class="font-bold text-gray-900">Notion</h3>
              <p class="text-sm text-gray-500 mb-3">All-in-one workspace for your team.</p>
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 bg-gray-300 rounded-full"></span>
                <span class="text-xs font-medium text-gray-500">Disconnected</span>
              </div>
            </div>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200 flex items-start justify-between">
          <div class="flex gap-4">
            <div class="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center text-white font-bold text-xl">S</div>
            <div>
              <h3 class="font-bold text-gray-900">Slack</h3>
              <p class="text-sm text-gray-500 mb-3">Team communication and collaboration.</p>
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                <span class="text-xs font-medium text-green-600">Connected</span>
              </div>
            </div>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer" checked>
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200 flex items-start justify-between">
          <div class="flex gap-4">
            <div class="w-12 h-12 bg-orange-500 rounded-lg flex items-center justify-center text-white font-bold text-xl">Z</div>
            <div>
              <h3 class="font-bold text-gray-900">Zapier</h3>
              <p class="text-sm text-gray-500 mb-3">Connect your apps and automate workflows.</p>
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 bg-gray-300 rounded-full"></span>
                <span class="text-xs font-medium text-gray-500">Disconnected</span>
              </div>
            </div>
          </div>
          <label class="relative inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
          </label>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-030",
        "title": "History List",
        "description": "Activity history list.",
        "dir": "lists/list-030",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100">
        <h2 class="text-xl font-bold text-gray-900">Activity History</h2>
      </div>

      <div class="p-6">
        <div class="relative border-l border-gray-200 ml-3 space-y-8">
          <div class="relative pl-8">
            <div class="absolute -left-[5px] top-1 w-2.5 h-2.5 rounded-full bg-blue-500 ring-4 ring-white"></div>
            <p class="text-sm text-gray-500 mb-1">Just now</p>
            <h3 class="text-gray-900 font-bold">Updated profile picture</h3>
            <p class="text-gray-600 text-sm mt-1">Changed profile photo from default to custom upload.</p>
          </div>

          <div class="relative pl-8">
            <div class="absolute -left-[5px] top-1 w-2.5 h-2.5 rounded-full bg-gray-300 ring-4 ring-white"></div>
            <p class="text-sm text-gray-500 mb-1">2 hours ago</p>
            <h3 class="text-gray-900 font-bold">Created new project</h3>
            <p class="text-gray-600 text-sm mt-1">Started "Website Redesign" project with 3 team members.</p>
          </div>

          <div class="relative pl-8">
            <div class="absolute -left-[5px] top-1 w-2.5 h-2.5 rounded-full bg-gray-300 ring-4 ring-white"></div>
            <p class="text-sm text-gray-500 mb-1">Yesterday</p>
            <h3 class="text-gray-900 font-bold">Completed task</h3>
            <p class="text-gray-600 text-sm mt-1">Marked "Design System" task as complete.</p>
          </div>

          <div class="relative pl-8">
            <div class="absolute -left-[5px] top-1 w-2.5 h-2.5 rounded-full bg-gray-300 ring-4 ring-white"></div>
            <p class="text-sm text-gray-500 mb-1">Oct 24</p>
            <h3 class="text-gray-900 font-bold">Joined team</h3>
            <p class="text-gray-600 text-sm mt-1">Accepted invitation to join "Engineering" team.</p>
          </div>

          <div class="relative pl-8">
            <div class="absolute -left-[5px] top-1 w-2.5 h-2.5 rounded-full bg-gray-300 ring-4 ring-white"></div>
            <p class="text-sm text-gray-500 mb-1">Oct 20</p>
            <h3 class="text-gray-900 font-bold">Account created</h3>
            <p class="text-gray-600 text-sm mt-1">Signed up for a new account.</p>
          </div>
        </div>
      </div>

      <div class="bg-gray-50 p-4 text-center border-t border-gray-100">
        <button class="text-sm font-medium text-gray-600 hover:text-gray-900">Load more activity</button>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_4_PART_1 = [
    {
        "id": "list-031",
        "title": "Contact List",
        "description": "Contact list with alphabet index.",
        "dir": "lists/list-031",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden flex h-[600px]">
      <div class="flex-1 overflow-y-auto">
        <div class="p-4 border-b border-gray-100 bg-white sticky top-0 z-10">
          <h2 class="text-xl font-bold text-gray-900">Contacts</h2>
          <div class="mt-2 relative">
            <input type="text" placeholder="Search" class="w-full bg-gray-100 border-none rounded-lg py-2 pl-10 pr-4 text-sm focus:ring-2 focus:ring-blue-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
        </div>

        <div>
          <div class="bg-gray-50 px-4 py-1 text-xs font-bold text-gray-500 sticky top-[73px]">A</div>
          <div class="divide-y divide-gray-100">
            <div class="p-4 flex items-center gap-3 hover:bg-gray-50 cursor-pointer">
              <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold">AB</div>
              <div>
                <h3 class="font-bold text-gray-900">Alice Brown</h3>
                <p class="text-xs text-gray-500">alice@example.com</p>
              </div>
            </div>
            <div class="p-4 flex items-center gap-3 hover:bg-gray-50 cursor-pointer">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div>
                <h3 class="font-bold text-gray-900">Andrew Smith</h3>
                <p class="text-xs text-gray-500">andrew@example.com</p>
              </div>
            </div>
          </div>

          <div class="bg-gray-50 px-4 py-1 text-xs font-bold text-gray-500 sticky top-[73px]">B</div>
          <div class="divide-y divide-gray-100">
            <div class="p-4 flex items-center gap-3 hover:bg-gray-50 cursor-pointer">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div>
                <h3 class="font-bold text-gray-900">Bob Johnson</h3>
                <p class="text-xs text-gray-500">bob@example.com</p>
              </div>
            </div>
            <div class="p-4 flex items-center gap-3 hover:bg-gray-50 cursor-pointer">
              <div class="w-10 h-10 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-bold">BW</div>
              <div>
                <h3 class="font-bold text-gray-900">Brian Wilson</h3>
                <p class="text-xs text-gray-500">brian@example.com</p>
              </div>
            </div>
          </div>

          <div class="bg-gray-50 px-4 py-1 text-xs font-bold text-gray-500 sticky top-[73px]">C</div>
          <div class="divide-y divide-gray-100">
            <div class="p-4 flex items-center gap-3 hover:bg-gray-50 cursor-pointer">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div>
                <h3 class="font-bold text-gray-900">Catherine Lee</h3>
                <p class="text-xs text-gray-500">catherine@example.com</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="w-6 bg-gray-50 border-l border-gray-200 flex flex-col items-center justify-center text-[10px] font-bold text-gray-500 gap-1 cursor-pointer">
        <span class="hover:text-blue-600">A</span>
        <span class="hover:text-blue-600">B</span>
        <span class="hover:text-blue-600">C</span>
        <span class="hover:text-blue-600">D</span>
        <span class="hover:text-blue-600">E</span>
        <span class="hover:text-blue-600">F</span>
        <span class="hover:text-blue-600">G</span>
        <span class="hover:text-blue-600">H</span>
        <span class="hover:text-blue-600">I</span>
        <span class="hover:text-blue-600">J</span>
        <span class="hover:text-blue-600">K</span>
        <span class="hover:text-blue-600">L</span>
        <span class="hover:text-blue-600">M</span>
        <span class="hover:text-blue-600">N</span>
        <span class="hover:text-blue-600">O</span>
        <span class="hover:text-blue-600">P</span>
        <span class="hover:text-blue-600">Q</span>
        <span class="hover:text-blue-600">R</span>
        <span class="hover:text-blue-600">S</span>
        <span class="hover:text-blue-600">T</span>
        <span class="hover:text-blue-600">U</span>
        <span class="hover:text-blue-600">V</span>
        <span class="hover:text-blue-600">W</span>
        <span class="hover:text-blue-600">X</span>
        <span class="hover:text-blue-600">Y</span>
        <span class="hover:text-blue-600">Z</span>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-032",
        "title": "Task List",
        "description": "Task list with drag handles.",
        "dir": "lists/list-032",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg overflow-hidden">
      <div class="p-6 bg-indigo-600 text-white flex justify-between items-center">
        <div>
          <h2 class="text-xl font-bold">Today's Tasks</h2>
          <p class="text-indigo-200 text-sm">5 tasks remaining</p>
        </div>
        <button class="bg-indigo-500 hover:bg-indigo-400 p-2 rounded-lg transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
        </button>
      </div>

      <div class="p-4 space-y-2">
        <div class="bg-white border border-gray-200 rounded-lg p-3 flex items-center gap-3 shadow-sm hover:shadow-md transition-shadow cursor-move group">
          <div class="text-gray-300 cursor-move">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <input type="checkbox" class="rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
              <span class="font-medium text-gray-900">Review PR #1024</span>
            </div>
          </div>
          <span class="bg-red-100 text-red-800 text-xs font-bold px-2 py-1 rounded">High</span>
        </div>

        <div class="bg-white border border-gray-200 rounded-lg p-3 flex items-center gap-3 shadow-sm hover:shadow-md transition-shadow cursor-move group">
          <div class="text-gray-300 cursor-move">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <input type="checkbox" class="rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
              <span class="font-medium text-gray-900">Update documentation</span>
            </div>
          </div>
          <span class="bg-yellow-100 text-yellow-800 text-xs font-bold px-2 py-1 rounded">Medium</span>
        </div>

        <div class="bg-white border border-gray-200 rounded-lg p-3 flex items-center gap-3 shadow-sm hover:shadow-md transition-shadow cursor-move group">
          <div class="text-gray-300 cursor-move">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <input type="checkbox" class="rounded text-indigo-600 focus:ring-indigo-500 border-gray-300" checked>
              <span class="font-medium text-gray-400 line-through">Team meeting</span>
            </div>
          </div>
          <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-1 rounded">Done</span>
        </div>

        <div class="bg-white border border-gray-200 rounded-lg p-3 flex items-center gap-3 shadow-sm hover:shadow-md transition-shadow cursor-move group">
          <div class="text-gray-300 cursor-move">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <input type="checkbox" class="rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
              <span class="font-medium text-gray-900">Email client</span>
            </div>
          </div>
          <span class="bg-blue-100 text-blue-800 text-xs font-bold px-2 py-1 rounded">Low</span>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-033",
        "title": "Notification List",
        "description": "Notification list with actions.",
        "dir": "lists/list-033",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100 flex justify-between items-center">
        <h2 class="text-xl font-bold text-gray-900">Notifications</h2>
        <button class="text-blue-600 text-sm font-medium hover:text-blue-800">Mark all as read</button>
      </div>

      <div class="divide-y divide-gray-100">
        <div class="p-4 bg-blue-50/50 hover:bg-blue-50 transition-colors">
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-blue-600 rounded-full"></div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-900"><span class="font-bold">Sarah</span> commented on your post.</p>
              <p class="text-xs text-gray-500 mt-1">2 minutes ago</p>
              <div class="mt-2 flex gap-2">
                <button class="text-xs bg-white border border-gray-300 px-3 py-1 rounded-md hover:bg-gray-50 font-medium">Reply</button>
                <button class="text-xs text-gray-500 hover:text-gray-700 font-medium">Dismiss</button>
              </div>
            </div>
          </div>
        </div>

        <div class="p-4 bg-blue-50/50 hover:bg-blue-50 transition-colors">
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-blue-600 rounded-full"></div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-900"><span class="font-bold">System</span> update completed successfully.</p>
              <p class="text-xs text-gray-500 mt-1">1 hour ago</p>
            </div>
          </div>
        </div>

        <div class="p-4 hover:bg-gray-50 transition-colors">
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-transparent rounded-full"></div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-600"><span class="font-bold text-gray-900">Mike</span> invited you to <span class="font-bold text-gray-900">Project X</span>.</p>
              <p class="text-xs text-gray-500 mt-1">Yesterday</p>
              <div class="mt-2 flex gap-2">
                <button class="text-xs bg-blue-600 text-white px-3 py-1 rounded-md hover:bg-blue-700 font-medium">Accept</button>
                <button class="text-xs bg-white border border-gray-300 px-3 py-1 rounded-md hover:bg-gray-50 font-medium">Decline</button>
              </div>
            </div>
          </div>
        </div>

        <div class="p-4 hover:bg-gray-50 transition-colors">
          <div class="flex gap-3">
            <div class="mt-1">
              <div class="w-2 h-2 bg-transparent rounded-full"></div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-600"><span class="font-bold text-gray-900">Anna</span> liked your photo.</p>
              <p class="text-xs text-gray-500 mt-1">2 days ago</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-034",
        "title": "Feature List",
        "description": "Feature comparison list.",
        "dir": "lists/list-034",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-8 text-center border-b border-gray-100">
        <h2 class="text-2xl font-bold text-gray-900">Compare Plans</h2>
        <p class="text-gray-500 mt-2">Choose the plan that fits your needs.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-gray-100">
        <div class="p-6">
          <h3 class="text-lg font-bold text-gray-900 text-center mb-4">Basic</h3>
          <ul class="space-y-4">
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-600">1 User</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-600">5 Projects</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-300 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-400">Analytics</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-300 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-400">Priority Support</span>
            </li>
          </ul>
          <button class="w-full mt-6 bg-gray-100 text-gray-900 font-bold py-2 rounded-lg hover:bg-gray-200 transition-colors">Select Basic</button>
        </div>

        <div class="p-6 bg-blue-50/30">
          <h3 class="text-lg font-bold text-blue-600 text-center mb-4">Pro</h3>
          <ul class="space-y-4">
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-900 font-medium">5 Users</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-900 font-medium">Unlimited Projects</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-900 font-medium">Analytics</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-300 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-400">Priority Support</span>
            </li>
          </ul>
          <button class="w-full mt-6 bg-blue-600 text-white font-bold py-2 rounded-lg hover:bg-blue-700 transition-colors shadow-sm">Select Pro</button>
        </div>

        <div class="p-6">
          <h3 class="text-lg font-bold text-gray-900 text-center mb-4">Enterprise</h3>
          <ul class="space-y-4">
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-600">Unlimited Users</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-600">Unlimited Projects</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-600">Advanced Analytics</span>
            </li>
            <li class="flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm text-gray-600">Priority Support</span>
            </li>
          </ul>
          <button class="w-full mt-6 bg-gray-900 text-white font-bold py-2 rounded-lg hover:bg-gray-800 transition-colors">Contact Sales</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-035",
        "title": "Order List",
        "description": "Order history list.",
        "dir": "lists/list-035",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-3xl w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100 flex justify-between items-center">
        <h2 class="text-xl font-bold text-gray-900">Order History</h2>
        <div class="flex gap-2">
          <select class="text-sm border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500">
            <option>Last 30 days</option>
            <option>Last 3 months</option>
            <option>2023</option>
          </select>
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left">
          <thead>
            <tr class="bg-gray-50 text-gray-500 text-xs uppercase">
              <th class="px-6 py-3 font-medium">Order ID</th>
              <th class="px-6 py-3 font-medium">Date</th>
              <th class="px-6 py-3 font-medium">Status</th>
              <th class="px-6 py-3 font-medium">Total</th>
              <th class="px-6 py-3 font-medium"></th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr class="hover:bg-gray-50">
              <td class="px-6 py-4 font-medium text-gray-900">#ORD-7352</td>
              <td class="px-6 py-4 text-gray-500">Oct 24, 2023</td>
              <td class="px-6 py-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                  Delivered
                </span>
              </td>
              <td class="px-6 py-4 text-gray-900 font-medium">$120.50</td>
              <td class="px-6 py-4 text-right">
                <button class="text-indigo-600 hover:text-indigo-900 text-sm font-medium">View</button>
              </td>
            </tr>

            <tr class="hover:bg-gray-50">
              <td class="px-6 py-4 font-medium text-gray-900">#ORD-7351</td>
              <td class="px-6 py-4 text-gray-500">Oct 21, 2023</td>
              <td class="px-6 py-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                  Shipped
                </span>
              </td>
              <td class="px-6 py-4 text-gray-900 font-medium">$85.00</td>
              <td class="px-6 py-4 text-right">
                <button class="text-indigo-600 hover:text-indigo-900 text-sm font-medium">View</button>
              </td>
            </tr>

            <tr class="hover:bg-gray-50">
              <td class="px-6 py-4 font-medium text-gray-900">#ORD-7350</td>
              <td class="px-6 py-4 text-gray-500">Oct 15, 2023</td>
              <td class="px-6 py-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">
                  Processing
                </span>
              </td>
              <td class="px-6 py-4 text-gray-900 font-medium">$210.25</td>
              <td class="px-6 py-4 text-right">
                <button class="text-indigo-600 hover:text-indigo-900 text-sm font-medium">View</button>
              </td>
            </tr>

            <tr class="hover:bg-gray-50">
              <td class="px-6 py-4 font-medium text-gray-900">#ORD-7349</td>
              <td class="px-6 py-4 text-gray-500">Oct 10, 2023</td>
              <td class="px-6 py-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                  Cancelled
                </span>
              </td>
              <td class="px-6 py-4 text-gray-900 font-medium">$45.00</td>
              <td class="px-6 py-4 text-right">
                <button class="text-indigo-600 hover:text-indigo-900 text-sm font-medium">View</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_4_PART_2 = [
    {
        "id": "list-036",
        "title": "Comment List",
        "description": "Comment thread list.",
        "dir": "lists/list-036",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100">
        <h2 class="text-xl font-bold text-gray-900">Comments (12)</h2>
      </div>

      <div class="p-6 space-y-6">
        <div class="flex gap-4">
          <img class="w-10 h-10 rounded-full object-cover flex-shrink-0" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-1">
            <div class="bg-gray-50 p-4 rounded-lg rounded-tl-none">
              <div class="flex justify-between items-baseline mb-2">
                <h3 class="font-bold text-gray-900">Mark Johnson</h3>
                <span class="text-xs text-gray-500">2 hours ago</span>
              </div>
              <p class="text-gray-600 text-sm">This is exactly what I was looking for! The design is clean and the code is easy to understand. Great job!</p>
            </div>
            <div class="flex gap-4 mt-2 ml-2">
              <button class="text-xs font-medium text-gray-500 hover:text-gray-900">Like</button>
              <button class="text-xs font-medium text-gray-500 hover:text-gray-900">Reply</button>
            </div>

            <div class="mt-4 flex gap-4">
              <img class="w-8 h-8 rounded-full object-cover flex-shrink-0" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="flex-1">
                <div class="bg-gray-50 p-3 rounded-lg rounded-tl-none">
                  <div class="flex justify-between items-baseline mb-2">
                    <h3 class="font-bold text-gray-900 text-sm">Emily Davis</h3>
                    <span class="text-xs text-gray-500">1 hour ago</span>
                  </div>
                  <p class="text-gray-600 text-sm">I agree! It saved me so much time.</p>
                </div>
                <div class="flex gap-4 mt-2 ml-2">
                  <button class="text-xs font-medium text-gray-500 hover:text-gray-900">Like</button>
                  <button class="text-xs font-medium text-gray-500 hover:text-gray-900">Reply</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="flex gap-4">
          <img class="w-10 h-10 rounded-full object-cover flex-shrink-0" src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-1">
            <div class="bg-gray-50 p-4 rounded-lg rounded-tl-none">
              <div class="flex justify-between items-baseline mb-2">
                <h3 class="font-bold text-gray-900">David Wilson</h3>
                <span class="text-xs text-gray-500">5 hours ago</span>
              </div>
              <p class="text-gray-600 text-sm">Is there a dark mode version available? I'd love to use this in my project but I need dark mode support.</p>
            </div>
            <div class="flex gap-4 mt-2 ml-2">
              <button class="text-xs font-medium text-gray-500 hover:text-gray-900">Like</button>
              <button class="text-xs font-medium text-gray-500 hover:text-gray-900">Reply</button>
            </div>
          </div>
        </div>
      </div>

      <div class="p-6 border-t border-gray-100 bg-gray-50">
        <div class="flex gap-4">
          <img class="w-10 h-10 rounded-full object-cover flex-shrink-0" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-1">
            <textarea rows="3" class="w-full border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500 text-sm" placeholder="Write a comment..."></textarea>
            <div class="mt-2 flex justify-end">
              <button class="bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700 transition-colors">Post Comment</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-037",
        "title": "FAQ List",
        "description": "FAQ list with accordion.",
        "dir": "lists/list-037",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full">
      <h2 class="text-3xl font-bold text-gray-900 text-center mb-8">Frequently Asked Questions</h2>

      <div class="space-y-4">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-gray-900">How do I get started?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 transform transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="px-6 pb-4 text-gray-600 text-sm">
            Getting started is easy! Simply sign up for an account, choose a plan, and you'll have instant access to all our features. We also offer a comprehensive guide to help you set up your first project.
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-gray-900">Can I cancel my subscription?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 transform transition-transform duration-200 -rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="px-6 pb-4 text-gray-600 text-sm hidden">
            Yes, you can cancel your subscription at any time. There are no long-term contracts or cancellation fees. Your access will continue until the end of your current billing period.
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-gray-900">Do you offer customer support?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 transform transition-transform duration-200 -rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="px-6 pb-4 text-gray-600 text-sm hidden">
            Absolutely! Our dedicated support team is available 24/7 to assist you with any questions or issues you may have. You can reach us via email, chat, or phone.
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
          <button class="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none">
            <span class="font-bold text-gray-900">Is my data secure?</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 transform transition-transform duration-200 -rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div class="px-6 pb-4 text-gray-600 text-sm hidden">
            Security is our top priority. We use industry-standard encryption to protect your data and ensure that it remains private and secure. We also perform regular security audits.
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-038",
        "title": "Team List",
        "description": "Team member list with roles.",
        "dir": "lists/list-038",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full">
      <div class="text-center mb-10">
        <h2 class="text-3xl font-bold text-gray-900">Meet Our Team</h2>
        <p class="text-gray-500 mt-2">The talented people behind the product.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden text-center p-6 hover:shadow-md transition-shadow">
          <img class="w-24 h-24 rounded-full object-cover mx-auto mb-4" src="https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <h3 class="font-bold text-gray-900 text-lg">James Wilson</h3>
          <p class="text-indigo-600 font-medium text-sm mb-3">CEO & Founder</p>
          <p class="text-gray-500 text-sm mb-4">Visionary leader with 15+ years of experience in tech.</p>
          <div class="flex justify-center gap-3">
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden text-center p-6 hover:shadow-md transition-shadow">
          <img class="w-24 h-24 rounded-full object-cover mx-auto mb-4" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <h3 class="font-bold text-gray-900 text-lg">Sarah Chen</h3>
          <p class="text-indigo-600 font-medium text-sm mb-3">CTO</p>
          <p class="text-gray-500 text-sm mb-4">Tech enthusiast with a passion for building scalable systems.</p>
          <div class="flex justify-center gap-3">
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden text-center p-6 hover:shadow-md transition-shadow">
          <img class="w-24 h-24 rounded-full object-cover mx-auto mb-4" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <h3 class="font-bold text-gray-900 text-lg">Michael Brown</h3>
          <p class="text-indigo-600 font-medium text-sm mb-3">Lead Designer</p>
          <p class="text-gray-500 text-sm mb-4">Creative mind behind our beautiful and intuitive designs.</p>
          <div class="flex justify-center gap-3">
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden text-center p-6 hover:shadow-md transition-shadow">
          <img class="w-24 h-24 rounded-full object-cover mx-auto mb-4" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <h3 class="font-bold text-gray-900 text-lg">Emily Davis</h3>
          <p class="text-indigo-600 font-medium text-sm mb-3">Marketing Head</p>
          <p class="text-gray-500 text-sm mb-4">Marketing guru with a knack for storytelling and growth.</p>
          <div class="flex justify-center gap-3">
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">Twitter</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-600">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" /></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-039",
        "title": "Article List",
        "description": "Article list with categories.",
        "dir": "lists/list-039",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-3xl w-full">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-900">Latest Articles</h2>
        <a href="#" class="text-indigo-600 font-medium hover:text-indigo-800">View All</a>
      </div>

      <div class="space-y-6">
        <article class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow flex flex-col md:flex-row">
          <div class="md:w-1/3 h-48 md:h-auto relative">
            <img class="w-full h-full object-cover" src="https://images.unsplash.com/photo-1496128858413-b36217c2ce36?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="">
            <span class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-indigo-600">Technology</span>
          </div>
          <div class="p-6 md:w-2/3 flex flex-col justify-between">
            <div>
              <h3 class="text-xl font-bold text-gray-900 mb-2 hover:text-indigo-600 cursor-pointer">The Future of Artificial Intelligence</h3>
              <p class="text-gray-600 text-sm line-clamp-2 mb-4">Artificial Intelligence is rapidly evolving and changing the way we live and work. In this article, we explore the latest trends and predictions for the future of AI.</p>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <img class="w-6 h-6 rounded-full object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="text-xs text-gray-500 font-medium">Tom Cook</span>
              </div>
              <span class="text-xs text-gray-400">5 min read</span>
            </div>
          </div>
        </article>

        <article class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow flex flex-col md:flex-row">
          <div class="md:w-1/3 h-48 md:h-auto relative">
            <img class="w-full h-full object-cover" src="https://images.unsplash.com/photo-1547586696-ea22b4d4235d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="">
            <span class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-green-600">Design</span>
          </div>
          <div class="p-6 md:w-2/3 flex flex-col justify-between">
            <div>
              <h3 class="text-xl font-bold text-gray-900 mb-2 hover:text-indigo-600 cursor-pointer">10 Tips for Better UI Design</h3>
              <p class="text-gray-600 text-sm line-clamp-2 mb-4">Good UI design is essential for creating a great user experience. Here are 10 tips to help you improve your UI design skills and create better products.</p>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <img class="w-6 h-6 rounded-full object-cover" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="text-xs text-gray-500 font-medium">Jane Doe</span>
              </div>
              <span class="text-xs text-gray-400">3 min read</span>
            </div>
          </div>
        </article>

        <article class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow flex flex-col md:flex-row">
          <div class="md:w-1/3 h-48 md:h-auto relative">
            <img class="w-full h-full object-cover" src="https://images.unsplash.com/photo-1492724441997-cd780d836cd8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="">
            <span class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-orange-600">Lifestyle</span>
          </div>
          <div class="p-6 md:w-2/3 flex flex-col justify-between">
            <div>
              <h3 class="text-xl font-bold text-gray-900 mb-2 hover:text-indigo-600 cursor-pointer">Finding Balance in a Busy World</h3>
              <p class="text-gray-600 text-sm line-clamp-2 mb-4">In today's fast-paced world, it can be difficult to find balance. We share some practical tips and strategies to help you achieve a healthier work-life balance.</p>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <img class="w-6 h-6 rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="text-xs text-gray-500 font-medium">Mark Smith</span>
              </div>
              <span class="text-xs text-gray-400">7 min read</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-040",
        "title": "Music List",
        "description": "Music track list with playback controls.",
        "dir": "lists/list-040",
        "content": """
  <div class="min-h-screen bg-gray-900 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-gray-800 rounded-xl shadow-2xl overflow-hidden border border-gray-700">
      <div class="p-6 border-b border-gray-700 bg-gradient-to-r from-indigo-900 to-purple-900">
        <div class="flex gap-4 items-center">
          <img class="w-20 h-20 rounded-lg shadow-lg" src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=60" alt="">
          <div>
            <h2 class="text-xl font-bold text-white">Midnight Vibes</h2>
            <p class="text-indigo-200 text-sm">Curated by Spotify</p>
            <div class="flex gap-2 mt-2">
              <button class="bg-green-500 text-black rounded-full p-2 hover:bg-green-400 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                </svg>
              </button>
              <button class="border border-gray-400 text-white rounded-full p-2 hover:bg-white/10 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="divide-y divide-gray-700">
        <div class="p-4 flex items-center justify-between hover:bg-gray-700/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <span class="text-gray-500 w-4 text-center group-hover:hidden">1</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white hidden group-hover:block" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
            <div>
              <h3 class="font-bold text-white text-sm group-hover:text-green-400 transition-colors">Night Drive</h3>
              <p class="text-xs text-gray-400">Synthwave Boy</p>
            </div>
          </div>
          <span class="text-xs text-gray-500">3:45</span>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-gray-700/50 transition-colors group cursor-pointer bg-gray-700/30">
          <div class="flex items-center gap-4">
            <img src="https://i.gifer.com/origin/3f/3fcf565ccc553afcfd89858c97304705.gif" class="w-4 h-4" alt="playing">
            <div>
              <h3 class="font-bold text-green-400 text-sm">Neon Lights</h3>
              <p class="text-xs text-gray-400">Retro Future</p>
            </div>
          </div>
          <span class="text-xs text-gray-500">4:12</span>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-gray-700/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <span class="text-gray-500 w-4 text-center group-hover:hidden">3</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white hidden group-hover:block" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
            <div>
              <h3 class="font-bold text-white text-sm group-hover:text-green-400 transition-colors">Cyber City</h3>
              <p class="text-xs text-gray-400">Digital Dreams</p>
            </div>
          </div>
          <span class="text-xs text-gray-500">3:28</span>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-gray-700/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <span class="text-gray-500 w-4 text-center group-hover:hidden">4</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white hidden group-hover:block" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
            <div>
              <h3 class="font-bold text-white text-sm group-hover:text-green-400 transition-colors">Starship</h3>
              <p class="text-xs text-gray-400">Galactic Sound</p>
            </div>
          </div>
          <span class="text-xs text-gray-500">5:01</span>
        </div>

        <div class="p-4 flex items-center justify-between hover:bg-gray-700/50 transition-colors group cursor-pointer">
          <div class="flex items-center gap-4">
            <span class="text-gray-500 w-4 text-center group-hover:hidden">5</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white hidden group-hover:block" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
            <div>
              <h3 class="font-bold text-white text-sm group-hover:text-green-400 transition-colors">Lost in Time</h3>
              <p class="text-xs text-gray-400">Time Traveler</p>
            </div>
          </div>
          <span class="text-xs text-gray-500">4:15</span>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_5_PART_1 = [
    {
        "id": "list-041",
        "title": "Recipe List",
        "description": "Recipe list with cooking time.",
        "dir": "lists/list-041",
        "content": """
  <div class="min-h-screen bg-orange-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg overflow-hidden">
      <div class="p-6 bg-orange-500 text-white">
        <h2 class="text-2xl font-bold">Popular Recipes</h2>
        <p class="text-orange-100 text-sm">Curated for you</p>
      </div>

      <div class="divide-y divide-gray-100">
        <div class="p-4 flex gap-4 hover:bg-orange-50 transition-colors cursor-pointer group">
          <img class="w-20 h-20 rounded-lg object-cover shadow-sm group-hover:shadow-md transition-shadow" src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=60" alt="">
          <div class="flex-1">
            <h3 class="font-bold text-gray-900 group-hover:text-orange-600 transition-colors">Classic Margherita Pizza</h3>
            <div class="flex items-center gap-4 mt-2 text-xs text-gray-500">
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                45 min
              </span>
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                4.8
              </span>
            </div>
            <span class="inline-block mt-2 px-2 py-1 bg-green-100 text-green-800 text-[10px] font-bold rounded-full">Vegetarian</span>
          </div>
        </div>

        <div class="p-4 flex gap-4 hover:bg-orange-50 transition-colors cursor-pointer group">
          <img class="w-20 h-20 rounded-lg object-cover shadow-sm group-hover:shadow-md transition-shadow" src="https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=60" alt="">
          <div class="flex-1">
            <h3 class="font-bold text-gray-900 group-hover:text-orange-600 transition-colors">Buttermilk Pancakes</h3>
            <div class="flex items-center gap-4 mt-2 text-xs text-gray-500">
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                25 min
              </span>
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                4.9
              </span>
            </div>
            <span class="inline-block mt-2 px-2 py-1 bg-yellow-100 text-yellow-800 text-[10px] font-bold rounded-full">Breakfast</span>
          </div>
        </div>

        <div class="p-4 flex gap-4 hover:bg-orange-50 transition-colors cursor-pointer group">
          <img class="w-20 h-20 rounded-lg object-cover shadow-sm group-hover:shadow-md transition-shadow" src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=60" alt="">
          <div class="flex-1">
            <h3 class="font-bold text-gray-900 group-hover:text-orange-600 transition-colors">Healthy Green Salad</h3>
            <div class="flex items-center gap-4 mt-2 text-xs text-gray-500">
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                15 min
              </span>
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                4.5
              </span>
            </div>
            <span class="inline-block mt-2 px-2 py-1 bg-green-100 text-green-800 text-[10px] font-bold rounded-full">Vegan</span>
          </div>
        </div>

        <div class="p-4 flex gap-4 hover:bg-orange-50 transition-colors cursor-pointer group">
          <img class="w-20 h-20 rounded-lg object-cover shadow-sm group-hover:shadow-md transition-shadow" src="https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=60" alt="">
          <div class="flex-1">
            <h3 class="font-bold text-gray-900 group-hover:text-orange-600 transition-colors">Chocolate Cake</h3>
            <div class="flex items-center gap-4 mt-2 text-xs text-gray-500">
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                60 min
              </span>
              <span class="flex items-center gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                4.9
              </span>
            </div>
            <span class="inline-block mt-2 px-2 py-1 bg-purple-100 text-purple-800 text-[10px] font-bold rounded-full">Dessert</span>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-042",
        "title": "Course List",
        "description": "Course list with progress.",
        "dir": "lists/list-042",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-3xl w-full">
      <h2 class="text-2xl font-bold text-gray-900 mb-6">My Courses</h2>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
          <div class="h-32 bg-blue-600 relative">
            <div class="absolute inset-0 bg-gradient-to-br from-blue-600 to-indigo-700"></div>
            <div class="absolute bottom-4 left-4 text-white">
              <span class="text-xs font-bold bg-white/20 px-2 py-1 rounded mb-2 inline-block">Development</span>
              <h3 class="text-lg font-bold">Advanced React Patterns</h3>
            </div>
          </div>
          <div class="p-6">
            <div class="flex justify-between items-center mb-2 text-sm text-gray-500">
              <span>Progress</span>
              <span class="font-bold text-blue-600">75%</span>
            </div>
            <div class="w-full bg-gray-100 rounded-full h-2 mb-4">
              <div class="bg-blue-600 h-2 rounded-full" style="width: 75%"></div>
            </div>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">+12</span>
              </div>
              <button class="text-blue-600 font-bold text-sm hover:underline">Continue</button>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
          <div class="h-32 bg-purple-600 relative">
            <div class="absolute inset-0 bg-gradient-to-br from-purple-600 to-pink-600"></div>
            <div class="absolute bottom-4 left-4 text-white">
              <span class="text-xs font-bold bg-white/20 px-2 py-1 rounded mb-2 inline-block">Design</span>
              <h3 class="text-lg font-bold">UI/UX Fundamentals</h3>
            </div>
          </div>
          <div class="p-6">
            <div class="flex justify-between items-center mb-2 text-sm text-gray-500">
              <span>Progress</span>
              <span class="font-bold text-purple-600">30%</span>
            </div>
            <div class="w-full bg-gray-100 rounded-full h-2 mb-4">
              <div class="bg-purple-600 h-2 rounded-full" style="width: 30%"></div>
            </div>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">+5</span>
              </div>
              <button class="text-purple-600 font-bold text-sm hover:underline">Continue</button>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
          <div class="h-32 bg-green-600 relative">
            <div class="absolute inset-0 bg-gradient-to-br from-green-600 to-teal-600"></div>
            <div class="absolute bottom-4 left-4 text-white">
              <span class="text-xs font-bold bg-white/20 px-2 py-1 rounded mb-2 inline-block">Business</span>
              <h3 class="text-lg font-bold">Product Management</h3>
            </div>
          </div>
          <div class="p-6">
            <div class="flex justify-between items-center mb-2 text-sm text-gray-500">
              <span>Progress</span>
              <span class="font-bold text-green-600">10%</span>
            </div>
            <div class="w-full bg-gray-100 rounded-full h-2 mb-4">
              <div class="bg-green-600 h-2 rounded-full" style="width: 10%"></div>
            </div>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">+8</span>
              </div>
              <button class="text-green-600 font-bold text-sm hover:underline">Continue</button>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
          <div class="h-32 bg-orange-600 relative">
            <div class="absolute inset-0 bg-gradient-to-br from-orange-600 to-red-600"></div>
            <div class="absolute bottom-4 left-4 text-white">
              <span class="text-xs font-bold bg-white/20 px-2 py-1 rounded mb-2 inline-block">Marketing</span>
              <h3 class="text-lg font-bold">Digital Marketing 101</h3>
            </div>
          </div>
          <div class="p-6">
            <div class="flex justify-between items-center mb-2 text-sm text-gray-500">
              <span>Progress</span>
              <span class="font-bold text-orange-600">0%</span>
            </div>
            <div class="w-full bg-gray-100 rounded-full h-2 mb-4">
              <div class="bg-orange-600 h-2 rounded-full" style="width: 0%"></div>
            </div>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">0</span>
              </div>
              <button class="text-orange-600 font-bold text-sm hover:underline">Start</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-043",
        "title": "File List",
        "description": "File manager list view.",
        "dir": "lists/list-043",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      <div class="p-6 border-b border-gray-100 flex justify-between items-center">
        <div class="flex items-center gap-2 text-gray-500 text-sm">
          <span class="hover:text-blue-600 cursor-pointer">Home</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
          <span class="hover:text-blue-600 cursor-pointer">Documents</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
          <span class="font-bold text-gray-900">Projects</span>
        </div>
        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Upload
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-sm">
          <thead>
            <tr class="bg-gray-50 text-gray-500 border-b border-gray-100">
              <th class="px-6 py-3 font-medium w-1/2">Name</th>
              <th class="px-6 py-3 font-medium">Size</th>
              <th class="px-6 py-3 font-medium">Modified</th>
              <th class="px-6 py-3 font-medium text-right">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr class="hover:bg-gray-50 group cursor-pointer">
              <td class="px-6 py-4">
                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-yellow-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M2 6a2 2 0 012-2h4l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clip-rule="evenodd" />
                  </svg>
                  <span class="font-medium text-gray-900">Design Assets</span>
                </div>
              </td>
              <td class="px-6 py-4 text-gray-500">-</td>
              <td class="px-6 py-4 text-gray-500">Oct 24, 2023</td>
              <td class="px-6 py-4 text-right">
                <button class="text-gray-400 hover:text-gray-600 opacity-0 group-hover:opacity-100 transition-opacity">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                  </svg>
                </button>
              </td>
            </tr>

            <tr class="hover:bg-gray-50 group cursor-pointer">
              <td class="px-6 py-4">
                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                  </svg>
                  <span class="font-medium text-gray-900">Project Proposal.docx</span>
                </div>
              </td>
              <td class="px-6 py-4 text-gray-500">2.4 MB</td>
              <td class="px-6 py-4 text-gray-500">Oct 22, 2023</td>
              <td class="px-6 py-4 text-right">
                <button class="text-gray-400 hover:text-gray-600 opacity-0 group-hover:opacity-100 transition-opacity">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                  </svg>
                </button>
              </td>
            </tr>

            <tr class="hover:bg-gray-50 group cursor-pointer">
              <td class="px-6 py-4">
                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                  </svg>
                  <span class="font-medium text-gray-900">Budget Q4.pdf</span>
                </div>
              </td>
              <td class="px-6 py-4 text-gray-500">1.8 MB</td>
              <td class="px-6 py-4 text-gray-500">Oct 20, 2023</td>
              <td class="px-6 py-4 text-right">
                <button class="text-gray-400 hover:text-gray-600 opacity-0 group-hover:opacity-100 transition-opacity">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                  </svg>
                </button>
              </td>
            </tr>

            <tr class="hover:bg-gray-50 group cursor-pointer">
              <td class="px-6 py-4">
                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-green-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                  </svg>
                  <span class="font-medium text-gray-900">Financials.xlsx</span>
                </div>
              </td>
              <td class="px-6 py-4 text-gray-500">560 KB</td>
              <td class="px-6 py-4 text-gray-500">Oct 18, 2023</td>
              <td class="px-6 py-4 text-right">
                <button class="text-gray-400 hover:text-gray-600 opacity-0 group-hover:opacity-100 transition-opacity">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-044",
        "title": "Chat List",
        "description": "Chat conversation list.",
        "dir": "lists/list-044",
        "content": """
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg overflow-hidden h-[600px] flex flex-col">
      <div class="p-4 bg-indigo-600 text-white flex justify-between items-center">
        <div class="flex items-center gap-3">
          <div class="relative">
            <img class="w-10 h-10 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <span class="absolute bottom-0 right-0 w-3 h-3 bg-green-400 border-2 border-indigo-600 rounded-full"></span>
          </div>
          <div>
            <h2 class="font-bold">Alice Smith</h2>
            <p class="text-indigo-200 text-xs">Online</p>
          </div>
        </div>
        <div class="flex gap-2">
          <button class="p-2 hover:bg-indigo-500 rounded-full transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
          </button>
          <button class="p-2 hover:bg-indigo-500 rounded-full transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
          </button>
        </div>
      </div>

      <div class="flex-1 bg-gray-50 p-4 overflow-y-auto space-y-4">
        <div class="flex justify-center">
          <span class="bg-gray-200 text-gray-500 text-xs px-2 py-1 rounded-full">Today</span>
        </div>

        <div class="flex gap-3">
          <img class="w-8 h-8 rounded-full self-end mb-1" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="max-w-[80%]">
            <div class="bg-white p-3 rounded-2xl rounded-bl-none shadow-sm text-sm text-gray-800">
              Hey! How's the project coming along?
            </div>
            <p class="text-[10px] text-gray-400 mt-1 ml-1">10:30 AM</p>
          </div>
        </div>

        <div class="flex gap-3 flex-row-reverse">
          <div class="max-w-[80%]">
            <div class="bg-indigo-600 p-3 rounded-2xl rounded-br-none shadow-sm text-sm text-white">
              It's going great! Just finishing up the last few components.
            </div>
            <p class="text-[10px] text-gray-400 mt-1 mr-1 text-right">10:32 AM</p>
          </div>
        </div>

        <div class="flex gap-3">
          <img class="w-8 h-8 rounded-full self-end mb-1" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="max-w-[80%]">
            <div class="bg-white p-3 rounded-2xl rounded-bl-none shadow-sm text-sm text-gray-800">
              That's awesome! Can you send me a preview?
            </div>
            <p class="text-[10px] text-gray-400 mt-1 ml-1">10:33 AM</p>
          </div>
        </div>

        <div class="flex gap-3 flex-row-reverse">
          <div class="max-w-[80%]">
            <div class="bg-indigo-600 p-3 rounded-2xl rounded-br-none shadow-sm text-sm text-white">
              Sure thing! Sending it over now.
            </div>
            <div class="bg-indigo-600 p-3 rounded-2xl rounded-tr-none shadow-sm text-sm text-white mt-1">
              <div class="flex items-center gap-3 bg-indigo-700/50 p-2 rounded-lg">
                <div class="bg-white/20 p-2 rounded">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
                <div class="flex-1 min-w-0">
                  <p class="font-medium truncate">preview_v1.png</p>
                  <p class="text-xs opacity-70">2.4 MB</p>
                </div>
              </div>
            </div>
            <p class="text-[10px] text-gray-400 mt-1 mr-1 text-right">10:35 AM</p>
          </div>
        </div>

        <div class="flex gap-3">
          <img class="w-8 h-8 rounded-full self-end mb-1" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="max-w-[80%]">
            <div class="bg-white p-3 rounded-2xl rounded-bl-none shadow-sm text-sm text-gray-800">
              <div class="flex gap-1">
                <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
                <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-100"></span>
                <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-200"></span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="p-4 bg-white border-t border-gray-100">
        <div class="flex gap-2">
          <button class="text-gray-400 hover:text-gray-600 p-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
            </svg>
          </button>
          <input type="text" placeholder="Type a message..." class="flex-1 bg-gray-100 border-none rounded-full px-4 py-2 focus:ring-2 focus:ring-indigo-500">
          <button class="bg-indigo-600 text-white p-2 rounded-full hover:bg-indigo-700 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-045",
        "title": "Timeline List",
        "description": "Vertical timeline list.",
        "dir": "lists/list-045",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-2xl w-full">
      <h2 class="text-2xl font-bold text-gray-900 mb-8 text-center">Project Timeline</h2>

      <div class="relative border-l-2 border-indigo-200 ml-3 md:ml-0 md:mx-auto space-y-8 md:space-y-0">
        <div class="relative md:flex items-center justify-between md:gap-8 group">
          <div class="absolute -left-[9px] top-0 md:static md:w-4 md:h-4 md:bg-indigo-600 md:rounded-full md:border-4 md:border-white md:shadow md:flex-shrink-0 z-10">
            <div class="w-4 h-4 bg-indigo-600 rounded-full border-4 border-white shadow md:hidden"></div>
          </div>

          <div class="ml-6 md:ml-0 md:w-[45%] md:text-right">
            <span class="text-sm font-bold text-indigo-600 bg-indigo-50 px-2 py-1 rounded">Phase 1</span>
            <h3 class="text-lg font-bold text-gray-900 mt-1">Project Kickoff</h3>
            <p class="text-gray-500 text-sm mt-2">Initial meeting with stakeholders to define project scope, goals, and timeline.</p>
            <span class="text-xs text-gray-400 mt-2 block">Oct 1, 2023</span>
          </div>

          <div class="hidden md:block w-[10%]"></div>
          <div class="md:w-[45%]"></div>
        </div>

        <div class="relative md:flex items-center justify-between md:gap-8 group">
          <div class="absolute -left-[9px] top-0 md:static md:order-2 md:w-4 md:h-4 md:bg-indigo-600 md:rounded-full md:border-4 md:border-white md:shadow md:flex-shrink-0 z-10">
            <div class="w-4 h-4 bg-indigo-600 rounded-full border-4 border-white shadow md:hidden"></div>
          </div>

          <div class="md:w-[45%] md:order-1"></div>

          <div class="ml-6 md:ml-0 md:w-[45%] md:order-3">
            <span class="text-sm font-bold text-indigo-600 bg-indigo-50 px-2 py-1 rounded">Phase 2</span>
            <h3 class="text-lg font-bold text-gray-900 mt-1">Design & Prototyping</h3>
            <p class="text-gray-500 text-sm mt-2">Creating wireframes, high-fidelity mockups, and interactive prototypes for user testing.</p>
            <span class="text-xs text-gray-400 mt-2 block">Oct 15, 2023</span>
          </div>
        </div>

        <div class="relative md:flex items-center justify-between md:gap-8 group">
          <div class="absolute -left-[9px] top-0 md:static md:w-4 md:h-4 md:bg-indigo-600 md:rounded-full md:border-4 md:border-white md:shadow md:flex-shrink-0 z-10">
            <div class="w-4 h-4 bg-indigo-600 rounded-full border-4 border-white shadow md:hidden"></div>
          </div>

          <div class="ml-6 md:ml-0 md:w-[45%] md:text-right">
            <span class="text-sm font-bold text-indigo-600 bg-indigo-50 px-2 py-1 rounded">Phase 3</span>
            <h3 class="text-lg font-bold text-gray-900 mt-1">Development</h3>
            <p class="text-gray-500 text-sm mt-2">Frontend and backend development, API integration, and database setup.</p>
            <span class="text-xs text-gray-400 mt-2 block">Nov 1, 2023</span>
          </div>

          <div class="hidden md:block w-[10%]"></div>
          <div class="md:w-[45%]"></div>
        </div>

        <div class="relative md:flex items-center justify-between md:gap-8 group">
          <div class="absolute -left-[9px] top-0 md:static md:order-2 md:w-4 md:h-4 md:bg-gray-300 md:rounded-full md:border-4 md:border-white md:shadow md:flex-shrink-0 z-10">
            <div class="w-4 h-4 bg-gray-300 rounded-full border-4 border-white shadow md:hidden"></div>
          </div>

          <div class="md:w-[45%] md:order-1"></div>

          <div class="ml-6 md:ml-0 md:w-[45%] md:order-3">
            <span class="text-sm font-bold text-gray-500 bg-gray-100 px-2 py-1 rounded">Phase 4</span>
            <h3 class="text-lg font-bold text-gray-500 mt-1">Testing & QA</h3>
            <p class="text-gray-400 text-sm mt-2">Comprehensive testing, bug fixing, and performance optimization.</p>
            <span class="text-xs text-gray-400 mt-2 block">Dec 1, 2023</span>
          </div>
        </div>

        <div class="relative md:flex items-center justify-between md:gap-8 group">
          <div class="absolute -left-[9px] top-0 md:static md:w-4 md:h-4 md:bg-gray-300 md:rounded-full md:border-4 md:border-white md:shadow md:flex-shrink-0 z-10">
            <div class="w-4 h-4 bg-gray-300 rounded-full border-4 border-white shadow md:hidden"></div>
          </div>

          <div class="ml-6 md:ml-0 md:w-[45%] md:text-right">
            <span class="text-sm font-bold text-gray-500 bg-gray-100 px-2 py-1 rounded">Phase 5</span>
            <h3 class="text-lg font-bold text-gray-500 mt-1">Launch</h3>
            <p class="text-gray-400 text-sm mt-2">Official product launch and marketing campaign rollout.</p>
            <span class="text-xs text-gray-400 mt-2 block">Jan 1, 2024</span>
          </div>

          <div class="hidden md:block w-[10%]"></div>
          <div class="md:w-[45%]"></div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_5_PART_2 = [
    {
        "id": "list-046",
        "title": "Kanban List",
        "description": "Kanban board list.",
        "dir": "lists/list-046",
        "content": """
  <div class="min-h-screen bg-blue-50 flex items-center justify-center p-4 overflow-x-auto">
    <div class="flex gap-6 h-[600px]">
      <div class="w-80 flex flex-col bg-gray-100 rounded-xl p-4">
        <div class="flex justify-between items-center mb-4">
          <h3 class="font-bold text-gray-700">To Do</h3>
          <span class="bg-gray-200 text-gray-600 text-xs font-bold px-2 py-1 rounded-full">3</span>
        </div>

        <div class="flex-1 overflow-y-auto space-y-3">
          <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
            <span class="bg-red-100 text-red-800 text-[10px] font-bold px-2 py-1 rounded mb-2 inline-block">High Priority</span>
            <h4 class="font-bold text-gray-900 text-sm mb-2">Research competitors</h4>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
              <div class="flex items-center text-gray-400 text-xs gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <span>Oct 25</span>
              </div>
            </div>
          </div>

          <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
            <h4 class="font-bold text-gray-900 text-sm mb-2">Draft project proposal</h4>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
              <div class="flex items-center text-gray-400 text-xs gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
                <span>2</span>
              </div>
            </div>
          </div>

          <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
            <span class="bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-1 rounded mb-2 inline-block">Design</span>
            <h4 class="font-bold text-gray-900 text-sm mb-2">Create moodboard</h4>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
            </div>
          </div>
        </div>

        <button class="mt-3 w-full py-2 flex items-center justify-center gap-2 text-gray-500 hover:bg-gray-200 rounded-lg transition-colors text-sm font-medium">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Add Task
        </button>
      </div>

      <div class="w-80 flex flex-col bg-gray-100 rounded-xl p-4">
        <div class="flex justify-between items-center mb-4">
          <h3 class="font-bold text-gray-700">In Progress</h3>
          <span class="bg-gray-200 text-gray-600 text-xs font-bold px-2 py-1 rounded-full">2</span>
        </div>

        <div class="flex-1 overflow-y-auto space-y-3">
          <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
            <div class="w-full h-32 mb-2 rounded-md overflow-hidden">
              <img src="https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=60" class="w-full h-full object-cover" alt="">
            </div>
            <h4 class="font-bold text-gray-900 text-sm mb-2">Design system update</h4>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
              <div class="flex items-center text-gray-400 text-xs gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                </svg>
                <span>1</span>
              </div>
            </div>
          </div>

          <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow">
            <span class="bg-yellow-100 text-yellow-800 text-[10px] font-bold px-2 py-1 rounded mb-2 inline-block">Medium</span>
            <h4 class="font-bold text-gray-900 text-sm mb-2">Client meeting prep</h4>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
              <div class="flex items-center text-gray-400 text-xs gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <span>Tomorrow</span>
              </div>
            </div>
          </div>
        </div>

        <button class="mt-3 w-full py-2 flex items-center justify-center gap-2 text-gray-500 hover:bg-gray-200 rounded-lg transition-colors text-sm font-medium">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Add Task
        </button>
      </div>

      <div class="w-80 flex flex-col bg-gray-100 rounded-xl p-4">
        <div class="flex justify-between items-center mb-4">
          <h3 class="font-bold text-gray-700">Done</h3>
          <span class="bg-gray-200 text-gray-600 text-xs font-bold px-2 py-1 rounded-full">1</span>
        </div>

        <div class="flex-1 overflow-y-auto space-y-3">
          <div class="bg-white p-3 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition-shadow opacity-75">
            <h4 class="font-bold text-gray-900 text-sm mb-2 line-through text-gray-500">Update dependencies</h4>
            <div class="flex justify-between items-center">
              <div class="flex -space-x-2">
                <img class="w-6 h-6 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
              <div class="flex items-center text-green-600 text-xs gap-1 font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                <span>Completed</span>
              </div>
            </div>
          </div>
        </div>

        <button class="mt-3 w-full py-2 flex items-center justify-center gap-2 text-gray-500 hover:bg-gray-200 rounded-lg transition-colors text-sm font-medium">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Add Task
        </button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-047",
        "title": "Event List",
        "description": "Event list with dates.",
        "dir": "lists/list-047",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-3xl w-full">
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-2xl font-bold text-gray-900">Upcoming Events</h2>
        <div class="flex gap-2">
          <button class="bg-white border border-gray-300 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium hover:bg-gray-50">Filter</button>
          <button class="bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700">Create Event</button>
        </div>
      </div>

      <div class="space-y-4">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-4 flex flex-col md:flex-row gap-6 hover:shadow-md transition-shadow">
          <div class="flex-shrink-0 flex flex-col items-center justify-center bg-indigo-50 rounded-lg w-full md:w-24 h-24 text-indigo-600">
            <span class="text-xs font-bold uppercase tracking-wider">Oct</span>
            <span class="text-3xl font-bold">24</span>
          </div>

          <div class="flex-1 flex flex-col justify-center">
            <div class="flex justify-between items-start">
              <div>
                <h3 class="text-lg font-bold text-gray-900 hover:text-indigo-600 cursor-pointer">Tech Conference 2023</h3>
                <p class="text-gray-500 text-sm mt-1">San Francisco, CA • 9:00 AM</p>
              </div>
              <button class="text-gray-400 hover:text-gray-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z" />
                </svg>
              </button>
            </div>
            <div class="mt-4 flex items-center gap-4">
              <div class="flex -space-x-2">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">+120</span>
              </div>
              <span class="text-sm text-gray-500">Going</span>
            </div>
          </div>

          <div class="flex items-center justify-center md:justify-end">
            <button class="w-full md:w-auto border border-indigo-600 text-indigo-600 px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-50 transition-colors">Register</button>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-4 flex flex-col md:flex-row gap-6 hover:shadow-md transition-shadow">
          <div class="flex-shrink-0 flex flex-col items-center justify-center bg-pink-50 rounded-lg w-full md:w-24 h-24 text-pink-600">
            <span class="text-xs font-bold uppercase tracking-wider">Nov</span>
            <span class="text-3xl font-bold">05</span>
          </div>

          <div class="flex-1 flex flex-col justify-center">
            <div class="flex justify-between items-start">
              <div>
                <h3 class="text-lg font-bold text-gray-900 hover:text-pink-600 cursor-pointer">Design Workshop</h3>
                <p class="text-gray-500 text-sm mt-1">Online • 2:00 PM</p>
              </div>
              <button class="text-gray-400 hover:text-gray-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z" />
                </svg>
              </button>
            </div>
            <div class="mt-4 flex items-center gap-4">
              <div class="flex -space-x-2">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">+45</span>
              </div>
              <span class="text-sm text-gray-500">Going</span>
            </div>
          </div>

          <div class="flex items-center justify-center md:justify-end">
            <button class="w-full md:w-auto bg-gray-100 text-gray-500 px-4 py-2 rounded-lg text-sm font-medium cursor-not-allowed">Sold Out</button>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-4 flex flex-col md:flex-row gap-6 hover:shadow-md transition-shadow">
          <div class="flex-shrink-0 flex flex-col items-center justify-center bg-green-50 rounded-lg w-full md:w-24 h-24 text-green-600">
            <span class="text-xs font-bold uppercase tracking-wider">Nov</span>
            <span class="text-3xl font-bold">12</span>
          </div>

          <div class="flex-1 flex flex-col justify-center">
            <div class="flex justify-between items-start">
              <div>
                <h3 class="text-lg font-bold text-gray-900 hover:text-green-600 cursor-pointer">Startup Networking</h3>
                <p class="text-gray-500 text-sm mt-1">New York, NY • 6:00 PM</p>
              </div>
              <button class="text-gray-400 hover:text-gray-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z" />
                </svg>
              </button>
            </div>
            <div class="mt-4 flex items-center gap-4">
              <div class="flex -space-x-2">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <span class="flex items-center justify-center w-8 h-8 rounded-full border-2 border-white bg-gray-100 text-xs font-medium text-gray-500">+80</span>
              </div>
              <span class="text-sm text-gray-500">Going</span>
            </div>
          </div>

          <div class="flex items-center justify-center md:justify-end">
            <button class="w-full md:w-auto border border-green-600 text-green-600 px-4 py-2 rounded-lg text-sm font-medium hover:bg-green-50 transition-colors">RSVP</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-048",
        "title": "Job List",
        "description": "Job listing list.",
        "dir": "lists/list-048",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full">
      <div class="text-center mb-10">
        <h2 class="text-3xl font-bold text-gray-900">Open Positions</h2>
        <p class="text-gray-500 mt-2">Join our team and help us build the future.</p>
      </div>

      <div class="space-y-4">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 hover:shadow-md transition-shadow group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Senior Frontend Developer</h3>
              <div class="flex flex-wrap gap-2 mt-2 text-sm text-gray-500">
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  Remote
                </span>
                <span>•</span>
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  Full-time
                </span>
                <span>•</span>
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  $120k - $150k
                </span>
              </div>
            </div>
          </div>

          <div class="flex items-center gap-3">
            <div class="flex -space-x-2">
              <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </div>
            <button class="bg-blue-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-blue-700 transition-colors">Apply Now</button>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 hover:shadow-md transition-shadow group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.357a4 4 0 015.656 5.656l-1.357 1.657" />
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-bold text-gray-900 group-hover:text-purple-600 transition-colors">Product Designer</h3>
              <div class="flex flex-wrap gap-2 mt-2 text-sm text-gray-500">
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  New York, NY
                </span>
                <span>•</span>
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  Full-time
                </span>
                <span>•</span>
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  $100k - $130k
                </span>
              </div>
            </div>
          </div>

          <div class="flex items-center gap-3">
            <div class="flex -space-x-2">
              <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </div>
            <button class="bg-purple-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-purple-700 transition-colors">Apply Now</button>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 hover:shadow-md transition-shadow group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center text-green-600 flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-bold text-gray-900 group-hover:text-green-600 transition-colors">Backend Engineer</h3>
              <div class="flex flex-wrap gap-2 mt-2 text-sm text-gray-500">
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  Remote
                </span>
                <span>•</span>
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  Contract
                </span>
                <span>•</span>
                <span class="flex items-center gap-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  $80/hr
                </span>
              </div>
            </div>
          </div>

          <div class="flex items-center gap-3">
            <div class="flex -space-x-2">
              <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </div>
            <button class="bg-green-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-green-700 transition-colors">Apply Now</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS_5_PART_3 = [
    {
        "id": "list-049",
        "title": "Notification List",
        "description": "Notification list with actions.",
        "dir": "lists/list-049",
        "content": """
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg overflow-hidden">
      <div class="p-4 border-b border-gray-100 flex justify-between items-center">
        <h2 class="font-bold text-gray-900">Notifications</h2>
        <button class="text-blue-600 text-sm font-medium hover:text-blue-700">Mark all as read</button>
      </div>

      <div class="divide-y divide-gray-100 max-h-[500px] overflow-y-auto">
        <div class="p-4 bg-blue-50/50 hover:bg-blue-50 transition-colors cursor-pointer relative group">
          <div class="absolute top-4 right-4 w-2 h-2 bg-blue-600 rounded-full"></div>
          <div class="flex gap-4">
            <div class="relative flex-shrink-0">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="absolute -bottom-1 -right-1 bg-blue-600 text-white rounded-full p-0.5 border-2 border-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z" />
                  <path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z" />
                </svg>
              </div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-900"><span class="font-bold">Sarah Jenkins</span> commented on your post <span class="font-medium text-gray-600">"Design System v2.0"</span></p>
              <p class="text-xs text-gray-500 mt-1">2 minutes ago</p>
              <div class="mt-2 text-sm text-gray-600 bg-white p-2 rounded border border-gray-200 italic">
                "Great work on the color palette! I really love the new primary blue."
              </div>
              <div class="mt-2 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button class="text-xs font-medium text-blue-600 hover:text-blue-700">Reply</button>
                <button class="text-xs font-medium text-gray-500 hover:text-gray-700">Like</button>
              </div>
            </div>
          </div>
        </div>

        <div class="p-4 hover:bg-gray-50 transition-colors cursor-pointer group">
          <div class="flex gap-4">
            <div class="relative flex-shrink-0">
              <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
              </div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-900">Your project <span class="font-bold">Mobile App Redesign</span> has been approved!</p>
              <p class="text-xs text-gray-500 mt-1">1 hour ago</p>
              <div class="mt-2 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button class="text-xs font-medium text-blue-600 hover:text-blue-700">View Project</button>
              </div>
            </div>
          </div>
        </div>

        <div class="p-4 hover:bg-gray-50 transition-colors cursor-pointer group">
          <div class="flex gap-4">
            <div class="relative flex-shrink-0">
              <img class="w-10 h-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="absolute -bottom-1 -right-1 bg-purple-600 text-white rounded-full p-0.5 border-2 border-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0 1 1 0 002 0z" />
                </svg>
              </div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-900"><span class="font-bold">Michael Chen</span> invited you to the team <span class="font-medium text-gray-600">"Marketing Squad"</span></p>
              <p class="text-xs text-gray-500 mt-1">3 hours ago</p>
              <div class="mt-2 flex gap-2">
                <button class="bg-blue-600 text-white text-xs px-3 py-1 rounded hover:bg-blue-700 transition-colors">Accept</button>
                <button class="bg-gray-100 text-gray-600 text-xs px-3 py-1 rounded hover:bg-gray-200 transition-colors">Decline</button>
              </div>
            </div>
          </div>
        </div>

        <div class="p-4 hover:bg-gray-50 transition-colors cursor-pointer group">
          <div class="flex gap-4">
            <div class="relative flex-shrink-0">
              <div class="w-10 h-10 rounded-full bg-yellow-100 flex items-center justify-center text-yellow-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                </svg>
              </div>
            </div>
            <div class="flex-1">
              <p class="text-sm text-gray-900">Your subscription is about to expire in <span class="font-bold">3 days</span></p>
              <p class="text-xs text-gray-500 mt-1">Yesterday</p>
              <div class="mt-2 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button class="text-xs font-medium text-blue-600 hover:text-blue-700">Renew Now</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="p-3 bg-gray-50 text-center border-t border-gray-100">
        <button class="text-sm text-gray-500 hover:text-gray-700 font-medium">View all notifications</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "list-050",
        "title": "Music List",
        "description": "Music playlist with controls.",
        "dir": "lists/list-050",
        "content": """
  <div class="min-h-screen bg-gray-900 flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-gray-800 rounded-xl shadow-2xl overflow-hidden border border-gray-700">
      <div class="relative h-48">
        <img class="w-full h-full object-cover opacity-50" src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
        <div class="absolute inset-0 bg-gradient-to-t from-gray-800 to-transparent"></div>
        <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end">
          <div>
            <h2 class="text-2xl font-bold text-white">Late Night Vibes</h2>
            <p class="text-gray-300 text-sm">Created by Alex • 50 songs</p>
          </div>
          <button class="w-12 h-12 bg-green-500 rounded-full flex items-center justify-center shadow-lg hover:bg-green-400 transition-colors transform hover:scale-105">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white ml-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>

      <div class="p-2">
        <div class="flex items-center p-3 hover:bg-gray-700/50 rounded-lg group cursor-pointer transition-colors">
          <span class="text-gray-500 w-8 text-center text-sm group-hover:hidden">1</span>
          <button class="w-8 text-center hidden group-hover:block text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </button>

          <div class="flex-1 ml-2">
            <h3 class="text-white font-medium text-sm">Midnight City</h3>
            <p class="text-gray-400 text-xs">M83</p>
          </div>

          <div class="flex items-center gap-4">
            <button class="text-gray-400 hover:text-green-500 opacity-0 group-hover:opacity-100 transition-opacity">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </button>
            <span class="text-gray-500 text-xs w-10 text-right">4:03</span>
          </div>
        </div>

        <div class="flex items-center p-3 bg-gray-700/50 rounded-lg group cursor-pointer transition-colors">
          <span class="text-green-500 w-8 text-center text-sm group-hover:hidden">
            <div class="flex gap-0.5 justify-center items-end h-3">
              <div class="w-0.5 bg-green-500 h-1 animate-[music-bar_1s_ease-in-out_infinite]"></div>
              <div class="w-0.5 bg-green-500 h-3 animate-[music-bar_1.2s_ease-in-out_infinite]"></div>
              <div class="w-0.5 bg-green-500 h-2 animate-[music-bar_0.8s_ease-in-out_infinite]"></div>
            </div>
          </span>
          <button class="w-8 text-center hidden group-hover:block text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
          </button>

          <div class="flex-1 ml-2">
            <h3 class="text-green-500 font-medium text-sm">Nightcall</h3>
            <p class="text-gray-400 text-xs">Kavinsky</p>
          </div>

          <div class="flex items-center gap-4">
            <button class="text-green-500 hover:text-green-400 opacity-100 transition-opacity">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
              </svg>
            </button>
            <span class="text-gray-500 text-xs w-10 text-right">4:18</span>
          </div>
        </div>

        <div class="flex items-center p-3 hover:bg-gray-700/50 rounded-lg group cursor-pointer transition-colors">
          <span class="text-gray-500 w-8 text-center text-sm group-hover:hidden">3</span>
          <button class="w-8 text-center hidden group-hover:block text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </button>

          <div class="flex-1 ml-2">
            <h3 class="text-white font-medium text-sm">Resonance</h3>
            <p class="text-gray-400 text-xs">Home</p>
          </div>

          <div class="flex items-center gap-4">
            <button class="text-gray-400 hover:text-green-500 opacity-0 group-hover:opacity-100 transition-opacity">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </button>
            <span class="text-gray-500 text-xs w-10 text-right">3:32</span>
          </div>
        </div>

        <div class="flex items-center p-3 hover:bg-gray-700/50 rounded-lg group cursor-pointer transition-colors">
          <span class="text-gray-500 w-8 text-center text-sm group-hover:hidden">4</span>
          <button class="w-8 text-center hidden group-hover:block text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
            </svg>
          </button>

          <div class="flex-1 ml-2">
            <h3 class="text-white font-medium text-sm">After Dark</h3>
            <p class="text-gray-400 text-xs">Mr. Kitty</p>
          </div>

          <div class="flex items-center gap-4">
            <button class="text-gray-400 hover:text-green-500 opacity-0 group-hover:opacity-100 transition-opacity">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </button>
            <span class="text-gray-500 text-xs w-10 text-right">4:17</span>
          </div>
        </div>
      </div>

      <div class="p-4 bg-gray-800 border-t border-gray-700">
        <div class="w-full bg-gray-700 rounded-full h-1 mb-4 cursor-pointer group">
          <div class="bg-green-500 h-1 rounded-full relative w-1/3">
            <div class="w-3 h-3 bg-white rounded-full absolute -right-1.5 -top-1 hidden group-hover:block shadow"></div>
          </div>
        </div>

        <div class="flex justify-between items-center">
          <button class="text-gray-400 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </button>

          <div class="flex items-center gap-6">
            <button class="text-gray-300 hover:text-white">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
              </svg>
            </button>

            <button class="w-10 h-10 bg-white rounded-full flex items-center justify-center hover:scale-105 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-900" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
            </button>

            <button class="text-gray-300 hover:text-white">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>

          <button class="text-gray-400 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_LISTS = TEMPLATES_LISTS_1 + TEMPLATES_LISTS_2 + TEMPLATES_LISTS_3_PART_1 + TEMPLATES_LISTS_3_PART_2 + TEMPLATES_LISTS_4_PART_1 + TEMPLATES_LISTS_4_PART_2 + TEMPLATES_LISTS_5_PART_1 + TEMPLATES_LISTS_5_PART_2 + TEMPLATES_LISTS_5_PART_3

# Combine all templates
TEMPLATES = TEMPLATES_GALLERY_1 + TEMPLATES_GALLERY_1_PART_2 + TEMPLATES_GALLERY_2 + TEMPLATES_GALLERY_2_PART_2 + TEMPLATES_GALLERY_2_PART_3 + TEMPLATES_FORMS + TEMPLATES_CARDS + TEMPLATES_LISTS

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
