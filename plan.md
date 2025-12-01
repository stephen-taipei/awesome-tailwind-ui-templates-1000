# Tailwind UI Templates 1000 - Development Plan

> Complete specification for 1000 UI templates organized into 20 categories

---

## Table of Contents

1. [Category Architecture](#category-architecture)
2. [Template Specifications](#template-specifications)
   - [01. Navigation (nav-001 ~ nav-050)](#01-navigation)
   - [02. Hero Sections (hero-001 ~ hero-050)](#02-hero-sections)
   - [03. Features (feat-001 ~ feat-050)](#03-features)
   - [04. Content Sections (content-001 ~ content-050)](#04-content-sections)
   - [05. CTA (cta-001 ~ cta-050)](#05-cta-call-to-action)
   - [06. Pricing (price-001 ~ price-050)](#06-pricing)
   - [07. Testimonials (test-001 ~ test-050)](#07-testimonials)
   - [08. Team (team-001 ~ team-050)](#08-team)
   - [09. Gallery (gallery-001 ~ gallery-050)](#09-gallery)
   - [10. Forms (form-001 ~ form-050)](#10-forms)
   - [11. Cards (card-001 ~ card-050)](#11-cards)
   - [12. Lists (list-001 ~ list-050)](#12-lists)
   - [13. Modals & Dialogs (modal-001 ~ modal-050)](#13-modals--dialogs)
   - [14. Notifications (notif-001 ~ notif-050)](#14-notifications)
   - [15. Footers (footer-001 ~ footer-050)](#15-footers)
   - [16. Authentication (auth-001 ~ auth-050)](#16-authentication)
   - [17. Dashboard (dash-001 ~ dash-050)](#17-dashboard)
   - [18. E-commerce (ecom-001 ~ ecom-050)](#18-e-commerce)
   - [19. Blog (blog-001 ~ blog-050)](#19-blog)
   - [20. Landing Pages (landing-001 ~ landing-050)](#20-landing-pages)
3. [Development Progress](#development-progress)

---

## Category Architecture

### Naming Convention

```
{category-prefix}-{number}.html

Examples:
- nav-001.html
- hero-025.html
- card-050.html
```

### Category Prefixes

| # | Category | Prefix | Range |
|---|----------|--------|-------|
| 01 | Navigation | `nav` | 001-050 |
| 02 | Hero Sections | `hero` | 001-050 |
| 03 | Features | `feat` | 001-050 |
| 04 | Content Sections | `content` | 001-050 |
| 05 | CTA | `cta` | 001-050 |
| 06 | Pricing | `price` | 001-050 |
| 07 | Testimonials | `test` | 001-050 |
| 08 | Team | `team` | 001-050 |
| 09 | Gallery | `gallery` | 001-050 |
| 10 | Forms | `form` | 001-050 |
| 11 | Cards | `card` | 001-050 |
| 12 | Lists | `list` | 001-050 |
| 13 | Modals & Dialogs | `modal` | 001-050 |
| 14 | Notifications | `notif` | 001-050 |
| 15 | Footers | `footer` | 001-050 |
| 16 | Authentication | `auth` | 001-050 |
| 17 | Dashboard | `dash` | 001-050 |
| 18 | E-commerce | `ecom` | 001-050 |
| 19 | Blog | `blog` | 001-050 |
| 20 | Landing Pages | `landing` | 001-050 |

---

## Template Specifications

---

## 01. Navigation

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Top Navigation Bars | Horizontal header navbars |
| 011-020 | Sidebar Navigation | Vertical side menus |
| 021-030 | Mobile Navigation | Hamburger menus, bottom nav |
| 031-040 | Mega Menus | Complex dropdown menus |
| 041-050 | Breadcrumbs & Tabs | Secondary navigation |

### Template Details

#### nav-001: Simple Centered Navbar
- **Purpose**: Minimalist centered navigation for portfolios and landing pages
- **Structure**: `<header>` → `<nav>` → `<ul>` with centered flex layout
- **Tailwind Utilities**: `flex justify-center items-center gap-8 py-4 bg-white shadow-sm`
- **Responsive**: Stack vertically on mobile with hamburger toggle
- **Status**: `[ ] Pending`

#### nav-002: Logo Left + Links Right Navbar
- **Purpose**: Standard corporate/SaaS navigation pattern
- **Structure**: `<header>` → Logo div + nav links + CTA button
- **Tailwind Utilities**: `flex justify-between items-center px-6 lg:px-8 py-4`
- **Responsive**: Collapse to hamburger on `md` breakpoint
- **Status**: `[ ] Pending`

#### nav-003: Transparent Navbar with Scroll Effect
- **Purpose**: Hero overlay navigation with scroll-triggered background
- **Structure**: `<header class="fixed">` with JS scroll listener
- **Tailwind Utilities**: `fixed top-0 w-full transition-colors duration-300 bg-transparent`
- **Responsive**: Full width, mobile hamburger
- **Status**: `[ ] Pending`

#### nav-004: Dark Mode Navbar
- **Purpose**: Dark-themed navigation for tech/gaming sites
- **Structure**: Standard navbar with dark color scheme
- **Tailwind Utilities**: `bg-slate-900 text-white border-b border-slate-800`
- **Responsive**: Standard responsive pattern
- **Status**: `[ ] Pending`

#### nav-005: Navbar with Search Box
- **Purpose**: Navigation with integrated search functionality
- **Structure**: Logo + nav links + search input + user actions
- **Tailwind Utilities**: `flex items-center gap-4` + input styling
- **Responsive**: Search collapses to icon on mobile
- **Status**: `[ ] Pending`

#### nav-006: Navbar with Dropdown Menus
- **Purpose**: Multi-level navigation with dropdown submenus
- **Structure**: Nav items with nested `<ul>` dropdowns
- **Tailwind Utilities**: `group relative` + `group-hover:block hidden absolute`
- **Responsive**: Dropdowns become accordion on mobile
- **Status**: `[ ] Pending`

#### nav-007: Navbar with User Avatar Menu
- **Purpose**: Authenticated user navigation with profile dropdown
- **Structure**: Main nav + avatar with dropdown menu
- **Tailwind Utilities**: `relative` avatar container with dropdown
- **Responsive**: Avatar menu remains on mobile
- **Status**: `[ ] Pending`

#### nav-008: Dual Row Navbar
- **Purpose**: Complex navigation with top utility bar
- **Structure**: Top bar (contact/social) + main navbar
- **Tailwind Utilities**: Two stacked flex rows
- **Responsive**: Top bar hidden on mobile
- **Status**: `[ ] Pending`

#### nav-009: Sticky Navbar
- **Purpose**: Always-visible navigation on scroll
- **Structure**: `<header class="sticky top-0">`
- **Tailwind Utilities**: `sticky top-0 z-50 bg-white/95 backdrop-blur`
- **Responsive**: Standard pattern
- **Status**: `[ ] Pending`

#### nav-010: Navbar with Notification Badge
- **Purpose**: Navigation with notification indicators
- **Structure**: Nav items with badge counters
- **Tailwind Utilities**: `relative` + `absolute -top-1 -right-1` badge
- **Responsive**: Badges remain visible
- **Status**: `[ ] Pending`

#### nav-011: Basic Sidebar
- **Purpose**: Simple vertical sidebar navigation
- **Structure**: `<aside>` with vertical nav list
- **Tailwind Utilities**: `w-64 h-screen bg-white border-r flex flex-col`
- **Responsive**: Overlay drawer on mobile
- **Status**: `[ ] Pending`

#### nav-012: Sidebar with Icons
- **Purpose**: Icon-labeled sidebar navigation
- **Structure**: Icon + label for each nav item
- **Tailwind Utilities**: `flex items-center gap-3 px-4 py-3`
- **Responsive**: Icons-only on tablet, drawer on mobile
- **Status**: `[ ] Pending`

#### nav-013: Collapsible Sidebar
- **Purpose**: Expandable/collapsible sidebar (icons to full)
- **Structure**: Sidebar with collapse toggle
- **Tailwind Utilities**: `w-16 lg:w-64 transition-all duration-300`
- **Responsive**: Auto-collapse based on viewport
- **Status**: `[ ] Pending`

#### nav-014: Sidebar with Nested Menu
- **Purpose**: Multi-level sidebar with accordion submenus
- **Structure**: Parent items with collapsible children
- **Tailwind Utilities**: Accordion pattern with `max-h-0` toggle
- **Responsive**: Full sidebar on desktop, drawer on mobile
- **Status**: `[ ] Pending`

#### nav-015: Dark Sidebar
- **Purpose**: Dark-themed sidebar for dashboards
- **Structure**: Standard sidebar with dark colors
- **Tailwind Utilities**: `bg-slate-900 text-slate-300`
- **Responsive**: Same as light variant
- **Status**: `[ ] Pending`

#### nav-016: Sidebar with Header Logo
- **Purpose**: Branded sidebar with logo section
- **Structure**: Logo header + nav items + footer
- **Tailwind Utilities**: `flex flex-col h-full` with logo at top
- **Responsive**: Logo remains in mobile drawer
- **Status**: `[ ] Pending`

#### nav-017: Sidebar with User Profile
- **Purpose**: Sidebar with user info section
- **Structure**: User avatar/name section + navigation
- **Tailwind Utilities**: Profile card styling at top/bottom
- **Responsive**: Profile compact on mobile
- **Status**: `[ ] Pending`

#### nav-018: Sidebar with Search
- **Purpose**: Searchable sidebar navigation
- **Structure**: Search input + filterable nav items
- **Tailwind Utilities**: Input with icon + scrollable nav
- **Responsive**: Search persists in drawer
- **Status**: `[ ] Pending`

#### nav-019: Sidebar with Sections
- **Purpose**: Grouped sidebar with section headers
- **Structure**: Multiple nav groups with headings
- **Tailwind Utilities**: Section headers with `text-xs uppercase tracking-wider`
- **Responsive**: Sections preserved
- **Status**: `[ ] Pending`

#### nav-020: Mini Sidebar (Icons Only)
- **Purpose**: Compact icon-only sidebar with tooltips
- **Structure**: Icons with hover tooltips
- **Tailwind Utilities**: `w-16` fixed + tooltip on hover
- **Responsive**: Bottom nav on mobile
- **Status**: `[ ] Pending`

#### nav-021: Mobile Hamburger Menu
- **Purpose**: Classic hamburger menu for mobile
- **Structure**: Hamburger icon + slide-out menu
- **Tailwind Utilities**: Hamburger animation + `translate-x` slide
- **Responsive**: Mobile-only component
- **Status**: `[ ] Pending`

#### nav-022: Mobile Full-Screen Menu
- **Purpose**: Full viewport overlay menu
- **Structure**: Full-screen overlay with centered nav
- **Tailwind Utilities**: `fixed inset-0 bg-white z-50`
- **Responsive**: Mobile-only
- **Status**: `[ ] Pending`

#### nav-023: Mobile Bottom Navigation
- **Purpose**: iOS/Android style bottom tab bar
- **Structure**: Fixed bottom bar with icon tabs
- **Tailwind Utilities**: `fixed bottom-0 w-full bg-white border-t`
- **Responsive**: Mobile-only, hidden on desktop
- **Status**: `[ ] Pending`

#### nav-024: Mobile Slide-In Drawer
- **Purpose**: Side drawer navigation (left or right)
- **Structure**: Off-canvas drawer with backdrop
- **Tailwind Utilities**: `translate-x-full` → `translate-x-0` transition
- **Responsive**: Mobile/tablet only
- **Status**: `[ ] Pending`

#### nav-025: Mobile Accordion Menu
- **Purpose**: Expandable accordion menu for mobile
- **Structure**: Collapsible sections
- **Tailwind Utilities**: Accordion `max-height` transitions
- **Responsive**: Mobile primary navigation
- **Status**: `[ ] Pending`

#### nav-026: Mobile App-Style Navigation
- **Purpose**: Native app feel navigation
- **Structure**: Header bar + content + bottom nav
- **Tailwind Utilities**: Safe area insets for notched phones
- **Responsive**: Mobile-only
- **Status**: `[ ] Pending`

#### nav-027: Mobile Floating Action Menu
- **Purpose**: FAB with expandable menu
- **Structure**: Floating button with radial/vertical menu
- **Tailwind Utilities**: `fixed bottom-4 right-4` + transform animations
- **Responsive**: Mobile/tablet
- **Status**: `[ ] Pending`

#### nav-028: Mobile Tab Bar with Labels
- **Purpose**: Bottom tabs with icon + text
- **Structure**: Tab items with icon and label
- **Tailwind Utilities**: `flex flex-col items-center gap-1`
- **Responsive**: Mobile-only
- **Status**: `[ ] Pending`

#### nav-029: Mobile Search Header
- **Purpose**: Mobile header with search focus
- **Structure**: Back button + search input + actions
- **Tailwind Utilities**: Sticky header with full-width search
- **Responsive**: Mobile-only
- **Status**: `[ ] Pending`

#### nav-030: Mobile Contextual Navigation
- **Purpose**: Context-aware mobile navigation
- **Structure**: Dynamic nav based on scroll/context
- **Tailwind Utilities**: Conditional visibility classes
- **Responsive**: Mobile-only
- **Status**: `[ ] Pending`

#### nav-031: Basic Mega Menu
- **Purpose**: Large dropdown with columns
- **Structure**: Full-width dropdown panel
- **Tailwind Utilities**: `absolute left-0 w-full` dropdown
- **Responsive**: Standard dropdown on mobile
- **Status**: `[ ] Pending`

#### nav-032: Mega Menu with Images
- **Purpose**: Visual mega menu with product images
- **Structure**: Grid layout with image cards
- **Tailwind Utilities**: Grid columns with image thumbnails
- **Responsive**: Simplified on mobile
- **Status**: `[ ] Pending`

#### nav-033: Mega Menu with Categories
- **Purpose**: E-commerce category mega menu
- **Structure**: Category columns with links
- **Tailwind Utilities**: Multi-column grid layout
- **Responsive**: Accordion on mobile
- **Status**: `[ ] Pending`

#### nav-034: Mega Menu with Featured Content
- **Purpose**: Mega menu with promotional area
- **Structure**: Nav columns + featured banner
- **Tailwind Utilities**: Grid with featured highlight area
- **Responsive**: Featured hidden on mobile
- **Status**: `[ ] Pending`

#### nav-035: Mega Menu with Tabs
- **Purpose**: Tabbed mega menu sections
- **Structure**: Tab headers + content panels
- **Tailwind Utilities**: Tab navigation pattern
- **Responsive**: Vertical tabs on mobile
- **Status**: `[ ] Pending`

#### nav-036: Mega Menu with Search
- **Purpose**: Mega menu with search functionality
- **Structure**: Search prominent + results/suggestions
- **Tailwind Utilities**: Large search input + dropdown results
- **Responsive**: Full search on mobile
- **Status**: `[ ] Pending`

#### nav-037: Mega Menu with Icons
- **Purpose**: Icon-rich mega menu
- **Structure**: Icon + label grid items
- **Tailwind Utilities**: Icon grid with descriptions
- **Responsive**: List format on mobile
- **Status**: `[ ] Pending`

#### nav-038: Mega Menu Dark Theme
- **Purpose**: Dark-themed mega menu
- **Structure**: Standard mega menu with dark colors
- **Tailwind Utilities**: `bg-slate-900 text-white` dropdown
- **Responsive**: Same as light
- **Status**: `[ ] Pending`

#### nav-039: Mega Menu with Promo Banner
- **Purpose**: Mega menu with advertisement space
- **Structure**: Nav content + promo sidebar
- **Tailwind Utilities**: Sidebar ad placement
- **Responsive**: Promo hidden on mobile
- **Status**: `[ ] Pending`

#### nav-040: Animated Mega Menu
- **Purpose**: Mega menu with entrance animations
- **Structure**: Standard + animation classes
- **Tailwind Utilities**: `animate-` classes + transforms
- **Responsive**: Reduced motion option
- **Status**: `[ ] Pending`

#### nav-041: Basic Breadcrumb
- **Purpose**: Simple breadcrumb trail
- **Structure**: `<nav>` with `<ol>` list
- **Tailwind Utilities**: `flex items-center gap-2 text-sm`
- **Responsive**: Truncate middle items on mobile
- **Status**: `[ ] Pending`

#### nav-042: Breadcrumb with Icons
- **Purpose**: Breadcrumb with icon separators
- **Structure**: Items with chevron/arrow icons
- **Tailwind Utilities**: Icon sizing and spacing
- **Responsive**: Compact on mobile
- **Status**: `[ ] Pending`

#### nav-043: Breadcrumb with Dropdown
- **Purpose**: Breadcrumb with expandable levels
- **Structure**: Dropdown for deep hierarchies
- **Tailwind Utilities**: Dropdown pattern for overflow
- **Responsive**: Dropdown for all on mobile
- **Status**: `[ ] Pending`

#### nav-044: Basic Tabs
- **Purpose**: Horizontal tab navigation
- **Structure**: Tab list + content panels
- **Tailwind Utilities**: `border-b` tabs with active state
- **Responsive**: Scrollable on mobile
- **Status**: `[ ] Pending`

#### nav-045: Pill Tabs
- **Purpose**: Pill-style tab buttons
- **Structure**: Rounded tab buttons
- **Tailwind Utilities**: `rounded-full bg-primary` active tab
- **Responsive**: Scrollable or dropdown
- **Status**: `[ ] Pending`

#### nav-046: Underline Tabs
- **Purpose**: Minimal underline indicator tabs
- **Structure**: Tabs with animated underline
- **Tailwind Utilities**: `border-b-2 border-primary` active
- **Responsive**: Scrollable
- **Status**: `[ ] Pending`

#### nav-047: Vertical Tabs
- **Purpose**: Side-positioned vertical tabs
- **Structure**: Vertical tab list + content area
- **Tailwind Utilities**: `flex-col` tabs on left
- **Responsive**: Horizontal on mobile
- **Status**: `[ ] Pending`

#### nav-048: Icon Tabs
- **Purpose**: Tabs with icons
- **Structure**: Icon + label tab items
- **Tailwind Utilities**: Icon above/beside label
- **Responsive**: Icons only on mobile
- **Status**: `[ ] Pending`

#### nav-049: Segmented Control
- **Purpose**: iOS-style segmented control
- **Structure**: Connected button group
- **Tailwind Utilities**: `rounded-lg overflow-hidden` group
- **Responsive**: Full width on mobile
- **Status**: `[ ] Pending`

#### nav-050: Step Navigation
- **Purpose**: Progress step indicator
- **Structure**: Numbered/icon steps with connector
- **Tailwind Utilities**: Step circles with connecting lines
- **Responsive**: Vertical on mobile
- **Status**: `[ ] Pending`

---

## 02. Hero Sections

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Image Background | Photo/image backgrounds |
| 011-020 | Video Background | Video backgrounds |
| 021-030 | Gradient | Gradient backgrounds |
| 031-040 | Split Layout | Two-column heroes |
| 041-050 | Animated | Motion/animation heroes |

### Template Details

#### hero-001: Centered Hero with Image Background
- **Purpose**: Classic hero with centered text over image
- **Structure**: Full viewport section with overlay text
- **Tailwind Utilities**: `min-h-screen bg-cover bg-center` + overlay
- **Responsive**: Text size scales, maintains readability
- **Status**: `[ ] Pending`

#### hero-002: Left-Aligned Hero with Image
- **Purpose**: Text left, image as background
- **Structure**: Container with left-aligned content
- **Tailwind Utilities**: `text-left max-w-xl` content container
- **Responsive**: Centered on mobile
- **Status**: `[ ] Pending`

#### hero-003: Hero with Parallax Image
- **Purpose**: Parallax scrolling effect hero
- **Structure**: Fixed background with scroll effect
- **Tailwind Utilities**: `bg-fixed bg-cover`
- **Responsive**: Disable parallax on mobile for performance
- **Status**: `[ ] Pending`

#### hero-004: Hero with Multiple Images
- **Purpose**: Collage-style image background
- **Structure**: Grid of background images
- **Tailwind Utilities**: Grid or absolute positioned images
- **Responsive**: Single image on mobile
- **Status**: `[ ] Pending`

#### hero-005: Hero with Image Overlay Pattern
- **Purpose**: Patterned overlay on image
- **Structure**: Image + SVG/CSS pattern overlay
- **Tailwind Utilities**: `bg-blend-overlay` or pseudo-element
- **Responsive**: Pattern scales appropriately
- **Status**: `[ ] Pending`

#### hero-006: Hero with Blurred Image
- **Purpose**: Blurred background image hero
- **Structure**: Image with blur filter
- **Tailwind Utilities**: `backdrop-blur-sm` or `blur` on image
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-007: Hero with Image Carousel
- **Purpose**: Rotating background images
- **Structure**: Carousel/slider with transitions
- **Tailwind Utilities**: CSS transitions between images
- **Responsive**: Touch-friendly swipe
- **Status**: `[ ] Pending`

#### hero-008: Hero with Ken Burns Effect
- **Purpose**: Slow zoom animation on image
- **Structure**: Image with scale animation
- **Tailwind Utilities**: `animate-` with scale transform
- **Responsive**: Reduced motion support
- **Status**: `[ ] Pending`

#### hero-009: Hero with Dark Overlay
- **Purpose**: Dark gradient over image
- **Structure**: Image + dark gradient overlay
- **Tailwind Utilities**: `bg-gradient-to-b from-black/60`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-010: Hero with Light Overlay
- **Purpose**: Light/white overlay on image
- **Structure**: Image + light overlay
- **Tailwind Utilities**: `bg-white/70` overlay
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-011: Full Video Background Hero
- **Purpose**: Full viewport video background
- **Structure**: `<video>` element with content overlay
- **Tailwind Utilities**: `object-cover w-full h-full absolute`
- **Responsive**: Fallback image on mobile
- **Status**: `[ ] Pending`

#### hero-012: Video with Play Button
- **Purpose**: Video thumbnail with play trigger
- **Structure**: Thumbnail + modal video player
- **Tailwind Utilities**: Play button centered overlay
- **Responsive**: Touch-friendly play area
- **Status**: `[ ] Pending`

#### hero-013: Looping Video Hero
- **Purpose**: Seamless looping background video
- **Structure**: `<video autoplay loop muted>`
- **Tailwind Utilities**: Standard video cover
- **Responsive**: Disable autoplay on mobile
- **Status**: `[ ] Pending`

#### hero-014: Video with Text Overlay
- **Purpose**: Video with prominent text
- **Structure**: Video + centered text block
- **Tailwind Utilities**: `z-10 relative` text layer
- **Responsive**: Text readable at all sizes
- **Status**: `[ ] Pending`

#### hero-015: Video Hero with CTA
- **Purpose**: Video background with call-to-action
- **Structure**: Video + CTA buttons
- **Tailwind Utilities**: CTA button styling over video
- **Responsive**: Large tap targets on mobile
- **Status**: `[ ] Pending`

#### hero-016: Split Video/Content Hero
- **Purpose**: Side-by-side video and content
- **Structure**: Grid with video and text columns
- **Tailwind Utilities**: `grid grid-cols-2` layout
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### hero-017: Video with Gradient Overlay
- **Purpose**: Video with gradient fade
- **Structure**: Video + gradient overlay
- **Tailwind Utilities**: Gradient from transparent to solid
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-018: Video Carousel Hero
- **Purpose**: Multiple video backgrounds
- **Structure**: Video slider/carousel
- **Tailwind Utilities**: Transition between videos
- **Responsive**: Single video on mobile
- **Status**: `[ ] Pending`

#### hero-019: Video with Sound Toggle
- **Purpose**: Video with audio control
- **Structure**: Video + mute/unmute button
- **Tailwind Utilities**: Audio icon button styling
- **Responsive**: Touch-friendly control
- **Status**: `[ ] Pending`

#### hero-020: YouTube/Vimeo Embed Hero
- **Purpose**: Embedded video service hero
- **Structure**: iframe embed with overlay content
- **Tailwind Utilities**: `aspect-video` container
- **Responsive**: Maintain aspect ratio
- **Status**: `[ ] Pending`

#### hero-021: Linear Gradient Hero
- **Purpose**: Simple linear gradient background
- **Structure**: Section with gradient background
- **Tailwind Utilities**: `bg-gradient-to-r from-blue-600 to-purple-600`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-022: Radial Gradient Hero
- **Purpose**: Radial gradient background
- **Structure**: CSS radial gradient
- **Tailwind Utilities**: Custom gradient via CSS variable
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-023: Multi-Color Gradient Hero
- **Purpose**: Complex multi-stop gradient
- **Structure**: Multiple color stops
- **Tailwind Utilities**: `via-` color stops
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-024: Animated Gradient Hero
- **Purpose**: Moving/shifting gradient
- **Structure**: CSS animation on gradient
- **Tailwind Utilities**: `animate-gradient` custom animation
- **Responsive**: Reduce motion option
- **Status**: `[ ] Pending`

#### hero-025: Gradient with Pattern
- **Purpose**: Gradient + decorative pattern
- **Structure**: Gradient background + SVG pattern
- **Tailwind Utilities**: Pattern overlay blend
- **Responsive**: Pattern may hide on mobile
- **Status**: `[ ] Pending`

#### hero-026: Mesh Gradient Hero
- **Purpose**: Mesh/blob gradient effect
- **Structure**: Multiple gradient blobs
- **Tailwind Utilities**: Absolute positioned gradient divs
- **Responsive**: Simplified on mobile
- **Status**: `[ ] Pending`

#### hero-027: Gradient with Noise Texture
- **Purpose**: Gradient + noise overlay
- **Structure**: Gradient + noise SVG filter
- **Tailwind Utilities**: Blend mode for texture
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-028: Dark Gradient Hero
- **Purpose**: Dark color gradient
- **Structure**: Dark color scheme gradient
- **Tailwind Utilities**: `from-slate-900 to-slate-800`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-029: Pastel Gradient Hero
- **Purpose**: Soft pastel gradient
- **Structure**: Light pastel colors
- **Tailwind Utilities**: `from-pink-100 to-blue-100`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-030: Gradient Border Hero
- **Purpose**: Hero with gradient border accent
- **Structure**: Content with gradient border
- **Tailwind Utilities**: Border gradient via pseudo-element
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-031: Image Left, Content Right
- **Purpose**: Classic split layout hero
- **Structure**: Two-column grid
- **Tailwind Utilities**: `grid grid-cols-1 lg:grid-cols-2 gap-12`
- **Responsive**: Stack on mobile (content first)
- **Status**: `[ ] Pending`

#### hero-032: Content Left, Image Right
- **Purpose**: Reversed split layout
- **Structure**: Two-column, reversed order
- **Tailwind Utilities**: `order-1 lg:order-2` for ordering
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### hero-033: Split with Angled Divider
- **Purpose**: Diagonal split between sections
- **Structure**: Angled clip-path divider
- **Tailwind Utilities**: `clip-path` polygon
- **Responsive**: Standard or simplified angle
- **Status**: `[ ] Pending`

#### hero-034: Split with Overlapping Image
- **Purpose**: Image overlaps into content area
- **Structure**: Negative margin overlap
- **Tailwind Utilities**: `-ml-12 lg:-ml-24` overlap
- **Responsive**: No overlap on mobile
- **Status**: `[ ] Pending`

#### hero-035: Split with Background Color
- **Purpose**: Different background colors per side
- **Structure**: Two backgrounds meeting
- **Tailwind Utilities**: Background color on each column
- **Responsive**: Single color on mobile
- **Status**: `[ ] Pending`

#### hero-036: Split with Stats
- **Purpose**: Split layout with statistics
- **Structure**: Content + stats grid
- **Tailwind Utilities**: Stats grid layout
- **Responsive**: Stats below content on mobile
- **Status**: `[ ] Pending`

#### hero-037: Split with Form
- **Purpose**: Content + form split
- **Structure**: Info section + form section
- **Tailwind Utilities**: Form styling in split
- **Responsive**: Form below content
- **Status**: `[ ] Pending`

#### hero-038: Split with Video
- **Purpose**: Content + video split
- **Structure**: Text column + video column
- **Tailwind Utilities**: Video embed in column
- **Responsive**: Video below content
- **Status**: `[ ] Pending`

#### hero-039: Three Column Split
- **Purpose**: Triple column hero layout
- **Structure**: Three equal columns
- **Tailwind Utilities**: `grid-cols-3` on desktop
- **Responsive**: Single column on mobile
- **Status**: `[ ] Pending`

#### hero-040: Split with App Mockup
- **Purpose**: Content + device mockup
- **Structure**: Text + phone/laptop mockup
- **Tailwind Utilities**: Device frame styling
- **Responsive**: Mockup scales or repositions
- **Status**: `[ ] Pending`

#### hero-041: Particle Animation Hero
- **Purpose**: Animated particles background
- **Structure**: Canvas/CSS particles
- **Tailwind Utilities**: Canvas positioning
- **Responsive**: Reduce particles on mobile
- **Status**: `[ ] Pending`

#### hero-042: Typing Animation Hero
- **Purpose**: Typewriter text effect
- **Structure**: JS typing animation
- **Tailwind Utilities**: Cursor blink animation
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-043: Scroll-Triggered Hero
- **Purpose**: Animations on scroll
- **Structure**: Intersection Observer triggers
- **Tailwind Utilities**: `animate-` classes triggered by scroll
- **Responsive**: Reduced animations on mobile
- **Status**: `[ ] Pending`

#### hero-044: 3D Tilt Effect Hero
- **Purpose**: Mouse-following 3D tilt
- **Structure**: Transform on mouse move
- **Tailwind Utilities**: `transform perspective-1000`
- **Responsive**: Disable on touch devices
- **Status**: `[ ] Pending`

#### hero-045: Floating Elements Hero
- **Purpose**: Floating animated decorations
- **Structure**: Absolute positioned elements
- **Tailwind Utilities**: `animate-bounce` or custom float
- **Responsive**: Fewer elements on mobile
- **Status**: `[ ] Pending`

#### hero-046: Counter Animation Hero
- **Purpose**: Animated number counters
- **Structure**: Count-up animation on numbers
- **Tailwind Utilities**: Number styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-047: Morphing Shape Hero
- **Purpose**: SVG shape morphing animation
- **Structure**: Animated SVG paths
- **Tailwind Utilities**: SVG positioning and sizing
- **Responsive**: Simpler shapes on mobile
- **Status**: `[ ] Pending`

#### hero-048: Glitch Effect Hero
- **Purpose**: Glitch/distortion text effect
- **Structure**: Layered text with offset
- **Tailwind Utilities**: Pseudo-elements for layers
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### hero-049: Parallax Layers Hero
- **Purpose**: Multi-layer parallax scrolling
- **Structure**: Stacked layers with different speeds
- **Tailwind Utilities**: Transform on scroll
- **Responsive**: Reduced layers on mobile
- **Status**: `[ ] Pending`

#### hero-050: Interactive Hero
- **Purpose**: User interaction responsive hero
- **Structure**: Mouse/touch reactive elements
- **Tailwind Utilities**: Transition classes for interactions
- **Responsive**: Touch-friendly interactions
- **Status**: `[ ] Pending`

---

## 03. Features

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Grid Features | Feature grids |
| 011-020 | List Features | Vertical feature lists |
| 021-030 | Icon Features | Icon-focused displays |
| 031-040 | Card Features | Feature cards |
| 041-050 | Alternating | Zigzag/alternating layouts |

### Template Details

#### feat-001: 3-Column Feature Grid
- **Purpose**: Standard three feature highlight
- **Structure**: 3-column grid with icon, title, description
- **Tailwind Utilities**: `grid grid-cols-1 md:grid-cols-3 gap-8`
- **Responsive**: Single column on mobile
- **Status**: `[ ] Pending`

#### feat-002: 4-Column Feature Grid
- **Purpose**: Four feature display
- **Structure**: 4-column responsive grid
- **Tailwind Utilities**: `grid-cols-2 lg:grid-cols-4`
- **Responsive**: 2 columns tablet, 1 mobile
- **Status**: `[ ] Pending`

#### feat-003: 6-Column Feature Grid
- **Purpose**: Many small features
- **Structure**: 6-column grid
- **Tailwind Utilities**: `grid-cols-2 md:grid-cols-3 lg:grid-cols-6`
- **Responsive**: Progressive column reduction
- **Status**: `[ ] Pending`

#### feat-004: Feature Grid with Images
- **Purpose**: Image-based feature grid
- **Structure**: Grid with image + text per item
- **Tailwind Utilities**: Image sizing within grid
- **Responsive**: Standard grid responsive
- **Status**: `[ ] Pending`

#### feat-005: Feature Grid with Numbers
- **Purpose**: Numbered feature steps
- **Structure**: Number badge + feature content
- **Tailwind Utilities**: `w-10 h-10 rounded-full` number badge
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-006: Feature Grid Centered
- **Purpose**: Centered text feature grid
- **Structure**: Center-aligned grid items
- **Tailwind Utilities**: `text-center` items
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-007: Feature Grid with Background
- **Purpose**: Colored background feature grid
- **Structure**: Alternating or solid backgrounds
- **Tailwind Utilities**: Background colors per item
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-008: Feature Grid with Hover Effects
- **Purpose**: Interactive hover states
- **Structure**: Transform/color on hover
- **Tailwind Utilities**: `hover:scale-105 hover:shadow-lg transition`
- **Responsive**: Focus states for touch
- **Status**: `[ ] Pending`

#### feat-009: Masonry Feature Grid
- **Purpose**: Pinterest-style masonry layout
- **Structure**: CSS columns or masonry grid
- **Tailwind Utilities**: `columns-3` or CSS grid masonry
- **Responsive**: Fewer columns on smaller screens
- **Status**: `[ ] Pending`

#### feat-010: Bento Grid Features
- **Purpose**: Bento box style varied sizes
- **Structure**: Mixed size grid items
- **Tailwind Utilities**: `col-span-2`, `row-span-2` variants
- **Responsive**: Simplified on mobile
- **Status**: `[ ] Pending`

#### feat-011: Simple Feature List
- **Purpose**: Vertical feature list
- **Structure**: Stacked feature items
- **Tailwind Utilities**: `space-y-6` vertical spacing
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-012: Feature List with Checkmarks
- **Purpose**: Checklist style features
- **Structure**: Check icon + feature text
- **Tailwind Utilities**: Check icon styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-013: Feature List with Descriptions
- **Purpose**: Title + description list
- **Structure**: Heading + paragraph per item
- **Tailwind Utilities**: Typography hierarchy
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-014: Feature List with Images
- **Purpose**: Image + text list items
- **Structure**: Horizontal image + content
- **Tailwind Utilities**: `flex items-start gap-4`
- **Responsive**: Stack image on mobile
- **Status**: `[ ] Pending`

#### feat-015: Numbered Feature List
- **Purpose**: Sequential numbered features
- **Structure**: Number + content list
- **Tailwind Utilities**: Counter styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-016: Feature List with Dividers
- **Purpose**: Separated feature items
- **Structure**: Items with border dividers
- **Tailwind Utilities**: `divide-y` or border-bottom
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-017: Expandable Feature List
- **Purpose**: Accordion feature list
- **Structure**: Click to expand details
- **Tailwind Utilities**: Accordion pattern
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-018: Feature List Two Columns
- **Purpose**: Side-by-side feature lists
- **Structure**: Two column list layout
- **Tailwind Utilities**: `grid grid-cols-2` list
- **Responsive**: Single column mobile
- **Status**: `[ ] Pending`

#### feat-019: Feature List with Progress
- **Purpose**: Features with progress indicators
- **Structure**: Feature + progress bar
- **Tailwind Utilities**: Progress bar styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-020: Timeline Feature List
- **Purpose**: Vertical timeline layout
- **Structure**: Timeline line with nodes
- **Tailwind Utilities**: Pseudo-element line connector
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-021: Large Icon Features
- **Purpose**: Prominent icon display
- **Structure**: Large icon + text below
- **Tailwind Utilities**: `w-16 h-16` icon sizing
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-022: Circular Icon Features
- **Purpose**: Icons in circles
- **Structure**: Circle background + icon
- **Tailwind Utilities**: `rounded-full p-4 bg-primary/10`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-023: Square Icon Features
- **Purpose**: Icons in squares
- **Structure**: Square container + icon
- **Tailwind Utilities**: `rounded-lg p-4`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-024: Gradient Icon Features
- **Purpose**: Icons with gradient backgrounds
- **Structure**: Gradient circle/square + icon
- **Tailwind Utilities**: Gradient background behind icon
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-025: Outline Icon Features
- **Purpose**: Stroke/outline style icons
- **Structure**: Outline icons with thin strokes
- **Tailwind Utilities**: Heroicons outline variant
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-026: Animated Icon Features
- **Purpose**: Icons with hover animations
- **Structure**: Transform on interaction
- **Tailwind Utilities**: `hover:rotate-12 transition`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-027: Dual-Tone Icon Features
- **Purpose**: Two-color icon treatment
- **Structure**: Primary + secondary colors
- **Tailwind Utilities**: Dual color icon styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-028: Icon Features with Badges
- **Purpose**: Icons with notification badges
- **Structure**: Icon + corner badge
- **Tailwind Utilities**: Absolute positioned badge
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-029: Icon Features Horizontal
- **Purpose**: Icon left, text right
- **Structure**: Horizontal icon + text layout
- **Tailwind Utilities**: `flex items-center gap-4`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-030: Icon Features with Lines
- **Purpose**: Connected icons with lines
- **Structure**: Icons connected by decorative lines
- **Tailwind Utilities**: Border or SVG connectors
- **Responsive**: Lines hidden on mobile
- **Status**: `[ ] Pending`

#### feat-031: Basic Feature Cards
- **Purpose**: Cards for each feature
- **Structure**: Card container per feature
- **Tailwind Utilities**: `rounded-xl shadow-lg p-6`
- **Responsive**: Standard grid responsive
- **Status**: `[ ] Pending`

#### feat-032: Feature Cards with Image Header
- **Purpose**: Image at top of card
- **Structure**: Image + content in card
- **Tailwind Utilities**: `rounded-t-xl` image
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-033: Feature Cards with Icon Header
- **Purpose**: Large icon at card top
- **Structure**: Icon + title + description
- **Tailwind Utilities**: Icon at top of card
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-034: Feature Cards with Border
- **Purpose**: Border-styled feature cards
- **Structure**: Border instead of shadow
- **Tailwind Utilities**: `border-2 border-slate-200`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-035: Feature Cards with Hover Lift
- **Purpose**: Cards lift on hover
- **Structure**: Transform elevation on hover
- **Tailwind Utilities**: `hover:-translate-y-2 hover:shadow-xl`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-036: Feature Cards Glassmorphism
- **Purpose**: Frosted glass effect cards
- **Structure**: Backdrop blur + transparency
- **Tailwind Utilities**: `backdrop-blur-lg bg-white/30`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-037: Feature Cards with Gradient Border
- **Purpose**: Gradient border effect
- **Structure**: Pseudo-element gradient border
- **Tailwind Utilities**: Gradient border technique
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-038: Feature Cards Dark Mode
- **Purpose**: Dark theme feature cards
- **Structure**: Dark color scheme
- **Tailwind Utilities**: `bg-slate-800 text-white`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-039: Feature Cards with Action
- **Purpose**: Cards with CTA button
- **Structure**: Card + button at bottom
- **Tailwind Utilities**: Button styling in card
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-040: Feature Cards Horizontal
- **Purpose**: Horizontal card layout
- **Structure**: Side-by-side image + content
- **Tailwind Utilities**: `flex` horizontal layout
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### feat-041: Zigzag Features
- **Purpose**: Alternating left/right layout
- **Structure**: `odd:flex-row-reverse` pattern
- **Tailwind Utilities**: `even:flex-row-reverse`
- **Responsive**: Standard stacking
- **Status**: `[ ] Pending`

#### feat-042: Zigzag with Large Images
- **Purpose**: Big image alternating layout
- **Structure**: Large images alternating sides
- **Tailwind Utilities**: `grid-cols-2` alternating
- **Responsive**: Stack images above
- **Status**: `[ ] Pending`

#### feat-043: Zigzag with Background Colors
- **Purpose**: Alternating background colors
- **Structure**: Different bg per row
- **Tailwind Utilities**: `odd:bg-slate-50`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-044: Zigzag with Icons
- **Purpose**: Icon-based alternating
- **Structure**: Large icon alternating sides
- **Tailwind Utilities**: Icon sizing + positioning
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-045: Zigzag with Stats
- **Purpose**: Stats alternating with content
- **Structure**: Stats block + description
- **Tailwind Utilities**: Stats grid styling
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### feat-046: Zigzag with Testimonials
- **Purpose**: Feature + testimonial alternating
- **Structure**: Feature + related quote
- **Tailwind Utilities**: Quote styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### feat-047: Zigzag Cards
- **Purpose**: Card-based alternating
- **Structure**: Cards alternating position
- **Tailwind Utilities**: Card + offset positioning
- **Responsive**: Standard stacking
- **Status**: `[ ] Pending`

#### feat-048: Zigzag with Video
- **Purpose**: Video alternating with text
- **Structure**: Video embed + description
- **Tailwind Utilities**: Video container styling
- **Responsive**: Video above on mobile
- **Status**: `[ ] Pending`

#### feat-049: Zigzag Timeline
- **Purpose**: Timeline alternating layout
- **Structure**: Center line with alternating content
- **Tailwind Utilities**: Timeline center line
- **Responsive**: Single side on mobile
- **Status**: `[ ] Pending`

#### feat-050: Zigzag with Animation
- **Purpose**: Scroll-animated alternating
- **Structure**: Reveal on scroll
- **Tailwind Utilities**: Animation trigger classes
- **Responsive**: Reduced motion option
- **Status**: `[ ] Pending`

---

## 04. Content Sections

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Text Content | Article/paragraph sections |
| 011-020 | Media Content | Image/video sections |
| 021-030 | Stats | Statistics displays |
| 031-040 | Quotes | Blockquotes and pull quotes |
| 041-050 | Mixed Content | Combined content types |

### Template Details

#### content-001: Single Column Article
- **Purpose**: Simple blog/article content
- **Structure**: Centered narrow column
- **Tailwind Utilities**: `max-w-prose mx-auto`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-002: Two Column Content
- **Purpose**: Side-by-side content sections
- **Structure**: Two equal columns
- **Tailwind Utilities**: `grid grid-cols-2 gap-12`
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### content-003: Content with Sidebar
- **Purpose**: Main content + sidebar
- **Structure**: Main area + aside
- **Tailwind Utilities**: `grid grid-cols-3` (2:1 ratio)
- **Responsive**: Sidebar below on mobile
- **Status**: `[ ] Pending`

#### content-004: Full Width Content
- **Purpose**: Edge-to-edge content section
- **Structure**: Full width container
- **Tailwind Utilities**: `w-full px-0`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-005: Narrow Centered Content
- **Purpose**: Focused reading width
- **Structure**: Narrow max-width
- **Tailwind Utilities**: `max-w-2xl mx-auto`
- **Responsive**: Standard with padding
- **Status**: `[ ] Pending`

#### content-006: Content with Drop Cap
- **Purpose**: Editorial style with drop cap
- **Structure**: First letter styled large
- **Tailwind Utilities**: `first-letter:text-5xl first-letter:float-left`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-007: Multi-Column Text
- **Purpose**: Newspaper-style columns
- **Structure**: CSS columns
- **Tailwind Utilities**: `columns-2 lg:columns-3`
- **Responsive**: Single column mobile
- **Status**: `[ ] Pending`

#### content-008: Content with Footnotes
- **Purpose**: Academic-style with footnotes
- **Structure**: Content + footnote section
- **Tailwind Utilities**: Footnote reference styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-009: Content with Table of Contents
- **Purpose**: Long content with TOC
- **Structure**: Sticky TOC sidebar
- **Tailwind Utilities**: `sticky top-24` TOC
- **Responsive**: TOC collapses on mobile
- **Status**: `[ ] Pending`

#### content-010: Content with Annotations
- **Purpose**: Content with inline notes
- **Structure**: Tooltip annotations
- **Tailwind Utilities**: Tooltip styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-011: Full Width Image
- **Purpose**: Edge-to-edge image section
- **Structure**: Full bleed image
- **Tailwind Utilities**: `w-full h-96 object-cover`
- **Responsive**: Adjust height for mobile
- **Status**: `[ ] Pending`

#### content-012: Image with Caption
- **Purpose**: Image with descriptive caption
- **Structure**: Figure + figcaption
- **Tailwind Utilities**: `figure` semantic element
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-013: Image Gallery Grid
- **Purpose**: Multiple image grid
- **Structure**: Image grid layout
- **Tailwind Utilities**: `grid grid-cols-3 gap-4`
- **Responsive**: 2 or 1 column on smaller
- **Status**: `[ ] Pending`

#### content-014: Side-by-Side Images
- **Purpose**: Two images comparison
- **Structure**: Two column images
- **Tailwind Utilities**: `grid grid-cols-2`
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### content-015: Image with Text Overlay
- **Purpose**: Text overlaid on image
- **Structure**: Relative container with overlay
- **Tailwind Utilities**: `absolute bottom-0` text
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-016: Video Section
- **Purpose**: Embedded video content
- **Structure**: Video player section
- **Tailwind Utilities**: `aspect-video`
- **Responsive**: Maintain aspect ratio
- **Status**: `[ ] Pending`

#### content-017: Video with Thumbnail
- **Purpose**: Video preview thumbnail
- **Structure**: Thumbnail + play button
- **Tailwind Utilities**: Play button overlay
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-018: Before/After Image Slider
- **Purpose**: Image comparison slider
- **Structure**: Overlapping images + slider
- **Tailwind Utilities**: Slider control styling
- **Responsive**: Touch-friendly
- **Status**: `[ ] Pending`

#### content-019: Image Carousel
- **Purpose**: Sliding image gallery
- **Structure**: Carousel component
- **Tailwind Utilities**: Carousel navigation
- **Responsive**: Touch swipe support
- **Status**: `[ ] Pending`

#### content-020: Lightbox Gallery
- **Purpose**: Click-to-expand images
- **Structure**: Thumbnails + modal view
- **Tailwind Utilities**: Modal overlay styling
- **Responsive**: Full screen on mobile
- **Status**: `[ ] Pending`

#### content-021: Single Large Stat
- **Purpose**: Hero stat number
- **Structure**: Large number + label
- **Tailwind Utilities**: `text-6xl font-bold`
- **Responsive**: Scale appropriately
- **Status**: `[ ] Pending`

#### content-022: Stats Row
- **Purpose**: Horizontal stats display
- **Structure**: Row of stat items
- **Tailwind Utilities**: `flex justify-around`
- **Responsive**: Grid on mobile
- **Status**: `[ ] Pending`

#### content-023: Stats Grid
- **Purpose**: Grid of statistics
- **Structure**: 2x2 or 3x2 stats grid
- **Tailwind Utilities**: `grid grid-cols-2 md:grid-cols-4`
- **Responsive**: Standard grid
- **Status**: `[ ] Pending`

#### content-024: Stats with Icons
- **Purpose**: Stats with visual icons
- **Structure**: Icon + number + label
- **Tailwind Utilities**: Icon positioning
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-025: Animated Counter Stats
- **Purpose**: Count-up animation stats
- **Structure**: Animated number counters
- **Tailwind Utilities**: Number display
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-026: Stats with Progress Bars
- **Purpose**: Stats with visual progress
- **Structure**: Number + progress bar
- **Tailwind Utilities**: Progress bar width
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-027: Stats Cards
- **Purpose**: Stats in card containers
- **Structure**: Card per stat
- **Tailwind Utilities**: Card styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-028: Stats with Comparison
- **Purpose**: Before/after or vs stats
- **Structure**: Comparison layout
- **Tailwind Utilities**: Side-by-side comparison
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### content-029: Stats with Trend Indicators
- **Purpose**: Stats with up/down arrows
- **Structure**: Number + trend icon
- **Tailwind Utilities**: Trend arrow styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-030: Stats Timeline
- **Purpose**: Stats along timeline
- **Structure**: Horizontal timeline + stats
- **Tailwind Utilities**: Timeline layout
- **Responsive**: Vertical on mobile
- **Status**: `[ ] Pending`

#### content-031: Simple Blockquote
- **Purpose**: Basic quote styling
- **Structure**: `<blockquote>` element
- **Tailwind Utilities**: `border-l-4 pl-4 italic`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-032: Blockquote with Attribution
- **Purpose**: Quote + author citation
- **Structure**: Quote + cite element
- **Tailwind Utilities**: Citation styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-033: Large Pull Quote
- **Purpose**: Editorial pull quote
- **Structure**: Large styled quote
- **Tailwind Utilities**: `text-3xl font-serif`
- **Responsive**: Scale text size
- **Status**: `[ ] Pending`

#### content-034: Quote with Photo
- **Purpose**: Quote + author photo
- **Structure**: Quote + avatar + name
- **Tailwind Utilities**: Avatar styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-035: Quote Card
- **Purpose**: Quote in card container
- **Structure**: Card with quote mark
- **Tailwind Utilities**: Quote icon decoration
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-036: Centered Quote
- **Purpose**: Center-aligned quote
- **Structure**: Centered text quote
- **Tailwind Utilities**: `text-center`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-037: Quote with Background Image
- **Purpose**: Quote over image
- **Structure**: Image bg + quote overlay
- **Tailwind Utilities**: Overlay + text
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-038: Quote Carousel
- **Purpose**: Rotating quotes
- **Structure**: Quote slider
- **Tailwind Utilities**: Carousel navigation
- **Responsive**: Touch swipe
- **Status**: `[ ] Pending`

#### content-039: Side Quote
- **Purpose**: Quote alongside content
- **Structure**: Pull quote to side
- **Tailwind Utilities**: `float-right w-1/3`
- **Responsive**: Full width on mobile
- **Status**: `[ ] Pending`

#### content-040: Quote Grid
- **Purpose**: Multiple quotes grid
- **Structure**: Grid of quote cards
- **Tailwind Utilities**: Grid layout
- **Responsive**: Standard grid
- **Status**: `[ ] Pending`

#### content-041: Text + Image Section
- **Purpose**: Standard content + visual
- **Structure**: Split layout
- **Tailwind Utilities**: `grid grid-cols-2`
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### content-042: Text + Video Section
- **Purpose**: Content + embedded video
- **Structure**: Text + video player
- **Tailwind Utilities**: Video embed styling
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### content-043: Text + Stats Section
- **Purpose**: Content + statistics
- **Structure**: Copy + stats display
- **Tailwind Utilities**: Stats alongside text
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### content-044: Content with Code Block
- **Purpose**: Technical content + code
- **Structure**: Text + syntax highlighted code
- **Tailwind Utilities**: Code block styling
- **Responsive**: Horizontal scroll code
- **Status**: `[ ] Pending`

#### content-045: Content with Embed
- **Purpose**: Content + third-party embed
- **Structure**: Text + iframe/embed
- **Tailwind Utilities**: Embed container
- **Responsive**: Responsive embed
- **Status**: `[ ] Pending`

#### content-046: Content with Timeline
- **Purpose**: History/process content
- **Structure**: Text + timeline visual
- **Tailwind Utilities**: Timeline styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### content-047: Content with Map
- **Purpose**: Location-based content
- **Structure**: Text + map embed
- **Tailwind Utilities**: Map container
- **Responsive**: Map adjusts
- **Status**: `[ ] Pending`

#### content-048: Content with Data Table
- **Purpose**: Content + tabular data
- **Structure**: Text + responsive table
- **Tailwind Utilities**: Table styling
- **Responsive**: Horizontal scroll table
- **Status**: `[ ] Pending`

#### content-049: Content with Infographic
- **Purpose**: Content + visual data
- **Structure**: Text + infographic image/SVG
- **Tailwind Utilities**: Infographic positioning
- **Responsive**: Scale infographic
- **Status**: `[ ] Pending`

#### content-050: Rich Media Content
- **Purpose**: Multi-media content section
- **Structure**: Mix of text, images, video
- **Tailwind Utilities**: Mixed media layout
- **Responsive**: Appropriate stacking
- **Status**: `[ ] Pending`

---

## 05. CTA (Call to Action)

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Simple CTAs | Basic call-to-action |
| 011-020 | Banner CTAs | Full-width banners |
| 021-030 | Card CTAs | Card-style CTAs |
| 031-040 | Inline CTAs | In-content CTAs |
| 041-050 | Animated CTAs | Motion-enhanced CTAs |

### Template Details

#### cta-001: Simple Centered CTA
- **Purpose**: Basic centered call-to-action
- **Structure**: Heading + subtext + button
- **Tailwind Utilities**: `text-center py-16`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-002: CTA with Two Buttons
- **Purpose**: Primary + secondary actions
- **Structure**: Two button options
- **Tailwind Utilities**: `flex gap-4 justify-center`
- **Responsive**: Stack buttons on mobile
- **Status**: `[ ] Pending`

#### cta-003: CTA with Email Input
- **Purpose**: Newsletter signup CTA
- **Structure**: Input + submit button
- **Tailwind Utilities**: `flex` input + button
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### cta-004: CTA with Form
- **Purpose**: Lead capture CTA
- **Structure**: Multiple form fields
- **Tailwind Utilities**: Form styling
- **Responsive**: Standard form
- **Status**: `[ ] Pending`

#### cta-005: Minimal CTA
- **Purpose**: Subtle call-to-action
- **Structure**: Text link style
- **Tailwind Utilities**: `underline hover:no-underline`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-006: CTA with Icon
- **Purpose**: Icon-enhanced CTA button
- **Structure**: Button with leading icon
- **Tailwind Utilities**: `flex items-center gap-2`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-007: CTA with Arrow
- **Purpose**: CTA with arrow indicator
- **Structure**: Text + arrow icon
- **Tailwind Utilities**: Arrow animation on hover
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-008: Gradient Button CTA
- **Purpose**: Eye-catching gradient button
- **Structure**: Gradient background button
- **Tailwind Utilities**: `bg-gradient-to-r`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-009: CTA with Social Proof
- **Purpose**: CTA with trust indicators
- **Structure**: CTA + avatars/logos
- **Tailwind Utilities**: Avatar stack styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-010: CTA with Countdown
- **Purpose**: Urgency-based CTA
- **Structure**: Timer + CTA button
- **Tailwind Utilities**: Countdown display
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-011: Full Width Banner CTA
- **Purpose**: Wide banner call-to-action
- **Structure**: Full width background
- **Tailwind Utilities**: `w-full py-12 bg-primary`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-012: Banner with Image Background
- **Purpose**: Image-backed CTA banner
- **Structure**: Background image + content
- **Tailwind Utilities**: `bg-cover bg-center`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-013: Banner with Gradient Background
- **Purpose**: Gradient CTA banner
- **Structure**: Gradient bg + content
- **Tailwind Utilities**: `bg-gradient-to-r`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-014: Split Banner CTA
- **Purpose**: Two-sided CTA banner
- **Structure**: Image + CTA side-by-side
- **Tailwind Utilities**: `grid grid-cols-2`
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### cta-015: Banner with Pattern
- **Purpose**: Patterned background CTA
- **Structure**: SVG pattern background
- **Tailwind Utilities**: Pattern overlay
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-016: Sticky Banner CTA
- **Purpose**: Fixed position banner
- **Structure**: Sticky/fixed banner
- **Tailwind Utilities**: `sticky bottom-0` or `fixed`
- **Responsive**: Full width on mobile
- **Status**: `[ ] Pending`

#### cta-017: Banner with Multiple CTAs
- **Purpose**: Multiple action options
- **Structure**: Several CTA buttons
- **Tailwind Utilities**: Button group styling
- **Responsive**: Stack or wrap
- **Status**: `[ ] Pending`

#### cta-018: Dark Banner CTA
- **Purpose**: Dark-themed CTA banner
- **Structure**: Dark background colors
- **Tailwind Utilities**: `bg-slate-900 text-white`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-019: Banner with Video Background
- **Purpose**: Video-backed CTA
- **Structure**: Video + overlay content
- **Tailwind Utilities**: Video container
- **Responsive**: Image fallback on mobile
- **Status**: `[ ] Pending`

#### cta-020: Dismissible Banner CTA
- **Purpose**: Banner with close button
- **Structure**: Banner + dismiss control
- **Tailwind Utilities**: Close button styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-021: CTA Card Simple
- **Purpose**: Basic CTA card
- **Structure**: Card container with CTA
- **Tailwind Utilities**: `rounded-xl shadow-lg p-8`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-022: CTA Card with Icon
- **Purpose**: Icon-featured CTA card
- **Structure**: Icon + text + button
- **Tailwind Utilities**: Icon at top of card
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-023: CTA Card with Image
- **Purpose**: Image-featured CTA card
- **Structure**: Image + CTA content
- **Tailwind Utilities**: Image header in card
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-024: CTA Card Horizontal
- **Purpose**: Landscape CTA card
- **Structure**: Side-by-side layout
- **Tailwind Utilities**: `flex` horizontal
- **Responsive**: Stack on mobile
- **Status**: `[ ] Pending`

#### cta-025: CTA Card with Border
- **Purpose**: Border-styled CTA card
- **Structure**: Border accent card
- **Tailwind Utilities**: `border-2` styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-026: CTA Card Gradient
- **Purpose**: Gradient background card
- **Structure**: Gradient card bg
- **Tailwind Utilities**: `bg-gradient-to-br`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-027: CTA Card Glassmorphism
- **Purpose**: Glass effect CTA card
- **Structure**: Backdrop blur card
- **Tailwind Utilities**: `backdrop-blur-lg bg-white/20`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-028: CTA Card with Stats
- **Purpose**: Stats + CTA combined
- **Structure**: Statistics + action
- **Tailwind Utilities**: Stats grid in card
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-029: CTA Card with Testimonial
- **Purpose**: Social proof + CTA
- **Structure**: Quote + CTA button
- **Tailwind Utilities**: Quote styling
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-030: CTA Card Floating
- **Purpose**: Elevated floating card
- **Structure**: Large shadow card
- **Tailwind Utilities**: `shadow-2xl -mt-16`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-031: Inline Text CTA
- **Purpose**: CTA within content
- **Structure**: Link-style inline CTA
- **Tailwind Utilities**: `inline-flex items-center`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-032: Inline Box CTA
- **Purpose**: Boxed inline CTA
- **Structure**: Small box within content
- **Tailwind Utilities**: Inline-block box
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-033: Sidebar CTA
- **Purpose**: Sidebar placement CTA
- **Structure**: Vertical sidebar CTA
- **Tailwind Utilities**: Sidebar positioning
- **Responsive**: Below content on mobile
- **Status**: `[ ] Pending`

#### cta-034: In-Article CTA
- **Purpose**: Mid-content CTA break
- **Structure**: CTA interrupting content
- **Tailwind Utilities**: `my-8` spacing
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-035: Exit Intent CTA
- **Purpose**: Mouse-leave triggered
- **Structure**: Modal CTA on exit
- **Tailwind Utilities**: Modal styling
- **Responsive**: Mobile variant
- **Status**: `[ ] Pending`

#### cta-036: Scroll-Triggered CTA
- **Purpose**: Appears on scroll
- **Structure**: Intersection Observer trigger
- **Tailwind Utilities**: `opacity-0` to visible
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-037: Floating Corner CTA
- **Purpose**: Fixed corner CTA
- **Structure**: Corner positioned
- **Tailwind Utilities**: `fixed bottom-4 right-4`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-038: Post-Content CTA
- **Purpose**: End of article CTA
- **Structure**: CTA after content
- **Tailwind Utilities**: `mt-12 pt-12 border-t`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-039: Tooltip CTA
- **Purpose**: Hover tooltip CTA
- **Structure**: Tooltip trigger + content
- **Tailwind Utilities**: Tooltip positioning
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-040: Expanding CTA
- **Purpose**: Expands on interaction
- **Structure**: Compact → expanded
- **Tailwind Utilities**: Transition size
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-041: Animated Button CTA
- **Purpose**: Animated button effects
- **Structure**: Button with animations
- **Tailwind Utilities**: `animate-` effects
- **Responsive**: Reduced motion
- **Status**: `[ ] Pending`

#### cta-042: Pulsing CTA
- **Purpose**: Pulse attention effect
- **Structure**: Pulse animation
- **Tailwind Utilities**: `animate-pulse`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-043: Shake CTA
- **Purpose**: Shake animation
- **Structure**: Periodic shake
- **Tailwind Utilities**: Custom shake animation
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-044: Bounce CTA
- **Purpose**: Bouncing effect
- **Structure**: Bounce animation
- **Tailwind Utilities**: `animate-bounce`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-045: Glow CTA
- **Purpose**: Glowing effect
- **Structure**: Shadow glow animation
- **Tailwind Utilities**: Box-shadow animation
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-046: Slide-In CTA
- **Purpose**: Slides in on trigger
- **Structure**: Transform animation
- **Tailwind Utilities**: `translate-y` animation
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-047: Fade-In CTA
- **Purpose**: Fades in on view
- **Structure**: Opacity animation
- **Tailwind Utilities**: `opacity-0 animate-fadeIn`
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-048: Rotate CTA
- **Purpose**: Rotation effect
- **Structure**: Rotating element
- **Tailwind Utilities**: `rotate` transform
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-049: Scale CTA
- **Purpose**: Scale animation
- **Structure**: Grow/shrink effect
- **Tailwind Utilities**: `scale` transform
- **Responsive**: Standard
- **Status**: `[ ] Pending`

#### cta-050: Multi-Step Animated CTA
- **Purpose**: Complex animation sequence
- **Structure**: Chained animations
- **Tailwind Utilities**: Keyframe sequences
- **Responsive**: Simplified on mobile
- **Status**: `[ ] Pending`

---

## 06. Pricing

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Basic Tables | Simple pricing tables |
| 011-020 | Card Pricing | Card-based pricing |
| 021-030 | Comparison | Feature comparisons |
| 031-040 | Toggle Pricing | Monthly/yearly toggle |
| 041-050 | Creative Pricing | Unique layouts |

### Template Details

#### price-001 ~ price-050
*[Detailed specifications follow same format as above categories]*

- **price-001**: Three Column Pricing Table
- **price-002**: Two Column Pricing
- **price-003**: Four Column Pricing
- **price-004**: Single Plan Highlighted
- **price-005**: Pricing with Feature List
- **price-006**: Pricing with Checkmarks
- **price-007**: Horizontal Pricing Table
- **price-008**: Pricing with Icons
- **price-009**: Minimal Pricing
- **price-010**: Dark Theme Pricing
- **price-011**: Pricing Cards Basic
- **price-012**: Pricing Cards with Shadow
- **price-013**: Pricing Cards Elevated
- **price-014**: Pricing Cards with Border
- **price-015**: Pricing Cards Gradient
- **price-016**: Pricing Cards with Image
- **price-017**: Pricing Cards with Icon Header
- **price-018**: Pricing Cards Stacked
- **price-019**: Pricing Cards with Ribbon
- **price-020**: Glassmorphism Pricing Cards
- **price-021**: Feature Comparison Table
- **price-022**: Detailed Comparison Grid
- **price-023**: Comparison with Tooltips
- **price-024**: Side-by-Side Comparison
- **price-025**: Comparison with Categories
- **price-026**: Interactive Comparison
- **price-027**: Comparison Accordion
- **price-028**: Comparison with Highlights
- **price-029**: Comparison Matrix
- **price-030**: Comparison with Recommendations
- **price-031**: Monthly/Yearly Toggle
- **price-032**: Toggle with Savings Badge
- **price-033**: Slider Price Selection
- **price-034**: Usage-Based Pricing
- **price-035**: Calculator Pricing
- **price-036**: Tier Selector
- **price-037**: Toggle with Animation
- **price-038**: Multiple Toggle Options
- **price-039**: Quote Calculator
- **price-040**: Dynamic Pricing
- **price-041**: Timeline Pricing
- **price-042**: Circular Pricing
- **price-043**: Split Screen Pricing
- **price-044**: Pricing with Testimonial
- **price-045**: Pricing FAQ Combined
- **price-046**: Pricing with Stats
- **price-047**: Animated Pricing
- **price-048**: 3D Pricing Cards
- **price-049**: Pricing with Video
- **price-050**: Gamified Pricing

---

## 07. Testimonials

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Simple | Basic testimonial styles |
| 011-020 | Cards | Card-based testimonials |
| 021-030 | Carousel | Sliding testimonials |
| 031-040 | Grid | Grid layouts |
| 041-050 | Creative | Unique designs |

### Template Details

#### test-001 ~ test-050
*[Each follows detailed specification format]*

- **test-001**: Simple Quote Testimonial
- **test-002**: Testimonial with Avatar
- **test-003**: Testimonial with Rating
- **test-004**: Testimonial with Company Logo
- **test-005**: Large Quote Testimonial
- **test-006**: Centered Testimonial
- **test-007**: Side Avatar Testimonial
- **test-008**: Testimonial with Role/Title
- **test-009**: Minimal Testimonial
- **test-010**: Dark Theme Testimonial
- **test-011**: Basic Testimonial Card
- **test-012**: Card with Image Background
- **test-013**: Card with Gradient
- **test-014**: Card with Border Accent
- **test-015**: Elevated Card Testimonial
- **test-016**: Glassmorphism Testimonial
- **test-017**: Card with Social Link
- **test-018**: Card with Video
- **test-019**: Card with Stats
- **test-020**: Horizontal Card Testimonial
- **test-021**: Basic Carousel
- **test-022**: Carousel with Thumbnails
- **test-023**: Carousel with Dots
- **test-024**: Carousel with Arrows
- **test-025**: Auto-Play Carousel
- **test-026**: Fade Carousel
- **test-027**: 3D Carousel
- **test-028**: Carousel with Preview
- **test-029**: Full Width Carousel
- **test-030**: Multi-Item Carousel
- **test-031**: Two Column Grid
- **test-032**: Three Column Grid
- **test-033**: Masonry Grid
- **test-034**: Featured + Grid
- **test-035**: Alternating Grid
- **test-036**: Bento Grid Testimonials
- **test-037**: Offset Grid
- **test-038**: Grid with Categories
- **test-039**: Infinite Scroll Grid
- **test-040**: Filterable Grid
- **test-041**: Twitter/X Style
- **test-042**: Chat Bubble Style
- **test-043**: Polaroid Style
- **test-044**: Post-it Note Style
- **test-045**: Timeline Testimonials
- **test-046**: Map-Based Testimonials
- **test-047**: Video Testimonials
- **test-048**: Audio Testimonials
- **test-049**: Before/After Testimonials
- **test-050**: Animated Testimonials

---

## 08. Team

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Grid | Team member grids |
| 011-020 | Cards | Team cards |
| 021-030 | List | Team lists |
| 031-040 | Featured | Highlighted members |
| 041-050 | Creative | Unique layouts |

### Template Details

#### team-001 ~ team-050
- **team-001**: Three Column Team Grid
- **team-002**: Four Column Team Grid
- **team-003**: Two Column Team Grid
- **team-004**: Team Grid with Roles
- **team-005**: Team Grid with Social Links
- **team-006**: Circular Avatar Grid
- **team-007**: Square Avatar Grid
- **team-008**: Team Grid with Hover Effect
- **team-009**: Team Grid with Bio
- **team-010**: Dark Theme Team Grid
- **team-011**: Basic Team Card
- **team-012**: Team Card with Image Top
- **team-013**: Team Card with Social
- **team-014**: Team Card Horizontal
- **team-015**: Team Card with Stats
- **team-016**: Team Card Glassmorphism
- **team-017**: Team Card with Background
- **team-018**: Team Card Flip
- **team-019**: Team Card with Quote
- **team-020**: Team Card Minimal
- **team-021**: Simple Team List
- **team-022**: Team List with Photos
- **team-023**: Team List with Descriptions
- **team-024**: Team List Grouped
- **team-025**: Team List with Contact
- **team-026**: Team List Expandable
- **team-027**: Team List with Skills
- **team-028**: Team List Timeline
- **team-029**: Team List with Search
- **team-030**: Team List Filterable
- **team-031**: CEO/Founder Feature
- **team-032**: Leadership Section
- **team-033**: Featured with Team Grid
- **team-034**: About the Founder
- **team-035**: Team Lead Cards
- **team-036**: Advisor Section
- **team-037**: Board Members
- **team-038**: Department Heads
- **team-039**: Featured Quote + Team
- **team-040**: Story Behind the Team
- **team-041**: Hexagon Team Grid
- **team-042**: Org Chart Style
- **team-043**: Team Map
- **team-044**: Team Timeline
- **team-045**: Team with Video Intro
- **team-046**: Team Carousel
- **team-047**: Team Mosaic
- **team-048**: Team with Achievements
- **team-049**: Interactive Team
- **team-050**: Animated Team Section

---

## 09. Gallery

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Grid | Image grids |
| 011-020 | Masonry | Pinterest-style |
| 021-030 | Carousel | Sliding galleries |
| 031-040 | Lightbox | Click-to-expand |
| 041-050 | Creative | Unique galleries |

### Template Details

#### gallery-001 ~ gallery-050
- **gallery-001**: Basic 3 Column Grid
- **gallery-002**: 4 Column Grid
- **gallery-003**: 2 Column Grid
- **gallery-004**: Grid with Gap
- **gallery-005**: Grid with Captions
- **gallery-006**: Grid with Hover Overlay
- **gallery-007**: Grid with Categories
- **gallery-008**: Filterable Grid
- **gallery-009**: Infinite Scroll Grid
- **gallery-010**: Grid with Zoom
- **gallery-011**: Basic Masonry
- **gallery-012**: Masonry with Captions
- **gallery-013**: Masonry Filterable
- **gallery-014**: Masonry with Load More
- **gallery-015**: Masonry with Hover
- **gallery-016**: Mixed Media Masonry
- **gallery-017**: Masonry with Lightbox
- **gallery-018**: Animated Masonry
- **gallery-019**: Masonry Portfolio
- **gallery-020**: Masonry Blog
- **gallery-021**: Basic Carousel
- **gallery-022**: Carousel with Thumbnails
- **gallery-023**: Carousel Full Width
- **gallery-024**: Carousel with Captions
- **gallery-025**: Auto-Play Carousel
- **gallery-026**: Fade Carousel
- **gallery-027**: 3D Carousel
- **gallery-028**: Carousel with Counter
- **gallery-029**: Multi-Row Carousel
- **gallery-030**: Vertical Carousel
- **gallery-031**: Basic Lightbox
- **gallery-032**: Lightbox with Captions
- **gallery-033**: Lightbox Gallery
- **gallery-034**: Lightbox with Zoom
- **gallery-035**: Lightbox with Navigation
- **gallery-036**: Lightbox with Thumbnails
- **gallery-037**: Lightbox Full Screen
- **gallery-038**: Lightbox with Video
- **gallery-039**: Lightbox with Info Panel
- **gallery-040**: Lightbox Social Share
- **gallery-041**: Horizontal Scroll Gallery
- **gallery-042**: Parallax Gallery
- **gallery-043**: Mosaic Gallery
- **gallery-044**: Polaroid Gallery
- **gallery-045**: Timeline Gallery
- **gallery-046**: Story Gallery
- **gallery-047**: Before/After Gallery
- **gallery-048**: 360 View Gallery
- **gallery-049**: Video Gallery
- **gallery-050**: Mixed Media Gallery

---

## 10. Forms

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Contact | Contact forms |
| 011-020 | Signup | Registration forms |
| 021-030 | Survey | Questionnaires |
| 031-040 | Checkout | Payment forms |
| 041-050 | Multi-Step | Wizard forms |

### Template Details

#### form-001 ~ form-050
- **form-001**: Simple Contact Form
- **form-002**: Contact with Map
- **form-003**: Contact with Info
- **form-004**: Contact Split Layout
- **form-005**: Contact Minimal
- **form-006**: Contact with Social
- **form-007**: Contact Card Style
- **form-008**: Contact Full Page
- **form-009**: Contact with FAQ
- **form-010**: Contact Dark Theme
- **form-011**: Email Signup
- **form-012**: Newsletter Inline
- **form-013**: Registration Form
- **form-014**: Account Creation
- **form-015**: Signup with Social
- **form-016**: Signup with Avatar
- **form-017**: Signup Multi-Field
- **form-018**: Waitlist Form
- **form-019**: Beta Signup
- **form-020**: Subscription Form
- **form-021**: Simple Survey
- **form-022**: NPS Survey
- **form-023**: Feedback Form
- **form-024**: Rating Form
- **form-025**: Poll/Vote Form
- **form-026**: Quiz Form
- **form-027**: Assessment Form
- **form-028**: Application Form
- **form-029**: Review Form
- **form-030**: Questionnaire
- **form-031**: Simple Checkout
- **form-032**: Checkout with Summary
- **form-033**: Payment Form
- **form-034**: Billing Form
- **form-035**: Shipping Form
- **form-036**: Order Form
- **form-037**: Donation Form
- **form-038**: Booking Form
- **form-039**: Reservation Form
- **form-040**: Quote Request Form
- **form-041**: Two Step Form
- **form-042**: Three Step Form
- **form-043**: Progress Bar Form
- **form-044**: Tabbed Form
- **form-045**: Accordion Form
- **form-046**: Wizard with Preview
- **form-047**: Conditional Steps
- **form-048**: Form with Validation
- **form-049**: Form with File Upload
- **form-050**: Complex Multi-Step

---

## 11. Cards

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Basic | Simple cards |
| 011-020 | Profile | User/profile cards |
| 021-030 | Product | E-commerce cards |
| 031-040 | Content | Blog/article cards |
| 041-050 | Interactive | Action cards |

### Template Details

#### card-001 ~ card-050
- **card-001**: Basic Card
- **card-002**: Card with Header
- **card-003**: Card with Footer
- **card-004**: Card with Image
- **card-005**: Card Horizontal
- **card-006**: Card with Border
- **card-007**: Card with Shadow
- **card-008**: Card Minimal
- **card-009**: Card Dark
- **card-010**: Card Gradient
- **card-011**: Profile Card Basic
- **card-012**: Profile Card with Cover
- **card-013**: Profile Card with Stats
- **card-014**: Profile Card Social
- **card-015**: Profile Card Compact
- **card-016**: Team Member Card
- **card-017**: Profile Card Horizontal
- **card-018**: Profile Card with Actions
- **card-019**: Profile Card Badge
- **card-020**: Profile Card Minimal
- **card-021**: Product Card Basic
- **card-022**: Product Card with Price
- **card-023**: Product Card with Rating
- **card-024**: Product Card with Badge
- **card-025**: Product Card Quick View
- **card-026**: Product Card Horizontal
- **card-027**: Product Card Compact
- **card-028**: Product Card with Actions
- **card-029**: Product Card Compare
- **card-030**: Product Card Wishlist
- **card-031**: Blog Card Basic
- **card-032**: Blog Card with Author
- **card-033**: Blog Card with Date
- **card-034**: Blog Card with Category
- **card-035**: Blog Card Featured
- **card-036**: Blog Card Horizontal
- **card-037**: Blog Card Minimal
- **card-038**: Blog Card with Excerpt
- **card-039**: Blog Card with Stats
- **card-040**: Blog Card Dark
- **card-041**: Expandable Card
- **card-042**: Flip Card
- **card-043**: Swipeable Card
- **card-044**: Card with Dropdown
- **card-045**: Card with Tabs
- **card-046**: Card with Progress
- **card-047**: Card with Toggle
- **card-048**: Card with Slider
- **card-049**: Card Stack
- **card-050**: Card with Animation

---

## 12. Lists

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Simple | Basic lists |
| 011-020 | Data | Data tables |
| 021-030 | Feed | Activity feeds |
| 031-040 | Settings | Settings lists |
| 041-050 | Interactive | Action lists |

### Template Details

#### list-001 ~ list-050
- **list-001**: Simple List
- **list-002**: List with Icons
- **list-003**: List with Avatars
- **list-004**: List with Actions
- **list-005**: List with Badges
- **list-006**: List Grouped
- **list-007**: List with Dividers
- **list-008**: List Numbered
- **list-009**: List Checkable
- **list-010**: List Dark
- **list-011**: Basic Data Table
- **list-012**: Table with Sorting
- **list-013**: Table with Search
- **list-014**: Table with Pagination
- **list-015**: Table Striped
- **list-016**: Table with Actions
- **list-017**: Table Responsive
- **list-018**: Table with Selection
- **list-019**: Table with Filters
- **list-020**: Table Expandable
- **list-021**: Activity Feed
- **list-022**: Timeline Feed
- **list-023**: Notification Feed
- **list-024**: Comment Feed
- **list-025**: Social Feed
- **list-026**: News Feed
- **list-027**: Update Feed
- **list-028**: Transaction Feed
- **list-029**: Chat Feed
- **list-030**: Event Feed
- **list-031**: Settings List Basic
- **list-032**: Settings with Toggle
- **list-033**: Settings Grouped
- **list-034**: Settings with Description
- **list-035**: Settings Navigation
- **list-036**: Settings Accordion
- **list-037**: Preference List
- **list-038**: Account Settings
- **list-039**: Notification Settings
- **list-040**: Privacy Settings
- **list-041**: Sortable List
- **list-042**: Drag and Drop List
- **list-043**: Filterable List
- **list-044**: Searchable List
- **list-045**: List with Load More
- **list-046**: Infinite Scroll List
- **list-047**: Collapsible List
- **list-048**: Multi-Select List
- **list-049**: Reorderable List
- **list-050**: List with Preview

---

## 13. Modals & Dialogs

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Basic | Simple modals |
| 011-020 | Alert | Alert dialogs |
| 021-030 | Form | Form modals |
| 031-040 | Content | Content modals |
| 041-050 | Special | Unique modals |

### Template Details

#### modal-001 ~ modal-050
- **modal-001**: Basic Modal
- **modal-002**: Modal with Header
- **modal-003**: Modal with Footer
- **modal-004**: Modal Centered
- **modal-005**: Modal Full Screen
- **modal-006**: Modal Slide-In
- **modal-007**: Modal with Backdrop
- **modal-008**: Modal Scrollable
- **modal-009**: Modal Dark
- **modal-010**: Modal Minimal
- **modal-011**: Alert Success
- **modal-012**: Alert Error
- **modal-013**: Alert Warning
- **modal-014**: Alert Info
- **modal-015**: Confirmation Dialog
- **modal-016**: Delete Confirmation
- **modal-017**: Alert with Icon
- **modal-018**: Alert with Actions
- **modal-019**: Alert Timeout
- **modal-020**: Alert Stack
- **modal-021**: Login Modal
- **modal-022**: Signup Modal
- **modal-023**: Contact Modal
- **modal-024**: Subscribe Modal
- **modal-025**: Feedback Modal
- **modal-026**: Search Modal
- **modal-027**: Filter Modal
- **modal-028**: Settings Modal
- **modal-029**: Profile Edit Modal
- **modal-030**: Multi-Step Modal
- **modal-031**: Image Modal
- **modal-032**: Video Modal
- **modal-033**: Gallery Modal
- **modal-034**: Product Modal
- **modal-035**: Article Modal
- **modal-036**: Map Modal
- **modal-037**: Share Modal
- **modal-038**: Print Modal
- **modal-039**: Help Modal
- **modal-040**: Terms Modal
- **modal-041**: Cookie Consent
- **modal-042**: Age Verification
- **modal-043**: Location Picker
- **modal-044**: Date Picker Modal
- **modal-045**: Color Picker Modal
- **modal-046**: File Upload Modal
- **modal-047**: Crop Image Modal
- **modal-048**: QR Code Modal
- **modal-049**: Payment Modal
- **modal-050**: Onboarding Modal

---

## 14. Notifications

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Toast | Toast messages |
| 011-020 | Banner | Banner alerts |
| 021-030 | Inline | Inline alerts |
| 031-040 | Snackbar | Snackbar style |
| 041-050 | Badge | Notification badges |

### Template Details

#### notif-001 ~ notif-050
- **notif-001**: Basic Toast
- **notif-002**: Toast Success
- **notif-003**: Toast Error
- **notif-004**: Toast Warning
- **notif-005**: Toast Info
- **notif-006**: Toast with Icon
- **notif-007**: Toast with Action
- **notif-008**: Toast with Progress
- **notif-009**: Toast Stack
- **notif-010**: Toast Dark
- **notif-011**: Top Banner
- **notif-012**: Bottom Banner
- **notif-013**: Dismissible Banner
- **notif-014**: Banner with CTA
- **notif-015**: Banner Animated
- **notif-016**: Cookie Banner
- **notif-017**: Announcement Banner
- **notif-018**: Sale Banner
- **notif-019**: Warning Banner
- **notif-020**: Maintenance Banner
- **notif-021**: Inline Alert Success
- **notif-022**: Inline Alert Error
- **notif-023**: Inline Alert Warning
- **notif-024**: Inline Alert Info
- **notif-025**: Inline with Icon
- **notif-026**: Inline with Link
- **notif-027**: Inline Dismissible
- **notif-028**: Inline with List
- **notif-029**: Inline Card Style
- **notif-030**: Inline Bordered
- **notif-031**: Basic Snackbar
- **notif-032**: Snackbar with Action
- **notif-033**: Snackbar with Icon
- **notif-034**: Snackbar Multi-Line
- **notif-035**: Snackbar Queue
- **notif-036**: Snackbar Positioned
- **notif-037**: Snackbar with Progress
- **notif-038**: Snackbar Undo
- **notif-039**: Snackbar Loading
- **notif-040**: Snackbar Custom
- **notif-041**: Count Badge
- **notif-042**: Dot Badge
- **notif-043**: Icon Badge
- **notif-044**: Badge on Avatar
- **notif-045**: Badge on Button
- **notif-046**: Badge Animated
- **notif-047**: Status Badge
- **notif-048**: Badge Group
- **notif-049**: Badge with Tooltip
- **notif-050**: Custom Badge

---

## 15. Footers

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Simple | Basic footers |
| 011-020 | Multi-Column | Column layouts |
| 021-030 | Newsletter | With signup |
| 031-040 | Mega | Large footers |
| 041-050 | Creative | Unique designs |

### Template Details

#### footer-001 ~ footer-050
- **footer-001**: Simple Centered Footer
- **footer-002**: Footer with Links
- **footer-003**: Footer with Social
- **footer-004**: Footer with Logo
- **footer-005**: Footer Minimal
- **footer-006**: Footer with Copyright
- **footer-007**: Footer Dark
- **footer-008**: Footer with Divider
- **footer-009**: Footer Two Lines
- **footer-010**: Footer Sticky
- **footer-011**: Three Column Footer
- **footer-012**: Four Column Footer
- **footer-013**: Five Column Footer
- **footer-014**: Footer with Categories
- **footer-015**: Footer with Description
- **footer-016**: Footer Uneven Columns
- **footer-017**: Footer with Icons
- **footer-018**: Footer Two Row
- **footer-019**: Footer with Contact
- **footer-020**: Footer Responsive Columns
- **footer-021**: Footer with Newsletter
- **footer-022**: Newsletter Inline
- **footer-023**: Newsletter Card
- **footer-024**: Newsletter Full Width
- **footer-025**: Newsletter with Benefits
- **footer-026**: Newsletter Minimal
- **footer-027**: Newsletter with Social
- **footer-028**: Newsletter Dark
- **footer-029**: Newsletter with Image
- **footer-030**: Newsletter Split
- **footer-031**: Mega Footer Basic
- **footer-032**: Mega Footer with Logo
- **footer-033**: Mega Footer with App Links
- **footer-034**: Mega Footer with Payment
- **footer-035**: Mega Footer with Map
- **footer-036**: Mega Footer with Awards
- **footer-037**: Mega Footer Corporate
- **footer-038**: Mega Footer E-commerce
- **footer-039**: Mega Footer SaaS
- **footer-040**: Mega Footer Agency
- **footer-041**: Wave Footer
- **footer-042**: Diagonal Footer
- **footer-043**: Gradient Footer
- **footer-044**: Image Background Footer
- **footer-045**: Video Background Footer
- **footer-046**: Animated Footer
- **footer-047**: Footer with Scroll Top
- **footer-048**: Footer with Chat
- **footer-049**: Footer with Stats
- **footer-050**: Footer with Testimonial

---

## 16. Authentication

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Login | Login forms |
| 011-020 | Register | Signup forms |
| 021-030 | Password | Password flows |
| 031-040 | Social | Social auth |
| 041-050 | Multi-Factor | 2FA/MFA |

### Template Details

#### auth-001 ~ auth-050
- **auth-001**: Simple Login
- **auth-002**: Login with Logo
- **auth-003**: Login Split Screen
- **auth-004**: Login Card
- **auth-005**: Login Full Page
- **auth-006**: Login with Image
- **auth-007**: Login Dark
- **auth-008**: Login Minimal
- **auth-009**: Login with Remember
- **auth-010**: Login with Captcha
- **auth-011**: Simple Register
- **auth-012**: Register with Logo
- **auth-013**: Register Split
- **auth-014**: Register Card
- **auth-015**: Register Multi-Step
- **auth-016**: Register with Terms
- **auth-017**: Register with Avatar
- **auth-018**: Register Detailed
- **auth-019**: Register with Progress
- **auth-020**: Register Invitation
- **auth-021**: Forgot Password
- **auth-022**: Reset Password
- **auth-023**: Change Password
- **auth-024**: Password Strength
- **auth-025**: Password Recovery
- **auth-026**: Password Sent
- **auth-027**: Password Success
- **auth-028**: Password Requirements
- **auth-029**: Password with Security
- **auth-030**: Password Link Expired
- **auth-031**: Social Login Buttons
- **auth-032**: Login with Google
- **auth-033**: Login with Apple
- **auth-034**: Login with Facebook
- **auth-035**: Login with Twitter/X
- **auth-036**: Login with GitHub
- **auth-037**: Multiple Social Options
- **auth-038**: Social + Email Login
- **auth-039**: Social Connect
- **auth-040**: Social Account Link
- **auth-041**: 2FA Setup
- **auth-042**: 2FA Verification
- **auth-043**: SMS Code Entry
- **auth-044**: Authenticator App
- **auth-045**: Backup Codes
- **auth-046**: Recovery Options
- **auth-047**: Security Questions
- **auth-048**: Email Verification
- **auth-049**: Phone Verification
- **auth-050**: Biometric Prompt

---

## 17. Dashboard

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Overview | Dashboard home |
| 011-020 | Stats | Statistics widgets |
| 021-030 | Charts | Data visualizations |
| 031-040 | Tables | Data tables |
| 041-050 | Layouts | Full layouts |

### Template Details

#### dash-001 ~ dash-050
- **dash-001**: Simple Dashboard
- **dash-002**: Dashboard with Stats
- **dash-003**: Dashboard with Chart
- **dash-004**: Dashboard with Table
- **dash-005**: Dashboard Minimal
- **dash-006**: Dashboard Dark
- **dash-007**: Dashboard with Sidebar
- **dash-008**: Dashboard with Cards
- **dash-009**: Dashboard with Activity
- **dash-010**: Dashboard Overview
- **dash-011**: Stats Card Simple
- **dash-012**: Stats Card with Icon
- **dash-013**: Stats Card with Chart
- **dash-014**: Stats Card with Trend
- **dash-015**: Stats Grid
- **dash-016**: Stats Row
- **dash-017**: Stats with Comparison
- **dash-018**: Stats Progress
- **dash-019**: Stats Animated
- **dash-020**: Stats Dark
- **dash-021**: Line Chart Widget
- **dash-022**: Bar Chart Widget
- **dash-023**: Pie Chart Widget
- **dash-024**: Area Chart Widget
- **dash-025**: Donut Chart Widget
- **dash-026**: Gauge Chart Widget
- **dash-027**: Sparkline Widget
- **dash-028**: Multiple Charts
- **dash-029**: Chart with Legend
- **dash-030**: Real-time Chart
- **dash-031**: Simple Data Table
- **dash-032**: Table with Search
- **dash-033**: Table with Filters
- **dash-034**: Table with Actions
- **dash-035**: Table Sortable
- **dash-036**: Table with Pagination
- **dash-037**: Table Expandable
- **dash-038**: Table with Selection
- **dash-039**: Table Responsive
- **dash-040**: Table Dark
- **dash-041**: Analytics Dashboard
- **dash-042**: Sales Dashboard
- **dash-043**: Project Dashboard
- **dash-044**: Finance Dashboard
- **dash-045**: User Dashboard
- **dash-046**: Admin Dashboard
- **dash-047**: CRM Dashboard
- **dash-048**: E-commerce Dashboard
- **dash-049**: Marketing Dashboard
- **dash-050**: Social Dashboard

---

## 18. E-commerce

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Product | Product displays |
| 011-020 | Cart | Shopping cart |
| 021-030 | Checkout | Checkout flows |
| 031-040 | Category | Product listing |
| 041-050 | Account | User account |

### Template Details

#### ecom-001 ~ ecom-050
- **ecom-001**: Product Card Basic
- **ecom-002**: Product Card with Rating
- **ecom-003**: Product Card with Badge
- **ecom-004**: Product Card Quick View
- **ecom-005**: Product Detail Simple
- **ecom-006**: Product Detail Gallery
- **ecom-007**: Product Detail Tabs
- **ecom-008**: Product Detail Full
- **ecom-009**: Product Comparison
- **ecom-010**: Product Reviews
- **ecom-011**: Mini Cart
- **ecom-012**: Cart Sidebar
- **ecom-013**: Cart Page
- **ecom-014**: Cart with Summary
- **ecom-015**: Cart Empty State
- **ecom-016**: Cart with Promo
- **ecom-017**: Cart Compact
- **ecom-018**: Cart with Suggestions
- **ecom-019**: Cart Save for Later
- **ecom-020**: Cart Multi-Seller
- **ecom-021**: Checkout Single Page
- **ecom-022**: Checkout Multi-Step
- **ecom-023**: Checkout with Summary
- **ecom-024**: Checkout Guest
- **ecom-025**: Express Checkout
- **ecom-026**: Checkout Payment
- **ecom-027**: Checkout Shipping
- **ecom-028**: Checkout Review
- **ecom-029**: Checkout Success
- **ecom-030**: Checkout Error
- **ecom-031**: Category Grid
- **ecom-032**: Category List
- **ecom-033**: Category with Filters
- **ecom-034**: Category with Sort
- **ecom-035**: Category with Sidebar
- **ecom-036**: Category Infinite Scroll
- **ecom-037**: Category with Pagination
- **ecom-038**: Category Banner
- **ecom-039**: Category Subcategories
- **ecom-040**: Category Empty
- **ecom-041**: Account Overview
- **ecom-042**: Order History
- **ecom-043**: Order Detail
- **ecom-044**: Address Book
- **ecom-045**: Payment Methods
- **ecom-046**: Wishlist
- **ecom-047**: Recently Viewed
- **ecom-048**: Account Settings
- **ecom-049**: Returns
- **ecom-050**: Loyalty/Points

---

## 19. Blog

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | Post | Single post layouts |
| 011-020 | List | Post listings |
| 021-030 | Sidebar | Sidebar widgets |
| 031-040 | Comments | Comment sections |
| 041-050 | Layout | Full layouts |

### Template Details

#### blog-001 ~ blog-050
- **blog-001**: Post Simple
- **blog-002**: Post with Hero
- **blog-003**: Post with Sidebar
- **blog-004**: Post Full Width
- **blog-005**: Post Magazine Style
- **blog-006**: Post with Author
- **blog-007**: Post with TOC
- **blog-008**: Post with Related
- **blog-009**: Post Dark
- **blog-010**: Post Minimal
- **blog-011**: Post List Basic
- **blog-012**: Post List with Thumbnails
- **blog-013**: Post Grid
- **blog-014**: Post Masonry
- **blog-015**: Post Featured + Grid
- **blog-016**: Post List with Sidebar
- **blog-017**: Post Timeline
- **blog-018**: Post Magazine Grid
- **blog-019**: Post Infinite Scroll
- **blog-020**: Post Filtered
- **blog-021**: Sidebar About
- **blog-022**: Sidebar Categories
- **blog-023**: Sidebar Tags
- **blog-024**: Sidebar Popular Posts
- **blog-025**: Sidebar Newsletter
- **blog-026**: Sidebar Social
- **blog-027**: Sidebar Search
- **blog-028**: Sidebar Archives
- **blog-029**: Sidebar Ads
- **blog-030**: Sidebar Combined
- **blog-031**: Comments Basic
- **blog-032**: Comments Threaded
- **blog-033**: Comments with Avatars
- **blog-034**: Comments with Reactions
- **blog-035**: Comments Form
- **blog-036**: Comments Pagination
- **blog-037**: Comments Real-time
- **blog-038**: Comments Moderation
- **blog-039**: Comments Social
- **blog-040**: Comments Collapsed
- **blog-041**: Blog Home Layout
- **blog-042**: Blog Category Page
- **blog-043**: Blog Author Page
- **blog-044**: Blog Search Results
- **blog-045**: Blog Archive
- **blog-046**: Blog Dark Theme
- **blog-047**: Blog Magazine
- **blog-048**: Blog Personal
- **blog-049**: Blog Corporate
- **blog-050**: Blog Multi-Author

---

## 20. Landing Pages

### Subcategories

| Range | Subcategory | Description |
|-------|-------------|-------------|
| 001-010 | SaaS | Software products |
| 011-020 | App | Mobile apps |
| 021-030 | Marketing | Campaign pages |
| 031-040 | Coming Soon | Launch pages |
| 041-050 | Industry | Specific verticals |

### Template Details

#### landing-001 ~ landing-050
- **landing-001**: SaaS Simple
- **landing-002**: SaaS with Demo
- **landing-003**: SaaS with Pricing
- **landing-004**: SaaS Dashboard Preview
- **landing-005**: SaaS Enterprise
- **landing-006**: SaaS Startup
- **landing-007**: SaaS API Product
- **landing-008**: SaaS Integration
- **landing-009**: SaaS Security Focus
- **landing-010**: SaaS AI Product
- **landing-011**: App Store Landing
- **landing-012**: App with Screenshots
- **landing-013**: App with Video
- **landing-014**: App with Reviews
- **landing-015**: App Feature Focus
- **landing-016**: App Game Style
- **landing-017**: App Fitness/Health
- **landing-018**: App Finance
- **landing-019**: App Social
- **landing-020**: App Productivity
- **landing-021**: Lead Generation
- **landing-022**: Webinar Registration
- **landing-023**: Ebook Download
- **landing-024**: Free Trial
- **landing-025**: Product Launch
- **landing-026**: Event Landing
- **landing-027**: Contest/Giveaway
- **landing-028**: Waitlist
- **landing-029**: Case Study
- **landing-030**: Black Friday/Sale
- **landing-031**: Coming Soon Simple
- **landing-032**: Coming Soon Countdown
- **landing-033**: Coming Soon with Email
- **landing-034**: Coming Soon Animated
- **landing-035**: Under Construction
- **landing-036**: Maintenance Mode
- **landing-037**: Beta Launch
- **landing-038**: Pre-Launch Teaser
- **landing-039**: Coming Soon Dark
- **landing-040**: Coming Soon Creative
- **landing-041**: Agency Landing
- **landing-042**: Restaurant Landing
- **landing-043**: Real Estate Landing
- **landing-044**: Education Landing
- **landing-045**: Healthcare Landing
- **landing-046**: Legal/Law Landing
- **landing-047**: Travel Landing
- **landing-048**: Fashion Landing
- **landing-049**: Cryptocurrency Landing
- **landing-050**: NFT/Web3 Landing

---

## Development Progress

### Overall Status

| Phase | Categories | Templates | Status |
|-------|------------|-----------|--------|
| Phase 1 | 01-05 | 250 | Not Started |
| Phase 2 | 06-10 | 250 | Not Started |
| Phase 3 | 11-15 | 250 | Not Started |
| Phase 4 | 16-20 | 250 | Not Started |
| **Total** | **20** | **1000** | **0%** |

### Category Progress

| # | Category | Done | Total | % |
|---|----------|------|-------|---|
| 01 | Navigation | 0 | 50 | 0% |
| 02 | Hero Sections | 0 | 50 | 0% |
| 03 | Features | 0 | 50 | 0% |
| 04 | Content Sections | 0 | 50 | 0% |
| 05 | CTA | 0 | 50 | 0% |
| 06 | Pricing | 0 | 50 | 0% |
| 07 | Testimonials | 0 | 50 | 0% |
| 08 | Team | 0 | 50 | 0% |
| 09 | Gallery | 0 | 50 | 0% |
| 10 | Forms | 0 | 50 | 0% |
| 11 | Cards | 0 | 50 | 0% |
| 12 | Lists | 0 | 50 | 0% |
| 13 | Modals | 0 | 50 | 0% |
| 14 | Notifications | 0 | 50 | 0% |
| 15 | Footers | 0 | 50 | 0% |
| 16 | Authentication | 0 | 50 | 0% |
| 17 | Dashboard | 0 | 50 | 0% |
| 18 | E-commerce | 0 | 50 | 0% |
| 19 | Blog | 0 | 50 | 0% |
| 20 | Landing Pages | 0 | 50 | 0% |

### Next Steps

1. [ ] Set up project structure and build system
2. [ ] Create base CSS with Tailwind v4 configuration
3. [ ] Implement i18n system
4. [ ] Build Web Components library
5. [ ] Start Phase 1: Navigation templates (nav-001 ~ nav-050)

---

## Appendix

### Template File Structure

Each template file follows this structure:

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Name | Category</title>
    <link href="../../src/css/main.css" rel="stylesheet">
</head>
<body>
    <!-- Template Content -->
    <section data-template="category-xxx">
        <!-- Semantic HTML with Tailwind utilities -->
        <!-- i18n attributes on text elements -->
    </section>

    <script src="../../src/js/i18n.js" type="module"></script>
</body>
</html>
```

### Common Tailwind Patterns

```css
/* Section Container */
.section-container {
    @apply py-16 sm:py-24 lg:py-32;
}

/* Content Container */
.content-container {
    @apply container mx-auto px-4 sm:px-6 lg:px-8;
}

/* Card Base */
.card-base {
    @apply bg-white rounded-xl shadow-lg p-6;
}

/* Button Primary */
.btn-primary {
    @apply px-6 py-3 bg-primary text-white rounded-lg
           hover:bg-primary/90 transition-colors;
}
```

---

*Document Version: 1.0.0*
*Last Updated: 2024-12-01*
