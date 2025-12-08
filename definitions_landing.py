TEMPLATES_LANDING_NEW = [
    {
        "id": "landing-001",
        "title": "SaaS Minimalist",
        "description": "Clean SaaS landing page with hero, features, and pricing.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <!-- Header -->
      <header class="absolute inset-x-0 top-0 z-50">
        <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
          <div class="flex lg:flex-1">
            <a href="#" class="-m-1.5 p-1.5">
              <span class="sr-only">Your Company</span>
              <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="">
            </a>
          </div>
          <div class="flex lg:hidden">
            <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700">
              <span class="sr-only">Open main menu</span>
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" /></svg>
            </button>
          </div>
          <div class="hidden lg:flex lg:gap-x-12">
            <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Product</a>
            <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Features</a>
            <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Marketplace</a>
            <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Company</a>
          </div>
          <div class="hidden lg:flex lg:flex-1 lg:justify-end">
            <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Log in <span aria-hidden="true">&rarr;</span></a>
          </div>
        </nav>
      </header>

      <main class="isolate">
        <!-- Hero section -->
        <div class="relative pt-14">
          <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
            <div class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
          </div>
          <div class="py-24 sm:py-32 lg:pb-40">
            <div class="mx-auto max-w-7xl px-6 lg:px-8">
              <div class="mx-auto max-w-2xl text-center">
                <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">Data to enrich your online business</h1>
                <p class="mt-6 text-lg leading-8 text-gray-600">Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.</p>
                <div class="mt-10 flex items-center justify-center gap-x-6">
                  <a href="#" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Get started</a>
                  <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Learn more <span aria-hidden="true">→</span></a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Features section -->
        <div class="mx-auto max-w-7xl px-6 lg:px-8 py-24 sm:py-32">
          <div class="mx-auto max-w-2xl lg:text-center">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">Deploy faster</h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Everything you need to deploy your app</p>
            <p class="mt-6 text-lg leading-8 text-gray-600">Quis tellus eget adipiscing convallis sit sit eget aliquet quis. Suspendisse eget egestas a elementum pulvinar et feugiat blandit at. In mi viverra elit nunc.</p>
          </div>
          <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
            <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
              <div class="relative pl-16">
                <dt class="text-base font-semibold leading-7 text-gray-900">
                  <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
                    <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 16.5V9.75m0 0l3 3m-3-3l-3 3M6.75 19.5a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z" /></svg>
                  </div>
                  Push to deploy
                </dt>
                <dd class="mt-2 text-base leading-7 text-gray-600">Morbi viverra dui mi arcu sed. Tellus semper adipiscing suspendisse semper morbi. Odio urna massa nunc massa.</dd>
              </div>
              <div class="relative pl-16">
                 <dt class="text-base font-semibold leading-7 text-gray-900">
                  <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
                    <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" /></svg>
                  </div>
                  SSL certificates
                </dt>
                <dd class="mt-2 text-base leading-7 text-gray-600">Sit quis amet rutrum tellus ullamcorper ultricies libero dolor eget. Sem sodales gravida quam turpis enim lacus amet.</dd>
              </div>
            </dl>
          </div>
        </div>
      </main>
    </div>"""
    },
    {
        "id": "landing-002",
        "title": "Mobile App Dark",
        "description": "Dark themed landing page for mobile apps.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gray-900">
      <main>
        <div class="relative isolate pt-14">
          <div class="py-24 sm:py-32 lg:pb-40">
            <div class="mx-auto max-w-7xl px-6 lg:px-8">
              <div class="mx-auto max-w-2xl text-center">
                <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">Download the future of finance</h1>
                <p class="mt-6 text-lg leading-8 text-gray-300">Manage your money with ease. Instant transfers, investment tracking, and detailed analytics all in one app.</p>
                <div class="mt-10 flex items-center justify-center gap-x-6">
                  <a href="#" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get the App</a>
                  <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
                </div>
              </div>
              <div class="mt-16 flow-root sm:mt-24">
                <div class="-m-2 rounded-xl bg-gray-900/5 p-2 ring-1 ring-inset ring-gray-900/10 lg:-m-4 lg:rounded-2xl lg:p-4">
                  <img src="https://tailwindui.com/img/component-images/project-app-screenshot.png" alt="App screenshot" width="2432" height="1442" class="rounded-md shadow-2xl ring-1 ring-gray-900/10">
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Feature Strip -->
        <div class="bg-gray-800 py-24 sm:py-32">
            <div class="mx-auto max-w-7xl px-6 lg:px-8">
                <div class="grid grid-cols-1 gap-8 md:grid-cols-3 text-center">
                    <div>
                        <h3 class="text-white text-lg font-bold">Secure</h3>
                        <p class="text-gray-400">Bank grade encryption.</p>
                    </div>
                     <div>
                        <h3 class="text-white text-lg font-bold">Fast</h3>
                        <p class="text-gray-400">Instant transactions worldwide.</p>
                    </div>
                     <div>
                        <h3 class="text-white text-lg font-bold">Reliable</h3>
                        <p class="text-gray-400">24/7 support.</p>
                    </div>
                </div>
            </div>
        </div>
      </main>
    </div>"""
    },
    {
        "id": "landing-003",
        "title": "Agency Creative",
        "description": "Bold creative agency portfolio landing.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-black text-white">
      <header class="p-6 flex justify-between items-center">
        <div class="text-2xl font-bold uppercase tracking-wider">Agency</div>
        <nav class="hidden md:flex gap-8">
            <a href="#" class="hover:text-gray-300">Work</a>
            <a href="#" class="hover:text-gray-300">Services</a>
            <a href="#" class="hover:text-gray-300">About</a>
        </nav>
        <a href="#" class="bg-white text-black px-4 py-2 rounded-full font-bold hover:bg-gray-200">Contact</a>
      </header>
      <main>
        <div class="px-6 py-24 sm:py-32 lg:px-8">
            <h1 class="text-6xl sm:text-9xl font-black uppercase leading-none mb-12">We Build<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 to-pink-500">Brands</span></h1>
            <p class="text-xl sm:text-2xl max-w-2xl text-gray-400">We are a digital product agency that helps brands crush their competition through design and technology.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
             <div class="aspect-square bg-gray-900 relative group overflow-hidden">
                <img src="https://images.unsplash.com/photo-1600607686527-6fb886090705?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity duration-500" alt="">
                <div class="absolute bottom-8 left-8">
                    <h3 class="text-3xl font-bold">Project Alpha</h3>
                    <p class="text-gray-400">Branding / Web</p>
                </div>
             </div>
             <div class="aspect-square bg-gray-800 relative group overflow-hidden">
                 <img src="https://images.unsplash.com/photo-1561070791-2526d30994b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity duration-500" alt="">
                 <div class="absolute bottom-8 left-8">
                    <h3 class="text-3xl font-bold">Project Beta</h3>
                    <p class="text-gray-400">Mobile App</p>
                </div>
             </div>
        </div>
      </main>
    </div>"""
    },
    {
        "id": "landing-004",
        "title": "E-Book Sales",
        "description": "Landing page optimized for selling a digital book.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-amber-50">
      <main class="grid grid-cols-1 lg:grid-cols-2 min-h-screen">
        <div class="px-6 py-24 sm:px-12 lg:px-24 flex flex-col justify-center">
            <span class="text-amber-600 font-semibold tracking-wide uppercase mb-4">New Release</span>
            <h1 class="text-4xl sm:text-6xl font-serif font-bold text-gray-900 mb-6">Mastering the Art of Cooking</h1>
            <p class="text-lg text-gray-700 mb-8">Unlock the secrets of professional chefs in your own kitchen. Over 100 recipes, techniques, and tips to elevate your culinary skills.</p>
            <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center mb-12">
                <a href="#" class="bg-amber-600 text-white px-8 py-3 rounded-lg font-bold shadow-lg hover:bg-amber-700 transition">Buy Now - $29</a>
                <p class="text-sm text-gray-500">Includes PDF, ePub, and Kindle formats.</p>
            </div>
            <div class="flex gap-4">
                 <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-12 h-12 rounded-full" alt="">
                 <div>
                     <p class="font-bold text-gray-900">Julia Child</p>
                     <p class="text-sm text-gray-600">Author & Chef</p>
                 </div>
            </div>
        </div>
        <div class="bg-amber-200 relative">
             <img src="https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="h-full w-full object-cover opacity-80 mix-blend-multiply" alt="">
             <div class="absolute inset-0 flex items-center justify-center p-12">
                 <div class="bg-white shadow-2xl p-8 max-w-xs rotate-3 transform hover:rotate-0 transition duration-500">
                      <div class="aspect-[2/3] bg-gray-100 border border-gray-200 flex items-center justify-center">
                          <span class="font-serif text-2xl text-center text-gray-400">Book Cover</span>
                      </div>
                 </div>
             </div>
        </div>
      </main>
    </div>"""
    },
    {
        "id": "landing-005",
        "title": "Webinar Registration",
        "description": "High conversion webinar sign-up page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <div class="relative isolate px-6 pt-14 lg:px-8">
        <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56 text-center">
          <div class="mb-8 flex justify-center">
            <div class="relative rounded-full px-3 py-1 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
              Live Event starting in <span class="font-mono font-bold text-indigo-600">02:14:55</span>
            </div>
          </div>
          <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">How to Scale Your Agency to 7 Figures</h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">Join us for a free 60-minute masterclass where we reveal the exact systems and strategies used by top agencies to grow rapidly.</p>
          <div class="mt-10 flex flex-col items-center gap-y-6">
              <form class="w-full max-w-md flex flex-col gap-4">
                  <input type="email" placeholder="Enter your email address" class="w-full rounded-md border-0 py-3 px-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                  <button type="submit" class="w-full rounded-md bg-indigo-600 px-3.5 py-3 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Reserve My Spot</button>
              </form>
              <p class="text-xs text-gray-500">Limited to 500 attendees. No replay.</p>
          </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-006",
        "title": "Newsletter Subscription",
        "description": "Minimal page focused on growing a mailing list.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gray-50 min-h-screen flex items-center justify-center px-6">
      <div class="w-full max-w-xl bg-white rounded-3xl shadow-xl p-8 sm:p-12 text-center">
         <div class="mx-auto h-16 w-16 bg-blue-100 rounded-full flex items-center justify-center mb-6">
             <svg class="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
         </div>
         <h1 class="text-3xl font-bold text-gray-900 mb-4">Weekly Wisdom</h1>
         <p class="text-gray-600 mb-8">Get the best tips on productivity, design, and tech delivered straight to your inbox every Monday. Join 10,000+ subscribers.</p>
         <form class="flex flex-col sm:flex-row gap-3">
             <input type="email" placeholder="john@example.com" class="flex-1 rounded-lg border-gray-300 focus:border-blue-500 focus:ring-blue-500 p-3 shadow-sm border">
             <button type="submit" class="bg-blue-600 text-white font-semibold py-3 px-6 rounded-lg hover:bg-blue-700 transition">Subscribe</button>
         </form>
         <p class="mt-4 text-xs text-gray-400">We respect your privacy. Unsubscribe at any time.</p>
      </div>
    </div>"""
    },
    {
        "id": "landing-007",
        "title": "Online Course",
        "description": "Educational course sales page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <!-- Course Hero -->
      <div class="relative bg-gray-900 py-24 sm:py-32">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
           <div class="max-w-2xl">
               <div class="inline-flex items-center rounded-full bg-indigo-500/10 px-3 py-1 text-sm font-medium text-indigo-400 ring-1 ring-inset ring-indigo-500/20 mb-6">Beginner to Pro</div>
               <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl mb-6">The Complete Python Bootcamp</h1>
               <p class="text-lg leading-8 text-gray-300 mb-8">Learn Python like a professional. Start from the basics and go all the way to creating your own applications and games.</p>
               <div class="flex flex-col sm:flex-row gap-4">
                   <button class="bg-indigo-500 text-white font-bold py-3 px-8 rounded-lg hover:bg-indigo-400 transition">Enroll Now</button>
                    <button class="text-white font-semibold py-3 px-8 rounded-lg border border-white/20 hover:bg-white/10 transition">Watch Preview</button>
               </div>
               <div class="mt-8 flex items-center gap-4 text-gray-400 text-sm">
                   <div class="flex text-yellow-500">
                       ★★★★★
                   </div>
                   <span>4.8 (12,000 ratings)</span>
                   <span>•</span>
                   <span>150,000 students</span>
               </div>
           </div>
        </div>
      </div>
      <!-- Syllabus -->
      <div class="py-24 sm:py-32">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-gray-900 mb-12">What you'll learn</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="flex gap-4">
                    <div class="flex-none w-6 h-6 rounded-full bg-green-100 flex items-center justify-center text-green-600">✓</div>
                    <p class="text-gray-700">Master Python 3 by building 100 projects in 100 days.</p>
                </div>
                 <div class="flex gap-4">
                    <div class="flex-none w-6 h-6 rounded-full bg-green-100 flex items-center justify-center text-green-600">✓</div>
                    <p class="text-gray-700">Learn to use Object Oriented Programming</p>
                </div>
                 <div class="flex gap-4">
                    <div class="flex-none w-6 h-6 rounded-full bg-green-100 flex items-center justify-center text-green-600">✓</div>
                    <p class="text-gray-700">Understand complex topics like Decorators.</p>
                </div>
                 <div class="flex gap-4">
                    <div class="flex-none w-6 h-6 rounded-full bg-green-100 flex items-center justify-center text-green-600">✓</div>
                    <p class="text-gray-700">Build GUIs and Desktop applications.</p>
                </div>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-008",
        "title": "Real Estate Luxury",
        "description": "Luxury property listing landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-stone-50">
      <div class="relative h-screen">
         <img src="https://images.unsplash.com/photo-1600596542815-60c37cabc38d?ixlib=rb-1.2.1&auto=format&fit=crop&w=2600&q=80" class="w-full h-full object-cover" alt="Luxury Home">
         <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
             <div class="text-center text-white px-6">
                 <h1 class="text-5xl md:text-7xl font-serif mb-6">The Summit Estate</h1>
                 <p class="text-xl md:text-2xl font-light tracking-wide mb-8">Beverly Hills, California</p>
                 <a href="#details" class="border border-white px-8 py-3 text-sm uppercase tracking-widest hover:bg-white hover:text-black transition">View Residence</a>
             </div>
         </div>
      </div>
      <div id="details" class="max-w-7xl mx-auto px-6 py-24 grid grid-cols-1 md:grid-cols-3 gap-12 text-center md:text-left">
           <div>
               <p class="text-stone-500 uppercase tracking-widest text-xs mb-2">Price</p>
               <p class="text-3xl font-serif text-stone-900">$12,500,000</p>
           </div>
            <div>
               <p class="text-stone-500 uppercase tracking-widest text-xs mb-2">Bedrooms</p>
               <p class="text-3xl font-serif text-stone-900">6 Beds / 8 Baths</p>
           </div>
            <div>
               <p class="text-stone-500 uppercase tracking-widest text-xs mb-2">Size</p>
               <p class="text-3xl font-serif text-stone-900">8,500 Sq Ft</p>
           </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-009",
        "title": "Restaurant Modern",
        "description": "Appetizing restaurant landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <div class="relative h-[600px]">
         <div class="absolute inset-0">
            <img class="h-full w-full object-cover" src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80" alt="Cocktails">
            <div class="absolute inset-0 bg-black/50"></div>
         </div>
         <div class="relative max-w-7xl mx-auto px-6 h-full flex items-center">
             <div class="text-white max-w-xl">
                 <h1 class="text-6xl font-serif italic mb-6">Taste the Extraordinary</h1>
                 <p class="text-xl mb-8">Experience a fusion of flavors in a modern, elegant setting.</p>
                 <button class="bg-orange-500 hover:bg-orange-600 text-white px-8 py-3 rounded-md font-bold transition">Book a Table</button>
             </div>
         </div>
      </div>
      <div class="py-24 px-6 max-w-3xl mx-auto text-center">
          <h2 class="text-3xl font-bold text-gray-900 mb-6">Our Menu</h2>
          <p class="text-gray-600 mb-12">Crafted with passion using the finest local ingredients.</p>
          <div class="space-y-8">
              <div class="flex justify-between border-b border-gray-100 pb-4">
                  <div class="text-left">
                      <h3 class="text-lg font-bold text-gray-900">Truffle Risotto</h3>
                      <p class="text-sm text-gray-500">Arborio rice, black truffle, parmesan crisp.</p>
                  </div>
                  <span class="text-lg font-bold text-orange-600">$28</span>
              </div>
               <div class="flex justify-between border-b border-gray-100 pb-4">
                  <div class="text-left">
                      <h3 class="text-lg font-bold text-gray-900">Pan-Seared Scallops</h3>
                      <p class="text-sm text-gray-500">Cauliflower puree, lemon butter, capers.</p>
                  </div>
                  <span class="text-lg font-bold text-orange-600">$34</span>
              </div>
               <div class="flex justify-between border-b border-gray-100 pb-4">
                  <div class="text-left">
                      <h3 class="text-lg font-bold text-gray-900">Wagyu Beef Burger</h3>
                      <p class="text-sm text-gray-500">Brioche bun, aged cheddar, caramelized onions.</p>
                  </div>
                  <span class="text-lg font-bold text-orange-600">$22</span>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-010",
        "title": "Conference Event",
        "description": "Event promotion and ticket sales page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-blue-900 text-white">
      <div class="container mx-auto px-6 py-24 text-center">
        <p class="text-blue-300 font-bold tracking-widest uppercase mb-4">November 12-14, 2023 • San Francisco</p>
        <h1 class="text-5xl md:text-8xl font-black mb-8 leading-tight">FUTURE<br>DESIGN<br>SUMMIT</h1>
        <p class="text-xl md:text-2xl text-blue-100 max-w-2xl mx-auto mb-12">The world's largest gathering of digital designers, innovators, and creators.</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
             <button class="bg-pink-600 hover:bg-pink-700 text-white text-xl font-bold py-4 px-10 rounded-full transition transform hover:scale-105">Get Tickets</button>
             <button class="bg-transparent border-2 border-white hover:bg-white hover:text-blue-900 text-white text-xl font-bold py-4 px-10 rounded-full transition">View Speakers</button>
        </div>
      </div>
      <div class="bg-white text-gray-900 py-24">
         <div class="container mx-auto px-6">
             <h2 class="text-3xl font-bold text-center mb-16">Featured Speakers</h2>
             <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
                 <div class="text-center">
                     <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-32 h-32 rounded-full mx-auto mb-6 grayscale" alt="">
                     <h3 class="text-xl font-bold">Sarah Jenkins</h3>
                     <p class="text-gray-500">VP Design, Google</p>
                 </div>
                 <div class="text-center">
                     <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-32 h-32 rounded-full mx-auto mb-6 grayscale" alt="">
                     <h3 class="text-xl font-bold">David Chang</h3>
                     <p class="text-gray-500">Founder, Ideo</p>
                 </div>
                 <div class="text-center">
                     <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" class="w-32 h-32 rounded-full mx-auto mb-6 grayscale" alt="">
                     <h3 class="text-xl font-bold">Marcus Ross</h3>
                     <p class="text-gray-500">Creative Director, Apple</p>
                 </div>
             </div>
         </div>
      </div>
    </div>"""
    }
]

TEMPLATES_LANDING_PART_2 = [
    {
        "id": "landing-011",
        "title": "Medical Clinic",
        "description": "Professional healthcare provider landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <header class="bg-blue-600 text-white p-4">
        <div class="container mx-auto flex justify-between items-center">
             <div class="font-bold text-xl">MediCare+</div>
             <a href="#" class="bg-white text-blue-600 px-4 py-2 rounded-full font-bold">Book Appointment</a>
        </div>
      </header>
      <div class="container mx-auto px-6 py-16 flex flex-col md:flex-row items-center">
          <div class="md:w-1/2 mb-12 md:mb-0">
              <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">Expert Healthcare for Your Family</h1>
              <p class="text-xl text-gray-600 mb-8">We provide compassionate, comprehensive care for patients of all ages. From pediatric checkups to geriatric care, we are here for you.</p>
              <div class="flex gap-4">
                  <button class="bg-blue-600 text-white px-6 py-3 rounded-lg font-bold">Our Services</button>
                  <button class="border border-blue-600 text-blue-600 px-6 py-3 rounded-lg font-bold">Find a Doctor</button>
              </div>
          </div>
          <div class="md:w-1/2 md:pl-12">
              <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="rounded-xl shadow-2xl" alt="Doctor with patient">
          </div>
      </div>
      <div class="bg-gray-50 py-16">
          <div class="container mx-auto px-6">
              <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                  <div class="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
                      <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 mb-4">
                          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
                      </div>
                      <h3 class="text-xl font-bold mb-2">Primary Care</h3>
                      <p class="text-gray-500">Routine check-ups, preventive care, and health management.</p>
                  </div>
                   <div class="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
                      <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 mb-4">
                           <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" /></svg>
                      </div>
                      <h3 class="text-xl font-bold mb-2">Cardiology</h3>
                      <p class="text-gray-500">Expert heart care including diagnostics and treatment.</p>
                  </div>
                   <div class="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
                      <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 mb-4">
                          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                      </div>
                      <h3 class="text-xl font-bold mb-2">Urgent Care</h3>
                      <p class="text-gray-500">Immediate attention for non-life-threatening conditions.</p>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-012",
        "title": "Law Firm Classic",
        "description": "Trustworthy layout for legal services.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gray-50 font-serif">
      <div class="bg-slate-900 text-white py-24">
          <div class="container mx-auto px-6 text-center">
              <h2 class="text-yellow-500 text-lg uppercase tracking-widest mb-4">Sterling & Partners</h2>
              <h1 class="text-5xl md:text-6xl font-bold mb-8">Justice You Can Trust.</h1>
              <p class="text-xl text-gray-300 max-w-2xl mx-auto mb-12">With over 40 years of combined experience, we fight tirelessly to protect your rights and secure your future.</p>
              <button class="bg-yellow-600 hover:bg-yellow-700 text-white px-8 py-4 text-lg font-bold rounded shadow-lg transition">Free Consultation</button>
          </div>
      </div>
      <div class="container mx-auto px-6 py-24 -mt-16">
          <div class="bg-white rounded-lg shadow-xl p-12">
              <div class="grid grid-cols-1 md:grid-cols-3 gap-12 text-center divide-y md:divide-y-0 md:divide-x divide-gray-200">
                  <div class="px-4">
                      <h3 class="text-2xl font-bold text-slate-900 mb-2">Corporate Law</h3>
                      <p class="text-gray-600">Navigating complex business regulations and contracts.</p>
                  </div>
                   <div class="px-4 pt-8 md:pt-0">
                      <h3 class="text-2xl font-bold text-slate-900 mb-2">Family Law</h3>
                      <p class="text-gray-600">Compassionate support for divorce and custody matters.</p>
                  </div>
                   <div class="px-4 pt-8 md:pt-0">
                      <h3 class="text-2xl font-bold text-slate-900 mb-2">Criminal Defense</h3>
                      <p class="text-gray-600">Aggressive representation when your freedom is at stake.</p>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-013",
        "title": "Fintech Modern",
        "description": "Clean fintech landing with card visuals.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <div class="container mx-auto px-6 py-24 flex flex-col-reverse lg:flex-row items-center">
          <div class="lg:w-1/2 mt-12 lg:mt-0">
               <h1 class="text-5xl font-bold text-gray-900 leading-tight mb-6">Banking that puts <span class="text-emerald-500">you</span> first.</h1>
               <p class="text-xl text-gray-600 mb-8 max-w-lg">No fees. No minimums. Just simple, transparent banking designed for the modern world.</p>
               <div class="flex gap-4">
                   <button class="bg-emerald-500 text-white px-8 py-3 rounded-lg font-bold hover:bg-emerald-600 transition shadow-lg shadow-emerald-500/30">Open Account</button>
                   <button class="text-emerald-700 px-8 py-3 rounded-lg font-bold hover:bg-emerald-50 transition">See Features</button>
               </div>
               <div class="mt-12 flex items-center gap-4 text-gray-500 text-sm">
                   <span>Trusted by over 1 million users</span>
                   <div class="flex -space-x-2">
                       <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                       <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                       <img class="w-8 h-8 rounded-full border-2 border-white" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                   </div>
               </div>
          </div>
          <div class="lg:w-1/2 flex justify-center lg:justify-end">
              <div class="relative w-80 h-96 bg-gray-900 rounded-3xl shadow-2xl rotate-12 transform hover:rotate-6 transition duration-500 border border-gray-800 p-8 text-white">
                  <div class="flex justify-between items-start mb-12">
                      <div class="w-12 h-8 bg-emerald-500 rounded-md opacity-80"></div>
                      <span class="font-mono text-xl">VISA</span>
                  </div>
                  <p class="font-mono text-2xl tracking-widest mb-2">4000 1234 5678 9010</p>
                  <div class="flex justify-between mt-12 items-end">
                      <div>
                          <p class="text-xs text-gray-400 uppercase">Card Holder</p>
                          <p class="uppercase font-bold">John Doe</p>
                      </div>
                      <div>
                           <p class="text-xs text-gray-400 uppercase">Expires</p>
                          <p class="uppercase font-bold">12/25</p>
                      </div>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-014",
        "title": "Crypto Web3",
        "description": "Dark gradient landing for crypto/web3 project.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-black text-white min-h-screen relative overflow-hidden">
       <!-- Gradient Orb -->
       <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-purple-600 rounded-full mix-blend-multiply filter blur-[128px] opacity-20 animate-pulse"></div>
       <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-blue-600 rounded-full mix-blend-multiply filter blur-[128px] opacity-20 animate-pulse"></div>

       <header class="relative z-10 flex justify-between items-center px-6 py-6 container mx-auto">
           <div class="font-bold text-2xl tracking-tighter">ETHER<span class="text-purple-500">VERSE</span></div>
           <button class="bg-white/10 border border-white/20 hover:bg-white/20 px-6 py-2 rounded-full font-bold backdrop-blur-md transition">Connect Wallet</button>
       </header>

       <main class="relative z-10 container mx-auto px-6 py-24 text-center">
           <h1 class="text-5xl md:text-8xl font-black mb-8 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500">THE NEXT ERA<br>OF DEFI</h1>
           <p class="text-xl text-gray-400 max-w-2xl mx-auto mb-12">Trade, stake, and earn with zero gas fees. Built on the fastest layer-2 solution.</p>
           <div class="flex justify-center gap-6">
               <button class="bg-gradient-to-r from-blue-600 to-purple-600 px-8 py-4 rounded-full font-bold text-lg hover:shadow-lg hover:shadow-purple-500/50 transition">Launch App</button>
               <button class="bg-black border border-gray-700 px-8 py-4 rounded-full font-bold text-lg hover:border-white transition">Read Whitepaper</button>
           </div>

           <div class="mt-24 grid grid-cols-2 md:grid-cols-4 gap-8 border-t border-white/10 pt-12">
               <div>
                   <p class="text-3xl font-bold">$12B+</p>
                   <p class="text-xs text-gray-500 uppercase tracking-widest mt-2">Total Value Locked</p>
               </div>
                <div>
                   <p class="text-3xl font-bold">2M+</p>
                   <p class="text-xs text-gray-500 uppercase tracking-widest mt-2">Users</p>
               </div>
                <div>
                   <p class="text-3xl font-bold">0.05s</p>
                   <p class="text-xs text-gray-500 uppercase tracking-widest mt-2">Block Time</p>
               </div>
                <div>
                   <p class="text-3xl font-bold">$0.00</p>
                   <p class="text-xs text-gray-500 uppercase tracking-widest mt-2">Gas Fees</p>
               </div>
           </div>
       </main>
    </div>"""
    },
    {
        "id": "landing-015",
        "title": "Charity Non-Profit",
        "description": "Emotional landing page for donations.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <div class="relative h-[500px]">
          <img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-full object-cover" alt="Children">
          <div class="absolute inset-0 bg-black/60 flex items-center justify-center">
              <div class="text-center text-white px-6">
                  <h1 class="text-4xl md:text-6xl font-bold mb-6">Give Hope to Tomorrow</h1>
                  <p class="text-xl md:text-2xl mb-8 max-w-2xl mx-auto">Your donation provides education, food, and medicine to children in need across the globe.</p>
                  <button class="bg-red-500 hover:bg-red-600 text-white text-lg font-bold py-3 px-8 rounded-full shadow-lg transition">Donate Now</button>
              </div>
          </div>
      </div>
      <div class="py-24 bg-gray-50">
          <div class="container mx-auto px-6 max-w-4xl text-center">
              <h2 class="text-3xl font-bold text-gray-900 mb-12">Where your money goes</h2>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                  <div class="bg-white p-6 rounded-lg shadow text-center">
                      <div class="text-5xl mb-4">🎒</div>
                      <h3 class="text-xl font-bold mb-2">Education</h3>
                      <p class="text-gray-600">School supplies and tuition.</p>
                  </div>
                  <div class="bg-white p-6 rounded-lg shadow text-center">
                      <div class="text-5xl mb-4">🍲</div>
                      <h3 class="text-xl font-bold mb-2">Nutrition</h3>
                      <p class="text-gray-600">Healthy meals daily.</p>
                  </div>
                  <div class="bg-white p-6 rounded-lg shadow text-center">
                      <div class="text-5xl mb-4">💊</div>
                      <h3 class="text-xl font-bold mb-2">Healthcare</h3>
                      <p class="text-gray-600">Vaccines and checkups.</p>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-016",
        "title": "Personal Portfolio",
        "description": "Clean portfolio for designers or developers.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-zinc-50 min-h-screen">
      <div class="container mx-auto px-6 py-24 md:py-32">
          <div class="max-w-3xl">
              <p class="text-zinc-500 font-mono mb-4">Hello, I'm Alex.</p>
              <h1 class="text-5xl md:text-7xl font-bold text-zinc-900 mb-8 leading-tight">I craft digital experiences that <span class="text-indigo-600">delight</span> and <span class="text-indigo-600">inspire</span>.</h1>
              <p class="text-xl text-zinc-600 mb-12 max-w-2xl leading-relaxed">I'm a multidisciplinary designer and front-end developer based in New York. I help startups build their flagship products.</p>
              <div class="flex gap-6">
                  <a href="#" class="text-zinc-900 font-bold border-b-2 border-zinc-900 pb-1 hover:text-indigo-600 hover:border-indigo-600 transition">View Projects</a>
                  <a href="#" class="text-zinc-500 font-bold hover:text-zinc-900 transition">Read About Me</a>
              </div>
          </div>

          <div class="mt-24 grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="group cursor-pointer">
                  <div class="bg-zinc-200 aspect-[4/3] rounded-sm overflow-hidden mb-4">
                       <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition transform group-hover:scale-105 duration-500 grayscale group-hover:grayscale-0" alt="">
                  </div>
                  <h3 class="text-2xl font-bold text-zinc-900">Project Fin</h3>
                  <p class="text-zinc-500">Finance App Redesign</p>
              </div>
               <div class="group cursor-pointer md:mt-16">
                  <div class="bg-zinc-200 aspect-[4/3] rounded-sm overflow-hidden mb-4">
                       <img src="https://images.unsplash.com/photo-1555421689-d68471e189f2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition transform group-hover:scale-105 duration-500 grayscale group-hover:grayscale-0" alt="">
                  </div>
                  <h3 class="text-2xl font-bold text-zinc-900">Tech Co</h3>
                  <p class="text-zinc-500">Corporate Identity</p>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-017",
        "title": "Gaming Dark Mode",
        "description": "High energy gaming landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gray-900 text-white relative font-sans">
      <div class="absolute inset-0">
          <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-full object-cover opacity-20" alt="Gaming Setup">
          <div class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent"></div>
      </div>

      <div class="relative z-10 container mx-auto px-6 min-h-screen flex flex-col justify-center items-center text-center">
           <h2 class="text-green-500 font-bold tracking-[0.2em] mb-4 uppercase animate-pulse">Available Now</h2>
           <h1 class="text-6xl md:text-9xl font-black uppercase italic tracking-tighter mb-8 transform -skew-x-6 text-transparent bg-clip-text bg-gradient-to-r from-gray-100 to-gray-500 drop-shadow-2xl">Cyber<br>Strike</h1>
           <p class="text-xl md:text-2xl text-gray-300 max-w-2xl mb-12">Dominate the battlefield in the most immersive FPS experience ever created.</p>

           <div class="flex flex-col sm:flex-row gap-6">
                <button class="bg-green-500 hover:bg-green-400 text-black text-xl font-bold py-4 px-12 rounded skew-x-[-12deg] transition transform hover:scale-110 shadow-[0px_0px_20px_rgba(34,197,94,0.6)]">
                    <span class="inline-block skew-x-[12deg]">Play Free</span>
                </button>
                <div class="flex items-center gap-4 text-gray-400">
                    <span class="border border-gray-600 p-2 rounded">Windows</span>
                    <span class="border border-gray-600 p-2 rounded">PS5</span>
                    <span class="border border-gray-600 p-2 rounded">Xbox</span>
                </div>
           </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-018",
        "title": "Travel Adventure",
        "description": "Exotic travel destination landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <div class="relative h-[80vh]">
          <img src="https://images.unsplash.com/photo-1502003148287-a82ef80a6abc?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-full object-cover" alt="Tropical Beach">
          <div class="absolute inset-0 bg-black/20"></div>

          <nav class="absolute top-0 left-0 w-full p-6 flex justify-between items-center text-white z-10">
              <div class="text-2xl font-bold font-serif">Wanderlust</div>
              <ul class="hidden md:flex gap-8 font-medium">
                  <li><a href="#" class="hover:underline opacity-90">Destinations</a></li>
                  <li><a href="#" class="hover:underline opacity-90">Experiences</a></li>
                  <li><a href="#" class="hover:underline opacity-90">About</a></li>
              </ul>
              <button class="bg-white text-black px-6 py-2 rounded-full font-bold hover:bg-gray-100 transition">Book Now</button>
          </nav>

          <div class="absolute bottom-24 left-6 md:left-24 text-white max-w-xl">
              <h1 class="text-5xl md:text-7xl font-serif font-bold leading-tight mb-6">Discover the Unseen</h1>
              <p class="text-xl opacity-90 mb-8 border-l-4 border-white pl-6">Curated journeys to the most breathtaking corners of the earth.</p>
              <div class="flex gap-4">
                 <button class="bg-white/20 backdrop-blur-md border border-white/50 text-white px-8 py-3 rounded-full hover:bg-white hover:text-black transition">Explore Bali</button>
              </div>
          </div>
      </div>
      <div class="py-24 px-6 container mx-auto">
          <h2 class="text-3xl font-bold mb-12 text-center text-gray-900">Popular Destinations</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div class="relative rounded-xl overflow-hidden group cursor-pointer h-96">
                  <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition duration-700 group-hover:scale-110" alt="Alps">
                  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-8">
                      <h3 class="text-2xl font-bold text-white">Swiss Alps</h3>
                      <p class="text-gray-300">Winter Wonderland</p>
                  </div>
              </div>
                <div class="relative rounded-xl overflow-hidden group cursor-pointer h-96">
                  <img src="https://images.unsplash.com/photo-1512453979798-5ea936a7d40c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition duration-700 group-hover:scale-110" alt="Dubai">
                  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-8">
                      <h3 class="text-2xl font-bold text-white">Dubai</h3>
                      <p class="text-gray-300">Desert Luxury</p>
                  </div>
              </div>
                <div class="relative rounded-xl overflow-hidden group cursor-pointer h-96">
                  <img src="https://images.unsplash.com/photo-1533929736472-594e45aa96d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition duration-700 group-hover:scale-110" alt="Kyoto">
                  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-8">
                      <h3 class="text-2xl font-bold text-white">Kyoto</h3>
                      <p class="text-gray-300">Ancient Tradition</p>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-019",
        "title": "Fitness Gym",
        "description": "High energy fitness landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-black text-white">
      <div class="relative h-screen">
         <img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-full object-cover opacity-40 grayscale" alt="Gym">
         <div class="absolute inset-0 flex flex-col justify-center items-center text-center p-6">
             <h1 class="text-6xl md:text-9xl font-black uppercase italic tracking-tighter mb-6 text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-orange-500">No Pain<br>No Gain</h1>
             <p class="text-2xl md:text-3xl font-light mb-12 uppercase tracking-widest text-gray-300">Transform your body. Transform your life.</p>
             <button class="bg-red-600 hover:bg-red-700 text-white text-xl font-bold py-4 px-12 rounded uppercase tracking-wider transition clip-path-polygon-[10%_0,100%_0,90%_100%,0_100%] skew-x-[-10deg]">Join The Club</button>
         </div>
      </div>
      <div class="py-24 bg-zinc-900">
          <div class="container mx-auto px-6">
              <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
                  <div class="p-8 border border-zinc-700 hover:border-red-500 transition duration-300 bg-zinc-800 rounded-lg group">
                      <h3 class="text-2xl font-black uppercase mb-4 group-hover:text-red-500 transition">Strength</h3>
                      <p class="text-gray-400">Heavy lifting area with olympic standard equipment.</p>
                  </div>
                   <div class="p-8 border border-zinc-700 hover:border-red-500 transition duration-300 bg-zinc-800 rounded-lg group">
                      <h3 class="text-2xl font-black uppercase mb-4 group-hover:text-red-500 transition">Cardio</h3>
                      <p class="text-gray-400">State of the art runners, rowers, and bikes.</p>
                  </div>
                   <div class="p-8 border border-zinc-700 hover:border-red-500 transition duration-300 bg-zinc-800 rounded-lg group">
                      <h3 class="text-2xl font-black uppercase mb-4 group-hover:text-red-500 transition">Classes</h3>
                      <p class="text-gray-400">HIIT, Yoga, and Boxing led by expert trainers.</p>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-020",
        "title": "Beauty Spa Clean",
        "description": "Serene and clean spa landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-rose-50">
      <div class="container mx-auto px-6 py-24 md:py-32 flex flex-col md:flex-row items-center gap-12">
          <div class="md:w-1/2">
              <span class="text-rose-400 tracking-widest uppercase text-sm font-semibold mb-2 block">Natural Beauty</span>
              <h1 class="text-5xl md:text-6xl font-serif text-stone-800 mb-6 leading-tight">Revitalize your skin with nature's touch.</h1>
              <p class="text-xl text-stone-600 mb-8 leading-relaxed">Experience organic treatments designed to restore balance and harmony to your body and mind.</p>
               <button class="bg-rose-300 hover:bg-rose-400 text-rose-900 font-medium py-3 px-8 rounded-full transition shadow-lg shadow-rose-200">Book Appointment</button>
          </div>
          <div class="md:w-1/2 relative">
               <div class="absolute inset-0 bg-rose-200 rounded-full blur-3xl opacity-20 transform translate-x-12 translate-y-12"></div>
               <img src="https://images.unsplash.com/photo-1540555700478-4be289fbecef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" class="relative rounded-t-[10rem] rounded-b-[2rem] shadow-2xl w-full max-w-md mx-auto" alt="Spa Treatment">
          </div>
      </div>
      <div class="bg-white py-24">
          <div class="container mx-auto px-6 text-center max-w-4xl">
              <h2 class="text-3xl font-serif text-stone-800 mb-16">Our Signature Treatments</h2>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
                   <div>
                       <div class="w-16 h-16 bg-rose-50 rounded-full mx-auto flex items-center justify-center text-rose-400 mb-6">
                           <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                       </div>
                       <h3 class="text-xl font-medium text-stone-800 mb-3">Facial Glow</h3>
                       <p class="text-stone-500">Deep cleansing and hydration for radiant skin.</p>
                   </div>
                    <div>
                       <div class="w-16 h-16 bg-rose-50 rounded-full mx-auto flex items-center justify-center text-rose-400 mb-6">
                          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                       </div>
                       <h3 class="text-xl font-medium text-stone-800 mb-3">Aroma Massage</h3>
                       <p class="text-stone-500">Relaxing full body massage with essential oils.</p>
                   </div>
                    <div>
                         <div class="w-16 h-16 bg-rose-50 rounded-full mx-auto flex items-center justify-center text-rose-400 mb-6">
                           <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
                       </div>
                       <h3 class="text-xl font-medium text-stone-800 mb-3">Hot Stone</h3>
                       <p class="text-stone-500">Therapeutic heat to melt away muscle tension.</p>
                   </div>
              </div>
          </div>
      </div>
    </div>"""
    }
]


TEMPLATES_LANDING_PART_3 = [
    {
        "id": "landing-021",
        "title": "Construction Industrial",
        "description": "Heavy industry and construction services landing.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
      <div class="relative bg-gray-900">
         <div class="absolute inset-0">
             <img class="h-full w-full object-cover opacity-30" src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" alt="Construction Site">
         </div>
         <div class="relative max-w-7xl mx-auto px-6 py-32 sm:py-48 flex flex-col items-start">
             <span class="text-yellow-500 font-bold tracking-wider uppercase mb-4">Building the Future</span>
             <h1 class="text-5xl md:text-7xl font-black text-white mb-8 border-l-8 border-yellow-500 pl-8">Solid Foundations<br>Expert Construction</h1>
             <p class="text-xl text-gray-300 max-w-xl mb-12">We deliver high-quality industrial, commercial, and residential projects on time and within budget.</p>
             <button class="bg-yellow-500 hover:bg-yellow-400 text-gray-900 font-bold py-4 px-10 rounded">Request a Quote</button>
         </div>
      </div>
      <div class="py-24 bg-gray-100">
          <div class="container mx-auto px-6">
              <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                  <div class="bg-white p-8 shadow-md border-b-4 border-yellow-500">
                      <h3 class="text-xl font-bold mb-4">General Contracting</h3>
                      <p class="text-gray-600">Complete project management from start to finish.</p>
                  </div>
                   <div class="bg-white p-8 shadow-md border-b-4 border-yellow-500">
                      <h3 class="text-xl font-bold mb-4">Pre-Construction</h3>
                      <p class="text-gray-600">Planning, estimating, and feasibility studies.</p>
                  </div>
                   <div class="bg-white p-8 shadow-md border-b-4 border-yellow-500">
                      <h3 class="text-xl font-bold mb-4">Design-Build</h3>
                      <p class="text-gray-600">Unified workflow for design and construction.</p>
                  </div>
                   <div class="bg-white p-8 shadow-md border-b-4 border-yellow-500">
                      <h3 class="text-xl font-bold mb-4">Renovations</h3>
                      <p class="text-gray-600">Modernizing and upgrading existing structures.</p>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-022",
        "title": "Automotive Car Dealer",
        "description": "Sleek car dealership or rental landing.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-black text-white">
      <div class="relative h-screen flex items-center">
          <div class="absolute inset-0 z-0">
               <img src="https://images.unsplash.com/photo-1503376763036-066120622c74?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-full object-cover opacity-60" alt="Sports Car">
               <div class="absolute inset-0 bg-gradient-to-r from-black via-black/50 to-transparent"></div>
          </div>
          <div class="relative z-10 px-6 max-w-7xl mx-auto w-full">
              <h1 class="text-6xl md:text-8xl font-black italic tracking-tighter mb-4">SPEED<br>REDEFINED</h1>
              <p class="text-2xl text-gray-300 max-w-lg mb-12">Experience the thrill of the open road with our premium selection of sports and luxury vehicles.</p>
              <div class="flex gap-6">
                  <button class="bg-red-600 hover:bg-red-700 text-white px-8 py-3 rounded-full font-bold transition">View Inventory</button>
                  <button class="border border-white hover:bg-white hover:text-black text-white px-8 py-3 rounded-full font-bold transition">Book Test Drive</button>
              </div>
          </div>
      </div>
      <div class="bg-zinc-900 py-24">
          <div class="max-w-7xl mx-auto px-6">
              <div class="flex justify-between items-end mb-12">
                   <h2 class="text-4xl font-bold">Featured Models</h2>
                   <a href="#" class="text-red-500 font-bold hover:underline">View All &rarr;</a>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                  <div class="bg-zinc-800 rounded-xl overflow-hidden group cursor-pointer hover:shadow-2xl hover:shadow-red-900/20 transition">
                      <div class="aspect-[16/9] overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1542282088-fe8426682b8f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" alt="Audi">
                      </div>
                      <div class="p-6">
                          <h3 class="text-2xl font-bold mb-2">Audi RS5</h3>
                          <div class="flex justify-between items-center text-gray-400 text-sm mb-4">
                              <span>2023</span>
                              <span>•</span>
                              <span>Automatic</span>
                              <span>•</span>
                              <span>Petrol</span>
                          </div>
                           <div class="flex justify-between items-center">
                              <span class="text-xl font-bold text-white">$85,000</span>
                              <span class="text-red-500 font-bold text-sm">Details</span>
                          </div>
                      </div>
                  </div>
                   <div class="bg-zinc-800 rounded-xl overflow-hidden group cursor-pointer hover:shadow-2xl hover:shadow-red-900/20 transition">
                      <div class="aspect-[16/9] overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1555215695-3004980adade?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" alt="BMW">
                      </div>
                      <div class="p-6">
                          <h3 class="text-2xl font-bold mb-2">BMW M4</h3>
                          <div class="flex justify-between items-center text-gray-400 text-sm mb-4">
                              <span>2024</span>
                              <span>•</span>
                              <span>Automatic</span>
                              <span>•</span>
                              <span>Petrol</span>
                          </div>
                           <div class="flex justify-between items-center">
                              <span class="text-xl font-bold text-white">$92,000</span>
                              <span class="text-red-500 font-bold text-sm">Details</span>
                          </div>
                      </div>
                  </div>
                   <div class="bg-zinc-800 rounded-xl overflow-hidden group cursor-pointer hover:shadow-2xl hover:shadow-red-900/20 transition">
                      <div class="aspect-[16/9] overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1617788138017-80ad40651399?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" alt="Porsche">
                      </div>
                      <div class="p-6">
                          <h3 class="text-2xl font-bold mb-2">Porsche 911</h3>
                          <div class="flex justify-between items-center text-gray-400 text-sm mb-4">
                              <span>2022</span>
                              <span>•</span>
                              <span>Manual</span>
                              <span>•</span>
                              <span>Petrol</span>
                          </div>
                           <div class="flex justify-between items-center">
                              <span class="text-xl font-bold text-white">$145,000</span>
                              <span class="text-red-500 font-bold text-sm">Details</span>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-023",
        "title": "Pet Care Services",
        "description": "Friendly landing page for pet grooming or walking.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-yellow-50">
      <div class="container mx-auto px-6 py-24 flex flex-col md:flex-row items-center">
          <div class="md:w-1/2 mb-12 md:mb-0">
               <span class="bg-orange-100 text-orange-600 px-3 py-1 rounded-full font-bold text-xs uppercase tracking-wider mb-4 inline-block">Professional Pet Care</span>
               <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">We treat your furry friends like <span class="text-orange-500">family</span>.</h1>
               <p class="text-xl text-gray-600 mb-8">Award-winning grooming, walking, and sitting services. Trusted by over 500 pet owners in the city.</p>
               <button class="bg-orange-500 text-white font-bold py-4 px-8 rounded-xl shadow-lg hover:bg-orange-600 transition transform hover:-translate-y-1">Schedule a Visit</button>
          </div>
          <div class="md:w-1/2 flex justify-center">
              <div class="relative">
                  <div class="absolute inset-0 bg-orange-200 rounded-full blur-2xl transform translate-x-4 translate-y-4"></div>
                  <img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="relative rounded-3xl z-10 w-96 rotate-3 border-8 border-white shadow-xl" alt="Happy Dog">
              </div>
          </div>
      </div>
      <div class="bg-white py-24">
          <div class="container mx-auto px-6">
             <div class="text-center max-w-2xl mx-auto mb-16">
                 <h2 class="text-3xl font-bold text-gray-900 mb-4">Our Services</h2>
                 <p class="text-gray-600">Tail-wagging goodness guaranteed.</p>
             </div>
             <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                  <div class="bg-orange-50 rounded-2xl p-8 hover:bg-orange-100 transition">
                      <div class="text-4xl mb-4">✂️</div>
                      <h3 class="text-xl font-bold text-gray-900 mb-3">Grooming & Spa</h3>
                      <p class="text-gray-600">Full service grooming, baths, and styling.</p>
                  </div>
                   <div class="bg-blue-50 rounded-2xl p-8 hover:bg-blue-100 transition">
                      <div class="text-4xl mb-4">🦮</div>
                      <h3 class="text-xl font-bold text-gray-900 mb-3">Dog Walking</h3>
                      <p class="text-gray-600">Daily walks and exercise for active pups.</p>
                  </div>
                   <div class="bg-green-50 rounded-2xl p-8 hover:bg-green-100 transition">
                      <div class="text-4xl mb-4">🏠</div>
                      <h3 class="text-xl font-bold text-gray-900 mb-3">Pet Sitting</h3>
                      <p class="text-gray-600">In-home care when you're away.</p>
                  </div>
             </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-024",
        "title": "Photography Portfolio",
        "description": "Image-focused landing for photographers.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-black text-white">
       <nav class="flex justify-between items-center p-8 fixed w-full z-50 bg-gradient-to-b from-black/80 to-transparent">
           <div class="text-2xl font-bold tracking-widest uppercase">LUMOS</div>
           <div class="hidden md:flex gap-8 text-sm uppercase tracking-widest font-bold">
               <a href="#" class="hover:text-gray-400">Portfolio</a>
               <a href="#" class="hover:text-gray-400">About</a>
               <a href="#" class="hover:text-gray-400">Contact</a>
           </div>
           <div class="md:hidden">
               <button class="text-white">Menu</button>
           </div>
       </nav>
       <div class="snap-y snap-mandatory h-screen overflow-y-scroll scroll-smooth">
           <section class="snap-start w-full h-screen relative flex items-center justify-center">
               <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="absolute inset-0 w-full h-full object-cover opacity-60" alt="">
               <div class="relative z-10 text-center">
                   <h1 class="text-6xl md:text-9xl font-bold mb-4">CAPTURING<br>LIGHT</h1>
                   <p class="text-xl uppercase tracking-widest">Portrait & Landscape Photography</p>
               </div>
           </section>
            <section class="snap-start w-full h-screen relative flex items-center justify-center">
               <img src="https://images.unsplash.com/photo-1469334031218-e382a71b716b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="absolute inset-0 w-full h-full object-cover opacity-60" alt="">
               <div class="relative z-10 p-12 bg-black/50 backdrop-blur-md max-w-2xl text-center">
                   <h2 class="text-4xl font-bold mb-4">Fashion</h2>
                   <p class="text-gray-300">Editorial and commercial shoots that tell a story.</p>
               </div>
           </section>
            <section class="snap-start w-full h-screen relative flex items-center justify-center bg-zinc-900">
               <div class="container mx-auto px-6 text-center">
                   <h2 class="text-4xl font-bold mb-12">Latest Work</h2>
                   <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                       <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="aspect-[2/3] object-cover hover:opacity-80 transition cursor-pointer" alt="">
                       <img src="https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="aspect-[2/3] object-cover hover:opacity-80 transition cursor-pointer" alt="">
                       <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="aspect-[2/3] object-cover hover:opacity-80 transition cursor-pointer" alt="">
                        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="aspect-[2/3] object-cover hover:opacity-80 transition cursor-pointer" alt="">
                   </div>
               </div>
           </section>
       </div>
    </div>"""
    },
    {
        "id": "landing-025",
        "title": "Podcast Home",
        "description": "Landing page for a podcast series.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-purple-900 text-white min-h-screen">
      <div class="container mx-auto px-6 py-24 md:py-32 flex flex-col md:flex-row items-center gap-12">
          <div class="md:w-1/2">
               <div class="w-20 h-1 bg-purple-400 mb-8"></div>
               <h1 class="text-5xl md:text-7xl font-bold leading-tight mb-8">The Future<br>Is Now.</h1>
               <p class="text-xl text-purple-200 mb-8 leading-relaxed max-w-lg">Conversations with the innovators, dreamers, and builders shaping our world. Hosted by Sarah Connor.</p>
               <div class="flex flex-col sm:flex-row gap-4 mb-12">
                   <button class="bg-white text-purple-900 px-8 py-3 rounded-full font-bold hover:bg-purple-100 transition flex items-center justify-center gap-2">
                       <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" /></svg>
                       Listen to Latest Episode
                   </button>
                    <button class="border border-purple-400 text-purple-200 px-8 py-3 rounded-full font-bold hover:bg-purple-800 transition">Subscribe</button>
               </div>
               <div class="flex gap-6 items-center">
                   <p class="text-sm font-bold uppercase tracking-wider text-purple-400">Available on</p>
                   <div class="flex gap-4 opacity-70">
                        <div class="w-8 h-8 bg-white rounded-full"></div>
                        <div class="w-8 h-8 bg-white rounded-full"></div>
                        <div class="w-8 h-8 bg-white rounded-full"></div>
                   </div>
               </div>
          </div>
          <div class="md:w-1/2 flex justify-center relative">
              <div class="absolute inset-0 bg-purple-500 rounded-full blur-[100px] opacity-30"></div>
              <img src="https://images.unsplash.com/photo-1590602847861-f357a9332bbc?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="relative z-10 rounded-2xl shadow-2xl w-full max-w-md border-gray-800 border-4" alt="Microphone">
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-026",
        "title": "Job Board Hero",
        "description": "Simple hero section for a job board.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gray-50 min-h-[600px] flex flex-col items-center justify-center text-center px-6 py-24">
        <h1 class="text-4xl md:text-6xl font-black text-gray-900 mb-6 max-w-4xl">Find your next <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">dream job</span> today.</h1>
        <p class="text-xl text-gray-600 mb-10 max-w-2xl">Connect with thousands of top companies hiring for remote, hybrid, and onsite roles.</p>

        <div class="bg-white p-4 rounded-xl shadow-lg w-full max-w-3xl flex flex-col md:flex-row gap-4 border border-gray-200">
             <div class="flex-1 relative">
                 <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                     <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                 </div>
                 <input type="text" placeholder="Job title, keywords, or company" class="pl-10 block w-full rounded-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 h-12 bg-gray-50 border-0">
             </div>
              <div class="flex-1 relative">
                 <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                     <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
                 </div>
                 <input type="text" placeholder="City, state, or zip code" class="pl-10 block w-full rounded-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 h-12 bg-gray-50 border-0">
             </div>
             <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-8 rounded-lg transition">Search</button>
        </div>

        <div class="mt-12 flex flex-wrap justify-center gap-4 text-sm text-gray-500">
            <span class="font-semibold text-gray-900">Popular:</span>
            <a href="#" class="hover:text-indigo-600">Remote</a>
            <span>•</span>
            <a href="#" class="hover:text-indigo-600">Software Engineer</a>
            <span>•</span>
            <a href="#" class="hover:text-indigo-600">Product Manager</a>
            <span>•</span>
             <a href="#" class="hover:text-indigo-600">Designer</a>
        </div>
    </div>"""
    },
    {
        "id": "landing-027",
        "title": "Marketplace Hero",
        "description": "Multi-category marketplace landing entry.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
       <nav class="border-b border-gray-100 p-4">
           <div class="container mx-auto flex justify-between items-center">
               <div class="text-2xl font-bold text-red-500">Market.</div>
               <div class="hidden md:flex gap-6 text-gray-600">
                   <a href="#" class="hover:text-gray-900">Sell</a>
                   <a href="#" class="hover:text-gray-900">Categories</a>
                   <a href="#" class="hover:text-gray-900">Community</a>
               </div>
               <div class="flex gap-4">
                   <button class="text-gray-900 font-bold">Log in</button>
                   <button class="bg-red-500 text-white px-4 py-2 rounded font-bold">Sign up</button>
               </div>
           </div>
       </nav>
       <div class="container mx-auto px-6 py-16">
           <div class="bg-red-50 rounded-3xl p-12 md:p-24 flex flex-col md:flex-row items-center justify-between">
               <div class="md:w-1/2 mb-12 md:mb-0">
                   <h1 class="text-5xl font-bold text-gray-900 mb-6">Buy & Sell<br>Anything, Anywhere.</h1>
                   <p class="text-xl text-gray-600 mb-8">The most trusted marketplace for vintage finds, handmade goods, and unique collectibles.</p>
                   <button class="bg-red-500 text-white px-8 py-3 rounded-full font-bold text-lg hover:bg-red-600 transition">Explore Collection</button>
               </div>
               <div class="md:w-1/2 grid grid-cols-2 gap-4">
                   <img src="https://images.unsplash.com/photo-1550989460-0adf9ea622e2?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="rounded-xl transform translate-y-8" alt="">
                   <img src="https://images.unsplash.com/photo-1595341888016-a392ef81b7de?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="rounded-xl" alt="">
               </div>
           </div>

           <div class="mt-24">
               <h2 class="text-2xl font-bold mb-8">Browse Categories</h2>
               <div class="grid grid-cols-2 md:grid-cols-6 gap-6">
                   <a href="#" class="flex flex-col items-center group">
                       <div class="w-full aspect-square bg-gray-100 rounded-xl mb-3 overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1441986300917-64674bd600d8?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover group-hover:scale-110 transition" alt="">
                       </div>
                       <span class="font-medium text-gray-900">Fashion</span>
                   </a>
                    <a href="#" class="flex flex-col items-center group">
                       <div class="w-full aspect-square bg-gray-100 rounded-xl mb-3 overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover group-hover:scale-110 transition" alt="">
                       </div>
                       <span class="font-medium text-gray-900">Electronics</span>
                   </a>
                   <a href="#" class="flex flex-col items-center group">
                       <div class="w-full aspect-square bg-gray-100 rounded-xl mb-3 overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4f9d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover group-hover:scale-110 transition" alt="">
                       </div>
                       <span class="font-medium text-gray-900">Home</span>
                   </a>
                   <a href="#" class="flex flex-col items-center group">
                       <div class="w-full aspect-square bg-gray-100 rounded-xl mb-3 overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1607513138275-1a610427a1a4?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover group-hover:scale-110 transition" alt="">
                       </div>
                       <span class="font-medium text-gray-900">Art</span>
                   </a>
                    <a href="#" class="flex flex-col items-center group">
                       <div class="w-full aspect-square bg-gray-100 rounded-xl mb-3 overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover group-hover:scale-110 transition" alt="">
                       </div>
                       <span class="font-medium text-gray-900">Gaming</span>
                   </a>
                    <a href="#" class="flex flex-col items-center group">
                       <div class="w-full aspect-square bg-gray-100 rounded-xl mb-3 overflow-hidden">
                           <img src="https://images.unsplash.com/photo-1592819695396-064b9572a660?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" class="w-full h-full object-cover group-hover:scale-110 transition" alt="">
                       </div>
                       <span class="font-medium text-gray-900">Garden</span>
                   </a>
               </div>
           </div>
       </div>
    </div>"""
    },
    {
        "id": "landing-028",
        "title": "Social Network",
        "description": "Signup page for a new social app.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white min-h-screen flex items-center">
       <div class="container mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
           <div class="md:order-2">
               <img src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" class="rounded-3xl shadow-2xl rotate-2 hover:rotate-0 transition duration-500" alt="App interface">
           </div>
           <div class="md:order-1">
               <div class="text-blue-500 font-bold mb-4 flex items-center gap-2">
                   <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold">C</div>
                   Connect
               </div>
               <h1 class="text-5xl font-black text-gray-900 mb-6 tracking-tight">Real friends.<br>Real moments.</h1>
               <p class="text-xl text-gray-500 mb-10 max-w-md">No algorithms. No data mining. Just you and the people who matter most sharing your life.</p>

               <div class="space-y-4 max-w-sm">
                   <button class="w-full bg-blue-600 text-white font-bold py-4 rounded-xl hover:bg-blue-700 transition">Sign up with Phone</button>
                   <button class="w-full bg-gray-100 text-gray-900 font-bold py-4 rounded-xl hover:bg-gray-200 transition">Log in</button>
               </div>

               <div class="mt-8 flex items-center gap-4 text-xs font-bold text-gray-400 uppercase tracking-widest">
                   <span>Free Forever</span>
                   <span>•</span>
                   <span>No Ads</span>
                   <span>•</span>
                   <span>Private</span>
               </div>
           </div>
       </div>
    </div>"""
    },
    {
        "id": "landing-029",
        "title": "Dating App",
        "description": "Vibrant and playful dating app landing.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gradient-to-br from-pink-500 to-orange-400 min-h-screen">
      <nav class="p-6 flex justify-between items-center text-white">
          <div class="text-2xl font-bold">Spark</div>
          <button class="bg-white text-pink-500 px-6 py-2 rounded-full font-bold hover:bg-gray-100 transition">Login</button>
      </nav>
      <div class="container mx-auto px-6 py-24 flex flex-col items-center text-center text-white">
          <h1 class="text-6xl md:text-8xl font-black mb-8 leading-none">Find Your<br>Match.</h1>
          <p class="text-2xl font-medium mb-12 max-w-2xl opacity-90">Swipe right on destiny. Join the fastest growing dating community in the world.</p>
          <div class="bg-white p-2 rounded-full pl-6 pr-2 py-2 flex w-full max-w-md shadow-2xl mb-12">
              <input type="email" placeholder="Enter your email" class="flex-grow outline-none text-gray-900 placeholder:text-gray-400">
              <button class="bg-pink-500 text-white px-8 py-3 rounded-full font-bold hover:bg-pink-600 transition">Join Now</button>
          </div>

          <div class="flex flex-wrap justify-center gap-8 mt-12">
               <div class="w-16 h-16 rounded-full border-4 border-white overflow-hidden transform translate-y-4">
                  <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80" alt="">
               </div>
               <div class="w-20 h-20 rounded-full border-4 border-white overflow-hidden transform -translate-y-4">
                  <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80" alt="">
               </div>
               <div class="w-16 h-16 rounded-full border-4 border-white overflow-hidden transform translate-y-4">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80" alt="">
               </div>
          </div>
          <p class="mt-8 font-bold opacity-80">14,000+ Matches made today</p>
      </div>
    </div>"""
    },
    {
        "id": "landing-030",
        "title": "Music Band",
        "description": "Edgy band or musician profile page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-neutral-900 text-white min-h-screen font-mono">
       <div class="fixed inset-0 z-0 opacity-20">
            <img src="https://images.unsplash.com/photo-1501612780327-45045538702b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-full object-cover grayscale" alt="Concert">
       </div>
       <div class="relative z-10 flex flex-col items-center justify-center min-h-screen px-6 text-center">
           <div class="border-4 border-white p-8 md:p-12 mb-12 backdrop-blur-sm">
               <h1 class="text-6xl md:text-9xl font-black uppercase tracking-tighter leading-none mb-4">The<br>Drifters</h1>
               <p class="text-xl uppercase tracking-[0.5em]">World Tour 2024</p>
           </div>

           <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl w-full">
               <a href="#" class="bg-white text-black hover:bg-neutral-200 transition p-6 font-bold text-xl uppercase tracking-widest flex justify-between items-center group">
                   <span>Listen</span>
                   <span class="transform group-hover:translate-x-2 transition">&rarr;</span>
               </a>
               <a href="#" class="bg-transparent border border-white hover:bg-white hover:text-black transition p-6 font-bold text-xl uppercase tracking-widest flex justify-between items-center group">
                   <span>Tour Dates</span>
                   <span class="transform group-hover:translate-x-2 transition">&rarr;</span>
               </a>
                <a href="#" class="bg-transparent border border-white hover:bg-white hover:text-black transition p-6 font-bold text-xl uppercase tracking-widest flex justify-between items-center group">
                   <span>Merch</span>
                   <span class="transform group-hover:translate-x-2 transition">&rarr;</span>
               </a>
                <a href="#" class="bg-transparent border border-white hover:bg-white hover:text-black transition p-6 font-bold text-xl uppercase tracking-widest flex justify-between items-center group">
                   <span>Videos</span>
                   <span class="transform group-hover:translate-x-2 transition">&rarr;</span>
               </a>
           </div>
       </div>
    </div>"""
    }
]


TEMPLATES_LANDING_PART_4 = [
    {
        "id": "landing-031",
        "title": "Hotel Resort",
        "description": "Luxury hotel or resort landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-stone-50 font-serif">
      <div class="h-screen relative flex items-center justify-center text-center px-6">
          <img src="https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="absolute inset-0 w-full h-full object-cover brightness-75" alt="Resort Pool">
          <div class="relative z-10 text-white">
              <p class="uppercase tracking-[0.3em] mb-4 text-sm md:text-base">Sanctuary of Peace</p>
              <h1 class="text-5xl md:text-8xl font-medium mb-8 italic">The azure coast</h1>
              <button class="bg-white text-stone-900 px-8 py-4 uppercase tracking-widest text-sm hover:bg-stone-200 transition">Book Your Stay</button>
          </div>
      </div>
      <div class="container mx-auto px-6 py-24">
          <div class="text-center max-w-3xl mx-auto mb-16">
              <span class="text-stone-400 uppercase tracking-widest text-xs mb-4 block">Welcome</span>
              <h2 class="text-3xl md:text-4xl text-stone-800 mb-6 leading-relaxed">Experience unpretentious luxury in the heart of the Riviera. A place to disconnect and reconnect.</h2>
              <img src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80" class="w-full h-96 object-cover mt-12" alt="Hotel Room">
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
              <div class="p-8 bg-white shadow-sm border border-stone-100 text-center">
                  <h3 class="text-xl uppercase tracking-widest mb-4">Dining</h3>
                  <p class="text-stone-500 mb-6">Locally sourced ingredients, prepared with passion by Chef Marco Rossi.</p>
                  <a href="#" class="border-b border-stone-900 pb-1 uppercase text-xs tracking-widest hover:text-stone-600">View Menu</a>
              </div>
               <div class="p-8 bg-white shadow-sm border border-stone-100 text-center">
                  <h3 class="text-xl uppercase tracking-widest mb-4">Wellness</h3>
                  <p class="text-stone-500 mb-6">Rejuvenate your senses in our world-class spa and thermal pools.</p>
                  <a href="#" class="border-b border-stone-900 pb-1 uppercase text-xs tracking-widest hover:text-stone-600">Discover Spa</a>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-032",
        "title": "Conference Event",
        "description": "Information and registration for a conference.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-blue-900 text-white">
      <div class="container mx-auto px-6 py-24 flex flex-col items-center text-center">
          <div class="inline-block bg-blue-800 px-4 py-2 rounded-full font-bold text-sm mb-8 border border-blue-700">Oct 12-14, 2024 • San Francisco, CA</div>
          <h1 class="text-5xl md:text-8xl font-black mb-8 tracking-tighter">FUTURE<span class="text-blue-400">TECH</span><br>SUMMIT</h1>
          <p class="text-xl text-blue-200 max-w-2xl mb-12">Join the world's leading minds in AI, Blockchain, and Quantum Computing for 3 days of inspiration and networking.</p>
          <div class="flex flex-col sm:flex-row gap-4 mb-24">
              <button class="bg-blue-500 text-white px-10 py-4 rounded-lg font-bold text-lg hover:bg-blue-400 transition shadow-lg shadow-blue-500/50">Get Tickets</button>
              <button class="bg-transparent border border-blue-500 text-blue-200 px-10 py-4 rounded-lg font-bold text-lg hover:bg-blue-800 transition">View Agenda</button>
          </div>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-8 w-full max-w-5xl border-t border-blue-800 pt-12">
              <div class="text-center">
                  <h3 class="text-4xl font-bold mb-2">50+</h3>
                  <p class="text-blue-400 uppercase text-xs tracking-widest">Speakers</p>
              </div>
               <div class="text-center">
                  <h3 class="text-4xl font-bold mb-2">2000+</h3>
                  <p class="text-blue-400 uppercase text-xs tracking-widest">Attendees</p>
              </div>
               <div class="text-center">
                  <h3 class="text-4xl font-bold mb-2">30</h3>
                  <p class="text-blue-400 uppercase text-xs tracking-widest">Sessions</p>
              </div>
               <div class="text-center">
                  <h3 class="text-4xl font-bold mb-2">∞</h3>
                  <p class="text-blue-400 uppercase text-xs tracking-widest">Possibilities</p>
              </div>
          </div>
      </div>

      <div class="bg-white text-blue-900 py-24">
          <div class="container mx-auto px-6">
              <h2 class="text-3xl font-bold mb-12 text-center">Featured Speakers</h2>
              <div class="flex flex-wrap justify-center gap-12">
                   <div class="flex flex-col items-center">
                       <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=200&h=200&q=80" class="w-32 h-32 rounded-full mb-4 grayscale hover:grayscale-0 transition duration-300" alt="">
                       <h4 class="font-bold text-lg">Jane Doe</h4>
                       <p class="text-gray-500 text-sm">CEO, TechCorp</p>
                   </div>
                   <div class="flex flex-col items-center">
                       <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=200&h=200&q=80" class="w-32 h-32 rounded-full mb-4 grayscale hover:grayscale-0 transition duration-300" alt="">
                       <h4 class="font-bold text-lg">John Smith</h4>
                       <p class="text-gray-500 text-sm">CTO, Innovate</p>
                   </div>
                    <div class="flex flex-col items-center">
                       <img src="https://images.unsplash.com/photo-1628157588553-6536b05691d6?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=200&h=200&q=80" class="w-32 h-32 rounded-full mb-4 grayscale hover:grayscale-0 transition duration-300" alt="">
                       <h4 class="font-bold text-lg">Alice Wong</h4>
                       <p class="text-gray-500 text-sm">Founder, AI Labs</p>
                   </div>
              </div>
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-033",
        "title": "Web Hosting",
        "description": "Tech-focused hosting provider landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-slate-900 text-white">
       <nav class="container mx-auto px-6 py-6 flex justify-between items-center">
           <div class="text-2xl font-bold text-cyan-400">HostPro</div>
           <div class="flex gap-4">
               <button class="text-slate-300 hover:text-white">Login</button>
               <button class="bg-cyan-500 text-white px-4 py-2 rounded font-bold hover:bg-cyan-600">Get Started</button>
           </div>
       </nav>
       <div class="container mx-auto px-6 py-20 text-center">
           <h1 class="text-5xl md:text-6xl font-bold mb-6">Blazing Fast Cloud Hosting</h1>
           <p class="text-xl text-slate-400 max-w-2xl mx-auto mb-12">Deploy your projects in seconds with our globally distributed infrastructure. 99.9% Uptime Guaranteed.</p>

           <div class="flex justify-center gap-8 mb-20">
               <div class="bg-slate-800 p-8 rounded-xl border border-slate-700 w-full max-w-xs hover:border-cyan-500 transition shadow-lg relative">
                   <h3 class="text-xl font-bold mb-2">Starter</h3>
                   <div class="text-4xl font-bold mb-4">$5<span class="text-sm font-normal text-slate-400">/mo</span></div>
                   <ul class="text-left text-slate-400 space-y-3 mb-8 text-sm">
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 1 Website</li>
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 10 GB Storage</li>
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Free SSL</li>
                   </ul>
                   <button class="w-full bg-slate-700 hover:bg-slate-600 py-3 rounded-lg font-bold">Choose Plan</button>
               </div>

               <div class="bg-slate-800 p-8 rounded-xl border-2 border-cyan-500 w-full max-w-xs shadow-2xl shadow-cyan-500/10 transform scale-105 relative z-10">
                   <div class="absolute top-0 right-0 bg-cyan-500 text-xs font-bold px-2 py-1 rounded-bl-lg rounded-tr-lg">POPULAR</div>
                   <h3 class="text-xl font-bold mb-2 text-cyan-400">Pro</h3>
                   <div class="text-4xl font-bold mb-4">$15<span class="text-sm font-normal text-slate-400">/mo</span></div>
                    <ul class="text-left text-slate-400 space-y-3 mb-8 text-sm">
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited Websites</li>
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> 50 GB NVMe Storage</li>
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Free Domain</li>
                   </ul>
                   <button class="w-full bg-cyan-500 hover:bg-cyan-600 py-3 rounded-lg font-bold">Choose Plan</button>
               </div>

               <div class="bg-slate-800 p-8 rounded-xl border border-slate-700 w-full max-w-xs hover:border-cyan-500 transition shadow-lg relative">
                   <h3 class="text-xl font-bold mb-2">Business</h3>
                   <div class="text-4xl font-bold mb-4">$49<span class="text-sm font-normal text-slate-400">/mo</span></div>
                   <ul class="text-left text-slate-400 space-y-3 mb-8 text-sm">
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Dedicated IP</li>
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Unlimited Storage</li>
                       <li class="flex items-center gap-2"><svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Priority Support</li>
                   </ul>
                   <button class="w-full bg-slate-700 hover:bg-slate-600 py-3 rounded-lg font-bold">Choose Plan</button>
               </div>
           </div>
       </div>
    </div>"""
    },
    {
        "id": "landing-034",
        "title": "Mobile App Dark",
        "description": "Dark themed mobile app showcase.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-black text-white min-h-screen overflow-hidden relative">
      <!-- Background Shapes -->
      <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-900 rounded-full filter blur-[100px] opacity-30 select-none"></div>
      <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-indigo-900 rounded-full filter blur-[100px] opacity-30 select-none"></div>

      <div class="container mx-auto px-6 py-24 flex flex-col items-center relative z-10">
          <div class="inline-flex items-center gap-2 border border-white/20 rounded-full px-4 py-1 mb-8 backdrop-blur-md">
              <span class="w-2 h-2 rounded-full bg-green-500"></span>
              <span class="text-sm font-medium text-gray-300">v2.0 is now live</span>
          </div>

          <h1 class="text-5xl md:text-7xl font-bold text-center mb-8 bg-clip-text text-transparent bg-gradient-to-br from-white to-gray-500">Master Your<br>Workflow.</h1>
          <p class="text-xl text-gray-400 text-center max-w-xl mb-12">The ultimate productivity tool designed for creative professionals. Focus on what matters, automate the rest.</p>

          <div class="flex gap-4 mb-20">
              <button class="bg-white text-black px-8 py-3 rounded-full font-bold hover:bg-gray-200 transition">Download for iOS</button>
              <button class="bg-white/10 border border-white/20 text-white px-8 py-3 rounded-full font-bold hover:bg-white/20 transition backdrop-blur-md">Android</button>
          </div>

          <div class="relative w-full max-w-sm mx-auto">
              <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent z-20 h-40 bottom-0 top-auto"></div>
               <img src="https://images.unsplash.com/photo-1618418386448-f42be2897c9b?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" class="rounded-[2.5rem] border-8 border-gray-900 shadow-2xl mx-auto" alt="App Screen">
          </div>
      </div>
    </div>"""
    },
    {
        "id": "landing-035",
        "title": "SASS Product Dark",
        "description": "B2B SaaS landing page in dark mode.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-gray-900 text-white font-sans">
       <nav class="flex justify-between items-center p-6 container mx-auto">
           <div class="font-bold text-xl tracking-tight">Struct<span class="text-blue-500">.io</span></div>
           <div class="hidden md:flex gap-8 text-sm font-medium text-gray-400">
               <a href="#" class="hover:text-white transition">Product</a>
               <a href="#" class="hover:text-white transition">Solutions</a>
               <a href="#" class="hover:text-white transition">Pricing</a>
           </div>
           <button class="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2 rounded-lg font-medium transition">Get Started</button>
       </nav>

       <div class="container mx-auto px-6 py-24 text-center">
           <h1 class="text-5xl md:text-7xl font-bold mb-8 leading-tight">Data infrastructure<br>for everyone.</h1>
           <p class="text-xl text-gray-400 max-w-2xl mx-auto mb-12">Unified analytics, observability, and data management platform. Scale your insights without scaling your team.</p>

           <div class="flex justify-center gap-4 mb-16">
               <input type="email" placeholder="work@email.com" class="bg-gray-800 border border-gray-700 text-white px-6 py-3 rounded-lg w-80 focus:outline-none focus:border-blue-500">
               <button class="bg-blue-600 hover:bg-blue-500 text-white px-8 py-3 rounded-lg font-medium transition">Start Free Trial</button>
           </div>

           <div class="border border-gray-800 rounded-xl overflow-hidden shadow-2xl bg-gray-800 max-w-5xl mx-auto">
                <div class="flex items-center gap-2 px-4 py-3 bg-gray-800 border-b border-gray-700">
                    <div class="w-3 h-3 rounded-full bg-red-500"></div>
                    <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                    <div class="w-3 h-3 rounded-full bg-green-500"></div>
                </div>
                <div class="p-8">
                     <!-- Abstract Dashboard UI Mockup -->
                     <div class="grid grid-cols-3 gap-6 mb-6">
                         <div class="bg-gray-900 h-32 rounded-lg animate-pulse"></div>
                         <div class="bg-gray-900 h-32 rounded-lg animate-pulse"></div>
                         <div class="bg-gray-900 h-32 rounded-lg animate-pulse"></div>
                     </div>
                     <div class="bg-gray-900 h-64 rounded-lg animate-pulse"></div>
                </div>
           </div>

           <div class="mt-24 grid grid-cols-2 md:grid-cols-5 gap-8 opacity-50 grayscale">
               <!-- Partner Logos -->
               <div class="font-bold text-2xl">ACME Corp</div>
               <div class="font-bold text-2xl">GlobalTech</div>
               <div class="font-bold text-2xl">Nebula</div>
               <div class="font-bold text-2xl">FoxRun</div>
               <div class="font-bold text-2xl">Circle</div>
           </div>
       </div>
    </div>"""
    },
    {
        "id": "landing-036",
        "title": "Influencer Media Kit",
        "description": "Profile page for social media influencers.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
       <div class="container mx-auto px-6 py-12 flex flex-col md:flex-row gap-12">
           <div class="md:w-1/3">
               <div class="sticky top-12">
                   <div class="rounded-2xl overflow-hidden mb-6">
                       <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full object-cover" alt="Profile">
                   </div>
                   <h1 class="text-3xl font-bold mb-2">Sarah Jenkins</h1>
                   <p class="text-gray-500 mb-6">Lifestyle & Travel Creator</p>
                   <p class="text-gray-600 mb-8 leading-relaxed">Sharing my journey exploring the hidden gems of the world. Passionate about sustainable travel and authentic experiences.</p>

                   <div class="flex gap-4">
                       <a href="#" class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center hover:bg-gray-200 transition">IG</a>
                       <a href="#" class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center hover:bg-gray-200 transition">YT</a>
                       <a href="#" class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center hover:bg-gray-200 transition">TK</a>
                   </div>

                   <button class="mt-8 w-full bg-black text-white font-bold py-3 rounded-lg hover:bg-gray-800 transition">Contact Me</button>
               </div>
           </div>
           <div class="md:w-2/3">
               <div class="grid grid-cols-2 gap-6 mb-12">
                   <div class="bg-pink-50 p-6 rounded-2xl text-center">
                       <h3 class="text-4xl font-bold text-pink-600 mb-1">250K+</h3>
                       <p class="text-gray-600 text-sm font-bold uppercase">Followers</p>
                   </div>
                    <div class="bg-purple-50 p-6 rounded-2xl text-center">
                       <h3 class="text-4xl font-bold text-purple-600 mb-1">4.8%</h3>
                       <p class="text-gray-600 text-sm font-bold uppercase">Engagement Rate</p>
                   </div>
               </div>

               <h2 class="text-2xl font-bold mb-6">Recent Collaborations</h2>
               <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                   <div class="bg-gray-50 rounded-xl p-4 flex items-center gap-4">
                       <div class="w-16 h-16 bg-white rounded-lg flex items-center justify-center font-bold text-gray-400">LOGO</div>
                       <div>
                           <h4 class="font-bold">Organic Co.</h4>
                           <p class="text-sm text-gray-500">Brand Ambassador</p>
                       </div>
                   </div>
                    <div class="bg-gray-50 rounded-xl p-4 flex items-center gap-4">
                       <div class="w-16 h-16 bg-white rounded-lg flex items-center justify-center font-bold text-gray-400">LOGO</div>
                       <div>
                           <h4 class="font-bold">TravelAway</h4>
                           <p class="text-sm text-gray-500">Sponsored Trip</p>
                       </div>
                   </div>
               </div>

               <h2 class="text-2xl font-bold mb-6">Audience Demographics</h2>
               <div class="bg-gray-50 p-6 rounded-2xl">
                   <div class="mb-4">
                       <div class="flex justify-between text-sm font-bold mb-1">
                           <span>Age 18-24</span>
                           <span>45%</span>
                       </div>
                       <div class="w-full bg-gray-200 rounded-full h-2">
                           <div class="bg-black h-2 rounded-full" style="width: 45%"></div>
                       </div>
                   </div>
                    <div class="mb-4">
                       <div class="flex justify-between text-sm font-bold mb-1">
                           <span>Age 25-34</span>
                           <span>30%</span>
                       </div>
                       <div class="w-full bg-gray-200 rounded-full h-2">
                           <div class="bg-black h-2 rounded-full" style="width: 30%"></div>
                       </div>
                   </div>
                    <div>
                       <div class="flex justify-between text-sm font-bold mb-1">
                           <span>Female</span>
                           <span>70%</span>
                       </div>
                       <div class="w-full bg-gray-200 rounded-full h-2">
                           <div class="bg-pink-400 h-2 rounded-full" style="width: 70%"></div>
                       </div>
                   </div>
               </div>
           </div>
       </div>
    </div>"""
    },
    {
        "id": "landing-037",
        "title": "eBook Author",
        "description": "Landing page for selling an eBook.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-amber-50">
       <div class="container mx-auto px-6 py-24 flex flex-col md:flex-row items-center gap-16">
           <div class="md:w-1/2 flex justify-center">
               <div class="relative w-64 md:w-80 aspect-[2/3] bg-white shadow-2xl skew-y-3 transform rotate-3 border border-gray-100 flex items-center justify-center text-center p-8">
                   <div class="border-4 border-amber-900 h-full w-full flex flex-col justify-center items-center p-4">
                        <h2 class="text-3xl font-serif font-bold text-amber-900 mb-2">The Art of<br>Simplicity</h2>
                        <div class="w-12 h-1 bg-amber-900 my-4"></div>
                        <p class="text-sm font-sans uppercase tracking-widest text-amber-700">James Clear</p>
                   </div>
               </div>
           </div>
           <div class="md:w-1/2">
               <h1 class="text-4xl md:text-5xl font-serif font-bold text-amber-900 mb-6">Master the habit of doing less, better.</h1>
               <p class="text-xl text-amber-800 mb-8 leading-relaxed">A comprehensive guide to decluttering your mind, your schedule, and your life. Reclaim your time and energy for what truly matters.</p>

               <ul class="space-y-4 mb-10">
                   <li class="flex items-center gap-3 text-amber-800">
                       <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                       Practical strategies for essentialism
                   </li>
                   <li class="flex items-center gap-3 text-amber-800">
                       <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                       Worksheets and templates included
                   </li>
                   <li class="flex items-center gap-3 text-amber-800">
                       <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                       Instant PDF & ePub download
                   </li>
               </ul>

               <div class="flex items-center gap-6">
                   <button class="bg-amber-600 text-white px-8 py-4 rounded font-bold hover:bg-amber-700 transition shadow-lg shadow-amber-600/30">Buy Now - $19</button>
                   <p class="text-sm text-amber-700 font-bold">100% Money-back guarantee</p>
               </div>
           </div>
       </div>
    </div>"""
    },
    {
        "id": "landing-038",
        "title": "Online Course",
        "description": "Hero section for an online course.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-indigo-900 text-white overflow-hidden">
        <div class="container mx-auto px-6 py-24 relative">
            <div class="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-indigo-600 rounded-full mix-blend-multiply filter blur-3xl opacity-50"></div>
            <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 bg-purple-600 rounded-full mix-blend-multiply filter blur-3xl opacity-50"></div>

            <div class="relative z-10 max-w-4xl mx-auto text-center">
                <div class="inline-block bg-indigo-800 text-indigo-200 px-4 py-1 rounded-full text-sm font-bold mb-6 border border-indigo-700">Best Seller Course</div>
                <h1 class="text-5xl md:text-7xl font-bold mb-8 leading-tight">Become a Pro Designer<br>in 30 Days.</h1>
                <p class="text-xl text-indigo-200 mb-10 max-w-2xl mx-auto">Master Figma, UI principles, and the business of design. No prior experience required. Lifetime access.</p>

                <div class="flex flex-col sm:flex-row justify-center gap-4 mb-16">
                    <button class="bg-white text-indigo-900 px-8 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 transition">Start Learning for Free</button>
                    <div class="flex items-center gap-2 text-indigo-200 px-8 py-4">
                        <div class="flex -space-x-2">
                            <div class="w-8 h-8 rounded-full bg-gray-300 border-2 border-indigo-900"></div>
                            <div class="w-8 h-8 rounded-full bg-gray-300 border-2 border-indigo-900"></div>
                            <div class="w-8 h-8 rounded-full bg-gray-300 border-2 border-indigo-900"></div>
                        </div>
                        <span class="text-sm font-bold">Joined by 10k+ students</span>
                    </div>
                </div>

                <div class="bg-indigo-800/50 backdrop-blur-md rounded-xl p-8 border border-indigo-700 flex flex-wrap justify-between gap-8 text-left">
                     <div>
                         <div class="text-3xl font-bold mb-1">12</div>
                         <div class="text-indigo-300 text-sm font-bold uppercase">Modules</div>
                     </div>
                     <div>
                         <div class="text-3xl font-bold mb-1">24h</div>
                         <div class="text-indigo-300 text-sm font-bold uppercase">Video Content</div>
                     </div>
                     <div>
                         <div class="text-3xl font-bold mb-1">5</div>
                         <div class="text-indigo-300 text-sm font-bold uppercase">Real Projects</div>
                     </div>
                     <div>
                         <div class="text-3xl font-bold mb-1">Cert</div>
                         <div class="text-indigo-300 text-sm font-bold uppercase">Included</div>
                     </div>
                </div>
            </div>
        </div>
    </div>"""
    },
    {
        "id": "landing-039",
        "title": "Consulting Agency",
        "description": "Professional services landing page.",
        "dir": "templates/20-landing-pages",
        "content": """
    <div class="bg-white">
       <div class="container mx-auto px-6 py-24">
           <div class="max-w-4xl">
               <h1 class="text-5xl md:text-7xl font-bold text-slate-900 mb-8 leading-tight">We help businesses <span class="text-blue-600">navigate change</span> and <span class="text-blue-600">unlock growth</span>.</h1>
               <p class="text-xl text-slate-600 mb-12 max-w-2xl leading-relaxed">Strategic consulting for the digital age. We partner with leaders to build the organizations of tomorrow.</p>
               <div class="flex gap-6">
                   <button class="bg-slate-900 text-white px-8 py-4 font-bold rounded-lg hover:bg-slate-800 transition">Work With Us</button>
                   <button class="text-slate-900 font-bold px-4 py-4 hover:text-blue-600 transition flex items-center gap-2">
                       View Case Studies
                       <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
                   </button>
               </div>
           </div>

           <div class="mt-24 grid grid-cols-1 md:grid-cols-3 gap-8 border-t border-gray-100 pt-16">
               <div>
                   <div class="w-12 h-12 bg-blue-50 rounded-lg flex items-center justify-center text-blue-600 mb-6">
                       <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                   </div>
                   <h3 class="text-xl font-bold text-slate-900 mb-4">Strategy & Innovation</h3>
                   <p class="text-slate-600">Identify new opportunities and build resilient business models.</p>
               </div>
               <div>
                   <div class="w-12 h-12 bg-blue-50 rounded-lg flex items-center justify-center text-blue-600 mb-6">
                       <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                   </div>
                   <h3 class="text-xl font-bold text-slate-900 mb-4">Digital Transformation</h3>
                   <p class="text-slate-600">Modernize your tech stack and optimize operations.</p>
               </div>
                <div>
                   <div class="w-12 h-12 bg-blue-50 rounded-lg flex items-center justify-center text-blue-600 mb-6">
                       <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
                   </div>
                   <h3 class="text-xl font-bold text-slate-900 mb-4">Organizational Culture</h3>
                   <p class="text-slate-600">Attract talent and foster a culture of excellence.</p>
               </div>
           </div>
       </div>
    </div>"""
    }
]

TEMPLATES_LANDING_NEW.extend(TEMPLATES_LANDING_PART_4)



