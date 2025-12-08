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

# Part 1: Features 013-030
TEMPLATES_PART_1 = [
    {
        "id": "feat-013",
        "title": "Feature List with Descriptions",
        "description": "Title + description list",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6 space-y-12">
      <div>
        <h3 class="text-2xl font-bold text-slate-900">Advanced Analytics</h3>
        <p class="mt-4 text-lg text-slate-600">Get detailed insights into your performance with our advanced analytics dashboard. Track metrics that matter.</p>
      </div>
      <div>
        <h3 class="text-2xl font-bold text-slate-900">User Management</h3>
        <p class="mt-4 text-lg text-slate-600">Easily manage your team members and their permissions. Control who has access to what.</p>
      </div>
      <div>
        <h3 class="text-2xl font-bold text-slate-900">Secure Storage</h3>
        <p class="mt-4 text-lg text-slate-600">Your data is safe with us. We use enterprise-grade encryption to protect your sensitive information.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-014",
        "title": "Feature List with Images",
        "description": "Image + text list items",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-4xl mx-auto px-6 space-y-12">
      <div class="flex flex-col md:flex-row gap-8 items-start">
        <img src="https://via.placeholder.com/200" class="w-full md:w-48 rounded-lg shadow-md" alt="Feature 1">
        <div>
          <h3 class="text-xl font-bold text-slate-900">Visual Editing</h3>
          <p class="mt-2 text-slate-600">Edit your content visually with our drag-and-drop builder. No coding required.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row gap-8 items-start">
        <img src="https://via.placeholder.com/200" class="w-full md:w-48 rounded-lg shadow-md" alt="Feature 2">
        <div>
          <h3 class="text-xl font-bold text-slate-900">Asset Library</h3>
          <p class="mt-2 text-slate-600">Access thousands of royalty-free images and icons directly within the editor.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-015",
        "title": "Numbered Feature List",
        "description": "Sequential numbered features",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6">
      <div class="space-y-12">
        <div class="relative pl-16">
          <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-full bg-primary-600 text-white font-bold">1</div>
          <h3 class="text-xl font-bold text-slate-900">Sign Up</h3>
          <p class="mt-2 text-slate-600">Create your account in seconds. No credit card required for the free trial.</p>
        </div>
        <div class="relative pl-16">
          <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-full bg-primary-600 text-white font-bold">2</div>
          <h3 class="text-xl font-bold text-slate-900">Configure</h3>
          <p class="mt-2 text-slate-600">Set up your preferences and customize the platform to fit your needs.</p>
        </div>
        <div class="relative pl-16">
          <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-full bg-primary-600 text-white font-bold">3</div>
          <h3 class="text-xl font-bold text-slate-900">Launch</h3>
          <p class="mt-2 text-slate-600">Go live and start seeing results immediately.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-016",
        "title": "Feature List with Dividers",
        "description": "Separated feature items",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6">
      <div class="divide-y divide-slate-200">
        <div class="py-8 first:pt-0 last:pb-0">
          <h3 class="text-lg font-bold text-slate-900">Cloud Sync</h3>
          <p class="mt-2 text-slate-600">Keep your data synchronized across all your devices automatically.</p>
        </div>
        <div class="py-8 first:pt-0 last:pb-0">
          <h3 class="text-lg font-bold text-slate-900">Offline Mode</h3>
          <p class="mt-2 text-slate-600">Continue working even when you don't have an internet connection.</p>
        </div>
        <div class="py-8 first:pt-0 last:pb-0">
          <h3 class="text-lg font-bold text-slate-900">Version History</h3>
          <p class="mt-2 text-slate-600">Restore previous versions of your work with a single click.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-017",
        "title": "Expandable Feature List",
        "description": "Accordion feature list",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-3xl mx-auto px-6 space-y-4">
      <details class="group bg-white p-6 rounded-lg shadow-sm open:ring-2 open:ring-primary-500">
        <summary class="flex cursor-pointer items-center justify-between font-medium text-slate-900">
          <span>Real-time Collaboration</span>
          <span class="transition group-open:rotate-180">
            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
          </span>
        </summary>
        <p class="group-open:animate-fadeIn mt-4 text-slate-600">Work together with your team in real-time. See changes as they happen.</p>
      </details>
      <details class="group bg-white p-6 rounded-lg shadow-sm open:ring-2 open:ring-primary-500">
        <summary class="flex cursor-pointer items-center justify-between font-medium text-slate-900">
          <span>API Access</span>
          <span class="transition group-open:rotate-180">
            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
          </span>
        </summary>
        <p class="group-open:animate-fadeIn mt-4 text-slate-600">Integrate with your existing tools using our robust API.</p>
      </details>
    </div>
  </div>"""
    },
    {
        "id": "feat-018",
        "title": "Feature List Two Columns",
        "description": "Side-by-side feature lists",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8">
        <div>
          <h3 class="font-bold text-slate-900">Fast Rendering</h3>
          <p class="mt-2 text-slate-600">Optimized for speed and performance.</p>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">SEO Friendly</h3>
          <p class="mt-2 text-slate-600">Built with search engines in mind.</p>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Accessibility</h3>
          <p class="mt-2 text-slate-600">Compliant with WCAG standards.</p>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Responsive Design</h3>
          <p class="mt-2 text-slate-600">Looks great on any device.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-019",
        "title": "Feature List with Progress",
        "description": "Features with progress indicators",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-3xl mx-auto px-6 space-y-8">
      <div>
        <div class="flex justify-between mb-2">
          <span class="font-bold text-slate-900">Performance</span>
          <span class="text-slate-600">98%</span>
        </div>
        <div class="w-full bg-slate-200 rounded-full h-2.5">
          <div class="bg-primary-600 h-2.5 rounded-full" style="width: 98%"></div>
        </div>
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <span class="font-bold text-slate-900">Reliability</span>
          <span class="text-slate-600">99.9%</span>
        </div>
        <div class="w-full bg-slate-200 rounded-full h-2.5">
          <div class="bg-primary-600 h-2.5 rounded-full" style="width: 99.9%"></div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-020",
        "title": "Timeline Feature List",
        "description": "Vertical timeline layout",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-3xl mx-auto px-6">
      <div class="relative border-l-2 border-slate-200 ml-3 space-y-12">
        <div class="pl-8 relative">
          <div class="absolute -left-[9px] top-0 h-4 w-4 rounded-full bg-primary-600 ring-4 ring-white"></div>
          <h3 class="font-bold text-slate-900">Q1 2024</h3>
          <p class="mt-2 text-slate-600">Launched beta version to initial user group.</p>
        </div>
        <div class="pl-8 relative">
          <div class="absolute -left-[9px] top-0 h-4 w-4 rounded-full bg-slate-300 ring-4 ring-white"></div>
          <h3 class="font-bold text-slate-900">Q2 2024</h3>
          <p class="mt-2 text-slate-600">Public release and marketing campaign.</p>
        </div>
        <div class="pl-8 relative">
          <div class="absolute -left-[9px] top-0 h-4 w-4 rounded-full bg-slate-300 ring-4 ring-white"></div>
          <h3 class="font-bold text-slate-900">Q3 2024</h3>
          <p class="mt-2 text-slate-600">Expansion to new markets.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-021",
        "title": "Large Icon Features",
        "description": "Prominent icon display",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
      <div>
        <div class="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-primary-100 text-primary-600 mb-6">
          <svg class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Lightning Fast</h3>
        <p class="mt-2 text-slate-600">Experience blazing fast load times.</p>
      </div>
      <div>
        <div class="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-primary-100 text-primary-600 mb-6">
          <svg class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Secure</h3>
        <p class="mt-2 text-slate-600">Bank-grade security for your data.</p>
      </div>
      <div>
        <div class="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-primary-100 text-primary-600 mb-6">
          <svg class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Global</h3>
        <p class="mt-2 text-slate-600">Available in over 100 countries.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-022",
        "title": "Circular Icon Features",
        "description": "Icons in circles",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-blue-100 text-blue-600 mb-4">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        </div>
        <h3 class="font-bold">Verified</h3>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-green-100 text-green-600 mb-4">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        </div>
        <h3 class="font-bold">Fast</h3>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-purple-100 text-purple-600 mb-4">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
        </div>
        <h3 class="font-bold">Science</h3>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-red-100 text-red-600 mb-4">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" /></svg>
        </div>
        <h3 class="font-bold">Loved</h3>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-023",
        "title": "Square Icon Features",
        "description": "Icons in squares",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="flex gap-4">
        <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-lg bg-primary-600 text-white">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" /></svg>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Square Icons</h3>
          <p class="mt-2 text-slate-600">Rounded corners for a modern look.</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-lg bg-primary-600 text-white">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Consistent</h3>
          <p class="mt-2 text-slate-600">Uniform sizing across all features.</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-lg bg-primary-600 text-white">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Bold</h3>
          <p class="mt-2 text-slate-600">High contrast for better visibility.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-024",
        "title": "Gradient Icon Features",
        "description": "Icons with gradient backgrounds",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-pink-500 to-orange-400 text-white mb-6 shadow-lg">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" /></svg>
        </div>
        <h3 class="font-bold text-lg">Passion</h3>
      </div>
      <div class="text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-500 to-cyan-400 text-white mb-6 shadow-lg">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <h3 class="font-bold text-lg">Energy</h3>
      </div>
      <div class="text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-purple-500 to-indigo-400 text-white mb-6 shadow-lg">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" /></svg>
        </div>
        <h3 class="font-bold text-lg">Innovation</h3>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-025",
        "title": "Outline Icon Features",
        "description": "Stroke/outline style icons",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="p-6 border border-slate-200 rounded-xl hover:border-primary-500 transition-colors group">
        <div class="h-12 w-12 text-slate-400 group-hover:text-primary-600 transition-colors mb-4">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" /></svg>
        </div>
        <h3 class="font-bold text-lg text-slate-900">Configuration</h3>
        <p class="mt-2 text-slate-600">Highly customizable settings.</p>
      </div>
      <div class="p-6 border border-slate-200 rounded-xl hover:border-primary-500 transition-colors group">
        <div class="h-12 w-12 text-slate-400 group-hover:text-primary-600 transition-colors mb-4">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
        </div>
        <h3 class="font-bold text-lg text-slate-900">Documentation</h3>
        <p class="mt-2 text-slate-600">Comprehensive guides and docs.</p>
      </div>
      <div class="p-6 border border-slate-200 rounded-xl hover:border-primary-500 transition-colors group">
        <div class="h-12 w-12 text-slate-400 group-hover:text-primary-600 transition-colors mb-4">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" /></svg>
        </div>
        <h3 class="font-bold text-lg text-slate-900">Support</h3>
        <p class="mt-2 text-slate-600">24/7 dedicated support team.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-026",
        "title": "Animated Icon Features",
        "description": "Icons with hover animations",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="group text-center p-6">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-slate-100 text-slate-600 mb-6 transition-transform group-hover:rotate-12 group-hover:scale-110 group-hover:bg-primary-100 group-hover:text-primary-600">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
        </div>
        <h3 class="font-bold text-lg">Hover Me</h3>
      </div>
      <div class="group text-center p-6">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-slate-100 text-slate-600 mb-6 transition-transform group-hover:-translate-y-2 group-hover:bg-primary-100 group-hover:text-primary-600">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" /></svg>
        </div>
        <h3 class="font-bold text-lg">Lift Off</h3>
      </div>
      <div class="group text-center p-6">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-slate-100 text-slate-600 mb-6 transition-transform group-hover:scale-125 group-hover:bg-primary-100 group-hover:text-primary-600">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
        </div>
        <h3 class="font-bold text-lg">Zoom In</h3>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-027",
        "title": "Dual-Tone Icon Features",
        "description": "Two-color icon treatment",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="flex gap-4">
        <div class="h-12 w-12 shrink-0">
          <svg class="h-full w-full text-primary-600" fill="currentColor" viewBox="0 0 24 24"><path class="text-primary-200" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/><path d="M12 6c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4z"/></svg>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Dual Tone</h3>
          <p class="mt-2 text-slate-600">Using opacity for depth.</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="h-12 w-12 shrink-0">
          <svg class="h-full w-full text-primary-600" fill="currentColor" viewBox="0 0 24 24"><path class="text-primary-200" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">Info</h3>
          <p class="mt-2 text-slate-600">Clear and distinct iconography.</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="h-12 w-12 shrink-0">
          <svg class="h-full w-full text-primary-600" fill="currentColor" viewBox="0 0 24 24"><path class="text-primary-200" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
        </div>
        <div>
          <h3 class="font-bold text-slate-900">World</h3>
          <p class="mt-2 text-slate-600">Connected everywhere.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-028",
        "title": "Icon Features with Badges",
        "description": "Icons with notification badges",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="flex flex-col items-center">
        <div class="relative mb-4">
          <div class="h-16 w-16 bg-slate-100 rounded-xl flex items-center justify-center">
            <svg class="h-8 w-8 text-slate-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
          </div>
          <span class="absolute -top-2 -right-2 flex h-6 w-6 items-center justify-center rounded-full bg-red-500 text-xs font-bold text-white ring-2 ring-white">3</span>
        </div>
        <h3 class="font-bold">Inbox</h3>
      </div>
      <div class="flex flex-col items-center">
        <div class="relative mb-4">
          <div class="h-16 w-16 bg-slate-100 rounded-xl flex items-center justify-center">
            <svg class="h-8 w-8 text-slate-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>
          </div>
          <span class="absolute -top-2 -right-2 flex h-6 w-6 items-center justify-center rounded-full bg-blue-500 text-xs font-bold text-white ring-2 ring-white">New</span>
        </div>
        <h3 class="font-bold">Notifications</h3>
      </div>
      <div class="flex flex-col items-center">
        <div class="relative mb-4">
          <div class="h-16 w-16 bg-slate-100 rounded-xl flex items-center justify-center">
            <svg class="h-8 w-8 text-slate-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          </div>
          <span class="absolute -top-2 -right-2 flex h-6 w-6 items-center justify-center rounded-full bg-green-500 text-xs font-bold text-white ring-2 ring-white">✓</span>
        </div>
        <h3 class="font-bold">Tasks</h3>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-029",
        "title": "Icon Features Horizontal",
        "description": "Icon left, text right",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div class="flex items-center gap-4 p-4 border rounded-lg">
        <div class="h-10 w-10 flex items-center justify-center bg-primary-100 text-primary-600 rounded-full shrink-0">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <span class="font-bold text-slate-900">Instant Activation</span>
      </div>
      <div class="flex items-center gap-4 p-4 border rounded-lg">
        <div class="h-10 w-10 flex items-center justify-center bg-primary-100 text-primary-600 rounded-full shrink-0">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
        </div>
        <span class="font-bold text-slate-900">Secure Payments</span>
      </div>
      <div class="flex items-center gap-4 p-4 border rounded-lg">
        <div class="h-10 w-10 flex items-center justify-center bg-primary-100 text-primary-600 rounded-full shrink-0">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
        </div>
        <span class="font-bold text-slate-900">24/7 Support</span>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-030",
        "title": "Icon Features with Lines",
        "description": "Connected icons with lines",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="relative grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
        <!-- Connecting Line -->
        <div class="hidden md:block absolute top-8 left-[16%] right-[16%] h-0.5 bg-slate-200 -z-10"></div>

        <div class="relative">
          <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-white border-2 border-primary-600 text-primary-600 mb-4">1</div>
          <h3 class="font-bold">Step One</h3>
        </div>
        <div class="relative">
          <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-white border-2 border-primary-600 text-primary-600 mb-4">2</div>
          <h3 class="font-bold">Step Two</h3>
        </div>
        <div class="relative">
          <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-white border-2 border-primary-600 text-primary-600 mb-4">3</div>
          <h3 class="font-bold">Step Three</h3>
        </div>
      </div>
    </div>
  </div>"""
    }
]

# Part 2: Features 031-050
TEMPLATES_PART_2 = [
    {
        "id": "feat-031",
        "title": "Basic Feature Cards",
        "description": "Cards for each feature",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow-lg">
        <h3 class="text-xl font-bold text-slate-900">Card One</h3>
        <p class="mt-4 text-slate-600">Simple card layout with shadow for depth.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg">
        <h3 class="text-xl font-bold text-slate-900">Card Two</h3>
        <p class="mt-4 text-slate-600">Consistent padding and rounded corners.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg">
        <h3 class="text-xl font-bold text-slate-900">Card Three</h3>
        <p class="mt-4 text-slate-600">Clean and effective presentation.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-032",
        "title": "Feature Cards with Image Header",
        "description": "Image at top of card",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white rounded-xl shadow-lg overflow-hidden">
        <img src="https://via.placeholder.com/400x200" class="w-full h-48 object-cover" alt="Card Header">
        <div class="p-6">
          <h3 class="text-xl font-bold text-slate-900">Visual Header</h3>
          <p class="mt-2 text-slate-600">Images add context and visual appeal.</p>
        </div>
      </div>
      <div class="bg-white rounded-xl shadow-lg overflow-hidden">
        <img src="https://via.placeholder.com/400x200" class="w-full h-48 object-cover" alt="Card Header">
        <div class="p-6">
          <h3 class="text-xl font-bold text-slate-900">Engaging</h3>
          <p class="mt-2 text-slate-600">Draw users in with high-quality photos.</p>
        </div>
      </div>
      <div class="bg-white rounded-xl shadow-lg overflow-hidden">
        <img src="https://via.placeholder.com/400x200" class="w-full h-48 object-cover" alt="Card Header">
        <div class="p-6">
          <h3 class="text-xl font-bold text-slate-900">Descriptive</h3>
          <p class="mt-2 text-slate-600">Combine imagery with text effectively.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-033",
        "title": "Feature Cards with Icon Header",
        "description": "Large icon at card top",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow-lg text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-primary-100 text-primary-600 mb-6">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Icon Header</h3>
        <p class="mt-4 text-slate-600">Focus on the symbol representing the feature.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-primary-100 text-primary-600 mb-6">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Clear</h3>
        <p class="mt-4 text-slate-600">Easy to scan and understand.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-primary-100 text-primary-600 mb-6">
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900">Simple</h3>
        <p class="mt-4 text-slate-600">Minimalist design approach.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-034",
        "title": "Feature Cards with Border",
        "description": "Border-styled feature cards",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="p-8 rounded-xl border-2 border-slate-200 hover:border-primary-500 transition-colors">
        <h3 class="text-xl font-bold text-slate-900">Bordered Card</h3>
        <p class="mt-4 text-slate-600">Using borders instead of shadows for definition.</p>
      </div>
      <div class="p-8 rounded-xl border-2 border-slate-200 hover:border-primary-500 transition-colors">
        <h3 class="text-xl font-bold text-slate-900">Clean Lines</h3>
        <p class="mt-4 text-slate-600">A sharper, more technical look.</p>
      </div>
      <div class="p-8 rounded-xl border-2 border-slate-200 hover:border-primary-500 transition-colors">
        <h3 class="text-xl font-bold text-slate-900">Interactive</h3>
        <p class="mt-4 text-slate-600">Border color change on hover indicates interactivity.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-035",
        "title": "Feature Cards with Hover Lift",
        "description": "Cards lift on hover",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl hover:-translate-y-2 transition-all duration-300 cursor-pointer">
        <h3 class="text-xl font-bold text-slate-900">Lift Effect</h3>
        <p class="mt-4 text-slate-600">Adds a sense of depth and tactility.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl hover:-translate-y-2 transition-all duration-300 cursor-pointer">
        <h3 class="text-xl font-bold text-slate-900">Engaging</h3>
        <p class="mt-4 text-slate-600">Encourages users to interact with the content.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl hover:-translate-y-2 transition-all duration-300 cursor-pointer">
        <h3 class="text-xl font-bold text-slate-900">Smooth</h3>
        <p class="mt-4 text-slate-600">Uses CSS transitions for fluid motion.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-036",
        "title": "Feature Cards Glassmorphism",
        "description": "Frosted glass effect cards",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-gradient-to-br from-purple-500 to-blue-600">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white/20 backdrop-blur-lg p-8 rounded-xl border border-white/30 text-white shadow-xl">
        <h3 class="text-xl font-bold">Glass Effect</h3>
        <p class="mt-4 text-white/80">Modern frosted glass aesthetic.</p>
      </div>
      <div class="bg-white/20 backdrop-blur-lg p-8 rounded-xl border border-white/30 text-white shadow-xl">
        <h3 class="text-xl font-bold">Translucent</h3>
        <p class="mt-4 text-white/80">Allows the background to peek through.</p>
      </div>
      <div class="bg-white/20 backdrop-blur-lg p-8 rounded-xl border border-white/30 text-white shadow-xl">
        <h3 class="text-xl font-bold">Premium</h3>
        <p class="mt-4 text-white/80">Creates a high-end, sophisticated feel.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-037",
        "title": "Feature Cards with Gradient Border",
        "description": "Gradient border effect",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-900">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="relative p-[2px] rounded-xl bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500">
        <div class="bg-slate-900 p-8 rounded-[10px] h-full">
          <h3 class="text-xl font-bold text-white">Gradient Border</h3>
          <p class="mt-4 text-slate-400">Eye-catching border treatment.</p>
        </div>
      </div>
      <div class="relative p-[2px] rounded-xl bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500">
        <div class="bg-slate-900 p-8 rounded-[10px] h-full">
          <h3 class="text-xl font-bold text-white">Neon Glow</h3>
          <p class="mt-4 text-slate-400">Perfect for dark mode interfaces.</p>
        </div>
      </div>
      <div class="relative p-[2px] rounded-xl bg-gradient-to-r from-green-400 via-teal-500 to-blue-500">
        <div class="bg-slate-900 p-8 rounded-[10px] h-full">
          <h3 class="text-xl font-bold text-white">Vibrant</h3>
          <p class="mt-4 text-slate-400">Adds a splash of color without overwhelming.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-038",
        "title": "Feature Cards Dark Mode",
        "description": "Dark theme feature cards",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-900">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-slate-800 p-8 rounded-xl shadow-lg border border-slate-700">
        <h3 class="text-xl font-bold text-white">Dark Card</h3>
        <p class="mt-4 text-slate-400">Optimized for low-light environments.</p>
      </div>
      <div class="bg-slate-800 p-8 rounded-xl shadow-lg border border-slate-700">
        <h3 class="text-xl font-bold text-white">Contrast</h3>
        <p class="mt-4 text-slate-400">High contrast text for readability.</p>
      </div>
      <div class="bg-slate-800 p-8 rounded-xl shadow-lg border border-slate-700">
        <h3 class="text-xl font-bold text-white">Sleek</h3>
        <p class="mt-4 text-slate-400">Professional and modern appearance.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-039",
        "title": "Feature Cards with Action",
        "description": "Cards with CTA button",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-xl shadow-lg flex flex-col items-start">
        <h3 class="text-xl font-bold text-slate-900">Starter</h3>
        <p class="mt-4 text-slate-600 mb-8 flex-grow">Perfect for individuals just starting out.</p>
        <button class="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors">Get Started</button>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg flex flex-col items-start">
        <h3 class="text-xl font-bold text-slate-900">Pro</h3>
        <p class="mt-4 text-slate-600 mb-8 flex-grow">For professionals who need more power.</p>
        <button class="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors">Upgrade Now</button>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg flex flex-col items-start">
        <h3 class="text-xl font-bold text-slate-900">Enterprise</h3>
        <p class="mt-4 text-slate-600 mb-8 flex-grow">Custom solutions for large teams.</p>
        <button class="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors">Contact Sales</button>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-040",
        "title": "Feature Cards Horizontal",
        "description": "Horizontal card layout",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-4xl mx-auto px-6 space-y-8">
      <div class="bg-white rounded-xl shadow-lg overflow-hidden flex flex-col md:flex-row">
        <img src="https://via.placeholder.com/300" class="w-full md:w-64 h-48 md:h-auto object-cover" alt="Feature">
        <div class="p-8">
          <h3 class="text-xl font-bold text-slate-900">Horizontal Layout</h3>
          <p class="mt-4 text-slate-600">Side-by-side image and text works well for list-like features.</p>
        </div>
      </div>
      <div class="bg-white rounded-xl shadow-lg overflow-hidden flex flex-col md:flex-row">
        <img src="https://via.placeholder.com/300" class="w-full md:w-64 h-48 md:h-auto object-cover" alt="Feature">
        <div class="p-8">
          <h3 class="text-xl font-bold text-slate-900">Responsive</h3>
          <p class="mt-4 text-slate-600">Stacks vertically on mobile devices for better readability.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-041",
        "title": "Zigzag Features",
        "description": "Alternating left/right layout",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="bg-slate-200 rounded-xl h-64 w-full"></div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Left Image</h3>
          <p class="mt-4 text-lg text-slate-600">Standard layout with image on the left and content on the right.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="bg-slate-200 rounded-xl h-64 w-full"></div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Right Image</h3>
          <p class="mt-4 text-lg text-slate-600">Alternating layout keeps the user engaged as they scroll down.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="bg-slate-200 rounded-xl h-64 w-full"></div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Left Image</h3>
          <p class="mt-4 text-lg text-slate-600">Repeating the pattern creates a rhythm.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-042",
        "title": "Zigzag with Large Images",
        "description": "Big image alternating layout",
        "dir": "templates/03-features",
        "content": """<div class="bg-white">
    <div class="grid grid-cols-1 md:grid-cols-2">
      <div class="h-96 md:h-auto bg-slate-200">
        <img src="https://via.placeholder.com/800" class="w-full h-full object-cover" alt="Large Image">
      </div>
      <div class="flex items-center justify-center p-12 md:p-24">
        <div>
          <h3 class="text-3xl font-bold text-slate-900">Full Height</h3>
          <p class="mt-4 text-lg text-slate-600">Images take up the full height of the section.</p>
        </div>
      </div>
      <div class="flex items-center justify-center p-12 md:p-24 md:order-last">
        <div>
          <h3 class="text-3xl font-bold text-slate-900">Immersive</h3>
          <p class="mt-4 text-lg text-slate-600">Great for showcasing product photography.</p>
        </div>
      </div>
      <div class="h-96 md:h-auto bg-slate-200">
        <img src="https://via.placeholder.com/800" class="w-full h-full object-cover" alt="Large Image">
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-043",
        "title": "Zigzag with Background Colors",
        "description": "Alternating background colors",
        "dir": "templates/03-features",
        "content": """<div>
    <div class="py-24 bg-white">
      <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2"><div class="bg-slate-200 h-64 rounded-xl"></div></div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">White Background</h3>
          <p class="mt-4 text-lg text-slate-600">Clean and simple start.</p>
        </div>
      </div>
    </div>
    <div class="py-24 bg-slate-50">
      <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="w-full md:w-1/2"><div class="bg-white h-64 rounded-xl shadow-sm"></div></div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Grey Background</h3>
          <p class="mt-4 text-lg text-slate-600">Subtle contrast to separate sections.</p>
        </div>
      </div>
    </div>
    <div class="py-24 bg-white">
      <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2"><div class="bg-slate-200 h-64 rounded-xl"></div></div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">White Background</h3>
          <p class="mt-4 text-lg text-slate-600">Back to clean.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-044",
        "title": "Zigzag with Icons",
        "description": "Icon-based alternating",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2 flex justify-center">
          <div class="h-48 w-48 bg-primary-100 rounded-full flex items-center justify-center text-primary-600">
            <svg class="h-24 w-24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
          </div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Icon Focus</h3>
          <p class="mt-4 text-lg text-slate-600">Using large icons instead of images.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="w-full md:w-1/2 flex justify-center">
          <div class="h-48 w-48 bg-secondary-100 rounded-full flex items-center justify-center text-secondary-600">
            <svg class="h-24 w-24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" /></svg>
          </div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Abstract</h3>
          <p class="mt-4 text-lg text-slate-600">Representing concepts visually.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-045",
        "title": "Zigzag with Stats",
        "description": "Stats alternating with content",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="bg-slate-900 text-white p-12 rounded-xl text-center">
            <div class="text-6xl font-bold text-primary-500">500%</div>
            <div class="mt-4 text-xl">Growth Year over Year</div>
          </div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Rapid Growth</h3>
          <p class="mt-4 text-lg text-slate-600">Our numbers speak for themselves.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="bg-slate-900 text-white p-12 rounded-xl text-center">
            <div class="text-6xl font-bold text-primary-500">1M+</div>
            <div class="mt-4 text-xl">Active Users</div>
          </div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Massive Scale</h3>
          <p class="mt-4 text-lg text-slate-600">Trusted by millions around the world.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-046",
        "title": "Zigzag with Testimonials",
        "description": "Feature + testimonial alternating",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2">
          <blockquote class="bg-slate-50 p-8 rounded-xl border-l-4 border-primary-600">
            <p class="text-lg italic text-slate-700">"This product changed my life. I can't imagine working without it."</p>
            <footer class="mt-4 font-bold text-slate-900">- Jane Doe, CEO</footer>
          </blockquote>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Loved by Leaders</h3>
          <p class="mt-4 text-lg text-slate-600">See what industry experts are saying.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="w-full md:w-1/2">
          <blockquote class="bg-slate-50 p-8 rounded-xl border-l-4 border-primary-600">
            <p class="text-lg italic text-slate-700">"The best investment we've made this year. ROI was immediate."</p>
            <footer class="mt-4 font-bold text-slate-900">- John Smith, CTO</footer>
          </blockquote>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Proven Results</h3>
          <p class="mt-4 text-lg text-slate-600">Real feedback from real customers.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-047",
        "title": "Zigzag Cards",
        "description": "Card-based alternating",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-slate-50">
    <div class="max-w-4xl mx-auto px-6 space-y-12">
      <div class="bg-white p-8 rounded-xl shadow-lg ml-0 mr-12">
        <h3 class="text-2xl font-bold text-slate-900">Left Aligned Card</h3>
        <p class="mt-4 text-slate-600">Offsetting cards creates a dynamic flow.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg ml-12 mr-0">
        <h3 class="text-2xl font-bold text-slate-900">Right Aligned Card</h3>
        <p class="mt-4 text-slate-600">Keeps the eye moving down the page.</p>
      </div>
      <div class="bg-white p-8 rounded-xl shadow-lg ml-0 mr-12">
        <h3 class="text-2xl font-bold text-slate-900">Left Aligned Card</h3>
        <p class="mt-4 text-slate-600">Consistent rhythm.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-048",
        "title": "Zigzag with Video",
        "description": "Video alternating with text",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="aspect-video bg-black rounded-xl overflow-hidden shadow-lg">
             <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0"></iframe>
          </div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Video Demo</h3>
          <p class="mt-4 text-lg text-slate-600">Show, don't just tell.</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row-reverse items-center gap-12">
        <div class="w-full md:w-1/2">
          <div class="aspect-video bg-black rounded-xl overflow-hidden shadow-lg">
             <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0"></iframe>
          </div>
        </div>
        <div class="w-full md:w-1/2">
          <h3 class="text-3xl font-bold text-slate-900">Tutorial</h3>
          <p class="mt-4 text-lg text-slate-600">Walk users through the process.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-049",
        "title": "Zigzag Timeline",
        "description": "Timeline alternating layout",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6 relative">
      <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-200 -translate-x-1/2 hidden md:block"></div>

      <div class="space-y-12">
        <div class="flex flex-col md:flex-row items-center justify-between">
          <div class="w-full md:w-5/12 order-2 md:order-1 text-center md:text-right p-4">
            <h3 class="text-xl font-bold text-slate-900">Phase 1</h3>
            <p class="mt-2 text-slate-600">Initial planning and research.</p>
          </div>
          <div class="w-4 h-4 bg-primary-600 rounded-full border-4 border-white shadow order-1 md:order-2 z-10"></div>
          <div class="w-full md:w-5/12 order-3"></div>
        </div>

        <div class="flex flex-col md:flex-row items-center justify-between">
          <div class="w-full md:w-5/12 order-3 md:order-1"></div>
          <div class="w-4 h-4 bg-primary-600 rounded-full border-4 border-white shadow order-1 md:order-2 z-10"></div>
          <div class="w-full md:w-5/12 order-2 md:order-3 text-center md:text-left p-4">
            <h3 class="text-xl font-bold text-slate-900">Phase 2</h3>
            <p class="mt-2 text-slate-600">Development and testing.</p>
          </div>
        </div>

        <div class="flex flex-col md:flex-row items-center justify-between">
          <div class="w-full md:w-5/12 order-2 md:order-1 text-center md:text-right p-4">
            <h3 class="text-xl font-bold text-slate-900">Phase 3</h3>
            <p class="mt-2 text-slate-600">Launch and optimization.</p>
          </div>
          <div class="w-4 h-4 bg-primary-600 rounded-full border-4 border-white shadow order-1 md:order-2 z-10"></div>
          <div class="w-full md:w-5/12 order-3"></div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "feat-050",
        "title": "Zigzag with Animation",
        "description": "Scroll-animated alternating",
        "dir": "templates/03-features",
        "content": """<div class="py-24 bg-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-6 space-y-24">
      <div class="flex flex-col md:flex-row items-center gap-12 group">
        <div class="w-full md:w-1/2 transition-all duration-1000 -translate-x-12 opacity-0 group-hover:translate-x-0 group-hover:opacity-100">
          <div class="bg-primary-100 h-64 rounded-xl"></div>
        </div>
        <div class="w-full md:w-1/2 transition-all duration-1000 translate-x-12 opacity-0 group-hover:translate-x-0 group-hover:opacity-100">
          <h3 class="text-3xl font-bold text-slate-900">Slide In</h3>
          <p class="mt-4 text-lg text-slate-600">Elements animate in as you hover (simulating scroll reveal).</p>
        </div>
      </div>
      <div class="flex flex-col md:flex-row-reverse items-center gap-12 group">
        <div class="w-full md:w-1/2 transition-all duration-1000 translate-x-12 opacity-0 group-hover:translate-x-0 group-hover:opacity-100">
          <div class="bg-secondary-100 h-64 rounded-xl"></div>
        </div>
        <div class="w-full md:w-1/2 transition-all duration-1000 -translate-x-12 opacity-0 group-hover:translate-x-0 group-hover:opacity-100">
          <h3 class="text-3xl font-bold text-slate-900">Reverse Slide</h3>
          <p class="mt-4 text-lg text-slate-600">Coming from the other side.</p>
        </div>
      </div>
    </div>
  </div>"""
    }
]

# Part 3: Content 001-012
TEMPLATES_PART_3 = [
    {
        "id": "content-001",
        "title": "Single Column Article",
        "description": "Simple blog/article content",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-prose mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 mb-8">The Future of Web Design</h2>
      <div class="prose prose-slate prose-lg text-slate-600">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-002",
        "title": "Two Column Content",
        "description": "Side-by-side content sections",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12">
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Our Mission</h2>
        <div class="prose prose-slate text-slate-600">
          <p>We believe in making the web a better place for everyone. Our tools are designed to be accessible, performant, and easy to use.</p>
          <p>By empowering developers and designers, we can create experiences that delight users and drive results.</p>
        </div>
      </div>
      <div>
        <h2 class="text-3xl font-bold text-slate-900 mb-6">Our Vision</h2>
        <div class="prose prose-slate text-slate-600">
          <p>A world where anyone can build beautiful, functional websites without needing a degree in computer science.</p>
          <p>We are constantly innovating to bring you the latest technologies and best practices.</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-003",
        "title": "Content with Sidebar",
        "description": "Main content + sidebar",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-3 gap-12">
      <div class="lg:col-span-2">
        <h2 class="text-3xl font-bold text-slate-900 mb-8">Main Content Area</h2>
        <div class="prose prose-slate prose-lg text-slate-600">
          <p>This is where your primary content goes. It takes up two-thirds of the available width on large screens.</p>
          <p>Perfect for long-form articles, documentation, or product details.</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        </div>
      </div>
      <div class="space-y-8">
        <div class="bg-slate-50 p-6 rounded-xl">
          <h3 class="font-bold text-slate-900 mb-4">Related Articles</h3>
          <ul class="space-y-2 text-slate-600">
            <li><a href="#" class="hover:text-primary-600">Getting Started</a></li>
            <li><a href="#" class="hover:text-primary-600">Advanced Techniques</a></li>
            <li><a href="#" class="hover:text-primary-600">Case Studies</a></li>
          </ul>
        </div>
        <div class="bg-primary-50 p-6 rounded-xl">
          <h3 class="font-bold text-primary-900 mb-4">Subscribe</h3>
          <p class="text-primary-700 mb-4">Get the latest updates delivered to your inbox.</p>
          <input type="email" placeholder="Enter your email" class="w-full px-4 py-2 rounded-lg border-primary-200 focus:ring-primary-500 focus:border-primary-500">
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-004",
        "title": "Full Width Content",
        "description": "Edge-to-edge content section",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-slate-900 text-white">
    <div class="w-full px-6 md:px-12 lg:px-24 text-center">
      <h2 class="text-4xl md:text-5xl font-bold mb-8">Immersive Experience</h2>
      <p class="text-xl text-slate-300 max-w-3xl mx-auto">
        Sometimes you need to break out of the container. Use full-width sections to create impact and break up the rhythm of your page.
      </p>
    </div>
  </div>"""
    },
    {
        "id": "content-005",
        "title": "Narrow Centered Content",
        "description": "Focused reading width",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-2xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-slate-900 mb-6">Less is More</h2>
      <p class="text-lg text-slate-600 leading-relaxed">
        By constraining the width of your content, you improve readability and focus. The eye doesn't have to travel as far across the screen, making for a more comfortable reading experience.
      </p>
    </div>
  </div>"""
    },
    {
        "id": "content-006",
        "title": "Content with Drop Cap",
        "description": "Editorial style with drop cap",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-prose mx-auto px-6">
      <div class="prose prose-slate prose-lg text-slate-600">
        <p class="first-letter:text-7xl first-letter:font-bold first-letter:text-slate-900 first-letter:float-left first-letter:mr-3 first-letter:mt-[-10px]">
          Once upon a time, in a digital landscape far, far away, designers struggled to make text look interesting. Then came the drop cap, a classic typographic element that adds a touch of elegance and sophistication to any layout.
        </p>
        <p>It signals the start of a new chapter or section and draws the reader's eye into the text.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-007",
        "title": "Multi-Column Text",
        "description": "Newspaper-style columns",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-slate-900 mb-12 text-center">The Daily News</h2>
      <div class="columns-1 md:columns-2 lg:columns-3 gap-12 space-y-12 text-slate-600">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
        <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-008",
        "title": "Content with Footnotes",
        "description": "Academic-style with footnotes",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-prose mx-auto px-6">
      <div class="prose prose-slate text-slate-600 mb-12">
        <p>
          The study of user interface design has evolved significantly over the last decade<sup class="text-primary-600 font-bold cursor-pointer">[1]</sup>.
          Researchers have found that simplicity often correlates with higher conversion rates<sup class="text-primary-600 font-bold cursor-pointer">[2]</sup>.
        </p>
      </div>
      <div class="border-t border-slate-200 pt-8">
        <h3 class="text-sm font-bold text-slate-900 uppercase tracking-wide mb-4">References</h3>
        <ol class="list-decimal list-inside text-sm text-slate-500 space-y-2">
          <li>Nielsen, J. (2010). <em>Usability Engineering</em>. Morgan Kaufmann.</li>
          <li>Norman, D. (2013). <em>The Design of Everyday Things</em>. Basic Books.</li>
        </ol>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-009",
        "title": "Content with Table of Contents",
        "description": "Long content with TOC",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-4 gap-12">
      <div class="hidden lg:block">
        <div class="sticky top-24">
          <h3 class="font-bold text-slate-900 mb-4">Contents</h3>
          <ul class="space-y-2 text-slate-600 border-l-2 border-slate-200 pl-4">
            <li><a href="#intro" class="block hover:text-primary-600 hover:border-l-2 hover:border-primary-600 -ml-[18px] pl-4 transition-all">Introduction</a></li>
            <li><a href="#method" class="block hover:text-primary-600 hover:border-l-2 hover:border-primary-600 -ml-[18px] pl-4 transition-all">Methodology</a></li>
            <li><a href="#results" class="block hover:text-primary-600 hover:border-l-2 hover:border-primary-600 -ml-[18px] pl-4 transition-all">Results</a></li>
            <li><a href="#conclusion" class="block hover:text-primary-600 hover:border-l-2 hover:border-primary-600 -ml-[18px] pl-4 transition-all">Conclusion</a></li>
          </ul>
        </div>
      </div>
      <div class="lg:col-span-3 prose prose-slate max-w-none">
        <h2 id="intro">Introduction</h2>
        <p>Lorem ipsum dolor sit amet...</p>
        <h2 id="method">Methodology</h2>
        <p>Consectetur adipiscing elit...</p>
        <h2 id="results">Results</h2>
        <p>Sed do eiusmod tempor incididunt...</p>
        <h2 id="conclusion">Conclusion</h2>
        <p>Ut labore et dolore magna aliqua...</p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-010",
        "title": "Content with Annotations",
        "description": "Content with inline notes",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-prose mx-auto px-6">
      <div class="prose prose-slate text-slate-600">
        <p>
          We utilize a
          <span class="relative group cursor-help border-b border-dotted border-slate-400">
            polymorphic
            <span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 p-2 bg-slate-900 text-white text-xs rounded shadow-lg opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10">
              Occurring in several different forms.
              <svg class="absolute top-full left-1/2 -translate-x-1/2 -mt-1 text-slate-900 h-2 w-4" fill="currentColor" viewBox="0 0 24 12"><path d="M12 12L0 0h24L12 12z"/></svg>
            </span>
          </span>
          approach to component design. This allows for maximum flexibility.
        </p>
        <p>
          Our system is built on
          <span class="relative group cursor-help border-b border-dotted border-slate-400">
            atomic principles
            <span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 p-2 bg-slate-900 text-white text-xs rounded shadow-lg opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10">
              Breaking down interfaces into their smallest fundamental parts.
              <svg class="absolute top-full left-1/2 -translate-x-1/2 -mt-1 text-slate-900 h-2 w-4" fill="currentColor" viewBox="0 0 24 12"><path d="M12 12L0 0h24L12 12z"/></svg>
            </span>
          </span>
          to ensure consistency.
        </p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "content-011",
        "title": "Full Width Image",
        "description": "Edge-to-edge image section",
        "dir": "templates/04-content",
        "content": """<div class="py-12 bg-white">
    <div class="w-full h-96 md:h-[600px]">
      <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=2000" class="w-full h-full object-cover" alt="Office Space">
    </div>
    <div class="max-w-7xl mx-auto px-6 mt-8">
      <p class="text-sm text-slate-500 text-right">Photo by Unsplash</p>
    </div>
  </div>"""
    },
    {
        "id": "content-012",
        "title": "Image with Caption",
        "description": "Image with descriptive caption",
        "dir": "templates/04-content",
        "content": """<div class="py-24 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <figure>
        <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80" class="w-full rounded-xl shadow-lg" alt="Team Meeting">
        <figcaption class="mt-4 text-center text-slate-600 italic">
          The team discussing the roadmap for Q4 2024.
        </figcaption>
      </figure>
    </div>
  </div>"""
    }
]

# Combine all templates
TEMPLATES = TEMPLATES_PART_1 + TEMPLATES_PART_2 + TEMPLATES_PART_3

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
