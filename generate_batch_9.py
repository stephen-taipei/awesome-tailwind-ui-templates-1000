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

# Part 1: Modals 001-050
TEMPLATES_MODALS_1 = [
    {
        "id": "modal-001",
        "title": "Basic Modal",
        "description": "Simple centered modal with title and content.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <!-- Background backdrop -->
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <!-- Modal panel -->
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Deactivate account</h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">Are you sure you want to deactivate your account? All of your data will be permanently removed. This action cannot be undone.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto">Deactivate</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-002",
        "title": "Success Modal",
        "description": "Modal for success message.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
          <div>
            <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-green-100">
              <svg class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
              </svg>
            </div>
            <div class="mt-3 text-center sm:mt-5">
              <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Payment successful</h3>
              <div class="mt-2">
                <p class="text-sm text-gray-500">Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur amet labore.</p>
              </div>
            </div>
          </div>
          <div class="mt-5 sm:mt-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Go back to dashboard</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-003",
        "title": "Form Modal",
        "description": "Modal with a form.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <h3 class="text-lg font-semibold leading-6 text-gray-900 mb-4" id="modal-title">Edit Profile</h3>
            <form>
              <div class="space-y-4">
                <div>
                  <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
                  <div class="mt-2">
                    <input type="text" name="name" id="name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Your Name">
                  </div>
                </div>
                <div>
                  <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                  <div class="mt-2">
                    <input type="email" name="email" id="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="you@example.com">
                  </div>
                </div>
              </div>
            </form>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Save Changes</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-004",
        "title": "Large Content Modal",
        "description": "Modal with scrollable content.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <h3 class="text-xl font-semibold leading-6 text-gray-900 mb-4" id="modal-title">Terms of Service</h3>
            <div class="mt-2 h-64 overflow-y-auto prose prose-sm text-gray-500">
              <p>Last modified: January 1, 2024</p>
              <h4>1. Introduction</h4>
              <p>Welcome to our website. If you continue to browse and use this website, you are agreeing to comply with and be bound by the following terms and conditions of use.</p>
              <h4>2. Use License</h4>
              <p>Permission is granted to temporarily download one copy of the materials (information or software) on our website for personal, non-commercial transitory viewing only.</p>
              <h4>3. Disclaimer</h4>
              <p>The materials on our website are provided on an 'as is' basis. We make no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</p>
              <h4>4. Limitations</h4>
              <p>In no event shall we or our suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on our website.</p>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
              <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">I Agree</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Decline</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-005",
        "title": "Video Modal",
        "description": "Modal with embedded video.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-90 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-black text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-4xl">
          <div class="aspect-w-16 aspect-h-9">
            <iframe class="w-full h-full" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
          </div>
          <button type="button" class="absolute top-0 right-0 m-4 text-white hover:text-gray-300">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-006",
        "title": "Search Modal",
        "description": "Command palette style search modal.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-25 transition-opacity"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto p-4 sm:p-6 md:p-20">
      <div class="mx-auto max-w-xl transform divide-y divide-gray-100 overflow-hidden rounded-xl bg-white shadow-2xl ring-1 ring-black ring-opacity-5 transition-all">
        <div class="relative">
          <svg class="pointer-events-none absolute left-4 top-3.5 h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" clip-rule="evenodd" />
          </svg>
          <input type="text" class="h-12 w-full border-0 bg-transparent pl-11 pr-4 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm" placeholder="Search..." role="combobox" aria-expanded="false" aria-controls="options">
        </div>

        <ul class="max-h-72 scroll-py-2 overflow-y-auto py-2 text-sm text-gray-800" id="options" role="listbox">
          <li class="cursor-default select-none px-4 py-2 hover:bg-indigo-600 hover:text-white" id="option-1" role="option" tabindex="-1">
            <a href="#">Dashboard</a>
          </li>
          <li class="cursor-default select-none px-4 py-2 hover:bg-indigo-600 hover:text-white" id="option-2" role="option" tabindex="-1">
            <a href="#">Projects</a>
          </li>
          <li class="cursor-default select-none px-4 py-2 hover:bg-indigo-600 hover:text-white" id="option-3" role="option" tabindex="-1">
            <a href="#">Calendar</a>
          </li>
          <li class="cursor-default select-none px-4 py-2 hover:bg-indigo-600 hover:text-white" id="option-4" role="option" tabindex="-1">
            <a href="#">Settings</a>
          </li>
        </ul>

        <div class="flex flex-wrap items-center bg-gray-50 px-4 py-2.5 text-xs text-gray-700">
            Type <kbd class="mx-1 flex h-5 w-5 items-center justify-center rounded border bg-white font-semibold sm:mx-2 border-gray-400 text-gray-900">#</kbd> <span class="sm:hidden">for projects,</span><span class="hidden sm:inline">for projects,</span>
            <kbd class="mx-1 flex h-5 w-5 items-center justify-center rounded border bg-white font-semibold sm:mx-2 border-gray-400 text-gray-900">&gt;</kbd> for commands
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-007",
        "title": "Pricing Modal",
        "description": "Modal with pricing options.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl">
          <div class="px-6 py-8 sm:p-10 sm:pb-6">
             <div class="sm:flex sm:items-center sm:justify-between">
                <h3 class="text-xl font-semibold leading-6 text-gray-900" id="modal-title">Change Plan</h3>
                <div class="mt-4 sm:ml-4 sm:mt-0">
                   <button type="button" class="text-gray-400 hover:text-gray-500">
                     <span class="sr-only">Close</span>
                     <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                     </svg>
                   </button>
                </div>
             </div>
             <div class="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-3">
                <div class="relative flex cursor-pointer rounded-lg border bg-white p-4 shadow-sm focus:outline-none border-gray-300">
                  <span class="flex flex-1">
                    <span class="flex flex-col">
                      <span class="block text-sm font-medium text-gray-900">Hobby</span>
                      <span class="mt-1 flex items-center text-sm text-gray-500">For personal use</span>
                      <span class="mt-6 text-sm font-medium text-gray-900">$19/mo</span>
                    </span>
                  </span>
                  <svg class="h-5 w-5 text-indigo-600 hidden" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
                  </svg>
                  <span class="pointer-events-none absolute -inset-px rounded-lg border-2 border-transparent" aria-hidden="true"></span>
                </div>
                <div class="relative flex cursor-pointer rounded-lg border bg-white p-4 shadow-sm focus:outline-none border-indigo-600 ring-2 ring-indigo-600">
                  <span class="flex flex-1">
                    <span class="flex flex-col">
                      <span class="block text-sm font-medium text-gray-900">Professional</span>
                      <span class="mt-1 flex items-center text-sm text-gray-500">For small teams</span>
                      <span class="mt-6 text-sm font-medium text-gray-900">$49/mo</span>
                    </span>
                  </span>
                  <svg class="h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
                  </svg>
                  <span class="pointer-events-none absolute -inset-px rounded-lg border-2 border-transparent" aria-hidden="true"></span>
                </div>
                <div class="relative flex cursor-pointer rounded-lg border bg-white p-4 shadow-sm focus:outline-none border-gray-300">
                  <span class="flex flex-1">
                    <span class="flex flex-col">
                      <span class="block text-sm font-medium text-gray-900">Enterprise</span>
                      <span class="mt-1 flex items-center text-sm text-gray-500">For large organizations</span>
                      <span class="mt-6 text-sm font-medium text-gray-900">$99/mo</span>
                    </span>
                  </span>
                  <svg class="h-5 w-5 text-indigo-600 hidden" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
                  </svg>
                  <span class="pointer-events-none absolute -inset-px rounded-lg border-2 border-transparent" aria-hidden="true"></span>
                </div>
             </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
             <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Update Plan</button>
             <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-008",
        "title": "Image Lightbox",
        "description": "Modal for viewing an image.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-black bg-opacity-90 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center">
        <div class="relative transform overflow-hidden rounded-lg text-left shadow-xl transition-all max-w-5xl">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80" alt="Full size image" class="max-h-[85vh] w-auto">
          <button type="button" class="absolute top-4 right-4 text-white hover:text-gray-300 bg-black bg-opacity-50 rounded-full p-2">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="absolute bottom-4 left-4 text-white bg-black bg-opacity-50 px-3 py-1 rounded">
             <p class="text-sm font-medium">Photo by Unsplash</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-009",
        "title": "Cookie Consent",
        "description": "Bottom-aligned cookie consent modal.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10">
    <div class="pointer-events-none fixed inset-x-0 bottom-0 px-6 pb-6">
      <div class="pointer-events-auto max-w-xl rounded-xl bg-white p-6 shadow-lg ring-1 ring-gray-900/10 ml-auto">
        <p class="text-sm leading-6 text-gray-900">This website uses cookies to supplement a balanced diet and provide a much deserved reward to the senses after consuming too much hidden spinach.</p>
        <div class="mt-4 flex items-center gap-x-5">
          <button type="button" class="rounded-md bg-gray-900 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-900">Accept all</button>
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Reject all</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-010",
        "title": "Date Picker Modal",
        "description": "Modal with calendar for date selection.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
          <div class="bg-white p-6">
            <h3 class="text-base font-semibold leading-6 text-gray-900 mb-4" id="modal-title">Select Date</h3>
            <div class="mt-2">
               <!-- Simple Calendar Header -->
               <div class="flex items-center justify-between mb-4">
                  <button class="text-gray-500 hover:text-gray-900">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                    </svg>
                  </button>
                  <span class="text-lg font-bold text-gray-900">October 2023</span>
                  <button class="text-gray-500 hover:text-gray-900">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                    </svg>
                  </button>
               </div>
               <!-- Calendar Grid -->
               <div class="grid grid-cols-7 gap-2 text-center text-sm">
                  <div class="text-gray-500 font-medium">Su</div>
                  <div class="text-gray-500 font-medium">Mo</div>
                  <div class="text-gray-500 font-medium">Tu</div>
                  <div class="text-gray-500 font-medium">We</div>
                  <div class="text-gray-500 font-medium">Th</div>
                  <div class="text-gray-500 font-medium">Fr</div>
                  <div class="text-gray-500 font-medium">Sa</div>

                  <div class="text-gray-300 py-2">29</div>
                  <div class="text-gray-300 py-2">30</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">1</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">2</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">3</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">4</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">5</div>

                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">6</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">7</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">8</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">9</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">10</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">11</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">12</div>

                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">13</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">14</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">15</div>
                  <div class="bg-indigo-600 text-white rounded-full py-2 cursor-pointer">16</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">17</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">18</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">19</div>

                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">20</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">21</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">22</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">23</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">24</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">25</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">26</div>

                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">27</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">28</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">29</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">30</div>
                  <div class="py-2 hover:bg-gray-100 rounded cursor-pointer">31</div>
                  <div class="text-gray-300 py-2">1</div>
                  <div class="text-gray-300 py-2">2</div>
               </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Select</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_MODALS_2 = [
    {
        "id": "modal-011",
        "title": "Feedback Modal",
        "description": "Modal for collecting user feedback.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="text-center">
              <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Your feedback matters</h3>
              <div class="mt-2">
                <p class="text-sm text-gray-500">How would you rate your experience with our product?</p>
              </div>
              <div class="flex justify-center gap-4 mt-6">
                 <button class="text-2xl hover:scale-110 transition-transform">😠</button>
                 <button class="text-2xl hover:scale-110 transition-transform">🙁</button>
                 <button class="text-2xl hover:scale-110 transition-transform">😐</button>
                 <button class="text-2xl hover:scale-110 transition-transform">🙂</button>
                 <button class="text-2xl hover:scale-110 transition-transform">😍</button>
              </div>
              <div class="mt-4">
                 <textarea rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Tell us more about your experience..."></textarea>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Submit Feedback</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-012",
        "title": "Share Modal",
        "description": "Modal with social sharing options.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <h3 class="text-base font-semibold leading-6 text-gray-900 mb-4" id="modal-title">Share this project</h3>
            <div class="grid grid-cols-2 gap-4">
               <button class="flex items-center justify-center gap-2 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50">
                  <svg class="h-5 w-5 text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                  Twitter
               </button>
               <button class="flex items-center justify-center gap-2 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50">
                  <svg class="h-5 w-5 text-blue-700" fill="currentColor" viewBox="0 0 24 24"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>
                  Facebook
               </button>
               <button class="flex items-center justify-center gap-2 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50">
                  <svg class="h-5 w-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  LinkedIn
               </button>
               <button class="flex items-center justify-center gap-2 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50">
                  <svg class="h-5 w-5 text-gray-900" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                  Copy Link
               </button>
            </div>
            <div class="mt-4">
                <label for="link" class="block text-sm font-medium leading-6 text-gray-900">Function to copy link</label>
                <div class="mt-2 flex rounded-md shadow-sm">
                  <span class="inline-flex items-center rounded-l-md border border-r-0 border-gray-300 px-3 text-gray-500 sm:text-sm bg-gray-50">http://</span>
                  <input type="text" name="link" id="link" class="block w-full min-w-0 flex-1 rounded-none rounded-r-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" value="example.com/project/123" readonly>
                </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-013",
        "title": "Welcome Modal",
        "description": "Welcome modal for new users.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
           <div class="relative">
              <img src="https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Welcome" class="w-full h-48 object-cover">
              <button class="absolute top-4 right-4 bg-white rounded-full p-1 text-gray-500 hover:text-gray-900">
                 <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                 </svg>
              </button>
           </div>
           <div class="px-6 py-6">
              <h3 class="text-2xl font-bold text-gray-900 mb-2">Welcome to our platform!</h3>
              <p class="text-gray-500 mb-6">We're thrilled to have you on board. Take a quick tour to learn how to get the most out of our tools.</p>
              <div class="flex flex-col gap-3">
                 <button type="button" class="w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Start Tour</button>
                 <button type="button" class="w-full rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Skip for now</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-014",
        "title": "Two-Factor Auth Modal",
        "description": "Modal for 2FA code entry.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md sm:p-6">
           <div class="text-center">
              <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-blue-100 mb-4">
                 <svg class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                 </svg>
              </div>
              <h3 class="text-lg font-semibold leading-6 text-gray-900">Two-Factor Authentication</h3>
              <p class="mt-2 text-sm text-gray-500">We've sent a code to your email. Please enter it below to verify your identity.</p>
              <div class="mt-6 flex justify-center gap-2">
                 <input type="text" class="w-12 h-12 text-center text-2xl border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500" maxlength="1">
                 <input type="text" class="w-12 h-12 text-center text-2xl border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500" maxlength="1">
                 <input type="text" class="w-12 h-12 text-center text-2xl border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500" maxlength="1">
                 <input type="text" class="w-12 h-12 text-center text-2xl border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500" maxlength="1">
                 <input type="text" class="w-12 h-12 text-center text-2xl border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500" maxlength="1">
                 <input type="text" class="w-12 h-12 text-center text-2xl border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500" maxlength="1">
              </div>
              <div class="mt-6">
                 <button type="button" class="inline-flex w-full justify-center rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500">Verify Code</button>
              </div>
              <p class="mt-4 text-sm text-gray-500">
                 Didn't receive the code? <a href="#" class="font-semibold text-blue-600 hover:text-blue-500">Resend</a>
              </p>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-015",
        "title": "Cart/Checkout Modal",
        "description": "Available cart items modal.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="slide-over-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 overflow-hidden">
      <div class="absolute inset-0 overflow-hidden">
        <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
          <div class="pointer-events-auto w-screen max-w-md">
            <div class="flex h-full flex-col overflow-y-scroll bg-white shadow-xl">
              <div class="flex-1 overflow-y-auto px-4 py-6 sm:px-6">
                <div class="flex items-start justify-between">
                  <h2 class="text-lg font-medium text-gray-900" id="slide-over-title">Shopping cart</h2>
                  <div class="ml-3 flex h-7 items-center">
                    <button type="button" class="relative -m-2 p-2 text-gray-400 hover:text-gray-500">
                      <span class="absolute -inset-0.5"></span>
                      <span class="sr-only">Close panel</span>
                      <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                    </button>
                  </div>
                </div>

                <div class="mt-8">
                  <div class="flow-root">
                    <ul role="list" class="-my-6 divide-y divide-gray-200">
                      <li class="flex py-6">
                        <div class="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200">
                          <img src="https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-01.jpg" alt="Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt." class="h-full w-full object-cover object-center">
                        </div>

                        <div class="ml-4 flex flex-1 flex-col">
                          <div>
                            <div class="flex justify-between text-base font-medium text-gray-900">
                              <h3>
                                <a href="#">Throwback Hip Bag</a>
                              </h3>
                              <p class="ml-4">$90.00</p>
                            </div>
                            <p class="mt-1 text-sm text-gray-500">Salmon</p>
                          </div>
                          <div class="flex flex-1 items-end justify-between text-sm">
                            <p class="text-gray-500">Qty 1</p>

                            <div class="flex">
                              <button type="button" class="font-medium text-indigo-600 hover:text-indigo-500">Remove</button>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li class="flex py-6">
                        <div class="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200">
                          <img src="https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-02.jpg" alt="Front of satchel with blue canvas body, black straps and handle, drawstring top, and front zipper pouch." class="h-full w-full object-cover object-center">
                        </div>

                        <div class="ml-4 flex flex-1 flex-col">
                          <div>
                            <div class="flex justify-between text-base font-medium text-gray-900">
                              <h3>
                                <a href="#">Medium Stuff Satchel</a>
                              </h3>
                              <p class="ml-4">$32.00</p>
                            </div>
                            <p class="mt-1 text-sm text-gray-500">Blue</p>
                          </div>
                          <div class="flex flex-1 items-end justify-between text-sm">
                            <p class="text-gray-500">Qty 1</p>

                            <div class="flex">
                              <button type="button" class="font-medium text-indigo-600 hover:text-indigo-500">Remove</button>
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>

              <div class="border-t border-gray-200 px-4 py-6 sm:px-6">
                <div class="flex justify-between text-base font-medium text-gray-900">
                  <p>Subtotal</p>
                  <p>$262.00</p>
                </div>
                <p class="mt-0.5 text-sm text-gray-500">Shipping and taxes calculated at checkout.</p>
                <div class="mt-6">
                  <a href="#" class="flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700">Checkout</a>
                </div>
                <div class="mt-6 flex justify-center text-center text-sm text-gray-500">
                  <p>
                    or
                    <button type="button" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Continue Shopping
                      <span aria-hidden="true"> &rarr;</span>
                    </button>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-016",
        "title": "Profile Switcher",
        "description": "Modal to switch user profiles.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="px-4 py-5 sm:p-6">
              <h3 class="text-base font-semibold leading-6 text-gray-900 mb-4">Switch Account</h3>
              <ul class="divide-y divide-gray-100">
                 <li class="flex items-center justify-between gap-x-6 py-3 hover:bg-gray-50 px-2 -mx-2 rounded-md cursor-pointer">
                    <div class="flex min-w-0 gap-x-4">
                       <img class="h-10 w-10 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                       <div class="min-w-0 flex-auto">
                          <p class="text-sm font-semibold leading-6 text-gray-900">Leslie Alexander</p>
                          <p class="mt-1 truncate text-xs leading-5 text-gray-500">leslie.alexander@example.com</p>
                       </div>
                    </div>
                    <div class="h-2 w-2 rounded-full bg-emerald-500"></div>
                 </li>
                 <li class="flex items-center justify-between gap-x-6 py-3 hover:bg-gray-50 px-2 -mx-2 rounded-md cursor-pointer">
                    <div class="flex min-w-0 gap-x-4">
                       <div class="h-10 w-10 flex-none rounded-full bg-gray-200 flex items-center justify-center text-gray-500">MA</div>
                       <div class="min-w-0 flex-auto">
                          <p class="text-sm font-semibold leading-6 text-gray-900">Michael Armstrong</p>
                          <p class="mt-1 truncate text-xs leading-5 text-gray-500">michael.a@example.com</p>
                       </div>
                    </div>
                 </li>
                 <li class="flex items-center justify-between gap-x-6 py-3 hover:bg-gray-50 px-2 -mx-2 rounded-md cursor-pointer">
                    <div class="flex min-w-0 gap-x-4">
                       <div class="h-10 w-10 flex-none rounded-full bg-gray-200 flex items-center justify-center text-gray-500">
                         <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                         </svg>
                       </div>
                       <div class="min-w-0 flex-auto flex items-center">
                          <p class="text-sm font-semibold leading-6 text-gray-900">Add another account</p>
                       </div>
                    </div>
                 </li>
              </ul>
           </div>
           <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6 border-t border-gray-200">
             <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-017",
        "title": "Delete Confirmation",
        "description": "Danger zone delete confirmation.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg ring-1 ring-red-500 ring-opacity-20">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Delete Project</h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">Unless you are absolutely sure, please don't do this. This action cannot be undone. This will permanently delete the project <span class="font-bold">"Marketing 2024"</span>, database, and remove all collaborator associations.</p>
                </div>
                <div class="mt-4">
                   <label for="verification" class="block text-sm font-medium leading-6 text-gray-900">Please type <span class="font-bold select-none">delete/marketing-2024</span> to confirm.</label>
                   <div class="mt-2">
                     <input type="text" name="verification" id="verification" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-red-600 sm:text-sm sm:leading-6">
                   </div>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto opacity-50 cursor-not-allowed">I understand, delete this project</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-018",
        "title": "Filter Modal",
        "description": "Modal with filter options.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="flex items-center justify-between mb-5">
              <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Filter Results</h3>
              <button class="text-gray-400 hover:text-gray-500">Clear all</button>
            </div>

            <div class="space-y-6">
              <div>
                 <h4 class="text-sm font-medium text-gray-900 mb-3">Category</h4>
                 <div class="flex flex-wrap gap-2">
                    <span class="inline-flex items-center rounded-full bg-indigo-50 px-2 py-1 text-xs font-medium text-indigo-700 ring-1 ring-inset ring-indigo-700/10 cursor-pointer">Electronics</span>
                    <span class="inline-flex items-center rounded-full bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10 cursor-pointer hover:bg-gray-100">Clothing</span>
                    <span class="inline-flex items-center rounded-full bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10 cursor-pointer hover:bg-gray-100">Books</span>
                    <span class="inline-flex items-center rounded-full bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10 cursor-pointer hover:bg-gray-100">Home</span>
                 </div>
              </div>

              <div>
                 <h4 class="text-sm font-medium text-gray-900 mb-3">Price Range</h4>
                 <div class="grid grid-cols-2 gap-4">
                    <div>
                       <label for="min-price" class="sr-only">Min Price</label>
                       <div class="relative rounded-md shadow-sm">
                          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                             <span class="text-gray-500 sm:text-sm">$</span>
                          </div>
                          <input type="text" name="min-price" id="min-price" class="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="0">
                       </div>
                    </div>
                    <div>
                       <label for="max-price" class="sr-only">Max Price</label>
                       <div class="relative rounded-md shadow-sm">
                          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                             <span class="text-gray-500 sm:text-sm">$</span>
                          </div>
                          <input type="text" name="max-price" id="max-price" class="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="1000">
                       </div>
                    </div>
                 </div>
              </div>

               <div>
                 <h4 class="text-sm font-medium text-gray-900 mb-3">Rating</h4>
                 <div class="space-y-2">
                    <div class="flex items-center">
                       <input id="filter-rating-4" name="rating[]" value="4" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                       <label for="filter-rating-4" class="ml-3 text-sm text-gray-600 flex items-center">4 Stars & up <span class="text-yellow-400 ml-1">★★★★☆</span></label>
                    </div>
                    <div class="flex items-center">
                       <input id="filter-rating-3" name="rating[]" value="3" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                       <label for="filter-rating-3" class="ml-3 text-sm text-gray-600 flex items-center">3 Stars & up <span class="text-yellow-400 ml-1">★★★☆☆</span></label>
                    </div>
                 </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Apply Filters</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-019",
        "title": "Onboarding Steps Modal",
        "description": "Multi-step onboarding modal.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6">
             <div class="mb-5">
               <nav aria-label="Progress">
                 <ol role="list" class="space-y-4 md:flex md:space-x-8 md:space-y-0 text-center justify-center">
                   <li class="md:flex-1">
                     <span class="flex flex-col border-b-4 border-indigo-600 py-2 pl-4 md:border-b-4 md:border-l-0 md:pl-0 md:pb-4 md:pt-4">
                       <span class="text-sm font-medium text-indigo-600">Step 1</span>
                       <span class="text-sm font-medium">Account</span>
                     </span>
                   </li>
                   <li class="md:flex-1">
                     <span class="flex flex-col border-b-4 border-gray-200 py-2 pl-4 md:border-b-4 md:border-l-0 md:pl-0 md:pb-4 md:pt-4">
                       <span class="text-sm font-medium text-gray-500">Step 2</span>
                       <span class="text-sm font-medium">Profile</span>
                     </span>
                   </li>
                   <li class="md:flex-1">
                     <span class="flex flex-col border-b-4 border-gray-200 py-2 pl-4 md:border-b-4 md:border-l-0 md:pl-0 md:pb-4 md:pt-4">
                       <span class="text-sm font-medium text-gray-500">Step 3</span>
                       <span class="text-sm font-medium">Theme</span>
                     </span>
                   </li>
                 </ol>
               </nav>
             </div>

             <div class="mt-4">
                <h3 class="text-lg font-medium leading-6 text-gray-900">Account Details</h3>
                <p class="mt-1 text-sm text-gray-500">Let's get your account set up properly.</p>

                <form class="mt-4 space-y-4">
                   <div>
                      <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
                      <div class="mt-2">
                         <input type="text" name="username" id="username" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="janesmith">
                      </div>
                   </div>
                   <div>
                      <label for="about" class="block text-sm font-medium leading-6 text-gray-900">Short Bio</label>
                      <div class="mt-2">
                         <input type="text" name="about" id="about" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="I love coding...">
                      </div>
                   </div>
                </form>
             </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Next Step</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Skip</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-020",
        "title": "API Key Modal",
        "description": "Modal for creating and showing API keys.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-yellow-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left w-full">
                <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">API Key Created</h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">Please copy your API key now. You won't be able to see it again.</p>

                  <div class="mt-4 relative rounded-md shadow-sm">
                    <input type="text" name="apikey" id="apikey" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-gray-50 font-mono" value="sk_test_51Mz9...a8Bc3d" readonly>
                    <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                       <button type="button" class="text-gray-400 hover:text-gray-600">
                         <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                         </svg>
                       </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Done</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_MODALS_3 = [
    {
        "id": "modal-021",
        "title": "Announcement Modal",
        "description": "Modal for major announcements or updates.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6">
              <div class="flex items-center justify-between mb-4">
                 <h3 class="text-xl font-bold text-gray-900">🚀 Big News!</h3>
                 <button class="text-gray-400 hover:text-gray-500"><svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg></button>
              </div>
              <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Announcement" class="w-full h-40 object-cover rounded-lg mb-4">
              <p class="text-gray-600 mb-4">We've just launched our new mobile app! It's packed with features to help you manage your projects on the go.</p>
              <div class="flex gap-4">
                 <button class="flex-1 bg-indigo-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-indigo-500">Download for iOS</button>
                 <button class="flex-1 bg-white border border-gray-300 text-gray-700 font-semibold py-2 px-4 rounded-md hover:bg-gray-50">Download for Android</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-022",
        "title": "Upgrade Upsell Modal",
        "description": "Modal encouraging user to upgrade.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="bg-gradient-to-r from-purple-600 to-indigo-600 p-6 text-white text-center">
              <svg class="h-12 w-12 mx-auto mb-4 text-yellow-300" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 2a1 1 0 011 1v1h1a1 1 0 010 2H6v1a1 1 0 01-2 0V6H3a1 1 0 010-2h1V3a1 1 0 011-1zm0 5a1 1 0 011 1v1h1a1 1 0 010 2H6v1a1 1 0 01-2 0V11H3a1 1 0 010-2h1V9a1 1 0 011-1zm5 0a1 1 0 011 1v1h1a1 1 0 010 2h-1v1a1 1 0 01-2 0v-1h-1a1 1 0 010-2h1V9a1 1 0 011-1zm5 0a1 1 0 011 1v1h1a1 1 0 010 2h-1v1a1 1 0 01-2 0v-1h-1a1 1 0 010-2h1V9a1 1 0 011-1z" clip-rule="evenodd"/></svg>
              <h3 class="text-2xl font-bold mb-2">Unlock Premium Features</h3>
              <p class="text-purple-100">Get access to advanced analytics, unlimited projects, and priority support.</p>
           </div>
           <div class="p-6">
              <ul class="space-y-3 text-gray-600 mb-6">
                 <li class="flex items-center"><svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg> Unlimited Projects</li>
                 <li class="flex items-center"><svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg> Advanced Analytics Dashboard</li>
                 <li class="flex items-center"><svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg> 24/7 Priority Support</li>
              </ul>
              <button class="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg shadow hover:bg-indigo-500 transition-colors">Upgrade Now - $29/mo</button>
              <button class="w-full mt-3 text-gray-500 text-sm hover:text-gray-700">No thanks, I'll stay on the free plan</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-023",
        "title": "Language Selection",
        "description": "Modal to select interface language.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm">
           <div class="px-4 py-5 sm:p-6">
              <h3 class="text-base font-semibold leading-6 text-gray-900 mb-4">Select Language</h3>
              <div class="space-y-2">
                 <button class="flex items-center justify-between w-full p-3 rounded-md border border-indigo-600 bg-indigo-50 text-indigo-700">
                    <div class="flex items-center">
                       <span class="text-xl mr-3">🇺🇸</span>
                       <span class="font-medium">English</span>
                    </div>
                    <svg class="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                 </button>
                 <button class="flex items-center justify-between w-full p-3 rounded-md border border-gray-200 hover:bg-gray-50 text-gray-700">
                    <div class="flex items-center">
                       <span class="text-xl mr-3">🇪🇸</span>
                       <span class="font-medium">Español</span>
                    </div>
                 </button>
                 <button class="flex items-center justify-between w-full p-3 rounded-md border border-gray-200 hover:bg-gray-50 text-gray-700">
                    <div class="flex items-center">
                       <span class="text-xl mr-3">🇫🇷</span>
                       <span class="font-medium">Français</span>
                    </div>
                 </button>
                 <button class="flex items-center justify-between w-full p-3 rounded-md border border-gray-200 hover:bg-gray-50 text-gray-700">
                    <div class="flex items-center">
                       <span class="text-xl mr-3">🇩🇪</span>
                       <span class="font-medium">Deutsch</span>
                    </div>
                 </button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-024",
        "title": "Date Range Picker",
        "description": "Modal with double calendar for range.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
           <div class="p-6">
              <div class="flex items-center justify-between mb-6">
                 <h3 class="text-base font-semibold text-gray-900">Select Dates</h3>
                 <div class="flex gap-2 text-sm text-gray-500">
                    <span class="px-2 py-1 bg-gray-100 rounded">Oct 16, 2023</span>
                    <span>-</span>
                    <span class="px-2 py-1 bg-gray-100 rounded">Oct 23, 2023</span>
                 </div>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                 <!-- Calendar 1 -->
                 <div>
                    <div class="text-center font-semibold text-gray-900 mb-4">October 2023</div>
                    <div class="grid grid-cols-7 gap-1 text-center text-xs">
                       <div class="text-gray-400 py-1">Su</div><div class="text-gray-400 py-1">Mo</div><div class="text-gray-400 py-1">Tu</div><div class="text-gray-400 py-1">We</div><div class="text-gray-400 py-1">Th</div><div class="text-gray-400 py-1">Fr</div><div class="text-gray-400 py-1">Sa</div>
                       <div class="text-gray-300 py-1">29</div><div class="text-gray-300 py-1">30</div><div class="py-1">1</div><div class="py-1">2</div><div class="py-1">3</div><div class="py-1">4</div><div class="py-1">5</div>
                       <div class="py-1">6</div><div class="py-1">7</div><div class="py-1">8</div><div class="py-1">9</div><div class="py-1">10</div><div class="py-1">11</div><div class="py-1">12</div>
                       <div class="py-1">13</div><div class="py-1">14</div><div class="py-1">15</div><div class="bg-indigo-600 text-white rounded-l-full py-1">16</div><div class="bg-indigo-100 py-1">17</div><div class="bg-indigo-100 py-1">18</div><div class="bg-indigo-100 py-1">19</div>
                       <div class="bg-indigo-100 py-1">20</div><div class="bg-indigo-100 py-1">21</div><div class="bg-indigo-100 py-1">22</div><div class="bg-indigo-600 text-white rounded-r-full py-1">23</div><div class="py-1">24</div><div class="py-1">25</div><div class="py-1">26</div>
                       <div class="py-1">27</div><div class="py-1">28</div><div class="py-1">29</div><div class="py-1">30</div><div class="py-1">31</div><div class="text-gray-300 py-1">1</div><div class="text-gray-300 py-1">2</div>
                    </div>
                 </div>
                 <!-- Calendar 2 -->
                 <div>
                    <div class="text-center font-semibold text-gray-900 mb-4">November 2023</div>
                    <div class="grid grid-cols-7 gap-1 text-center text-xs">
                       <div class="text-gray-400 py-1">Su</div><div class="text-gray-400 py-1">Mo</div><div class="text-gray-400 py-1">Tu</div><div class="text-gray-400 py-1">We</div><div class="text-gray-400 py-1">Th</div><div class="text-gray-400 py-1">Fr</div><div class="text-gray-400 py-1">Sa</div>
                       <div class="text-gray-300 py-1">29</div><div class="text-gray-300 py-1">30</div><div class="text-gray-300 py-1">31</div><div class="py-1">1</div><div class="py-1">2</div><div class="py-1">3</div><div class="py-1">4</div>
                       <div class="py-1">5</div><div class="py-1">6</div><div class="py-1">7</div><div class="py-1">8</div><div class="py-1">9</div><div class="py-1">10</div><div class="py-1">11</div>
                       <div class="py-1">12</div><div class="py-1">13</div><div class="py-1">14</div><div class="py-1">15</div><div class="py-1">16</div><div class="py-1">17</div><div class="py-1">18</div>
                       <div class="py-1">19</div><div class="py-1">20</div><div class="py-1">21</div><div class="py-1">22</div><div class="py-1">23</div><div class="py-1">24</div><div class="py-1">25</div>
                       <div class="py-1">26</div><div class="py-1">27</div><div class="py-1">28</div><div class="py-1">29</div><div class="py-1">30</div><div class="text-gray-300 py-1">1</div><div class="text-gray-300 py-1">2</div>
                    </div>
                 </div>
              </div>
           </div>
           <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
              <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Apply</button>
              <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-025",
        "title": "Team Member Modal",
        "description": "Modal with team member details.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="relative text-center p-6">
              <div class="absolute top-0 left-0 w-full h-24 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-t-lg"></div>
              <div class="relative flex justify-center mt-12 mb-4">
                 <img class="h-24 w-24 rounded-full ring-4 ring-white object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              </div>
              <h3 class="text-xl font-bold text-gray-900">Lindsay Walton</h3>
              <p class="text-sm text-indigo-600 font-medium">Front-end Developer</p>
              <p class="mt-4 text-gray-500 text-sm">Lindsay loves crafting beautiful user interfaces and has a passion for accessibility and performance.</p>

              <div class="flex justify-center gap-4 mt-6">
                 <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg></a>
                 <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg></a>
                 <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
              </div>
           </div>
           <div class="px-6 py-4 bg-gray-50 border-t border-gray-200">
               <button class="w-full bg-white border border-gray-300 text-gray-700 font-semibold py-2 px-4 rounded-md hover:bg-gray-50 shadow-sm">Send Message</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-026",
        "title": "File Upload Modal",
        "description": "Modal for uploading files.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6">
              <h3 class="text-base font-semibold leading-6 text-gray-900 mb-4" id="modal-title">Upload Documents</h3>
              <div class="flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                <div class="text-center">
                  <svg class="mx-auto h-12 w-12 text-gray-300" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M1.5 6a2.25 2.25 0 012.25-2.25h16.5A2.25 2.25 0 0122.5 6v12a2.25 2.25 0 01-2.25 2.25H3.75A2.25 2.25 0 011.5 18V6zM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0021 18v-1.94l-2.69-2.689a1.5 1.5 0 00-2.12 0l-.88.879.97.97a.75.75 0 11-1.06 1.06l-5.16-5.159a1.5 1.5 0 00-2.12 0L3 16.061zm10.125-7.81a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0z" clip-rule="evenodd" />
                  </svg>
                  <div class="mt-4 flex text-sm leading-6 text-gray-600 justify-center">
                    <label for="file-upload" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                      <span>Upload a file</span>
                      <input id="file-upload" name="file-upload" type="file" class="sr-only">
                    </label>
                    <p class="pl-1">or drag and drop</p>
                  </div>
                  <p class="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
                </div>
              </div>
              <ul class="mt-4 space-y-2">
                 <li class="flex items-center justify-between p-2 rounded bg-gray-50 text-sm">
                    <div class="flex items-center">
                       <svg class="h-5 w-5 text-gray-400 mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"/></svg>
                       <span class="text-gray-700">report_q3.pdf</span>
                       <span class="text-gray-400 ml-2">(2.4MB)</span>
                    </div>
                    <button class="text-red-500 hover:text-red-700">&times;</button>
                 </li>
              </ul>
           </div>
           <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Upload 1 file</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-027",
        "title": "Maintenance Modal",
        "description": "Modal for system maintenance message.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-90 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-8 text-center">
              <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-orange-100 mb-6">
                 <svg class="h-8 w-8 text-orange-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                 </svg>
              </div>
              <h3 class="text-xl font-bold text-gray-900 mb-2">System Maintenance</h3>
              <p class="text-gray-500 mb-6">We're currently performing scheduled maintenance to improve our services. Please check back in a few hours.</p>
              <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700 mb-4">
                <div class="bg-orange-600 h-2.5 rounded-full" style="width: 45%"></div>
              </div>
              <p class="text-sm text-gray-400">Estimated completion time: 2:00 PM UTC</p>
              <div class="mt-8">
                 <button class="text-indigo-600 hover:text-indigo-500 font-medium">Check Status Page &rarr;</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-028",
        "title": "Achievement Unlocked",
        "description": "Modal for gamification achievement.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm border-4 border-yellow-400">
           <div class="text-center p-8">
              <div class="animate-bounce mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-yellow-100 mb-6 border-4 border-yellow-200">
                 <span class="text-4xl">🏆</span>
              </div>
              <h3 class="text-2xl font-black text-gray-900 mb-2 uppercase tracking-wide">Level Up!</h3>
              <p class="text-gray-600 font-medium mb-6">You've reached Level 5 and unlocked the "Power User" badge.</p>
              <div class="bg-gray-50 rounded-lg p-4 mb-6">
                 <p class="text-sm text-gray-500 mb-1">Rewards</p>
                 <p class="font-bold text-indigo-600">+500 Points</p>
                 <p class="font-bold text-indigo-600">New Avatar Frame</p>
              </div>
              <button class="w-full bg-yellow-400 text-yellow-900 font-extrabold py-3 px-4 rounded-lg shadow-lg hover:bg-yellow-300 transform hover:-translate-y-1 transition-all">Claim Rewards</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-029",
        "title": "Poll Modal",
        "description": "Modal with poll options.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="p-6">
              <h3 class="text-lg font-bold text-gray-900 mb-4">Quick Poll</h3>
              <p class="text-gray-600 mb-6">Which feature should we build next?</p>

              <div class="space-y-3">
                 <label class="flex items-center p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-indigo-50 hover:border-indigo-200 transition-colors">
                    <input type="radio" name="poll" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                    <div class="ml-3 flex-1">
                       <span class="block text-sm font-medium text-gray-900">Dark Mode</span>
                    </div>
                    <span class="text-xs text-gray-500">45%</span>
                 </label>
                 <label class="flex items-center p-3 border border-indigo-200 rounded-lg cursor-pointer bg-indigo-50">
                    <input type="radio" name="poll" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" checked>
                    <div class="ml-3 flex-1">
                       <span class="block text-sm font-medium text-gray-900">Mobile App</span>
                    </div>
                    <span class="text-xs text-gray-500">30%</span>
                 </label>
                 <label class="flex items-center p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-indigo-50 hover:border-indigo-200 transition-colors">
                    <input type="radio" name="poll" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                    <div class="ml-3 flex-1">
                       <span class="block text-sm font-medium text-gray-900">API Access</span>
                    </div>
                    <span class="text-xs text-gray-500">25%</span>
                 </label>
              </div>

              <div class="mt-6 flex justify-between items-center">
                 <p class="text-xs text-gray-400">Total votes: 1,234</p>
                 <button class="bg-indigo-600 text-white text-sm font-semibold py-2 px-4 rounded hover:bg-indigo-500">Vote</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-030",
        "title": "Code Snippet Modal",
        "description": "Modal displaying code.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-gray-900 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl">
           <div class="flex items-center justify-between px-4 py-3 bg-gray-800 border-b border-gray-700">
              <div class="flex gap-2">
                 <div class="w-3 h-3 rounded-full bg-red-500"></div>
                 <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                 <div class="w-3 h-3 rounded-full bg-green-500"></div>
              </div>
              <span class="text-gray-400 text-xs font-mono">example.js</span>
              <button class="text-gray-400 hover:text-white"><svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" /></svg></button>
           </div>
           <div class="p-6 overflow-x-auto">
              <pre class="text-sm font-mono text-gray-300 leading-relaxed"><code><span class="text-purple-400">const</span> <span class="text-blue-400">calculateTotal</span> <span class="text-gray-400">=</span> (<span class="text-orange-400">items</span>) <span class="text-purple-400">=></span> {
    <span class="text-purple-400">return</span> items.<span class="text-blue-400">reduce</span>((<span class="text-orange-400">total</span>, <span class="text-orange-400">item</span>) <span class="text-purple-400">=></span> {
      <span class="text-purple-400">return</span> total <span class="text-gray-400">+</span> (item.<span class="text-blue-400">price</span> <span class="text-gray-400">*</span> item.<span class="text-blue-400">quantity</span>);
    }, <span class="text-green-400">0</span>);
  };

  <span class="text-gray-500">// Usage example</span>
  <span class="text-purple-400">const</span> <span class="text-orange-400">cart</span> <span class="text-gray-400">=</span> [
    { <span class="text-blue-400">name</span>: <span class="text-green-400">'Apple'</span>, <span class="text-blue-400">price</span>: <span class="text-green-400">1.2</span>, <span class="text-blue-400">quantity</span>: <span class="text-green-400">2</span> },
    { <span class="text-blue-400">name</span>: <span class="text-green-400">'Orange'</span>, <span class="text-blue-400">price</span>: <span class="text-green-400">0.8</span>, <span class="text-blue-400">quantity</span>: <span class="text-green-400">5</span> }
  ];

  <span class="text-blue-400">console</span>.<span class="text-blue-400">log</span>(<span class="text-blue-400">calculateTotal</span>(cart)); <span class="text-gray-500">// Output: 6.4</span></code></pre>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_MODALS_4 = [
    {
        "id": "modal-031",
        "title": "Color Picker Modal",
        "description": "Modal for color selection.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm">
           <div class="p-4">
              <h3 class="text-base font-semibold text-gray-900 mb-4">Choose Color</h3>

              <div class="grid grid-cols-5 gap-2 mb-4">
                 <button class="w-8 h-8 rounded-full bg-red-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-red-500"></button>
                 <button class="w-8 h-8 rounded-full bg-orange-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-orange-500"></button>
                 <button class="w-8 h-8 rounded-full bg-amber-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-amber-500"></button>
                 <button class="w-8 h-8 rounded-full bg-yellow-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-yellow-500"></button>
                 <button class="w-8 h-8 rounded-full bg-lime-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-lime-500"></button>

                 <button class="w-8 h-8 rounded-full bg-green-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-green-500"></button>
                 <button class="w-8 h-8 rounded-full bg-emerald-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-emerald-500"></button>
                 <button class="w-8 h-8 rounded-full bg-teal-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-teal-500"></button>
                 <button class="w-8 h-8 rounded-full bg-cyan-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-cyan-500"></button>
                 <button class="w-8 h-8 rounded-full bg-sky-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-sky-500"></button>

                 <button class="w-8 h-8 rounded-full bg-blue-500 ring-2 ring-white ring-offset-2 ring-offset-blue-500"></button>
                 <button class="w-8 h-8 rounded-full bg-indigo-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-indigo-500"></button>
                 <button class="w-8 h-8 rounded-full bg-violet-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-violet-500"></button>
                 <button class="w-8 h-8 rounded-full bg-purple-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-purple-500"></button>
                 <button class="w-8 h-8 rounded-full bg-fuchsia-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-fuchsia-500"></button>

                 <button class="w-8 h-8 rounded-full bg-pink-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-pink-500"></button>
                 <button class="w-8 h-8 rounded-full bg-rose-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-rose-500"></button>
                 <button class="w-8 h-8 rounded-full bg-slate-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-slate-500"></button>
                 <button class="w-8 h-8 rounded-full bg-gray-500 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-gray-500"></button>
                 <button class="w-8 h-8 rounded-full bg-black ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300 focus:outline-none focus:ring-offset-2 focus:ring-black"></button>
              </div>

              <div class="mb-4">
                 <label for="hex" class="block text-xs font-medium text-gray-700">Hex Code</label>
                 <div class="mt-1 flex rounded-md shadow-sm">
                    <span class="inline-flex items-center rounded-l-md border border-r-0 border-gray-300 bg-gray-50 px-3 text-gray-500 sm:text-sm">#</span>
                    <input type="text" name="hex" id="hex" class="block w-full min-w-0 flex-1 rounded-none rounded-r-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 uppercase" value="3B82F6">
                 </div>
              </div>

              <div class="flex justify-end gap-2">
                 <button type="button" class="rounded bg-white px-2 py-1 text-xs font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Cancel</button>
                 <button type="button" class="rounded bg-indigo-600 px-2 py-1 text-xs font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Select</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-032",
        "title": "Keyboard Shortcuts",
        "description": "Modal showing keyboard shortcuts.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6">
              <h3 class="text-base font-semibold text-gray-900 mb-6">Keyboard Shortcuts</h3>

              <div class="space-y-4">
                 <div class="flex justify-between items-center group">
                    <span class="text-sm text-gray-600 group-hover:text-gray-900">Search</span>
                    <div class="flex gap-1">
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">Cmd</kbd>
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">K</kbd>
                    </div>
                 </div>
                 <div class="flex justify-between items-center group">
                    <span class="text-sm text-gray-600 group-hover:text-gray-900">New Project</span>
                    <div class="flex gap-1">
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">Cmd</kbd>
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">N</kbd>
                    </div>
                 </div>
                 <div class="flex justify-between items-center group">
                    <span class="text-sm text-gray-600 group-hover:text-gray-900">Go to Dashboard</span>
                    <div class="flex gap-1">
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">G</kbd>
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">D</kbd>
                    </div>
                 </div>
                 <div class="flex justify-between items-center group">
                    <span class="text-sm text-gray-600 group-hover:text-gray-900">Help</span>
                    <div class="flex gap-1">
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">?</kbd>
                    </div>
                 </div>
                 <div class="flex justify-between items-center group">
                    <span class="text-sm text-gray-600 group-hover:text-gray-900">Close Modal</span>
                    <div class="flex gap-1">
                       <kbd class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg">Esc</kbd>
                    </div>
                 </div>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-033",
        "title": "Review Modal",
        "description": "Modal for writing a review.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6">
              <h3 class="text-lg font-semibold text-gray-900 text-center mb-2">Write a Review</h3>
              <div class="flex justify-center mb-6">
                 <img src="https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg" alt="Product" class="w-16 h-16 object-cover rounded-md">
                 <div class="ml-4 text-left">
                    <p class="text-sm font-medium text-gray-900">Basic Tee</p>
                    <p class="text-sm text-gray-500">Black, Large</p>
                 </div>
              </div>

              <div class="flex justify-center gap-1 mb-6">
                 <button class="text-yellow-400 hover:scale-110 transition-transform"><svg class="h-8 w-8" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg></button>
                 <button class="text-yellow-400 hover:scale-110 transition-transform"><svg class="h-8 w-8" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg></button>
                 <button class="text-yellow-400 hover:scale-110 transition-transform"><svg class="h-8 w-8" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg></button>
                 <button class="text-yellow-400 hover:scale-110 transition-transform"><svg class="h-8 w-8" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg></button>
                 <button class="text-gray-300 hover:text-yellow-400 hover:scale-110 transition-transform"><svg class="h-8 w-8" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg></button>
              </div>

              <div class="mb-4">
                 <label for="review" class="block text-sm font-medium text-gray-700">Review</label>
                 <div class="mt-1">
                    <textarea id="review" name="review" rows="4" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="What did you like or dislike?"></textarea>
                 </div>
              </div>

              <div class="flex justify-end gap-3">
                 <button type="button" class="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Cancel</button>
                 <button type="button" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Submit Review</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-034",
        "title": "Calculator Modal",
        "description": "Modal with a functional layout for calculations.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-gray-900 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xs">
           <div class="p-4">
              <div class="bg-gray-800 rounded-lg p-4 mb-4 text-right">
                 <span class="text-white text-3xl font-mono">0</span>
              </div>
              <div class="grid grid-cols-4 gap-2">
                 <button class="bg-gray-700 text-white p-3 rounded hover:bg-gray-600">AC</button>
                 <button class="bg-gray-700 text-white p-3 rounded hover:bg-gray-600">+/-</button>
                 <button class="bg-gray-700 text-white p-3 rounded hover:bg-gray-600">%</button>
                 <button class="bg-orange-500 text-white p-3 rounded hover:bg-orange-400">÷</button>

                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">7</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">8</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">9</button>
                 <button class="bg-orange-500 text-white p-3 rounded hover:bg-orange-400">×</button>

                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">4</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">5</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">6</button>
                 <button class="bg-orange-500 text-white p-3 rounded hover:bg-orange-400">-</button>

                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">1</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">2</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">3</button>
                 <button class="bg-orange-500 text-white p-3 rounded hover:bg-orange-400">+</button>

                 <button class="col-span-2 bg-gray-800 text-white p-3 rounded hover:bg-gray-700 text-left pl-7">0</button>
                 <button class="bg-gray-800 text-white p-3 rounded hover:bg-gray-700">.</button>
                 <button class="bg-orange-500 text-white p-3 rounded hover:bg-orange-400">=</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-035",
        "title": "Session Timeout Modal",
        "description": "Modal warning about session expiration.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6 text-center">
              <svg class="h-16 w-16 mx-auto text-yellow-400 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <h3 class="text-xl font-semibold text-gray-900 mb-2">Are you still there?</h3>
              <p class="text-gray-500 mb-6">Your session will expire in <span class="font-bold text-gray-900" id="countdown">02:00</span> minutes. We want to protect your account security.</p>

              <div class="flex flex-col gap-3 sm:flex-row sm:justify-center">
                 <button type="button" class="w-full sm:w-auto inline-flex justify-center rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">
                    Stay Logged In
                 </button>
                 <button type="button" class="w-full sm:w-auto inline-flex justify-center rounded-md bg-white px-4 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                    Log Out
                 </button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-036",
        "title": "Map Modal",
        "description": "Modal containing a map.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
           <div class="relative h-96 bg-gray-200">
              <!-- Placeholder for Map -->
              <div class="absolute inset-0 flex items-center justify-center text-gray-400">
                 <div class="text-center">
                    <svg class="h-12 w-12 mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                       <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                    </svg>
                    <span>Google Maps Integration</span>
                 </div>
              </div>

              <!-- Location Card Overlay -->
              <div class="absolute bottom-4 left-4 right-4 bg-white p-4 rounded-lg shadow-lg sm:left-4 sm:right-auto sm:w-80">
                 <h4 class="font-bold text-gray-900">Headquarters</h4>
                 <p class="text-sm text-gray-500 mb-3">123 Innovation Drive, Tech City, TC 90210</p>
                 <div class="flex gap-2">
                    <button class="flex-1 bg-indigo-600 text-white text-xs font-semibold py-2 px-3 rounded hover:bg-indigo-500">Get Directions</button>
                    <button class="flex-1 bg-gray-100 text-gray-900 text-xs font-semibold py-2 px-3 rounded hover:bg-gray-200">Copy Address</button>
                 </div>
              </div>

              <button class="absolute top-4 right-4 bg-white p-2 rounded-full shadow-md text-gray-500 hover:text-gray-900">
                 <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                 </svg>
              </button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-037",
        "title": "Permissions Modal",
        "description": "Modal for managing user permissions.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-1">Manage Permissions</h3>
              <p class="text-sm text-gray-500 mb-6">Control what team members can do in this project.</p>

              <div class="space-y-4">
                 <div class="flex items-start justify-between">
                    <div>
                       <label for="perm-edit" class="font-medium text-gray-900">Edit Content</label>
                       <p class="text-xs text-gray-500">Allows editing text and images.</p>
                    </div>
                    <div class="flex h-6 items-center">
                       <input id="perm-edit" name="perm-edit" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" checked>
                    </div>
                 </div>
                 <div class="flex items-start justify-between">
                    <div>
                       <label for="perm-publish" class="font-medium text-gray-900">Publish Changes</label>
                       <p class="text-xs text-gray-500">Allows publishing changes to live site.</p>
                    </div>
                    <div class="flex h-6 items-center">
                       <input id="perm-publish" name="perm-publish" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                    </div>
                 </div>
                 <div class="flex items-start justify-between">
                    <div>
                       <label for="perm-invite" class="font-medium text-gray-900">Invite Members</label>
                       <p class="text-xs text-gray-500">Allows inviting new users to the project.</p>
                    </div>
                    <div class="flex h-6 items-center">
                       <input id="perm-invite" name="perm-invite" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                    </div>
                 </div>
                 <div class="flex items-start justify-between">
                    <div>
                       <label for="perm-delete" class="font-medium text-gray-900">Delete Project</label>
                       <p class="text-xs text-gray-500">Allows permanent deletion of the project.</p>
                    </div>
                    <div class="flex h-6 items-center">
                       <input id="perm-delete" name="perm-delete" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" disabled>
                    </div>
                 </div>
              </div>

              <div class="mt-8 flex justify-end gap-3">
                 <button type="button" class="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Cancel</button>
                 <button type="button" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">Save Changes</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-038",
        "title": "History/Activity Modal",
        "description": "Modal showing history timeline.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-6">Activity History</h3>

              <div class="flow-root">
                 <ul role="list" class="-mb-8">
                    <li>
                       <div class="relative pb-8">
                          <span class="absolute left-4 top-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true"></span>
                          <div class="relative flex space-x-3">
                             <div>
                                <span class="h-8 w-8 rounded-full bg-blue-500 flex items-center justify-center ring-8 ring-white">
                                   <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                                </span>
                             </div>
                             <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                <div>
                                   <p class="text-sm text-gray-500">Created new project <a href="#" class="font-medium text-gray-900">Website Redesign</a></p>
                                </div>
                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                   <time datetime="2023-09-20">2h ago</time>
                                </div>
                             </div>
                          </div>
                       </div>
                    </li>
                    <li>
                       <div class="relative pb-8">
                          <span class="absolute left-4 top-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true"></span>
                          <div class="relative flex space-x-3">
                             <div>
                                <span class="h-8 w-8 rounded-full bg-green-500 flex items-center justify-center ring-8 ring-white">
                                   <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                                </span>
                             </div>
                             <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                <div>
                                   <p class="text-sm text-gray-500">Completed task <a href="#" class="font-medium text-gray-900">Wireframes</a></p>
                                </div>
                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                   <time datetime="2023-09-20">4h ago</time>
                                </div>
                             </div>
                          </div>
                       </div>
                    </li>
                    <li>
                       <div class="relative pb-8">
                          <div class="relative flex space-x-3">
                             <div>
                                <span class="h-8 w-8 rounded-full bg-gray-400 flex items-center justify-center ring-8 ring-white">
                                   <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" /></svg>
                                </span>
                             </div>
                             <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                <div>
                                   <p class="text-sm text-gray-500">Commented on <a href="#" class="font-medium text-gray-900">Design Mockup</a></p>
                                </div>
                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                   <time datetime="2023-09-19">1d ago</time>
                                </div>
                             </div>
                          </div>
                       </div>
                    </li>
                 </ul>
              </div>
              <button class="w-full mt-6 bg-gray-50 text-gray-600 font-medium py-2 rounded-md hover:bg-gray-100">View All Activity</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-039",
        "title": "Audio Player Modal",
        "description": "Modal with audio player interface.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-90 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-gray-800 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="p-6">
              <div class="flex items-center gap-4 mb-6">
                 <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-1.2.1&auto=format&fit=crop&w=150&q=80" alt="Album Art" class="w-20 h-20 rounded bg-gray-700 object-cover">
                 <div>
                    <h3 class="text-white font-bold text-lg">Midnight Synthwave</h3>
                    <p class="text-gray-400">Electronic Dreams</p>
                 </div>
              </div>

              <div class="mb-4">
                 <div class="relative w-full h-1 bg-gray-600 rounded cursor-pointer group">
                    <div class="absolute h-full bg-indigo-500 rounded w-1/3 group-hover:bg-indigo-400"></div>
                    <div class="absolute h-3 w-3 bg-white rounded-full -top-1 left-1/3 shadow hidden group-hover:block"></div>
                 </div>
                 <div class="flex justify-between text-xs text-gray-400 mt-2">
                    <span>1:23</span>
                    <span>3:45</span>
                 </div>
              </div>

              <div class="flex items-center justify-center gap-6">
                 <button class="text-gray-400 hover:text-white"><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 20 20"><path d="M8.445 14.832A1 1 0 0010 14v-2.798l5.445 3.63A1 1 0 0017 14V6a1 1 0 00-1.555-.832L10 8.798V6a1 1 0 00-1.555-.832l-6 4a1 1 0 000 1.664l6 4z"/></svg></button>
                 <button class="bg-white text-gray-900 rounded-full p-3 hover:scale-105 transition-transform"><svg class="h-8 w-8" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"/></svg></button>
                 <button class="text-gray-400 hover:text-white"><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 20 20"><path d="M4.555 5.168A1 1 0 003 6v8a1 1 0 001.555.832L10 11.202V14a1 1 0 001.555.832l6-4a1 1 0 000-1.664l-6-4A1 1 0 0010 6v2.798l-5.445-3.63z"/></svg></button>
              </div>

              <div class="flex items-center gap-2 mt-6">
                 <svg class="h-4 w-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M9.383 3.076A1 1 0 0110 4v12a1 1 0 01-1.707.707L4.586 13H2a1 1 0 01-1-1V8a1 1 0 011-1h2.586l3.707-3.707a1 1 0 011.09-.217zM14.657 2.929a1 1 0 011.414 0A9.972 9.972 0 0119 10a9.972 9.972 0 01-2.929 7.071 1 1 0 01-1.414-1.414A7.971 7.971 0 0017 10c0-2.21-.894-4.208-2.343-5.657a1 1 0 010-1.414zm-2.829 2.828a1 1 0 011.415 0A5.983 5.983 0 0115 10a5.984 5.984 0 01-1.757 4.243 1 1 0 01-1.415-1.415A3.984 3.984 0 0013 10a3.983 3.983 0 00-1.172-2.828 1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                 <div class="relative w-24 h-1 bg-gray-600 rounded cursor-pointer">
                    <div class="absolute h-full bg-gray-400 rounded w-2/3"></div>
                 </div>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-040",
        "title": "Contact Support Modal",
        "description": "Modal with contact support form.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="p-6">
              <h3 class="text-base font-semibold leading-6 text-gray-900 mb-1">Contact Support</h3>
              <p class="text-sm text-gray-500 mb-6">We usually get back to you within 24 hours.</p>

              <form class="space-y-4">
                 <div>
                    <label for="topic" class="block text-sm font-medium text-gray-700">Topic</label>
                    <select id="topic" name="topic" class="mt-1 block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm sm:leading-6">
                       <option>General Inquiry</option>
                       <option>Billing Issue</option>
                       <option>Technical Support</option>
                       <option>Feature Request</option>
                    </select>
                 </div>

                 <div>
                    <label for="message" class="block text-sm font-medium text-gray-700">Message</label>
                    <div class="mt-1">
                       <textarea id="message" name="message" rows="4" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                    </div>
                 </div>

                 <div>
                    <label for="attachment" class="block text-sm font-medium text-gray-700">Attachment (optional)</label>
                    <div class="mt-1 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-4">
                       <div class="text-center">
                          <div class="mt-2 flex text-sm leading-6 text-gray-600 justify-center">
                             <label for="file-upload-support" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                                <span>Upload a file</span>
                                <input id="file-upload-support" name="file-upload" type="file" class="sr-only">
                             </label>
                          </div>
                       </div>
                    </div>
                 </div>
              </form>
           </div>
           <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:ml-3 sm:w-auto">Send Message</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_MODALS_5 = [
    {
        "id": "modal-041",
        "title": "Onboarding Modal",
        "description": "Modal with onboarding steps.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="p-6 text-center">
              <img src="https://cdni.iconscout.com/illustration/premium/thumb/welcome-back-illustration-download-in-svg-png-gif-file-formats--wave-hi-hello-business-activities-pack-illustrations-3970725.png" alt="Welcome" class="mx-auto h-40 w-auto mb-6">
              <h3 class="text-2xl font-bold text-gray-900 mb-2">Welcome to Acme Corp!</h3>
              <p class="text-gray-500 mb-8">We're excited to have you on board. Let's get you set up in just a few simple steps.</p>

              <div class="flex justify-center gap-2 mb-8">
                 <div class="w-2.5 h-2.5 rounded-full bg-indigo-600"></div>
                 <div class="w-2.5 h-2.5 rounded-full bg-gray-300"></div>
                 <div class="w-2.5 h-2.5 rounded-full bg-gray-300"></div>
              </div>

              <button class="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg shadow hover:bg-indigo-500 transition-colors">Let's Get Started &rarr;</button>
              <button class="w-full mt-3 text-gray-500 text-sm hover:text-gray-700">Skip For Now</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-042",
        "title": "Feedback Modal",
        "description": "Modal for detailed feedback.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
           <div class="bg-indigo-600 px-4 py-6 sm:px-6">
              <h3 class="text-base font-semibold leading-6 text-white" id="modal-title">We value your feedback</h3>
              <p class="mt-1 text-sm text-indigo-100">Help us improve your experience.</p>
           </div>
           <div class="p-6">
              <div class="mb-6">
                 <label class="block text-sm font-medium text-gray-700 mb-2">How would you rate your experience?</label>
                 <div class="flex justify-between items-center text-4xl grayscale hover:grayscale-0 transition-all cursor-pointer">
                    <span class="hover:scale-110 transition-transform" title="Terrible">😠</span>
                    <span class="hover:scale-110 transition-transform" title="Bad">🙁</span>
                    <span class="hover:scale-110 transition-transform" title="Okay">😐</span>
                    <span class="hover:scale-110 transition-transform" title="Good">🙂</span>
                    <span class="hover:scale-110 transition-transform" title="Excellent">🤩</span>
                 </div>
              </div>

              <div class="mb-6">
                 <label for="feedback-details" class="block text-sm font-medium text-gray-700 mb-2">What can we do better?</label>
                 <textarea id="feedback-details" rows="4" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
              </div>

              <div class="flex justify-end gap-3">
                 <button type="button" class="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Cancel</button>
                 <button type="button" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">Submit Feedback</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-043",
        "title": "Download App Modal",
        "description": "Modal promoting mobile app download.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
           <div class="flex flex-col md:flex-row">
              <div class="md:w-1/2 relative bg-gray-900">
                 <img src="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Mobile App" class="h-64 w-full md:h-full object-cover opacity-75">
                 <div class="absolute inset-0 flex items-center justify-center">
                    <h3 class="text-3xl font-bold text-white text-center px-4">Experience it on mobile</h3>
                 </div>
              </div>
              <div class="md:w-1/2 p-8 flex flex-col justify-center">
                 <h4 class="text-xl font-bold text-gray-900 mb-4">Get the App</h4>
                 <p class="text-gray-600 mb-6">Scan the QR code to download our app instantly.</p>
                 <div class="flex justify-center mb-6">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example" alt="QR Code" class="h-32 w-32 border border-gray-200 p-2 rounded">
                 </div>
                 <div class="flex flex-col gap-3">
                    <button class="flex items-center justify-center bg-black text-white py-2 px-4 rounded-lg hover:bg-gray-800 transition-colors">
                       <svg class="h-6 w-6 mr-2" viewBox="0 0 24 24" fill="currentColor"><path d="M17.653 17.512c-.543.805-1.121 1.583-1.898 1.583-.795 0-1.071-.482-2.031-.482-.942 0-1.246.471-2.036.471-.828 0-1.46-.826-2.008-1.637-2.316-3.375-1.956-8.385 1.574-8.385.966 0 1.633.649 2.162.649.522 0 1.343-.635 2.274-.635.952 0 2.527.702 3.125 1.597-2.673 1.397-2.228 5.64 1.838 7.339zm-3.38-12.083c.421-.522.709-1.25.709-1.972 0-.108-.011-.214-.033-.316-.763.032-1.666.521-2.203 1.159-.442.518-.838 1.325-.838 2.016 0 .098.017.202.046.302.827-.066 1.776-.583 2.319-1.189z"/></svg>
                       <div class="text-left">
                          <div class="text-[10px] leading-tight">Download on the</div>
                          <div class="text-sm font-bold leading-tight">App Store</div>
                       </div>
                    </button>
                    <button class="flex items-center justify-center bg-black text-white py-2 px-4 rounded-lg hover:bg-gray-800 transition-colors">
                       <svg class="h-6 w-6 mr-2" viewBox="0 0 24 24" fill="currentColor"><path d="M3.609 1.814L13.792 12 3.61 22.186c-.184.184-.424.234-.585.166-.16-.07-.327-.291-.327-.611V2.258c0-.32.167-.541.327-.61.161-.069.401-.019.585.166zm10.963 10.941L19.78 17.8l-1.666 1.666-6.666-6.666 3.124-3.124zm.82-1.509l5.06-5.061c.218.21.365.508.365.845v13.94c0 .337-.146.635-.365.845l-5.06-5.061M18.114 6.2l1.666 1.666-5.208 5.208-3.124-3.125 6.666-6.666z"/></svg>
                       <div class="text-left">
                          <div class="text-[10px] leading-tight">GET IT ON</div>
                          <div class="text-sm font-bold leading-tight">Google Play</div>
                       </div>
                    </button>
                 </div>
              </div>
           </div>
           <button class="absolute top-2 right-2 md:text-gray-500 text-white hover:text-gray-700 bg-white/20 md:bg-transparent rounded-full p-1"><svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg></button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-044",
        "title": "Success Celebration Modal",
        "description": "Modal with confetti for success.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm">
           <div class="p-6 text-center">
              <div class="mx-auto flex h-24 w-24 items-center justify-center rounded-full bg-green-100 mb-6">
                 <svg class="h-12 w-12 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                 </svg>
              </div>
              <h3 class="text-2xl font-bold text-gray-900 mb-2">Order Placed!</h3>
              <p class="text-gray-500 mb-6">Your order #12345 has been successfully placed and is being processed.</p>

              <div class="bg-gray-50 rounded p-4 mb-6 text-sm text-left">
                 <div class="flex justify-between mb-2">
                    <span class="text-gray-500">Amount Paid</span>
                    <span class="font-bold text-gray-900">$129.00</span>
                 </div>
                 <div class="flex justify-between">
                    <span class="text-gray-500">Estimated Delivery</span>
                    <span class="font-bold text-gray-900">Oct 25, 2023</span>
                 </div>
              </div>

              <button class="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg shadow hover:bg-indigo-500">Track Order</button>
              <button class="w-full mt-3 text-indigo-600 font-medium text-sm hover:text-indigo-500">Continue Shopping</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-045",
        "title": "Terms of Service Modal",
        "description": "Scrollable modal for terms and conditions.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
           <div class="p-6">
              <h3 class="text-xl font-bold text-gray-900 mb-4">Terms of Service</h3>
              <div class="h-64 overflow-y-auto bg-gray-50 p-4 rounded-md border border-gray-200 text-sm text-gray-600 mb-6">
                 <p class="mb-3"><strong>1. Acceptance of Terms</strong><br>By accessing and using this service, you accept and agree to be bound by the terms and provision of this agreement.</p>
                 <p class="mb-3"><strong>2. Privacy Policy</strong><br>We respect your privacy and authorize you to control the treatment of your personal information.</p>
                 <p class="mb-3"><strong>3. User Conduct</strong><br>You agree to use our website only for lawful purposes. You are prohibited from posting on or transmitting through our site any unlawful, harmful, threatening, abusive, harassing, defamatory, vulgar, obscene, sexually explicit, profane, hateful, racially, ethnically, or otherwise objectionable material of any kind.</p>
                 <p class="mb-3"><strong>4. Limitation of Liability</strong><br>In no event shall we be liable for any direct, indirect, incidental, special, consequential, or exemplary damages.</p>
                 <p class="mb-3"><strong>5. Termination</strong><br>We may terminate your access to the Site, without cause or notice, which may result in the forfeiture and destruction of all information associated with you.</p>
                 <p class="mb-3"><strong>6. Changes to Terms</strong><br>We reserve the right, at our sole discretion, to modify or replace these Terms at any time.</p>
                 <p><strong>7. Contact Information</strong><br>If you have any questions about these Terms, please contact us.</p>
              </div>

              <div class="flex items-center mb-6">
                 <input id="terms-agree" name="terms-agree" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                 <label for="terms-agree" class="ml-3 block text-sm leading-6 text-gray-900">I have read and agree to the Terms of Service</label>
              </div>

              <div class="flex justify-end gap-3">
                 <button type="button" class="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Decline</button>
                 <button type="button" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed">Accept & Continue</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-046",
        "title": "Split Bill Modal",
        "description": "Modal for splitting costs.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="p-6">
              <h3 class="text-base font-semibold text-gray-900 mb-6">Split the Bill</h3>

              <div class="flex justify-between items-center mb-6 bg-gray-50 p-4 rounded-lg">
                 <span class="text-gray-600 font-medium">Total Amount</span>
                 <span class="text-2xl font-bold text-gray-900">$124.50</span>
              </div>

              <div class="mb-6">
                 <label class="block text-sm font-medium text-gray-700 mb-2">Split with</label>
                 <div class="flex -space-x-2 overflow-hidden mb-4">
                    <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt="">
                    <button class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 ring-2 ring-white text-gray-500 hover:bg-gray-200">
                       <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                    </button>
                 </div>
              </div>

              <div class="mb-8">
                 <div class="flex justify-between text-sm mb-1">
                    <span class="text-gray-500">4 People</span>
                    <span class="font-bold text-gray-900">$31.12 / person</span>
                 </div>
                 <input type="range" min="1" max="10" value="4" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-indigo-600">
              </div>

              <button class="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg shadow hover:bg-indigo-500">Send Request</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-047",
        "title": "Weather Modal",
        "description": "Modal showing weather details.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-gradient-to-br from-blue-400 to-blue-600 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm text-white">
           <div class="p-6">
              <div class="flex justify-between items-start mb-8">
                 <div>
                    <h3 class="text-2xl font-bold">San Francisco</h3>
                    <p class="text-blue-100">Monday, 10:23 AM</p>
                 </div>
                 <svg class="h-6 w-6 text-white cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
              </div>

              <div class="flex items-center justify-between mb-8">
                 <div class="flex items-center">
                    <svg class="h-20 w-20 text-yellow-300 animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
                    <div class="ml-4">
                       <span class="text-6xl font-thin">72°</span>
                       <p class="text-blue-100">Sunny</p>
                    </div>
                 </div>
              </div>

              <div class="grid grid-cols-3 gap-4 border-t border-blue-400 pt-6">
                 <div class="text-center">
                    <p class="text-blue-200 text-xs uppercase mb-1">Wind</p>
                    <p class="font-bold">6 mph</p>
                 </div>
                 <div class="text-center border-l border-blue-400">
                    <p class="text-blue-200 text-xs uppercase mb-1">Humidity</p>
                    <p class="font-bold">42%</p>
                 </div>
                 <div class="text-center border-l border-blue-400">
                    <p class="text-blue-200 text-xs uppercase mb-1">Precip</p>
                    <p class="font-bold">0%</p>
                 </div>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-048",
        "title": "Product Quick View",
        "description": "Modal for quick product details.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
           <div class="grid grid-cols-1 md:grid-cols-2">
              <div class="h-64 md:h-full bg-gray-200 relative">
                 <img src="https://tailwindui.com/img/ecommerce-images/product-page-02-secondary-product-shot.jpg" alt="Product" class="absolute inset-0 w-full h-full object-cover">
              </div>
              <div class="p-8 relative">
                 <button class="absolute top-4 right-4 text-gray-400 hover:text-gray-500"><svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg></button>

                 <h2 class="text-2xl font-bold text-gray-900 mb-2">Basic Tee</h2>
                 <p class="text-2xl text-gray-900 font-medium mb-4">$35.00</p>

                 <div class="flex items-center mb-6">
                    <div class="flex text-yellow-400">
                       <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                       <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                       <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                       <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                       <svg class="h-5 w-5 text-gray-300" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                    </div>
                    <span class="ml-2 text-sm text-gray-500">117 reviews</span>
                 </div>

                 <p class="text-gray-500 text-sm mb-6">The Basic Tee 6-Pack is just that—a pack of 6 basic tees. It's the only way to get that perfect "I just woke up" look.</p>

                 <div class="mb-6">
                    <label class="block text-sm font-medium text-gray-700 mb-2">Color</label>
                    <div class="flex gap-2">
                       <button class="w-8 h-8 rounded-full bg-black ring-2 ring-offset-2 ring-gray-400"></button>
                       <button class="w-8 h-8 rounded-full bg-gray-400 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300"></button>
                       <button class="w-8 h-8 rounded-full bg-white border border-gray-300 ring-2 ring-transparent hover:ring-offset-1 hover:ring-gray-300"></button>
                    </div>
                 </div>

                 <button class="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg shadow hover:bg-indigo-500">Add to Bag</button>
                 <button class="w-full mt-3 text-indigo-600 text-sm font-medium hover:text-indigo-500 text-center">View Full Details</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-049",
        "title": "Share Modal",
        "description": "Modal options for sharing content.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-md">
           <div class="p-6">
              <h3 class="text-base font-semibold leading-6 text-gray-900 mb-4">Share Project</h3>

              <div class="grid grid-cols-4 gap-4 mb-6">
                 <button class="flex flex-col items-center gap-2 group">
                    <div class="w-12 h-12 rounded-full bg-blue-500 flex items-center justify-center text-white shadow-sm group-hover:scale-110 transition-transform">
                       <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                    </div>
                    <span class="text-xs text-gray-600">Twitter</span>
                 </button>
                 <button class="flex flex-col items-center gap-2 group">
                    <div class="w-12 h-12 rounded-full bg-blue-700 flex items-center justify-center text-white shadow-sm group-hover:scale-110 transition-transform">
                       <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    </div>
                    <span class="text-xs text-gray-600">LinkedIn</span>
                 </button>
                 <button class="flex flex-col items-center gap-2 group">
                    <div class="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center text-white shadow-sm group-hover:scale-110 transition-transform">
                       <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385h-3.047v-3.47h3.047v-2.641c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953h-1.514c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385c5.737-.9 10.125-5.864 10.125-11.854z"/></svg>
                    </div>
                    <span class="text-xs text-gray-600">Facebook</span>
                 </button>
                 <button class="flex flex-col items-center gap-2 group">
                    <div class="w-12 h-12 rounded-full bg-gray-600 flex items-center justify-center text-white shadow-sm group-hover:scale-110 transition-transform">
                       <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03z"/></svg>
                    </div>
                    <span class="text-xs text-gray-600">Discord</span>
                 </button>
              </div>

              <div class="relative">
                 <label for="share-link" class="block text-sm font-medium text-gray-700 mb-1">Copy Link</label>
                 <div class="flex rounded-md shadow-sm">
                    <input type="text" name="share-link" id="share-link" class="block w-full rounded-l-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" value="https://example.com/p/12345" readonly>
                    <button type="button" class="relative -ml-px inline-flex items-center gap-x-1.5 rounded-r-md px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                       <svg class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
                       Copy
                    </button>
                 </div>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "modal-050",
        "title": "Welcome Back Modal",
        "description": "Modal greeting returning user.",
        "dir": "templates/13-modals",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-80 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-gray-800 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg border border-gray-700">
           <div class="p-8 text-center">
              <div class="mx-auto w-20 h-20 bg-gradient-to-tr from-pink-500 to-violet-500 rounded-full flex items-center justify-center mb-6 shadow-lg shadow-pink-500/30">
                 <span class="text-3xl">👋</span>
              </div>
              <h3 class="text-3xl font-bold text-white mb-2">Welcome Back, Alex!</h3>
              <p class="text-gray-400 mb-8">We've missed you. Check out what's new since your last visit.</p>

              <div class="grid grid-cols-2 gap-4 mb-8 text-left">
                 <div class="bg-gray-700/50 p-4 rounded-lg">
                    <div class="flex items-center mb-2">
                       <span class="w-2 h-2 rounded-full bg-green-400 mr-2"></span>
                       <span class="text-white font-medium">New Dashboard</span>
                    </div>
                    <p class="text-xs text-gray-400">Completely redesigned analytics view.</p>
                 </div>
                 <div class="bg-gray-700/50 p-4 rounded-lg">
                    <div class="flex items-center mb-2">
                       <span class="w-2 h-2 rounded-full bg-blue-400 mr-2"></span>
                       <span class="text-white font-medium">Dark Mode</span>
                    </div>
                    <p class="text-xs text-gray-400">Now available for all pages.</p>
                 </div>
              </div>

              <button class="w-full bg-gradient-to-r from-pink-600 to-violet-600 text-white font-bold py-3 px-4 rounded-lg shadow-lg hover:from-pink-500 hover:to-violet-500 transform hover:-translate-y-0.5 transition-all">Explore Dashboard</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_MODALS = TEMPLATES_MODALS_1 + TEMPLATES_MODALS_2 + TEMPLATES_MODALS_3 + TEMPLATES_MODALS_4 + TEMPLATES_MODALS_5

# Part 2: Notifications 001-050
TEMPLATES_NOTIFICATIONS_1 = [
    {
        "id": "notification-001",
        "title": "Simple Success Notification",
        "description": "Basic success notification with icon.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
           </svg>
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
          <p class="text-sm font-medium text-gray-900">Successfully saved!</p>
          <p class="mt-1 text-sm text-gray-500">Your changes have been saved to the database.</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-002",
        "title": "Simple Error Notification",
        "description": "Basic error notification with icon.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
           </svg>
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
          <p class="text-sm font-medium text-gray-900">There was an error!</p>
          <p class="mt-1 text-sm text-gray-500">Your changes could not be saved. Please try again.</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-003",
        "title": "Simple Warning Notification",
        "description": "Basic warning notification with icon.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
           </svg>
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
          <p class="text-sm font-medium text-gray-900">Attention needed</p>
          <p class="mt-1 text-sm text-gray-500">Your subscription is ending soon. Renew now.</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-004",
        "title": "Simple Info Notification",
        "description": "Basic info notification with icon.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
           </svg>
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
          <p class="text-sm font-medium text-gray-900">New feature available</p>
          <p class="mt-1 text-sm text-gray-500">Check out the new dashboard layout in settings.</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-005",
        "title": "Notification with Actions",
        "description": "Notification with action buttons.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0 pt-0.5">
          <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.2&w=160&h=160&q=80" alt="">
        </div>
        <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Emilia Gates</p>
          <p class="mt-1 text-sm text-gray-500">Sent you an invite to connect.</p>
          <div class="mt-4 flex">
            <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Accept</button>
            <button type="button" class="ml-3 inline-flex items-center rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Decline</button>
          </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-006",
        "title": "Condensed Notification",
        "description": "Compact single-line notification.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-center">
        <div class="flex w-0 flex-1 justify-between">
          <p class="w-0 flex-1 truncate text-sm font-medium text-gray-900">Discussion archived</p>
          <button type="button" class="ml-3 flex-shrink-0 rounded-md bg-white text-sm font-medium text-indigo-600 hover:text-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Undo</button>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-007",
        "title": "Notification with Avatar",
        "description": "Notification showing user avatar.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="flex p-4">
       <div class="flex-shrink-0">
          <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
       </div>
       <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Reply from Sarah</p>
          <p class="mt-1 text-sm text-gray-500">Hey! I just saw your message. Let's catch up later today?</p>
       </div>
       <div class="ml-4 flex flex-shrink-0 self-start">
        <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
           <span class="sr-only">Close</span>
           <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
        </button>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-008",
        "title": "Split Notification buttons",
        "description": "Notification with split button layout.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto flex w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="w-0 flex-1 p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0 pt-0.5">
          <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.2&w=160&h=160&q=80" alt="">
        </div>
        <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Emilia Gates</p>
          <p class="mt-1 text-sm text-gray-500">Sent you an invite to connect.</p>
        </div>
      </div>
    </div>
    <div class="flex border-l border-gray-200">
      <button type="button" class="flex w-full items-center justify-center rounded-none rounded-r-lg border border-transparent p-4 text-sm font-medium text-indigo-600 hover:text-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500">Reply</button>
    </div>
  </div>"""
    },
    {
        "id": "notification-009",
        "title": "Loading Notification",
        "description": "Notification with spinner.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-center">
        <div class="flex-shrink-0">
           <svg class="animate-spin h-5 w-5 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
           </svg>
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
          <p class="text-sm font-medium text-gray-900">Processing file...</p>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-010",
        "title": "Dark Mode Notification",
        "description": "Notification with dark theme.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gray-800 shadow-lg ring-1 ring-white ring-opacity-10 text-white">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
           </svg>
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
          <p class="text-sm font-medium">Successfully saved!</p>
          <p class="mt-1 text-sm text-gray-400">Your changes have been saved to the database.</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-gray-800 text-gray-400 hover:text-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_NOTIFICATIONS_2 = [
    {
        "id": "notification-011",
        "title": "Stacked Notifications",
        "description": "Multiple notifications stacked vertically.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="flex flex-col gap-2 pointer-events-auto w-full max-w-sm">
      <div class="w-full overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
        <div class="p-4">
          <div class="flex items-start">
            <div class="flex-shrink-0">
               <svg class="h-6 w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <div class="ml-3 w-0 flex-1 pt-0.5">
              <p class="text-sm font-medium text-gray-900">Upload Complete</p>
              <p class="mt-1 text-sm text-gray-500">image-001.jpg has been uploaded.</p>
            </div>
            <div class="ml-4 flex flex-shrink-0">
              <button class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"><span class="sr-only">Close</span><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
            </div>
          </div>
        </div>
      </div>
      <div class="w-full overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
        <div class="p-4">
          <div class="flex items-start">
            <div class="flex-shrink-0">
               <svg class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <div class="ml-3 w-0 flex-1 pt-0.5">
              <p class="text-sm font-medium text-gray-900">New Message</p>
              <p class="mt-1 text-sm text-gray-500">You have a new message from Alex.</p>
            </div>
             <div class="ml-4 flex flex-shrink-0">
              <button class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"><span class="sr-only">Close</span><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
            </div>
          </div>
        </div>
      </div>
  </div>"""
    },
    {
        "id": "notification-012",
        "title": "Friend Request",
        "description": "Notification for friend request.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
       <div class="flex items-start">
          <div class="flex-shrink-0">
             <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=160&h=160&q=80" alt="Avatar">
          </div>
          <div class="ml-3 w-0 flex-1">
             <p class="text-sm font-medium text-gray-900">Ashley Jones</p>
             <p class="mt-1 text-sm text-gray-500">wants to add you as a friend.</p>
             <div class="mt-3 flex gap-3">
                <button type="button" class="inline-flex justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">Confirm</button>
                <button type="button" class="inline-flex justify-center rounded-md bg-white px-3 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Delete</button>
             </div>
          </div>
           <div class="ml-4 flex flex-shrink-0 self-start">
              <button class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"><span class="sr-only">Close</span><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
            </div>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-013",
        "title": "Call Incoming",
        "description": "Notification for incoming call.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gray-900 shadow-lg ring-1 ring-white ring-opacity-10 text-white">
    <div class="p-4">
       <div class="flex items-center">
          <div class="flex-shrink-0 relative">
             <div class="absolute inline-flex items-center justify-center w-full h-full rounded-full bg-green-400 opacity-75 animate-ping"></div>
             <img class="relative h-12 w-12 rounded-full border-2 border-gray-800" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=160&h=160&q=80" alt="Avatar">
          </div>
          <div class="ml-4 flex-1">
             <p class="text-base font-semibold">Incoming Call</p>
             <p class="text-sm text-gray-400">David Smith</p>
          </div>
          <div class="flex gap-2">
             <button class="bg-red-500 p-2 rounded-full hover:bg-red-600 transition-colors text-white"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.28 5.22a.75.75 0 00-1.06 1.06l1.89 1.89-1.89 1.89a.75.75 0 101.06 1.06l1.89-1.89 1.89 1.89a.75.75 0 101.06-1.06l-1.89-1.89 1.89-1.89a.75.75 0 00-1.06-1.06l-1.89 1.89-1.89-1.89z"/></svg></button>
             <button class="bg-green-500 p-2 rounded-full hover:bg-green-600 transition-colors text-white"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/></svg></button>
          </div>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-014",
        "title": "Minimal Toast",
        "description": "Very simple toast message.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-auto max-w-sm rounded-full bg-gray-900 px-4 py-2 text-sm text-white shadow-lg flex items-center gap-2">
    <span>Link copied to clipboard</span>
    <button class="text-gray-400 hover:text-white"><svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
  </div>"""
    },
    {
        "id": "notification-015",
        "title": "Progress Notification",
        "description": "Notification showing progress bar.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
       <div class="flex justify-between items-center mb-1">
          <h4 class="text-sm font-medium text-gray-900">Exporting Data</h4>
          <span class="text-xs text-gray-500">45%</span>
       </div>
       <div class="w-full bg-gray-200 rounded-full h-1.5 dark:bg-gray-700">
         <div class="bg-indigo-600 h-1.5 rounded-full" style="width: 45%"></div>
       </div>
       <p class="mt-2 text-xs text-gray-400">This may take a few moments...</p>
    </div>
  </div>"""
    },
    {
        "id": "notification-016",
        "title": "Cookie Consent",
        "description": "Small cookie consent notification.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-xl ring-1 ring-black ring-opacity-5 p-4 border border-gray-100">
     <div class="flex items-start gap-4">
        <span class="text-2xl">🍪</span>
        <div class="flex-1">
           <p class="text-sm font-medium text-gray-900 mb-1">We use cookies</p>
           <p class="text-xs text-gray-500 mb-3">To ensure you get the best experience on our website.</p>
           <div class="flex gap-2">
              <button class="bg-indigo-600 text-white text-xs px-3 py-1.5 rounded font-medium hover:bg-indigo-500">Accept</button>
              <button class="bg-gray-100 text-gray-700 text-xs px-3 py-1.5 rounded font-medium hover:bg-gray-200">Settings</button>
           </div>
        </div>
        <button class="text-gray-400 hover:text-gray-500"><svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
     </div>
  </div>"""
    },
    {
        "id": "notification-017",
        "title": "System Update",
        "description": "Notification about system update.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-md rounded-lg bg-indigo-50 shadow-md border border-indigo-100 p-4">
    <div class="flex">
      <div class="flex-shrink-0">
         <svg class="h-5 w-5 text-indigo-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
           <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
         </svg>
      </div>
      <div class="ml-3 flex-1 md:flex md:justify-between">
        <p class="text-sm text-indigo-700">A new software update is available. See what’s new in version 2.0.4.</p>
        <p class="mt-3 text-sm md:ml-6 md:mt-0">
          <a href="#" class="whitespace-nowrap font-medium text-indigo-700 hover:text-indigo-600">Details <span aria-hidden="true">&rarr;</span></a>
        </p>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-018",
        "title": "Email Confirmed",
        "description": "Notification for email confirmation.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5 relative">
    <div class="absolute top-0 left-0 w-1 h-full bg-green-500"></div>
    <div class="p-4 pl-6">
      <div class="flex items-start">
        <div class="flex-1">
           <h3 class="text-sm font-medium text-gray-900">Email Confirmed</h3>
           <p class="mt-1 text-sm text-gray-500">Thank you for verifying your email address. Your account is now fully active.</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-019",
        "title": "Network Offline",
        "description": "Notification for offline status.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-red-50 shadow-md ring-1 ring-red-100">
    <div class="p-4">
      <div class="flex">
        <div class="flex-shrink-0">
           <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
             <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clip-rule="evenodd" />
           </svg>
        </div>
        <div class="ml-3">
          <h3 class="text-sm font-medium text-red-800">Connection Lost</h3>
          <div class="mt-2 text-sm text-red-700">
            <p>You appear to be offline. Reconnecting in 3s...</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-020",
        "title": "Achievement Unlocked Notification",
        "description": "Notification for game achievement.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gradient-to-r from-yellow-100 to-yellow-50 shadow-lg ring-1 ring-yellow-200">
     <div class="p-4 flex items-center gap-4">
        <div class="h-12 w-12 flex items-center justify-center rounded-full bg-yellow-200 text-2xl border-2 border-white shadow-sm">
           🏆
        </div>
        <div class="flex-1">
           <p class="text-xs font-bold text-yellow-800 uppercase tracking-wide">Achievement Unlocked</p>
           <p class="text-sm font-semibold text-gray-900">Master Coder</p>
           <p class="text-xs text-gray-600">You wrote 1000 lines of code!</p>
        </div>
     </div>
  </div>"""
    }
]
TEMPLATES_NOTIFICATIONS_3 = [
    {
        "id": "notification-021",
        "title": "Interactive Notification",
        "description": "Notification with input field.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
          <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
        </div>
        <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Lindsay Walton</p>
          <p class="mt-1 text-sm text-gray-500">Commented on your post.</p>
          <div class="mt-2">
             <form class="relative">
                <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-xs sm:leading-6" placeholder="Reply...">
                <button type="submit" class="absolute inset-y-0 right-0 flex items-center pr-3 group">
                   <svg class="h-4 w-4 text-gray-400 group-hover:text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" /></svg>
                </button>
             </form>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-022",
        "title": "Reminder Notification",
        "description": "Notification event reminder.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
       <div class="flex items-center gap-4">
          <div class="flex flex-col items-center justify-center h-12 w-12 rounded-lg bg-indigo-50 text-indigo-700 bg-opacity-50">
             <span class="text-xs font-bold uppercase">Oct</span>
             <span class="text-lg font-bold">24</span>
          </div>
          <div class="flex-1">
             <h4 class="text-sm font-medium text-gray-900">Team Meeting</h4>
             <p class="text-xs text-gray-500">10:00 AM - 11:30 AM</p>
             <p class="text-xs text-gray-500">Conference Room A</p>
          </div>
          <button class="rounded-full p-1 text-gray-400 hover:bg-gray-100 hover:text-gray-500"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"/></svg></button>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-023",
        "title": "File Download",
        "description": "Notification for file download complete.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
     <div class="p-4 flex items-center">
        <div class="h-10 w-10 flex-shrink-0 rounded bg-indigo-100 flex items-center justify-center text-indigo-600">
           <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
           <div class="flex justify-between items-start">
              <p class="text-sm font-medium text-gray-900 truncate">report-q3.pdf</p>
              <span class="text-xs text-green-600 font-medium bg-green-50 px-2 py-0.5 rounded-full">Completed</span>
           </div>
           <p class="text-xs text-gray-500 mt-1">2.4 MB</p>
        </div>
        <div class="ml-4 flex flex-shrink-0 gap-2">
           <button class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg></button>
           <button class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
        </div>
     </div>
  </div>"""
    },
    {
        "id": "notification-024",
        "title": "Low Battery",
        "description": "Notification warning for low battery.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex">
         <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M12 9v5m0 0v-5m0 0h.01m0 0h-.01m-2.293 9.414a1 1 0 001.414 0L12 12.586l1.121 1.121a1 1 0 001.414 0L14.414 13l2.293-2.293a1 1 0 000-1.414L12 4.586 7.293 9.293a1 1 0 000 1.414l2.293 2.293zm0 0l2.293 2.293z" /></svg>
         </div>
         <div class="ml-3 w-0 flex-1">
            <h3 class="text-sm font-medium text-gray-900">Low Battery</h3>
            <p class="mt-1 text-sm text-gray-500">10% remaining. Please plug in your charger.</p>
            <div class="mt-3">
               <button class="text-sm font-medium text-indigo-600 hover:text-indigo-500">Enable Power Saver</button>
            </div>
         </div>
         <div class="ml-4 flex flex-shrink-0">
            <button class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
         </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-025",
        "title": "Mention Notification",
        "description": "Notification user mention.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-indigo-600 text-white shadow-lg">
     <div class="p-4">
        <div class="flex items-start">
           <div class="flex-shrink-0">
              <span class="inline-flex items-center justify-center h-8 w-8 rounded-full bg-indigo-500">
                 <span class="text-sm font-medium leading-none text-white">@</span>
              </span>
           </div>
           <div class="ml-3 w-0 flex-1">
              <p class="text-sm font-semibold">New Mention</p>
              <p class="mt-1 text-sm text-indigo-100">
                 <span class="font-bold">@sarah</span> mentioned you in <span class="underline">Project X</span>
              </p>
              <p class="mt-2 text-xs text-indigo-200 italic">"Can you take a look at the latest designs?"</p>
           </div>
           <div class="ml-4 flex flex-shrink-0">
              <button class="text-indigo-200 hover:text-white"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
           </div>
        </div>
     </div>
  </div>"""
    },
    {
        "id": "notification-026",
        "title": "Verification Code",
        "description": "Notification with verification code.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
     <div class="p-4 text-center">
        <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-blue-100 mb-3">
           <svg class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
        </div>
        <h3 class="text-base font-semibold text-gray-900 mb-1">Verification Code</h3>
        <p class="text-sm text-gray-500 mb-4">Use this code to sign in to your dashboard.</p>
        <div class="bg-gray-100 rounded-lg p-2 mb-4">
           <span class="text-2xl font-mono font-bold tracking-widest text-gray-800">8429</span>
        </div>
        <button class="text-sm font-medium text-indigo-600 hover:text-indigo-500">Copy Code</button>
     </div>
  </div>"""
    },
    {
        "id": "notification-027",
        "title": "Welcome Notification",
        "description": "Notification for new user welcome.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gradient-to-r from-purple-500 to-indigo-600 shadow-lg text-white">
    <div class="p-1">
      <div class="bg-white/10 backdrop-blur-sm rounded-md p-4">
         <div class="flex items-start">
            <div class="flex-shrink-0">
               <span class="text-2xl">🎉</span>
            </div>
            <div class="ml-3 flex-1">
               <h3 class="text-sm font-bold">Welcome Aboard!</h3>
               <p class="mt-1 text-xs text-white/90">Thanks for joining our platform. We're excited to help you build amazing things.</p>
               <div class="mt-3">
                  <button class="bg-white text-indigo-600 text-xs font-bold px-3 py-1.5 rounded-full shadow-sm hover:bg-gray-50">Get Started</button>
               </div>
            </div>
            <button class="text-white/60 hover:text-white"><svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
         </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-028",
        "title": "Task Assigned",
        "description": "Notification for task assignment.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4 border-l-4 border-blue-500">
       <div class="flex justify-between items-start">
          <div>
             <p class="text-xs font-semibold text-blue-500 uppercase tracking-wide mb-1">New Task</p>
             <h3 class="text-sm font-bold text-gray-900">Update Documentation</h3>
          </div>
          <span class="bg-red-100 text-red-800 text-xs font-medium px-2 py-0.5 rounded">High Prio</span>
       </div>
       <p class="mt-2 text-sm text-gray-600">Please review and update the API docs by EOD.</p>
       <div class="mt-3 flex items-center justify-between">
          <div class="flex -space-x-2">
             <img class="inline-block h-6 w-6 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
             <img class="inline-block h-6 w-6 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
          </div>
          <a href="#" class="text-xs font-medium text-blue-600 hover:text-blue-500">View Details &rarr;</a>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-029",
        "title": "Backup Failed",
        "description": "Notification for failed backup.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-md rounded-lg bg-white shadow-lg border border-red-200">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-10 w-10 text-red-100 bg-red-600 rounded-full p-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
        </div>
        <div class="ml-4 w-0 flex-1">
           <h3 class="text-lg font-medium text-gray-900">Backup Failed</h3>
           <p class="mt-1 text-sm text-gray-500">Automated daily backup failed due to insufficient storage space.</p>
           <div class="mt-4 flex gap-3">
              <button class="w-full rounded-md border border-transparent bg-red-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">Upgrade Storage</button>
              <button class="w-full rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Retry</button>
           </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
           <button class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-030",
        "title": "Live Stream Notification",
        "description": "Notification for live event.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gray-900 text-white shadow-xl ring-1 ring-white/10">
    <div class="relative overflow-hidden rounded-t-lg h-32">
       <img src="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="Event" class="w-full h-full object-cover opacity-75">
       <div class="absolute top-2 left-2 bg-red-600 text-white text-[10px] font-bold px-2 py-0.5 rounded animate-pulse">LIVE</div>
       <div class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent"></div>
    </div>
    <div class="p-4 -mt-6 relative z-10">
       <h3 class="text-lg font-bold">Design Conference 2023</h3>
       <p class="text-sm text-gray-300 mb-4">Keynote started: Future of UI</p>
       <button class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 rounded transition-colors">Watch Now</button>
    </div>
  </div>"""
    }
]
TEMPLATES_NOTIFICATIONS_4 = [
    {
        "id": "notification-031",
        "title": "Newsletter Signup",
        "description": "Notification with newsletter form.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
          <svg class="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Weekly Newsletter</p>
          <p class="mt-1 text-sm text-gray-500">Get the latest updates delivered to your inbox.</p>
          <div class="mt-3">
             <form class="flex gap-2">
                <label for="email" class="sr-only">Email address</label>
                <input type="email" name="email" id="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-xs sm:leading-6" placeholder="you@example.com">
                <button type="submit" class="flex-shrink-0 rounded-md bg-indigo-600 px-2 py-1.5 text-xs font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Subscribe</button>
             </form>
          </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-032",
        "title": "Security Alert",
        "description": "Notification for new login detection.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-orange-50 shadow-lg ring-1 ring-orange-200">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-orange-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
           <h3 class="text-sm font-medium text-orange-800">New Login Detected</h3>
           <div class="mt-2 text-sm text-orange-700">
              <p>Device: MacBook Pro (Chrome)<br>Location: San Francisco, CA<br>Time: Just now</p>
           </div>
           <div class="mt-4">
              <div class="-mx-2 -my-1.5 flex">
                 <button type="button" class="rounded-md bg-orange-50 px-2 py-1.5 text-sm font-medium text-orange-800 hover:bg-orange-100 focus:outline-none focus:ring-2 focus:ring-orange-600 focus:ring-offset-2 focus:ring-offset-orange-50">It was me</button>
                 <button type="button" class="ml-3 rounded-md bg-orange-50 px-2 py-1.5 text-sm font-medium text-orange-800 hover:bg-orange-100 focus:outline-none focus:ring-2 focus:ring-orange-600 focus:ring-offset-2 focus:ring-offset-orange-50">Secure Account</button>
              </div>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-033",
        "title": "Storage Warning",
        "description": "Notification storage almost full.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
          <svg class="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
          <h3 class="text-sm font-medium text-gray-900">Storage almost full</h3>
          <p class="mt-1 text-sm text-gray-500">You have used 9.5GB of your 10GB limit.</p>
          <div class="mt-3">
             <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-red-500 h-2 rounded-full" style="width: 95%"></div>
             </div>
          </div>
          <div class="mt-3">
             <button type="button" class="text-sm font-medium text-indigo-600 hover:text-indigo-500">Upgrade Plan</button>
          </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-034",
        "title": "Payment Failed",
        "description": "Notification for payment failure.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-red-50 shadow-lg ring-1 ring-red-200">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
           <h3 class="text-sm font-medium text-red-800">Payment Failed</h3>
           <p class="mt-1 text-sm text-red-700">We couldn't process your payment for Invoice #2023-10.</p>
           <p class="mt-2 text-xs text-red-600">Reason: Card declined.</p>
           <div class="mt-4">
              <button type="button" class="w-full rounded-md bg-red-100 px-3 py-2 text-sm font-semibold text-red-800 hover:bg-red-200">Update Payment Method</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-035",
        "title": "New Comment",
        "description": "Notification for new comment.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
       <div class="flex items-start">
          <div class="flex-shrink-0">
             <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt="">
          </div>
          <div class="ml-3 w-0 flex-1">
             <p class="text-sm font-medium text-gray-900">Tom Cook</p>
             <p class="text-xs text-gray-400">2 minutes ago</p>
             <div class="mt-2 text-sm text-gray-600 bg-gray-50 p-2 rounded">
                <p>"Looks great! I really like the new color scheme you used here."</p>
             </div>
             <div class="mt-2 flex gap-4">
                <button class="text-xs font-medium text-gray-500 hover:text-indigo-600">Like</button>
                <button class="text-xs font-medium text-gray-500 hover:text-indigo-600">Reply</button>
             </div>
          </div>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-036",
        "title": "System Maintenance",
        "description": "Notification for scheduled maintenance.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-indigo-900 text-indigo-100 shadow-xl">
    <div class="p-4">
       <div class="flex items-center mb-3">
          <svg class="h-5 w-5 mr-2 text-indigo-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
          <span class="font-bold">Scheduled Maintenance</span>
       </div>
       <p class="text-sm">We'll be offline for maintenance on <span class="font-semibold text-white">Sunday, Oct 29</span> from <span class="font-semibold text-white">2am to 4am UTC</span>.</p>
       <button class="mt-3 text-xs uppercase tracking-wider font-bold text-indigo-300 hover:text-white transition-colors">Add to Calendar</button>
    </div>
  </div>"""
    },
    {
        "id": "notification-037",
        "title": "Daily Digest",
        "description": "Notification summary digest.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
       <h3 class="text-sm font-bold text-gray-900 mb-2">Daily Digest &bull; Oct 25</h3>
       <ul class="space-y-3">
          <li class="flex items-center text-sm text-gray-600">
             <span class="h-2 w-2 bg-blue-500 rounded-full mr-2"></span>
             <span>5 new tasks assigned</span>
          </li>
          <li class="flex items-center text-sm text-gray-600">
             <span class="h-2 w-2 bg-green-500 rounded-full mr-2"></span>
             <span>Project Alpha completed</span>
          </li>
          <li class="flex items-center text-sm text-gray-600">
             <span class="h-2 w-2 bg-purple-500 rounded-full mr-2"></span>
             <span>2 team meetings scheduled</span>
          </li>
       </ul>
       <button class="mt-4 w-full bg-gray-50 text-gray-600 text-xs font-semibold py-2 rounded border border-gray-200 hover:bg-gray-100">Read Full Digest</button>
    </div>
  </div>"""
    },
    {
        "id": "notification-038",
        "title": "Connection Restored",
        "description": "Notification connection success.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-green-50 shadow-md ring-1 ring-green-100">
    <div class="p-4">
      <div class="flex items-center">
        <div class="flex-shrink-0">
           <svg class="h-5 w-5 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        </div>
        <div class="ml-3">
           <p class="text-sm font-medium text-green-800">Connection Restored</p>
        </div>
        <div class="ml-auto pl-3">
           <div class="-mx-1.5 -my-1.5">
              <button type="button" class="inline-flex rounded-md bg-green-50 p-1.5 text-green-500 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-green-600 focus:ring-offset-2 focus:ring-offset-green-50">
                 <span class="sr-only">Dismiss</span>
                 <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
              </button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-039",
        "title": "Subscription Renewed",
        "description": "Notification subscription info.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4 border-t-4 border-indigo-500 rounded-lg">
       <h3 class="text-sm font-bold text-gray-900">Subscription Renewed</h3>
       <p class="mt-1 text-sm text-gray-500">Your Pro Plan has been renewed for another month.</p>
       <div class="mt-3 flex justify-between items-center text-xs">
          <span class="text-gray-400">Next billing: Nov 25, 2023</span>
          <a href="#" class="text-indigo-600 hover:text-indigo-500 font-medium">View Invoice</a>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-040",
        "title": "User Followed You",
        "description": "Notification social follow.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5 p-4">
     <div class="flex items-center">
        <div class="relative">
           <img class="h-10 w-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
           <div class="absolute -bottom-1 -right-1 bg-blue-500 rounded-full p-0.5 border-2 border-white">
              <svg class="h-3 w-3 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM17 7a1 1 0 10-2 0 1 1 0 002 0z" /></svg>
           </div>
        </div>
        <div class="ml-3 flex-1">
           <p class="text-sm font-medium text-gray-900"><span class="font-bold">Anna Smith</span> started following you</p>
           <p class="text-xs text-gray-500">UX Designer @ Apple</p>
        </div>
        <button class="ml-2 bg-indigo-50 text-indigo-700 text-xs font-semibold px-3 py-1.5 rounded-full hover:bg-indigo-100">Follow Back</button>
     </div>
  </div>"""
    }
]
TEMPLATES_NOTIFICATIONS_5 = [
    {
        "id": "notification-041",
        "title": "Group Invitation",
        "description": "Notification to join a group.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
          <div class="h-10 w-10 flex items-center justify-center rounded-lg bg-indigo-100 text-indigo-600">
             <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" /></svg>
          </div>
        </div>
        <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Frontend Team</p>
          <p class="mt-1 text-sm text-gray-500">Alex invited you to join this group.</p>
          <div class="mt-4 flex">
            <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Join Group</button>
            <button type="button" class="ml-3 inline-flex items-center rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">View Details</button>
          </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="inline-flex rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-042",
        "title": "Calendar Invite",
        "description": "Notification for calendar event.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
          <div class="h-10 w-10 flex items-center justify-center rounded-lg bg-red-50 text-red-600 font-bold border border-red-100">
             27
          </div>
        </div>
        <div class="ml-3 w-0 flex-1">
          <p class="text-sm font-medium text-gray-900">Project Kickoff</p>
          <p class="mt-1 text-sm text-gray-500">Friday, Oct 27 at 10:00 AM</p>
          <div class="mt-2 flex -space-x-1 overflow-hidden">
             <img class="inline-block h-6 w-6 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
             <img class="inline-block h-6 w-6 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
             <img class="inline-block h-6 w-6 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt=""/>
          </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
          <button type="button" class="text-indigo-600 hover:text-indigo-500 text-sm font-semibold">RSVP</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-043",
        "title": "Task Completed",
        "description": "Notification task completion.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4">
      <div class="flex items-center">
        <div class="flex-shrink-0">
           <div class="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center text-green-600">
              <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
           </div>
        </div>
        <div class="ml-3 w-0 flex-1">
           <p class="text-sm font-medium text-gray-900 line-through text-gray-500">Review quarterly report</p>
           <p class="text-xs text-gray-400">Completed by Sarah at 2:30 PM</p>
        </div>
        <div class="ml-4 flex flex-shrink-0">
           <button class="text-gray-400 hover:text-gray-500 text-xs">Undo</button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-044",
        "title": "Account Verification",
        "description": "Notification verify account.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-yellow-50 shadow-md border border-yellow-100">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
           <h3 class="text-sm font-semibold text-yellow-800">Verify your Account</h3>
           <p class="mt-1 text-sm text-yellow-700">Please verify your email address to access all features.</p>
           <div class="mt-3">
              <button class="bg-yellow-100 text-yellow-800 text-xs font-bold px-3 py-2 rounded hover:bg-yellow-200">Resend Verification Email</button>
           </div>
        </div>
        <div class="ml-4 flex flex-shrink-0">
           <button class="text-yellow-400 hover:text-yellow-500"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-045",
        "title": "Review Request",
        "description": "Notification requesting review.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-6 text-center">
       <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-indigo-100 mb-4 text-indigo-600">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" /></svg>
       </div>
       <h3 class="text-sm font-medium text-gray-900">Enjoying our app?</h3>
       <p class="mt-1 text-sm text-gray-500">Would you mind taking a moment to rate us?</p>
       <div class="mt-4 flex justify-center gap-3">
          <button class="text-gray-400 hover:text-gray-500 text-sm font-medium">No, thanks</button>
          <button class="bg-indigo-600 text-white text-sm font-semibold px-4 py-2 rounded hover:bg-indigo-500">Rate Now</button>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-046",
        "title": "Goal Reached",
        "description": "Notification goal celebration.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gradient-to-br from-green-400 to-emerald-600 text-white shadow-lg">
    <div class="p-4 flex items-center">
       <div class="h-12 w-12 rounded-full bg-white/20 flex items-center justify-center text-3xl">
          🎯
       </div>
       <div class="ml-4 flex-1">
          <h3 class="text-lg font-bold">Goal Reached!</h3>
          <p class="text-sm text-emerald-50">You hit your daily target of 10,000 steps.</p>
       </div>
       <div class="ml-2">
          <button class="text-white/70 hover:text-white"><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg></button>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-047",
        "title": "New Device Paired",
        "description": "Notification device paired.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-gray-800 text-gray-200 shadow-lg ring-1 ring-white/10">
    <div class="p-4">
      <div class="flex items-start">
        <div class="flex-shrink-0">
           <svg class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M12 9v5m0 0v-5m0 0h.01m0 0h-.01m-2.293 9.414a1 1 0 001.414 0L12 12.586l1.121 1.121a1 1 0 001.414 0L14.414 13l2.293-2.293a1 1 0 000-1.414L12 4.586 7.293 9.293a1 1 0 000 1.414l2.293 2.293zm0 0l2.293 2.293z" /></svg>
        </div>
        <div class="ml-3 w-0 flex-1">
           <h3 class="text-sm font-medium text-white">New Device Paired</h3>
           <p class="mt-1 text-sm text-gray-400">AirPods Pro connected</p>
           <div class="mt-2 text-xs text-gray-500">Battery: 85%</div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "notification-048",
        "title": "Refund Processed",
        "description": "Notification refund info.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5">
    <div class="p-4 flex items-center">
       <div class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center text-green-600">
          <span class="text-lg font-bold">$</span>
       </div>
       <div class="ml-3 flex-1">
          <p class="text-sm font-medium text-gray-900">Refund Processed</p>
          <p class="text-sm text-gray-500">Your refund of $49.00 has been sent.</p>
       </div>
       <a href="#" class="text-sm font-medium text-indigo-600 hover:text-indigo-500 p-2">View</a>
    </div>
  </div>"""
    },
    {
        "id": "notification-049",
        "title": "Message Failed",
        "description": "Notification message failure.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-auto max-w-sm rounded-full bg-red-100 pl-2 pr-4 py-1 text-red-700 shadow-sm flex items-center gap-2 border border-red-200">
    <div class="h-6 w-6 rounded-full bg-red-200 flex items-center justify-center flex-shrink-0">
       <svg class="h-4 w-4 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
    </div>
    <span class="text-sm font-medium">Message failed to send</span>
    <button class="ml-2 text-xs uppercase font-bold text-red-800 hover:text-red-900 underline">Retry</button>
  </div>"""
    },
    {
        "id": "notification-050",
        "title": "Welcome Bonus",
        "description": "Notification bonus info.",
        "dir": "templates/14-notifications",
        "content": """
  <div class="pointer-events-auto w-full max-w-sm rounded-lg bg-white shadow-lg ring-1 ring-black ring-opacity-5 overflow-hidden">
    <div class="h-2 bg-gradient-to-r from-pink-500 to-yellow-500"></div>
    <div class="p-4">
       <h3 class="text-lg font-bold text-gray-900">You got a bonus!</h3>
       <p class="mt-1 text-sm text-gray-500">Congrats! You've earned a $10 credit to use on your next purchase.</p>
       <button class="mt-4 w-full bg-black text-white py-2 rounded-md font-medium text-sm hover:bg-gray-800 transition-colors">Claim Credit</button>
    </div>
  </div>"""
    }
]
TEMPLATES_NOTIFICATIONS = TEMPLATES_NOTIFICATIONS_1 + TEMPLATES_NOTIFICATIONS_2 + TEMPLATES_NOTIFICATIONS_3 + TEMPLATES_NOTIFICATIONS_4 + TEMPLATES_NOTIFICATIONS_5

 # Part 3: Footers 001-050
TEMPLATES_FOOTERS_1 = [
    {
        "id": "footer-001",
        "title": "Simple Copyright",
        "description": "Minimalist footer with copyright.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-center lg:px-8">
      <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-002",
        "title": "Centered Links",
        "description": "Footer with centered navigation links.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl overflow-hidden px-6 py-20 sm:py-24 lg:px-8">
      <nav class="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12" aria-label="Footer">
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">About</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Blog</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Jobs</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Press</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Accessibility</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Partners</a>
        </div>
      </nav>
      <p class="mt-10 text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-003",
        "title": "Split Links & Copyright",
        "description": "Links on left, copyright on right.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2">
         <a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">Facebook</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/></svg></a>
         <a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">Twitter</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg></a>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-004",
        "title": "Social Icons Only",
        "description": "Footer with just social links",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-center lg:px-8">
      <div class="flex justify-center space-x-6">
         <a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">Instagram</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.468 3.2c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd"/></svg></a>
         <a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">GitHub</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/></svg></a>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-005",
        "title": "4 Columns",
        "description": "Footer with 4 columns of links.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-100" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <div class="space-y-8">
          <img class="h-7" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Company name">
          <p class="text-sm leading-6 text-gray-600">Making the world a better place through constructing elegant hierarchies.</p>
        </div>
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-gray-900">Solutions</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Marketing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Analytics</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Commerce</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Insights</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-gray-900">Support</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Pricing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Documentation</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Guides</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">API Status</a></li>
              </ul>
            </div>
          </div>
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-gray-900">Company</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">About</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Blog</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Jobs</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Press</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-gray-900">Legal</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Claim</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Privacy</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Terms</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-006",
        "title": "5 Columns",
        "description": "Footer with 5 columns of links.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <div class="space-y-8">
          <img class="h-7" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Company name">
          <p class="text-sm leading-6 text-gray-300">Making the world a better place through constructing elegant hierarchies.</p>
        </div>
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Solutions</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Marketing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Analytics</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Commerce</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Support</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Pricing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Documentation</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Guides</a></li>
              </ul>
            </div>
          </div>
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Company</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">About</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Blog</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Jobs</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Legal</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Claim</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Privacy</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Terms</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-007",
        "title": "Centered Newsletter",
        "description": "Footer with centered newsletter signup.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
      <div class="flex flex-col items-center">
         <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Subscribe to our newsletter.</h2>
         <p class="mt-4 text-lg leading-8 text-gray-300">The latest news, articles, and resources, sent to your inbox weekly.</p>
         <form class="mt-6 flex max-w-md gap-x-4">
            <label for="email-address" class="sr-only">Email address</label>
            <input id="email-address" name="email" type="email" autocomplete="email" required class="min-w-0 flex-auto rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6" placeholder="Enter your email">
            <button type="submit" class="flex-none rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Subscribe</button>
         </form>
         <p class="mt-8 text-xs leading-5 text-gray-400">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-008",
        "title": "Left Newsletter",
        "description": "Footer with newsletter signup on left.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 pb-8 pt-16 sm:pt-24 lg:px-8 lg:pt-32">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <div class="space-y-8">
          <img class="h-7" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Company name">
          <p class="text-sm leading-6 text-gray-600">Making the world a better place through constructing elegant hierarchies.</p>
          <div class="flex space-x-6">
             <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/></svg></a>
          </div>
        </div>
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
           <div class="md:grid md:grid-cols-2 md:gap-8">
             <div>
               <h3 class="text-sm font-semibold leading-6 text-gray-900">Solutions</h3>
               <ul role="list" class="mt-6 space-y-4">
                 <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Marketing</a></li>
               </ul>
             </div>
           </div>
           <div>
               <h3 class="text-sm font-semibold leading-6 text-gray-900">Subscribe</h3>
               <p class="mt-2 text-sm leading-6 text-gray-600">The latest news, articles, and resources, sent to your inbox weekly.</p>
               <form class="mt-6 sm:flex sm:max-w-md">
                 <label for="email-address" class="sr-only">Email address</label>
                 <input type="email" name="email-address" id="email-address" autocomplete="email" required class="w-full min-w-0 appearance-none rounded-md border-0 bg-white px-3 py-1.5 text-base text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:w-64 sm:text-sm sm:leading-6 xl:w-full" placeholder="Enter your email">
                 <div class="mt-4 sm:ml-4 sm:mt-0 sm:flex-shrink-0">
                   <button type="submit" class="flex w-full items-center justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Subscribe</button>
                 </div>
               </form>
           </div>
        </div>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-009",
        "title": "Logo and Social",
        "description": "Footer with large logo and social links.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl overflow-hidden px-6 py-20 sm:py-24 lg:px-8">
      <div class="flex justify-center mb-8">
         <img class="h-10" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Company name">
      </div>
      <nav class="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12" aria-label="Footer">
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">About</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Blog</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Jobs</a>
        </div>
      </nav>
      <div class="mt-10 flex justify-center space-x-10">
         <a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">Twitter</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg></a>
      </div>
      <p class="mt-10 text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-010",
        "title": "Big Footer with App Download",
        "description": "Footer with app download badges.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <div class="space-y-8">
          <img class="h-7" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Company name">
          <p class="text-sm leading-6 text-gray-300">Making the world a better place through constructing elegant hierarchies.</p>
          <div class="flex space-x-4">
             <a href="#" class="rounded-md bg-gray-800 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700">App Store</a>
             <a href="#" class="rounded-md bg-gray-800 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700">Google Play</a>
          </div>
        </div>
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Solutions</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Marketing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Analytics</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Support</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Pricing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Documentation</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-16 border-t border-white/10 pt-8 sm:mt-20 lg:mt-24">
        <p class="text-xs leading-5 text-gray-400">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    }
]
TEMPLATES_FOOTERS_2 = [
    {
        "id": "footer-011",
        "title": "Minimal Social Dark",
        "description": "Minimal footer with social dark mode.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2">
         <a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">Facebook</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/></svg></a>
         <a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">Twitter</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg></a>
         <a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">GitHub</span><svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/></svg></a>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-012",
        "title": "Simple Dark",
        "description": "Minimal dark footer.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-center lg:px-8">
      <p class="text-center text-xs leading-5 text-gray-400">&copy; 2023 Your Company, Inc. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-013",
        "title": "Simple Centered Dark",
        "description": "Centered links dark footer.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900">
    <div class="mx-auto max-w-7xl overflow-hidden px-6 py-20 sm:py-24 lg:px-8">
      <nav class="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12" aria-label="Footer">
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">About</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Blog</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Jobs</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Press</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Accessibility</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Partners</a>
        </div>
      </nav>
      <p class="mt-10 text-center text-xs leading-5 text-gray-400">&copy; 2023 Your Company, Inc. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-014",
        "title": "2 Columns Split",
        "description": "2 columns split footer.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="flex justify-between">
            <div class="w-1/2 pr-8 border-r border-gray-200">
              <h3 class="text-sm font-semibold leading-6 text-gray-900">Solutions</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Marketing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Analytics</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Commerce</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Insights</a></li>
              </ul>
            </div>
            <div class="w-1/2 pl-8">
              <h3 class="text-sm font-semibold leading-6 text-gray-900">Company</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">About</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Blog</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Jobs</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Press</a></li>
              </ul>
            </div>
      </div>
      <div class="mt-16 border-t border-gray-900/10 pt-8 sm:mt-20 lg:mt-24">
        <p class="text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-015",
        "title": "3 Columns Newsletter",
        "description": "3 columns with newsletter.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="xl:grid xl:grid-cols-2 xl:gap-8">
        <div class="grid grid-cols-2 gap-8">
          <div>
            <h3 class="text-sm font-semibold leading-6 text-gray-900">Solutions</h3>
            <ul role="list" class="mt-6 space-y-4">
              <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Marketing</a></li>
              <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Analytics</a></li>
            </ul>
          </div>
          <div>
            <h3 class="text-sm font-semibold leading-6 text-gray-900">Support</h3>
            <ul role="list" class="mt-6 space-y-4">
              <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Pricing</a></li>
              <li><a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Documentation</a></li>
            </ul>
          </div>
        </div>
        <div class="mt-10 xl:mt-0">
          <h3 class="text-sm font-semibold leading-6 text-gray-900">Subscribe</h3>
          <p class="mt-2 text-sm leading-6 text-gray-600">The latest news, articles, and resources, sent to your inbox weekly.</p>
          <form class="mt-6 sm:flex sm:max-w-md">
            <label for="email-address" class="sr-only">Email address</label>
            <input type="email" name="email-address" id="email-address" autocomplete="email" required class="w-full min-w-0 appearance-none rounded-md border-0 bg-white px-3 py-1.5 text-base text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:w-64 sm:text-sm sm:leading-6 xl:w-full" placeholder="Enter your email">
            <div class="mt-4 sm:ml-4 sm:mt-0 sm:flex-shrink-0">
              <button type="submit" class="flex w-full items-center justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Subscribe</button>
            </div>
          </form>
        </div>
      </div>
      <div class="mt-16 border-t border-gray-900/10 pt-8 sm:mt-20 lg:mt-24">
        <p class="text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-016",
        "title": "4 Columns Dark",
        "description": "Dark footer with 4 columns.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <div class="space-y-8">
          <img class="h-7" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Company name">
          <p class="text-sm leading-6 text-gray-300">Making the world a better place through constructing elegant hierarchies.</p>
        </div>
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Solutions</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Marketing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Analytics</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Commerce</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Support</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Pricing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Documentation</a></li>
              </ul>
            </div>
          </div>
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Company</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">About</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Blog</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Legal</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Claim</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Privacy</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-017",
        "title": "5 Columns Dark",
        "description": "Dark footer with 5 columns.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <div class="space-y-8">
          <img class="h-7" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Company name">
          <p class="text-sm leading-6 text-gray-300">Making the world a better place through constructing elegant hierarchies.</p>
        </div>
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Solutions</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Marketing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Analytics</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Commerce</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Support</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Pricing</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Documentation</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Guides</a></li>
              </ul>
            </div>
          </div>
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Company</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">About</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Blog</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Jobs</a></li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Legal</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Claim</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Privacy</a></li>
                <li><a href="#" class="text-sm leading-6 text-gray-300 hover:text-white">Terms</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-16 border-t border-white/10 pt-8 sm:mt-20 lg:mt-24">
        <p class="text-xs leading-5 text-gray-400">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-018",
        "title": "Big Footer with Map",
        "description": "Footer with embedded map.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-16 sm:py-24 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div>
                 <h2 class="text-2xl font-bold tracking-tight text-gray-900">Visit our office</h2>
                 <p class="mt-6 text-base text-gray-600">
                    1234 Rainbow Road<br>
                    San Francisco, CA 94107
                 </p>
                 <div class="mt-8 rounded-lg overflow-hidden h-64 bg-gray-100 border border-gray-200">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d100939.98555098464!2d-122.507640204439!3d37.757814996609724!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80859a6d00690021%3A0x4a501367f076adff!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1619524992238!5m2!1sen!2sus" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
                 </div>
            </div>
            <div>
              <h2 class="text-2xl font-bold tracking-tight text-gray-900">Get in touch</h2>
              <ul role="list" class="mt-6 space-y-4">
                <li><a href="#" class="text-base text-gray-600 hover:text-gray-900">Sales</a></li>
                <li><a href="#" class="text-base text-gray-600 hover:text-gray-900">Support</a></li>
                <li><a href="#" class="text-base text-gray-600 hover:text-gray-900">Partnerships</a></li>
                <li><a href="#" class="text-base text-gray-600 hover:text-gray-900">Press</a></li>
              </ul>
              <div class="mt-10 border-t border-gray-100 pt-8">
                 <p class="text-xs text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
              </div>
            </div>
        </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-019",
        "title": "Language Selector",
        "description": "Footer with language picker.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2">
         <select class="rounded-md bg-gray-800 border-gray-700 text-gray-300 text-sm focus:ring-indigo-500 focus:border-indigo-500">
             <option>English</option>
             <option>Spanish</option>
             <option>French</option>
             <option>German</option>
         </select>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-020",
        "title": "Currency Selector",
        "description": "Footer with currency picker.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2">
         <select class="rounded-md bg-gray-100 border-gray-200 text-gray-900 text-sm focus:ring-indigo-600 focus:border-indigo-600">
             <option>USD ($)</option>
             <option>EUR (€)</option>
             <option>GBP (£)</option>
             <option>JPY (¥)</option>
         </select>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    }
]
TEMPLATES_FOOTERS_3 = [
    {
        "id": "footer-021",
        "title": "Footer with Search",
        "description": "Footer containing a search bar.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-50">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center md:order-2">
         <form class="flex gap-2">
            <input type="text" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Search...">
            <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">Search</button>
         </form>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-022",
        "title": "Top Border Footer",
        "description": "Footer with distinct top border.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white border-t-4 border-indigo-600">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-center lg:px-8">
      <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-023",
        "title": "Mobile Bottom Nav",
        "description": "Sticky bottom navigation for mobile.",
        "dir": "templates/10-footers",
        "content": """
  <div class="relative min-h-[200px] bg-gray-100 flex items-end justify-center">
    <footer class="w-full bg-white border-t border-gray-200">
       <div class="grid grid-cols-4 gap-1 p-2">
          <a href="#" class="flex flex-col items-center justify-center py-2 text-indigo-600">
             <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
             <span class="text-xs mt-1 font-medium">Home</span>
          </a>
          <a href="#" class="flex flex-col items-center justify-center py-2 text-gray-500 hover:text-gray-900">
             <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
             <span class="text-xs mt-1 font-medium">Search</span>
          </a>
          <a href="#" class="flex flex-col items-center justify-center py-2 text-gray-500 hover:text-gray-900">
             <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>
             <span class="text-xs mt-1 font-medium">Notifs</span>
          </a>
          <a href="#" class="flex flex-col items-center justify-center py-2 text-gray-500 hover:text-gray-900">
             <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
             <span class="text-xs mt-1 font-medium">Profile</span>
          </a>
       </div>
    </footer>
  </div>"""
    },
    {
        "id": "footer-024",
        "title": "Simple Brand Footer",
        "description": "Footer with dominant brand color.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-indigo-600">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-center lg:px-8">
      <div class="flex flex-col items-center">
         <img class="h-8 mb-6 brightness-0 invert" src="https://tailwindui.com/img/logos/mark.svg?color=white" alt="Company name">
         <p class="text-center text-xs leading-5 text-indigo-100">&copy; 2023 Your Company, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-025",
        "title": "Detailed Brand Footer",
        "description": "Brand footer with links.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-indigo-900" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-12 border-b border-indigo-800 pb-12">
          <div>
             <h3 class="text-lg font-bold text-white mb-4">Product</h3>
             <ul class="space-y-2 text-indigo-200 text-sm">
                <li><a href="#" class="hover:text-white">Features</a></li>
                <li><a href="#" class="hover:text-white">Integrations</a></li>
                <li><a href="#" class="hover:text-white">Pricing</a></li>
             </ul>
          </div>
          <div>
             <h3 class="text-lg font-bold text-white mb-4">Resources</h3>
             <ul class="space-y-2 text-indigo-200 text-sm">
                <li><a href="#" class="hover:text-white">Documentation</a></li>
                <li><a href="#" class="hover:text-white">Guides</a></li>
                <li><a href="#" class="hover:text-white">Support</a></li>
             </ul>
          </div>
           <div>
             <h3 class="text-lg font-bold text-white mb-4">Company</h3>
             <ul class="space-y-2 text-indigo-200 text-sm">
                <li><a href="#" class="hover:text-white">About</a></li>
                <li><a href="#" class="hover:text-white">Blog</a></li>
                <li><a href="#" class="hover:text-white">Careers</a></li>
             </ul>
          </div>
           <div>
             <h3 class="text-lg font-bold text-white mb-4">Legal</h3>
             <ul class="space-y-2 text-indigo-200 text-sm">
                <li><a href="#" class="hover:text-white">Privacy</a></li>
                <li><a href="#" class="hover:text-white">Terms</a></li>
             </ul>
          </div>
       </div>
       <div class="flex justify-between items-center text-indigo-300 text-sm">
           <p>&copy; 2023 BrandName.</p>
           <div class="flex space-x-6">
              <a href="#" class="hover:text-white">Twitter</a>
              <a href="#" class="hover:text-white">LinkedIn</a>
           </div>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-026",
        "title": "Footer with Reviews",
        "description": "Footer showing review badge.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <div class="flex flex-col md:flex-row justify-between items-center gap-6">
          <div class="flex items-center gap-2">
             <div class="flex text-yellow-400">
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
             </div>
             <span class="text-sm font-semibold text-gray-900">Rated 4.9/5 by 500+ customers</span>
          </div>
          <p class="text-xs text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-027",
        "title": "Certifications Footer",
        "description": "Footer showing certification logos.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-50">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
       <div class="flex space-x-6 items-center grayscale opacity-70">
          <img class="h-8" src="https://tailwindui.com/img/logos/tuple-logo-gray-400.svg" alt="Certification 1">
          <img class="h-8" src="https://tailwindui.com/img/logos/reform-logo-gray-400.svg" alt="Certification 2">
          <img class="h-8" src="https://tailwindui.com/img/logos/savvycal-logo-gray-400.svg" alt="Certification 3">
       </div>
       <div class="mt-8 md:mt-0">
          <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-028",
        "title": "Payment Icons Footer",
        "description": "Footer with payment method icons.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
       <div>
          <p class="text-xs leading-5 text-gray-500">&copy; 2023 Your Company, Inc. All rights reserved.</p>
       </div>
       <div class="mt-8 md:mt-0 flex space-x-4">
           <div class="h-8 w-12 bg-gray-200 rounded flex items-center justify-center text-xs text-gray-500 font-bold">VISA</div>
           <div class="h-8 w-12 bg-gray-200 rounded flex items-center justify-center text-xs text-gray-500 font-bold">MC</div>
           <div class="h-8 w-12 bg-gray-200 rounded flex items-center justify-center text-xs text-gray-500 font-bold">AMEX</div>
           <div class="h-8 w-12 bg-gray-200 rounded flex items-center justify-center text-xs text-gray-500 font-bold">PP</div>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-029",
        "title": "Footer with Contact Form",
        "description": "Footer containing a mini contact form.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-800 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div>
               <h2 class="text-2xl font-bold mb-4">Contact Us</h2>
               <p class="text-gray-400 mb-6">Have questions? Send us a message directly.</p>
               <form class="space-y-4">
                  <input type="email" placeholder="Your Email" class="w-full rounded bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:ring-indigo-500">
                  <textarea placeholder="Message" rows="3" class="w-full rounded bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:ring-indigo-500"></textarea>
                  <button type="submit" class="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded font-medium">Send Message</button>
               </form>
            </div>
            <div class="pl-0 md:pl-12">
               <h3 class="text-xl font-bold mb-4">Links</h3>
               <ul class="space-y-2 text-gray-400">
                  <li><a href="#" class="hover:text-white">FAQ</a></li>
                  <li><a href="#" class="hover:text-white">Shipping</a></li>
                  <li><a href="#" class="hover:text-white">Returns</a></li>
               </ul>
            </div>
        </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-030",
        "title": "Recent Posts Footer",
        "description": "Footer with recent blog posts.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16 lg:px-8">
       <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
             <h3 class="font-bold text-lg mb-4">About Us</h3>
             <p class="text-gray-400 text-sm">We are a team of passionate developers building the future of web.</p>
          </div>
          <div class="col-span-2">
             <h3 class="font-bold text-lg mb-4">Recent Posts</h3>
             <ul class="space-y-4">
                <li>
                   <a href="#" class="group block">
                      <span class="text-sm font-medium group-hover:text-indigo-400 transition-colors">How to optimize your React app</span>
                      <span class="block text-xs text-gray-500">Oct 24, 2023</span>
                   </a>
                </li>
                 <li>
                   <a href="#" class="group block">
                      <span class="text-sm font-medium group-hover:text-indigo-400 transition-colors">Understanding CSS Grid</span>
                      <span class="block text-xs text-gray-500">Oct 20, 2023</span>
                   </a>
                </li>
             </ul>
          </div>
       </div>
       <div class="mt-12 pt-8 border-t border-gray-800 text-center text-xs text-gray-500">
          &copy; 2023 Blog Company.
       </div>
    </div>
  </footer>"""
    }
]
TEMPLATES_FOOTERS_4 = [
    {
        "id": "footer-031",
        "title": "Team Avatars Footer",
        "description": "Footer showing team member avatars.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <div class="flex flex-col items-center">
          <p class="text-gray-500 text-sm mb-4">Built by the team at Company</p>
          <div class="flex -space-x-2 overflow-hidden mb-6">
             <img class="inline-block h-8 w-8 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
             <img class="inline-block h-8 w-8 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
             <img class="inline-block h-8 w-8 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt=""/>
             <img class="inline-block h-8 w-8 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""/>
          </div>
          <p class="text-xs text-gray-400">&copy; 2023 Your Company, Inc. All rights reserved.</p>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-032",
        "title": "Footer with Stats",
        "description": "Footer displaying some key stats.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900 text-white">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center border-b border-gray-700 pb-12 mb-8">
          <div>
             <p class="text-3xl font-bold text-indigo-400">100k+</p>
             <p class="text-sm text-gray-400">Users</p>
          </div>
          <div>
             <p class="text-3xl font-bold text-indigo-400">99.9%</p>
             <p class="text-sm text-gray-400">Uptime</p>
          </div>
          <div>
             <p class="text-3xl font-bold text-indigo-400">24/7</p>
             <p class="text-sm text-gray-400">Support</p>
          </div>
       </div>
       <div class="flex justify-between items-center text-xs text-gray-500">
           <p>&copy; 2023 Stats Company.</p>
           <a href="#" class="hover:text-white">Privacy Policy</a>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-033",
        "title": "Footer with Screenshot",
        "description": "Footer showing a product screenshot.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white overflow-hidden">
    <div class="mx-auto max-w-7xl px-6 pt-16 lg:px-8">
       <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          <div>
             <h2 class="text-2xl font-bold text-gray-900">Try our app today</h2>
             <p class="mt-4 text-gray-600">Download for iOS and Android.</p>
             <div class="mt-6 flex gap-4">
                <button class="bg-black text-white px-4 py-2 rounded-lg">App Store</button>
                <button class="bg-black text-white px-4 py-2 rounded-lg">Play Store</button>
             </div>
             <p class="mt-8 text-xs text-gray-500">&copy; 2023 App Company.</p>
          </div>
          <div class="relative h-64 lg:h-80 w-full bg-gray-100 rounded-t-xl overflow-hidden mt-8 lg:mt-0">
              <img src="https://tailwindui.com/img/component-images/project-app-screenshot.png" alt="App screenshot" class="absolute top-0 left-0 w-full h-full object-cover object-top">
          </div>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-034",
        "title": "Partner Logos Footer",
        "description": "Footer with partner company logos.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-50">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <p class="text-center text-sm font-semibold text-gray-500">Trusted by top companies</p>
       <div class="mt-6 grid grid-cols-2 gap-8 md:grid-cols-5 opacity-60 grayscale">
          <div class="flex justify-center"><img class="h-8" src="https://tailwindui.com/img/logos/transistor-logo-gray-400.svg" alt="Transistor"></div>
          <div class="flex justify-center"><img class="h-8" src="https://tailwindui.com/img/logos/reform-logo-gray-400.svg" alt="Reform"></div>
          <div class="flex justify-center"><img class="h-8" src="https://tailwindui.com/img/logos/tuple-logo-gray-400.svg" alt="Tuple"></div>
          <div class="flex justify-center"><img class="h-8" src="https://tailwindui.com/img/logos/savvycal-logo-gray-400.svg" alt="SavvyCal"></div>
          <div class="flex justify-center"><img class="h-8" src="https://tailwindui.com/img/logos/statamic-logo-gray-400.svg" alt="Statamic"></div>
       </div>
       <div class="mt-12 text-center text-xs text-gray-400">
          &copy; 2023 Partner Network.
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-035",
        "title": "Blog Grid Footer",
        "description": "Footer with featured blog posts grid.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white border-t border-gray-200">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <h3 class="text-lg font-bold text-gray-900 mb-6">Latest from the blog</h3>
       <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <a href="#" class="group">
             <div class="h-40 bg-gray-100 rounded-lg mb-3"></div>
             <h4 class="font-medium text-gray-900 group-hover:text-indigo-600">Article Title 1</h4>
             <p class="text-sm text-gray-500">Short excerpt goes here.</p>
          </a>
          <a href="#" class="group">
             <div class="h-40 bg-gray-100 rounded-lg mb-3"></div>
             <h4 class="font-medium text-gray-900 group-hover:text-indigo-600">Article Title 2</h4>
             <p class="text-sm text-gray-500">Short excerpt goes here.</p>
          </a>
          <a href="#" class="group">
             <div class="h-40 bg-gray-100 rounded-lg mb-3"></div>
             <h4 class="font-medium text-gray-900 group-hover:text-indigo-600">Article Title 3</h4>
             <p class="text-sm text-gray-500">Short excerpt goes here.</p>
          </a>
       </div>
       <div class="border-t border-gray-100 pt-8 flex justify-between items-center">
          <p class="text-xs text-gray-500">&copy; 2023 Blog Footer.</p>
          <div class="flex gap-4">
             <a href="#" class="text-gray-400 hover:text-gray-500">RSS</a>
             <a href="#" class="text-gray-400 hover:text-gray-500">Twitter</a>
          </div>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-036",
        "title": "Testimonial Footer",
        "description": "Footer featuring a customer quote.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-indigo-700 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16 lg:px-8">
       <div class="text-center mb-12">
          <blockquote class="text-xl font-semibold italic">
             "This product completely changed how we work. Highly recommended!"
          </blockquote>
          <div class="mt-4">
             <p class="font-bold">Jane Doe</p>
             <p class="text-indigo-200 text-sm">CEO at ExampleCorp</p>
          </div>
       </div>
       <div class="border-t border-indigo-500 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-indigo-200">
          <p>&copy; 2023 Testimonial Inc.</p>
          <ul class="flex space-x-6 mt-4 md:mt-0">
             <li><a href="#" class="hover:text-white">Terms</a></li>
             <li><a href="#" class="hover:text-white">Privacy</a></li>
          </ul>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-037",
        "title": "CTA Footer",
        "description": "Footer with prominent Call to Action.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-50">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8 text-center">
       <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Ready to get started?</h2>
       <p class="mt-4 text-lg leading-8 text-gray-600">Join thousands of satisfied customers today.</p>
       <div class="mt-8 flex items-center justify-center gap-x-6">
          <a href="#" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Get started</a>
          <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Learn more <span aria-hidden="true">→</span></a>
       </div>
       <div class="mt-12 border-t border-gray-200 pt-8">
          <p class="text-xs text-gray-500">&copy; 2023 CTA Company, Inc.</p>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-038",
        "title": "Legal Footer",
        "description": "Footer focused on legal links.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white border-t border-gray-200">
    <div class="mx-auto max-w-7xl px-6 py-8 md:flex md:items-center md:justify-between lg:px-8">
       <div class="flex space-x-6 md:order-2 text-sm text-gray-600">
          <a href="#" class="hover:text-gray-900 hover:underline">Privacy Policy</a>
          <a href="#" class="hover:text-gray-900 hover:underline">Terms of Service</a>
          <a href="#" class="hover:text-gray-900 hover:underline">Cookie Policy</a>
          <a href="#" class="hover:text-gray-900 hover:underline">GDPR</a>
       </div>
       <div class="mt-8 md:order-1 md:mt-0">
          <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Legal Entity. All rights reserved.</p>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-039",
        "title": "Cookie Consent Link",
        "description": "Footer with explicit cookie settings link.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900 text-white">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex space-x-4 md:order-2">
         <button class="text-xs text-gray-400 hover:text-white underline">Cookie Settings</button>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
         <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Privacy First. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-040",
        "title": "Support Chat Trigger",
        "description": "Footer with support chat button.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white relative">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2">
         <a href="#" class="text-gray-400 hover:text-gray-500">Contact</a>
         <a href="#" class="text-gray-400 hover:text-gray-500">Help Center</a>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Support Inc.</p>
      </div>
    </div>
    <div class="fixed bottom-4 right-4">
       <button class="bg-indigo-600 text-white p-3 rounded-full shadow-lg hover:bg-indigo-500 flex items-center gap-2">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
          <span class="font-semibold text-sm">Chat</span>
       </button>
    </div>
  </footer>"""
    }
]
TEMPLATES_FOOTERS_5 = [
    {
        "id": "footer-041",
        "title": "Status Indicator Footer",
        "description": "Footer showing system status.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2 items-center">
         <span class="flex h-3 w-3 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
         </span>
         <span class="text-sm text-gray-600">All systems operational</span>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 System Status. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-042",
        "title": "Theme Toggler Footer",
        "description": "Footer with theme switch.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-50">
    <div class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8">
      <div class="flex justify-center space-x-6 md:order-2">
         <button class="bg-white border rounded-lg px-3 py-1 text-sm text-gray-700 hover:bg-gray-100 shadow-sm">Light</button>
         <button class="bg-gray-800 border-gray-900 rounded-lg px-3 py-1 text-sm text-white hover:bg-gray-700 shadow-sm">Dark</button>
         <button class="bg-white border rounded-lg px-3 py-1 text-sm text-gray-700 hover:bg-gray-100 shadow-sm">Auto</button>
      </div>
      <div class="mt-8 md:order-1 md:mt-0">
        <p class="text-center text-xs leading-5 text-gray-500">&copy; 2023 Themed App. All rights reserved.</p>
      </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-043",
        "title": "App Badges Centered",
        "description": "Footer with app store badges centered.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8 text-center">
       <div class="flex justify-center gap-4 mb-8">
          <img class="h-10" src="https://tailwindui.com/img/logos/app-store-badge.svg" alt="App Store">
          <img class="h-10" src="https://tailwindui.com/img/logos/google-play-badge.svg" alt="Google Play">
       </div>
       <nav class="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12" aria-label="Footer">
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">About</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Blog</a>
        </div>
        <div class="pb-6">
          <a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Jobs</a>
        </div>
      </nav>
      <p class="mt-8 text-xs leading-5 text-gray-500">&copy; 2023 Mobile App. All rights reserved.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-044",
        "title": "Legal Heavy Footer",
        "description": "Footer with lots of small print.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-100 text-gray-500 text-xs">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <p class="mb-4">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
       </p>
       <p class="mb-4">
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
       </p>
       <div class="border-t border-gray-200 pt-8 flex justify-between">
          <p>&copy; 2023 Banking Corp.</p>
          <div class="flex space-x-4">
             <a href="#" class="hover:underline">Terms</a>
             <a href="#" class="hover:underline">Privacy</a>
             <a href="#" class="hover:underline">Security</a>
          </div>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-045",
        "title": "Two Rows Footer",
        "description": "Footer with navigation row and legal row.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
       <!-- Top Row: Navigation -->
       <div class="flex justify-center flex-wrap gap-8 text-sm font-semibold text-gray-900 mb-8 pb-8 border-b border-gray-100">
          <a href="#">Product</a>
          <a href="#">Features</a>
          <a href="#">Marketplace</a>
          <a href="#">Company</a>
          <a href="#">Team</a>
          <a href="#">Contact</a>
       </div>
       <!-- Bottom Row: Social & Copy -->
       <div class="flex flex-col md:flex-row justify-between items-center text-gray-400">
          <div class="flex space-x-6 mb-4 md:mb-0">
             <a href="#" class="hover:text-gray-500">FB</a>
             <a href="#" class="hover:text-gray-500">TW</a>
             <a href="#" class="hover:text-gray-500">IG</a>
          </div>
          <p class="text-xs">&copy; 2023 TwoRow Inc.</p>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-046",
        "title": "Grid Links Newsletter",
        "description": "Grid of links with newsletter on side.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16 lg:px-8 grid grid-cols-1 lg:grid-cols-5 gap-8">
       <div class="lg:col-span-2">
          <h2 class="text-2xl font-bold mb-4">Stay updated</h2>
          <p class="text-gray-400 mb-6">Join our newsletter for the latest updates.</p>
          <form class="flex gap-2">
             <input type="email" placeholder="Email" class="bg-gray-800 border-none rounded text-white p-2 w-full">
             <button class="bg-indigo-600 rounded px-4 py-2 hover:bg-indigo-500">Join</button>
          </form>
       </div>
       <div>
          <h3 class="font-bold mb-4">Product</h3>
          <ul class="space-y-2 text-gray-400 text-sm">
             <li><a href="#" class="hover:text-white">Overview</a></li>
             <li><a href="#" class="hover:text-white">Features</a></li>
             <li><a href="#" class="hover:text-white">Solutions</a></li>
             <li><a href="#" class="hover:text-white">Tutorials</a></li>
          </ul>
       </div>
        <div>
          <h3 class="font-bold mb-4">Company</h3>
          <ul class="space-y-2 text-gray-400 text-sm">
             <li><a href="#" class="hover:text-white">About</a></li>
             <li><a href="#" class="hover:text-white">Careers</a></li>
             <li><a href="#" class="hover:text-white">Press</a></li>
             <li><a href="#" class="hover:text-white">News</a></li>
          </ul>
       </div>
        <div>
          <h3 class="font-bold mb-4">Resource</h3>
          <ul class="space-y-2 text-gray-400 text-sm">
             <li><a href="#" class="hover:text-white">Blog</a></li>
             <li><a href="#" class="hover:text-white">Newsletter</a></li>
             <li><a href="#" class="hover:text-white">Events</a></li>
             <li><a href="#" class="hover:text-white">Help Center</a></li>
          </ul>
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-047",
        "title": "Background Image Footer",
        "description": "Footer with background image overlay.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="relative bg-gray-900 text-white">
    <div class="absolute inset-0 overflow-hidden">
       <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=2850&q=80" alt="" class="w-full h-full object-cover opacity-10">
    </div>
    <div class="relative mx-auto max-w-7xl px-6 py-16 lg:px-8 text-center">
       <h2 class="text-2xl font-bold mb-6">Join our community</h2>
       <p class="mb-8 max-w-2xl mx-auto text-gray-300">Connect with thousands of developers building the next generation of apps.</p>
       <button class="bg-white text-gray-900 font-bold px-6 py-3 rounded-full hover:bg-gray-100 transition">Get Involved</button>
       <div class="mt-12 text-xs text-gray-500">
          &copy; 2023 Community.
       </div>
    </div>
  </footer>"""
    },
    {
        "id": "footer-048",
        "title": "Gradient Footer",
        "description": "Footer with gradient background.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gradient-to-r from-purple-600 to-indigo-600 text-white">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8 flex flex-col md:flex-row justify-between items-center">
       <div class="mb-4 md:mb-0">
          <h2 class="text-xl font-bold">GradientBrand</h2>
          <p class="text-purple-200 text-sm">Design with color.</p>
       </div>
       <div class="flex space-x-6 text-purple-100">
          <a href="#" class="hover:text-white">Home</a>
          <a href="#" class="hover:text-white">About</a>
          <a href="#" class="hover:text-white">Contact</a>
       </div>
    </div>
    <div class="bg-black/10 py-4 text-center text-xs text-purple-200">
       &copy; 2023 Gradient Inc.
    </div>
  </footer>"""
    },
    {
        "id": "footer-049",
        "title": "Simple Top Logo",
        "description": "Footer with logo centered on top border.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-white relative mt-16 pt-16">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white p-4 rounded-full border border-gray-100 shadow-sm">
       <img class="h-8 w-8" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Logo">
    </div>
    <div class="mx-auto max-w-7xl px-6 pb-12 lg:px-8 text-center">
       <nav class="flex justify-center space-x-8 mb-8 text-sm font-medium text-gray-600">
          <a href="#" class="hover:text-gray-900">About</a>
          <a href="#" class="hover:text-gray-900">Blog</a>
          <a href="#" class="hover:text-gray-900">Jobs</a>
          <a href="#" class="hover:text-gray-900">Press</a>
       </nav>
       <p class="text-xs text-gray-400">&copy; 2023 TopLogo Inc.</p>
    </div>
  </footer>"""
    },
    {
        "id": "footer-050",
        "title": "Massive Site Map",
        "description": "Footer with extensive site map columns.",
        "dir": "templates/10-footers",
        "content": """
  <footer class="bg-gray-900 text-gray-300">
    <div class="mx-auto max-w-7xl px-6 py-16 lg:px-8">
       <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-8">
          <div class="col-span-2 lg:col-span-2">
             <img class="h-8 mb-4" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Logo">
             <p class="text-sm text-gray-400 mb-6 max-w-xs">Making web development easier and more accessible for everyone.</p>
             <div class="flex space-x-4">
                <a href="#" class="text-gray-400 hover:text-white">FB</a>
                <a href="#" class="text-gray-400 hover:text-white">TW</a>
                <a href="#" class="text-gray-400 hover:text-white">GH</a>
             </div>
          </div>
          <div>
             <h3 class="text-white font-bold mb-4">Product</h3>
             <ul class="space-y-2 text-sm">
                <li><a href="#" class="hover:text-white">Features</a></li>
                <li><a href="#" class="hover:text-white">Pricing</a></li>
                <li><a href="#" class="hover:text-white">Download</a></li>
                <li><a href="#" class="hover:text-white">Changelog</a></li>
             </ul>
          </div>
          <div>
             <h3 class="text-white font-bold mb-4">Company</h3>
             <ul class="space-y-2 text-sm">
                <li><a href="#" class="hover:text-white">About</a></li>
                <li><a href="#" class="hover:text-white">Blog</a></li>
                <li><a href="#" class="hover:text-white">Careers</a></li>
                <li><a href="#" class="hover:text-white">Contact</a></li>
             </ul>
          </div>
          <div>
             <h3 class="text-white font-bold mb-4">Resources</h3>
             <ul class="space-y-2 text-sm">
                <li><a href="#" class="hover:text-white">Docs</a></li>
                <li><a href="#" class="hover:text-white">Community</a></li>
                <li><a href="#" class="hover:text-white">Help</a></li>
                <li><a href="#" class="hover:text-white">Status</a></li>
             </ul>
          </div>
          <div>
             <h3 class="text-white font-bold mb-4">Legal</h3>
             <ul class="space-y-2 text-sm">
                <li><a href="#" class="hover:text-white">Privacy</a></li>
                <li><a href="#" class="hover:text-white">Terms</a></li>
                <li><a href="#" class="hover:text-white">Security</a></li>
                <li><a href="#" class="hover:text-white">Cookies</a></li>
             </ul>
          </div>
       </div>
       <div class="mt-16 pt-8 border-t border-gray-800 text-center text-xs text-gray-500">
          &copy; 2023 Massive Footer Inc. All rights reserved.
       </div>
    </div>
  </footer>"""
    }
]
TEMPLATES_FOOTERS = TEMPLATES_FOOTERS_1 + TEMPLATES_FOOTERS_2 + TEMPLATES_FOOTERS_3 + TEMPLATES_FOOTERS_4 + TEMPLATES_FOOTERS_5

# Part 4: Authentication 001-050
TEMPLATES_AUTHENTICATION_1 = [
    {
        "id": "auth-001",
        "title": "Simple Sign In",
        "description": "Minimal sign in form centered.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
            </div>
          </div>
          <div class="mt-2">
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Not a member?
        <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Start a 14-day free trial</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-002",
        "title": "Sign In Card",
        "description": "Sign in form in a card container.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8 bg-gray-50">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
      <div class="bg-white px-6 py-12 shadow sm:rounded-lg sm:px-12">
        <form class="space-y-6" action="#" method="POST">
          <div>
            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
            <div class="mt-2">
              <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            <div class="mt-2">
              <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
              <label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-900">Remember me</label>
            </div>

            <div class="text-sm leading-6">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
            </div>
          </div>

          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
          </div>
        </form>
      </div>

      <p class="mt-10 text-center text-sm text-gray-500">
        Not a member?
        <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Start a 14-day free trial</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-003",
        "title": "Split Screen Sign In",
        "description": "Split screen sign in with branding area.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-1">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
          <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
        </div>

        <div class="mt-10">
          <div>
            <form action="#" method="POST" class="space-y-6">
              <div>
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                <div class="mt-2">
                  <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>

              <div>
                <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                <div class="mt-2">
                  <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                  <label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-900">Remember me</label>
                </div>

                <div class="text-sm leading-6">
                  <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                </div>
              </div>

              <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <img class="absolute inset-0 h-full w-full object-cover" src="https://images.unsplash.com/photo-1496917756835-20cb06e75b4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80" alt="">
    </div>
  </div>"""
    },
    {
        "id": "auth-004",
        "title": "Sign In with Social",
        "description": "Sign in page including social providers.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
            </div>
          </div>
          <div class="mt-2">
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
           <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
        </div>
      </form>

      <div class="mt-10">
        <div class="relative">
          <div class="absolute inset-0 flex items-center" aria-hidden="true">
            <div class="w-full border-t border-gray-200"></div>
          </div>
          <div class="relative flex justify-center text-sm font-medium leading-6">
            <span class="bg-white px-6 text-gray-900">Or continue with</span>
          </div>
        </div>

        <div class="mt-6 grid grid-cols-2 gap-4">
          <a href="#" class="flex w-full items-center justify-center gap-3 rounded-md bg-[#1D9BF0] px-3 py-1.5 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#1D9BF0]">
            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
              <path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 013 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
            </svg>
            <span class="text-sm font-semibold leading-6">Twitter</span>
          </a>

          <a href="#" class="flex w-full items-center justify-center gap-3 rounded-md bg-[#24292F] px-3 py-1.5 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#24292F]">
            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
              <path fill-rule="evenodd" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z" clip-rule="evenodd" />
            </svg>
            <span class="text-sm font-semibold leading-6">GitHub</span>
          </a>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-005",
        "title": "Sign In with Image",
        "description": "Sign in with decorative image side.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
       <!-- Form content same as split usually -->
       <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
          <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Welcome back</h2>
        </div>
        <form class="space-y-6 mt-10">
             <div>
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                <div class="mt-2">
                  <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>
              <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Sign in</button>
              </div>
        </form>
       </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <img class="absolute inset-0 h-full w-full object-cover" src="https://images.unsplash.com/photo-1505904267569-f02eaeb45a4c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1908&q=80" alt="">
    </div>
  </div>"""
    },
    {
        "id": "auth-006",
        "title": "Simple Sign Up",
        "description": "Minimal registration form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Create your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Full Name</label>
          <div class="mt-2">
            <input id="name" name="name" type="text" autocomplete="name" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          <div class="mt-2">
            <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign up</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Already have an account?
        <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign in</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-007",
        "title": "Sign Up Card",
        "description": "Registration form in a card.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8 bg-gray-50">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Create an account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
      <div class="bg-white px-6 py-12 shadow sm:rounded-lg sm:px-12">
        <form class="space-y-6" action="#" method="POST">
           <div>
            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
            <div class="mt-2">
              <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
            </div>
          </div>
          <div>
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            <div class="mt-2">
              <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
            </div>
          </div>
          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign up</button>
          </div>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-008",
        "title": "Split Sign Up",
        "description": "Split screen registration.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-1">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
          <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Get started for free</h2>
        </div>
        <form class="space-y-6 mt-10">
             <div>
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                <div class="mt-2">
                  <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>
              <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Create account</button>
              </div>
        </form>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <img class="absolute inset-0 h-full w-full object-cover" src="https://images.unsplash.com/photo-1510915228340-29c85a43dcfe?ixlib=rb-1.2.1&auto=format&fit=crop&w=1908&q=80" alt="">
    </div>
  </div>"""
    },
    {
        "id": "auth-009",
        "title": "Forgot Password",
        "description": "Simple forgot password form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Reset your password</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Send reset link</button>
        </div>
      </form>
       <p class="mt-10 text-center text-sm text-gray-500">
        <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Back to sign in</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-010",
        "title": "Reset Password",
        "description": "New password entry form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Set new password</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="password" class="block text-sm font-medium leading-6 text-gray-900">New Password</label>
          <div class="mt-2">
            <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <label for="confirm-password" class="block text-sm font-medium leading-6 text-gray-900">Confirm Password</label>
          <div class="mt-2">
            <input id="confirm-password" name="confirm-password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Update password</button>
        </div>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_AUTHENTICATION_2 = [
    {
        "id": "auth-011",
        "title": "Verify Email",
        "description": "Email verification message.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-green-100">
         <svg class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Check your email</h2>
      <p class="mt-2 text-center text-sm text-gray-600">
         We sent a verification link to <span class="font-medium text-gray-900">user@example.com</span>.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <p class="text-center text-sm text-gray-500">
           Didn't receive the email? <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Click to resend</a>
        </p>
        <div class="mt-6">
           <a href="#" class="flex w-full justify-center text-sm font-medium text-gray-600 hover:text-gray-500">
              <span aria-hidden="true"> &larr;</span> Back to login
           </a>
        </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-012",
        "title": "Lock Screen",
        "description": "Screen to re-enter password.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User Avatar">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Welcome back, Tom</h2>
      <p class="mt-2 text-sm text-gray-500">Enter your password to access the admin.</p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
           <label for="password" class="sr-only">Password</label>
           <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Password">
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Unlock</button>
        </div>
      </form>
       <p class="mt-6 text-center text-sm text-gray-500">
        <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Sign in as a different user</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-013",
        "title": "2FA Input",
        "description": "Two-factor authentication input.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Two-Factor Authentication</h2>
      <p class="mt-2 text-center text-sm text-gray-600">
          We sent a code to your phone ending in **** 1234.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="code" class="block text-sm font-medium leading-6 text-gray-900">Security Code</label>
          <div class="mt-2 flex gap-2">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-lg sm:leading-6" maxlength="1">
          </div>
        </div>

        <div>
           <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Verify</button>
        </div>
      </form>
      <p class="mt-6 text-center text-sm text-gray-500">
         Resend code in <span class="font-semibold text-gray-900">00:30</span>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-014",
        "title": "Password Success",
        "description": "Password reset success message.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
       <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-indigo-100">
         <svg class="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Password reset successful</h2>
      <p class="mt-2 text-center text-sm text-gray-600">
          Your password has been successfully updated.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
         <a href="#" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Continue to sign in</a>
    </div>
  </div>"""
    },
    {
        "id": "auth-015",
        "title": "Sign In Dark",
        "description": "Dark mode sign in form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-white">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-white">Password</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-400 hover:text-indigo-300">Forgot password?</a>
            </div>
          </div>
          <div class="mt-2">
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Sign in</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-400">
        Not a member?
        <a href="#" class="font-semibold leading-6 text-indigo-400 hover:text-indigo-300">Start a 14-day free trial</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-016",
        "title": "Sign Up Dark",
        "description": "Dark mode registration form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">Create your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
         <div>
          <label for="email" class="block text-sm font-medium leading-6 text-white">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <label for="password" class="block text-sm font-medium leading-6 text-white">Password</label>
          <div class="mt-2">
            <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Sign up</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-400">
        Already have an account?
        <a href="#" class="font-semibold leading-6 text-indigo-400 hover:text-indigo-300">Sign in</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-017",
        "title": "Forgot Password Dark",
        "description": "Dark mode forgot password.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">Reset your password</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-white">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Send reset link</button>
        </div>
      </form>
       <p class="mt-10 text-center text-sm text-gray-400">
        <a href="#" class="font-semibold leading-6 text-indigo-400 hover:text-indigo-300">Back to sign in</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-018",
        "title": "Split Login Dark",
        "description": "Dark mode split screen login.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-1 bg-gray-900 text-white">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
          <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-white">Sign in to your account</h2>
        </div>

        <div class="mt-10">
          <div>
            <form action="#" method="POST" class="space-y-6">
              <div>
                <label for="email" class="block text-sm font-medium leading-6 text-white">Email address</label>
                <div class="mt-2">
                  <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
                </div>
              </div>

              <div>
                <label for="password" class="block text-sm font-medium leading-6 text-white">Password</label>
                <div class="mt-2">
                   <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
                </div>
              </div>
              <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Sign in</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <img class="absolute inset-0 h-full w-full object-cover opacity-80" src="https://images.unsplash.com/photo-1496917756835-20cb06e75b4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80" alt="">
    </div>
  </div>"""
    },
    {
        "id": "auth-019",
        "title": "Card Login Dark",
        "description": "Dark mode card based login.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-white">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
      <div class="bg-gray-800 px-6 py-12 shadow sm:rounded-lg sm:px-12 border border-white/10">
        <form class="space-y-6" action="#" method="POST">
          <div>
            <label for="email" class="block text-sm font-medium leading-6 text-white">Email address</label>
            <div class="mt-2">
              <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium leading-6 text-white">Password</label>
            <div class="mt-2">
               <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6">
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-white/10 bg-white/5 text-indigo-500 focus:ring-indigo-500 ring-offset-gray-900">
              <label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-300">Remember me</label>
            </div>

            <div class="text-sm leading-6">
              <a href="#" class="font-semibold text-indigo-400 hover:text-indigo-300">Forgot password?</a>
            </div>
          </div>

          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Sign in</button>
          </div>
        </form>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-020",
        "title": "2FA Dark",
        "description": "Dark mode 2FA input.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">Two-Factor Authentication</h2>
      <p class="mt-2 text-center text-sm text-gray-400">
          We sent a code to your phone ending in **** 1234.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
       <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="code" class="block text-sm font-medium leading-6 text-white">Security Code</label>
          <div class="mt-2 flex gap-2">
              <input type="text" class="block w-12 h-12 text-center rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-lg sm:leading-6" maxlength="1">
             <input type="text" class="block w-12 h-12 text-center rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-lg sm:leading-6" maxlength="1">
          </div>
        </div>

        <div>
           <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Verify</button>
        </div>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_AUTHENTICATION_3 = [
    {
        "id": "auth-021",
        "title": "Unlock Dark",
        "description": "Dark mode password prompt.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <img class="mx-auto h-24 w-24 rounded-full border-4 border-gray-800" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="User Avatar">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-white">Welcome back, Tom</h2>
      <p class="mt-2 text-sm text-gray-400">Enter your password to access the admin.</p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
           <label for="password" class="sr-only">Password</label>
           <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6" placeholder="Password">
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Unlock</button>
        </div>
      </form>
       <p class="mt-6 text-center text-sm text-gray-400">
        <a href="#" class="font-semibold text-indigo-400 hover:text-indigo-300">Sign in as a different user</a>
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-022",
        "title": "Verify Email Dark",
        "description": "Dark mode email verification.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-green-900/20">
         <svg class="h-6 w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-white">Check your email</h2>
      <p class="mt-2 text-center text-sm text-gray-400">
         We sent a verification link to <span class="font-medium text-white">user@example.com</span>.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <p class="text-center text-sm text-gray-400">
           Didn't receive the email? <a href="#" class="font-semibold text-indigo-400 hover:text-indigo-300">Click to resend</a>
        </p>
        <div class="mt-6">
           <a href="#" class="flex w-full justify-center text-sm font-medium text-gray-400 hover:text-gray-300">
              <span aria-hidden="true"> &larr;</span> Back to login
           </a>
        </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-023",
        "title": "Password Success Dark",
        "description": "Dark mode password reset success.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8 bg-gray-900 text-white">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
       <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-indigo-900/20">
         <svg class="h-6 w-6 text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-white">Password reset successful</h2>
      <p class="mt-2 text-center text-sm text-gray-400">
          Your password has been successfully updated.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
         <a href="#" class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Continue to sign in</a>
    </div>
  </div>"""
    },
    {
        "id": "auth-024",
        "title": "Sign In Top Logo",
        "description": "Sign in with logo above form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-20 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm border-t pt-8">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
           <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          <div class="mt-2">
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-025",
        "title": "Sign Up Top Logo",
        "description": "Sign up with logo above form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-20 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Create Account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm border-t pt-8">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
         <div>
          <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          <div class="mt-2">
            <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Register</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-026",
        "title": "Forgot Password Top Logo",
        "description": "Forgot password with logo above.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-20 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Recover Account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm border-t pt-8">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Send Code</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-027",
        "title": "Sign In Borderless",
        "description": "Very clean, minimal sign in.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-4xl font-light leading-9 tracking-tight text-gray-900">Sign In</h2>
      <p class="mt-2 text-center text-gray-500">Welcome back to the platform.</p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full border-0 border-b border-gray-300 py-2 text-gray-900 placeholder:text-gray-400 focus:border-indigo-600 focus:ring-0 sm:text-sm sm:leading-6" placeholder="Email Address">
        </div>

        <div>
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full border-0 border-b border-gray-300 py-2 text-gray-900 placeholder:text-gray-400 focus:border-indigo-600 focus:ring-0 sm:text-sm sm:leading-6" placeholder="Password">
        </div>

        <div class="pt-4">
          <button type="submit" class="flex w-full justify-center rounded-full bg-black px-3 py-3 text-sm font-bold leading-6 text-white shadow-sm hover:bg-gray-800 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black">Go</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-028",
        "title": "Sign In Illustration",
        "description": "Sign in page with custom illustration.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-screen bg-white">
    <div class="flex flex-1 flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
          <h2 class="mt-6 text-3xl font-extrabold text-gray-900">Sign in to your account</h2>
        </div>

        <div class="mt-8">
            <form action="#" method="POST" class="space-y-6">
               <div>
                <label for="email" class="block text-sm font-medium text-gray-700"> Email address </label>
                <div class="mt-1">
                  <input id="email" name="email" type="email" autocomplete="email" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>
              </div>

              <div>
                <label for="password" class="block text-sm font-medium text-gray-700"> Password </label>
                <div class="mt-1">
                  <input id="password" name="password" type="password" autocomplete="current-password" required class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>
              </div>

              <div>
                <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Sign in</button>
              </div>
            </form>
        </div>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block bg-gray-50">
       <div class="flex items-center justify-center h-full">
          <img src="https://tailwindui.com/img/component-images/project-app-screenshot.png" alt="App Illustration" class="max-w-[800px] shadow-2xl rounded-xl">
       </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-029",
        "title": "Sign In Illustration Dark",
        "description": "Dark mode sign in with illustration.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-screen bg-gray-900 text-white">
    <div class="flex flex-1 flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
          <h2 class="mt-6 text-3xl font-extrabold text-white">Sign in to your account</h2>
        </div>

        <div class="mt-8">
            <form action="#" method="POST" class="space-y-6">
               <div>
                <label for="email" class="block text-sm font-medium text-gray-300"> Email address </label>
                <div class="mt-1">
                  <input id="email" name="email" type="email" autocomplete="email" required class="appearance-none block w-full px-3 py-2 border border-gray-700 rounded-md shadow-sm placeholder-gray-500 bg-gray-800 text-white focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>
              </div>

              <div>
                <label for="password" class="block text-sm font-medium text-gray-300"> Password </label>
                <div class="mt-1">
                  <input id="password" name="password" type="password" autocomplete="current-password" required class="appearance-none block w-full px-3 py-2 border border-gray-700 rounded-md shadow-sm placeholder-gray-500 bg-gray-800 text-white focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>
              </div>

              <div>
                <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Sign in</button>
              </div>
            </form>
        </div>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block bg-gray-800">
       <div class="flex items-center justify-center h-full">
          <img src="https://tailwindui.com/img/component-images/dark-project-app-screenshot.png" alt="App Illustration" class="max-w-[800px] shadow-2xl rounded-xl border border-gray-700">
       </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-030",
        "title": "Simple 2FA",
        "description": "Minimal 2FA screen.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <h2 class="text-2xl font-bold leading-9 tracking-tight text-gray-900">Verify it's you</h2>
      <p class="mt-2 text-sm text-gray-500">Enter the code from your authenticator app.</p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <input type="text" class="block w-full text-center text-3xl tracking-[1em] rounded-md border-0 py-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="000000" maxlength="6">
        </div>
        <div>
           <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Verify Code</button>
        </div>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_AUTHENTICATION_4 = [
    {
        "id": "auth-031",
        "title": "Confirm Password",
        "description": "Confirm password before sensitive action.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Confirm Password</h2>
      <p class="mt-2 text-center text-sm text-gray-500">Please confirm your password to continue.</p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          <div class="mt-2">
            <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Confirm</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-032",
        "title": "Auth Error Message",
        "description": "Example of authentication error alert.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
       <div class="rounded-md bg-red-50 p-4 mb-8">
          <div class="flex">
             <div class="flex-shrink-0">
                <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                   <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clip-rule="evenodd" />
                </svg>
             </div>
             <div class="ml-3">
                <h3 class="text-sm font-medium text-red-800">Login failed</h3>
                <div class="mt-2 text-sm text-red-700">
                   <ul role="list" class="list-disc space-y-1 pl-5">
                      <li>Incorrect email or password.</li>
                   </ul>
                </div>
             </div>
          </div>
       </div>

      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" value="wrong@email.com">
          </div>
        </div>

        <div>
           <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
           <div class="mt-2">
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-033",
        "title": "Auth Success Message",
        "description": "Example of authentication success alert.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
     <div class="sm:mx-auto sm:w-full sm:max-w-sm">
       <div class="rounded-md bg-green-50 p-4 mb-8">
          <div class="flex">
             <div class="flex-shrink-0">
                <svg class="h-5 w-5 text-green-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                   <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
                </svg>
             </div>
             <div class="ml-3">
                <h3 class="text-sm font-medium text-green-800">Login Successful</h3>
                <div class="mt-2 text-sm text-green-700">
                   <p>Redirecting you to the dashboard...</p>
                </div>
             </div>
          </div>
       </div>

      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Please wait</h2>
    </div>
  </div>"""
    },
    {
        "id": "auth-034",
        "title": "Sign In with Disclaimer",
        "description": "Login form with legal text disclaimer.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
           <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
           <div class="mt-2">
            <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
        </div>
      </form>

      <p class="mt-10 text-center text-xs text-gray-500">
        By signing in, you agree to our <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Terms of Service</a> and <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Privacy Policy</a>.
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-035",
        "title": "Sign Up with Newsletter",
        "description": "Registration with newsletter opt-in.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Create your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
           <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Email">
        </div>
        <div>
           <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Password">
        </div>

        <div class="flex items-start">
            <div class="flex h-6 items-center">
              <input id="newsletter" name="newsletter" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
            </div>
            <div class="ml-3 text-sm leading-6">
              <label for="newsletter" class="font-medium text-gray-900">Subscribe to newsletter</label>
              <p class="text-gray-500">Get the latest news and updates.</p>
            </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign up</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-036",
        "title": "Social Auth Row",
        "description": "Login with row of social icons.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <h2 class="text-2xl font-bold leading-9 tracking-tight text-gray-900">Welcome Back</h2>
      <p class="mt-2 text-sm text-gray-500">Login to continue</p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div class="grid grid-cols-3 gap-3">
           <button type="button" class="flex w-full items-center justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:ring-transparent">
              <svg class="h-5 w-5" aria-hidden="true" viewBox="0 0 24 24"><path d="M12.0003 20.45c-4.6667 0-8.45-3.7833-8.45-8.45 0-4.6667 3.7833-8.45 8.45-8.45 4.6667 0 8.45 3.7833 8.45 8.45 0 4.6667-3.7833 8.45-8.45 8.45Z" fill="#181717"/></svg>
           </button>
           <button type="button" class="flex w-full items-center justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:ring-transparent">
              <svg class="h-5 w-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 013 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
           </button>
           <button type="button" class="flex w-full items-center justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:ring-transparent">
              <svg class="h-5 w-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z" clip-rule="evenodd" /></svg>
           </button>
        </div>
        <div class="relative mt-8">
            <div class="absolute inset-0 flex items-center" aria-hidden="true">
              <div class="w-full border-t border-gray-200"></div>
            </div>
            <div class="relative flex justify-center text-sm font-medium leading-6">
              <span class="bg-white px-6 text-gray-900">Or continue with email</span>
            </div>
        </div>
        <form class="space-y-6 mt-8" action="#" method="POST">
             <!-- Email input ... -->
             <div>
                <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Email address">
             </div>
             <div>
               <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Sign in</button>
             </div>
        </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-037",
        "title": "Social Auth Grid",
        "description": "Grid of social login options.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <h2 class="text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign In</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div class="grid grid-cols-2 gap-4">
           <button class="flex items-center justify-center gap-2 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Twitter</button>
           <button class="flex items-center justify-center gap-2 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">GitHub</button>
           <button class="flex items-center justify-center gap-2 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Google</button>
           <button class="flex items-center justify-center gap-2 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Facebook</button>
        </div>
         <p class="mt-6 text-center text-sm text-gray-500">
           Or sign in with <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">email</a>.
        </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-038",
        "title": "Anonymous Login Info",
        "description": "Info card about anonymous login.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <div class="bg-blue-50 border-l-4 border-blue-400 p-4 mb-8">
         <div class="flex">
            <div class="flex-shrink-0">
               <svg class="h-5 w-5 text-blue-400" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
               </svg>
            </div>
            <div class="ml-3">
               <p class="text-sm text-blue-700">
                  You are logging in anonymously. Your data will not be synced unless you create an account later.
               </p>
            </div>
         </div>
      </div>
      <button class="flex w-full justify-center rounded-md bg-gray-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-gray-500">Continue Anonymously</button>
    </div>
  </div>"""
    },
    {
        "id": "auth-039",
        "title": "Guest Checkout",
        "description": "Guest checkout option.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
       <h2 class="text-2xl font-bold text-gray-900">Checkout</h2>
    </div>
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm space-y-4">
        <button class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-3 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">Sign In to Checkout</button>
        <div class="relative">
            <div class="absolute inset-0 flex items-center" aria-hidden="true">
              <div class="w-full border-t border-gray-200"></div>
            </div>
            <div class="relative flex justify-center text-sm font-medium leading-6">
              <span class="bg-white px-2 text-gray-500">or</span>
            </div>
        </div>
        <button class="flex w-full justify-center rounded-md bg-white px-3 py-3 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Continue as Guest</button>
    </div>
  </div>"""
    },
    {
        "id": "auth-040",
        "title": "Password Strength Meter",
        "description": "Password input with strength indicator.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="text-center text-2xl font-bold text-gray-900">Set Password</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6">
        <div>
           <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
           <div class="mt-2">
            <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
          <div class="mt-2 h-1 w-full bg-gray-200 rounded-full overflow-hidden">
             <div class="h-full bg-yellow-500 w-1/3"></div>
          </div>
          <p class="mt-1 text-xs text-yellow-600">Weak password</p>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Save</button>
        </div>
      </form>
    </div>
  </div>"""
    }
]
TEMPLATES_AUTHENTICATION_5 = [
    {
        "id": "auth-041",
        "title": "Multi Step Wizard",
        "description": "Step-based registration form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Setup Account</h2>
      <div class="mt-4 flex justify-between items-center text-sm font-medium text-gray-500">
         <span class="text-indigo-600">Step 1</span>
         <span>Step 2</span>
         <span>Step 3</span>
      </div>
      <div class="mt-2 h-1 w-full bg-gray-200 rounded-full overflow-hidden">
         <div class="h-full bg-indigo-600 w-1/3"></div>
      </div>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6">
        <div>
           <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
           <div class="mt-2">
            <input id="username" name="username" type="text" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>

        <div class="flex justify-end">
          <button type="button" class="rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Next</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-042",
        "title": "Terms Agreement Modal",
        "description": "Modal prompt to agree to terms.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
          <div>
            <div class="mt-3 text-center sm:mt-5">
              <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Updated Terms of Service</h3>
              <div class="mt-2">
                <p class="text-sm text-gray-500">
                   Please review and accept our updated terms of service to continue using the application.
                </p>
                <div class="h-32 overflow-y-auto border p-2 mt-4 text-xs text-gray-500 text-left bg-gray-50">
                   Lorem ipsum dolor sit amet... (Legal Text)
                </div>
              </div>
            </div>
          </div>
          <div class="mt-5 sm:mt-6 sm:grid sm:grid-flow-row-dense sm:grid-cols-2 sm:gap-3">
            <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:col-start-2">Accept</button>
            <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:col-start-1 sm:mt-0">Decline</button>
          </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-043",
        "title": "Privacy Policy Modal",
        "description": "Simple privacy policy view.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="relative z-10" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
           <div class="px-4 py-5 sm:px-6">
              <h3 class="text-base font-semibold leading-6 text-gray-900">Privacy Policy</h3>
           </div>
           <div class="px-4 py-5 sm:p-6 text-sm text-gray-500">
              <p>We respect your privacy. Here is how we handle your data...</p>
           </div>
           <div class="px-4 py-4 sm:flex sm:flex-row-reverse sm:px-6">
               <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 sm:w-auto">Close</button>
           </div>
        </div>
      </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-044",
        "title": "Account Deleted",
        "description": "Confirmation screen after account deletion.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
       <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-gray-100">
         <svg class="h-6 w-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Account Deleted</h2>
      <p class="mt-2 text-center text-sm text-gray-600">
          We're sorry to see you go. Your account has been permanently deleted.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
         <a href="#" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Return to Home</a>
    </div>
  </div>"""
    },
    {
        "id": "auth-045",
        "title": "Account Suspended",
        "description": "Notice for suspended accounts.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
       <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-red-100">
         <svg class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Account Suspended</h2>
      <p class="mt-2 text-center text-sm text-gray-600">
          Your account has been suspended for violating our terms of service.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
         <a href="#" class="flex w-full justify-center rounded-md bg-gray-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-gray-500">Contact Support</a>
    </div>
  </div>"""
    },
    {
        "id": "auth-046",
        "title": "Maintenance Mode Auth",
        "description": "Login disabled due to maintenance.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
       <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-yellow-100">
         <svg class="h-6 w-6 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
      </div>
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Maintenance Mode</h2>
      <p class="mt-2 text-center text-sm text-gray-600">
          We are currently undergoing scheduled maintenance. Login is temporarily disabled.
      </p>
    </div>
  </div>"""
    },
    {
        "id": "auth-047",
        "title": "Coming Soon Auth",
        "description": "Pre-launch signup form.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <h2 class="text-3xl font-bold leading-9 tracking-tight text-gray-900">Coming Soon</h2>
      <p class="mt-2 text-gray-500">
          Be the first to know when we launch.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
           <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Enter your email">
        </div>
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Notify Me</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-048",
        "title": "Beta Access Request",
        "description": "Request access to beta.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm text-center">
      <h2 class="text-2xl font-bold text-gray-900">Request Beta Access</h2>
       <p class="mt-2 text-sm text-gray-500">
          Join our waiting list for early access.
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
         <div>
           <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
           <div class="mt-2">
            <input id="name" name="name" type="text" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
           <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
           <div class="mt-2">
            <input id="email" name="email" type="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Request Access</button>
        </div>
      </form>
    </div>
  </div>"""
    },
    {
        "id": "auth-049",
        "title": "Login with Side Note",
        "description": "Login form with side informational note.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-1">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in</h2>
        <form class="space-y-6 mt-10">
             <div>
                <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Email">
             </div>
             <div>
                <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Password">
             </div>
             <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Sign in</button>
        </form>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block bg-indigo-900 text-white p-12 flex items-center">
       <div>
          <h3 class="text-2xl font-bold mb-4">Did you know?</h3>
          <p class="text-indigo-200">
             Our platform processes over 1 million requests per second. Join us and scale your business today.
          </p>
       </div>
    </div>
  </div>"""
    },
    {
        "id": "auth-050",
        "title": "Login with Testimonial",
        "description": "Login form with customer testimonial.",
        "dir": "templates/11-authentication",
        "content": """
  <div class="flex min-h-full flex-1">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in</h2>
        <form class="space-y-6 mt-10">
             <div>
                <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Email">
             </div>
             <div>
                <input id="password" name="password" type="password" required class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Password">
             </div>
             <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500">Sign in</button>
        </form>
      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block relative">
      <img class="absolute inset-0 h-full w-full object-cover brightness-50" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1908&q=80" alt="">
      <div class="absolute bottom-0 left-0 right-0 p-12 text-white">
          <blockquote class="text-xl font-medium italic mb-4">
             "The best authentication library we've ever used. Simple, secure, and fast."
          </blockquote>
          <p class="font-bold">Sarah Connor</p>
          <p class="text-gray-300 text-sm">CTO, Skynet Inc.</p>
      </div>
    </div>
  </div>"""
    }
]
TEMPLATES_AUTHENTICATION = TEMPLATES_AUTHENTICATION_1 + TEMPLATES_AUTHENTICATION_2 + TEMPLATES_AUTHENTICATION_3 + TEMPLATES_AUTHENTICATION_4 + TEMPLATES_AUTHENTICATION_5

# Combine all templates
TEMPLATES = TEMPLATES_AUTHENTICATION



def generate_and_push():
    print(f"Generating {len(TEMPLATES)} templates...")
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
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', "feat: implement batch 9 authentication templates"], check=True)
        subprocess.run(['git', 'push', 'origin', 'dev'], check=True)
        print("Pushed all changes successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")

if __name__ == "__main__":
    generate_and_push()
