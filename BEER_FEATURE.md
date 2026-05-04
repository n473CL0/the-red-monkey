# Beer Feature Implementation

## What's New

### Beer Collection
- Created `_beers` collection with 6 sample beers
- Each beer has properties: name, style, brewery, ABV, IBU, color, color_hex, ingredients, description, and price
- Beer layout (`_layouts/beer.html`) displays detailed breakdown with 1/3 image, 2/3 stats

### Beers Page
- New `/beers/` page with 3-column grid layout (responsive: 2 columns on tablet, 1 on mobile)
- Each card shows beer image, name, style, and ABV
- Cards are clickable and link to individual beer pages

### Random Beer Integration
- All inner pages (posts, events, about) now display a random beer in the sidebar
- Beer image and description are clickable, linking to the beer's detail page
- Uses Jekyll's `sample` filter to randomly select a beer on each page load

### Navigation Updates

#### Desktop
- Added "Beers" tap before "Events" in the tap navigation
- Now shows: Beers, Events, Blog, About

#### Mobile (≤600px)
- Replaced multiple taps with single "Explore" tap
- Clicking the tap rotates it down (like desktop hover)
- Accordion menu appears below with all navigation links
- Menu slides between tap and footer

## Files Created
- `_beers/*.md` - 6 sample beer files
- `_layouts/beer.html` - Beer detail page layout
- `beers/index.html` - Beers listing page

## Files Modified
- `_config.yml` - Added beers collection
- `_layouts/default.html` - Added Beers tap and mobile navigation
- `_layouts/inner.html` - Random beer integration
- `_layouts/event.html` - Random beer integration
- `_layouts/post.html` - Random beer integration
- `_sass/base.scss` - Added styles for beers, beer cards, mobile nav
- `assets/css/main.scss` - Fixed import syntax

## Testing
Run `bundle exec jekyll serve` and visit:
- `/beers/` - View all beers in grid
- `/beers/hopsworth-pale-ale/` - View individual beer
- Any post/event page - See random beer in sidebar
- Mobile view - Test accordion navigation
