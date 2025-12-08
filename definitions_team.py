TEMPLATES_TEAM_NEW = [
    {
        "id": "team-013",
        "title": "Minimal Grid with Socials",
        "description": "Clean grid layout with social icons below name.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Our Team</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">We're a dynamic group of individuals who are passionate about what we do.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          <li>
            <img class="aspect-[3/2] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=800&h=800&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Michael Foster</h3>
            <p class="text-base leading-7 text-gray-600">Co-Founder / CTO</p>
            <ul role="list" class="mt-6 flex gap-x-6">
              <li><a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">Twitter</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a></li>
              <li><a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">LinkedIn</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763h2.674v-8.59H3.668v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg></a></li>
            </ul>
          </li>
          <!-- More people... -->
           <li>
            <img class="aspect-[3/2] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=800&h=800&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Lindsay Walton</h3>
            <p class="text-base leading-7 text-gray-600">Front-end Developer</p>
             <ul role="list" class="mt-6 flex gap-x-6">
              <li><a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">Twitter</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a></li>
            </ul>
          </li>
           <li>
            <img class="aspect-[3/2] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=800&h=800&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Courtney Henry</h3>
            <p class="text-base leading-7 text-gray-600">Designer</p>
             <ul role="list" class="mt-6 flex gap-x-6">
               <li><a href="#" class="text-gray-400 hover:text-gray-500"><span class="sr-only">LinkedIn</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763h2.674v-8.59H3.668v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg></a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-014",
        "title": "Large Round Avatars",
        "description": "Large circular avatars with text center.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl text-center">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Meet the Leadership</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Our leaders are dedicated to our mission and values.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-2 gap-x-8 gap-y-16 text-center sm:grid-cols-3 md:grid-cols-4 lg:mx-0 lg:max-w-none lg:grid-cols-5 xl:grid-cols-6">
          <li>
            <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900">Michael Foster</h3>
            <p class="text-sm leading-6 text-gray-600">Co-Founder / CTO</p>
          </li>
          <li>
            <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900">Dries Vincent</h3>
            <p class="text-sm leading-6 text-gray-600">Business Relations</p>
          </li>
          <li>
            <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900">Lindsay Walton</h3>
            <p class="text-sm leading-6 text-gray-600">Front-end Developer</p>
          </li>
           <li>
            <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900">Courtney Henry</h3>
            <p class="text-sm leading-6 text-gray-600">Designer</p>
          </li>
           <li>
            <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900">Tom Cook</h3>
            <p class="text-sm leading-6 text-gray-600">Director of Product</p>
          </li>
           <li>
            <img class="mx-auto h-24 w-24 rounded-full" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900">Whitney Francis</h3>
            <p class="text-sm leading-6 text-gray-600">Copywriter</p>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-015",
        "title": "Horizontal Cards with Bio",
        "description": "Horizontal cards with image on left/right and bio.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Creative Minds</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Meet the people behind the magic.</p>
        </div>
        <div class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 lg:mx-0 lg:max-w-none lg:grid-cols-2">
          <div class="flex flex-col gap-6 xl:flex-row">
            <img class="aspect-[4/5] w-52 flex-none rounded-2xl object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <div class="flex-auto">
              <h3 class="text-lg font-semibold leading-8 text-gray-900">Michael Foster</h3>
              <p class="text-base leading-7 text-gray-600">Co-Founder / CTO</p>
              <p class="mt-6 text-base leading-7 text-gray-600">Quia illum aut in beatae. Possimus dolores aliquid accusantium aut in ut non assumenda. Elementum ac interdum morbi.</p>
            </div>
          </div>
          <div class="flex flex-col gap-6 xl:flex-row">
            <img class="aspect-[4/5] w-52 flex-none rounded-2xl object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <div class="flex-auto">
              <h3 class="text-lg font-semibold leading-8 text-gray-900">Lindsay Walton</h3>
              <p class="text-base leading-7 text-gray-600">Front-end Developer</p>
              <p class="mt-6 text-base leading-7 text-gray-600">Libero fames augue nisl porttitor nisi, quis. Id ac elit odio vitae elementum enim vitae ullamcorper suspendisse.</p>
            </div>
          </div>
           <div class="flex flex-col gap-6 xl:flex-row">
            <img class="aspect-[4/5] w-52 flex-none rounded-2xl object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <div class="flex-auto">
              <h3 class="text-lg font-semibold leading-8 text-gray-900">Courtney Henry</h3>
              <p class="text-base leading-7 text-gray-600">Designer</p>
              <p class="mt-6 text-base leading-7 text-gray-600">Amet amet eget scelerisque tellus sit neque faucibus non eleifend. Integer eu praesent at a. Ornare arcu gravida natoque erat.</p>
            </div>
          </div>
           <div class="flex flex-col gap-6 xl:flex-row">
            <img class="aspect-[4/5] w-52 flex-none rounded-2xl object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <div class="flex-auto">
              <h3 class="text-lg font-semibold leading-8 text-gray-900">Tom Cook</h3>
              <p class="text-base leading-7 text-gray-600">Director of Product</p>
              <p class="mt-6 text-base leading-7 text-gray-600">Quia illum aut in beatae. Possimus dolores aliquid accusantium aut in ut non assumenda. Elementum ac interdum morbi.</p>
            </div>
          </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-016",
        "title": "Dark Mode Cards",
        "description": "Team cards on dark background.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-900 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Our Team</h2>
          <p class="mt-6 text-lg leading-8 text-gray-300">We’re a distributed team of over 30 talented individuals.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 xl:gap-8">
          <li class="rounded-2xl bg-gray-800 px-8 py-10">
            <img class="mx-auto h-48 w-48 rounded-full md:h-56 md:w-56" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-white">Michael Foster</h3>
            <p class="text-sm leading-6 text-gray-400">Co-Founder / CTO</p>
            <ul role="list" class="mt-6 flex justify-center gap-x-6">
              <li><a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">Twitter</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a></li>
            </ul>
          </li>
          <li class="rounded-2xl bg-gray-800 px-8 py-10">
            <img class="mx-auto h-48 w-48 rounded-full md:h-56 md:w-56" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-white">Dries Vincent</h3>
            <p class="text-sm leading-6 text-gray-400">Business Relations</p>
             <ul role="list" class="mt-6 flex justify-center gap-x-6">
              <li><a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">Twitter</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a></li>
            </ul>
          </li>
          <li class="rounded-2xl bg-gray-800 px-8 py-10">
            <img class="mx-auto h-48 w-48 rounded-full md:h-56 md:w-56" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-white">Lindsay Walton</h3>
            <p class="text-sm leading-6 text-gray-400">Front-end Developer</p>
             <ul role="list" class="mt-6 flex justify-center gap-x-6">
              <li><a href="#" class="text-gray-400 hover:text-gray-300"><span class="sr-only">Twitter</span><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-017",
        "title": "Full Width with Overlay",
        "description": "Full width image background with text overlay.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-900 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Meet our global team</h2>
          <p class="mt-6 text-lg leading-8 text-gray-300">We are a 100% remote team spread all across the world.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-14 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 xl:grid-cols-4">
          <li class="relative">
            <img class="aspect-[14/13] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-white w-full">Leslie Alexander</h3>
            <p class="text-base leading-7 text-gray-300 w-full">Co-Founder / CEO</p>
          </li>
           <li class="relative">
            <img class="aspect-[14/13] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-white w-full">Michael Foster</h3>
            <p class="text-base leading-7 text-gray-300 w-full">Co-Founder / CTO</p>
          </li>
           <li class="relative">
            <img class="aspect-[14/13] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-white w-full">Dries Vincent</h3>
            <p class="text-base leading-7 text-gray-300 w-full">Manager, Business Relations</p>
          </li>
           <li class="relative">
            <img class="aspect-[14/13] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-white w-full">Lindsay Walton</h3>
            <p class="text-base leading-7 text-gray-300 w-full">Front-end Developer</p>
          </li>
        </ul>
      </div>
    </div>"""
    }
]

TEMPLATES_TEAM_PART_2 = [
    {
        "id": "team-018",
        "title": "Team with Stats",
        "description": "Team members with individual statistics.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">We build bridges</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Our expert team has decades of combined experience.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          <li>
            <img class="aspect-[3/2] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=800&h=800&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Leonard Krasner</h3>
            <p class="text-base leading-7 text-gray-600">Senior Designer</p>
            <div class="mt-4 flex gap-x-4 text-sm font-medium text-gray-500">
               <div>10+ Years Exp</div>
               <div>•</div>
               <div>50+ Projects</div>
            </div>
          </li>
           <li>
            <img class="aspect-[3/2] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=800&h=800&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Floyd Miles</h3>
            <p class="text-base leading-7 text-gray-600">Principal Designer</p>
             <div class="mt-4 flex gap-x-4 text-sm font-medium text-gray-500">
               <div>8+ Years Exp</div>
               <div>•</div>
               <div>30+ Projects</div>
            </div>
          </li>
           <li>
            <img class="aspect-[3/2] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=800&h=800&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Emily Selman</h3>
            <p class="text-base leading-7 text-gray-600">VP, User Experience</p>
             <div class="mt-4 flex gap-x-4 text-sm font-medium text-gray-500">
               <div>12+ Years Exp</div>
               <div>•</div>
               <div>80+ Projects</div>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-019",
        "title": "Simple List",
        "description": "Simple vertical list of team members.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Team Members</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Browse our talented team.</p>
        </div>
        <ul role="list" class="divide-y divide-gray-100 mt-10">
          <li class="flex justify-between gap-x-6 py-5">
            <div class="flex min-w-0 gap-x-4">
              <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">Leslie Alexander</p>
                <p class="mt-1 truncate text-xs leading-5 text-gray-500">leslie.alexander@example.com</p>
              </div>
            </div>
            <div class="hidden sm:flex sm:flex-col sm:items-end">
              <p class="text-sm leading-6 text-gray-900">Co-Founder / CEO</p>
              <div class="mt-1 flex items-center gap-x-1.5">
                <div class="flex-none rounded-full bg-emerald-500/20 p-1">
                  <div class="h-1.5 w-1.5 rounded-full bg-emerald-500"></div>
                </div>
                <p class="text-xs leading-5 text-gray-500">Online</p>
              </div>
            </div>
          </li>
          <li class="flex justify-between gap-x-6 py-5">
            <div class="flex min-w-0 gap-x-4">
              <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">Michael Foster</p>
                <p class="mt-1 truncate text-xs leading-5 text-gray-500">michael.foster@example.com</p>
              </div>
            </div>
            <div class="hidden sm:flex sm:flex-col sm:items-end">
               <p class="text-sm leading-6 text-gray-900">Co-Founder / CTO</p>
              <div class="mt-1 flex items-center gap-x-1.5">
                <div class="flex-none rounded-full bg-emerald-500/20 p-1">
                  <div class="h-1.5 w-1.5 rounded-full bg-emerald-500"></div>
                </div>
                <p class="text-xs leading-5 text-gray-500">Online</p>
              </div>
            </div>
          </li>
          <li class="flex justify-between gap-x-6 py-5">
            <div class="flex min-w-0 gap-x-4">
              <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">Dries Vincent</p>
                <p class="mt-1 truncate text-xs leading-5 text-gray-500">dries.vincent@example.com</p>
              </div>
            </div>
            <div class="hidden sm:flex sm:flex-col sm:items-end">
               <p class="text-sm leading-6 text-gray-900">Business Relations</p>
               <p class="text-xs leading-5 text-gray-500">Last seen 3h ago</p>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-020",
        "title": "Grid with Hover Effect",
        "description": "Image grid with hover overlay for details.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-50 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="text-center">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Meet the Crew</h2>
          <p class="mt-4 text-lg leading-8 text-gray-600">The talented people behind the scenes.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-4">
          <li class="relative group overflow-hidden rounded-2xl">
            <img class="aspect-[2/3] w-full object-cover transition duration-300 group-hover:scale-110" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900/90 to-transparent p-6 translate-y-4 group-hover:translate-y-0 transition duration-300">
               <h3 class="text-lg font-semibold leading-tight text-white">Lindsay Walton</h3>
               <p class="text-sm text-gray-300">Front-end Developer</p>
               <div class="mt-4 flex gap-4 opacity-0 group-hover:opacity-100 transition duration-300 delay-100">
                 <a href="#" class="text-white hover:text-gray-200">Twitter</a>
                 <a href="#" class="text-white hover:text-gray-200">LinkedIn</a>
               </div>
            </div>
          </li>
           <li class="relative group overflow-hidden rounded-2xl">
            <img class="aspect-[2/3] w-full object-cover transition duration-300 group-hover:scale-110" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900/90 to-transparent p-6 translate-y-4 group-hover:translate-y-0 transition duration-300">
               <h3 class="text-lg font-semibold leading-tight text-white">Courtney Henry</h3>
               <p class="text-sm text-gray-300">Designer</p>
               <div class="mt-4 flex gap-4 opacity-0 group-hover:opacity-100 transition duration-300 delay-100">
                 <a href="#" class="text-white hover:text-gray-200">Twitter</a>
                 <a href="#" class="text-white hover:text-gray-200">Dribbble</a>
               </div>
            </div>
          </li>
           <li class="relative group overflow-hidden rounded-2xl">
            <img class="aspect-[2/3] w-full object-cover transition duration-300 group-hover:scale-110" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900/90 to-transparent p-6 translate-y-4 group-hover:translate-y-0 transition duration-300">
               <h3 class="text-lg font-semibold leading-tight text-white">Tom Cook</h3>
               <p class="text-sm text-gray-300">Director of Product</p>
               <div class="mt-4 flex gap-4 opacity-0 group-hover:opacity-100 transition duration-300 delay-100">
                 <a href="#" class="text-white hover:text-gray-200">Twitter</a>
                 <a href="#" class="text-white hover:text-gray-200">LinkedIn</a>
               </div>
            </div>
          </li>
           <li class="relative group overflow-hidden rounded-2xl">
            <img class="aspect-[2/3] w-full object-cover transition duration-300 group-hover:scale-110" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900/90 to-transparent p-6 translate-y-4 group-hover:translate-y-0 transition duration-300">
               <h3 class="text-lg font-semibold leading-tight text-white">Whitney Francis</h3>
               <p class="text-sm text-gray-300">Copywriter</p>
               <div class="mt-4 flex gap-4 opacity-0 group-hover:opacity-100 transition duration-300 delay-100">
                 <a href="#" class="text-white hover:text-gray-200">Twitter</a>
                 <a href="#" class="text-white hover:text-gray-200">Medium</a>
               </div>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-021",
        "title": "Small Round Avatars Grid",
        "description": "Dense grid with small round avatars.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Contributors</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Thanks to all our amazing contributors.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-2 gap-x-8 gap-y-8 sm:grid-cols-4 md:grid-cols-6 lg:mx-0 lg:max-w-none lg:grid-cols-8">
          <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Leslie</h3>
          </li>
          <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Michael</h3>
          </li>
          <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Dries</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Lindsay</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Courtney</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Tom</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Whitney</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Leonard</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Floyd</h3>
          </li>
           <li>
            <img class="mx-auto h-16 w-16 rounded-full" src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-2 text-xs font-semibold text-center text-gray-900">Emily</h3>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-022",
        "title": "Sidebar Team List",
        "description": "Team list suitable for sidebar or narrow column.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-12 px-6 max-w-xs border-r border-gray-200 min-h-screen">
      <h3 class="text-sm font-semibold leading-6 text-gray-900">Team</h3>
      <ul role="list" class="mt-6 divide-y divide-gray-100 border-b border-gray-200">
        <li class="flex gap-x-3 py-4">
          <img class="h-8 w-8 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-auto">
            <div class="flex items-baseline justify-between">
              <p class="text-sm font-semibold leading-6 text-gray-900">Leslie</p>
              <p class="flex-none text-xs text-gray-600">10m</p>
            </div>
            <p class="mt-1 line-clamp-2 text-xs leading-5 text-gray-500">Design updates</p>
          </div>
        </li>
         <li class="flex gap-x-3 py-4">
          <img class="h-8 w-8 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-auto">
            <div class="flex items-baseline justify-between">
              <p class="text-sm font-semibold leading-6 text-gray-900">Michael</p>
              <p class="flex-none text-xs text-gray-600">2h</p>
            </div>
            <p class="mt-1 line-clamp-2 text-xs leading-5 text-gray-500">New project plan</p>
          </div>
        </li>
         <li class="flex gap-x-3 py-4">
          <img class="h-8 w-8 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
          <div class="flex-auto">
            <div class="flex items-baseline justify-between">
              <p class="text-sm font-semibold leading-6 text-gray-900">Dries</p>
              <p class="flex-none text-xs text-gray-600">1d</p>
            </div>
            <p class="mt-1 line-clamp-2 text-xs leading-5 text-gray-500">Meeting notes</p>
          </div>
        </li>
      </ul>
      <a href="#" class="mt-4 block text-sm font-medium text-indigo-600 hover:text-indigo-500">View all</a>
    </div>"""
    },
    {
        "id": "team-023",
        "title": "Cards with Skills",
        "description": "Team cards highlighting top skills.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Specialists</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Masters of their craft.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          <li class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow border border-gray-100">
            <div class="flex w-full items-center justify-between space-x-6 p-6">
              <div class="flex-1 truncate">
                <div class="flex items-center space-x-3">
                  <h3 class="truncate text-sm font-medium text-gray-900">Jane Cooper</h3>
                  <span class="inline-flex flex-shrink-0 items-center rounded-full bg-green-50 px-1.5 py-0.5 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Admin</span>
                </div>
                <p class="mt-1 truncate text-sm text-gray-500">Regional Paradigm Technician</p>
                <div class="mt-4 flex flex-wrap gap-2">
                    <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Python</span>
                    <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">React</span>
                </div>
              </div>
              <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
            </div>
            <div>
              <div class="-mt-px flex divide-x divide-gray-200">
                <div class="flex w-0 flex-1">
                  <a href="mailto:janecooper@example.com" class="relative -mr-px inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-bl-lg border border-transparent py-4 text-sm font-semibold text-gray-900 hover:bg-gray-50">
                    Email
                  </a>
                </div>
                <div class="-ml-px flex w-0 flex-1">
                  <a href="tel:+1-202-555-0170" class="relative inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-br-lg border border-transparent py-4 text-sm font-semibold text-gray-900 hover:bg-gray-50">
                    Call
                  </a>
                </div>
              </div>
            </div>
          </li>
          <!-- More people... -->
           <li class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow border border-gray-100">
            <div class="flex w-full items-center justify-between space-x-6 p-6">
              <div class="flex-1 truncate">
                <div class="flex items-center space-x-3">
                  <h3 class="truncate text-sm font-medium text-gray-900">Cody Fisher</h3>
                </div>
                <p class="mt-1 truncate text-sm text-gray-500">Product Manager</p>
                 <div class="mt-4 flex flex-wrap gap-2">
                    <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Strategy</span>
                    <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Agile</span>
                </div>
              </div>
              <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
            </div>
            <div>
              <div class="-mt-px flex divide-x divide-gray-200">
                <div class="flex w-0 flex-1">
                  <a href="mailto:janecooper@example.com" class="relative -mr-px inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-bl-lg border border-transparent py-4 text-sm font-semibold text-gray-900 hover:bg-gray-50">
                    Email
                  </a>
                </div>
                <div class="-ml-px flex w-0 flex-1">
                  <a href="tel:+1-202-555-0170" class="relative inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-br-lg border border-transparent py-4 text-sm font-semibold text-gray-900 hover:bg-gray-50">
                    Call
                  </a>
                </div>
              </div>
            </div>
          </li>
           <li class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow border border-gray-100">
            <div class="flex w-full items-center justify-between space-x-6 p-6">
              <div class="flex-1 truncate">
                <div class="flex items-center space-x-3">
                  <h3 class="truncate text-sm font-medium text-gray-900">Esther Howard</h3>
                </div>
                <p class="mt-1 truncate text-sm text-gray-500">Frontend Dev</p>
                 <div class="mt-4 flex flex-wrap gap-2">
                    <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Vue.js</span>
                    <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Tailwind</span>
                </div>
              </div>
              <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1520813792240-56fc4a3765a7?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
            </div>
            <div>
              <div class="-mt-px flex divide-x divide-gray-200">
                <div class="flex w-0 flex-1">
                  <a href="mailto:janecooper@example.com" class="relative -mr-px inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-bl-lg border border-transparent py-4 text-sm font-semibold text-gray-900 hover:bg-gray-50">
                    Email
                  </a>
                </div>
                <div class="-ml-px flex w-0 flex-1">
                  <a href="tel:+1-202-555-0170" class="relative inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-br-lg border border-transparent py-4 text-sm font-semibold text-gray-900 hover:bg-gray-50">
                    Call
                  </a>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-024",
        "title": "Minimal Text Only",
        "description": "Minimal team list without avatars.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Board of Directors</h2>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          <li>
            <h3 class="text-lg font-semibold leading-8 text-gray-900">Michael Foster</h3>
            <p class="text-base leading-7 text-gray-600">Co-Founder / CTO</p>
            <p class="mt-4 text-base leading-7 text-gray-600">Former engineering lead at Google. PhD from Stanford.</p>
          </li>
           <li>
            <h3 class="text-lg font-semibold leading-8 text-gray-900">Lindsay Walton</h3>
            <p class="text-base leading-7 text-gray-600">Front-end Developer</p>
            <p class="mt-4 text-base leading-7 text-gray-600">Open source contributor. Author of 'CSS for the Soul'.</p>
          </li>
          <li>
            <h3 class="text-lg font-semibold leading-8 text-gray-900">Courtney Henry</h3>
            <p class="text-base leading-7 text-gray-600">Designer</p>
            <p class="mt-4 text-base leading-7 text-gray-600">Award winning designer. Featured in Smashing Magazine.</p>
          </li>
          <li>
            <h3 class="text-lg font-semibold leading-8 text-gray-900">Tom Cook</h3>
            <p class="text-base leading-7 text-gray-600">Director of Product</p>
            <p class="mt-4 text-base leading-7 text-gray-600">20+ years in product management. Agile coach.</p>
          </li>
           <li>
            <h3 class="text-lg font-semibold leading-8 text-gray-900">Whitney Francis</h3>
            <p class="text-base leading-7 text-gray-600">Copywriter</p>
            <p class="mt-4 text-base leading-7 text-gray-600">Creative writer with a passion for storytelling.</p>
          </li>
           <li>
            <h3 class="text-lg font-semibold leading-8 text-gray-900">Leonard Krasner</h3>
            <p class="text-base leading-7 text-gray-600">Senior Designer</p>
            <p class="mt-4 text-base leading-7 text-gray-600">Minimalist. Typography enthusiast.</p>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-025",
        "title": "Grid with Location",
        "description": "Team grid showing location/country.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl text-center mb-16">Global Representatives</h2>
            <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
                <div class="flex flex-col items-center p-8 bg-gray-50 rounded-2xl">
                    <img class="h-24 w-24 rounded-full object-cover mb-4" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-lg font-semibold text-gray-900">Sarah J.</h3>
                    <p class="text-sm text-gray-500">New York, USA</p>
                    <span class="mt-2 inline-flex items-center rounded-md bg-blue-50 px-2 py-1 text-xs font-medium text-blue-700 ring-1 ring-inset ring-blue-700/10">North America</span>
                </div>
                <div class="flex flex-col items-center p-8 bg-gray-50 rounded-2xl">
                    <img class="h-24 w-24 rounded-full object-cover mb-4" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-lg font-semibold text-gray-900">David K.</h3>
                    <p class="text-sm text-gray-500">London, UK</p>
                     <span class="mt-2 inline-flex items-center rounded-md bg-indigo-50 px-2 py-1 text-xs font-medium text-indigo-700 ring-1 ring-inset ring-indigo-700/10">Europe</span>
                </div>
                <div class="flex flex-col items-center p-8 bg-gray-50 rounded-2xl">
                    <img class="h-24 w-24 rounded-full object-cover mb-4" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-lg font-semibold text-gray-900">Amara L.</h3>
                    <p class="text-sm text-gray-500">Lagos, Nigeria</p>
                     <span class="mt-2 inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-700/10">Africa</span>
                </div>
                <div class="flex flex-col items-center p-8 bg-gray-50 rounded-2xl">
                    <img class="h-24 w-24 rounded-full object-cover mb-4" src="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-lg font-semibold text-gray-900">Wei C.</h3>
                    <p class="text-sm text-gray-500">Shanghai, China</p>
                     <span class="mt-2 inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-700/10">Asia</span>
                </div>
            </div>
        </div>
    </div>"""
    }
]


TEMPLATES_TEAM_NEW.extend(TEMPLATES_TEAM_PART_2)

TEMPLATES_TEAM_PART_3 = [
    {
        "id": "team-026",
        "title": "Cards with Cover Photo",
        "description": "Team cards featuring a background cover photo.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-100 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl text-center">
             <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Our Leadership</h2>
        </div>
        <div class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          <div class="flex flex-col overflow-hidden rounded-lg shadow-lg bg-white">
            <div class="flex-shrink-0 h-32 bg-indigo-500">
                <img class="h-full w-full object-cover opacity-50" src="https://images.unsplash.com/photo-1557683316-973673baf926?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            </div>
            <div class="flex-1 flex flex-col p-6 pt-0 relative">
                <div class="-mt-12 mb-4">
                    <img class="h-24 w-24 rounded-full border-4 border-white shadow-sm mx-auto" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                </div>
                <div class="text-center">
                    <h3 class="text-xl font-bold text-gray-900">Leslie Alexander</h3>
                    <p class="text-sm font-medium text-indigo-600">Co-Founder / CEO</p>
                    <p class="mt-4 text-base text-gray-500">Leading the company with vision and integrity for over 10 years.</p>
                </div>
            </div>
          </div>
          <div class="flex flex-col overflow-hidden rounded-lg shadow-lg bg-white">
            <div class="flex-shrink-0 h-32 bg-pink-500">
                 <img class="h-full w-full object-cover opacity-50" src="https://images.unsplash.com/photo-1557682250-33bd709cbe85?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            </div>
            <div class="flex-1 flex flex-col p-6 pt-0 relative">
                 <div class="-mt-12 mb-4">
                    <img class="h-24 w-24 rounded-full border-4 border-white shadow-sm mx-auto" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                </div>
                <div class="text-center">
                    <h3 class="text-xl font-bold text-gray-900">Michael Foster</h3>
                    <p class="text-sm font-medium text-pink-600">Head of Product</p>
                    <p class="mt-4 text-base text-gray-500">Passionate about building products that users love and depend on.</p>
                </div>
            </div>
          </div>
          <div class="flex flex-col overflow-hidden rounded-lg shadow-lg bg-white">
            <div class="flex-shrink-0 h-32 bg-green-500">
                 <img class="h-full w-full object-cover opacity-50" src="https://images.unsplash.com/photo-1557682224-5b8590cd18b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
            </div>
            <div class="flex-1 flex flex-col p-6 pt-0 relative">
                 <div class="-mt-12 mb-4">
                    <img class="h-24 w-24 rounded-full border-4 border-white shadow-sm mx-auto" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                </div>
                <div class="text-center">
                    <h3 class="text-xl font-bold text-gray-900">Dries Vincent</h3>
                    <p class="text-sm font-medium text-green-600">Engineering Manager</p>
                    <p class="mt-4 text-base text-gray-500">Scaling systems and teams to high performance and reliability.</p>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-027",
        "title": "Masonry Grid Style",
        "description": "Team grid with staggered layout.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl text-center mb-16">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">The Collective</h2>
        </div>
        <div class="columns-1 md:columns-2 lg:columns-3 gap-8 space-y-8">
             <div class="break-inside-avoid bg-gray-50 rounded-2xl p-6">
                <img class="w-24 h-24 rounded-full object-cover mb-4" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-bold text-gray-900">Leslie Alexander</h3>
                <p class="text-sm text-gray-500">CEO</p>
                <p class="mt-2 text-sm text-gray-600">Visionary leader driving innovation.</p>
            </div>
             <div class="break-inside-avoid bg-blue-50 rounded-2xl p-6 text-center">
                 <img class="w-32 h-32 rounded-full object-cover mx-auto mb-4" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-bold text-gray-900">Michael Foster</h3>
                <p class="text-sm text-blue-600">CTO</p>
                <p class="mt-2 text-sm text-gray-600">Tech genius with a plan.</p>
            </div>
            <div class="break-inside-avoid bg-gray-50 rounded-2xl p-6">
                <div class="flex items-center gap-4">
                    <img class="w-16 h-16 rounded-full object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <div>
                         <h3 class="text-lg font-bold text-gray-900">Dries Vincent</h3>
                        <p class="text-sm text-gray-500">Engineering</p>
                    </div>
                </div>
                 <p class="mt-4 text-sm text-gray-600">Building robust infrastructure.</p>
            </div>
             <div class="break-inside-avoid bg-indigo-600 rounded-2xl p-6 text-white">
                 <img class="w-20 h-20 rounded-full object-cover mb-4 border-2 border-white" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-bold text-white">Lindsay Walton</h3>
                <p class="text-sm text-indigo-200">Frontend</p>
                <p class="mt-2 text-sm text-indigo-100">Crafting pixels.</p>
            </div>
             <div class="break-inside-avoid bg-gray-50 rounded-2xl p-6">
                <img class="w-full h-48 object-cover rounded-lg mb-4" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=512&h=512&q=80" alt="">
                <h3 class="text-xl font-bold text-gray-900">Courtney Henry</h3>
                <p class="text-sm text-gray-500">Design Lead</p>
            </div>
             <div class="break-inside-avoid bg-pink-50 rounded-2xl p-6">
                <h3 class="text-lg font-bold text-gray-900">Tom Cook</h3>
                <p class="text-sm text-pink-600">Product</p>
                 <div class="mt-4 flex items-center gap-3">
                    <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <p class="text-sm italic text-gray-600">"Focus on the user."</p>
                 </div>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-028",
        "title": "Hexagon Avatars",
        "description": "Unique hexagon shaped avatar masks.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-900 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
         <div class="mx-auto max-w-2xl text-center mb-20">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">The Hex Team</h2>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 justify-items-center">
            <div class="text-center">
                 <div class="relative w-32 h-32 mx-auto mb-4 hexagon-mask bg-indigo-500 p-1">
                    <img class="w-full h-full object-cover hexagon-clip" style="clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="text-lg font-bold text-white">Leslie</h3>
                 <p class="text-sm text-indigo-400">CEO</p>
            </div>
            <div class="text-center">
                 <div class="relative w-32 h-32 mx-auto mb-4 hexagon-mask bg-purple-500 p-1">
                    <img class="w-full h-full object-cover hexagon-clip" style="clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="text-lg font-bold text-white">Michael</h3>
                 <p class="text-sm text-purple-400">CTO</p>
            </div>
            <div class="text-center">
                 <div class="relative w-32 h-32 mx-auto mb-4 hexagon-mask bg-pink-500 p-1">
                    <img class="w-full h-full object-cover hexagon-clip" style="clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="text-lg font-bold text-white">Dries</h3>
                 <p class="text-sm text-pink-400">Dev</p>
            </div>
             <div class="text-center">
                 <div class="relative w-32 h-32 mx-auto mb-4 hexagon-mask bg-cyan-500 p-1">
                    <img class="w-full h-full object-cover hexagon-clip" style="clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="text-lg font-bold text-white">Lindsay</h3>
                 <p class="text-sm text-cyan-400">Design</p>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-029",
        "title": "Team Slider",
        "description": "Horizontal scrolling team slider.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32 overflow-hidden">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
         <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl mb-12">Who We Are</h2>
         <div class="flex overflow-x-auto gap-8 pb-8 snap-x snap-mandatory">
            <div class="flex-none w-80 snap-center bg-gray-50 rounded-2xl p-6 text-center shadow-sm">
                <img class="w-32 h-32 rounded-full mx-auto mb-6 object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-xl font-bold text-gray-900">Leslie Alexander</h3>
                <p class="text-gray-500">Co-Founder / CEO</p>
                <p class="mt-4 text-sm text-gray-600">"Leadership is about empowering others."</p>
            </div>
            <div class="flex-none w-80 snap-center bg-gray-50 rounded-2xl p-6 text-center shadow-sm">
                <img class="w-32 h-32 rounded-full mx-auto mb-6 object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-xl font-bold text-gray-900">Michael Foster</h3>
                <p class="text-gray-500">Co-Founder / CTO</p>
                 <p class="mt-4 text-sm text-gray-600">"Building the future, one line at a time."</p>
            </div>
             <div class="flex-none w-80 snap-center bg-gray-50 rounded-2xl p-6 text-center shadow-sm">
                <img class="w-32 h-32 rounded-full mx-auto mb-6 object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-xl font-bold text-gray-900">Dries Vincent</h3>
                <p class="text-gray-500">Business Relations</p>
                 <p class="mt-4 text-sm text-gray-600">"Relationships are the currency of business."</p>
            </div>
             <div class="flex-none w-80 snap-center bg-gray-50 rounded-2xl p-6 text-center shadow-sm">
                <img class="w-32 h-32 rounded-full mx-auto mb-6 object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-xl font-bold text-gray-900">Lindsay Walton</h3>
                <p class="text-gray-500">Front-end Developer</p>
                 <p class="mt-4 text-sm text-gray-600">"User experience is everything."</p>
            </div>
         </div>
      </div>
    </div>"""
    },
    {
        "id": "team-030",
        "title": "Minimal Circle Detailed",
        "description": "Minimal layout with circle avatars and detailed bio below.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <ul role="list" class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-4">
          <li>
            <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900 text-center">Leslie Alexander</h3>
            <p class="text-sm leading-6 text-blue-600 text-center">Co-Founder / CEO</p>
            <p class="mt-4 text-sm leading-6 text-gray-500 text-center text-balance">Leslie is an expert in strategic planning and execution. She loves hiking and coffee.</p>
          </li>
           <li>
            <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
             <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900 text-center">Michael Foster</h3>
            <p class="text-sm leading-6 text-blue-600 text-center">Co-Founder / CTO</p>
            <p class="mt-4 text-sm leading-6 text-gray-500 text-center text-balance">Michael ensures our tech stack is cutting edge. He's also a part-time DJ.</p>
          </li>
           <li>
            <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
             <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900 text-center">Dries Vincent</h3>
            <p class="text-sm leading-6 text-blue-600 text-center">Manager, Business Relations</p>
            <p class="mt-4 text-sm leading-6 text-gray-500 text-center text-balance">Dries connects us with the world. He travels extensively for work and fun.</p>
          </li>
           <li>
            <img class="mx-auto h-40 w-40 rounded-full object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
             <h3 class="mt-6 text-base font-semibold leading-7 tracking-tight text-gray-900 text-center">Lindsay Walton</h3>
            <p class="text-sm leading-6 text-blue-600 text-center">Front-end Developer</p>
            <p class="mt-4 text-sm leading-6 text-gray-500 text-center text-balance">Lindsay creates beautiful interfaces. She enjoys painting in her free time.</p>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-031",
        "title": "Team Table",
        "description": "Team directory in a table format.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="px-4 sm:px-6 lg:px-8">
            <div class="sm:flex sm:items-center">
                <div class="sm:flex-auto">
                    <h1 class="text-base font-semibold leading-6 text-gray-900">Users</h1>
                    <p class="mt-2 text-sm text-gray-700">A list of all the users in your account including their name, title, email and role.</p>
                </div>
            </div>
            <div class="mt-8 flow-root">
                <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                    <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                        <table class="min-w-full divide-y divide-gray-300">
                            <thead>
                                <tr>
                                    <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Name</th>
                                    <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Title</th>
                                    <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Status</th>
                                    <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Role</th>
                                    <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
                                        <span class="sr-only">Edit</span>
                                    </th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-200 bg-white">
                                <tr>
                                    <td class="whitespace-nowrap py-5 pl-4 pr-3 text-sm sm:pl-0">
                                        <div class="flex items-center">
                                            <div class="h-11 w-11 flex-shrink-0">
                                                <img class="h-11 w-11 rounded-full" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                                            </div>
                                            <div class="ml-4">
                                                <div class="font-medium text-gray-900">Lindsay Walton</div>
                                                <div class="text-gray-500">lindsay.walton@example.com</div>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-500">
                                        <div class="text-gray-900">Front-end Developer</div>
                                        <div class="text-gray-500">Optimization</div>
                                    </td>
                                    <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-500">
                                        <span class="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Active</span>
                                    </td>
                                    <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-500">Member</td>
                                    <td class="relative whitespace-nowrap py-5 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                                        <a href="#" class="text-indigo-600 hover:text-indigo-900">Edit</a>
                                    </td>
                                </tr>
                                 <tr>
                                    <td class="whitespace-nowrap py-5 pl-4 pr-3 text-sm sm:pl-0">
                                        <div class="flex items-center">
                                            <div class="h-11 w-11 flex-shrink-0">
                                                <img class="h-11 w-11 rounded-full" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                                            </div>
                                            <div class="ml-4">
                                                <div class="font-medium text-gray-900">Courtney Henry</div>
                                                <div class="text-gray-500">courtney.henry@example.com</div>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-500">
                                        <div class="text-gray-900">Designer</div>
                                        <div class="text-gray-500">Intranet</div>
                                    </td>
                                    <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-500">
                                        <span class="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Active</span>
                                    </td>
                                    <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-500">Admin</td>
                                    <td class="relative whitespace-nowrap py-5 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                                        <a href="#" class="text-indigo-600 hover:text-indigo-900">Edit</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-032",
        "title": "Stacked List Actions",
        "description": "Team list with action buttons.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-50 py-24 sm:py-32">
       <div class="mx-auto max-w-3xl px-6 lg:px-8">
         <h2 class="text-2xl font-bold mb-6 text-gray-900">Pending Invites</h2>
         <ul role="list" class="divide-y divide-gray-100 overflow-hidden bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl">
            <li class="relative flex justify-between gap-x-6 px-4 py-5 hover:bg-gray-50 sm:px-6">
                <div class="flex gap-x-4">
                    <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <div class="min-w-0 flex-auto">
                        <p class="text-sm font-semibold leading-6 text-gray-900">
                            <a href="#">
                            <span class="absolute inset-x-0 -top-px bottom-0"></span>
                            Leslie Alexander
                            </a>
                        </p>
                        <p class="mt-1 flex text-xs leading-5 text-gray-500">
                            <a href="mailto:leslie.alexander@example.com" class="relative truncate hover:underline">leslie.alexander@example.com</a>
                        </p>
                    </div>
                </div>
                <div class="flex items-center gap-x-4">
                    <div class="hidden sm:flex sm:flex-col sm:items-end">
                        <p class="text-sm leading-6 text-gray-900">Co-Founder / CEO</p>
                         <p class="mt-1 text-xs leading-5 text-gray-500">Invited 2 days ago</p>
                    </div>
                     <svg class="h-5 w-5 flex-none text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z" clip-rule="evenodd" /></svg>
                </div>
            </li>
             <li class="relative flex justify-between gap-x-6 px-4 py-5 hover:bg-gray-50 sm:px-6">
                <div class="flex gap-x-4">
                    <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <div class="min-w-0 flex-auto">
                        <p class="text-sm font-semibold leading-6 text-gray-900">
                            <a href="#">
                            <span class="absolute inset-x-0 -top-px bottom-0"></span>
                            Michael Foster
                            </a>
                        </p>
                        <p class="mt-1 flex text-xs leading-5 text-gray-500">
                             <a href="mailto:michael.foster@example.com" class="relative truncate hover:underline">michael.foster@example.com</a>
                        </p>
                    </div>
                </div>
                <div class="flex items-center gap-x-4">
                    <div class="hidden sm:flex sm:flex-col sm:items-end">
                        <p class="text-sm leading-6 text-gray-900">Co-Founder / CTO</p>
                         <p class="mt-1 text-xs leading-5 text-gray-500">Invited 1 week ago</p>
                    </div>
                    <svg class="h-5 w-5 flex-none text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z" clip-rule="evenodd" /></svg>
                </div>
            </li>
         </ul>
       </div>
    </div>"""
    },
    {
        "id": "team-033",
        "title": "Grid Offset",
        "description": "Offset grid design.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl text-center mb-16">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Creative Force</h2>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-y-16 gap-x-8">
            <div class="sm:pt-12">
                 <img class="aspect-[3/4] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
                <h3 class="mt-4 text-lg font-semibold text-gray-900">Leslie Alexander</h3>
                <p class="text-sm text-gray-500">Art Director</p>
            </div>
            <div>
                 <img class="aspect-[3/4] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
                <h3 class="mt-4 text-lg font-semibold text-gray-900">Lindsay Walton</h3>
                <p class="text-sm text-gray-500">Senior Creative</p>
            </div>
            <div class="sm:pt-12">
                 <img class="aspect-[3/4] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" alt="">
                <h3 class="mt-4 text-lg font-semibold text-gray-900">Courtney Henry</h3>
                <p class="text-sm text-gray-500">Designer</p>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-034",
        "title": "Spotlight Effect",
        "description": "Team grid with central spotlight.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-900 py-24 sm:py-32 relative overflow-hidden">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[500px] bg-indigo-500/20 rounded-full blur-3xl -z-10"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
         <div class="mx-auto max-w-2xl text-center mb-16">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">The Visionaries</h2>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="bg-gray-800/50 backdrop-blur-sm border border-gray-700 p-8 rounded-2xl text-center hover:border-indigo-500 transition-colors">
                 <img class="w-24 h-24 rounded-full mx-auto mb-4 border-2 border-indigo-500" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-bold text-white">Michael Foster</h3>
                <p class="text-sm text-indigo-400">Founder</p>
            </div>
             <div class="bg-gray-800/50 backdrop-blur-sm border border-gray-700 p-8 rounded-2xl text-center hover:border-indigo-500 transition-colors scale-105 shadow-xl shadow-indigo-500/10">
                 <img class="w-32 h-32 rounded-full mx-auto mb-4 border-4 border-indigo-500" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-xl font-bold text-white">Leslie Alexander</h3>
                <p class="text-base text-indigo-400">Co-Founder</p>
            </div>
             <div class="bg-gray-800/50 backdrop-blur-sm border border-gray-700 p-8 rounded-2xl text-center hover:border-indigo-500 transition-colors">
                 <img class="w-24 h-24 rounded-full mx-auto mb-4 border-2 border-indigo-500" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-bold text-white">Dries Vincent</h3>
                <p class="text-sm text-indigo-400">Partner</p>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-035",
        "title": "Glassmorphism Cards",
        "description": "Team cards with glassmorphism effect.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gradient-to-br from-purple-900 to-indigo-900 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl text-center mb-16">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Future Makers</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
                <div class="flex items-center gap-4 mb-4">
                     <img class="h-16 w-16 rounded-full border-2 border-white/50" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                     <div>
                         <h3 class="text-lg font-bold text-white">Lindsay</h3>
                         <p class="text-sm text-purple-200">Engineer</p>
                     </div>
                </div>
                <p class="text-gray-300 text-sm">"Glassmorphism adds a modern touch to any interface. It's clean and beautiful."</p>
            </div>
            <div class="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
                <div class="flex items-center gap-4 mb-4">
                     <img class="h-16 w-16 rounded-full border-2 border-white/50" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                     <div>
                         <h3 class="text-lg font-bold text-white">Courtney</h3>
                         <p class="text-sm text-purple-200">Creative</p>
                     </div>
                </div>
                <p class="text-gray-300 text-sm">"Transparency creates depth and hierarchy. It's not just a trend, it's a tool."</p>
            </div>
            <div class="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
                <div class="flex items-center gap-4 mb-4">
                     <img class="h-16 w-16 rounded-full border-2 border-white/50" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                     <div>
                         <h3 class="text-lg font-bold text-white">Tom</h3>
                         <p class="text-sm text-purple-200">Product</p>
                     </div>
                </div>
                <p class="text-gray-300 text-sm">"Good design is obvious. Great design is transparent, quite literally here."</p>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-036",
        "title": "Team TimelineJoined",
        "description": "Team list organized by join year.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-12">History of Us</h2>
        <div class="border-l-2 border-gray-200 ml-4 space-y-12">
            <div class="relative pl-8">
                <div class="absolute -left-1.5 mt-1.5 h-3 w-3 rounded-full border-2 border-white bg-indigo-600"></div>
                <span class="text-sm text-gray-500 font-mono">2020</span>
                <h3 class="text-lg font-bold text-gray-900 mt-1">The Beginning</h3>
                <div class="flex items-center gap-4 mt-4">
                     <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" title="Leslie">
                     <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" title="Michael">
                     <span class="text-sm text-gray-500">Co-Founders joined.</span>
                </div>
            </div>
             <div class="relative pl-8">
                <div class="absolute -left-1.5 mt-1.5 h-3 w-3 rounded-full border-2 border-white bg-gray-300"></div>
                <span class="text-sm text-gray-500 font-mono">2021</span>
                <h3 class="text-lg font-bold text-gray-900 mt-1">First Hires</h3>
                <div class="flex items-center gap-4 mt-4">
                     <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" title="Dries">
                     <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" title="Lindsay">
                      <span class="text-sm text-gray-500">Engineering team formed.</span>
                </div>
            </div>
             <div class="relative pl-8">
                <div class="absolute -left-1.5 mt-1.5 h-3 w-3 rounded-full border-2 border-white bg-gray-300"></div>
                <span class="text-sm text-gray-500 font-mono">2022</span>
                 <h3 class="text-lg font-bold text-gray-900 mt-1">Expansion</h3>
                <div class="flex items-center gap-4 mt-4">
                     <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" title="Courtney">
                     <img class="h-12 w-12 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" title="Tom">
                     <span class="text-sm text-gray-500">+10 others joined.</span>
                </div>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-037",
        "title": "Org Chart Tree",
        "description": "Visual organizational chart structure.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-50 py-24 sm:py-32 overflow-x-auto">
      <div class="mx-auto min-w-[320px] max-w-4xl px-6 text-center">
         <h2 class="text-3xl font-bold mb-16 text-gray-900">Structure</h2>
         <div class="flex flex-col items-center">
            <!-- CEO -->
            <div class="border border-gray-200 bg-white rounded-lg p-4 shadow-sm w-48 relative">
                <img class="h-12 w-12 rounded-full mx-auto mb-2" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <p class="font-bold text-gray-900 text-sm">Leslie</p>
                <p class="text-xs text-gray-500">CEO</p>
                <div class="absolute bottom-[-24px] left-1/2 w-px h-6 bg-gray-300"></div>
            </div>

            <!-- Connector -->
            <div class="w-[300px] h-px bg-gray-300 mt-6 relative">
                 <div class="absolute top-0 left-0 w-px h-6 bg-gray-300 transform translate-y-0"></div>
                 <div class="absolute top-0 right-0 w-px h-6 bg-gray-300 transform translate-y-0"></div>
                  <div class="absolute top-0 left-1/2 w-px h-6 bg-gray-300 transform translate-y-0"></div>
            </div>

            <div class="flex gap-8 mt-6">
                 <!-- VP 1 -->
                <div class="border border-gray-200 bg-white rounded-lg p-4 shadow-sm w-40">
                    <img class="h-10 w-10 rounded-full mx-auto mb-2" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <p class="font-bold text-gray-900 text-sm">Michael</p>
                    <p class="text-xs text-gray-500">CTO</p>
                </div>
                 <!-- VP 2 -->
                <div class="border border-gray-200 bg-white rounded-lg p-4 shadow-sm w-40">
                    <img class="h-10 w-10 rounded-full mx-auto mb-2" src="https://images.unsplash.com/photo-1557683316-973673baf926?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <p class="font-bold text-gray-900 text-sm">John</p>
                    <p class="text-xs text-gray-500">CFO</p>
                </div>
                 <!-- VP 3 -->
                <div class="border border-gray-200 bg-white rounded-lg p-4 shadow-sm w-40">
                    <img class="h-10 w-10 rounded-full mx-auto mb-2" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <p class="font-bold text-gray-900 text-sm">Dries</p>
                    <p class="text-xs text-gray-500">COO</p>
                </div>
            </div>
         </div>
      </div>
    </div>"""
    },
    {
         "id": "team-038",
         "title": "Grid with Bio Hover",
         "description": "Clean grid where bio slides up on hover.",
         "dir": "templates/08-team",
         "content": """
    <div class="bg-white py-24 sm:py-32">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl text-center mb-16">The Storytellers</h2>
            <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
                 <div class="relative overflow-hidden rounded-2xl group cursor-pointer bg-gray-100 aspect-[3/4]">
                    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" alt="">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-80"></div>
                    <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                        <h3 class="text-xl font-bold text-white">Leslie Alexander</h3>
                        <p class="text-indigo-300 font-medium">Editor in Chief</p>
                        <p class="text-gray-300 text-sm mt-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 delay-100">Oversees content strategy and quality across all publications.</p>
                    </div>
                 </div>
                 <div class="relative overflow-hidden rounded-2xl group cursor-pointer bg-gray-100 aspect-[3/4]">
                    <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" alt="">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-80"></div>
                    <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                        <h3 class="text-xl font-bold text-white">Lindsay Walton</h3>
                        <p class="text-indigo-300 font-medium">Senior Writer</p>
                        <p class="text-gray-300 text-sm mt-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 delay-100">Specializes in technology analysis and feature stories.</p>
                    </div>
                 </div>
                 <div class="relative overflow-hidden rounded-2xl group cursor-pointer bg-gray-100 aspect-[3/4]">
                    <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" alt="">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-80"></div>
                    <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                        <h3 class="text-xl font-bold text-white">Courtney Henry</h3>
                        <p class="text-indigo-300 font-medium">Photo Journalist</p>
                        <p class="text-gray-300 text-sm mt-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 delay-100">Captures the essence of stories through compelling imagery.</p>
                    </div>
                 </div>
            </div>
        </div>
    </div>"""
    }
]


TEMPLATES_TEAM_NEW.extend(TEMPLATES_TEAM_PART_3)

TEMPLATES_TEAM_PART_4a = [
    {
        "id": "team-039",
        "title": "Split Layout with Image",
        "description": "Team section with large image on side.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white">
      <div class="mx-auto max-w-7xl">
        <div class="grid grid-cols-1 lg:grid-cols-2">
            <div class="relative h-64 lg:h-auto">
                <img class="absolute inset-0 h-full w-full object-cover" src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80" alt="Team meeting">
            </div>
            <div class="px-6 py-24 sm:px-12 sm:py-32 lg:px-16">
                 <div class="mx-auto max-w-2xl lg:mx-0">
                    <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Join our team</h2>
                    <p class="mt-6 text-lg leading-8 text-gray-600">We are always looking for talented individuals to join our growing team.</p>
                     <ul role="list" class="mt-10 grid grid-cols-1 gap-x-8 gap-y-8 sm:grid-cols-2">
                        <li>
                            <h3 class="text-base font-semibold leading-7 tracking-tight text-gray-900">Perks</h3>
                            <p class="text-sm leading-6 text-gray-600">Remote work, health insurance, 401k matching.</p>
                        </li>
                         <li>
                            <h3 class="text-base font-semibold leading-7 tracking-tight text-gray-900">Culture</h3>
                            <p class="text-sm leading-6 text-gray-600">Collaborative, inclusive, and fun environment.</p>
                        </li>
                        <li>
                            <h3 class="text-base font-semibold leading-7 tracking-tight text-gray-900">Growth</h3>
                            <p class="text-sm leading-6 text-gray-600">Professional development budget and mentorship.</p>
                        </li>
                         <li>
                            <h3 class="text-base font-semibold leading-7 tracking-tight text-gray-900">Impact</h3>
                            <p class="text-sm leading-6 text-gray-600">Work on projects that matter to millions of users.</p>
                        </li>
                     </ul>
                     <div class="mt-10 flex items-center gap-x-6">
                        <a href="#" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">See open positions</a>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-040",
        "title": "Blurred Background Cards",
        "description": "Cards with blurred backdrop filter.",
        "dir": "templates/08-team",
        "content": """
    <div class="relative isolate overflow-hidden bg-gray-900 py-24 sm:py-32">
       <img src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=2830&q=80&blend=111827&sat=-100&exp=15&blend-mode=multiply" alt="" class="absolute inset-0 -z-10 h-full w-full object-cover">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Our Leaders</h2>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          <li class="group">
             <div class="relative overflow-hidden rounded-2xl bg-white/5 p-8 backdrop-blur-sm ring-1 ring-white/10 transition-all hover:bg-white/10">
                <img class="h-24 w-24 rounded-full bg-gray-800 object-cover mb-6 border-2 border-white/20" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-semibold leading-8 text-white">Leslie Alexander</h3>
                <p class="text-base leading-7 text-gray-300">Co-Founder / CEO</p>
             </div>
          </li>
           <li class="group">
             <div class="relative overflow-hidden rounded-2xl bg-white/5 p-8 backdrop-blur-sm ring-1 ring-white/10 transition-all hover:bg-white/10">
                <img class="h-24 w-24 rounded-full bg-gray-800 object-cover mb-6 border-2 border-white/20" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-semibold leading-8 text-white">Michael Foster</h3>
                <p class="text-base leading-7 text-gray-300">Co-Founder / CTO</p>
             </div>
          </li>
           <li class="group">
             <div class="relative overflow-hidden rounded-2xl bg-white/5 p-8 backdrop-blur-sm ring-1 ring-white/10 transition-all hover:bg-white/10">
                <img class="h-24 w-24 rounded-full bg-gray-800 object-cover mb-6 border-2 border-white/20" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                <h3 class="text-lg font-semibold leading-8 text-white">Dries Vincent</h3>
                <p class="text-base leading-7 text-gray-300">Business Relations</p>
             </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-041",
        "title": "Neon Glow Effect",
        "description": "Dark theme with neon accents.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-black py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-violet-500 sm:text-4xl text-center mb-16">Neon Squad</h2>
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
             <div class="relative p-1 rounded-2xl bg-gradient-to-r from-pink-600 to-violet-600 transition-transform hover:scale-105">
                <div class="bg-gray-900 rounded-xl p-6 h-full text-center">
                    <img class="w-20 h-20 rounded-full mx-auto mb-4 border-2 border-pink-500" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-white font-bold text-lg">Lindsay</h3>
                    <p class="text-violet-400 text-sm">Design</p>
                </div>
             </div>
             <div class="relative p-1 rounded-2xl bg-gradient-to-r from-cyan-500 to-blue-500 transition-transform hover:scale-105">
                <div class="bg-gray-900 rounded-xl p-6 h-full text-center">
                    <img class="w-20 h-20 rounded-full mx-auto mb-4 border-2 border-cyan-500" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-white font-bold text-lg">Michael</h3>
                    <p class="text-cyan-400 text-sm">Tech</p>
                </div>
             </div>
             <div class="relative p-1 rounded-2xl bg-gradient-to-r from-green-400 to-emerald-500 transition-transform hover:scale-105">
                <div class="bg-gray-900 rounded-xl p-6 h-full text-center">
                    <img class="w-20 h-20 rounded-full mx-auto mb-4 border-2 border-green-500" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-white font-bold text-lg">Dries</h3>
                    <p class="text-green-400 text-sm">Ops</p>
                </div>
             </div>
             <div class="relative p-1 rounded-2xl bg-gradient-to-r from-yellow-400 to-orange-500 transition-transform hover:scale-105">
                <div class="bg-gray-900 rounded-xl p-6 h-full text-center">
                    <img class="w-20 h-20 rounded-full mx-auto mb-4 border-2 border-yellow-500" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    <h3 class="text-white font-bold text-lg">Courtney</h3>
                    <p class="text-yellow-400 text-sm">Art</p>
                </div>
             </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-042",
        "title": "Brutalist Design",
        "description": "Bold borders and high contrast shadows.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-yellow-50 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-5xl font-black text-black mb-16 uppercase tracking-tight">The Team</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="bg-white border-2 border-black p-4 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[4px] hover:translate-y-[4px] hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all">
                <div class="aspect-square bg-gray-200 border-2 border-black mb-4 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all" alt="">
                </div>
                <h3 class="text-2xl font-black uppercase">Leslie</h3>
                <p class="font-mono text-sm border-t-2 border-black mt-2 pt-2">BOSS</p>
            </div>
             <div class="bg-white border-2 border-black p-4 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[4px] hover:translate-y-[4px] hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all">
                <div class="aspect-square bg-gray-200 border-2 border-black mb-4 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all" alt="">
                </div>
                <h3 class="text-2xl font-black uppercase">Michael</h3>
                <p class="font-mono text-sm border-t-2 border-black mt-2 pt-2">TECH</p>
            </div>
             <div class="bg-white border-2 border-black p-4 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[4px] hover:translate-y-[4px] hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all">
                <div class="aspect-square bg-gray-200 border-2 border-black mb-4 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all" alt="">
                </div>
                <h3 class="text-2xl font-black uppercase">Dries</h3>
                <p class="font-mono text-sm border-t-2 border-black mt-2 pt-2">DEV</p>
            </div>
             <div class="bg-white border-2 border-black p-4 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[4px] hover:translate-y-[4px] hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all">
                <div class="aspect-square bg-gray-200 border-2 border-black mb-4 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all" alt="">
                </div>
                <h3 class="text-2xl font-black uppercase">Courtney</h3>
                <p class="font-mono text-sm border-t-2 border-black mt-2 pt-2">DESIGN</p>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-043",
        "title": "Sketchbook Style",
        "description": "Hand-drawn feel.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-stone-100 py-24 sm:py-32 font-serif">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-stone-800 sm:text-4xl text-center mb-16 italic">Our Sketches</h2>
        <div class="grid grid-cols-1 gap-12 sm:grid-cols-2 lg:grid-cols-3">
             <div class="flex flex-col items-center">
                 <div class="relative">
                   <div class="absolute inset-0 bg-stone-300 rounded-full transform translate-x-1 translate-y-1"></div>
                   <img class="relative w-40 h-40 rounded-full object-cover border-2 border-stone-800" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="mt-6 text-xl font-bold text-stone-900 border-b-2 border-stone-800 pb-1">Leslie A.</h3>
                 <p class="mt-2 text-stone-600 italic">"Drawing the future"</p>
             </div>
             <div class="flex flex-col items-center">
                 <div class="relative">
                   <div class="absolute inset-0 bg-stone-300 rounded-full transform translate-x-1 translate-y-1"></div>
                   <img class="relative w-40 h-40 rounded-full object-cover border-2 border-stone-800" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="mt-6 text-xl font-bold text-stone-900 border-b-2 border-stone-800 pb-1">Michael F.</h3>
                 <p class="mt-2 text-stone-600 italic">"Sketching code"</p>
             </div>
             <div class="flex flex-col items-center">
                 <div class="relative">
                   <div class="absolute inset-0 bg-stone-300 rounded-full transform translate-x-1 translate-y-1"></div>
                   <img class="relative w-40 h-40 rounded-full object-cover border-2 border-stone-800" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                 </div>
                 <h3 class="mt-6 text-xl font-bold text-stone-900 border-b-2 border-stone-800 pb-1">Dries V.</h3>
                 <p class="mt-2 text-stone-600 italic">"Designing systems"</p>
             </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-044",
        "title": "Minimal Grid with Icons",
        "description": "Grid with social icons integrated cleanly.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Connect with us</h2>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-4">
          <li>
            <img class="aspect-[1/1] w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Leslie Alexander</h3>
            <div class="flex gap-4 mt-2">
                <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a>
                <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763h2.674v-8.59H3.668v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" /></svg></a>
            </div>
          </li>
           <li>
            <img class="aspect-[1/1] w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
             <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Michael Foster</h3>
             <div class="flex gap-4 mt-2">
                <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a>
            </div>
          </li>
           <li>
            <img class="aspect-[1/1] w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
             <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Dries Vincent</h3>
             <div class="flex gap-4 mt-2">
                <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a>
            </div>
          </li>
           <li>
            <img class="aspect-[1/1] w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
             <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Courtney Henry</h3>
             <div class="flex gap-4 mt-2">
                <a href="#" class="text-gray-400 hover:text-gray-500"><svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg></a>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    }
]


TEMPLATES_TEAM_NEW.extend(TEMPLATES_TEAM_PART_4a)

TEMPLATES_TEAM_PART_4b = [
    {
        "id": "team-045",
        "title": "Cards with Latest Post",
        "description": "Team card showing the latest article/post.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Authors</h2>
          <p class="mt-6 text-lg leading-8 text-gray-600">Meet the voices behind our blog.</p>
        </div>
        <div class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3">
            <article class="flex flex-col items-start">
               <div class="relative flex items-center gap-x-4 mb-4">
                  <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="h-10 w-10 rounded-full bg-gray-50">
                  <div class="text-sm leading-6">
                    <p class="font-semibold text-gray-900">
                      <a href="#">
                        <span class="absolute inset-0"></span>
                        Michael Foster
                      </a>
                    </p>
                    <p class="text-gray-600">Co-Founder</p>
                  </div>
                </div>
                <h3 class="mt-3 text-lg font-semibold leading-6 text-gray-900">
                  <a href="#">
                    Boost your conversion rate
                  </a>
                </h3>
                <p class="mt-5 line-clamp-3 text-sm leading-6 text-gray-600">Illo sint voluptas. Error voluptates culpa eligendi. Hic vel totam vitae illo. Non aliquid explicabo necessitatibus unde. Sed exercitationem placeat consectetur nulla deserunt vel. Iusto corrupti dicta.</p>
            </article>
             <article class="flex flex-col items-start">
               <div class="relative flex items-center gap-x-4 mb-4">
                  <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="h-10 w-10 rounded-full bg-gray-50">
                  <div class="text-sm leading-6">
                    <p class="font-semibold text-gray-900">
                      <a href="#">
                        <span class="absolute inset-0"></span>
                        Lindsay Walton
                      </a>
                    </p>
                    <p class="text-gray-600">Front-end Developer</p>
                  </div>
                </div>
                <h3 class="mt-3 text-lg font-semibold leading-6 text-gray-900">
                  <a href="#">
                    How to use search engine optimization to drive sales
                  </a>
                </h3>
                <p class="mt-5 line-clamp-3 text-sm leading-6 text-gray-600">Optio cumque autem voluntatem quae aut et ea quasi. Maiores est quasi sint quos imperdiet. Sed et quis voluptas sed ipsum. Architecto omnis perferendis.</p>
            </article>
             <article class="flex flex-col items-start">
               <div class="relative flex items-center gap-x-4 mb-4">
                  <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" class="h-10 w-10 rounded-full bg-gray-50">
                  <div class="text-sm leading-6">
                    <p class="font-semibold text-gray-900">
                      <a href="#">
                        <span class="absolute inset-0"></span>
                        Tom Cook
                      </a>
                    </p>
                    <p class="text-gray-600">Director of Product</p>
                  </div>
                </div>
                <h3 class="mt-3 text-lg font-semibold leading-6 text-gray-900">
                  <a href="#">
                    Improve your customer experience
                  </a>
                </h3>
                <p class="mt-5 line-clamp-3 text-sm leading-6 text-gray-600">Cupiditate maiores ullam eveniet adipisci in doloribus nulla minus. Voluptas iusto libero adipisci rem et corporis. Nostrum veritatis. Voluptas iusto libero adipisci.</p>
            </article>
        </div>
      </div>
    </div>"""
    },
    {
         "id": "team-046",
         "title": "Bento Grid Layout",
         "description": "Japanese bento box inspired grid.",
         "dir": "templates/08-team",
         "content": """
    <div class="bg-gray-100 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl mb-12">The Squad</h2>
        <div class="grid grid-cols-1 md:grid-cols-4 grid-rows-4 md:grid-rows-2 gap-4 h-[800px] md:h-[600px]">
            <!-- Large Item -->
            <div class="md:col-span-2 md:row-span-2 relative rounded-2xl overflow-hidden group">
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition-transform group-hover:scale-105" alt="">
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex flex-col justify-end p-6">
                    <h3 class="text-white text-2xl font-bold">The Engineering Team</h3>
                    <p class="text-gray-300">Building the core platform.</p>
                </div>
            </div>
            <!-- Medium Item -->
            <div class="md:col-span-1 md:row-span-1 relative rounded-2xl overflow-hidden group">
                 <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition-transform group-hover:scale-105" alt="">
                 <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-colors"></div>
                 <div class="absolute bottom-4 left-4">
                     <p class="text-white font-bold">Leslie</p>
                 </div>
            </div>
             <!-- Medium Item -->
            <div class="md:col-span-1 md:row-span-1 relative rounded-2xl overflow-hidden group">
                 <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition-transform group-hover:scale-105" alt="">
                 <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-colors"></div>
                  <div class="absolute bottom-4 left-4">
                     <p class="text-white font-bold">Michael</p>
                 </div>
            </div>
             <!-- Wide Item -->
            <div class="md:col-span-2 md:row-span-1 relative rounded-2xl overflow-hidden group">
                  <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover transition-transform group-hover:scale-105" alt="">
                 <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex flex-col justify-end p-6">
                    <h3 class="text-white text-xl font-bold">Design Studio</h3>
                    <p class="text-gray-300">Where magic happens.</p>
                </div>
            </div>
        </div>
      </div>
    </div>"""
    },
    {
        "id": "team-047",
        "title": "Profile with Status",
        "description": "Team list with a clear status indicator.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <li class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow">
            <div class="flex w-full items-center justify-between space-x-6 p-6">
              <div class="flex-1 truncate">
                <div class="flex items-center space-x-3">
                  <h3 class="truncate text-sm font-medium text-gray-900">Jane Cooper</h3>
                  <span class="inline-flex flex-shrink-0 items-center rounded-full bg-green-50 px-1.5 py-0.5 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Available</span>
                </div>
                <p class="mt-1 truncate text-sm text-gray-500">Regional Paradigm Technician</p>
              </div>
              <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
            </div>
          </li>
           <li class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow">
            <div class="flex w-full items-center justify-between space-x-6 p-6">
              <div class="flex-1 truncate">
                <div class="flex items-center space-x-3">
                  <h3 class="truncate text-sm font-medium text-gray-900">Cody Fisher</h3>
                   <span class="inline-flex flex-shrink-0 items-center rounded-full bg-red-50 px-1.5 py-0.5 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-600/20">Busy</span>
                </div>
                <p class="mt-1 truncate text-sm text-gray-500">Product Manager</p>
              </div>
              <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
            </div>
          </li>
           <li class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow">
            <div class="flex w-full items-center justify-between space-x-6 p-6">
              <div class="flex-1 truncate">
                <div class="flex items-center space-x-3">
                  <h3 class="truncate text-sm font-medium text-gray-900">Esther Howard</h3>
                   <span class="inline-flex flex-shrink-0 items-center rounded-full bg-yellow-50 px-1.5 py-0.5 text-xs font-medium text-yellow-800 ring-1 ring-inset ring-yellow-600/20">Away</span>
                </div>
                <p class="mt-1 truncate text-sm text-gray-500">Frontend Developer</p>
              </div>
              <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" src="https://images.unsplash.com/photo-1520813792240-56fc4a3765a7?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-048",
        "title": "Cards with Languages",
        "description": "Team members with languages spoken.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-gray-50 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <li class="col-span-1 flex flex-col text-center bg-white rounded-lg shadow divide-y divide-gray-200">
            <div class="flex-1 flex flex-col p-8">
              <img class="w-32 h-32 flex-shrink-0 mx-auto rounded-full" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
              <h3 class="mt-6 text-gray-900 text-sm font-medium">Leslie Alexander</h3>
              <dl class="mt-1 flex-grow flex flex-col justify-between">
                <dt class="sr-only">Title</dt>
                <dd class="text-gray-500 text-sm">Customer Support</dd>
                <dt class="sr-only">Role</dt>
                <dd class="mt-3">
                  <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">English</span>
                  <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">Spanish</span>
                </dd>
              </dl>
            </div>
          </li>
           <li class="col-span-1 flex flex-col text-center bg-white rounded-lg shadow divide-y divide-gray-200">
            <div class="flex-1 flex flex-col p-8">
              <img class="w-32 h-32 flex-shrink-0 mx-auto rounded-full" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
              <h3 class="mt-6 text-gray-900 text-sm font-medium">Michael Foster</h3>
              <dl class="mt-1 flex-grow flex flex-col justify-between">
                <dt class="sr-only">Title</dt>
                <dd class="text-gray-500 text-sm">Sales</dd>
                <dt class="sr-only">Role</dt>
                 <dd class="mt-3">
                  <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">English</span>
                  <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">French</span>
                   <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">German</span>
                </dd>
              </dl>
            </div>
          </li>
           <li class="col-span-1 flex flex-col text-center bg-white rounded-lg shadow divide-y divide-gray-200">
            <div class="flex-1 flex flex-col p-8">
              <img class="w-32 h-32 flex-shrink-0 mx-auto rounded-full" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60" alt="">
              <h3 class="mt-6 text-gray-900 text-sm font-medium">Dries Vincent</h3>
              <dl class="mt-1 flex-grow flex flex-col justify-between">
                <dt class="sr-only">Title</dt>
                <dd class="text-gray-500 text-sm">Technical Support</dd>
                <dt class="sr-only">Role</dt>
                 <dd class="mt-3">
                  <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">English</span>
                  <span class="px-2 py-1 text-green-800 text-xs font-medium bg-green-100 rounded-full">Dutch</span>
                </dd>
              </dl>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-049",
        "title": "Team with Pronouns",
        "description": "Inclusive team cards sharing pronouns.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Our Diverse Team</h2>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-4">
          <li>
            <img class="aspect-[1/1] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Leslie Alexander</h3>
            <p class="text-base leading-7 text-indigo-600">She/Her</p>
            <p class="text-sm leading-6 text-gray-600">Co-Founder / CEO</p>
          </li>
           <li>
            <img class="aspect-[1/1] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Michael Foster</h3>
            <p class="text-base leading-7 text-indigo-600">He/Him</p>
            <p class="text-sm leading-6 text-gray-600">Co-Founder / CTO</p>
          </li>
           <li>
            <img class="aspect-[1/1] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Dries Vincent</h3>
            <p class="text-base leading-7 text-indigo-600">He/They</p>
            <p class="text-sm leading-6 text-gray-600">Business Relations</p>
          </li>
           <li>
            <img class="aspect-[1/1] w-full rounded-2xl object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            <h3 class="mt-6 text-lg font-semibold leading-8 text-gray-900">Courtney Henry</h3>
            <p class="text-base leading-7 text-indigo-600">She/Her</p>
            <p class="text-sm leading-6 text-gray-600">Designer</p>
          </li>
        </ul>
      </div>
    </div>"""
    },
    {
        "id": "team-050",
        "title": "Simple Circle List Bio",
        "description": "Clean list with circle avatar and short bio.",
        "dir": "templates/08-team",
        "content": """
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <ul role="list" class="divide-y divide-gray-100">
          <li class="flex justify-between gap-x-6 py-5">
            <div class="flex min-w-0 gap-x-4">
              <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">Leslie Alexander</p>
                <p class="mt-1 truncate text-xs leading-5 text-gray-500">leslie.alexander@example.com</p>
                 <p class="mt-1 text-sm text-gray-600">Leslie focuses on the long-term strategy and health of the company.</p>
              </div>
            </div>
            <div class="hidden sm:flex sm:flex-col sm:items-end">
              <p class="text-sm leading-6 text-gray-900">Co-Founder / CEO</p>
            </div>
          </li>
           <li class="flex justify-between gap-x-6 py-5">
            <div class="flex min-w-0 gap-x-4">
              <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">Michael Foster</p>
                <p class="mt-1 truncate text-xs leading-5 text-gray-500">michael.foster@example.com</p>
                 <p class="mt-1 text-sm text-gray-600">Michael leads the engineering and product teams.</p>
              </div>
            </div>
            <div class="hidden sm:flex sm:flex-col sm:items-end">
              <p class="text-sm leading-6 text-gray-900">Co-Founder / CTO</p>
            </div>
          </li>
           <li class="flex justify-between gap-x-6 py-5">
            <div class="flex min-w-0 gap-x-4">
              <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
              <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">Dries Vincent</p>
                <p class="mt-1 truncate text-xs leading-5 text-gray-500">dries.vincent@example.com</p>
                 <p class="mt-1 text-sm text-gray-600">Dries handles all our partner and business relationships.</p>
              </div>
            </div>
            <div class="hidden sm:flex sm:flex-col sm:items-end">
              <p class="text-sm leading-6 text-gray-900">Business Relations</p>
            </div>
          </li>
        </ul>
      </div>
    </div>"""
    }
]

TEMPLATES_TEAM_NEW.extend(TEMPLATES_TEAM_PART_4b)




