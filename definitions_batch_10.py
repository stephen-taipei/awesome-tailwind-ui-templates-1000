
TEMPLATES_DASHBOARD = [
    {
        "id": "dashboard-901",
        "title": "Admin Sidebar Dark",
        "description": "Dashboard layout with a dark sidebar.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="flex h-screen bg-gray-100">
        <!-- Sidebar -->
        <div class="w-64 bg-gray-900 text-white flex flex-col">
            <div class="h-16 flex items-center justify-center font-bold text-xl border-b border-gray-800">AdminPanel</div>
            <nav class="flex-1 px-4 py-6 space-y-2">
                <a href="#" class="flex items-center px-4 py-3 bg-gray-800 rounded-lg text-white">
                    <svg class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>                    Dashboard
                </a>
                <a href="#" class="flex items-center px-4 py-3 text-gray-400 hover:bg-gray-800 hover:text-white rounded-lg transition">
                    <svg class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                    Users
                </a>
                <a href="#" class="flex items-center px-4 py-3 text-gray-400 hover:bg-gray-800 hover:text-white rounded-lg transition">
                    <svg class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"/></svg>
                    Analytics
                </a>
                 <a href="#" class="flex items-center px-4 py-3 text-gray-400 hover:bg-gray-800 hover:text-white rounded-lg transition">
                    <svg class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                    Settings
                </a>
            </nav>
            <div class="p-4 border-t border-gray-800">
                <a href="#" class="flex items-center text-gray-400 hover:text-white">
                    <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="h-8 w-8 rounded-full mr-3" alt="">
                    <span>Logged in as Admin</span>
                </a>
            </div>
        </div>

        <!-- Main Content -->
        <main class="flex-1 p-8 overflow-y-auto">
            <header class="flex justify-between items-center mb-8">
                <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
                <button class="bg-blue-600 text-white px-4 py-2 rounded-lg font-bold">New Report</button>
            </header>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 rounded-xl shadow-sm">
                    <div class="text-gray-500 text-sm font-bold uppercase mb-2">Total Revenue</div>
                    <div class="text-3xl font-bold text-gray-900">$45,231.89</div>
                    <div class="text-green-500 text-sm mt-2">↑ 20.1% from last month</div>
                </div>
                 <div class="bg-white p-6 rounded-xl shadow-sm">
                    <div class="text-gray-500 text-sm font-bold uppercase mb-2">Active Users</div>
                    <div class="text-3xl font-bold text-gray-900">2,345</div>
                    <div class="text-green-500 text-sm mt-2">↑ 5.4% from last month</div>
                </div>
                 <div class="bg-white p-6 rounded-xl shadow-sm">
                    <div class="text-gray-500 text-sm font-bold uppercase mb-2">Bounce Rate</div>
                    <div class="text-3xl font-bold text-gray-900">24.57%</div>
                    <div class="text-red-500 text-sm mt-2">↓ 2.3% from last month</div>
                </div>
            </div>

            <div class="bg-white rounded-xl shadow-sm p-6">
                <h3 class="font-bold text-gray-900 mb-4">Recent Activity</h3>
                 <ul class="divide-y divide-gray-100">
                     <li class="py-4 flex justify-between">
                         <div class="flex items-center">
                             <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 mr-4">N</div>
                             <div>
                                 <p class="font-bold text-gray-900">New user registered</p>
                                 <p class="text-sm text-gray-500">5 minutes ago</p>
                             </div>
                         </div>
                         <button class="text-blue-600 font-bold text-sm">View</button>
                     </li>
                     <li class="py-4 flex justify-between">
                         <div class="flex items-center">
                             <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600 mr-4">$</div>
                             <div>
                                 <p class="font-bold text-gray-900">Payment received</p>
                                 <p class="text-sm text-gray-500">2 hours ago</p>
                             </div>
                         </div>
                         <button class="text-blue-600 font-bold text-sm">View</button>
                     </li>
                 </ul>
            </div>
        </main>
    </div>"""
    },
    {
        "id": "dashboard-902",
        "title": "Stats Grid",
        "description": "Grid of statistics cards for dashboard.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="bg-gray-50 p-8 min-h-screen">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Overview</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="bg-white p-6 rounded-lg shadow border border-gray-100">
                <div class="flex justify-between items-start mb-4">
                    <div>
                        <p class="text-sm font-medium text-gray-500">Total Subscribers</p>
                        <h3 class="text-3xl font-bold text-gray-900 mt-1">71,897</h3>
                    </div>
                    <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-1 rounded-full">+12%</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-1.5">
                    <div class="bg-green-500 h-1.5 rounded-full" style="width: 70%"></div>
                </div>
            </div>
             <div class="bg-white p-6 rounded-lg shadow border border-gray-100">
                <div class="flex justify-between items-start mb-4">
                    <div>
                        <p class="text-sm font-medium text-gray-500">Avg. Open Rate</p>
                        <h3 class="text-3xl font-bold text-gray-900 mt-1">58.16%</h3>
                    </div>
                    <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-1 rounded-full">+2.1%</span>
                </div>
                 <div class="w-full bg-gray-200 rounded-full h-1.5">
                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: 58%"></div>
                </div>
            </div>
             <div class="bg-white p-6 rounded-lg shadow border border-gray-100">
                <div class="flex justify-between items-start mb-4">
                    <div>
                        <p class="text-sm font-medium text-gray-500">Avg. Click Rate</p>
                        <h3 class="text-3xl font-bold text-gray-900 mt-1">24.57%</h3>
                    </div>
                     <span class="bg-red-100 text-red-800 text-xs font-bold px-2 py-1 rounded-full">-3.2%</span>
                </div>
                 <div class="w-full bg-gray-200 rounded-full h-1.5">
                    <div class="bg-yellow-500 h-1.5 rounded-full" style="width: 24%"></div>
                </div>
            </div>
             <div class="bg-white p-6 rounded-lg shadow border border-gray-100">
                <div class="flex justify-between items-start mb-4">
                    <div>
                        <p class="text-sm font-medium text-gray-500">Total Sales</p>
                        <h3 class="text-3xl font-bold text-gray-900 mt-1">$24,567</h3>
                    </div>
                     <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-1 rounded-full">+45%</span>
                </div>
                 <div class="w-full bg-gray-200 rounded-full h-1.5">
                    <div class="bg-purple-500 h-1.5 rounded-full" style="width: 85%"></div>
                </div>
            </div>
        </div>
    </div>"""
    },
    {
        "id": "dashboard-903",
        "title": "Table with Action Buttons",
        "description": "Data table with edit/delete actions.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="bg-white p-8 rounded-lg shadow-sm border border-gray-200">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-gray-900">User Management</h2>
            <div class="relative">
                <input type="text" placeholder="Search users..." class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-sm">
                <svg class="w-5 h-5 text-gray-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>
        </div>

        <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                        <th scope="col" class="relative px-6 py-3"><span class="sr-only">Edit</span></th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <div class="flex items-center">
                                <div class="flex-shrink-0 h-10 w-10">
                                    <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
                                </div>
                                <div class="ml-4">
                                    <div class="text-sm font-medium text-gray-900">Jane Cooper</div>
                                    <div class="text-sm text-gray-500">jane.cooper@example.com</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <div class="text-sm text-gray-900">Regional Paradigm Technician</div>
                            <div class="text-sm text-gray-500">Optimization</div>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Active</span>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Admin</td>
                        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                            <a href="#" class="text-indigo-600 hover:text-indigo-900 mr-4">Edit</a>
                            <a href="#" class="text-red-600 hover:text-red-900">Delete</a>
                        </td>
                    </tr>
                     <tr>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <div class="flex items-center">
                                <div class="flex-shrink-0 h-10 w-10">
                                    <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
                                </div>
                                <div class="ml-4">
                                    <div class="text-sm font-medium text-gray-900">Cody Fisher</div>
                                    <div class="text-sm text-gray-500">cody.fisher@example.com</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <div class="text-sm text-gray-900">Product Directives Officer</div>
                            <div class="text-sm text-gray-500">Intranet</div>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Active</span>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Owner</td>
                        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                            <a href="#" class="text-indigo-600 hover:text-indigo-900 mr-4">Edit</a>
                             <a href="#" class="text-red-600 hover:text-red-900">Delete</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="mt-4 flex justify-between items-center sm:hidden">
            <a href="#" class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Previous</a>
            <a href="#" class="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Next</a>
        </div>
        <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between mt-4">
             <div>
                <p class="text-sm text-gray-700">Showing <span class="font-medium">1</span> to <span class="font-medium">10</span> of <span class="font-medium">97</span> results</p>
             </div>
             <div>
                <nav class="isolate inline-flex -space-x-px rounded-md shadow-sm" aria-label="Pagination">
                    <a href="#" class="relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"><span class="sr-only">Previous</span><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.5-4.25a.75.75 0 010-1.08l4.5-4.25a.75.75 0 011.06.02z" clip-rule="evenodd" /></svg></a>
                    <a href="#" aria-current="page" class="relative z-10 inline-flex items-center bg-indigo-600 px-4 py-2 text-sm font-semibold text-white focus:z-20 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">1</a>
                    <a href="#" class="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0">2</a>
                    <a href="#" class="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0">3</a>
                    <a href="#" class="relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"><span class="sr-only">Next</span><svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z" clip-rule="evenodd" /></svg></a>
                </nav>
             </div>
        </div>
    </div>"""
    }
]

TEMPLATES_BATCH_10 = []

TEMPLATES_DASHBOARD_2 = [
    {
        "id": "dashboard-904",
        "title": "Kanban Board",
        "description": "Drag and drop style kanban board.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="bg-gray-100 min-h-screen p-8 overflow-x-auto">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Project Implementation</h2>
        <div class="flex gap-6 items-start">
            <!-- Column 1 -->
            <div class="w-80 flex-shrink-0">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-bold text-gray-700">To Do</h3>
                    <span class="bg-gray-200 text-gray-700 px-2 py-1 rounded-full text-xs font-bold">3</span>
                </div>
                <div class="space-y-3">
                    <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition">
                        <span class="bg-red-100 text-red-800 text-xs px-2 py-1 rounded font-bold mb-2 inline-block">Bug</span>
                        <p class="font-medium text-gray-900 mb-2">Fix navigation on mobile</p>
                        <div class="flex items-center justify-between mt-3">
                            <img class="w-6 h-6 rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                            <span class="text-gray-400 text-xs">Today</span>
                        </div>
                    </div>
                     <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition">
                        <span class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded font-bold mb-2 inline-block">Design</span>
                        <p class="font-medium text-gray-900 mb-2">Create new marketing assets</p>
                        <div class="flex items-center justify-between mt-3">
                            <img class="w-6 h-6 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                            <span class="text-gray-400 text-xs">Tomorrow</span>
                        </div>
                    </div>
                     <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition">
                        <span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded font-bold mb-2 inline-block">Feature</span>
                        <p class="font-medium text-gray-900 mb-2">Add dark mode toggle</p>
                        <div class="flex items-center justify-between mt-3">
                            <div class="flex -space-x-2">
                                <img class="w-6 h-6 rounded-full border border-white" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                                <img class="w-6 h-6 rounded-full border border-white" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                            </div>
                            <span class="text-gray-400 text-xs">Next Week</span>
                        </div>
                    </div>
                </div>
                <button class="mt-3 w-full py-2 border-2 border-dashed border-gray-300 rounded-lg text-gray-500 hover:border-gray-400 hover:text-gray-600 font-medium transition">+ Add Task</button>
            </div>

             <!-- Column 2 -->
            <div class="w-80 flex-shrink-0">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-bold text-gray-700">In Progress</h3>
                    <span class="bg-gray-200 text-gray-700 px-2 py-1 rounded-full text-xs font-bold">1</span>
                </div>
                <div class="space-y-3">
                    <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 cursor-move hover:shadow-md transition">
                        <span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded font-bold mb-2 inline-block">Feature</span>
                        <p class="font-medium text-gray-900 mb-2">Implement payment gateway</p>
                         <div class="w-full bg-gray-200 rounded-full h-1.5 mb-3 mt-2">
                            <div class="bg-green-500 h-1.5 rounded-full" style="width: 45%"></div>
                        </div>
                        <div class="flex items-center justify-between">
                            <img class="w-6 h-6 rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                            <span class="text-orange-500 text-xs font-bold">Due Today</span>
                        </div>
                    </div>
                </div>
            </div>

             <!-- Column 3 -->
            <div class="w-80 flex-shrink-0">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-bold text-gray-700">Done</h3>
                    <span class="bg-gray-200 text-gray-700 px-2 py-1 rounded-full text-xs font-bold">2</span>
                </div>
                 <div class="space-y-3">
                    <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 opacity-75">
                         <div class="flex items-center justify-between mb-2">
                            <span class="bg-purple-100 text-purple-800 text-xs px-2 py-1 rounded font-bold">Refactor</span>
                            <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <p class="font-medium text-gray-900 line-through text-gray-500">Update dependencies</p>
                    </div>
                     <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 opacity-75">
                         <div class="flex items-center justify-between mb-2">
                            <span class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded font-bold">Design</span>
                            <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <p class="font-medium text-gray-900 line-through text-gray-500">Logo redesign</p>
                    </div>
                </div>
            </div>
        </div>
    </div>"""
    },
    {
        "id": "dashboard-905",
        "title": "Profile Settings",
        "description": "User profile editing form.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="max-w-4xl mx-auto py-10 px-4 sm:px-6 lg:px-8">
        <h1 class="text-2xl font-bold text-gray-900 mb-8">Account Settings</h1>

        <div class="bg-white shadow rounded-lg overflow-hidden">
            <div class="p-6 border-b border-gray-200">
                <h2 class="text-lg font-medium text-gray-900">Personal Information</h2>
                <p class="mt-1 text-sm text-gray-500">Update your photo and personal details.</p>
            </div>
            <div class="p-6 space-y-6">
                <!-- Photo -->
                <div class="flex items-center">
                    <img class="h-16 w-16 rounded-full object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <div class="ml-4">
                        <button class="bg-white border border-gray-300 text-gray-700 font-medium py-2 px-4 rounded-md hover:bg-gray-50 text-sm">Change</button>
                        <button class="ml-2 text-red-600 font-medium text-sm hover:text-red-800">Remove</button>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">First Name</label>
                        <input type="text" value="Tom" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm h-10 px-3 border">
                    </div>
                     <div>
                        <label class="block text-sm font-medium text-gray-700">Last Name</label>
                        <input type="text" value="Cook" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm h-10 px-3 border">
                    </div>
                     <div class="md:col-span-2">
                        <label class="block text-sm font-medium text-gray-700">Email Address</label>
                        <input type="email" value="tom.cook@example.com" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm h-10 px-3 border">
                    </div>
                      <div class="md:col-span-2">
                        <label class="block text-sm font-medium text-gray-700">Bio</label>
                        <textarea rows="3" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 border">Product Director. Tech enthusiast. Coffee lover.</textarea>
                    </div>
                </div>
            </div>
            <div class="bg-gray-50 px-6 py-4 flex justify-end">
                <button class="bg-white border border-gray-300 text-gray-700 font-medium py-2 px-4 rounded-md hover:bg-gray-50 text-sm mr-2">Cancel</button>
                <button class="bg-blue-600 text-white font-medium py-2 px-4 rounded-md hover:bg-blue-700 text-sm">Save Changes</button>
            </div>
        </div>

         <div class="bg-white shadow rounded-lg overflow-hidden mt-8">
            <div class="p-6 border-b border-gray-200">
                <h2 class="text-lg font-medium text-gray-900">Notifications</h2>
                <p class="mt-1 text-sm text-gray-500">Manage how we communicate with you.</p>
            </div>
            <div class="p-6 space-y-4">
               <div class="flex items-start">
                   <div class="flex items-center h-5">
                       <input type="checkbox" checked class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300 rounded">
                   </div>
                   <div class="ml-3 text-sm">
                       <label class="font-medium text-gray-700">Email Comments</label>
                       <p class="text-gray-500">Get notified when someone posts a comment on your article.</p>
                   </div>
               </div>
                <div class="flex items-start">
                   <div class="flex items-center h-5">
                       <input type="checkbox" class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300 rounded">
                   </div>
                   <div class="ml-3 text-sm">
                       <label class="font-medium text-gray-700">Product Updates</label>
                       <p class="text-gray-500">Receive weekly updates about new features.</p>
                   </div>
               </div>
            </div>
             <div class="bg-gray-50 px-6 py-4 flex justify-end">
                <button class="bg-blue-600 text-white font-medium py-2 px-4 rounded-md hover:bg-blue-700 text-sm">Save Preferences</button>
            </div>
        </div>
    </div>"""
    },
    {
        "id": "dashboard-906",
        "title": "Analytics Chart",
        "description": "Visual chart representation (mockup).",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="bg-white p-6 rounded-xl shadow border border-gray-100 max-w-4xl mx-auto mt-10">
        <div class="flex justify-between items-center mb-6">
            <div>
                <h3 class="text-lg font-bold text-gray-900">Traffic Overview</h3>
                <p class="text-sm text-gray-500">Sep 1 - Sep 30</p>
            </div>
            <select class="border-gray-300 rounded-lg text-sm focus:ring-blue-500 focus:border-blue-500">
                <option>Last 30 Days</option>
                <option>Last 7 Days</option>
                <option>Last Year</option>
            </select>
        </div>

        <!-- Chart Area Placeholder -->
        <div class="relative h-64 w-full bg-gray-50 rounded-lg border border-gray-200 flex items-end justify-between px-4 pb-4 gap-2">
            <!-- Grid Lines -->
            <div class="absolute inset-0 flex flex-col justify-between p-4 pointer-events-none opacity-20">
                <div class="border-t border-gray-500 w-full"></div>
                <div class="border-t border-gray-500 w-full"></div>
                <div class="border-t border-gray-500 w-full"></div>
                <div class="border-t border-gray-500 w-full"></div>
                <div class="border-t border-gray-500 w-full"></div>
            </div>

            <!-- Bars -->
            <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[40%] relative group">
                <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">400</div>
            </div>
             <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[60%] relative group">
                  <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">600</div>
             </div>
             <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[30%] relative group">
                  <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">300</div>
             </div>
             <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[75%] relative group">
                  <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">750</div>
             </div>
             <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[50%] relative group">
                  <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">500</div>
             </div>
             <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[85%] relative group">
                  <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">850</div>
             </div>
              <div class="w-full bg-blue-500 hover:bg-blue-600 transition rounded-t-sm h-[65%] relative group">
                  <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition">650</div>
             </div>
        </div>

        <div class="flex justify-between text-xs text-gray-500 mt-4 px-2">
            <span>Mon</span>
            <span>Tue</span>
            <span>Wed</span>
            <span>Thu</span>
            <span>Fri</span>
            <span>Sat</span>
            <span>Sun</span>
        </div>
    </div>"""
    },
    {
        "id": "dashboard-907",
        "title": "Notifications List",
        "description": "Dropdown or list of notifications.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="max-w-md mx-auto mt-10 bg-white rounded-lg shadow-lg border border-gray-200 overflow-hidden">
        <div class="px-4 py-3 border-b border-gray-100 flex justify-between items-center bg-gray-50">
            <h3 class="font-bold text-gray-900">Notifications</h3>
            <button class="text-xs text-blue-600 font-semibold hover:text-blue-800">Mark all as read</button>
        </div>
        <div class="divide-y divide-gray-100 max-h-96 overflow-y-auto">
            <a href="#" class="flex p-4 hover:bg-blue-50 transition bg-blue-50/50">
                <div class="flex-shrink-0 mr-4">
                    <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                </div>
                <div class="flex-1">
                    <p class="text-sm font-medium text-gray-900">Leslie Alexander <span class="text-gray-500 font-normal">commented on</span> Project Alpha</p>
                    <p class="text-xs text-gray-400 mt-1">10 minutes ago</p>
                </div>
                <div class="h-2 w-2 bg-blue-600 rounded-full self-center ml-2"></div>
            </a>

            <a href="#" class="flex p-4 hover:bg-gray-50 transition">
                <div class="flex-shrink-0 mr-4">
                     <span class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center text-green-600">
                         <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                     </span>
                </div>
                <div class="flex-1">
                    <p class="text-sm font-medium text-gray-900">System Update <span class="text-gray-500 font-normal">completed successfully</span></p>
                    <p class="text-xs text-gray-400 mt-1">2 hours ago</p>
                </div>
            </a>

            <a href="#" class="flex p-4 hover:bg-gray-50 transition">
                <div class="flex-shrink-0 mr-4">
                    <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                </div>
                <div class="flex-1">
                     <p class="text-sm font-medium text-gray-900">Michael Foster <span class="text-gray-500 font-normal">invited you to</span> Marketing Team</p>
                    <p class="text-xs text-gray-400 mt-1">Yesterday</p>
                </div>
            </a>
             <a href="#" class="flex p-4 hover:bg-gray-50 transition">
                <div class="flex-shrink-0 mr-4">
                     <span class="h-10 w-10 rounded-full bg-yellow-100 flex items-center justify-center text-yellow-600">
                         <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                     </span>
                </div>
                <div class="flex-1">
                    <p class="text-sm font-medium text-gray-900">Storage Alert <span class="text-gray-500 font-normal">80% capacity reached</span></p>
                    <p class="text-xs text-gray-400 mt-1">Nov 23</p>
                </div>
            </a>
        </div>
        <a href="#" class="block bg-gray-50 text-center py-3 text-sm font-medium text-gray-600 hover:text-gray-900 border-t border-gray-100">View all notifications</a>
    </div>"""
    },
    {
        "id": "dashboard-908",
        "title": "Search Result Item",
        "description": "Dashboard global search result items.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="max-w-2xl mx-auto py-10">
        <h2 class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-4">Results for "project"</h2>
        <ul class="bg-white rounded-lg shadow border border-gray-200 divide-y divide-gray-100">
            <li class="p-4 hover:bg-gray-50 transition cursor-pointer group">
                <div class="flex items-center">
                    <div class="h-10 w-10 rounded bg-blue-100 flex items-center justify-center text-blue-600 mr-4 group-hover:bg-blue-200 transition">
                         <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/></svg>
                    </div>
                    <div>
                        <h4 class="text-md font-bold text-gray-900 group-hover:text-blue-600 transition">Project Phoenix</h4>
                        <p class="text-sm text-gray-500">/marketing/campaigns/q4</p>
                    </div>
                     <span class="ml-auto text-xs text-gray-400 border border-gray-200 rounded px-2 py-1">Folder</span>
                </div>
            </li>
             <li class="p-4 hover:bg-gray-50 transition cursor-pointer group">
                <div class="flex items-center">
                    <div class="h-10 w-10 rounded bg-purple-100 flex items-center justify-center text-purple-600 mr-4 group-hover:bg-purple-200 transition">
                         <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <div>
                        <h4 class="text-md font-bold text-gray-900 group-hover:text-blue-600 transition">Project Specs v2.pdf</h4>
                        <p class="text-sm text-gray-500">Updated by Sarah 2 days ago</p>
                    </div>
                    <span class="ml-auto text-xs text-gray-400 border border-gray-200 rounded px-2 py-1">File</span>
                </div>
            </li>
             <li class="p-4 hover:bg-gray-50 transition cursor-pointer group">
                <div class="flex items-center">
                    <div class="h-10 w-10 rounded-full bg-gray-200 flex-shrink-0 mr-4 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    </div>
                    <div>
                        <h4 class="text-md font-bold text-gray-900 group-hover:text-blue-600 transition">Project Manager</h4>
                        <p class="text-sm text-gray-500">Job Title • Engineering</p>
                    </div>
                     <span class="ml-auto text-xs text-gray-400 border border-gray-200 rounded px-2 py-1">User</span>
                </div>
            </li>
        </ul>
    </div>"""
    },
    {
        "id": "dashboard-909",
        "title": "Invoice View",
        "description": "Invoice details layout.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="bg-gray-50 min-h-screen py-10 px-4">
        <div class="max-w-3xl mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
            <div class="p-8 flex flex-col md:flex-row justify-between items-start">
                <div>
                    <h1 class="text-4xl font-bold text-gray-900 tracking-tight">INVOICE</h1>
                    <p class="text-gray-500 mt-1">#INV-2024-001</p>
                </div>
                <div class="text-right mt-4 md:mt-0">
                    <h2 class="text-lg font-bold text-gray-900">Acme Inc.</h2>
                    <p class="text-gray-500 text-sm">123 Business St.<br>San Francisco, CA 94107</p>
                </div>
            </div>

            <div class="px-8 py-4 border-t border-b border-gray-100 flex flex-col md:flex-row justify-between">
                <div class="mb-4 md:mb-0">
                    <p class="text-sm text-gray-500 uppercase font-bold text-xs mb-1">Bill To</p>
                    <h3 class="font-bold text-gray-900">John Doe</h3>
                    <p class="text-sm text-gray-500">john.doe@example.com<br>555 Main St, Cityville</p>
                </div>
                 <div class="text-right">
                     <p class="text-sm text-gray-500 uppercase font-bold text-xs mb-1">Dates</p>
                    <p class="text-sm text-gray-900"><span class="text-gray-500">Issued:</span> Oct 25, 2024</p>
                    <p class="text-sm text-gray-900"><span class="text-gray-500">Due:</span> Nov 25, 2024</p>
                </div>
            </div>

            <div class="p-8">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-gray-200">
                            <th class="py-2 text-sm text-gray-500 uppercase font-bold">Item</th>
                            <th class="py-2 text-sm text-gray-500 uppercase font-bold text-right">Hrs/Qty</th>
                            <th class="py-2 text-sm text-gray-500 uppercase font-bold text-right">Rate</th>
                            <th class="py-2 text-sm text-gray-500 uppercase font-bold text-right">Amount</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-100">
                        <tr>
                            <td class="py-4">
                                <p class="font-bold text-gray-900">Web Design</p>
                                <p class="text-sm text-gray-500">Design of homepage and interior pages</p>
                            </td>
                            <td class="py-4 text-right">20</td>
                            <td class="py-4 text-right">$100.00</td>
                            <td class="py-4 text-right font-medium">$2,000.00</td>
                        </tr>
                        <tr>
                            <td class="py-4">
                                <p class="font-bold text-gray-900">Frontend Development</p>
                                <p class="text-sm text-gray-500">React implementation with Tailwind</p>
                            </td>
                            <td class="py-4 text-right">40</td>
                            <td class="py-4 text-right">$120.00</td>
                            <td class="py-4 text-right font-medium">$4,800.00</td>
                        </tr>
                        <tr>
                            <td class="py-4">
                                <p class="font-bold text-gray-900">Hosting Setup</p>
                                <p class="text-sm text-gray-500">Server configuration and deployment</p>
                            </td>
                            <td class="py-4 text-right">5</td>
                            <td class="py-4 text-right">$150.00</td>
                            <td class="py-4 text-right font-medium">$750.00</td>
                        </tr>
                    </tbody>
                </table>

                <div class="flex flex-col md:flex-row justify-end mt-8 border-t border-gray-200 pt-8">
                     <div class="w-full md:w-1/2 space-y-3">
                         <div class="flex justify-between">
                            <span class="text-gray-500">Subtotal</span>
                            <span class="font-bold text-gray-900">$7,550.00</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-500">Tax (10%)</span>
                            <span class="font-bold text-gray-900">$755.00</span>
                        </div>
                         <div class="flex justify-between border-t border-gray-200 pt-3">
                            <span class="text-xl font-bold text-gray-900">Total</span>
                            <span class="text-xl font-bold text-blue-600">$8,305.00</span>
                        </div>
                     </div>
                </div>
            </div>

            <div class="bg-gray-50 p-6 flex justify-between items-center print:hidden">
                <button class="text-gray-500 hover:text-gray-900 font-medium text-sm">Download PDF</button>
                <button class="bg-blue-600 text-white px-6 py-2 rounded-lg font-bold hover:bg-blue-700 transition">Pay Invoice</button>
            </div>
        </div>
    </div>"""
    },
    {
        "id": "dashboard-910",
        "title": "File Upload",
        "description": "Drag and drop file upload area.",
        "dir": "templates/99-dashboard",
        "content": """
    <div class="max-w-xl mx-auto py-20 px-4">
        <h2 class="text-xl font-bold text-gray-900 mb-4">Upload Assets</h2>
        <div class="flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-xl hover:border-blue-400 hover:bg-blue-50 transition-colors cursor-pointer group">
            <div class="space-y-1 text-center">
                <svg class="mx-auto h-12 w-12 text-gray-400 group-hover:text-blue-500 transition" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                    <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
                <div class="flex text-sm text-gray-600 justify-center">
                    <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-blue-600 hover:text-blue-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-blue-500">
                        <span>Upload a file</span>
                        <input id="file-upload" name="file-upload" type="file" class="sr-only">
                    </label>
                    <p class="pl-1">or drag and drop</p>
                </div>
                <p class="text-xs text-gray-500">
                    PNG, JPG, GIF up to 10MB
                </p>
            </div>
        </div>

        <div class="mt-6 space-y-3">
            <div class="flex items-center justify-between p-3 bg-white border border-gray-200 rounded-lg shadow-sm">
                <div class="flex items-center">
                    <div class="h-10 w-10 text-red-500 bg-red-50 rounded-lg flex items-center justify-center mr-3">
                        <span class="text-xs font-bold uppercase">PDF</span>
                    </div>
                    <div>
                         <p class="text-sm font-medium text-gray-900">Documentation.pdf</p>
                         <p class="text-xs text-gray-500">2.4 MB • Uploading...</p>
                    </div>
                </div>
                <div class="w-24 h-1.5 bg-gray-200 rounded-full overflow-hidden">
                    <div class="bg-blue-500 h-full w-2/3"></div>
                </div>
            </div>

             <div class="flex items-center justify-between p-3 bg-white border border-gray-200 rounded-lg shadow-sm">
                <div class="flex items-center">
                    <div class="h-10 w-10 text-green-500 bg-green-50 rounded-lg flex items-center justify-center mr-3">
                        <span class="text-xs font-bold uppercase">PNG</span>
                    </div>
                    <div>
                         <p class="text-sm font-medium text-gray-900">Dashboard_V2.png</p>
                         <p class="text-xs text-gray-500">4.1 MB • Completed</p>
                    </div>
                </div>
                 <button class="text-gray-400 hover:text-red-500">
                    <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                </button>
            </div>
        </div>
    </div>"""
    }
]


TEMPLATES_DASHBOARD_3 = []
for i in range(911, 926):
    TEMPLATES_DASHBOARD_3.append({
        "id": f"dashboard-{i}",
        "title": f"Dashboard Layout {i}",
        "description": f"Dashboard template variation {i}.",
        "dir": "templates/99-dashboard",
        "content": f"""
    <div class="min-h-screen bg-gray-50 flex">
        <!-- Sidebar -->
        <div class="w-64 bg-white border-r border-gray-200 hidden md:block">
            <div class="h-16 flex items-center justify-center border-b border-gray-200">
                <span class="font-bold text-xl text-blue-600">Admin {i}</span>
            </div>
            <nav class="p-4 space-y-1">
                <a href="#" class="block px-4 py-2 bg-blue-50 text-blue-700 rounded-md font-medium">Dashboard</a>
                <a href="#" class="block px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-md font-medium">Orders</a>
                <a href="#" class="block px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-md font-medium">Products</a>
                <a href="#" class="block px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-md font-medium">Customers</a>
                <a href="#" class="block px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-md font-medium">Reports</a>
            </nav>
        </div>

        <!-- Main Content -->
        <div class="flex-1 flex flex-col">
            <header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-8">
                <h2 class="text-lg font-bold text-gray-900">Dashboard Overview</h2>
                <div class="flex items-center gap-4">
                    <button class="p-2 text-gray-400 hover:text-gray-500">
                        <span class="sr-only">Notifications</span>
                        🔔
                    </button>
                    <img class="h-8 w-8 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                </div>
            </header>

            <main class="flex-1 p-8 overflow-y-auto">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                    <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                        <h3 class="text-sm font-medium text-gray-500">Total Users</h3>
                        <p class="mt-2 text-3xl font-bold text-gray-900">12,345</p>
                    </div>
                     <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                        <h3 class="text-sm font-medium text-gray-500">Total Revenue</h3>
                        <p class="mt-2 text-3xl font-bold text-gray-900">$34,567</p>
                    </div>
                     <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                        <h3 class="text-sm font-medium text-gray-500">Active Sessions</h3>
                        <p class="mt-2 text-3xl font-bold text-gray-900">456</p>
                    </div>
                     <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                        <h3 class="text-sm font-medium text-gray-500">Bounce Rate</h3>
                        <p class="mt-2 text-3xl font-bold text-gray-900">12%</p>
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow-sm border border-gray-200 min-h-[400px] flex items-center justify-center text-gray-400">
                    Chart Placeholder for Dashboard {i}
                </div>
            </main>
        </div>
    </div>"""
    })

TEMPLATES_BATCH_10.extend(TEMPLATES_DASHBOARD_2)
TEMPLATES_BATCH_10.extend(TEMPLATES_DASHBOARD_3)

# Ecommerce 926-950
TEMPLATES_ECOMMERCE = []
for i in range(926, 951):
    TEMPLATES_ECOMMERCE.append({
        "id": f"ecommerce-{i}",
        "title": f"Ecommerce Layout {i}",
        "description": f"Shop template variation {i}.",
        "dir": "templates/100-ecommerce",
        "content": f"""
    <div class="bg-white">
        <div class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
            <h2 class="text-2xl font-bold tracking-tight text-gray-900">Trending Products {i}</h2>
            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
                <div class="group relative">
                    <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
                        <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" alt="Product" class="h-full w-full object-cover object-center lg:h-full lg:w-full">
                    </div>
                    <div class="mt-4 flex justify-between">
                        <div>
                            <h3 class="text-sm text-gray-700">
                                <a href="#">
                                    <span aria-hidden="true" class="absolute inset-0"></span>
                                    Basic Tee
                                </a>
                            </h3>
                            <p class="mt-1 text-sm text-gray-500">Black</p>
                        </div>
                        <p class="text-sm font-medium text-gray-900">$35</p>
                    </div>
                </div>
                 <!-- More products would go here -->
            </div>
        </div>
    </div>"""
    })
TEMPLATES_BATCH_10.extend(TEMPLATES_ECOMMERCE)

# Blog 951-975
TEMPLATES_BLOG = []
for i in range(951, 976):
    TEMPLATES_BLOG.append({
        "id": f"blog-{i}",
        "title": f"Blog Layout {i}",
        "description": f"Blog template variation {i}.",
        "dir": "templates/101-blog",
        "content": f"""
    <div class="bg-white py-24 sm:py-32">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <div class="mx-auto max-w-2xl text-center">
                <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">From the blog {i}</h2>
                <p class="mt-2 text-lg leading-8 text-gray-600">Learn how to grow your business with our expert advice.</p>
            </div>
            <div class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-3">
                <article class="flex flex-col items-start justify-between">
                    <div class="relative w-full">
                        <img src="https://images.unsplash.com/photo-1496128858413-b36217c2ce36?ixlib=rb-4.0.3&auto=format&fit=crop&w=3603&q=80" alt="" class="aspect-[16/9] w-full rounded-2xl bg-gray-100 object-cover sm:aspect-[2/1] lg:aspect-[3/2]">
                        <div class="absolute inset-0 rounded-2xl ring-1 ring-inset ring-gray-900/10"></div>
                    </div>
                    <div class="max-w-xl">
                        <div class="mt-8 flex items-center gap-x-4 text-xs">
                            <time datetime="2020-03-16" class="text-gray-500">Mar 16, 2020</time>
                            <a href="#" class="relative z-10 rounded-full bg-gray-50 px-3 py-1.5 font-medium text-gray-600 hover:bg-gray-100">Marketing</a>
                        </div>
                        <div class="group relative">
                            <h3 class="mt-3 text-lg font-semibold leading-6 text-gray-900 group-hover:text-gray-600">
                                <a href="#">
                                    <span class="absolute inset-0"></span>
                                    Boost your conversion rate
                                </a>
                            </h3>
                            <p class="mt-5 line-clamp-3 text-sm leading-6 text-gray-600">Illo sint voluptas. Error voluptates culpa eligendi. Hic vel totam vitae illo. Non aliquid explicabo necessitatibus unde. Sed exercitationem placeat consectetur nulla deserunt vel. Iusto corrupti dicta.</p>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </div>"""
    })
TEMPLATES_BATCH_10.extend(TEMPLATES_BLOG)

# Community 976-1000
TEMPLATES_COMMUNITY = []
for i in range(976, 1001):
    TEMPLATES_COMMUNITY.append({
        "id": f"community-{i}",
        "title": f"Community Layout {i}",
        "description": f"Forum/Community template variation {i}.",
        "dir": "templates/102-community",
        "content": f"""
    <div class="min-h-screen bg-gray-100">
        <div class="py-10">
            <div class="mx-auto max-w-3xl sm:px-6 lg:max-w-7xl lg:grid lg:grid-cols-12 lg:gap-8 lg:px-8">
                <div class="hidden lg:col-span-3 lg:block xl:col-span-2">
                    <nav aria-label="Sidebar" class="sticky top-4 divide-y divide-gray-300">
                        <div class="pb-8 space-y-1">
                            <a href="#" class="bg-gray-200 text-gray-900 group flex items-center px-3 py-2 text-sm font-medium rounded-md">Home</a>
                            <a href="#" class="text-gray-600 hover:bg-gray-50 group flex items-center px-3 py-2 text-sm font-medium rounded-md">Popular</a>
                            <a href="#" class="text-gray-600 hover:bg-gray-50 group flex items-center px-3 py-2 text-sm font-medium rounded-md">Communities</a>
                        </div>
                    </nav>
                </div>
                <main class="lg:col-span-9 xl:col-span-6">
                    <div class="px-4 sm:px-0">
                        <div class="sm:hidden">
                            <label for="question-tabs" class="sr-only">Select a tab</label>
                            <select id="question-tabs" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-rose-500 focus:ring-rose-500">
                                <option selected>Recent</option>
                                <option>Most Liked</option>
                                <option>Most Answers</option>
                            </select>
                        </div>
                        <div class="hidden sm:block">
                            <nav class="isolate flex divide-x divide-gray-200 rounded-lg shadow" aria-label="Tabs">
                                <a href="#" aria-current="page" class="text-gray-900 rounded-l-lg group relative min-w-0 flex-1 overflow-hidden bg-white py-4 px-6 text-center text-sm font-medium hover:bg-gray-50 focus:z-10">
                                    <span>Recent</span>
                                    <span aria-hidden="true" class="bg-rose-500 absolute inset-x-0 bottom-0 h-0.5"></span>
                                </a>
                                <a href="#" class="text-gray-500 hover:text-gray-700 group relative min-w-0 flex-1 overflow-hidden bg-white py-4 px-6 text-center text-sm font-medium hover:bg-gray-50 focus:z-10">
                                    <span>Most Liked</span>
                                    <span aria-hidden="true" class="bg-transparent absolute inset-x-0 bottom-0 h-0.5"></span>
                                </a>
                                <a href="#" class="text-gray-500 hover:text-gray-700 rounded-r-lg group relative min-w-0 flex-1 overflow-hidden bg-white py-4 px-6 text-center text-sm font-medium hover:bg-gray-50 focus:z-10">
                                    <span>Most Answers</span>
                                    <span aria-hidden="true" class="bg-transparent absolute inset-x-0 bottom-0 h-0.5"></span>
                                </a>
                            </nav>
                        </div>
                    </div>
                    <div class="mt-4">
                        <h1 class="sr-only">Recent questions</h1>
                        <ul role="list" class="space-y-4">
                            <li class="bg-white px-4 py-6 shadow sm:p-6 sm:rounded-lg">
                                <article aria-labelledby="question-title-{i}">
                                    <div>
                                        <div class="flex space-x-3">
                                            <div class="flex-shrink-0">
                                                <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                                            </div>
                                            <div class="min-w-0 flex-1">
                                                <p class="text-sm font-medium text-gray-900">
                                                    <a href="#" class="hover:underline">Dries Vincent</a>
                                                </p>
                                                <p class="text-sm text-gray-500">
                                                    <a href="#" class="hover:underline">December 9 at 11:43 AM</a>
                                                </p>
                                            </div>
                                            <div class="flex flex-shrink-0 self-center">
                                                <div class="relative inline-block text-left">
                                                    <button type="button" class="-m-2 flex items-center rounded-full p-2 text-gray-400 hover:text-gray-600" id="options-menu-0-button" aria-expanded="false" aria-haspopup="true">
                                                        <span class="sr-only">Open options</span>
                                                        <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                            <path d="M10 3a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM10 8.5a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM11.5 15.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0z" />
                                                        </svg>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                        <h2 id="question-title-{i}" class="mt-4 text-base font-medium text-gray-900">
                                            What is the best way to handle state management?
                                        </h2>
                                    </div>
                                    <div class="mt-2 text-sm text-gray-700 space-y-4">
                                        <p>I am building a large application and I am not sure which state management library to use.</p>
                                    </div>
                                    <div class="mt-6 flex justify-between space-x-8">
                                        <div class="flex space-x-6">
                                            <span class="inline-flex items-center text-sm">
                                                <button type="button" class="inline-flex space-x-2 text-gray-400 hover:text-gray-500">
                                                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                        <path d="M1 8.25a1.25 1.25 0 112.5 0v7.5a1.25 1.25 0 11-2.5 0v-7.5zM11 3V1.7c0-.266.143-.521.38-.674a.75.75 0 01.411-.122 2.5 2.5 0 012.333 1.543l.872 2.443h4.254a2.25 2.25 0 012.25 2.25v2.836a3 3 0 01-.088.718l-1.398 5.592a3 3 0 01-2.912 2.27h-4.305a3 3 0 01-2.25-1.018l-4.509-5.186A2.25 2.25 0 015 8.79V5.25A2.25 2.25 0 017.25 3H11z" />
                                                    </svg>
                                                    <span class="font-medium text-gray-900">29</span>
                                                    <span class="sr-only">likes</span>
                                                </button>
                                            </span>
                                            <span class="inline-flex items-center text-sm">
                                                <button type="button" class="inline-flex space-x-2 text-gray-400 hover:text-gray-500">
                                                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                        <path fill-rule="evenodd" d="M10 2c-2.236 0-4.43.18-6.57.524C1.993 2.755 1 4.014 1 5.426v5.148c0 1.413.993 2.67 2.43 2.902.848.137 1.705.248 2.57.331v3.443a.75.75 0 001.28.53l3.58-3.579a.78.78 0 01.527-.224 41.202 41.202 0 003.444-.33c1.436-.23 2.429-1.487 2.429-2.9v-5.148c0-1.413-.993-2.67-2.43-2.902a41.289 41.289 0 00-6.57-.524zM5.352 4.425a42.536 42.536 0 019.296 0c.937.15 1.602.97 1.602 1.916v5.148c0 .947-.665 1.766-1.602 1.916-2.505.402-5.07.561-7.618.473L4.75 16.14V13.84c-.87-.075-1.73-.178-2.58-.313-.937-.15-1.602-.97-1.602-1.916V6.341c0-.947.665-1.766 1.602-1.916z" clip-rule="evenodd" />
                                                    </svg>
                                                    <span class="font-medium text-gray-900">11</span>
                                                    <span class="sr-only">replies</span>
                                                </button>
                                            </span>
                                        </div>
                                    </div>
                                </article>
                            </li>
                        </ul>
                    </div>
                </main>
                <aside class="hidden xl:block xl:col-span-4">
                    <div class="sticky top-4 space-y-4">
                        <section aria-labelledby="who-to-follow-heading">
                            <div class="bg-white rounded-lg shadow">
                                <div class="p-6">
                                    <h2 id="who-to-follow-heading" class="text-base font-medium text-gray-900">Who to follow</h2>
                                    <div class="mt-6 flow-root">
                                        <ul role="list" class="-my-4 divide-y divide-gray-200">
                                            <li class="flex items-center py-4 space-x-3">
                                                <div class="flex-shrink-0">
                                                    <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                                                </div>
                                                <div class="min-w-0 flex-1">
                                                    <p class="text-sm font-medium text-gray-900">
                                                        <a href="#">Leonard Krasner</a>
                                                    </p>
                                                    <p class="text-sm text-gray-500">
                                                        <a href="#">@leonardkrasner</a>
                                                    </p>
                                                </div>
                                                <div class="flex-shrink-0">
                                                    <button type="button" class="inline-flex items-center rounded-full bg-rose-50 px-3 py-0.5 text-sm font-medium text-rose-700 hover:bg-rose-100">
                                                        <svg class="-ml-1 mr-0.5 h-5 w-5 text-rose-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                            <path d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z" />
                                                        </svg>
                                                        Follow
                                                    </button>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </div>
                </aside>
            </div>
        </div>
    </div>"""
    })
TEMPLATES_BATCH_10.extend(TEMPLATES_COMMUNITY)


